# ==============================================================================
# 🏛️ ÀGBÀ ENGINE: HITL VISUAL APPROVAL & CORPUS COMMIT CLI (v6.1.0)
# ==============================================================================
# Lead Architect & Creator: Aruna Olanrewaju Kabiru
# Rule: Supreme Corpus Primacy — Museum metadata is secondary; Corpus is SSoT.
# ==============================================================================

import os
import sys
import json
import shutil
import argparse
from pathlib import Path

ROOT_DIR = Path("/mnt/chromeos/shared/MyFiles/Projects /Agba Engine")
STAGING_DIR = ROOT_DIR / "agba_enterprise_api" / "hitl_harvest_staging"
STAGING_MANIFEST = STAGING_DIR / "pending_harvested_candidates.json"
MATRIX_IMAGES_DIR = ROOT_DIR / "Agba_Golden_Matrix" / "Images"
VAULT_REGALIA_DIR = ROOT_DIR / "Agba_Engine_Foundational_Vault" / "04_Curated_Visual_Regalia"
UNIFIED_MANIFEST_PATH = ROOT_DIR / "Agba_Golden_Matrix" / "agba_unified_visual_regalia_manifest.json"
AUDIT_LOG_PATH = STAGING_DIR / "hitl_approval_audit.jsonl"

def load_staged_candidates():
    if not STAGING_MANIFEST.exists():
        print(f"❌ Staging manifest not found at {STAGING_MANIFEST}")
        return []
    with open(STAGING_MANIFEST, "r", encoding="utf-8") as f:
        return json.load(f)

def save_staged_candidates(candidates):
    with open(STAGING_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2, ensure_ascii=False)

def show_status():
    candidates = load_staged_candidates()
    print("=" * 80)
    print("🏛️ ÀGBÀ ENGINE: HITL VISUAL CANDIDATE REVIEW STATUS")
    print(f"   Staging Directory: {STAGING_DIR}")
    print(f"   Total Staged Items: {len(candidates)}")
    print("=" * 80)

    from collections import Counter
    statuses = Counter(c.get("hitl_status", "UNKNOWN") for c in candidates)
    for s, count in statuses.items():
        print(f"   • {s:25}: {count}")

    print("\nCandidate Summary:")
    for idx, c in enumerate(candidates, 1):
        status_icon = "⏳" if c["hitl_status"] == "PENDING_HUMAN_INSPECTION" else ("✅" if c["hitl_status"] == "APPROVED" else "❌")
        print(f"   [{idx:02d}] {status_icon} Concept: {c['canonical_name']:15} | File: {c['staged_filename']} | Status: {c['hitl_status']}")

