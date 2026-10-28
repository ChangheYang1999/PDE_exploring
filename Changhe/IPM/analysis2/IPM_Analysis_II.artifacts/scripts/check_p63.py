"""Third computation for verification topic 63 (consolidated audit of the conditional weighted inverse and nonlinear
theorem at s = 3*2^-21, r0 = 5*2^-27, eta = 2^-30). Exact rational arithmetic only; every comparison involving
sqrt(s) is squared after both sides are shown positive. Written from the statement in topic 63; no verifier code
is imported.

Checks: the exponent c of the original checkpoint and 9/5 < c < 37/20; beta = 1/20 - 2^13 s - 400 r0/sqrt(s) >
6283/245760 > 1/40 (so the high inverse bound is below 40); 9325421/1200 < 2^13; the low rate 1/5 - 12 * 4 r0/sqrt(s)
> 1/6; 40 eta = r0; the contraction factor 6 * 2048 r0/sqrt(s) = 15/(16 sqrt 6), its square 75/512 < 4/25; the
slope variation 4 r0/sqrt(s) < 2^-12; the output constant 40 * 146/sqrt(s) < 2^23; and the first-jet identity
(A_k h)_y(0) = c[k] h_y(0) + a0 c[h] under c + c[rho] = 1, with (B_k h)_y(0) = c[k] h_y(0), by symbolic linear jets.

Usage: python3 check_p63.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
src = ROOT.parents[1] / 'source/case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json'
c = Q(json.loads(src.read_text())['cl'])
s, r0, eta = Q(3, 2 ** 21), Q(5, 2 ** 27), Q(1, 2 ** 30)


def lt_sqrt(a, b, x):
    """a < b sqrt(x) for a, b > 0."""
    assert a > 0 and b > 0
    return a * a < b * b * x


out = {'inputs': {'source': sha(src)}, 'c': str(c)}
out['9/5<c<37/20'] = Q(9, 5) < c < Q(37, 20) and c == Q(4076476460239181, 2251799813685248)
# beta > m  <=>  400 r0 / sqrt(s) < 1/20 - 2^13 s - m  <=>  400 r0 < (1/20 - 2^13 s - m) sqrt(s)
m = Q(6283, 245760)
out['beta>6283/245760'] = lt_sqrt(400 * r0, Q(1, 20) - 2 ** 13 * s - m, s)
out['6283/245760>1/40'] = m > Q(1, 40)
out['9325421/1200<2^13'] = Q(9325421, 1200) < 2 ** 13
out['high_bound_1/beta<40'] = out['beta>6283/245760'] and m > Q(1, 40)
out['low_rate>1/6'] = lt_sqrt(12 * 4 * r0, Q(1, 5) - Q(1, 6), s)
out['40eta=r0'] = 40 * eta == r0
k = 6 * 2048 * r0                                         # contraction factor k/sqrt(s)
out['contraction=15/(16sqrt6)'] = k * k / s == Q(225, 256 * 6)
out['contraction^2=75/512<4/25'] = k * k / s == Q(75, 512) and Q(75, 512) < Q(4, 25)
out['slope_variation<2^-12'] = lt_sqrt(4 * r0, Q(1, 2 ** 12), s)
out['output_constant<2^23'] = lt_sqrt(40 * 146, Q(2 ** 23), s)
# first-jet identity with linear jets: h = hy*y + o(|X|) (even in x, odd in y), V_k = DV(0) X + o, U[h] = DU[h](0) X + o
x, y, hy, a0, cc, cr, ck, ch, p, q = sp.symbols('x y hy a0 cc crho ck ch p q')
# parity: U_1 is odd in x, even in y ... at the linear level DU(0) is diagonal with entries (-c[.], c[.]) by
# incompressibility; rho_bar = a0 y + o, D rho_bar(0) = (0, a0)
V = sp.Matrix([cc * x + (-cr - ck) * x, cc * y + (cr + ck) * y])
h = hy * y
Dh = sp.Matrix([sp.diff(h, x), sp.diff(h, y)])
Uh = sp.Matrix([-ch * x, ch * y]); Drho = sp.Matrix([0, a0])
Ah = (V.T * Dh)[0] - h + (Uh.T * Drho)[0]
jet = sp.diff(Ah, y).subs({x: 0, y: 0})
out['A_y(0)=c[k]h_y(0)+a0c[h]'] = sp.simplify(jet.subs(cc, 1 - cr) - (ck * hy + a0 * ch)) == 0
Bh = Ah - ch * (x * 0 + y * a0)                          # X . D rho_bar = a0 y + o
out['B_y(0)=c[k]h_y(0)'] = sp.simplify(sp.diff(Bh, y).subs({x: 0, y: 0}).subs(cc, 1 - cr) - ck * hy) == 0
print(out)
assert all(v for kk, v in out.items() if isinstance(v, bool))
out['all_pass'] = True
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2, default=bool) + '\n'); print('DONE')
