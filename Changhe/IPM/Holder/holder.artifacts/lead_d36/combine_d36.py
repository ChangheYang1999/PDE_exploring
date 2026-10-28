"""Theorem 3.6 upper bounds for D at the exponents of the direct Theorem 3.7 certificates (lead table37).

Theorem 3.6 reads D_a <= 2^(1-a) A_a/a + 1/2 + sec(pi/(4m)) max_j (W_a + X_a + E_a)(phi_j), m = 16, where
  W_a: middle circles, from the middle chunks of the direct Theorem 3.7 certificates (plans chosen at the exponent),
       lowered phase by phase by the accepted middle-arc residual gains of the same certificates;
  X_a: pole-disk (cross) integral of Theorem 3.4, from the verifier's cross-disk certificate;
  E_a: exterior circles, the smaller at each phase of the two accepted exterior-circle certificates (the one of the direct
       certificates and the verifier's fine one); each is an upper bound for the exterior term at that phase.
No new transport plan and no new mass is computed here: this is a recombination of accepted interval data.
Output: results/d36.json."""
from flint import arb, fmpq, ctx
from fractions import Fraction as F
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from datetime import datetime, timezone
import json, glob, hashlib
ctx.prec = 256
HERE = Path(__file__).resolve().parent
VER = HERE.parent   # inside the accompanying artifacts
T37 = HERE.parent / ('table37' if (HERE.parent / 'table37').exists() else 'lead_table37')
MR = VER / '08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification'
ALPHAS = [F(1, 1000), F(1, 100), F(1, 20), F(1, 10), F(1, 5), F(99, 100)]
M = 16
def q(f): return arb(fmpq(f.numerator, f.denominator))
def up(x, places):
    return str(Decimal(x.upper().str(60, radius=False)).quantize(Decimal(10) ** -places, rounding=ROUND_CEILING))
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def A(a): return ((a + 2) / 2).gamma() / (2 * arb.pi().sqrt() * ((a + 3) / 2).gamma())
def nearD(a): return 2 * A(a) * arb(2) ** (-a) / a + arb(1) / 2
sources = {}
# middle circles: the same merge and checks as table37.py
mch = [json.load(open(f)) for f in sorted(glob.glob(str(T37 / 'mid' / 'n512_*.json')))]
keys = ['precision_bits', 'angles_per_half', 'radial_cells', 'phase_intervals', 'integer_unit', 'plan_trials', 'groups', 'source_hashes']
for c in mch:
    for k in keys: assert c[k] == mch[0][k], k
for name, h in mch[0]['source_hashes'].items(): assert sha(T37 / 'code' / name) == h, name
assert mch[0]['phase_intervals'] == M and mch[0]['radial_cells'] == 512
cov = [0] * 512
for c in mch:
    for r in range(c['row_start'], c['row_stop']): cov[r] += 1
assert cov == [1] * 512, 'middle rows not covered exactly once'
for f in sorted(glob.glob(str(T37 / 'mid' / 'n512_*.json'))): sources[str(f)] = sha(f)
mid = {}
for c in mch:
    for r in c['rows']:
        k = (F(r['plan_reference_alpha']), F(r['alpha'])); v = [arb(y) for y in r['middle_phase_intervals']]
        mid[k] = v if k not in mid else [s + t for s, t in zip(mid[k], v)]
# accepted middle-arc residual gains (V171)
acc = json.load(open(MR / 'accepted.json')); assert acc['verdict'] == 'CONFIRMED' and acc['ledger'] == 'V171'
aud = json.load(open(MR / 'independent_audit.json'))
sources[str(MR / 'accepted.json')] = sha(MR / 'accepted.json'); sources[str(MR / 'independent_audit.json')] = sha(MR / 'independent_audit.json')
gain = {}
for r in aud['rows']:
    g = [F(x) for x in r['accepted_gains']]; lo = [F(x) for x in r['old_source_lower']]; hi = [F(x) for x in r['new_residual_upper']]
    assert len(g) == M + 1 and all(x >= 0 for x in g)
    assert all(x == max(F(0), a - b) for x, a, b in zip(g, lo, hi)), r['alpha']
    gain[F(r['alpha'])] = g
