"""Theorem 3.6 upper bounds for D at alpha = 1/5 and 99/100 from the direct Theorem 3.7 certificates (lead table37), with the
pole-disk (cross) integral X_a from the finer cross-disk certificate on 4096 x 4096 cells (same certifier, unchanged source).
Otherwise identical to combine_d36.py.

Theorem 3.6 reads D_a <= 2^(1-a) A_a/a + 1/2 + sec(pi/(4m)) max_j (W_a + X_a + E_a)(phi_j), m = 16, where
  W_a: middle circles, from the middle chunks of the direct Theorem 3.7 certificates (plans chosen at the exponent),
       lowered phase by phase by the accepted middle-arc residual gains of the same certificates;
  X_a: pole-disk (cross) integral of Theorem 3.4, from data/cross_disk_certificate_4096.json (4096 cells per axis);
  E_a: exterior circles, the smaller at each phase of the two accepted exterior-circle certificates (the one of the direct
       certificates and the verifier's fine one); each is an upper bound for the exterior term at that phase.
No new transport plan and no new mass is computed here: this is a recombination of accepted interval data.
Output: results/d36x4096.json."""
from flint import arb, fmpq, ctx
from fractions import Fraction as F
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from datetime import datetime, timezone
import json, glob, hashlib
ctx.prec = 256
HERE = Path(__file__).resolve().parent
VER = Path('the verification work')
if not VER.exists(): VER = HERE.parent   # inside the accompanying artifacts
T37 = HERE.parent / ('table37' if (HERE.parent / 'table37').exists() else 'lead_table37')
XC = HERE / 'data' / 'cross_disk_certificate_4096.json'
MR = VER / '08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification'
ALPHAS = [F(1, 5), F(99, 100)]
M = 16
def q(f): return arb(fmpq(f.numerator, f.denominator))
def up(x, places):
    return str(Decimal(x.upper().str(60, radius=False)).quantize(Decimal(10) ** -places, rounding=ROUND_CEILING))
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def A(a): return ((a + 2) / 2).gamma() / (2 * arb.pi().sqrt() * ((a + 3) / 2).gamma())
def nearD(a): return 2 * A(a) * arb(2) ** (-a) / a + arb(1) / 2
LOG43 = (arb(4) / 3).log()
JJ = arb(653) / 288 - 63 * LOG43 / 8
KK = arb(56627) / 138240 - 729 * LOG43 / 512
assert JJ > arb(7) / 4608 and KK > 0
def eta(a):
    p = a * (1 - a); return JJ * p / 4 + KK * p * (2 - a) * (3 - a) / 16
def eta2(a): return JJ * a * (1 - a) / 4
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
cr = json.load(open(XC)); assert cr['phase_intervals'] == M and cr['cells_per_axis'] == 4096 and cr['precision_bits'] == 160
assert cr['source_hashes'] == json.load(open(VER / 'data/cross_disk_certificate.json'))['source_hashes']
for n, h in cr['source_hashes'].items(): assert sha(HERE / n) == h, n
sources[str(XC)] = sha(XC)
fv = json.load(open(VER / 'data/far_circle_certificate_fine.json')); assert fv['phase_intervals'] == M
for p in ['data/far_circle_certificate_fine.json']: sources[str(VER / p)] = sha(VER / p)
CR = {F(r['alpha']): [arb(x) for x in r['cross_phase_intervals']] for r in cr['rows']}
FV = {F(r['alpha']): [arb(x) for x in r['far_phase_intervals']] for r in fv['rows']}
far_sha = sha(T37 / 'code' / 'far_nodes.py')
sec = 1 / (arb.pi() / (4 * M)).cos(); dl = arb.pi() / (2 * M)
def H(u, v):
    """exact maximum of the sine interpolation of adjacent node bounds (Theorem 3.8, accepted V177)"""
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
    UHE = UH - eta(a); UHE2 = UH - eta2(a)
    rows.append(dict(alpha=str(x), near_D=up(nearD(a), 10), phase_values=[up(v, 10) for v in vals], worst_phase=jmax,
                     parts_at_worst_phase=dict(middle=up(W[jmax], 8), cross=up(X[jmax], 8), exterior=up(E[jmax], 8)),
                     exterior_source=['table37' if a_.upper() <= b_.upper() else 'the verification work fine' for a_, b_ in zip(E1, E2)],
                     D_upper_interval=U.str(50, more=True), safe_upper_D=up(U, 10),
                     interpolated_D_upper=up(UH, 10), pending_interpolated_eta_D_upper=up(UHE, 10),
                     pending_interpolated_eta_quadratic_only_D_upper=up(UHE2, 10), eta_used=up(eta(a), 12)))
    print(x, up(U, 10), 'worst', jmax, 'interp', up(UH, 10), 'interp-eta', up(UHE, 10), 'interp-eta2', up(UHE2, 10))
for p in [Path(__file__)] + [T37 / 'code' / n for n in mch[0]['source_hashes']]: sources[str(p)] = sha(p)
out = dict(time_utc=datetime.now(timezone.utc).isoformat(), method='Theorem 3.6 recombination: middle (direct table37 plans, V171 gains) + cross (4096 cells) + exterior',
           phase_intervals=M, rows=rows, source_sha256=sources,
           verdict='Lead computation; awaiting verifier audit. interpolated_D_upper uses the accepted phase interpolation (V177); pending_* also subtract the not yet accepted eta (V188, V191).')
(HERE / 'results').mkdir(exist_ok=True)
(HERE / 'results' / 'd36x4096.json').write_text(json.dumps(out, indent=2) + '\n')
