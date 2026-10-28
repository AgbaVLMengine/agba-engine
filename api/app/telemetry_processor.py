# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: TELEMETRY PROCESSING & HITL COORDINATOR (v6.2.0)
# ==============================================================================
# Lead Architect & Creator: Àrùnà Ọlànrewájú Kábírù
# Lean MLOps Streaming Coordinator (< 200 LOC):
#   1. Delegates candidate extraction & diagnosis to hitl_diagnostics.py
#   2. Delegates HITL card & report generation to hitl_card_generator.py
#   3. Manages candidate approval/rejection state and atomic corpus commits
# ==============================================================================

import sys
import json
import time
import shutil
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

if str(Path(__file__).resolve().parent.parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.config import ÀgbàConfig, AgbaConfig
from app.hitl_diagnostics import (
    normalize_nfc,
    strip_accents,
    load_jsonl_records,
    diagnose_candidate,
    extract_actionable_candidates as _extract_candidates,
)
from app.hitl_card_generator import (
    generate_hitl_report as _render_hitl_report,
    print_flywheel_status,
)


class TelemetryProcessor:
    """MLOps Feedback Ingestion and Human-in-the-Loop Review Coordinator."""

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
        if not self.corpus_path.exists():
            raise FileNotFoundError(f"Master corpus not found at {self.corpus_path}")
        self.corpus = json.loads(self.corpus_path.read_text(encoding="utf-8"))
        self.corpus_by_id = {e["id"]: e for e in self.corpus}
        self.corpus_by_folded = {strip_accents(e["id"]): e for e in self.corpus}
        print(f"📖 Loaded {len(self.corpus)} master entities for telemetry evaluation.")

    def load_telemetry_records(self) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
        return load_jsonl_records(self.feedback_path, self.query_log_path)

    def _diagnose_candidate(self, candidate: Dict[str, Any]) -> Dict[str, Any]:
        return diagnose_candidate(candidate, self.corpus_by_id, self.corpus_by_folded)

    def extract_actionable_candidates(self) -> List[Dict[str, Any]]:
        feedbacks, queries_by_id = self.load_telemetry_records()
        return _extract_candidates(
            feedbacks, queries_by_id, self.pending_json_path, self.corpus_by_id, self.corpus_by_folded
        )

    def generate_hitl_report(self) -> Tuple[Path, Path]:
        candidates = self.extract_actionable_candidates()
        return _render_hitl_report(candidates, len(self.corpus), self.pending_json_path, self.pending_md_path)

    def _update_feedback_status(self, query_ids: set, new_status: str) -> None:
        if not query_ids or not self.feedback_path.exists():
            return
        lines = []
        for line in self.feedback_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    rec = json.loads(line)
                    if rec.get("query_id") in query_ids:
                        rec["status"] = new_status
                    lines.append(json.dumps(rec, ensure_ascii=False))
                except Exception:
                    lines.append(line.strip())
        self.feedback_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

    def approve_candidate(self, candidate_id: str) -> bool:
        if not self.pending_json_path.exists():
            self.generate_hitl_report()
        candidates = json.loads(self.pending_json_path.read_text(encoding="utf-8"))
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c["status"] = "APPROVED"
                self.pending_json_path.write_text(json.dumps(candidates, indent=2, ensure_ascii=False), encoding="utf-8")
                print(f"✅ Candidate '{candidate_id}' marked as APPROVED.")
                self.generate_hitl_report()
                return True
        print(f"❌ Candidate '{candidate_id}' not found in pending queue.")
        return False

    def reject_candidate(self, candidate_id: str, reason: str = "Disapproved by Lead Architect") -> bool:
        if not self.pending_json_path.exists():
            self.generate_hitl_report()
        candidates = json.loads(self.pending_json_path.read_text(encoding="utf-8"))
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c["status"] = "DISMISSED"
                c["dismissal_reason"] = reason
                self.pending_json_path.write_text(json.dumps(candidates, indent=2, ensure_ascii=False), encoding="utf-8")
                if c.get("query_id"):
                    self._update_feedback_status({c["query_id"]}, "DISMISSED")
                print(f"🚫 Candidate '{candidate_id}' marked as DISMISSED ({reason}).")
                self.generate_hitl_report()
                return True
        print(f"❌ Candidate '{candidate_id}' not found in pending queue.")
        return False

    def apply_approved_candidates(self) -> int:
        if not self.pending_json_path.exists():
            print("⚠️ No pending_candidates.json found. Run review generation first.")
            return 0
        candidates = json.loads(self.pending_json_path.read_text(encoding="utf-8"))
        approved = [c for c in candidates if c.get("status") == "APPROVED"]
        if not approved:
            print("ℹ️ No candidates currently marked 'APPROVED' in pending_candidates.json.")
            return 0

        backup_dir = self.root_dir / "agba_engine_backups" / "corpus_backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(self.corpus_path, backup_dir / f"yoruba_corpus_1007_backup_{int(time.time())}.json")

        committed_count, audit_records = 0, []
        for c in approved:
            patch = c.get("proposed_patch", {})
            eid, alias = patch.get("entity_id"), patch.get("add_alias")
            if eid and alias and eid in self.corpus_by_id:
                aliases = self.corpus_by_id[eid].setdefault("aliases", [])
                if alias not in aliases:
                    aliases.append(alias)
                committed_count += 1
                c["status"] = "COMMITTED"
                audit_records.append({
                    "timestamp": time.time(),
                    "candidate_id": c.get("candidate_id"),
                    "action": "ADDED_ALIAS",
                    "entity_id": eid,
                    "alias": alias,
                    "approved_by": "Aruna Olanrewaju Kabiru",
                })

        if committed_count > 0:
            self.corpus_path.write_text(json.dumps(self.corpus, indent=2, ensure_ascii=False), encoding="utf-8")
            for sync_p in [
                self.root_dir / "Agba_Engine_Foundational_Vault" / "02_Master_Corpus_&_Taxonomy" / "yoruba_corpus_1007_NORMALIZED.json",
                self.root_dir / "agba_enterprise_api" / "data" / "yoruba_corpus_1007_NORMALIZED.json",
            ]:
                if sync_p.exists() and sync_p.resolve() != self.corpus_path.resolve():
                    shutil.copyfile(self.corpus_path, sync_p)
            self.audit_log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.audit_log_path, "a", encoding="utf-8") as f:
                for a in audit_records:
                    f.write(json.dumps(a, ensure_ascii=False) + "\n")
            self._update_feedback_status({c.get("query_id") for c in approved if c.get("status") == "COMMITTED"}, "COMMITTED")
            self.pending_json_path.write_text(json.dumps(candidates, indent=2, ensure_ascii=False), encoding="utf-8")

        return committed_count

    def print_status(self) -> None:
        feedbacks, queries_by_id = self.load_telemetry_records()
        print_flywheel_status(feedbacks, queries_by_id, self.pending_json_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Àgbà Engine MLOps Telemetry & HITL Review Engine")
    parser.add_argument("--status", action="store_true", help="Display flywheel telemetry metrics")
    parser.add_argument("--generate", action="store_true", help="Generate pending HITL review ledger")
    parser.add_argument("--approve", type=str, metavar="CANDIDATE_ID", help="Approve candidate by ID")
    parser.add_argument("--reject", type=str, metavar="CANDIDATE_ID", help="Dismiss candidate by ID")
    parser.add_argument("--reason", type=str, default="Disapproved by Lead Architect", help="Reason for rejection")
    parser.add_argument("--apply", action="store_true", help="Commit all APPROVED candidates to Master Corpus")
    args = parser.parse_args()
    proc = TelemetryProcessor()
    if args.status:
        proc.print_status()
    elif args.approve:
        proc.approve_candidate(args.approve)
    elif args.reject:
        proc.reject_candidate(args.reject, args.reason)
    elif args.apply:
        proc.apply_approved_candidates()
    else:
        proc.generate_hitl_report()
