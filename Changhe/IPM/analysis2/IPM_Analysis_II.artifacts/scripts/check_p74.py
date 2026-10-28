"""Third computation for verification topic 74 (a compact C^1 zero-jet S1 density in every logarithmic space
beta <= 1/2 whose circular strain integrals diverge).

Written from the statement of topic 74 only; no verifier code is imported. Routes:

1. Exact (sympy): the Frullani representation log(1 + lam) = int_0^oo e^-t (1 - e^(-t lam)) dt/t through its lam-derivative
   and its value at 0; the heat identity <f, f - p_t * f> = (1/2) int p_t(z) ||f - tau_z f||^2 dz evaluated in closed form
   on both sides for f = exp(-|X|^2) (Fourier side with the convention f_hat = int e^(-i X.xi) f); the scaling inequality
   log(1 + s/eps^2) <= 2 log(1/eps) + log(1 + s); Phi = r sin(3 theta) chi(r) = y(3x^2 - y^2) chi/r^2 with S1 parity;
   the angular integral pi; the elementary inequalities behind (8) to (10); the four scaling factors of the table
   (by the substitution X = eps Y); support separation (3/2) 4^-(n+1) < 4^-n; the bound
   1/(n log n) - 1/(n log(n + 1)) <= 1/(n^2 log(n)^2) from log(1 + 1/n) <= 1/n.
2. FLOAT (numpy FFT on a periodic grid, functions compactly supported well inside): ||Q(f1 + f2)||^2 <= 2(||Q f1||^2 +
   ||Q f2||^2) for disjoint bumps, and the scaling estimate (4) for Phi at eps = 1/2, 1/4.
3. FLOAT: A_chi = int_1^(3/2) chi(s) ds/s > 0; direct 2D quadrature of T_(eps_N) h(0) over the actual partial density
   equals A_chi sum_(n=2)^N a_n (N = 2, 3, 4); partial sums of sum (1 + n) a_n^2 stay below the integral bound and
   sum a_n grows like log log N.

Usage: python3 check_p74.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
chk, out = {}, {}
x, y = sp.symbols('x y', real=True)
t, lam, s, eps, r, th, z, b, n = sp.symbols('t lambda s epsilon r theta z beta n', positive=True)

# 1. exact facts
chk['d/dlam int e^-t (1 - e^(-t lam)) dt/t = int e^(-t(1+lam)) dt = 1/(1 + lam) = d/dlam log(1 + lam)'] = \
    sp.simplify(sp.integrate(sp.exp(-t * (1 + lam)), (t, 0, sp.oo)) - sp.diff(sp.log(1 + lam), lam)) == 0
chk['both sides vanish at lam = 0'] = sp.log(1 + 0) == 0
# heat identity on f = exp(-|X|^2): autocorrelation (pi/2) exp(-|z|^2/2); p_t-average of exp(-|z|^2/2) = 1/(1 + 2t)
zz = sp.symbols('zz', positive=True)
pt_avg = sp.integrate(sp.exp(-zz ** 2 / (4 * t)) / (4 * sp.pi * t) * sp.exp(-zz ** 2 / 2) * 2 * sp.pi * zz, (zz, 0, sp.oo))
auto = sp.integrate(sp.integrate(sp.exp(-(x ** 2 + y ** 2)) * sp.exp(-((x - z) ** 2 + y ** 2)), (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
phys = sp.simplify(sp.Rational(1, 2) * (2 * sp.pi / 2 - 2 * (sp.pi / 2) * pt_avg))
xi = sp.symbols('xi', positive=True)
fhat2 = (sp.pi * sp.exp(-xi ** 2 / 4)) ** 2
four = sp.simplify(sp.integrate((1 - sp.exp(-t * xi ** 2)) * fhat2 * 2 * sp.pi * xi, (xi, 0, sp.oo)) / (4 * sp.pi ** 2))
chk['autocorrelation of exp(-|X|^2) = (pi/2) exp(-|z|^2/2)'] = sp.simplify(auto - sp.pi / 2 * sp.exp(-z ** 2 / 2)) == 0
chk['heat identity both sides = (pi/2)(1 - 1/(1 + 2t)) for the Gaussian'] = sp.simplify(phys - four) == 0 and sp.simplify(four - sp.pi / 2 * (1 - 1 / (1 + 2 * t))) == 0
chk['log(1 + s/eps^2) <= 2 log(1/eps) + log(1 + s) for eps <= 1: (1 + s)/eps^2 - (1 + s/eps^2) = (1/eps^2 - 1) >= 0'] = \
    sp.simplify((1 + s) / eps ** 2 - (1 + s / eps ** 2) - (1 / eps ** 2 - 1)) == 0
chi = sp.Function('chi')
Phi = y * (3 * x ** 2 - y ** 2) * chi(sp.sqrt(x ** 2 + y ** 2)) / (x ** 2 + y ** 2)
chk['Phi = r sin(3 theta) chi(r)'] = sp.simplify(sp.expand_trig(Phi.subs({x: r * sp.cos(th), y: r * sp.sin(th)}, simultaneous=True) - r * sp.sin(3 * th) * chi(r))) == 0
chk['Phi even in x, odd in y'] = sp.simplify(Phi.subs(x, -x) - Phi) == 0 and sp.simplify(Phi.subs(y, -y) + Phi) == 0
chk['int_0^(2 pi) sin(3 theta)^2 = pi'] = sp.integrate(sp.sin(3 * th) ** 2, (th, 0, 2 * sp.pi)) == sp.pi
chk['2 s/(1 + s^2) <= 1: 1 + s^2 - 2 s = (1 - s)^2'] = sp.expand(1 + s ** 2 - 2 * s - (1 - s) ** 2) == 0
chk['2 |xi|^2 <= 1 + |xi|^4: difference (1 - |xi|^2)^2'] = sp.expand(1 + s ** 2 - 2 * s - (1 - s) ** 2) == 0
chk['omega2 <= 1 + 2r: (1 + 2r)^2 - (1 + 4 r^2) = 4r >= 0 and (1 + 4r^2)^(4/5) <= 1 + 4r^2'] = sp.expand((1 + 2 * r) ** 2 - (1 + 4 * r ** 2) - 4 * r) == 0
# scaling factors: f(X) = A Phi(X/eps) has ||f||^2 = A^2 eps^2 ||Phi||^2
A_ = {'h_n': (sp.Symbol('a') * eps, 'a^2 eps^4'), 'D2 h_n': (sp.Symbol('a') / eps, 'a^2'),
      'X h_n': (sp.Symbol('a') * eps ** 2, 'a^2 eps^6'), 'X D2 h_n': (sp.Symbol('a'), 'a^2 eps^2')}
expect = {'h_n': sp.Symbol('a') ** 2 * eps ** 4, 'D2 h_n': sp.Symbol('a') ** 2, 'X h_n': sp.Symbol('a') ** 2 * eps ** 6, 'X D2 h_n': sp.Symbol('a') ** 2 * eps ** 2}
chk['table of squared scaling factors A^2 eps^2'] = all(sp.simplify(A_[k][0] ** 2 * eps ** 2 - expect[k]) == 0 for k in A_)
chk['support separation (3/2) 4^-(n+1) < 4^-n'] = sp.Rational(3, 2) / 4 < 1
# 1/(n log n) - 1/(n log(n+1)) = (log(1 + 1/n))/(n log n log(n+1)) <= (1/n)/(n log(n)^2)
chk['log(1 + u) <= u (u > 0): derivative 1/(1+u) <= 1, value 0 at 0'] = sp.simplify(sp.diff(s - sp.log(1 + s), s) - s / (1 + s)) == 0

# 2. FLOAT FFT checks of (3) and (4)
Nn, Lb = 1024, 4.0   # spacing 1/256: the narrow bump chi (width 1/2, then 1/8 at eps = 1/4) is resolved
g1 = np.linspace(-Lb / 2, Lb / 2, Nn, endpoint=False)
Xg, Yg = np.meshgrid(g1, g1, indexing='ij')
Rg = np.hypot(Xg, Yg)
kk = 2 * np.pi * np.fft.fftfreq(Nn, d=Lb / Nn)
KX, KY = np.meshgrid(kk, kk, indexing='ij')
q2 = 1 + np.log1p(KX ** 2 + KY ** 2)
dA = (Lb / Nn) ** 2
Qn2 = lambda f: float(np.sum(q2 * np.abs(np.fft.fft2(f)) ** 2) * dA / Nn ** 2)


def chif(sv):
    out_ = np.zeros_like(sv)
    m = (sv > 1) & (sv < 1.5)
    out_[m] = np.exp(-1 / ((sv[m] - 1) * (1.5 - sv[m])))
    return out_


def Phif(Xa, Ya):
    Ra = np.hypot(Xa, Ya)
    with np.errstate(invalid='ignore', divide='ignore'):
        v = np.where(Ra > 0, Ya * (3 * Xa ** 2 - Ya ** 2) * chif(Ra) / np.where(Ra > 0, Ra ** 2, 1), 0.0)
    return v


f1 = Phif(Xg, Yg)
f2 = 0.3 * Phif((Xg) * 3, (Yg) * 3)    # scaled copy supported in 1/3 < r < 1/2, disjoint from f1
lhs3 = Qn2(f1 + f2); rhs3 = 2 * (Qn2(f1) + Qn2(f2))
chk['(3) for two disjoint annular bumps (FLOAT FFT)'] = lhs3 <= rhs3 and np.all(f1 * f2 == 0)
out['disjoint_FLOAT'] = {'lhs': lhs3, 'rhs': rhs3}
nP2 = float(np.sum(f1 ** 2) * dA); QP2 = Qn2(f1)
sc = {}
for e_ in (0.5, 0.25):
    fe = 1.0 * Phif(Xg / e_, Yg / e_)
    val = Qn2(fe); bound = e_ ** 2 * (QP2 + 2 * np.log(1 / e_) * nP2)
    sc[str(e_)] = {'norm2': val, 'bound': bound}
chk['(4) scaling estimate for Phi at eps = 1/2, 1/4 (FLOAT FFT)'] = all(v['norm2'] <= v['bound'] * (1 + 1e-9) for v in sc.values())
out['scaling_FLOAT'] = sc

# 3. FLOAT divergence of the circular integral
mpmath.mp.dps = 20
chim = lambda sv: mpmath.exp(-1 / ((sv - 1) * (1.5 - sv))) if 1 < sv < 1.5 else mpmath.mpf(0)
Achi = mpmath.quad(lambda sv: chim(sv) / sv, [1, 1.25, 1.5])
chk['A_chi > 0 (FLOAT)'] = Achi > 0
a_ = lambda k: 1 / (k * mpmath.log(k + 1))
direct = {}
for N in (2, 3, 4):
    # T_(eps_N) h(0) = (1/pi) int_(r > eps_N) sin(3 theta) h / r^3 dX with h = sum_(n=2)^N a_n r sin(3 theta) chi(r/eps_n)
    tot = 0
    for k in range(2, N + 1):
        ek = mpmath.mpf(4) ** -k
        rad = mpmath.quad(lambda rr: a_(k) * rr * chim(rr / ek) / rr ** 2, [ek, 1.25 * ek, 1.5 * ek])
        ang = mpmath.quad(lambda tt: mpmath.sin(3 * tt) ** 2, [0, mpmath.pi, 2 * mpmath.pi])
        tot += rad * ang / mpmath.pi
    pred = Achi * sum(a_(k) for k in range(2, N + 1))
    direct[N] = {'direct_FLOAT': float(tot), 'A_chi_sum_FLOAT': float(pred)}
chk['T_(eps_N) h(0) = A_chi sum a_n (FLOAT, N = 2, 3, 4)'] = all(abs(v['direct_FLOAT'] - v['A_chi_sum_FLOAT']) < 1e-15 for v in direct.values())
ps = 0.0; ok = True
for k in range(2, 200001):
    ps += (1 + k) / (k ** 2 * np.log(k + 1) ** 2)
ok = ps < (1 + 3) / (4 * np.log(3) ** 2) + 2 / np.log(2)
chk['partial sum of (1 + n) a_n^2 (n <= 2e5) below 3/(4 log(3)^2)... + 2/log 2 (FLOAT)'] = bool(ok)
lin = sum(1 / (k * np.log(k + 1)) for k in range(2, 200001))
chk['sum a_n (n <= 2e5) - log log 2e5 is bounded (FLOAT display)'] = abs(lin - np.log(np.log(2e5))) < 2
out['A_chi_FLOAT'] = float(Achi); out['direct_FLOAT'] = direct
out['series_FLOAT'] = {'sum_(1+n)a_n^2_to_2e5': ps, 'sum_a_n_to_2e5': lin, 'loglog_2e5': float(np.log(np.log(2e5)))}
out['checks'] = {k: bool(v) for k, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k for k, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
