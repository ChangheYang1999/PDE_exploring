"""Validate the frozen independent cover against N4's completed certificate."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import json, time
from flint import arb, ctx
R = Path(__file__).resolve().parents[3]
B = R / 'research/candidate_background_cover'
P = B / 'peer_review/T4'
C = P / 'research/candidate007_signed_cover'
ctx.prec = 1024
start = time.monotonic()
def H(p):
    h = sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()
def read(p):
    return json.loads(p.read_text())
v = read(C / 'verification/FINAL_VALIDATION.json')
for rel, expected in v['inputs'].items():
    assert H(P / rel) == expected, rel
cover_path = C / 'verification/candidate007_signed_cover_v2.json'
assert H(cover_path) == v['cover_sha256']
d = read(cover_path)
assert d['all_pass'] and not d['pending']
assert d['source_sha256'] == '153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
assert d['precision_bits'] == 1024
rectangles = []
for row in d['accepted']:
    assert row['pass'] and arb(row['schur_lower']) > 0
    a,b,c,e = map(Q, (0,1,-1,1))
    for letter in row['path']:
        if letter == 't': b = (a+b)/2
        elif letter == 'T': a = (a+b)/2
        elif letter == 'z': e = (c+e)/2
        elif letter == 'Z': c = (c+e)/2
        else: raise ValueError(letter)
    rectangles.append((a,b,c,e))
assert len(set(row['path'] for row in d['accepted'])) == len(rectangles)
assert sum(((b-a)*(e-c) for a,b,c,e in rectangles), Q(0)) == 2
pair_count = 0
for i, (a,b,c,e) in enumerate(rectangles):
    for f,g,h,j in rectangles[i+1:]:
        assert max(a,f) >= min(b,g) or max(c,h) >= min(e,j)
        pair_count += 1
seed = read(C / 'verification/candidate007_signed_cover.json')
final_rows = {r['path']: r for r in d['accepted']}
for row in seed['accepted']:
    augmented = dict(row, source_code_sha256=seed['code_sha256'])
    assert final_rows[row['path']] == augmented
own_path = B / 'verification/C1-N1-007-d2w-j7-e2bal_theta_2_25_768.json'
own = read(own_path)
assert own['all_pass'] and not own['pending']
assert arb(v['signed_rate']).overlaps(arb(own['signed_rate_lower']))
assert arb(v['signed_rate']) > 2
out = {'utc': datetime.now(timezone.utc).isoformat(), 'candidate': d['candidate'],
       'status': 'CONFIRMED theta<=2/25; original signed low rate>2',
       'peer_cells': len(rectangles), 'N4_cells': len(own['accepted']),
       'disjoint_interior_pairs': pair_count, 'exact_rectangle_area': '2',
       'seed_rows_preserved': len(seed['accepted']), 'all_recorded_margins_positive': True,
       'signed_rate': v['signed_rate'], 'rate_overlaps_N4': True,
       'peer_validation_sha256': H(C/'verification/FINAL_VALIDATION.json'),
       'peer_cover_sha256': H(cover_path), 'N4_cover_sha256': H(own_path),
       'code_sha256': H(Path(__file__)), 'elapsed_seconds': time.monotonic()-start,
       'scope': 'Acceptance of an independently evaluated complete cover; no high inverse or nonlinear closure.'}
target = B/'verification/T4_007_confirmation.json'
assert not target.exists()
target.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
