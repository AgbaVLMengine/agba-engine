#!/usr/bin/env python3
"""
🏛️ ÀGBÀ ENGINE: UNIVERSAL INTRA-DOMAIN CONFINEMENT & CLUSTER PURITY BENCHMARK
=============================================================================
Evaluates Category 1 (Spiritual & Cosmological Matrix) and the Universal
Categorical Boundary Law across all 17 categories.

Key Mathematical Invariants:
1. P_Tier3 (Tier 3 Intra-Category Purity) == 100.00%
   Dynamic token scoring in Tier 3 MUST NEVER cross categorical boundaries.
2. Cross-Domain Hop Legitimacy (H_CrossDomain) == 100.00%
   Cross-domain links are ONLY permissible if forged via explicit bilateral
   edges in data (Tiers 1 & 2: related_entities, cultural_relatives, sub_variants).
3. Cluster Purity Score (CPS) >= 98.5% across Category 1.

Author: Ọlọ́yè Sùúrù (suuru-qa)
Supervising Architect: Ọlọ́yè Àgbà (agba-pa-architect)
Lead Architect: Àrùnà Ọlànrewájú Kábírù (Kábíyèsí)
"""

import sys
import os
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_PATH = REPO_ROOT / "web" / "src" / "data" / "yoruba_master_corpus.json"


def run_clustering_audit() -> dict:
    js_code = """
import fs from 'fs';
import { resolveKnowledgeGraphRelatives } from './web/src/utils/relativesResolver.js';

const corpus = JSON.parse(fs.readFileSync('./web/src/data/yoruba_master_corpus.json', 'utf8'));
const cat1 = corpus.filter(e => e.category === 'Spiritual & Cosmological Matrix');

function stripAccents(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
}
function normalizeNFC(s) {
  return (s || '').trim().toLowerCase().normalize('NFC');
}

let total_cat1_entities = cat1.length;
let total_resolved_links = 0;
let cross_category_links = 0;
let explicit_sanctioned_cross = 0;
let lineage_sibling_cross = 0;
let unsanctioned_tier3_leaks = 0;

const leak_details = [];

for (const ent of cat1) {
  const rels = resolveKnowledgeGraphRelatives(ent, corpus, 6);
  total_resolved_links += rels.length;

  const explicitSet = new Set([
    ...(ent.sub_variants || []),
    ...(ent.related_entities || []),
    ...(ent.cultural_relatives || []),
    ent.sovereign_parent
  ].filter(Boolean).map(x => normalizeNFC(stripAccents(x))));

  const entNFC = normalizeNFC(stripAccents(ent.title));

  for (const r of rels) {
    if (r.category !== 'Spiritual & Cosmological Matrix') {
      cross_category_links++;

      const rNFC = normalizeNFC(stripAccents(r.title));
      const rIdNFC = normalizeNFC(stripAccents(r.id || ''));

      // 1. Direct explicit edge check (Tier 1 & Tier 2 direct parent)
      const isExplicit = (
        explicitSet.has(rNFC) ||
        explicitSet.has(rIdNFC) ||
        (r.sub_variants && r.sub_variants.some(s => normalizeNFC(stripAccents(s)) === entNFC)) ||
        (r.related_entities && r.related_entities.some(s => normalizeNFC(stripAccents(s)) === entNFC)) ||
        (r.cultural_relatives && r.cultural_relatives.some(s => normalizeNFC(stripAccents(s)) === entNFC)) ||
        normalizeNFC(stripAccents(r.sovereign_parent || '')) === entNFC ||
        normalizeNFC(stripAccents(ent.sovereign_parent || '')) === rNFC
      );

      // 2. Lineage sibling check (Tier 2/2b shared sovereign parent)
      const isLineageSibling = corpus.some(p => {
        const pSubs = (p.sub_variants || []).map(s => normalizeNFC(stripAccents(s)));
        const pTitleNFC = normalizeNFC(stripAccents(p.title));
        const entSovNFC = normalizeNFC(stripAccents(ent.sovereign_parent || ''));
        const rSovNFC = normalizeNFC(stripAccents(r.sovereign_parent || ''));

        return (
          (pSubs.includes(entNFC) && pSubs.includes(rNFC)) ||
          (pTitleNFC === entSovNFC && pSubs.includes(rNFC)) ||
          (pTitleNFC === rSovNFC && pSubs.includes(entNFC))
        );
      });

      if (isExplicit) {
        explicit_sanctioned_cross++;
      } else if (isLineageSibling) {
        lineage_sibling_cross++;
      } else {
        unsanctioned_tier3_leaks++;
        leak_details.push({
          source: ent.title,
          source_cat: ent.category,
          pollutant: r.title,
          pollutant_cat: r.category
        });
      }
    }
  }
}

// Invariants
const total_sanctioned = explicit_sanctioned_cross + lineage_sibling_cross;
const tier3_purity = unsanctioned_tier3_leaks === 0 ? 100.0 : ((total_resolved_links - unsanctioned_tier3_leaks) / total_resolved_links) * 100.0;
const cps = ((total_resolved_links - unsanctioned_tier3_leaks) / total_resolved_links) * 100.0;

const result = {
  total_cat1_entities,
  total_resolved_links,
  cross_category_links,
  explicit_sanctioned_cross,
  lineage_sibling_cross,
  unsanctioned_tier3_leaks,
  tier3_purity,
  cps,
  sample_leaks: leak_details.slice(0, 10)
};

process.stdout.write(JSON.stringify(result));
"""
    cmd = ["node", "--input-type=module", "-e", js_code]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        print("STDERR from Node harness:\n", proc.stderr, file=sys.stderr)
        raise RuntimeError(f"Audit failed with exit code {proc.returncode}")
    return json.loads(proc.stdout)


