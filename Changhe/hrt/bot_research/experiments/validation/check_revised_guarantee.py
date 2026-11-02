"""Compare the revised economy certificate with independent exact evidence."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from bot_research.bots.economy.guarantee import bound
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', default='bot_research/runs/validation/attack-certificate-001-inputs.json')
    parser.add_argument('--reference', default='bot_research/runs/validation/attack-certificate-001.json')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    paths = set(static_closure({'bot_research.experiments.validation.check_revised_guarantee'}))
    paths |= {Path(args.inputs), Path(args.reference), Path('td_game/balanced.json')}
    sources = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    cases = json.loads(Path(args.inputs).read_text())['cases']
    reference = json.loads(Path(args.reference).read_text())
    assert reference['complete'] and not reference['violations'] and not reference['source_changed_during_run']
    rows = {r['id']: r for r in reference['results']}
    rules = balanced_config().to_dict()
    started = time.perf_counter()
    results = []
    for case in cases:
        old = rows[case['id']]
        expected = old['certificate']['integer_lower_bound']
        actual = bound(case['buildings'], case['gold'], len(case['prefix']), case['package'], rules)
        fixed = bound(case['buildings'], case['gold'], len(case['prefix']), case['package'], rules,
                      L_max=old['certificate']['L_max'])
        result = {'id': case['id'], 'expected_independent_integer_bound': expected,
                  'actual': actual, 'actual_supplied_L_max': fixed,
                  'is_int': type(actual) is int and type(fixed) is int,
                  'matches_reference': fixed == expected,
                  'default_matches_reference': actual == expected,
                  'zero_gold_tighter_route_bound': case['gold'] == 0 and actual != fixed,
                  'minimum_tested_package_damage': min(r['package_damage'] for r in old['combat'])}
        if case['gold'] == 0:
            exact = bound(case['buildings'], 0, len(case['prefix']), case['package'], rules,
                          existing_types=case['prefix'])
            result['no_response_exact_branch'] = exact
            result['no_response_matches_engine'] = exact == old['combat'][0]['package_damage']
        results.append(result)
    changed = [p for p, h in sources.items() if hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
    failed = [r['id'] for r in results if not r['is_int'] or not r['matches_reference']
              or not r.get('no_response_matches_engine', True)
              or r['actual'] > r['minimum_tested_package_damage']]
    output = {'time_utc': now(), 'runtime_seconds': time.perf_counter() - started,
              'source_sha256': sources, 'source_changed_during_run': changed,
              'cases': len(results), 'failed': failed, 'results': results,
              'scope': 'Regression comparison with independent exact bounds and preserved original-combat measurements; no new response enumeration.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'runtime_seconds', 'cases', 'failed', 'source_changed_during_run')}))
    assert not failed and not changed


if __name__ == '__main__':
    main()