# pole-disk (cross) integral and the two exterior certificates
cr = json.load(open(VER / 'data/cross_disk_certificate.json')); assert cr['phase_intervals'] == M
fv = json.load(open(VER / 'data/far_circle_certificate_fine.json')); assert fv['phase_intervals'] == M
for p in ['data/cross_disk_certificate.json', 'data/far_circle_certificate_fine.json']: sources[str(VER / p)] = sha(VER / p)
CR = {F(r['alpha']): [arb(x) for x in r['cross_phase_intervals']] for r in cr['rows']}
FV = {F(r['alpha']): [arb(x) for x in r['far_phase_intervals']] for r in fv['rows']}
far_sha = sha(T37 / 'code' / 'far_nodes.py')
sec = 1 / (arb.pi() / (4 * M)).cos(); dl = arb.pi() / (2 * M)
def H(u, v):
    """exact maximum of the sine interpolation of adjacent node bounds (pending: the verification work phase_interpolation, not yet accepted)"""
    u = arb(u.upper()); v = arb(v.upper())   # exact upper endpoints; the bound is increasing in u and v
    if (v - u * dl.cos()) < 0: return u
    if (u - v * dl.cos()) < 0: return v
    amp = (u * u + v * v - 2 * u * v * dl.cos()).sqrt() / dl.sin()
    return amp if amp.upper() < (sec * arb.max(u, v)).upper() else sec * arb.max(u, v)
rows = []
for x in ALPHAS:
    name = str(x).replace('/', '_')
    fd = json.load(open(T37 / 'far' / f'far_{name}.json')); sources[str(T37 / 'far' / f'far_{name}.json')] = sha(T37 / 'far' / f'far_{name}.json')
    assert F(fd['plan_reference_alpha']) == x and fd['phase_intervals'] == M and fd['source_sha256'] == far_sha
    (fr,) = [r['far_phase_intervals'] for r in fd['rows'] if F(r['alpha']) == x]
    E1 = [arb(z) for z in fr]; E2 = FV[x]
    E = [a if a.upper() <= b.upper() else b for a, b in zip(E1, E2)]
    W = [m - q(g) for m, g in zip(mid[(x, x)], gain[x])]
    X = CR[x]
    vals = [w + c + e for w, c, e in zip(W, X, E)]
    mx = vals[0]
    for v in vals[1:]: mx = arb.max(mx, v)
    a = q(x); U = nearD(a) + sec * mx
    jmax = max(range(M + 1), key=lambda j: vals[j].upper())
    hx = H(vals[0], vals[1])
    for j in range(1, M): hx = arb.max(hx, H(vals[j], vals[j + 1]))
    UH = nearD(a) + hx
    rows.append(dict(alpha=str(x), near_D=up(nearD(a), 10), phase_values=[up(v, 10) for v in vals], worst_phase=jmax,
                     parts_at_worst_phase=dict(middle=up(W[jmax], 8), cross=up(X[jmax], 8), exterior=up(E[jmax], 8)),
                     exterior_source=['table37' if a_.upper() <= b_.upper() else 'the verification work fine' for a_, b_ in zip(E1, E2)],
                     D_upper_interval=U.str(50, more=True), safe_upper_D=up(U, 10),
                     pending_interpolated_D_upper=up(UH, 10)))
    print(x, up(U, 10), 'worst', jmax, 'interp (pending)', up(UH, 10))
for p in [Path(__file__)] + [T37 / 'code' / n for n in mch[0]['source_hashes']]: sources[str(p)] = sha(p)
out = dict(time_utc=datetime.now(timezone.utc).isoformat(), method='Theorem 3.6 recombination: middle (direct table37 plans, V171 gains) + cross + exterior',
           phase_intervals=M, rows=rows, source_sha256=sources,
           verdict='Lead computation; awaiting verifier audit. pending_interpolated_D_upper uses the not yet accepted phase interpolation.')
(HERE / 'results').mkdir(exist_ok=True)
(HERE / 'results' / 'd36.json').write_text(json.dumps(out, indent=2) + '\n')