def main():
    print("=" * 80)
    print("🏛️ ÀGBÀ ENGINE: CATEGORY 1 CLUSTER PURITY BENCHMARK")
    print("Lead QA Specialist: Ọlọ́yè Sùúrù (`suuru-qa`) | Lead Architect: Àrùnà Ọlànrewájú Kábírù")
    print("=" * 80)

    res = run_clustering_audit()

    print(f"📊 CATEGORY 1 ENTITIES AUDITED: {res['total_cat1_entities']}")
    print(f"🔗 TOTAL RESOLVED RELATIVE LINKS: {res['total_resolved_links']}")
    print(f"🌐 CROSS-CATEGORY LINKS TOTAL: {res['cross_category_links']} ({(res['cross_category_links']/res['total_resolved_links'])*100:.2f}%)")
    print(f"  • Explicit Curated Edges (Tier 1 & Tier 2): {res['explicit_sanctioned_cross']}")
    print(f"  • Sovereign Sibling Lineage Links (Tier 2b): {res['lineage_sibling_cross']}")
    print(f"  • Unsanctioned Tier-3 Dynamic Bleed: {res['unsanctioned_tier3_leaks']}")
    print("-" * 80)
    print(f"🛡️ TIER 3 INTRA-CATEGORY PURITY (P_Tier3): {res['tier3_purity']:.4f}% (Invariant: 100.00%)")
    print(f"👑 CLUSTER PURITY SCORE (CPS): {res['cps']:.4f}% (Invariant: >= 98.50%)")
    print("=" * 80)

    if res['unsanctioned_tier3_leaks'] > 0:
        print(f"⚠️ {res['unsanctioned_tier3_leaks']} UNSANCTIONED CROSS-DOMAIN LEAKS DETECTED:")
        for leak in res['sample_leaks']:
            print(f"  - [{leak['source']}] (Category 1) -> [{leak['pollutant']}] ({leak['pollutant_cat']})")
        print("\n❌ VERDICT: FAIL — Cross-domain leakage violates Universal Confinement Law.")
        sys.exit(1)
    else:
        print("✅ VERDICT: 100.00% CERTIFIED PASS (Zero Tier-3 Cross-Domain Bleed)")
        print("✨ Category 1 (Spiritual & Cosmological Matrix) is completely sealed against secular drift.")
        sys.exit(0)


if __name__ == "__main__":
    main()
