"""Theorem 3.7 upper bounds for C at six exponents of Table 1.

Theorem 3.7 reads C_a <= S_a(delta) + sec(pi/(4m)) max_j (paired local circles + middle circles + exterior circles)(phi_j),
with delta = 1/64, m = 16 and
  S_a(delta) = 2 a_2 delta^a/a + (1+2 delta)^a delta^2/(2(1-delta)^2).
The three terms are merged from the chunks in local/, mid/ and far/ (exact coverage of all radial rows and phases is
checked, together with the hashes of the scripts that produced them).  Output: results/table37.json."""
from flint import arb, fmpq, ctx
from fractions import Fraction as F
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from datetime import datetime, timezone
import json, glob, hashlib
ctx.prec = 200
ROOT = Path(__file__).resolve().parents[1]
ALPHAS = [F(1, 1000), F(1, 100), F(1, 20), F(1, 10), F(1, 5), F(99, 100)]
DELTA = F(1, 64); M = 16
def q(f): return arb(fmpq(f.numerator, f.denominator))
def up(x, places):
    return str(Decimal(x.upper().str(40, radius=False)).quantize(Decimal(10) ** -places, rounding=ROUND_CEILING))
def a2(a): return 2 ** (1 + a / 2) / (arb.pi() * (a + 2))
def S(x):
    a = q(x); d = q(DELTA)
    return 2 * a2(a) * d ** a / a + (1 + 2 * d) ** a * d ** 2 / (2 * (1 - d) ** 2)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

# middle circles: exact coverage of the 512 radial rows, common parameters and source hashes
mch = [json.load(open(f)) for f in sorted(glob.glob(str(ROOT / 'mid' / 'n512_*.json')))]
keys = ['precision_bits', 'angles_per_half', 'radial_cells', 'phase_intervals', 'integer_unit', 'plan_trials', 'groups', 'source_hashes']
for c in mch:
    for k in keys: assert c[k] == mch[0][k], k
for name, h in mch[0]['source_hashes'].items(): assert sha(ROOT / 'code' / name) == h, name
cov = [0] * mch[0]['radial_cells']
for c in mch:
    for r in range(c['row_start'], c['row_stop']): cov[r] += 1
assert cov == [1] * len(cov), 'middle rows not covered exactly once'
mid = {}
for c in mch:
    for r in c['rows']:
        k = (F(r['plan_reference_alpha']), F(r['alpha'])); v = [arb(y) for y in r['middle_phase_intervals']]
        mid[k] = v if k not in mid else [s + t for s, t in zip(mid[k], v)]

def local(x):
    name = str(x).replace('/', '_')
    ch = [json.load(open(f)) for f in sorted(glob.glob(str(ROOT / 'local' / f'r*_{name}.json')))]
    assert ch and all(F(c['alpha']) == x for c in ch)
    keys = ['alpha', 'precision_bits', 'angles_per_circle', 'radial_cells', 'phase_intervals', 'delta', 'integer_unit', 'source_hashes']
    for c in ch:
        for k in keys: assert c[k] == ch[0][k], k
    for name_, h in ch[0]['source_hashes'].items(): assert sha(ROOT / 'code' / name_) == h, name_
    assert F(ch[0]['delta']) == DELTA and ch[0]['phase_intervals'] == M
    nr = ch[0]['radial_cells']; cov = [[0] * (M + 1) for _ in range(nr)]; tot = [arb(0) for _ in range(M + 1)]
    for c in ch:
        assert set(map(int, c['partial_phase_intervals'])) == set(range(c['phase_start'], c['phase_stop']))
        for r in range(c['row_start'], c['row_stop']):
            for j in range(c['phase_start'], c['phase_stop']): cov[r][j] += 1
        for j, v in c['partial_phase_intervals'].items(): tot[int(j)] += arb(v)
        assert S(x).overlaps(arb(c['small_disk_upper']))
    assert all(v == 1 for row in cov for v in row), 'local rows/phases not covered exactly once'
    return tot, ch[0]

rows = []; far_sha = sha(ROOT / 'code' / 'far_nodes.py')
for x in ALPHAS:
    name = str(x).replace('/', '_')
    fd = json.load(open(ROOT / 'far' / f'far_{name}.json'))
    assert F(fd['plan_reference_alpha']) == x and fd['phase_intervals'] == M and fd['source_sha256'] == far_sha
    assert fd['angles'] == 512 and fd['radial_cells'] == 128 and F(fd['umin']) == F(1, 4)
    (fr,) = [r['far_phase_intervals'] for r in fd['rows'] if F(r['alpha']) == x]
    lt, l0 = local(x); mv = mid[(x, x)]; fv = [arb(z) for z in fr]
    assert len(lt) == len(mv) == len(fv) == M + 1
    vals = [s + t + u for s, t, u in zip(lt, mv, fv)]
    mx = vals[0]
    for v in vals[1:]: mx = arb.max(mx, v)
    R = mx / (arb.pi() / (4 * M)).cos(); U = S(x) + R
    jmax = max(range(M + 1), key=lambda j: vals[j].upper())
    rows.append(dict(alpha=str(x), small_disk=up(S(x), 10), remainder=up(R, 10), C_upper=up(U, 10), C_upper_6=up(U, 6),
                     C_upper_minus_2_over_pi_alpha=up(U - 2 / (arb.pi() * q(x)), 10), worst_phase=jmax,
                     parts_at_worst_phase=dict(local=up(lt[jmax], 8), middle=up(mv[jmax], 8), exterior=up(fv[jmax], 8))))
    print(rows[-1])
src = ['code/table37.py', 'code/far_nodes.py', 'code/refl_nodes.py', 'code/local_nodes.py', 'code/mid_nodes.py',
       'code/certify_far_circles.py', 'code/certify_local_circles_greedy.py', 'code/local_circle_greedy.py',
       'code/middle_circle_plan.py', 'code/circle_transport_plan.py']
res = dict(time_utc=datetime.now(timezone.utc).isoformat(), method=__doc__, delta=str(DELTA), phase_intervals=M,
           grids=dict(local='512 cells per circle, 256 radial bins of [delta, 1/2], greedy integer flows',
                      middle='512 cells per half, 512 bins of [0, pi/2], best_plan (17 trials) at the exponent itself',
                      exterior='512 cells, 128 bins of u in [1/4, 1], best_plan (9 trials) at the exponent itself'),
           rows=rows, source_sha256={p: sha(ROOT / p) for p in src},
           verdict='Upper bounds C_a <= C_upper (rounded up), given Theorems 3.5, 3.6 and 3.7 of the report.')
(ROOT / 'results' / 'table37.json').write_text(json.dumps(res, indent=1) + '\n')
