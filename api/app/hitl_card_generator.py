# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: HITL REVIEW CARD & LEDGER GENERATOR (v6.2.0)
# ==============================================================================
# Lead Architect & Creator: Àrùnà Ọlànrewájú Kábírù
# Formats Human-in-the-Loop (HITL) Markdown review cards, JSON candidate state,
# and CLI operational status summaries for the MLOps telemetry flywheel.
# ==============================================================================

import json
import time
from pathlib import Path
from typing import Dict, Any, List, Tuple


def format_hitl_markdown_card(idx: int, c: Dict[str, Any]) -> List[str]:
    """Render a single HITL candidate into Markdown review lines."""
    status = c.get("status")
    icon = "⏳" if status == "PENDING_REVIEW" else ("✅" if status in ["APPROVED", "COMMITTED"] else "❌")
    cid = c.get("candidate_id")
    conf = (c.get("confidence_score") or 0.0) * 100
    return [
        f"#### Candidate #{idx}: `{cid}` [{c.get('diagnosis_type')}] {icon}",
        f"- **Queried Concept:** `{c.get('queried_concept')}`",
        f"- **Returned Entity:** `{c.get('returned_entity_id') or 'None'}`",
        f"- **User Rating:** `{c.get('rating')}` | **Client Tier:** `{c.get('client_tier')}`",
        f"- **User Correction/Note:** *{c.get('user_correction') or 'No text note provided'}*",
        f"- **Categorical Tags:** `{', '.join(c.get('tags', []))}`",
        f"- **Proposed Action:** `{c.get('proposed_action')}` (Confidence: `{conf:.0f}%`)",
        f"- **Curatorial Recommendation:** {c.get('recommendation')}",
        "",
        "```json",
        json.dumps(c.get("proposed_patch", {}), indent=2, ensure_ascii=False),
        "```",
        "",
        f"- Current Status: `{status}`",
        f"- Approval Command: `python3 -m agba_enterprise_api.app.telemetry_processor --approve {cid}`",
        f"- Dismiss Command: `python3 -m agba_enterprise_api.app.telemetry_processor --reject {cid}`",
        "",
        "---",
        "",
    ]


def generate_hitl_report(
    candidates: List[Dict[str, Any]],
    corpus_count: int,
    pending_json_path: Path,
    pending_md_path: Path,
) -> Tuple[Path, Path]:
    """Write pending_candidates.json state and pending_self_learning_candidates.md report."""
    pending_json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pending_json_path, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2, ensure_ascii=False)

    md_lines = [
        "# 🛡️ ÀGBÀ ENGINE: HUMAN-IN-THE-LOOP (HITL) SELF-LEARNING REVIEW QUEUE",
        "## Telemetry Feedback & Active Learning Staging Ledger",
        "",
        "**Lead Architect & Reviewer:** Aruna Olanrewaju Kabiru  ",
        f"**Generated At:** {time.strftime('%Y-%m-%d %H:%M:%S')}  ",
        f"**Total Pending Actionable Candidates:** `{len(candidates)}`  ",
        f"**Master Corpus Baseline:** `{corpus_count}` entities (`yoruba_corpus_1007_NORMALIZED.json`)  ",
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
        "",
    ]

    if not candidates:
        md_lines.append("✨ *No pending feedback items require action at this time. All telemetry is verified.*")
    else:
        for idx, c in enumerate(candidates, start=1):
            md_lines.extend(format_hitl_markdown_card(idx, c))

    md_content = "\n".join(md_lines)
    pending_md_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pending_md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    mirror_path = Path("/home/aruna_olanrewaju/agba-engine/api/pending_self_learning_candidates.md")
    try:
        mirror_path.parent.mkdir(parents=True, exist_ok=True)
        with open(mirror_path, "w", encoding="utf-8") as ef:
            ef.write(md_content)
    except Exception:
        pass

    print(f"✅ Generated HITL review state: {pending_json_path}")
    print(f"📄 Generated HITL Markdown report: {pending_md_path}")
    return pending_md_path, pending_json_path


def print_flywheel_status(
    feedbacks: List[Dict[str, Any]],
    queries_by_id: Dict[str, Dict[str, Any]],
    pending_json_path: Path,
) -> None:
    """Display operational summary of telemetry flywheel."""
    pending = json.loads(pending_json_path.read_text(encoding="utf-8")) if pending_json_path.exists() else []
    print("=" * 80)
    print("🏛️ ÀGBÀ ENGINE: MLOPS TELEMETRY FLYWHEEL STATUS")
    print("   Lead Architect & Reviewer: Aruna Olanrewaju Kabiru")
    print("=" * 80)
    print(f"📊 Total Queries Logged       : {len(queries_by_id)}")
    print(f"📝 Total Feedback Records     : {len(feedbacks)}")
    print(f"👍 Thumbs Up Ratings          : {sum(1 for fb in feedbacks if fb.get('rating') == 'thumbs_up')}")
    print(f"👎 Thumbs Down Ratings        : {sum(1 for fb in feedbacks if fb.get('rating') == 'thumbs_down')}")
    print(f"⏳ Pending HITL Reviews       : {sum(1 for p in pending if p.get('status') == 'PENDING_REVIEW')}")
    print(f"✅ Approved (Awaiting Commit) : {sum(1 for p in pending if p.get('status') == 'APPROVED')}")
    print(f"✨ Committed to Master Corpus : {sum(1 for p in pending if p.get('status') == 'COMMITTED')}")
    print(f"🚫 Dismissed / Quarantined    : {sum(1 for p in pending if p.get('status') == 'DISMISSED')}")
    print("=" * 80)
