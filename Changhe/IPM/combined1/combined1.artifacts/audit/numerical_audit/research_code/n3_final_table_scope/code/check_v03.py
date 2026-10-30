"""Check frozen component statuses and the already accepted007 Q3 display."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import json, re, time

R = Path(__file__).resolve().parents[3]
B = R / 'research/n3_final_table_scope'
def sha(raw): return sha256(raw).hexdigest()
def interval(text):
    match = re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]', str(text))
    if match:
        mid, rad = map(Q, match.groups())
        assert rad >= 0
        return mid-rad, mid+rad
    value = Q(text)
    return value, value

def main():
    start = time.monotonic()
    checks, inputs = {}, {}
    def ck(name, value):
        checks[name] = bool(value)
        assert value, name
    def bind(path, expected=None):
        path = B / path
        raw = path.read_bytes()
        if expected: assert sha(raw) == expected, path
        inputs[str(path.relative_to(R))] = sha(raw)
        return raw
    prep = json.loads(bind('verification/PREPARE.json'))
    bind('PROOF.md', prep['proof_sha256'])
    ck('proof before checker', not prep['checker_exists'])
    bind('code/check.py')
    bind('code/check_v02.py')
    bind('code/check_v03.py')
    bind('DISPLAY_PROOF_v02.md')
    bind('PARSING_PROOF_v03.md')
    manifest = json.loads(bind('source/MANIFEST.json', prep['manifest_sha256']))
    data = {}
    for entry in manifest:
        raw = bind('source/'+entry['local'], entry['sha256'])
        ck('byte length '+entry['local'], len(raw) == entry['bytes'])
        data[entry['local']] = raw.decode()
    def read(name): return json.loads(data[name])
    table = data['N3_FINAL_TABLES.md']
    qrow = next(line for line in table.splitlines() if line.startswith('| Q3 ='))
    mrow = next(line for line in table.splitlines() if line.startswith('| C1-A2-Mpen2 |'))
    crow = next(line for line in table.splitlines() if line.startswith('| C1-N1-001-refit860-jabs |'))
    ck('frozen007 corrected label', 'CONFIRMED (N4-166' in qrow)
    ck('frozen Mpen2 broad citation', 'CONFIRMED (N4-024/026 package)' in mrow)
    ck('frozen001 broad citation', 'CONFIRMED (N4-028:' in crow)
    for n in [24, 26]:
        text = data[f'N4-{n:03d}.md']
        ck(f'{n} d2 claim', 'd2' in text and 'Mpen2' not in text and 'CONFIRMED' in text)
    ck('060 explicit limited scope',
       'No Mpen2 Hdot^-1, P2 or Q3 claim is established by this check' in data['N4-060.md'])
    ck('028 no finite norm', 'No full-plane finite norm is assigned.' in data['N4-028.md'])
    ck('068 unreproduced', 'OPEN pending independent numerical reproduction' in data['N4-068.md'])
    own, comp = read('007_full.json'), read('007_comparison.json')
    ck('166 complete acceptance', 'CONFIRMED for the complete007 Q3' in data['N4-166.md'])
    ck('007 full exact accepted hash', sha(data['007_full.json'].encode()) ==
       'ccecb46f06398c1883065e68c2141607f430ff7f5edc903d3341b9b49aa2543a')
    ck('007 comparison exact accepted hash', sha(data['007_comparison.json'].encode()) ==
       '60324957509a9b0697c2ac30a0a74edde42f3c8d5d3c34f4caf27b4b0f64f42b')
    ck('007 complete', own['complete'] and not own['missing_modes'])
    ck('007 exact endpoints', own['norm_lower_ball'] == comp['own_lower_ball'] and
       own['norm_upper_ball'] == comp['own_upper_ball'])
    fields = [s.strip() for s in qrow.strip('|').split(' | ')]
    lo, hi = Q(fields[1]), Q(fields[2])
    ck('007 directed table endpoints', lo < interval(own['norm_lower_ball'])[0] and
       hi > interval(own['norm_upper_ball'])[1])
    ck('Mpen2 accepted comparison hash', sha(data['Mpen2_comparison.json'].encode()) ==
       'be8e0ca17a5718313f3b5f714c63a89d3a8415d708d34c93498638232a0c0a2c')
    ck('001 accepted sector hash', sha(data['001_sectors.json'].encode()) ==
       '7c523fc56a2f6ac8cd54b74d8a6c3103c5022e6cf226172081c74d9354b64222')
    for p, expected in inputs.items():
        assert sha((R/p).read_bytes()) == expected, p
    result = {
        'utc': datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds': time.monotonic()-start,
        'checks_passed': len(checks), 'checks': checks, 'inputs': inputs,
        'table_rows': {'007_Q3': qrow, 'Mpen2': mrow, '001': crow},
        'verdicts': {
            '007_Q3_value': 'CONFIRMED by accepted166; printed short endpoints outward',
            '007_Q3_current_status': 'CONFIRMED repaired in frozen15:06:15 table',
            'Mpen2_024_026_blanket_support': 'REFUTED; G0/G1 supported by060',
            '001_028_finite_P2_Q3_support': 'REFUTED',
            'uncited_finite_components': 'OPEN; no numerical refutation',
            'new_mathematics': 'none'
        }}
    (B/'verification/result_v03.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['utc', 'elapsed_seconds', 'checks_passed', 'verdicts']}))

if __name__ == '__main__': main()
