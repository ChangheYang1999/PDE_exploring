"""Own finite repair acceptance. All executable and read paths stay in this lane."""
from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, os, re, time
R = Path(__file__).resolve().parents[3]
B = R / 'research/final_report_repair_acceptance'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def get(p):
    return json.loads(p.read_text())
def rows(text):
    out = {}; active = False
    for n, line in enumerate(text.splitlines(), 1):
        if '| # | framework | candidate |' in line:
            active = True
            continue
        if not active:
            continue
        if out and not line.startswith('|'):
            break
        cells = [v.strip() for v in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) != 8 or not re.fullmatch(r'\d+(?:-\d+)?', cells[0]):
            continue
        bounds = list(map(int, cells[0].split('-')))
        for k in range(bounds[0], bounds[-1] + 1):
            assert k not in out
            out[k] = {'line': n, 'cells': cells}
    return out

def main():
    assert os.sched_getaffinity(0) == {57}
    assert os.getpriority(os.PRIO_PROCESS, 0) == 19
    start = datetime.now(timezone.utc).isoformat(); tick = time.monotonic()
    target = B / 'verification/result.json'; assert not target.exists()
    checks = []
    def ck(value, label):
        checks.append({'check': label, 'pass': bool(value)})
        assert value, label
    m = get(B / 'verification/PROOF_FIRST.json')
    ck(not m['checker_exists'] and not m['result_exists'], 'proof precedes code and result')
    for rel, h in m['inputs'].items():
        p = R / rel
        ck(p.resolve().is_relative_to(R) and sha(p) == h, 'bound local bytes ' + rel)
    source = B / 'source'
    a = (source / 'report1914.md').read_text(); rr = (source / 'reproduce1914.md').read_text()
    a0 = (R / 'research/final_report_diff/source/report1900.md').read_text()
    r0 = (R / 'research/final_report_diff/source/reproduce1900.md').read_text()
    ck(sha(source / 'report1914.md') == '12638987379f94b545751c9f96008696718861a3057b5ca02e1165a980b9502a', 'precise acquired report')
    for old, new, label in [(a0, a, 'report'), (r0, rr, 'reproduce')]:
        diff = ''.join(difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True), fromfile=label + '1900.md', tofile=label + '1914.md'))
        ck(diff == (source / (label + '1900_to1914.diff')).read_text(), label + ' exact stored difference')
    ar, br = rows(a0), rows(a)
    ck(set(ar) == set(br) == set(range(1, 109)), '108 unique expanded comparison rows')
    for n in range(1, 109):
        for j in range(8):
            ck(ar[n]['cells'][j] == br[n]['cells'][j], 'unchanged row ' + str(n) + ' column ' + str(j))
    flat = ' '.join(a.split()); repro = ' '.join(rr.split())
    applied = {}
    def applied_check(tag, value):
        ck(value, tag + ' applied'); applied[tag] = bool(value)
    section1 = flat.split('## 1.', 1)[1].split('## 2.', 1)[0]
    section8 = flat.split('## 8.', 1)[1]
    applied_check('N4-443-F1', 'final version 18:54:37Z, 15dec905...' in section1 and '18:56:58Z' in section1 and 'c62e02da' not in section1)
    applied_check('N4-443-F2', 'up to run times, clock stamps and, in three outputs, the stored final rc=0 line' in section8 and 'CONFIRMED in T4-511 and N4-442' in section8)
    applied_check('N4-443-F3', section1.count('a file that keeps growing') == 2 and '91334e80' not in section1 and 'FINAL_ADDENDA_through510.md (387c487f...)' in section1 and 'FINAL_ADDENDA_through512.md (6c05f797...)' in section1)
    rr438 = next(x for x in rr.splitlines() if '| structural | component shares quoted' in x)
    applied_check('N4-443-F4', 'since CONFIRMED independently by T4-509 and accepted in N4-440' in rr438)
    applied_check('N4-438-preserved', flat.count('E_star^2=P2^2+2^14 G1^2+2^18 G0^2') == 2 and flat.count('the weighted G1 term contributes about 72 percent') == 2)
    applied_check('N4-439-preserved', 'residual value or bound' in a and 'are rounded summaries of their cited certificates and are not directed bounds' in flat and 'Ratios use the exact underlying bounds and thresholds' in flat)
    applied_check('T4-512-F1', 'none differs in a mathematical number, a check count or a verdict' in flat and 'reading of team note v72' in flat)
    applied_check('T4-512-F2', applied['N4-443-F2'])
    applied_check('T4-512-C1', 'Static checks of the selected final evidence:' in section8 and 'These validators check hashes and links only' in section8)
    applied_check('T4-512-C2', 'registered scalar and graded correction balls about this reference contain no exact solution (matrix rows 56 and 57)' in section8 and 'its dyadic scheme is also excluded under that scheme\'s stated premises (row 64; T4-512 C2)' in section8)
    saved = get(R / 'research/theory_final_rerun_receipt/verification/result.json')
    ck(saved['counts'] == {'byte_identical': 51, 'timing_only': 15, 'rc_trailer_only': 3} and saved['saved_log_rc0'] == 69, 'saved receipt exact partition')
    ck('comparison of saved files, not the execution, the wall time or the core affinity' in flat, 'execution scope explicit')
    t4 = get(source / 'T4_validation_v07.json')
    ck(t4['check_count'] == len(t4['checks']) == 5302 and t4['failures'] == [], 'saved T4 receipt 5302 check strings and zero failures')
    ck(t4['unique_files_hashed'] == 1077 and t4['source_bindings'] == 793 and t4['postfreeze_source_bindings'] == 336, 'saved T4 receipt provenance counts only')
    ck(sha(source / 'T4_validate_v03.py') == t4['checker_sha256'] == 'a681c4c17e63e448e9c2d8418afd026ae8075ba945d85c25ba406f0f64535f59', 'copied inert T4 checker identity')
    ck(sha(source / 'T4_validation_v07.json') == '14899816ef8d9041b34418d56ac5b39bdc3af3089b7a750371cb29b9f8a1adfd', 'copied T4 receipt identity')
    ck('validation_v07.json, 5302 checks' in section8 and '5302 checks, 1077 files hashed' in repro, 'new report and reproduction receipt counts')
    for topic, number, code in [('rounded_table_peer_acceptance', 441, 'check.py'), ('theory_final_rerun_receipt', 442, 'check.py'), ('final_report_diff', 443, 'check_v02.py')]:
        base = R / 'research' / topic
        line = next(x for x in rr.splitlines() if '(' + 'N4-' + str(number) + ')' in x and str(base.relative_to(R)) in x)
        for p in [base / 'code' / code, base / 'verification/result.json']:
            ck(sha(p) in line, 'reproduce exact N4-' + str(number) + ' ' + str(p.relative_to(base)))
        if number != 443:
            ck(sha(base / 'PROOF.md') in line, 'reproduce exact N4-' + str(number) + ' proof')
        data = get(base / 'verification/result.json')
        ck(str(len(data['checks'])) + ' checks' in line and str(len(data['inputs'])) + (' local bindings' if number == 443 else ' bindings') in line, 'reproduce N4-' + str(number) + ' counts')
    expected = {'AUDIT_SUMMARY.md': 'd9e0c36554b1aff4f5ebe0809133e8397f6cd8f114b16af63091f92fd3863931', 'FINAL_REPORT_NUMERICAL_AUDIT.md': '15dec90541c3708d88dc92c582da16edcdc2c111f04fc6f560c52a34bbf193bc', 'NEXT_AUDIT_PLAN.md': 'b4e5e460f4844e4853a8d99bfdf37de80dace0e2a7c3bcc4921c99ed29d7f934', 'FINAL_EVIDENCE_INDEX_v03.json': 'a66ac924b3d283b883b9a1846eca00eaaba1799f1bd26f424a011527388d15d5'}
    for name, h in expected.items():
        ck(sha(R / name) == h, 'main freeze unchanged ' + name)
    inputs = dict(m['inputs'])
    for p in [Path(__file__), B / 'verification/PROOF_FIRST.json']:
        inputs[str(p.relative_to(R))] = sha(p)
    result = {'utc': datetime.now(timezone.utc).isoformat(), 'started_utc': start, 'elapsed_seconds': time.monotonic() - tick, 'inputs': inputs, 'checks': checks, 'check_count': len(checks), 'target_report_sha256': sha(source / 'report1914.md'), 'target_reproduce_sha256': sha(source / 'reproduce1914.md'), 'report_acquired_utc': '2026-10-29T19:14:19.330764+00:00', 'unchanged_expanded_rows': 108, 'unchanged_table_cells': 864, 'applied_repairs': applied, 'T4_saved_metadata_only': {'checks': 5302, 'unique_files': 1077, 'fresh_underlying_file_check': False}, 'verdict': 'CONFIRMED finite repair acceptance at acquisition time; future final report and unlisted claims OPEN', 'peer_code_executed': False, 'candidate_verdict_changes': False, 'new_numerical_integration': False}
    with target.open('x') as f:
        json.dump(result, f, indent=2); f.write('\n')
    print(result['utc'], len(checks), 'checks', len(inputs), 'bindings', sha(target), result['elapsed_seconds'])
if __name__ == '__main__':
    main()
