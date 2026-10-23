#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tier A Sub-Variant Generator Wrapper (Gate 2 Compliant <500 LOC).
Loads pre-compiled bespoke records from scripts/tier_a_subvariants_data.json.
"""
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "tier_a_subvariants_data.json"

def get_tier_a_records():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    records = get_tier_a_records()
    print(f"Loaded {len(records)} Tier A records from {DATA_PATH.name}")
