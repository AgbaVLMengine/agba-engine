# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: HITL TELEMETRY DIAGNOSTICS & CANDIDATE EXTRACTOR (v6.2.0)
# ==============================================================================
# Lead Architect & Creator: Àrùnà Ọlànrewájú Kábírù
# Pure diagnostic engine for MLOps candidate extraction and discrepancy analysis.
# ==============================================================================

import json
import time
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Tuple


def normalize_nfc(text: str) -> str:
    """Normalize string using Unicode NFC."""
    return unicodedata.normalize("NFC", text.strip()) if text else ""


def strip_accents(text: str) -> str:
    """Strip accents for ASCII-folded matching."""
    nfkd = unicodedata.normalize("NFKD", text or "")
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower()


def load_jsonl_records(
    feedback_path: Path, query_log_path: Path
) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    """Stream and parse feedback store and query telemetry logs."""
    feedbacks: List[Dict[str, Any]] = []
    queries_by_id: Dict[str, Dict[str, Any]] = {}

    if query_log_path.exists():
        with open(query_log_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        rec = json.loads(line)
                        if rec.get("query_id"):
                            queries_by_id[rec["query_id"]] = rec
                    except Exception:
                        pass

    if feedback_path.exists():
        with open(feedback_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        feedbacks.append(json.loads(line))
                    except Exception:
                        pass

    return feedbacks, queries_by_id


def diagnose_candidate(
    candidate: Dict[str, Any],
    corpus_by_id: Dict[str, Dict[str, Any]],
    corpus_by_folded: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """Perform deterministic cultural diagnosis and propose action."""
    concept = candidate.get("queried_concept", "")
    correction = candidate.get("user_correction", "")
    returned_id = candidate.get("returned_entity_id")
    tags = candidate.get("tags", [])

    matched = (corpus_by_id.get(returned_id) if returned_id else None) or corpus_by_folded.get(strip_accents(concept))

    if "diacritic_error" in tags or (
        matched and strip_accents(concept) == strip_accents(matched.get("id", "")) and concept != matched.get("id")
    ):
        eid = matched.get("id") if matched else None
        return {
            "diagnosis_type": "DIACRITIC_ERROR",
            "target_entity_id": eid,
            "proposed_action": "VERIFY_CANONICAL_DIACRITICS",
            "recommendation": f"Add ASCII folded query '{concept}' as search alias to canonical '{eid}' if not already present.",
            "proposed_patch": {"entity_id": eid, "add_alias": concept if concept != eid else None},
            "confidence_score": 0.95,
        }

    if matched and correction:
        eid = matched.get("id")
        return {
            "diagnosis_type": "NEW_ALIAS_PROPOSAL",
            "target_entity_id": eid,
            "proposed_action": "ADD_CULTURAL_ALIAS",
            "recommendation": f"User proposed alternative name or diaspora term for '{eid}': '{correction}'.",
            "proposed_patch": {"entity_id": eid, "add_alias": correction.strip()},
            "confidence_score": 0.88,
        }

    if not matched:
        return {
            "diagnosis_type": "NEW_ENTITY_CANDIDATE",
            "target_entity_id": None,
            "proposed_action": "STAGE_FOR_14_TIER_ENRICHMENT",
            "recommendation": f"Queried concept '{concept}' does not exist in master corpus. Stage for full 14-tier scholarly creation.",
            "proposed_patch": {"new_concept_title": concept, "user_notes": correction},
            "confidence_score": 0.75,
        }

    return {
        "diagnosis_type": "GENERAL_FEEDBACK",
        "target_entity_id": matched.get("id") if matched else None,
        "proposed_action": "MANUAL_REVIEW",
        "recommendation": "Review feedback notes against cultural context.",
        "proposed_patch": {},
        "confidence_score": 0.60,
    }


def extract_actionable_candidates(
    feedbacks: List[Dict[str, Any]],
    queries_by_id: Dict[str, Dict[str, Any]],
    pending_json_path: Path,
    corpus_by_id: Dict[str, Dict[str, Any]],
    corpus_by_folded: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Identify negative ratings, explicit user corrections, and zero-hit queries."""
    actionable: List[Dict[str, Any]] = []
    existing_status_map: Dict[str, Dict[str, Any]] = {}

    if pending_json_path.exists():
        try:
            for ec in json.loads(pending_json_path.read_text(encoding="utf-8")):
                if ec.get("candidate_id"):
                    existing_status_map[ec["candidate_id"]] = ec
        except Exception:
            pass

    special_tags = {"diacritic_error", "missing_alias", "missing_entity", "domain_mismatch"}
    for fb in feedbacks:
        if fb.get("status") in ["COMMITTED", "DISMISSED"]:
            continue
        rating, correction, tags, query_id = fb.get("rating"), fb.get("user_correction"), fb.get("tags", []), fb.get("query_id")
        if rating == "thumbs_down" or bool(correction and correction.strip()) or any(t in special_tags for t in tags):
            q_meta = queries_by_id.get(query_id, {})
            cid = f"cand_{query_id}"
            candidate = {
                "candidate_id": cid,
                "query_id": query_id,
                "timestamp": fb.get("timestamp", time.time()),
                "client_tier": fb.get("client_tier", "Unknown"),
                "rating": rating,
                "queried_concept": fb.get("queried_concept") or q_meta.get("queried_concept") or "Unknown Concept",
                "returned_entity_id": fb.get("returned_entity_id") or q_meta.get("top_entity_id"),
                "user_correction": correction,
                "tags": tags,
                "status": existing_status_map.get(cid, {}).get("status", "PENDING_REVIEW"),
            }
            candidate.update(diagnose_candidate(candidate, corpus_by_id, corpus_by_folded))
            actionable.append(candidate)

    seen_zero = set()
    for qid, q in queries_by_id.items():
        if q.get("results_count", 0) == 0:
            concept = (q.get("queried_concept") or q.get("raw_query") or q.get("query") or "").strip()
            c_norm = strip_accents(concept)
            if not concept or c_norm in seen_zero:
                continue
            seen_zero.add(c_norm)
            cid = f"cand_zero_{qid}"
            candidate = {
                "candidate_id": cid,
                "query_id": qid,
                "timestamp": q.get("timestamp", time.time()),
                "client_tier": q.get("client_tier", "Universal_Web"),
                "rating": "zero_hit",
                "queried_concept": concept,
                "returned_entity_id": None,
                "user_correction": "Zero-shot search returned 0 hits from master corpus.",
                "tags": ["zero_hit", "telemetry_mined"],
                "status": existing_status_map.get(cid, {}).get("status", "PENDING_REVIEW"),
            }
            candidate.update(diagnose_candidate(candidate, corpus_by_id, corpus_by_folded))
            actionable.append(candidate)

    return actionable
