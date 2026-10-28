"""Nodal remainders for the closed-form bound of C via Theorem 3.7 (all groups).

Theorem 3.7 reads C_a <= S_a(delta) + R37(a), with delta = 1/64,
  S_a(delta) = 2 a_2 delta^a/a + (1+2 delta)^a delta^2/(2(1-delta)^2),
  R37(a) = sec(pi/64) max_j (paired local circles + middle circles + exterior circles)(phi_j).
Groups 0, 1 and 7: R37 is merged here from the chunks in local/, mid/ (groups 0, 1), local7/, mid7/ (group 7) and the
exterior certificates data/far2_g0.json, data/far2_g1.json, data/far_a0.json (exponent 0, plans of group 0),
data/far2_g7.json; this includes the node a = 0.
Groups 2-6: R37_i = upper(U37_i) - lower(S_{a_i}), from the nodal values of the uniform comparison (pass 3).
Each value is rounded up to 10 decimals.  Output: data/remainders37.json."""
from flint import arb, fmpq, ctx
from fractions import Fraction as F
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
import json, glob, hashlib, sys
ctx.prec = 200
ROOT = Path(__file__).resolve().parents[1]
def q(f): return arb(fmpq(f.numerator, f.denominator))
def up10(x):
    return F(Decimal(x.upper().str(40, radius=False)).quantize(Decimal('1e-10'), rounding=ROUND_CEILING))
nodes = json.load(open(ROOT / 'data/nodes2.json'))
DELTA = F(1, 64)
def a2(a): return 2 ** (1 + a / 2) / (arb.pi() * (a + 2))
def S(x):
    a = q(x); d = q(DELTA)
    return 2 * a2(a) * d ** a / a + (1 + 2 * d) ** a * d ** 2 / (2 * (1 - d) ** 2)

# middle circles: exact coverage of the 512 radial rows, common parameters and source hashes
def mid_merge(folder):
    mch = [json.load(open(f)) for f in sorted(glob.glob(str(ROOT / folder / 'n512_*.json')))]
    keys = ['precision_bits', 'angles_per_half', 'radial_cells', 'phase_intervals', 'integer_unit', 'plan_trials', 'groups', 'source_hashes']
    for c in mch:
        for k in keys: assert c[k] == mch[0][k], k
    for name, h in mch[0]['source_hashes'].items():
        assert hashlib.sha256(open(ROOT / 'code' / name, 'rb').read()).hexdigest() == h, name
    nr = mch[0]['radial_cells']; cov = [0] * nr
    for c in mch:
        for r in range(c['row_start'], c['row_stop']): cov[r] += 1
    assert cov == [1] * nr, 'middle rows not covered exactly once'
    mid = {}
    for c in mch:
        for r in c['rows']:
            k = (F(r['plan_reference_alpha']), F(r['alpha'])); v = [arb(y) for y in r['middle_phase_intervals']]
            mid[k] = v if k not in mid else [s + t for s, t in zip(mid[k], v)]
    return mid
mid = mid_merge('mid'); mid7 = mid_merge('mid7'); assert not set(mid) & set(mid7); mid.update(mid7)

