"""Finite final report support from explicitly accepted own numerical roots."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import argparse
import importlib.util
import json
import os
import re
import sys
import time

R = Path(__file__).resolve().parents[3]
B = R / 'research/final_report_numerical'
sys.set_int_max_str_digits(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', required=True)
    version = ap.parse_args().version
    assert re.fullmatch(r'v\d{2}', version)
    assert os.sched_getaffinity(0) == {57}
    assert os.getpriority(os.PRIO_PROCESS, 0) == 19
    started = time.monotonic()
    inputs, checks, issues, displays = {}, {}, [], []
    observed, cache = {}, {}
    target = B / f'verification/result_{version}.json'
    assert not target.exists()

    def sha(p):
        p = Path(p).resolve(strict=True)
        assert p.is_relative_to(R)
        s = p.stat()
        sig = (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
        key = (str(p), sig)
        if key not in cache:
            h = sha256()
            with p.open('rb') as f:
                while chunk := f.read(1024 * 1024):
                    h.update(chunk)
            t = p.stat()
            assert sig == (t.st_dev, t.st_ino, t.st_size, t.st_mtime_ns)
            cache[key] = h.hexdigest()
        observed[str(p)] = sig
        return cache[key]

    def bind(p, expected=None):
        p = Path(p)
        p = p if p.is_absolute() else R / p
        h = sha(p)
        key = str(p.relative_to(R))
        assert expected is None or h == expected, (key, expected, h)
        assert key not in inputs or inputs[key] == h
        inputs[key] = h
        return p

    def read(p, expected=None):
        return json.loads(bind(p, expected).read_text())

    def ck(name, okay, detail=None):
        assert name not in checks, name
        checks[name] = bool(okay)
        if not okay:
            issues.append({'check': name, 'detail': detail})

    def ball(text):
        m = re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]', text)
        assert m, text
        center, radius = map(Q, m.groups())
        assert radius >= 0
        return center - radius, center + radius

    prepared = read(B / 'verification/PROOF_FIRST.json')
    assert not prepared['checker_exists'] and not prepared['result_exists']
    bind(B / 'PROOF.md', prepared['proof_sha256'])
    bind(Path(__file__))
    prepared2 = read(B / "verification/PROOF_FIRST_v02.json")
    assert not prepared2["checker_exists"] and not prepared2["any_result_exists"]
    bind(B / "THRESHOLD_PROOF_v02.md", prepared2["supplement_sha256"])
    bind(B / "code/check.py", prepared2["previous_unexecuted_checker_sha256"])
    prepared3 = read(B / "verification/PROOF_FIRST_v03.json")
    assert not prepared3["checker_exists"] and not prepared3["result_exists"]
    bind(B / "PATH_PROOF_v03.md", prepared3["supplement_sha256"])
    bind(B / "code/check_v02.py", prepared3["previous_checker_sha256"])
    bind(B / "verification/run_v01.log", prepared3["failure_log_sha256"])
    manifest = read(B / f'source/MANIFEST_{version}.json')
    assert manifest['version'] == version and not manifest['result_exists']
    for path, h in manifest['files'].items():
        bind(path, h)
    report = (R / manifest['report']).read_text()
    matrix = (R / manifest['matrix']).read_text()
    ledger = (R / manifest['ledger']).read_text()
    headings = {}
    for block in re.split(r'(?m)(?=^## )', ledger):
        head = block.splitlines()[0] if block.splitlines() else ''
        ids = re.findall(r'N4-(\d{3})', head)
        bare = re.match(r'^## (\d{3})\.', head)
        if bare:
            ids.append(bare.group(1))
        for early in ['001', '002']:
            if 'V' + early in head:
                ids.append(early)
        for number in set(ids):
            headings.setdefault(int(number), []).append(block)
    roots = {}
    for role, rec in manifest['accepted_roots'].items():
        obj = read(rec['record'], rec['sha256'])
        bind(rec['proof'])
        number = int(rec['claim'].removeprefix('N4-'))
        sections = headings.get(number, [])
        assert any(rec['sha256'] in s and 'CONFIRMED' in s for s in sections), rec
        if isinstance(obj.get('checks'), dict):
            assert all(obj['checks'].values()), rec['claim']
        assert not obj.get('errors'), rec['claim']
        if role == 'X007180':
            assert set(obj['inputs']) == {'source/MANIFEST.json', 'PROOF.md', 'code/check.py'}
        for rel, h in obj.get('inputs', {}).items():
            resolved = Path('research/registered_norm_assembly') / rel if role == 'X007180' else rel
            bind(resolved, h)
        roots[role] = obj

    parser_path = bind('research/final_table_trace/code/check_documentary_v02.py')
    spec = importlib.util.spec_from_file_location('own_table_parser', parser_path)
    parser = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parser)
    rr = parser.rows(report, 8, '| # | framework | candidate |')
    mm = parser.rows(matrix, 11)
    ck('complete_numbered_rows', set(rr) == set(mm) == set(range(1, 109)))

    def candidate(text):
        text = text.split('(', 1)[0]
        text = re.sub(r'(?<![A-Za-z0-9-])(d2|Mpen2|b6)(?![A-Za-z0-9-])',
                      lambda m: 'C1-A2-' + m.group(1), text)
        return set(re.findall(r'C1-N1-\d{3}|C1-BASE-S131|C1-A2-(?:d2|Mpen2|b6)', text))

    trace = []
    for n, row in rr.items():
        peer = mm.get(n)
        if peer is None:
            continue
        a, b = candidate(row['cells'][2]), candidate(peer['cells'][2])
        ck(f'row{n}_candidate', b <= a if n in [12, 13, 14] else a == b)
        label = parser.lab(row['cells'][-1])
        ck(f'row{n}_status', label == parser.lab(peer['cells'][-1]))
        ck(f'row{n}_no_existence_promotion', label not in ['PROVED', 'CONDITIONAL'])
        trace.append({'row': n, 'report_line': row['line'], 'matrix_line': peer['line'],
                      'candidate_ids': sorted(a), 'status': label,
                      'scope': 'candidate and primary status linkage only'})
    citation_trace = []
    for name, text in [('report', report), ('matrix', matrix)]:
        for n in sorted({int(v) for v in re.findall(r'N4-(\d{3})', text)}):
            ck(f'{name}_N4_{n}_heading', n in headings)
            citation_trace.append({'source': name, 'number': n,
                                   'headings': [s.splitlines()[0] for s in headings.get(n, [])]})

    distance = roots['distance387']
    for i, edge in enumerate(distance['edges']):
        assert edge['pass'] and not edge['decoded_gzip']
        bind(edge['path'], edge['expected_sha256'])
        ck(f'distance_edge{i}', True)
    ck('distance2023_edges', len(distance['edges']) == 2023)
    principal = []
    for row in distance['results']:
        n = row['report_row']
        vals = [(m.group(0), Q(m.group(1)))
                for m in re.finditer(r'>\s*(0\.\d+)', rr[n]['text'])]
        choices = [pair for pair in vals if Q(row['floor']) / 2 < pair[1] < 2 * Q(row['floor'])]
        ck(f'principal{n}_present', bool(choices))
        if not choices:
            continue
        literal, value = choices[0]
        okay = value <= Q(row['floor']) < Q(row['root_interval'][0])
        ck(f'principal{n}_directed', okay, literal)
        principal.append({'row': n, 'candidate': row['candidate'], 'literal': literal,
                          'display_exact': str(value), 'floor': row['floor'],
                          'root_lower': row['root_interval'][0], 'pass': okay})
    ratio_rows = []
    for i, row in enumerate(distance['selected_ratios']):
        ck(f'ratio{i}_same_literal', row['literal'] in rr[row['report_row']]['text'])
        ck(f'ratio{i}_directed', Q(row['printed_factor']) < Q(row['exact_lower_ratio']))
        ratio_rows.append(row)
    ck('nineteen_principals', len(principal) == 19)
    ck('twentytwo_ratios', len(ratio_rows) == 22)

    scalar = roots['coverage390']['scalar_families']
    ck('eight_fixed_scalar_tuples', len(scalar) == 8)
    for row in scalar:
        ck('scalar:' + row['name'], Q(row['ceiling_squared_exact']) < Q(3793, 10**9)**2)
    graded2 = Q(50, 651)**2 / 28248
    ck('graded_exact_square', graded2 == Q(625, 2992882662))
    ck('graded457e_minus6', graded2 < Q('4.57e-4')**2)
    ck('scalar38e_minus7', Q(3793, 10**9) < Q('3.8e-6'))

    h016, e007, x007, optimum = (roots[k] for k in ['complete016', 'E007252', 'X007180', 'optimum415'])
    selected = report.split('## Answers in brief', 1)[1].split('## Short answers', 1)[0]
    selected += '\n' + rr[80]['text']
    lower_h, upper_h = Q(h016['H_strict_lower_exact']), Q(h016['H_strict_upper_exact'])
    lower_e, upper_e = Q(h016['E2_strict_lower_exact']), Q(h016['E2_strict_upper_exact'])
    patterns = [
        ('H016 lower', r'(0\.\d+)\s*<\s*H\(016\)', lower_h, 'lower'),
        ('H016 upper', r'H\(016\)\s*<\s*(0\.\d+)', upper_h, 'upper'),
        ('E2016 lower', r'E_2\(016\)\s*>\s*([0-9]+\.\d+)', lower_e, 'lower'),
        ('E2016 upper', r'E_2\(016\)\s*<\s*([0-9]+\.\d+)', upper_e, 'upper'),
    ]
    for name, pattern, accepted, direction in patterns:
        for i, match in enumerate(re.finditer(pattern, selected)):
            value = Q(match.group(1))
            okay = value <= accepted if direction == 'lower' else accepted <= value
            ck(f'{name}:{i}', okay, match.group(0))
            displays.append({'kind': name, 'literal': match.group(0), 'display_exact': str(value),
                             'accepted_exact': str(accepted), 'pass': okay})
    ck('selected_H016_lower_and_upper_present',
       any(x['kind'] == 'H016 lower' for x in displays) and any(x['kind'] == 'H016 upper' for x in displays))
    e007_upper = Q(e007['E_upper']['strict_upper_exact'])
    ck('E2016_gap21759869526341', lower_e - e007_upper >= Q('21.759869526341'))
    h007_lower = ball(e007['H_input_lower_ball'])[0]
    ck('H007_H016_gap017571422145091', h007_lower - upper_h > Q('0.017571422145091'))
    ck('H016_less_than_H007', upper_h < h007_lower)
    for row in e007['instances']:
        ck('four007thresholds:' + row['framework'],
           Q(row['lower_comparison']['strict_lower_exact']) / Q(row['threshold_exact']) > 5700000)
    rebal = next(row for row in e007['instances'] if row['framework'] == 'FW-T-TB-rebal-v1')
    threshold = Q(rebal['threshold_exact'])
    ck('rebal_exact_threshold_and_s', threshold == Q(3, 327680) and Q(rebal['s_exact']) == Q(1, 65536))
    ck('rebal_decimal_error', Q('9.1553e-6') - threshold == Q(17, 640000000000))
    ck('rebal_decimal_nearest_only', 0 < Q('9.1553e-6') - threshold < Q(1, 20000000000))
    registration = [line for line in report.splitlines() if line.startswith('| FW-T-TB-rebal-v1 |')]
    ck('one_rebal_registration_row', len(registration) == 1)
    ck('rebal_registration_exact_fraction', len(registration) == 1 and '3/327680' in registration[0], registration)
    sharpw = next(row for row in x007['instances'] if row['label'] == 'sharpw')
    xlo = ball(sharpw['lower_comparison']['ball'])[0]
    xhi = ball(sharpw['upper_comparison']['ball'])[1]
    ck('007_coarse_sharpw_display', Q('756.531') < xlo and xhi < Q('757.852'))
    ck('007_sharpw_ratio_display', xlo / Q(sharpw['threshold_exact']) > Q('3596535.57'))
    mu, A = Q(optimum['mu']), Q(optimum['A'])
    ck('fixed_optimum_r', mu / (2 * A) == Q(optimum['r_star']) == Q(201799, 149299200))
    ck('fixed_optimum_eta', mu**2 / (4 * A) == Q(optimum['eta_star']) == Q(40722836401, 193491763200000))
    ck('fixed_optimum_printed', optimum['eta_star'] in selected and optimum['r_star'] in selected)
    ck('007_ratio_eta_star', xlo / Q(optimum['eta_star']) > 3594606)
    partial = roots['partial017425']
    ck('017_full_upper_root_stays_open', partial['complete_H_upper'].startswith('OPEN'))
    ck('017_full_E2_root_stays_open', partial['complete_E2_and_017_less_than007'].startswith('OPEN'))
    ck('017_sixteen_duals', [x['n'] for x in partial['modes']] == list(range(1, 32, 2)))
    ck('017_only_two_hres', [x['n'] for x in partial['modes'] if x['independent_hres']] == [1, 3])
    ck('017_strict_lower', Q(partial['H_strict_lower_exact']) == Q('0.614419598760047422137134027058'))
    ck('selected017_conditional_label', 'CLAIMS E_2(017) < E_2(007)' in selected and 'conditional arithmetic' in selected)
    ck('selected017_lower_not_upper', Q(partial['H_strict_lower_exact'])**2 < Q(partial['H_lower_square_exact']))

    for path, sig in observed.items():
        s = Path(path).stat()
        assert sig == (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns), path
    output = {
        'utc': datetime.now(timezone.utc).isoformat(), 'version': version,
        'inputs': inputs, 'checks': checks, 'check_count': len(checks), 'issues': issues,
        'report_sha256': inputs[manifest['report']], 'matrix_sha256': inputs[manifest['matrix']],
        'numbered_rows': len(trace), 'physical_report_rows': len({r['line'] for r in rr.values()}),
        'row_trace': trace, 'N4_citation_trace': citation_trace,
        'principal_displays': principal, 'selected_ratios': ratio_rows,
        'norm_displays': displays, 'complete016_root': manifest['accepted_roots']['complete016'],
        'candidate017_scope': 'Sixteen dual lower trials and n1/n3 residual trials only. Full upper/E2 OPEN.',
        'numerics_literal_repair_root': manifest['accepted_roots']['repairs424'],
        'selected_answer_scope': 'Answers in brief and row80 for selected016/017 labels; not every narrative subclaim.',
        'scope': 'Finite documentary and directed numerical support from accepted roots. No new PDE or integral certificate.',
        'source_integrals_recomputed': False, 'peer_code_executed': False,
        'elapsed_seconds': time.monotonic() - started,
        'verdict': 'CONFIRMED listed finite checks' if not issues else 'OPEN or REFUTED listed source support, see issues',
    }
    with target.open('x') as f:
        json.dump(output, f, indent=2)
        f.write('\n')
    print(json.dumps({'utc': output['utc'], 'checks': len(checks), 'inputs': len(inputs),
                      'issues': issues, 'sha256': sha(target), 'elapsed_seconds': output['elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
