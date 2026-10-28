"""Rigorous check of the closed-form bound C_a <= L_C(a) + kappa/(1-a) + c for every 0 < a < 1, with
L_C(a) = 2^(1-a) a_2(a)/a = 4 2^(-a/2)/(pi a (a+2)).
Part 1 (groups 0-7, 0 < a <= 199/200).  Theorem 3.7 gives C_a <= L_C(a) + g(a) + R37(a) with
   g(a) = S_a(delta) - L_C(a) = -2 a_2(a) int_delta^(1/2) u^(a-1) du + (1+2 delta)^a delta^2/(2(1-delta)^2),  delta = 1/64.
   log R37 is convex on each group (fixed plans), so log R37 <= E, the chord through the nodal values of
   data/remainders37.json (at a = 0 by continuity).  Each segment is split into N equal rational pieces [p,q]; exp(E) is
   at most its larger endpoint value, kappa/(1-t)+c >= kappa/(1-p)+c, and g(t) <= g(q) when q <= 7/8 (a_2 and the
   integral are positive and decreasing on [0, 0.885], and (1+2 delta)^a increases); for q > 7/8, g is enclosed by
   ball evaluation on the interval [p,q].
Part 2 (199/200 <= a < 1).  As in the check of Theorem 9.3: 2 a_2 s^a/a < delta' L_C + kappa + c delta' (delta' = 1-a) on M
   closed subintervals with interval exponent arguments (Theorem 3.1 with b = 2^(a+1)/(3 pi)).
Usage: python3 code/check_closed_form37.py kappa c N M"""
from pathlib import Path
import json, sys, hashlib
from fractions import Fraction as Fr
from datetime import datetime, timezone
from flint import arb, ctx, fmpq
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / 'code'))
from check_explicit_bounds import positive_integral
ctx.prec = 256
pi = arb.pi()
def q(x): return arb(fmpq(x.numerator, x.denominator))
kap = Fr(sys.argv[1]); c = Fr(sys.argv[2]); N = int(sys.argv[3]); M = int(sys.argv[4])
d = json.loads((ROOT / 'data/remainders37.json').read_text())
DELTA = q(Fr(d['delta'])); assert Fr(d['delta']) == Fr(1, 64)
def a2(a): return arb(2) ** (1 + a / 2) / (pi * (a + 2))
def g(a):
    integral = (arb(2) ** (-a) - DELTA ** a) / a
    return -2 * a2(a) * integral + (1 + 2 * DELTA) ** a * DELTA ** 2 / (2 * (1 - DELTA) ** 2)
def g_upper(p, qq):
    if qq <= Fr(7, 8): return g(q(qq))
    return g(q(p).union(q(qq)))
G = d['groups']; worst = {}; nseg = 0
assert G['0'][0]['alpha'] == '0' and G['7'][-1]['alpha'] == '199/200'
for gi in map(str, range(8)):
    L = [(Fr(r['alpha']), Fr(r['R']), r['kind']) for r in G[gi]]
    assert all(k == 'thm37' for _, _, k in L)
    if gi != '0': assert L[0][0] == Fr(G[str(int(gi) - 1)][-1]['alpha'])
    for (a, Ra, _), (b, Rb, kind) in zip(L, L[1:]):
        nseg += 1; la = q(Ra).log(); lb = q(Rb).log()
        def ex(t):
            s = (t - a) / (b - a); return ((1 - q(s)) * la + q(s) * lb).exp()
        for i in range(N):
            p = a + (b - a) * Fr(i, N); qq = a + (b - a) * Fr(i + 1, N)
            gu = g_upper(p, qq)
            m = (q(kap) / (1 - q(p)) + q(c)) - (gu + arb.max(ex(p), ex(qq)))
            if not m > 0: print('FAIL', gi, a, b, p, qq, m); sys.exit(1)
            if gi not in worst or m.lower() < worst[gi][0]: worst[gi] = (m.lower(), str(p), str(qq))
lo = Fr(199, 200); worst3 = None
for i in range(M):
    a = q(lo + (1 - lo) * Fr(i, M)).union(q(lo + (1 - lo) * Fr(i + 1, M)))
    a3 = 3 * arb(2) ** a / pi * (3 * positive_integral(a, 0) - 4 * positive_integral(a, 1))
    b = arb(2) ** (a + 1) / (3 * pi); s = (2 * a3 + (1 - a) * b) / (2 * a2(a))
    lhs = 2 * a2(a) * s ** a / a; LC = 2 ** (1 - a) * a2(a) / a
    m = (1 - a) * LC + q(kap) + q(c) * (1 - a) - lhs
    if not m > 0: print('FAIL part 2', i, m); sys.exit(1)
    if worst3 is None or m.lower() < worst3[0]: worst3 = (m.lower(), i)
res = dict(time_utc=datetime.now(timezone.utc).isoformat(), kappa=str(kap), c=str(c), pieces_per_segment=N, segments=nseg,
           min_margin_lower_by_group={k: dict(margin=str(v[0]), piece=[v[1], v[2]]) for k, v in worst.items()},
           end_subintervals=M, part2_min_margin_lower=str(worst3[0]),
           source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in
                          ['data/remainders37.json', 'code/check_closed_form37.py', 'code/check_explicit_bounds.py']},
           verdict='PASS: C_a <= L_C(a) + kappa/(1-a) + c for every 0<a<1, given Theorems 3.1, 3.7 and the nodal certificates.')
(ROOT / 'results' / (f'closed_form37_check_{kap}_{c}'.replace('/', '_') + '.json')).write_text(json.dumps(res, indent=1) + '\n')
print('PASS', res['kappa'], res['c'], {k: float(arb(v['margin'])) for k, v in res['min_margin_lower_by_group'].items()}, float(arb(res['part2_min_margin_lower'])))
