"""Theorem 3.6 upper bounds for D at alpha = 3/10, 1/2, 3/4, 9/10 (the accepted V168 bounds) with the pole-disk (cross)
integral X_a taken from the finer cross-disk certificate on 2048 x 2048 cells (same certifier, unchanged source).

Per phase j the V168 bound is D_a <= nearD_a + sec(pi/64) max_j U_j with U_j = upper(W_j + X_j + E_j) - g_j, where W_j is the
middle-circle interval of data/middle_circle_certificate_n512.json, X_j the cross interval, E_j the exterior interval of
data/far_circle_certificate_fine.json and g_j >= 0 the accepted middle-arc residual gain (V168). Here U_j is recomputed from the
same W_j, E_j and g_j with the new X_j. No transport plan, mass or gain is recomputed.

Two checks: (1) with the old cross intervals the recomputed U_j are at most the accepted D_phase_upper of V168, and the
resulting bound is at most the accepted safe_upper_D; (2) a second, independent upper bound per phase, obtained from the accepted
D_phase_upper by subtracting the exact upper endpoint c + r of the old printed cross ball and adding that of the new one, is
reported and must be at least the first (it is valid because the accepted value was formed from the arb ball of the printed
old cross string, whose upper endpoint is at least c + r).
Pending variants (not accepted): the phase interpolation H_delta in place of sec * max, and 1/2 - eta_a in place of 1/2.
Output: results/v168x.json."""
from flint import arb, fmpq, ctx
from fractions import Fraction as Q
from decimal import Decimal, ROUND_CEILING
from pathlib import Path
from datetime import datetime, timezone
import json, re, hashlib
ctx.prec = 256
HERE = Path(__file__).resolve().parent
VER = Path('the verification work')
if not VER.exists(): VER = HERE.parent   # inside the accompanying artifacts
BASE = VER / '08_improved_upper_bounds/middle_circle_transport/balanced_residual'
XC = HERE / 'data' / 'cross_disk_certificate_2048.json'
ALPHAS = ['3/10', '1/2', '3/4', '9/10']
M = 16
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def load(p): return json.load(open(p))
def qa(x): return arb(fmpq(x.numerator, x.denominator))
def upq(x): return Q(str(x.upper().fmpq()))
def ends(t):
    m = re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]', t); assert m, t
    c, r = map(Q, m.groups()); assert r >= 0; return c - r, c + r
def ceil10(q):
    k = -((-q * 10 ** 10).__floor__()); return f'{k // 10 ** 10}.{k % 10 ** 10:010d}'
def up(x, places):
    return str(Decimal(x.upper().str(60, radius=False)).quantize(Decimal(10) ** -places, rounding=ROUND_CEILING))
def A(a): return ((a + 2) / 2).gamma() / (2 * arb.pi().sqrt() * ((a + 3) / 2).gamma())
def nearD(a): return 2 * A(a) * arb(2) ** (-a) / a + arb(1) / 2
def eta(a): return arb(82) / 321489 * a * (1 - a) * (arb(11) / 9) ** (a - 2)
sources = {}
acc = load(BASE / 'verification/accepted.json'); assert acc['verdict'] == 'CONFIRMED' and acc['ledger'] == 'V168'
aud = load(BASE / 'verification/independent_audit.json')
assert acc['sha256']['08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/independent_audit.json'] == sha(BASE / 'verification/independent_audit.json')
for p in [BASE / 'verification/accepted.json', BASE / 'verification/independent_audit.json']: sources[str(p)] = sha(p)
mid = load(VER / 'data/middle_circle_certificate_n512.json'); far = load(VER / 'data/far_circle_certificate_fine.json')
old = load(VER / 'data/cross_disk_certificate.json'); new = load(XC)
comp = load(VER / 'data/middle_composite_upper_n512.json')
for n in ['data/middle_circle_certificate_n512.json', 'data/far_circle_certificate_fine.json', 'data/cross_disk_certificate.json']:
    assert comp['input_sha256'][n] == sha(VER / n), n; sources[str(VER / n)] = sha(VER / n)
