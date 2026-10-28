"""Third computation for verification topic 69 (sharp small-regularity cost of the strain trace).

Written from the statement of topic 69 only; no verifier code is imported. Exact symbolic checks (sympy):
1. The symbols: with h(X) = (2 pi)^-2 int exp(i X.xi) h_hat, b[h] = h_y(0) has symbol i xi_2 and c[h] = d_y R1^2 h(0)
   has symbol i xi_2 (-xi_1^2/|xi|^2); in polar form -i r sin(theta) cos(theta)^2 = -(i r/4)(sin theta + sin 3 theta).
2. The radial integral int_0^inf r^3 (1+r^2)^(-2-s) dr = 1/(2 s (s+1)), the angular integrals pi, pi/4, pi/8, the
   Gram matrix (2), the norms (3), (4) by the Schur complement, and the angular constants A_p = pi/8 and pi/16.
3. The asymptotic constants sqrt(A_p/(8 pi^2)) = 1/(8 sqrt(pi)), 1/(8 sqrt(2 pi)), and their agreement with the
   small-s limits of the exact H^(2+s) norms; the log-divergence coefficient 1/(64 pi) of section 6.
4. The concavity bound (1 + 4 r^2)^(4/5) - 1 <= (16/5) r^2 and the constant 26 * 2^22 < 2^53 of (7).
5. FLOAT: I_s - 1/(2s) stays bounded for s = 2^-k (k = 4..12) with a concrete smooth cutoff, and the radial integral
   of (5) by quadrature at s = 2^-12.

Usage: python3 check_p69.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from pathlib import Path
import sympy as sp
import mpmath
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
out = {}
th, r, s, t, x1, x2 = sp.symbols('theta r s t xi1 xi2', positive=True)
# 1. symbols
lb = sp.I * x2
lc = sp.I * x2 * (-x1 ** 2 / (x1 ** 2 + x2 ** 2))
pol = {x1: r * sp.cos(th), x2: r * sp.sin(th)}
lb_p = sp.simplify(lb.subs(pol)); lc_p = sp.simplify(lc.subs(pol))
chk = {'lb=i r sin': sp.simplify(lb_p - sp.I * r * sp.sin(th)) == 0,
       'lc=-i r sin cos^2': sp.simplify(lc_p + sp.I * r * sp.sin(th) * sp.cos(th) ** 2) == 0,
       'lc=-(i r/4)(sin+sin3)': sp.simplify(sp.expand_trig(lc_p + sp.I * r / 4 * (sp.sin(th) + sp.sin(3 * th)))) == 0,
       'c+b/4 pure harmonic 3': sp.simplify(sp.expand_trig(lc_p + lb_p / 4 + sp.I * r / 4 * sp.sin(3 * th))) == 0}
# 2. radial and angular integrals, Gram matrix
rad = sp.integrate(t * (1 + t) ** (-2 - s), (t, 0, sp.oo), conds='none') / 2
chk['radial=1/(2s(s+1))'] = sp.simplify(rad - 1 / (2 * s * (s + 1))) == 0
ang = lambda f: sp.integrate(f, (th, 0, 2 * sp.pi))
pb, pc = sp.sin(th), -sp.sin(th) * sp.cos(th) ** 2          # symbols / (i r)
G = sp.Matrix(2, 2, lambda i, j: ang([pb, pc][i] * [pb, pc][j]))
chk['angular pi, pi/4, pi/8'] = (G[0, 0] == sp.pi and G[0, 1] == -sp.pi / 4 and G[1, 1] == sp.pi / 8)
Gram = G * rad / (4 * sp.pi ** 2)
target = sp.Matrix([[1, -sp.Rational(1, 4)], [-sp.Rational(1, 4), sp.Rational(1, 8)]]) / (8 * sp.pi * s * (s + 1))
chk['Gram (2)'] = sp.simplify(Gram - target) == sp.zeros(2, 2)
nc = sp.sqrt(Gram[1, 1]); nc0 = sp.sqrt(sp.simplify(Gram[1, 1] - Gram[0, 1] ** 2 / Gram[0, 0]))
chk['norm (3)'] = sp.simplify(nc - 1 / (8 * sp.sqrt(sp.pi * s * (s + 1)))) == 0
chk['norm (4)'] = sp.simplify(nc0 - 1 / (8 * sp.sqrt(2 * sp.pi * s * (s + 1)))) == 0
p3 = sp.sin(3 * th) / 4
chk['b-orthogonal to harmonic 3'] = ang(pb * p3) == 0
chk['Schur = harmonic-3 variance'] = sp.simplify(ang(p3 ** 2) * rad / (4 * sp.pi ** 2) - nc0 ** 2) == 0
Ap = {'c': ang(pc ** 2), 'c+b/4': ang(p3 ** 2), 'b': ang(pb ** 2)}
chk['A_p = pi/8, pi/16, pi'] = Ap == {'c': sp.pi / 8, 'c+b/4': sp.pi / 16, 'b': sp.pi}
# 3. asymptotic constants
lim_c = sp.sqrt(Ap['c'] / (8 * sp.pi ** 2)); lim_c0 = sp.sqrt(Ap['c+b/4'] / (8 * sp.pi ** 2))
chk['limit 1/(8 sqrt pi)'] = sp.simplify(lim_c - 1 / (8 * sp.sqrt(sp.pi))) == 0
chk['limit 1/(8 sqrt(2 pi))'] = sp.simplify(lim_c0 - 1 / (8 * sp.sqrt(2 * sp.pi))) == 0
chk['agrees with exact H^(2+s) limits'] = (sp.limit(sp.sqrt(s) * nc, s, 0) == lim_c and sp.limit(sp.sqrt(s) * nc0, s, 0) == lim_c0)
chk['log coefficient 1/(64 pi)'] = sp.simplify(Ap['c+b/4'] / (4 * sp.pi ** 2) - 1 / (64 * sp.pi)) == 0
# lower sequence pairing signs: (lc/(i r)) * p > 0 in angular mean for both choices of p
chk['pairing c with i p (p = sin cos^2) = pi/8'] = ang(sp.sin(th) * sp.cos(th) ** 2 * sp.sin(th) * sp.cos(th) ** 2) == sp.pi / 8
chk['pairing c with i p (p = sin3/4) = pi/16'] = sp.simplify(ang((sp.sin(th) + sp.sin(3 * th)) / 4 * p3)) == sp.pi / 16
# 4. elementary constants
y = sp.symbols('y', nonnegative=True)
f = 1 + sp.Rational(16, 5) * y - (1 + 4 * y) ** sp.Rational(4, 5)
chk['concavity (16/5)'] = sp.simplify(f.subs(y, 0)) == 0 and sp.simplify(sp.diff(f, y) - (sp.Rational(16, 5) - sp.Rational(16, 5) * (1 + 4 * y) ** sp.Rational(-1, 5))) == 0
chk['26*2^22 < 2^53'] = 26 * 2 ** 22 < 2 ** 53
# 5. FLOAT checks
mpmath.mp.dps = 30
def chi0(rr):
    rr = mpmath.mpf(rr)
    if rr <= 1: return mpmath.mpf(1)
    if rr >= 2: return mpmath.mpf(0)
    a = mpmath.exp(-1 / (rr - 1)); b = mpmath.exp(-1 / (2 - rr)); return b / (a + b)
dev = {}
for k in range(4, 13):
    ss = mpmath.mpf(2) ** -k
    # on r >= 2 put r = e^u: int_(log 2)^inf e^(-2 s u) (1 + e^(-2u))^(-s) du; the main part is exact, the rest decays like e^(-2u)
    L2 = mpmath.log(2)
    tail = mpmath.exp(-2 * ss * L2) / (2 * ss) + mpmath.quad(lambda u: mpmath.exp(-2 * ss * u) * ((1 + mpmath.exp(-2 * u)) ** (-ss) - 1), [L2, 10, 40, mpmath.inf])
    Is = mpmath.quad(lambda rr: (1 - chi0(rr)) ** 2 / rr * (1 + rr * rr) ** (-ss), [1, 2]) + tail
    dev[k] = float(Is - 1 / (2 * ss))
chk['I_s - 1/(2s) bounded (FLOAT)'] = max(abs(v) for v in dev.values()) < 2
ss = mpmath.mpf(2) ** -12
# int_0^inf r^3 (1+r^2)^(-2-s) dr = int_R e^(4u)(1 + e^(2u))^(-2-s) du; on u >= 0 write e^(-2su)(1 + e^(-2u))^(-2-s)
radq = mpmath.quad(lambda u: mpmath.exp(4 * u) * (1 + mpmath.exp(2 * u)) ** (-2 - ss), [-mpmath.inf, -10, 0]) + \
    1 / (2 * ss) + mpmath.quad(lambda u: mpmath.exp(-2 * ss * u) * ((1 + mpmath.exp(-2 * u)) ** (-2 - ss) - 1), [0, 10, 40, mpmath.inf])
chk['radial quadrature at s=2^-12 (FLOAT)'] = abs(radq / (1 / (2 * ss * (1 + ss))) - 1) < 1e-8
out['I_s_minus_1_over_2s_FLOAT'] = dev
out['checks'] = {k: bool(v) for k, v in chk.items()}
out['norms_at_s=2^-12'] = {'c': float(nc.subs(s, sp.Rational(1, 4096))), 'c_on_ker_b': float(nc0.subs(s, sp.Rational(1, 4096)))}
print(json.dumps(out, indent=1))
assert all(out['checks'].values())
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
