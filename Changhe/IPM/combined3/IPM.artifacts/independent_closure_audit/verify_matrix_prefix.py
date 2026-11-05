#!/usr/bin/env python3
"""Independent whole-cover validator plus isolated prefix-assembler replay.

Only this audit directory is written. A pending producer cannot yield PASS.
"""
import argparse
import json
import math
import subprocess
import sys
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ART = HERE.parent
OP = ART / 'operator_theory'
PRODUCER = OP / 'assemble_matrix_prefix_signed_far_v01.py'
RESULT = OP / 'matrix_prefix_signed_far_v01/result.json'
REPLAY = HERE / 'matrix_prefix_replay'
ctx.prec = 512

def digest(p):
    return sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.loads(p.read_text())

def check_bindings(mapping):
    assert mapping
    for name, expected in mapping.items():
        assert digest(ART/name) == expected, name

def complete(paths, max_depth):
    assert len(paths) == len(set(paths))
    paths = set(paths)
    assert all(set(p) <= {'0','1'} and len(p) <= max_depth for p in paths)
    def visit(s):
        if s in paths:
            assert not any(p != s and p.startswith(s) for p in paths)
            return
        assert len(s) < max_depth
        visit(s+'0')
        visit(s+'1')
    visit('')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--replay', action='store_true')
    args = ap.parse_args()
    if args.replay:
        subprocess.run([sys.executable, '-B', str(PRODUCER), '--out', str(REPLAY)], check=True,
                       stdout=subprocess.DEVNULL)
    out = {'finished_utc': datetime.now(timezone.utc).isoformat(),
           'auditor_code_sha256': digest(Path(__file__))}
    if not RESULT.exists() or not (REPLAY/'result.json').exists():
        out.update(status='INDEPENDENT_MATRIX_PREFIX_AUDIT_PENDING', reason='missing main or replay result')
    else:
        main_result, replay_result = read(RESULT), read(REPLAY/'result.json')
        want = 'CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR'
        if main_result['status'] != want or replay_result['status'] != want:
            out.update(status='INDEPENDENT_MATRIX_PREFIX_AUDIT_PENDING',
                       main_status=main_result['status'], replay_status=replay_result['status'],
                       main_available=main_result.get('available_base_panels'),
                       replay_available=replay_result.get('available_base_panels'))
        else:
            fields = ['configuration', 'used_base_panels', 'available_base_panels',
                      'missing_base_panels', 'core_endpoint_exact', 'exterior_start',
                      'origin_lower', 'origin_detail', 'exterior_lower', 'exterior_detail',
                      'used_chunk_sha256', 'bindings', 'failed_base_panels', 'total_leaves']
            assert all(main_result[k] == replay_result[k] for k in fields)
            d = main_result
            cfg = d['configuration']
            cp = ART/'actual_matrix_v01/configuration.json'
            assert read(cp) == cfg
            check_bindings(cfg['bindings'])
            check_bindings(d['bindings'])
            ratio, lo, hi = map(F, [cfg['ratio'], cfg['rmin'], cfg['rmax']])
            n, used_n = cfg['panels'], d['used_base_panels']
            assert lo > 0 and ratio > 1 and lo*ratio**(n-1) < hi <= lo*ratio**n
            assert 0 < used_n <= n
            endpoint = min(lo*ratio**used_n, hi)
            assert endpoint == F(d['core_endpoint_exact']) and endpoint >= d['exterior_start']
            assert F(cfg['beta']) == F(7,10)
            assert arb(d['origin_lower']) >= arb(7)/10
            assert arb(d['exterior_lower']) >= arb(7)/10
            assert d['origin_detail']['exact_strain_and_constant_harmonic_checks'] is True
            assert not d['failed_base_panels'] and not d['missing_base_panels']
            rows = {}
            for name, expected in d['used_chunk_sha256'].items():
                p = ART/name
                assert digest(p) == expected
                chunk = read(p)
                assert chunk['configuration'] == cfg
                for row in chunk['rows']:
                    index = row['index']
                    if index >= used_n:
                        continue
                    assert 0 <= index < used_n and index not in rows and row['pass']
                    complete([x['path'] for x in row['leaves']], cfg['max_depth'])
                    for leaf in row['leaves']:
                        assert leaf['pass']
                        assert all(math.isfinite(leaf[k]) and leaf[k] >= 0 for k in
                                   ['min_aa','min_dd','min_determinant'])
                    rows[index] = row
            assert sorted(rows) == list(range(used_n))
            origin = RESULT.parent/'origin.json'
            replay_origin = REPLAY/'origin.json'
            assert read(origin) == read(replay_origin)
            assert read(origin)['origin'] == d['origin_detail']
            price = OP/'signed_matrix_far_price_v01.json'
            assert read(HERE/'signed_matrix_far_audit.json')['status'] == 'INDEPENDENT_SIGNED_MATRIX_FAR_AUDIT_PASS'
            assert read(HERE/'signed_matrix_far_audit.json')['price_sha256'] == digest(price)
            out.update(status='INDEPENDENT_MATRIX_PREFIX_AUDIT_PASS',
                       producer_sha256=digest(PRODUCER), result_sha256=digest(RESULT),
                       origin_sha256=digest(origin), configuration_sha256=digest(cp),
                       signed_far_price_sha256=digest(price),
                       replay_result_sha256=digest(REPLAY/'result.json'),
                       replay_origin_sha256=digest(replay_origin),
                       source_configuration=cfg, used_chunk_sha256=d['used_chunk_sha256'],
                       used_base_panels=used_n, total_leaves=d['total_leaves'],
                       core_endpoint_exact=str(endpoint), exterior_start=d['exterior_start'],
                       origin_lower=d['origin_lower'], exterior_lower=d['exterior_lower'],
                       mathematical_values_identical=True, values_identical=True,
                       bindings={str(p.relative_to(ART)):digest(p) for p in
                                 [PRODUCER, RESULT, origin, cp, price, Path(__file__),
                                  HERE/'signed_matrix_far_audit.json', REPLAY/'result.json', replay_origin]},
                       conclusion='Whole-plane actual M>=7/10 verified by origin, complete core prefix, and independently audited signed exterior. No stationary theorem follows from this certificate alone.')
    (HERE/'matrix_prefix_audit.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_configuration','used_chunk_sha256']}, indent=2))

if __name__ == '__main__':
    main()
