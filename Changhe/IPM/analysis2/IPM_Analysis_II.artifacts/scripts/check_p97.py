"""Third computation for verification topic 97 (the full absolute jet moment I(h) = int_(r<1) |h - b[h] y| r^-3 dX is
bounded on H_beta exactly for beta > 3/2; a nested C1 construction with b = c = 0 and zero third harmonic lies in every
H_beta and N_(beta,R), beta <= 3/2, and has I(h) = infinity).

Written from the statement of topic 97 only; no verifier code is imported. Routes:

1. Exact (sympy, Fraction): the integral remainder formula e^(iu) - 1 - iu = -int_0^u (u - t) e^(it) dt (so the
   bound u^2/2), |e^(iu) - 1|^2 = 4 sin^2(u/2) (so the bound 2|u| <= 3|u|); the radial integrals defining B(s); the
   prefactor 2 pi (2 pi)^-2 (2 pi) = 1; the limit of s (log s)^(2 beta - 2) times the integrand of (2), equal to
   9/4^beta, so the integrand is integrable at infinity exactly for beta > 3/2; the scaling identities
   D g_n(X) = (D Phi)(X/eps) and F_n_hat(xi) = eps F_hat(eps xi) for g_n = eps Phi(X/eps) (on the stand-in
   Phi = y exp(-r^2)); zero mean and zero first moments of D^2 Phi for a compactly supported stand-in
   Phi = y (1 - r^2)^4; the annulus exponent 4^(k - n) min(4^(2(k - n)), 4^(-4(k - n))) = 4^(-3|k - n|);
   1 + k <= (1 + n)(1 + |k - n|); the kernel sum ||K||_1 < 6/5; (1 + 1/n)^3 <= 27/8 < 4;
   int_2^oo dx/(x log^2 x) = 1/log 2; the multiplier comparison behind (8) as exact differences; the gap conditions
   on chi(r/eps_n); omega2 <= 1 + 2r; the gap contribution 4 log 2 and the double-sum identity; the divergence
   comparison (n - 2)/(n^2 log(n + 1)) >= 1/(3 n log(n + 1)) for n >= 3.
2. FLOAT: the two remainder bounds on a grid; C_beta at beta = 2, 5/2, 3 and the growth of the truncated beta = 3/2
   integral; the bound I(h) <= C_beta ||h||_(H_beta) for h = y exp(-a r^2) (a = 1, 4, 16; exact Fourier transform,
   radial quadrature); the explicit nested construction with the smooth cutoff of the text: h_N on the gaps equals
   -y sum_(m <= n <= N) a_n, b[h_N] = 0, and the gap lower bound of I(h_N) grows without bound;
   sup |D q_(3/2)| finite on a grid.

Usage: python3 check_p97.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath as mp
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t00 = time.monotonic()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
chk, out = {}, {}

# 1. exact
u, t, s, r, th, x, y, eps, beta = sp.symbols('u t s r theta x y epsilon beta', positive=True)
rem = -sp.integrate((u - t) * sp.exp(sp.I * t), (t, 0, u))
chk['97 (a): e^(iu) - 1 - iu = -int_0^u (u - t) e^(it) dt, whose modulus is at most int_0^u (u - t) dt = u^2/2'] = \
    sp.simplify(sp.expand(rem - (sp.exp(sp.I * u) - 1 - sp.I * u))) == 0 and sp.integrate(u - t, (t, 0, u)) == u ** 2 / 2
chk['97 (a): |e^(iu) - 1|^2 = 4 sin^2(u/2) <= u^2, so |e^(iu) - 1 - iu| <= 2|u| <= 3|u|'] = \
    sp.simplify(sp.expand_complex((sp.exp(sp.I * u) - 1) * (sp.exp(-sp.I * u) - 1)) - 4 * sp.sin(u / 2) ** 2) == 0
B_lo = sp.integrate(s ** 2 * r ** 2 / 2 / r ** 2, (r, 0, 1))
B_hi = sp.integrate(s ** 2 * r ** 2 / 2 / r ** 2, (r, 0, 1 / s)) + sp.integrate(3 * s * r / r ** 2, (r, 1 / s, 1))
chk['97 (2): int_0^1 dr/r^2 of the bound gives B(s) = s^2/2 (s <= 1) and s(1/2 + 3 log s) (s >= 1), continuous at 1'] = \
    sp.simplify(B_lo - s ** 2 / 2) == 0 and sp.simplify(B_hi - s * (sp.Rational(1, 2) + 3 * sp.log(s))) == 0 and \
    (s * (sp.Rational(1, 2) + 3 * sp.log(s))).subs(s, 1) == sp.Rational(1, 2)
chk['97 (2): prefactor 2 pi (2 pi)^-2 (2 pi) = 1 (polar angle, inversion, Plancherel)'] = 2 * sp.pi * (2 * sp.pi) ** -2 * 2 * sp.pi == 1
integrand = (s * (sp.Rational(1, 2) + 3 * sp.log(s))) ** 2 * s / ((1 + s ** 2) ** 2 * (1 + sp.log(1 + s ** 2)) ** (2 * beta))
lims = {b: sp.limit((integrand * s * sp.log(s) ** (2 * b - 2)).subs(beta, b), s, sp.oo) for b in (1, sp.Rational(3, 2), 2)}
chk['97 (a): s (log s)^(2 beta - 2) * integrand -> 9/4^beta (beta = 1, 3/2, 2), so integrable at oo iff beta > 3/2'] = \
    all(sp.simplify(v - 9 / sp.Integer(4) ** b) == 0 for b, v in lims.items()) and \
    sp.limit(sp.integrate(1 / (s * sp.log(s) ** 2), (s, 2, sp.Symbol('S', positive=True))), sp.Symbol('S', positive=True), sp.oo) == 1 / sp.log(2)
chk['97 (a): at s -> 0 the integrand is O(s^5) (s^-5 * integrand -> 1/4 at beta = 2)'] = \
    sp.limit(((s ** 2 / 2) ** 2 * s / ((1 + s ** 2) ** 2 * (1 + sp.log(1 + s ** 2)) ** 4)) / s ** 5, s, 0) == sp.Rational(1, 4)
# scaling identities for g = eps Phi(X/eps), on a stand-in Phi = y exp(-r^2) with a closed-form transform
Phis = y * sp.exp(-(x ** 2 + y ** 2))
g = eps * Phis.subs({x: x / eps, y: y / eps})
chk['97 section 3: D g_n(X) = (D Phi)(X/eps): the C1 norms of g_n are bounded uniformly in n (stand-in)'] = \
    all(sp.simplify(sp.diff(g, v) - sp.diff(Phis, v).subs({x: x / eps, y: y / eps})) == 0 for v in (x, y))
k1, k2 = sp.symbols('k1 k2', real=True)
Ph = sp.I * sp.diff(sp.pi * sp.exp(-(k1 ** 2 + k2 ** 2) / 4), k2)  # transform of the stand-in: i d_k2 (pi e^(-|k|^2/4))
Fh = -k1 * k2 * Ph  # transform of d_x d_y Phi
gh = eps ** 3 * Ph.subs({k1: eps * k1, k2: eps * k2})  # transform of eps Phi(X/eps)
chk['97 (5): F_n_hat(xi) = eps F_hat(eps xi) for F_n = D^2 g_n (exact, Gaussian stand-in, mixed component)'] = \
    sp.simplify(-k1 * k2 * gh - eps * Fh.subs({k1: eps * k1, k2: eps * k2})) == 0
Pc = y * (1 - x ** 2 - y ** 2) ** 4
pol = lambda f: sp.integrate(sp.integrate(sp.expand(f.subs({x: r * sp.cos(th), y: r * sp.sin(th)}) * r), (th, 0, 2 * sp.pi)), (r, 0, 1))
mom = all(pol(sp.diff(Pc, a_, b_) * m_) == 0 for a_, b_ in ((x, x), (x, y), (y, y)) for m_ in (1, x, y))
chk['97 (4): D^2 Phi has zero mean and zero first moments (compact stand-in y (1 - r^2)^4 on r < 1, exact)'] = mom
chk['97 (5): 4^(-n) 4^k min(4^(2(k-n)), 4^(-4(k-n))) = 4^(-3|k-n|) and 1 + k <= (1 + n)(1 + |k - n|) (0 <= k, n <= 60)'] = \
    all(Q(4) ** (k - n) * min(Q(4) ** (2 * (k - n)), Q(4) ** (-4 * (k - n))) == Q(4) ** (-3 * abs(k - n)) and
        1 + k <= (1 + n) * (1 + abs(k - n)) for k in range(61) for n in range(61))
qk = Q(1, 64)
Kc = 2 * (1 + qk) / (1 - qk) ** 3 - 1  # 2 sum_(l>=0) (1 + l)^2 q^l - 1
Kp = 1 + 2 * sum((1 + l) ** 2 * qk ** l for l in range(1, 200))
chk['97 (6): ||K||_1 <= 1 + 2 sum_(l>=1) (1 + l)^2 64^-l = 2 (1 + q)/(1 - q)^3 - 1 at q = 1/64, which is < 6/5'] = \
    Kc < Q(6, 5) and Kp < Kc and Kc - Kp < Q(1, 10 ** 300)
chk['97 (7): (1 + n)^3 a_n^2 <= 4/(n log(n)^2): (1 + 1/n)^3 <= 27/8 < 4 for n >= 2, log(n + 1) >= log n'] = \
    all(Q(n + 1, n) ** 3 <= Q(27, 8) for n in range(2, 2000)) and Q(27, 8) < 4
Le, Lh = sp.symbols('L_e L_h', nonnegative=True)
aa_ = sp.Symbol('A', nonnegative=True)
chk['97 (8): (1 + |eta|^2)/eps^2 - (1 + |eta|^2/eps^2) = (1 - eps^2)/eps^2 >= 0 and (1 + 2 L_eps)(1 + L_eta) - (1 + 2 L_eps + L_eta) = 2 L_eps L_eta >= 0'] = \
    sp.simplify((1 + aa_) / eps ** 2 - (1 + aa_ / eps ** 2) - (1 - eps ** 2) / eps ** 2) == 0 and \
    sp.expand((1 + 2 * Le) * (1 + Lh) - (1 + 2 * Le + Lh)) == 2 * Le * Lh
chk['97 section 5: omega2 = (1 + 4 r^2)^(2/5) <= (1 + 4 r^2)^(1/2) <= 1 + 2 r ((1 + 2r)^2 - (1 + 4 r^2) = 4 r)'] = \
    sp.expand((1 + 2 * r) ** 2 - (1 + 4 * r ** 2)) == 4 * r
gap = 2 * sp.integrate(sp.sin(th), (th, 0, sp.pi)) * sp.integrate(r * r / r ** 3, (r, 2 * eps, 4 * eps))  # int_0^(2 pi) |sin| = 2 int_0^pi sin
chk['97 (10): on 2 eps_m < r < 4 eps_m the summand -y S_m contributes S_m int |sin| int dr/r = 4 log 2 S_m'] = \
    sp.simplify(gap - 4 * sp.log(2)) == 0
an = lambda n: 1 / (n * n * math.log(n + 1))
Nt = 400
lhs = sum(sum(an(n) for n in range(m, Nt + 1)) for m in range(3, Nt + 1)); rhs = sum((n - 2) * an(n) for n in range(3, Nt + 1))
chk['97 (10): sum_(m=3)^N sum_(n=m)^N a_n = sum_(n=3)^N (n - 2) a_n (N = 400, both orders, FLOAT agreement 1e-12)'] = abs(lhs - rhs) < 1e-12 * rhs
chk['97 (10): (n - 2)/n >= 1/3 for n >= 3, and int dx/((x + 1) log(x + 1)) = log log(x + 1) is unbounded'] = \
    all(Q(n - 2, n) >= Q(1, 3) for n in range(3, 5000)) and \
    sp.simplify(sp.diff(sp.log(sp.log(x + 1)), x) - 1 / ((x + 1) * sp.log(x + 1))) == 0
ep = lambda n: Q(1, 4 ** n)
chk['97 section 6: on 2 eps_m < r < 4 eps_m (m >= 3): r/eps_n <= 1 for n < m, r/eps_n >= 2 for n >= m, r <= 1/16; gaps disjoint'] = \
    all(ep(m - 1) == 4 * ep(m) and 4 * ep(m) <= Q(1, 16) and 4 * ep(m + 1) < 2 * ep(m) and
        all(4 * ep(m) <= ep(n) for n in range(2, m)) and all(2 * ep(n) <= 2 * ep(m) for n in range(m, m + 30))
        for m in range(3, 40))

# 2. FLOAT
ok_rem = True
for i in range(1, 20001):
    uu = i * 1e-3
    v = abs(complex(math.cos(uu) - 1, math.sin(uu) - uu))
    ok_rem = ok_rem and v <= uu * uu / 2 * (1 + 1e-12) + 1e-300 and v <= 2 * uu * (1 + 1e-12)
chk['97 FLOAT: |e^(iu) - 1 - iu| <= min(u^2/2, 2u) on u = 0.001, ..., 20'] = ok_rem
mp.mp.dps = 30
Bf = lambda z: z * z / 2 if z <= 1 else z * (mp.mpf(1) / 2 + 3 * mp.log(z))
def Cb(b, umax=mp.inf):
    # s <= 1 directly; s = e^u >= 1 in the variable u, where the integrand decays like u^(2 - 2 beta)
    f = lambda z: Bf(z) ** 2 * z / ((1 + z * z) ** 2 * (1 + mp.log(1 + z * z)) ** (2 * b))
    g_ = lambda uu: f(mp.exp(uu)) * mp.exp(uu)
    pts = [0] + [p for p in (1, 4, 16, 64, 256, 1024) if p < umax] + [umax]
    return mp.sqrt(2 * mp.pi * (mp.quad(f, [0, 1]) + mp.quad(g_, pts)))
C = {b: Cb(b) for b in (2, 2.5, 3)}
trunc = [Cb(1.5, e * mp.log(10)) for e in (4, 8, 16, 32, 64)]
chk['97 FLOAT: C_beta finite at beta = 2, 5/2, 3; the truncated beta = 3/2 integral keeps growing (like log log S)'] = \
    all(mp.isfinite(v) and v > 0 for v in C.values()) and all(trunc[i + 1] > trunc[i] for i in range(4)) and C[2] > C[3]
out['C_beta_FLOAT'] = {str(b): float(v) for b, v in C.items()}; out['C_3/2_truncated_FLOAT'] = [float(v) for v in trunc]
# I(h) <= C_beta ||h||_H_beta for h = y exp(-a r^2): |h_hat| = (pi/(2 a^2)) s |sin phi| exp(-s^2/(4a)), b[h] = 1
okI = True; rowsI = []
for a in (1, 4, 16):
    Ih = 4 * mp.quad(lambda z: (1 - mp.exp(-a * z * z)) / z, [0, 1])
    for b in (2, 2.5, 3):
        n2 = (2 * mp.pi) ** -2 * (mp.pi / (2 * a * a)) ** 2 * mp.pi * mp.quad(
            lambda z: (1 + z * z) ** 2 * (1 + mp.log(1 + z * z)) ** (2 * b) * z ** 3 * mp.exp(-z * z / (2 * a)), [0, 1, 10, 100, mp.inf])
        okI = okI and Ih <= C[b] * mp.sqrt(n2)
        rowsI.append({'a': a, 'beta': b, 'I': float(Ih), 'C_beta_norm': float(C[b] * mp.sqrt(n2))})
chk['97 (a) FLOAT: I(h) <= C_beta ||h||_(H_beta) for h = y exp(-a r^2), a = 1, 4, 16, beta = 2, 5/2, 3'] = okI
out['bound_tests_FLOAT'] = rowsI
# the nested construction with the smooth cutoff of the text
mp.mp.dps = 20
bump = lambda z: mp.exp(-1 / ((z - 1) * (2 - z))) if 1 < z < 2 else mp.mpf(0)
Z = mp.quad(bump, [1, 2])
chi = lambda z: mp.mpf(1) if z <= 1 else (mp.mpf(0) if z >= 2 else mp.quad(bump, [z, 2]) / Z)
NN = 9
def hN(xv, yv, N=NN):
    rr = mp.sqrt(xv * xv + yv * yv)
    return sum(an(n) * (yv * chi(rr * 4 ** n) - yv * chi(rr)) for n in range(2, N + 1))
okg = True
for m in range(3, NN + 1):
    for frac, ang in ((0.1, 0.3), (0.5, 1.2), (0.9, 2.5)):
        rr = 2 * mp.mpf(4) ** -m * (1 + frac)  # 2 eps_m < r < 4 eps_m
        xv, yv = rr * mp.cos(ang), rr * mp.sin(ang)
        okg = okg and abs(hN(xv, yv) + yv * sum(an(n) for n in range(m, NN + 1))) < 1e-15
chk[f'97 (10) FLOAT: h_N (N = {NN}, smooth cutoff of the text) equals -y sum_(m<=n<=N) a_n on the gaps (21 points)'] = okg
d = mp.mpf(4) ** -(NN + 2)
chk['97 FLOAT: b[h_N] = d_y h_N(0) = 0 (h_N vanishes on r < 4^-N)'] = hN(0, d) == 0 and hN(d / 3, d / 2) == 0
gl = [4 * math.log(2) * sum((n - 2) * an(n) for n in range(3, N + 1)) for N in (10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5)]
chk['97 (10) FLOAT: the gap lower bound 4 log 2 sum_(n=3)^N (n - 2) a_n of I(h_N) increases at N = 10, ..., 10^5'] = \
    all(gl[i + 1] > gl[i] + 0.3 for i in range(4))
out['gap_lower_bounds_FLOAT'] = gl
dq = max(2 * 1.5 * z / (1 + z * z) * (1 + math.log(1 + z * z)) ** 0.5 for z in [10 ** (e / 50) for e in range(-200, 1000)])
chk['97 (9) FLOAT: sup |D q_(3/2)| = sup 3 s (1 + s^2)^-1 (1 + log(1 + s^2))^(1/2) is finite (grid 1e-4 to 1e20)'] = dq < 3
out['sup_Dq_3/2_FLOAT'] = dq
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t00, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