def local(x, folder):
    name = str(x).replace('/', '_')
    ch = [json.load(open(f)) for f in sorted(glob.glob(str(ROOT / folder / f'r*_{name}.json')))]
    assert ch and all(F(c['alpha']) == x for c in ch)
    keys = ['alpha', 'precision_bits', 'angles_per_circle', 'radial_cells', 'phase_intervals', 'delta', 'integer_unit', 'source_hashes']
    for c in ch:
        for k in keys: assert c[k] == ch[0][k], k
    for name_, h in ch[0]['source_hashes'].items():
        assert hashlib.sha256(open(ROOT / 'code' / name_, 'rb').read()).hexdigest() == h, name_
    assert F(ch[0]['delta']) == DELTA
    nr = ch[0]['radial_cells']; m = ch[0]['phase_intervals']; cov = [[0] * (m + 1) for _ in range(nr)]
    tot = [arb(0) for _ in range(m + 1)]
    for c in ch:
        assert set(map(int, c['partial_phase_intervals'])) == set(range(c['phase_start'], c['phase_stop']))
        for r in range(c['row_start'], c['row_stop']):
            for j in range(c['phase_start'], c['phase_stop']): cov[r][j] += 1
        for j, v in c['partial_phase_intervals'].items(): tot[int(j)] += arb(v)
    assert all(v == 1 for row in cov for v in row), 'local rows/phases not covered exactly once'
    if x > 0:
        for c in ch: assert S(x).overlaps(arb(c['small_disk_upper']))
    else:
        for c in ch: assert c['small_disk_upper'] is None
    return m, tot

out = {'0': [], '1': [], '7': []}
for gi, farfiles, lf in ((0, ['data/far_a0.json', 'data/far2_g0.json'], 'local'), (1, ['data/far2_g1.json'], 'local'),
                         (7, ['data/far2_g7.json'], 'local7')):
    g = nodes['groups'][gi]; ref = F(g['far_ref']); fr = {}
    for fn in farfiles:
        d = json.load(open(ROOT / fn)); assert F(d['plan_reference_alpha']) == ref and d['phase_intervals'] == 16
        for r in d['rows']:
            x = F(r['alpha'])
            if x in fr: assert fr[x] == r['far_phase_intervals'], 'exterior rows differ'   # the 1/200 row occurs twice
            fr[x] = r['far_phase_intervals']
    xs = ([F(0)] if gi == 0 else []) + [F(t) for t in g['upper_nodes']]
    for x in xs:
        m, lt = local(x, lf); mv = mid[(ref, x)]; fv = [arb(z) for z in fr[x]]
        assert m == 16 and len(lt) == len(mv) == len(fv) == m + 1
        vals = [s + t + u for s, t, u in zip(lt, mv, fv)]
        mx = vals[0]
        for v in vals[1:]: mx = arb.max(mx, v)
        R = mx / (arb.pi() / (4 * m)).cos()
        out[str(gi)].append(dict(alpha=str(x), R=str(up10(R)), kind='thm37',
                                 C_upper_thm37=None if x == 0 else float((S(x) + R).upper())))
p37 = json.load(open(ROOT / 'data/uniform_result_thm37_pass3.json'))['nodal_upper']
p35 = json.load(open(ROOT / 'data/uniform_result_thm35_pass3.json'))['nodal_upper']
for gi in range(2, 7):
    out[str(gi)] = [dict(alpha=x, R=str(up10(arb(v) - S(F(x)).lower())), kind='thm37') for x, v in p37[str(gi)]['C'].items()]
    out[str(gi)].sort(key=lambda r: F(r['alpha']))
for r in out['7']:   # comparison only: the Theorem 3.5 value at the same node
    r['C_upper_thm35'] = float(arb(p35['7']['C'][r['alpha']]).upper())
for gi in range(8):
    xs = [F(r['alpha']) for r in out[str(gi)]]; g = nodes['groups'][gi]
    assert xs == ([F(0)] if gi == 0 else []) + [F(t) for t in g['upper_nodes']], gi
src = ['code/nodes37.py', 'data/nodes2.json', 'data/far_a0.json', 'data/far2_g0.json', 'data/far2_g1.json', 'data/far2_g7.json',
       'data/uniform_result_thm37_pass3.json', 'data/uniform_result_thm35_pass3.json']
res = dict(method=__doc__, delta=str(DELTA), groups={str(i): out[str(i)] for i in range(8)},
           source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in src})
(ROOT / 'data/remainders37.json').write_text(json.dumps(res, indent=1) + '\n')
for gi in ('0', '1', '7'):
    for r in out[gi]: print(gi, r['alpha'], r['R'], r['C_upper_thm37'])