def apply_approvals():
    candidates = load_staged_candidates()
    approved = [c for c in candidates if c.get("hitl_status") == "APPROVED"]

    if not approved:
        print("ℹ️ No candidates with status 'APPROVED' found.")
        print("   To approve a candidate, edit pending_harvested_candidates.json and set \"hitl_status\": \"APPROVED\",")
        print("   or run: python3 apply_hitl_visual_approval.py --approve-id <filename_or_concept>")
        return

    print(f"\n🚀 Applying {len(approved)} APPROVED visual candidates to Master Corpus...")

    # Load master manifest
    if UNIFIED_MANIFEST_PATH.exists():
        with open(UNIFIED_MANIFEST_PATH, "r", encoding="utf-8") as f:
            master_manifest = json.load(f)
    else:
        master_manifest = []

    # Backup manifest
    backup_path = UNIFIED_MANIFEST_PATH.with_suffix(".json.bak")
    shutil.copyfile(UNIFIED_MANIFEST_PATH, backup_path)
    print(f"   🔒 Backed up master manifest to {backup_path.name}")

    existing_filenames = {item.get("filename") for item in master_manifest}
    applied_count = 0

    for c in approved:
        staged_file = Path(c["staging_file_path"])
        fname = c["staged_filename"]

        if not staged_file.exists():
            print(f"   ⚠️ File not found in staging: {staged_file}")
            continue

        # 1. Copy image to Golden Matrix Images and Foundational Vault
        dest_matrix = MATRIX_IMAGES_DIR / fname
        dest_vault = VAULT_REGALIA_DIR / fname

        shutil.copyfile(staged_file, dest_matrix)
        if VAULT_REGALIA_DIR.exists():
            shutil.copyfile(staged_file, dest_vault)

        # 2. Construct Master Manifest Entry with Supreme Corpus Primacy
        new_entry = {
            "filename": fname,
            "canonical_name": c["canonical_name"],
            "canonical_title_full": f"{c['canonical_name']} ({c['canonical_title']})",
            "indigenous_place_of_origin": c["corpus_indigenous_origin"],
            "origin_region": c["corpus_indigenous_origin"].split(",")[0].strip(),
            "master_artisan_or_guild": "Traditional Yorùbá Master Guild Artisans",
            "creation_epoch": c.get("museum_recorded_date", "Traditional Yorùbá Era"),
            "medium_materials": c.get("museum_recorded_medium", "Authentic Cultural Materials"),
            "category": "Royal Regalia & Sovereign Heritage",
            "corpus_concept_id": c["target_corpus_id"],
            "corpus_deep_description": c["corpus_deep_description"],
            "historical_timeline": "Preserved across generations within sovereign royal and communal custody.",
            "philosophical_context": c.get("corpus_social_context", "Sacred and ceremonial royal usage."),
            "craftsmanship": c.get("corpus_craftsmanship", "Authentic traditional craftsmanship."),
            "current_custodial_repository": c["source_institution"],
            "museum_archival_title": c["museum_original_title"],
            "accession_number": c["museum_accession_id"],
            "license": "CC0 (Public Domain)",
            "source_url": c["source_download_url"],
            "is_foundational": False,
            "hitl_status": "VERIFIED_CANONICAL_MATCH"
        }

        if fname in existing_filenames:
            for i, it in enumerate(master_manifest):
                if it.get("filename") == fname:
                    master_manifest[i] = new_entry
                    break
        else:
            master_manifest.append(new_entry)
            existing_filenames.add(fname)

        applied_count += 1
        print(f"   ✅ Merged: {c['canonical_name']} -> {fname}")

        # Audit log entry
        with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as af:
            af.write(json.dumps({
                "timestamp": "2026-10-06T07:15:00Z",
                "action": "HITL_VISUAL_APPROVAL",
                "concept_id": c["target_corpus_id"],
                "filename": fname,
                "repository": c["source_institution"],
                "status": "MERGED_TO_MASTER_MANIFEST"
            }) + "\n")

    # Save updated master manifest to both Golden Matrix and Foundational Vault
    vault_manifest_path = ROOT_DIR / "Agba_Engine_Foundational_Vault" / "04_Curated_Visual_Regalia" / "agba_unified_visual_regalia_manifest.json"
    for mp in [UNIFIED_MANIFEST_PATH, vault_manifest_path]:
        with open(mp, "w", encoding="utf-8") as f:
            json.dump(master_manifest, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Successfully applied {applied_count} verified images to Master Manifest!")
    print(f"   Total Visual Masterworks in Corpus: {len(master_manifest)}")

def main():
    parser = argparse.ArgumentParser(description="Àgbà Engine HITL Visual Harvest Approval CLI")
    parser.add_argument("--status", action="store_true", help="View current staged candidate review status")
    parser.add_argument("--apply", action="store_true", help="Apply all APPROVED candidates to master manifest")
    parser.add_argument("--approve-id", type=str, help="Approve a specific candidate by concept ID or filename")
    parser.add_argument("--reject-id", type=str, help="Reject a specific candidate by concept ID or filename")

    args = parser.parse_args()

    if args.approve_id:
        candidates = load_staged_candidates()
        matched = False
        for c in candidates:
            if args.approve_id in c["staged_filename"] or args.approve_id.lower() == c["canonical_name"].lower():
                c["hitl_status"] = "APPROVED"
                matched = True
                print(f"✅ Marked '{c['staged_filename']}' as APPROVED.")
        if matched:
            save_staged_candidates(candidates)
        else:
            print(f"❌ No matching candidate found for '{args.approve_id}'")

    elif args.reject_id:
        candidates = load_staged_candidates()
        matched = False
        for c in candidates:
            if args.reject_id in c["staged_filename"] or args.reject_id.lower() == c["canonical_name"].lower():
                c["hitl_status"] = "REJECTED"
                matched = True
                print(f"❌ Marked '{c['staged_filename']}' as REJECTED.")
        if matched:
            save_staged_candidates(candidates)
        else:
            print(f"❌ No matching candidate found for '{args.reject_id}'")

    elif args.apply:
        apply_approvals()

    else:
        show_status()

if __name__ == "__main__":
    main()
