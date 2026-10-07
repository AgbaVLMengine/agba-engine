# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: TELEMETRY PROCESSING & HITL REVIEW ENGINE (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Continuous MLOps Flywheel:
#   1. Ingests query telemetry & user feedback from feedback_store.jsonl
#   2. Analyzes queries, drift, and user corrections (Diacritics, Aliases, Entities)
#   3. Generates Human-in-the-Loop (HITL) review cards (pending_candidates.md/.json)
#   4. Safely commits Lead-Architect-approved updates with automated backups
#   5. Synchronizes Master Corpus across Vault, Workspace, and Container bundles
# ==============================================================================

import os
import sys
import json
import time
import shutil
import argparse
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

try:
    from app.config import ÀgbàConfig, AgbaConfig
except ImportError:
    # Standalone execution support
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from app.config import ÀgbàConfig, AgbaConfig


def normalize_nfc(text: str) -> str:
    """Normalize string using Unicode NFC."""
    return unicodedata.normalize("NFC", text.strip()) if text else ""


def strip_accents(text: str) -> str:
    """Strip accents for ASCII-folded matching."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


class TelemetryProcessor:
    """
    MLOps Feedback Ingestion and Human-in-the-Loop Review Engine.
    Ensures zero unverified data enters the sacred Master Corpus.
    """

    def __init__(self, root_dir: Optional[Path] = None):
        self.root_dir = Path(root_dir) if root_dir else ÀgbàConfig.ROOT_DIR
        self.feedback_path = ÀgbàConfig.get_feedback_store_path()
        self.query_log_path = ÀgbàConfig.get_query_store_path()
        self.audit_log_path = self.root_dir / "agba_enterprise_api" / "telemetry_audit_history.jsonl"
        self.pending_json_path = ÀgbàConfig.get_pending_candidates_path()
        self.pending_md_path = self.root_dir / "agba_enterprise_api" / "pending_self_learning_candidates.md"

        self.corpus_path = ÀgbàConfig.get_normalized_corpus_path()
        self.corpus: List[Dict[str, Any]] = []
        self.corpus_by_id: Dict[str, Dict[str, Any]] = {}
        self.corpus_by_folded: Dict[str, Dict[str, Any]] = {}

        self._load_corpus()

    def _load_corpus(self) -> None:
        """Load and index master corpus in memory."""
        if not self.corpus_path.exists():
            raise FileNotFoundError(f"Master corpus not found at {self.corpus_path}")

        with open(self.corpus_path, "r", encoding="utf-8") as f:
            self.corpus = json.load(f)

        self.corpus_by_id = {entity["id"]: entity for entity in self.corpus}
        self.corpus_by_folded = {strip_accents(entity["id"]): entity for entity in self.corpus}
        print(f"📖 Loaded {len(self.corpus)} master entities for telemetry evaluation.")

    def load_telemetry_records(self) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
        """Load feedback store and associated query telemetry logs."""
        feedbacks = []
        queries_by_id = {}

        # 1. Load Query Logs
        if self.query_log_path.exists():
            with open(self.query_log_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            record = json.loads(line)
                            qid = record.get("query_id")
                            if qid:
                                queries_by_id[qid] = record
                        except Exception:
                            pass

        # 2. Load Feedback Store
        if self.feedback_path.exists():
            with open(self.feedback_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            feedbacks.append(json.loads(line))
                        except Exception:
                            pass

        return feedbacks, queries_by_id

    def extract_actionable_candidates(self) -> List[Dict[str, Any]]:
        """
        Identify feedback records requiring cultural diagnosis and HITL review:
        - Negative ratings ('thumbs_down')
        - Explicit user corrections or suggestions
        - Tags: diacritic_error, missing_alias, missing_entity, domain_mismatch
        """
        feedbacks, queries_by_id = self.load_telemetry_records()
        actionable = []

        existing_status_map = {}
        if self.pending_json_path.exists():
            try:
                with open(self.pending_json_path, "r", encoding="utf-8") as f:
                    for ec in json.load(f):
                        cid = ec.get("candidate_id")
                        if cid:
                            existing_status_map[cid] = ec
            except Exception:
                pass

        for fb in feedbacks:
            # Skip already approved/dismissed records
            if fb.get("status") in ["COMMITTED", "DISMISSED"]:
                continue

            rating = fb.get("rating")
            correction = fb.get("user_correction")
            tags = fb.get("tags", [])
            query_id = fb.get("query_id")

            # Check if this feedback contains an actionable signal
            is_negative = rating == "thumbs_down"
            has_correction = bool(correction and correction.strip())
            has_special_tag = any(t in tags for t in ["diacritic_error", "missing_alias", "missing_entity", "domain_mismatch"])

            if is_negative or has_correction or has_special_tag:
                # Merge query metadata if available
                q_meta = queries_by_id.get(query_id, {})
                queried_concept = fb.get("queried_concept") or q_meta.get("queried_concept") or "Unknown Concept"
                returned_entity_id = fb.get("returned_entity_id") or q_meta.get("top_entity_id")

                cid = f"cand_{query_id}"
                status_val = "PENDING_REVIEW"
                if cid in existing_status_map:
                    status_val = existing_status_map[cid].get("status", "PENDING_REVIEW")

                candidate = {
                    "candidate_id": cid,
                    "query_id": query_id,
                    "timestamp": fb.get("timestamp", time.time()),
                    "client_tier": fb.get("client_tier", "Unknown"),
                    "rating": rating,
                    "queried_concept": queried_concept,
                    "returned_entity_id": returned_entity_id,
                    "user_correction": correction,
                    "tags": tags,
                    "status": status_val
                }

                # Run cultural analysis on the candidate
                analysis = self._diagnose_candidate(candidate)
                candidate.update(analysis)
                actionable.append(candidate)

        return actionable

    def _diagnose_candidate(self, candidate: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform deterministic cultural diagnosis and propose action:
        - DIACRITIC_ERROR
        - NEW_ALIAS_PROPOSAL
        - CONTEXT_ENRICHMENT
        - NEW_ENTITY_PROPOSAL
        """
        concept = candidate.get("queried_concept", "")
        correction = candidate.get("user_correction", "")
        returned_id = candidate.get("returned_entity_id")
        tags = candidate.get("tags", [])

        # Check matched entity in corpus
        matched_entity = self.corpus_by_id.get(returned_id) if returned_id else None
        if not matched_entity:
            # Fallback to folded match
            matched_entity = self.corpus_by_folded.get(strip_accents(concept))

        # 1. Diacritic Issue Diagnosis
        if "diacritic_error" in tags or (matched_entity and strip_accents(concept) == strip_accents(matched_entity.get("id", "")) and concept != matched_entity.get("id")):
            return {
                "diagnosis_type": "DIACRITIC_ERROR",
                "target_entity_id": matched_entity.get("id") if matched_entity else None,
                "proposed_action": "VERIFY_CANONICAL_DIACRITICS",
                "recommendation": f"Add ASCII folded query '{concept}' as search alias to canonical '{matched_entity.get('id')}' if not already present.",
                "proposed_patch": {
                    "entity_id": matched_entity.get("id") if matched_entity else None,
                    "add_alias": concept if concept != matched_entity.get("id") else None
                },
                "confidence_score": 0.95
            }

        # 2. Alias Suggestion
        if matched_entity and correction:
            return {
                "diagnosis_type": "NEW_ALIAS_PROPOSAL",
                "target_entity_id": matched_entity.get("id"),
                "proposed_action": "ADD_CULTURAL_ALIAS",
                "recommendation": f"User proposed alternative name or diaspora term for '{matched_entity.get('id')}': '{correction}'.",
                "proposed_patch": {
                    "entity_id": matched_entity.get("id"),
                    "add_alias": correction.strip()
                },
                "confidence_score": 0.88
            }

        # 3. Missing / New Entity
        if not matched_entity:
            return {
                "diagnosis_type": "NEW_ENTITY_CANDIDATE",
                "target_entity_id": None,
                "proposed_action": "STAGE_FOR_14_TIER_ENRICHMENT",
                "recommendation": f"Queried concept '{concept}' does not exist in master corpus. Stage for full 14-tier scholarly creation.",
                "proposed_patch": {
                    "new_concept_title": concept,
                    "user_notes": correction
                },
                "confidence_score": 0.75
            }

        # Default: General review
        return {
            "diagnosis_type": "GENERAL_FEEDBACK",
            "target_entity_id": matched_entity.get("id") if matched_entity else None,
            "proposed_action": "MANUAL_REVIEW",
            "recommendation": "Review feedback notes against cultural context.",
            "proposed_patch": {},
            "confidence_score": 0.60
        }

    def generate_hitl_report(self) -> Tuple[Path, Path]:
        """
        Generate Human-in-the-Loop review artifacts:
        1. pending_self_learning_candidates.md (Interactive Markdown review ledger)
        2. pending_candidates.json (State storage for programmatic approval)
        """
        candidates = self.extract_actionable_candidates()

        # 1. Write JSON state
        self.pending_json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.pending_json_path, "w", encoding="utf-8") as f:
            json.dump(candidates, f, indent=2, ensure_ascii=False)

        # 2. Build Markdown Report
        md_lines = [
            "# 🛡️ ÀGBÀ ENGINE: HUMAN-IN-THE-LOOP (HITL) SELF-LEARNING REVIEW QUEUE",
            "## Telemetry Feedback & Active Learning Staging Ledger",
            "",
            f"**Lead Architect & Reviewer:** Aruna Olanrewaju Kabiru  ",
            f"**Generated At:** {time.strftime('%Y-%m-%d %H:%M:%S')}  ",
            f"**Total Pending Actionable Candidates:** `{len(candidates)}`  ",
            f"**Master Corpus Baseline:** `{len(self.corpus)}` entities (`yoruba_corpus_1007_NORMALIZED.json`)  ",
            "",
            "> [!IMPORTANT]",
            "> **Cultural Integrity Invariant:** No autonomous model drift is permitted to modify the master corpus directly.",
            "> Every candidate generated from user feedback must be reviewed and approved by the Lead Architect.",
            "",
            "---",
            "",
            "### 📊 Review Status Summary",
            "",
            "| Metric | Count |",
            "| :--- | :--- |",
            f"| Total Actionable Telemetry Items | **{len(candidates)}** |",
            f"| Diacritic Adjustments | **{sum(1 for c in candidates if c.get('diagnosis_type') == 'DIACRITIC_ERROR')}** |",
            f"| New Cultural Alias Proposals | **{sum(1 for c in candidates if c.get('diagnosis_type') == 'NEW_ALIAS_PROPOSAL')}** |",
            f"| New Entity Candidates | **{sum(1 for c in candidates if c.get('diagnosis_type') == 'NEW_ENTITY_CANDIDATE')}** |",
            f"| General Cultural Feedback | **{sum(1 for c in candidates if c.get('diagnosis_type') == 'GENERAL_FEEDBACK')}** |",
            "",
            "---",
            "",
            "### 🔍 Actionable Review Queue",
            ""
        ]

        if not candidates:
            md_lines.append("✨ *No pending feedback items require action at this time. All telemetry is verified.*")
        else:
            for idx, c in enumerate(candidates, start=1):
                status_icon = "⏳" if c.get("status") == "PENDING_REVIEW" else ("✅" if c.get("status") == "APPROVED" else "❌")
                md_lines.extend([
                    f"#### Candidate #{idx}: `{c.get('candidate_id')}` [{c.get('diagnosis_type')}] {status_icon}",
                    f"- **Queried Concept:** `{c.get('queried_concept')}`",
                    f"- **Returned Entity:** `{c.get('returned_entity_id') or 'None'}`",
                    f"- **User Rating:** `{c.get('rating')}` | **Client Tier:** `{c.get('client_tier')}`",
                    f"- **User Correction/Note:** *{c.get('user_correction') or 'No text note provided'}*",
                    f"- **Categorical Tags:** `{', '.join(c.get('tags', []))}`",
                    f"- **Proposed Action:** `{c.get('proposed_action')}` (Confidence: `{c.get('confidence_score') * 100:.0f}%`)",
                    f"- **Curatorial Recommendation:** {c.get('recommendation')}",
                    "",
                    "```json",
                    json.dumps(c.get("proposed_patch", {}), indent=2, ensure_ascii=False),
                    "```",
                    "",
                    f"- Current Status: `{c.get('status')}`",
                    f"- Approval Command: `python3 -m agba_enterprise_api.app.telemetry_processor --approve {c.get('candidate_id')}`",
                    f"- Dismiss Command: `python3 -m agba_enterprise_api.app.telemetry_processor --reject {c.get('candidate_id')}`",
                    "",
                    "---",
                    ""
                ])

        md_content = chr(10).join(md_lines)
        with open(self.pending_md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✅ Generated HITL review state: {self.pending_json_path}")
        print(f"📄 Generated HITL Markdown report: {self.pending_md_path}")
        return self.pending_md_path, self.pending_json_path

    def approve_candidate(self, candidate_id: str) -> bool:
        """Mark a candidate as APPROVED in pending_candidates.json."""
        if not self.pending_json_path.exists():
            self.generate_hitl_report()

        with open(self.pending_json_path, "r", encoding="utf-8") as f:
            candidates = json.load(f)

        found = False
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c["status"] = "APPROVED"
                found = True
                print(f"✅ Candidate '{candidate_id}' marked as APPROVED.")
                break

        if found:
            with open(self.pending_json_path, "w", encoding="utf-8") as f:
                json.dump(candidates, f, indent=2, ensure_ascii=False)
            self.generate_hitl_report()
            return True
        else:
            print(f"❌ Candidate '{candidate_id}' not found in pending queue.")
            return False

    def reject_candidate(self, candidate_id: str, reason: str = "Disapproved by Lead Architect") -> bool:
        """Mark a candidate as DISMISSED in pending_candidates.json and update feedback store."""
        if not self.pending_json_path.exists():
            self.generate_hitl_report()

        with open(self.pending_json_path, "r", encoding="utf-8") as f:
            candidates = json.load(f)

        found = False
        target_query_id = None
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c["status"] = "DISMISSED"
                c["dismissal_reason"] = reason
                target_query_id = c.get("query_id")
                found = True
                print(f"🚫 Candidate '{candidate_id}' marked as DISMISSED ({reason}).")
                break

        if found:
            with open(self.pending_json_path, "w", encoding="utf-8") as f:
                json.dump(candidates, f, indent=2, ensure_ascii=False)

            # Update status in feedback store
            if target_query_id and self.feedback_path.exists():
                lines = []
                with open(self.feedback_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            try:
                                rec = json.loads(line)
                                if rec.get("query_id") == target_query_id:
                                    rec["status"] = "DISMISSED"
                                lines.append(json.dumps(rec, ensure_ascii=False))
                            except Exception:
                                lines.append(line.strip())
                with open(self.feedback_path, "w", encoding="utf-8") as f:
                    for l in lines:
                        f.write(l + chr(10))

            self.generate_hitl_report()
            return True
        else:
            print(f"❌ Candidate '{candidate_id}' not found in pending queue.")
            return False

    def apply_approved_candidates(self) -> int:
        """
        Commit candidates marked as APPROVED in pending_candidates.json:
        1. Creates timestamped backup of master corpus.
        2. Applies alias additions or entity patches.
        3. Synchronizes to Foundational Vault and bundled data/.
        4. Logs to telemetry audit ledger.
        """
        if not self.pending_json_path.exists():
            print("⚠️ No pending_candidates.json found. Run review generation first.")
            return 0

        with open(self.pending_json_path, "r", encoding="utf-8") as f:
            candidates = json.load(f)

        approved = [c for c in candidates if c.get("status") == "APPROVED"]
        if not approved:
            print("ℹ️ No candidates currently marked 'APPROVED' in pending_candidates.json.")
            print("   To approve a candidate, run: python3 -m agba_enterprise_api.app.telemetry_processor --approve <candidate_id>")
            return 0

        print(f"🚀 Committing {len(approved)} approved candidate(s) to Master Corpus...")

        # 1. Create Timestamped Backup
        backup_dir = self.root_dir / "agba_engine_backups" / "corpus_backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_file = backup_dir / f"yoruba_corpus_1007_backup_{int(time.time())}.json"
        shutil.copyfile(self.corpus_path, backup_file)
        print(f"🛡️ Safety Backup created: {backup_file}")

        # 2. Apply Patches
        committed_count = 0
        audit_records = []

        for c in approved:
            patch = c.get("proposed_patch", {})
            entity_id = patch.get("entity_id")
            add_alias = patch.get("add_alias")

            if entity_id and add_alias and entity_id in self.corpus_by_id:
                entity = self.corpus_by_id[entity_id]
                if "aliases" not in entity:
                    entity["aliases"] = []
                if add_alias not in entity["aliases"]:
                    entity["aliases"].append(add_alias)
                    committed_count += 1
                    print(f"   ✨ Added alias '{add_alias}' to canonical entity '{entity_id}'")
                else:
                    committed_count += 1
                    print(f"   ✨ Alias '{add_alias}' already present on '{entity_id}' (fulfilled)")

                c["status"] = "COMMITTED"
                audit_records.append({
                    "timestamp": time.time(),
                    "candidate_id": c.get("candidate_id"),
                    "action": "ADDED_ALIAS",
                    "entity_id": entity_id,
                    "alias": add_alias,
                    "approved_by": "Aruna Olanrewaju Kabiru"
                })

        if committed_count > 0:
            # 3. Save to active location
            with open(self.corpus_path, "w", encoding="utf-8") as f:
                json.dump(self.corpus, f, indent=2, ensure_ascii=False)
            print(f"💾 Updated active master corpus: {self.corpus_path}")

            # 4. Synchronize to Foundational Vault
            vault_corpus = self.root_dir / "Agba_Engine_Foundational_Vault" / "02_Master_Corpus_&_Taxonomy" / "yoruba_corpus_1007_NORMALIZED.json"
            if vault_corpus.exists() and vault_corpus.resolve() != self.corpus_path.resolve():
                shutil.copyfile(self.corpus_path, vault_corpus)
                print(f"🏛️ Synchronized to Foundational Vault: {vault_corpus}")

            # 5. Synchronize to Bundled data/ Directory (Cloud Run parity)
            bundled_corpus = self.root_dir / "agba_enterprise_api" / "data" / "yoruba_corpus_1007_NORMALIZED.json"
            if bundled_corpus.exists() and bundled_corpus.resolve() != self.corpus_path.resolve():
                shutil.copyfile(self.corpus_path, bundled_corpus)
                print(f"📦 Synchronized to Bundled data/: {bundled_corpus}")

            # 6. Append to Audit History
            with open(self.audit_log_path, "a", encoding="utf-8") as f:
                for a in audit_records:
                    f.write(json.dumps(a, ensure_ascii=False) + chr(10))
            print(f"📜 Audit log appended: {self.audit_log_path}")

            # 7. Update feedback_store.jsonl records to COMMITTED
            committed_query_ids = {c.get("query_id") for c in approved if c.get("status") == "COMMITTED"}
            if self.feedback_path.exists():
                updated_lines = []
                with open(self.feedback_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                fb_rec = json.loads(line)
                                if fb_rec.get("query_id") in committed_query_ids:
                                    fb_rec["status"] = "COMMITTED"
                                updated_lines.append(json.dumps(fb_rec, ensure_ascii=False))
                            except Exception:
                                updated_lines.append(line)
                with open(self.feedback_path, "w", encoding="utf-8") as f:
                    for u in updated_lines:
                        f.write(u + chr(10))
                print(f"📝 Updated status to COMMITTED in {self.feedback_path}")

            # 8. Save updated pending status
            with open(self.pending_json_path, "w", encoding="utf-8") as f:
                json.dump(candidates, f, indent=2, ensure_ascii=False)

        return committed_count

    def print_status(self) -> None:
        """Display operational summary of telemetry flywheel."""
        feedbacks, queries_by_id = self.load_telemetry_records()
        print("=" * 80)
        print("🏛️ ÀGBÀ ENGINE: MLOPS TELEMETRY FLYWHEEL STATUS")
        print("   Lead Architect & Reviewer: Aruna Olanrewaju Kabiru")
        print("=" * 80)
        print(f"📊 Total Queries Logged       : {len(queries_by_id)}")
        print(f"📝 Total Feedback Records     : {len(feedbacks)}")
        thumbs_up = sum(1 for fb in feedbacks if fb.get("rating") == "thumbs_up")
        thumbs_down = sum(1 for fb in feedbacks if fb.get("rating") == "thumbs_down")
        print(f"👍 Thumbs Up Ratings          : {thumbs_up}")
        print(f"👎 Thumbs Down Ratings        : {thumbs_down}")

        pending = []
        if self.pending_json_path.exists():
            with open(self.pending_json_path, "r", encoding="utf-8") as f:
                pending = json.load(f)

        pending_rev = sum(1 for p in pending if p.get("status") == "PENDING_REVIEW")
        approved_rev = sum(1 for p in pending if p.get("status") == "APPROVED")
        committed_rev = sum(1 for p in pending if p.get("status") == "COMMITTED")
        dismissed_rev = sum(1 for p in pending if p.get("status") == "DISMISSED")

        print(f"⏳ Pending HITL Reviews       : {pending_rev}")
        print(f"✅ Approved (Awaiting Commit) : {approved_rev}")
        print(f"✨ Committed to Master Corpus : {committed_rev}")
        print(f"🚫 Dismissed / Quarantined    : {dismissed_rev}")
        print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Àgbà Engine MLOps Telemetry & HITL Review Engine")
    parser.add_argument("--status", action="store_true", help="Display flywheel telemetry metrics")
    parser.add_argument("--generate", action="store_true", help="Generate pending HITL review ledger")
    parser.add_argument("--approve", type=str, metavar="CANDIDATE_ID", help="Approve candidate by ID")
    parser.add_argument("--reject", type=str, metavar="CANDIDATE_ID", help="Dismiss candidate by ID")
    parser.add_argument("--reason", type=str, default="Disapproved by Lead Architect", help="Reason for rejection")
    parser.add_argument("--apply", action="store_true", help="Commit all APPROVED candidates to Master Corpus")

    args = parser.parse_args()
    processor = TelemetryProcessor()

    if args.status:
        processor.print_status()
    elif args.approve:
        processor.approve_candidate(args.approve)
    elif args.reject:
        processor.reject_candidate(args.reject, args.reason)
    elif args.apply:
        processor.apply_approved_candidates()
    else:
        processor.generate_hitl_report()