assert new['phase_intervals'] == old['phase_intervals'] == mid['phase_intervals'] == far['phase_intervals'] == M
assert new['cells_per_axis'] == 2048 and old['cells_per_axis'] == 512 and new['precision_bits'] == old['precision_bits'] == 160
assert new['source_hashes'] == old['source_hashes']
for n, h in new['source_hashes'].items(): assert sha(HERE / n) == h, n; sources[str(HERE / n)] = h
sources[str(XC)] = sha(XC)
W = {r['alpha']: r['middle_phase_intervals'] for r in mid['rows']}
E = {r['alpha']: r['far_phase_intervals'] for r in far['rows']}
X0 = {r['alpha']: r['cross_phase_intervals'] for r in old['rows']}
X1 = {r['alpha']: r['cross_phase_intervals'] for r in new['rows']}
sec = 1 / (arb.pi() / (4 * M)).cos(); dl = arb.pi() / (2 * M)
def H(u, v):
    """exact maximum of the sine interpolation of adjacent node bounds (pending: phase interpolation, not yet accepted)"""
    u = arb(u.upper()); v = arb(v.upper())
    if (v - u * dl.cos()) < 0: return u
    if (u - v * dl.cos()) < 0: return v
    amp = (u * u + v * v - 2 * u * v * dl.cos()).sqrt() / dl.sin()
    return amp if amp.upper() < (sec * arb.max(u, v)).upper() else sec * arb.max(u, v)
rows = []
for r in aud['rows']:
    a = r['alpha']; assert a in ALPHAS
    g = [Q(z['accepted_gain']) for z in r['residual_checks']]; assert len(g) == M + 1 and all(x >= 0 for x in g)
    DP = [Q(x) for x in r['D_phase_upper']]
    # check (1): the old cross reproduces the accepted phase bounds from below
    U0 = [upq(arb(w) + arb(x) + arb(e)) - gg for w, x, e, gg in zip(W[a], X0[a], E[a], g)]
    assert all(u <= d for u, d in zip(U0, DP)), a
    U = [upq(arb(w) + arb(x) + arb(e)) - gg for w, x, e, gg in zip(W[a], X1[a], E[a], g)]
    # check (2): independent phase bounds by exact substitution of the cross upper endpoints
    U2 = [d - ends(x0)[1] + ends(x1)[1] for d, x0, x1 in zip(DP, X0[a], X1[a])]
    assert all(u <= v for u, v in zip(U, U2)), a
    al = arb(fmpq(*map(int, a.split('/'))))
    nd = nearD(al)
    assert ends(r['upper_D']['display'])[1] >= upq(nd + sec * qa(max(U0)))
    D = nd + sec * qa(max(U)); D2 = nd + sec * qa(max(U2))
    assert Q(ceil10(upq(nd + sec * qa(max(U0))))) <= Q(r['safe_upper_D'])
    hx = H(qa(U[0]), qa(U[1]))
    for j in range(1, M): hx = arb.max(hx, H(qa(U[j]), qa(U[j + 1])))
    DH = nd + hx; DE = D - eta(al); DHE = DH - eta(al)
    jw = max(range(M + 1), key=lambda j: U[j])
    rows.append(dict(alpha=a, old_safe_upper_D=r['safe_upper_D'], safe_upper_D=ceil10(upq(D)), D_upper_interval=D.str(50, more=True),
                     check_substitution_upper_D=ceil10(upq(D2)), worst_phase=jw, phase_upper=[str(u) for u in U],
                     phase_upper_display=[up(qa(u), 10) for u in U],
                     cross_at_worst_phase=dict(old=X0[a][jw], new=X1[a][jw]),
                     pending_interpolated_D_upper=ceil10(upq(DH)), pending_eta_D_upper=ceil10(upq(DE)),
                     pending_interpolated_eta_D_upper=ceil10(upq(DHE))))
    print(a, 'old', r['safe_upper_D'], 'new', ceil10(upq(D)), 'subst', ceil10(upq(D2)), 'worst', jw,
          'H', ceil10(upq(DH)), 'eta', ceil10(upq(DE)), 'H+eta', ceil10(upq(DHE)))
sources[str(Path(__file__))] = sha(Path(__file__))
out = dict(time_utc=datetime.now(timezone.utc).isoformat(), method='Theorem 3.6: V168 phase bounds with the cross term from 2048 x 2048 cells',
           phase_intervals=M, precision_bits=ctx.prec, rows=rows, source_sha256=sources,
           verdict='Lead computation; awaiting verifier audit. The pending_* values use the not yet accepted phase interpolation and eta.')
(HERE / 'results').mkdir(exist_ok=True)
(HERE / 'results' / 'v168x.json').write_text(json.dumps(out, indent=2) + '\n')
