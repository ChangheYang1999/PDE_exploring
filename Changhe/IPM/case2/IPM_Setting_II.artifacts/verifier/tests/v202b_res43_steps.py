"""V202b: heavier independent exact checks for referee result 43 (not using the check script of referee result 43).
Part A (Steps 3-4): concrete descents for M = N with s = 0 (q_N = p) and s = 1 (q_N = p z, y = y* + eps z), all integration
constants symbolic, a bookkeeping factor lam on the linear (l-Euler) terms; checks function class, leading powers,
{Q,T} structure and the contradiction in the unused lower coefficient equations.
Part B (Steps 7-11): the exact E = 0 pole family n = K z^-6 (v = c z exactly) with the complete solution space of
T6..T2 + Poisson after the translation (m = mu4 z^-4 + mu7 z^7, three b modes, two u modes, constant in k); checks the
asserted leading coefficients and the T0 contradiction in the three cases B != 0; B = 0, U != 0; B = U = 0."""
import sympy as sp
from math import factorial
R = []
def ok(name, val):
    R.append(bool(val)); print('%-100s %s' % (name, bool(val)), flush=True)
l, x, zp = sp.symbols('l x zp')
beta = 2 * l - sp.Rational(1, 2)
nx = lambda e: sp.expand(sp.sympify(e))
def inv(c):
    c = sp.sympify(c)
    return sp.Rational(1, 1) / c if c.is_Rational else sp.expand(sp.radsimp(1 / c))
fl = lambda e: float(sp.N(e, 30))

class PL:
    """finite sum of c z^e (log z)^k, stored as {(e, k): c}"""
    def __init__(self, d=None):
        self.d = {}
        for key, c in (d or {}).items():
            c = sp.expand(c)
            if c != 0:
                self.d[key] = c
    @staticmethod
    def mono(c, e=0, k=0):
        return PL({(nx(e), k): c})
    def _acc(self, items):
        r = {}
        for key, c in items:
            r.setdefault(key, []).append(c)
        return PL({k_: sp.Add(*v) for k_, v in r.items()})
    def __add__(self, o):
        if not isinstance(o, PL): o = PL.mono(o)
        return self._acc(list(self.d.items()) + list(o.d.items()))
    __radd__ = __add__
    def __neg__(self): return PL({k_: -c for k_, c in self.d.items()})
    def __sub__(self, o): return self + (-o if isinstance(o, PL) else PL.mono(-o))
    def __rsub__(self, o): return (-self) + o
    def __mul__(self, o):
        if not isinstance(o, PL): return PL({k_: c * o for k_, c in self.d.items()})
        return self._acc([((nx(e1 + e2), k1 + k2), c1 * c2) for (e1, k1), c1 in self.d.items() for (e2, k2), c2 in o.d.items()])
    __rmul__ = __mul__
    def __truediv__(self, o): return self * inv(o)
    def diff(self):
        it = []
        for (e, k), c in self.d.items():
            if e != 0: it.append(((nx(e - 1), k), e * c))
            if k > 0: it.append(((nx(e - 1), k - 1), k * c))
        return self._acc(it)
    def integ(self):
        it = []
        for (e, k), c in self.d.items():
            if e == -1:
                it.append(((sp.Integer(0), k + 1), c / (k + 1)))
            else:
                a_ = nx(e + 1); ia = inv(a_)
                for i in range(k + 1):
                    it.append(((a_, k - i), (-1)**i * sp.Rational(factorial(k), factorial(k - i)) * c * ia**(i + 1)))
        return self._acc(it)
    def mulz(self, s):
        return PL({(nx(e + s), k): c for (e, k), c in self.d.items()})
    def theta(self): return self.diff().mulz(1)
    def subs(self, sb): return PL({k_: c.subs(sb) for k_, c in self.d.items()})
    def iszero(self): return len(self.d) == 0
    def lead_inf(self):
        if not self.d: return None
        em = max(fl(e) for e, k in self.d)
        ks = [(e, k) for (e, k) in self.d if abs(fl(e) - em) < 1e-20]
        e0, k0 = max(ks, key=lambda t: t[1]); return e0, k0, self.d[(e0, k0)]
    def lead_0(self):
        if not self.d: return None
        em = min(fl(e) for e, k in self.d)
        ks = [(e, k) for (e, k) in self.d if abs(fl(e) - em) < 1e-20]
        e0, k0 = max(ks, key=lambda t: t[1]); return e0, k0, self.d[(e0, k0)]
    def coeff(self, e, k=0): return self.d.get((nx(e), k), sp.Integer(0))
    def has_log(self): return any(k > 0 for (e, k) in self.d)

th = sp.Symbol('theta')
def apply_P(Pth, Y):
    """P(theta) Y for polynomial P"""
    cs = sp.Poly(Pth, th).all_coeffs(); out = PL()
    for c in cs:
        out = out.theta() + Y * c if not out.iszero() else Y * c
    return out
def euler_solve(Pth, F):
    """a particular solution of P(theta) Y = F, F a power-log sum (handles resonance)"""
    deg = sp.degree(Pth, th); out = PL()
    groups = {}
    for (e, k), c in F.d.items():
        groups.setdefault(e, {})[k] = c
    for g, cks in groups.items():
        a_ = [sp.expand(sp.radsimp(sp.diff(Pth, th, i).subs(th, g) / factorial(i))) for i in range(deg + 1)]
        mu = 0
        while a_[mu] == 0: mu += 1
        kmax = max(cks); qv = {}
        for mm in range(kmax, -1, -1):
            acc = cks.get(mm, 0) - sum(a_[i] * sp.Rational(factorial(mm + i), factorial(mm)) * qv.get(mm + i, 0) for i in range(mu + 1, deg + 1))
            qv[mm + mu] = sp.expand(acc * inv(a_[mu] * sp.Rational(factorial(mm + mu), factorial(mm))))
        out = out + PL({(g, j): c for j, c in qv.items()})
    return out

# self-test of the power-log machinery: resonant Euler solves verified by applying P(theta)
zt = PL.mono(1, 1) * PL.mono(1, 0, 1) + PL.mono(3, sp.Rational(1, 2), 2) + PL.mono(5, -2)
good = True
for Pt in [(th - 1)**2 * (th + 2), (th - sp.Rational(1, 2)) * (th - 3), th**2 + th - 14, (th + 2) * (th**2 - th - 28)]:
    good &= (apply_P(Pt, euler_solve(Pt, zt)) - zt).iszero()
Ft = PL.mono(2, -1, 1) + PL.mono(sp.sqrt(3), sp.sqrt(2), 2)
good &= (Ft.integ().diff() - Ft).iszero()
ok('PL self-test: P(theta) euler_solve(P, F) = F with resonances (logs); (integ F)\' = F incl. exponent -1', good)

# =============== Part A: concrete descents (Steps 3-4) ===============
pS, CS, AS, ysS, lam = sp.symbols('p C A ystar lam')
def Qcoef(N, s, i):
    j = N - i
    return pS * (-CS)**j * sp.Rational(factorial(N) * factorial(s), factorial(N - j) * factorial(s + 2 * j))
def descent(N, r, s, eps=1):
    D = 2 * N + s; d = sp.Rational(D * r, N)
    cnt = [0]
    def newc():
        cnt[0] += 1; return sp.Symbol('k%d' % cnt[0])
    Y = (PL.mono(ysS) + PL.mono(eps, 1)) if s == 1 else PL.mono(1, 1)
    dy = lambda F: F.diff() * eps
    q = {N: PL.mono(pS, s)}; Rd = {r: PL.mono(AS, sp.Rational(s * r, N))}
    Q = lambda i: q[i] if i in q else PL()
    RR = lambda j: Rd[j] if j in Rd else PL()
    def ensure_q(i):
        if i in q or i > N or i < 0: return
        ensure_q(i + 1); ensure_q(i + 2)
        assert i + 1 > r or (i + 1) in Rd, ('missing R', i + 1)
        F = (CS * Q(i + 1) + RR(i + 1)) * (-(i + 1)) - Q(i + 2) * ((i + 2) * (i + 1))
        q[i] = F.integ().integ() + PL.mono(newc(), 1) + PL.mono(newc(), 0)
    def coef(e, skip=None):
        tot = PL()
        for i in range(0, e + 2):
            kk = e + 1 - i
            if kk == skip or kk not in Rd or i > N: continue
            assert i in q, ('missing q', i)
            tot = tot + Q(i) * dy(RR(kk)) * i - dy(Q(i)) * RR(kk) * kk
        lin = (Q(e) * (l * e - 1) + Y * dy(Q(e)) * l) * CS + RR(e) * (l * e - 1) + Y * dy(RR(e)) * l
        return tot + lin * lam
    for j in range(r - 1, -1, -1):
        for i in range(N - 1, N + j - r - 1, -1):
            ensure_q(i)
        e = N + j - 1
        rest = coef(e, skip=j)
        if s == 0:      # N p eps R_j' = -rest
            Rd[j] = (-rest).integ() / (N * pS * eps) + PL.mono(newc())
        else:           # N p z eps R_j' - j eps p R_j = -rest  <=>  (theta - j/N) R_j = -rest/(N p eps)
            Rd[j] = euler_solve(th - sp.Rational(j, N), (-rest) / (N * pS * eps)) + PL.mono(newc(), sp.Rational(j, N))
    for i in range(N - 1, -1, -1):
        ensure_q(i)
    used_ok = all(coef(e).iszero() for e in range(N - 1, N + r))
    pois_ok = all((Q(i).diff().diff() + (CS * Q(i + 1) + RR(i + 1)) * (i + 1) + Q(i + 2) * ((i + 2) * (i + 1))).iszero() for i in range(0, N + 1))
    return dict(q=q, R=Rd, D=D, d=d, coef=coef, used_ok=used_ok, pois_ok=pois_ok)

def check_descent(N, r, s, eps=1):
    out = descent(N, r, s, eps); q, Rd, D, d = out['q'], out['R'], out['D'], out['d']
    lab = 'N=%d r=%d s=%d eps=%+d' % (N, r, s, eps)
    ok('S3 descent %s: used coefficient eqs x^(N-1..N+r-1) and all Poisson eqs hold exactly' % lab, out['used_ok'] and out['pois_ok'])
    if s == 0:
        cls = all(k == 0 and sp.sympify(e).is_integer and e >= 0 for F in list(q.values()) + list(Rd.values()) for (e, k) in F.d)
        ok('S3 descent %s: every q_i, R_j is a polynomial in z (s=0 claim)' % lab, cls)
    # leading powers
    lq = True
    for i in range(0, N + 1):
        top = [(e, k) for (e, k) in q[i].d if fl(e) > (D - 2 * i) - 1e-12]
        lq &= top == [(nx(D - 2 * i), 0)] and sp.simplify(q[i].coeff(D - 2 * i) - Qcoef(N, s, i)) == 0
    ok('S3 descent %s: q_i = h_i z^(D-2i) + lower, h_i = coefficients of the displayed Q(x,z), no log at top' % lab, lq)
    lr = True; rj = {}
    for j in range(0, r + 1):
        top = [(e, k) for (e, k) in Rd[j].d if fl(e) > fl(d - 2 * j) - 1e-12]
        lr &= all(e == nx(d - 2 * j) and k == 0 for (e, k) in top)
        rj[j] = Rd[j].coeff(d - 2 * j)
        lr &= not any(c.has(lam) or any(c.has(sp.Symbol('k%d' % t)) for t in range(1, 60)) for c in [rj[j]])
    ok('S3 descent %s: R_j = r_j z^(d-2j) + lower (no larger power, no log there), r_j indep. of constants and lam' % lab, lr and rj[r] == AS)
    lw = all(fl(e) + 2 * j <= 3 + 1e-12 for j in range(0, r) for (e, k), c in Rd[j].d.items() if sp.diff(c, lam) != 0)
    ok('S3 descent %s: lam (linear) parts of R_j have weight 2j + exponent <= 3 < d = %s' % (lab, d), lw and d > 3)
    if s == 1:
        lg = all(F.has_log() is False or all(fl(e) < fl(top) - 1e-12 for (e, k) in F.d if k > 0)
                 for F, top in [(q[i], D - 2 * i) for i in q] + [(Rd[j], d - 2 * j) for j in Rd])
        ok('S3 descent %s: logs (if any) only strictly below the leading powers' % lab, lg)
    # weighted leading problem {Q, T} with T from the descent
    xs, zs = sp.symbols('xs zs', positive=True)
    Qw = sum(Qcoef(N, s, i) * xs**i * zs**(D - 2 * i) for i in range(N + 1))
    Tw = sum(rj[j] * xs**j * zs**(d - 2 * j) for j in range(r + 1))
    br = sp.expand(sp.diff(Qw, xs) * sp.diff(Tw, zs) - sp.diff(Qw, zs) * sp.diff(Tw, xs))
    brp = sp.Poly(br, xs)
    zer = all(sp.simplify(brp.coeff_monomial(xs**e)) == 0 for e in range(N - 1, N + r))
    ok('S3 descent %s: {Q,T}_(x,z) coefficients of x^e vanish for e = N-1..N+r-1 (the descent equations)' % lab, zer)
    # lower equations: actual residual leading term = eps * {Q,T} coefficient, and one is nonzero
    found = False; agree = True; info = []
    for e in range(N - 2, -1, -1):
        res = out['coef'](e).subs({lam: 1})
        w = D + d - 3 - 2 * e
        top = [(ee, k) for (ee, k) in res.d if fl(ee) > fl(w) - 1e-12]
        brc = sp.simplify(brp.coeff_monomial(xs**e) / zs**w)
        agree &= all(ee == nx(w) and k == 0 for (ee, k) in top) and sp.simplify(res.coeff(w) - eps * brc) == 0
        if brc != 0 and not found:
            found = True
            fac = sp.factor(brc); info.append((e, fac))
            isnz = all(sym in (pS, CS, AS) for sym in fac.free_symbols) and sp.Poly(sp.numer(fac), pS, CS, AS).is_monomial
    ok('S3 descent %s: lower eq residuals have leading term eps*{Q,T}_e z^(D+d-3-2e) (weight claim)' % lab, agree)
    ok('S3 descent %s: first lower {Q,T} coefficient is a nonzero monomial in p, C, A -> contradiction %s' % (lab, info), found and isnz)

for (N, r, s, eps) in [(3, 2, 0, 1), (4, 2, 0, 1), (4, 3, 0, 1), (5, 2, 0, 1), (5, 3, 0, 1), (5, 4, 0, 1),
                       (3, 2, 1, 1), (3, 2, 1, -1), (4, 2, 1, 1), (4, 3, 1, 1)]:
    check_descent(N, r, s, eps)

# =============== Part B: exact pole family (Steps 7-11), E = 0 ===============
s113, s57 = sp.sqrt(113), sp.sqrt(57)
rB = (1 - s113) / 2; rP = (1 + s113) / 2; tau = (-1 - s57) / 2; tauP = (-1 + s57) / 2
K, Bc, B2, B3, Uc, U2, mu4, mu7, kc = sp.symbols('K B B2 B3 U U2 mu4 mu7 kc')
Pm = (th + 6) * (th + 4) * (th - 7); Pb = (th + 2) * (th**2 - th - 28); Pu = th**2 + th - 14
D1 = lambda F: F.diff()
D2 = lambda F: F.diff().diff()
D3 = lambda F: F.diff().diff().diff()
def family(Bv, Uv):
    n = PL.mono(K, -6); invn = PL.mono(1 / K, 6)
    a = D2(n) * sp.Rational(-1, 4)
    m = PL.mono(mu4, -4) + PL.mono(mu7, 7)
    Lm = D3(m) - D1(n) * invn * D2(m) - D2(n) * invn * D1(m) + D3(n) * invn * m * sp.Rational(1, 2)
    h = D2(m) * sp.Rational(-1, 3)
    Rb = D1(n) * (-2) - D2(n) * invn * ((8 * l - 1) / 6) - m * D3(m) * invn * sp.Rational(4, 9) + D1(m) * D2(m) * invn * sp.Rational(2, 3)
    b = euler_solve(Pb, Rb.mulz(3)) + PL.mono(Bv, rB) + PL.mono(B3, rP) + PL.mono(B2, -2)
    Lb = D3(b) - D1(n) * invn * D2(b) * sp.Rational(2, 3) - D2(n) * invn * D1(b) * sp.Rational(2, 3) + D3(n) * invn * b * sp.Rational(1, 6)
    f = (D2(b) + n * 6) * sp.Rational(-1, 2)
    Ru = (D2(m) * invn * (-(6 * l - 1) / 9) - b * D3(m) * invn * sp.Rational(1, 9) - m * D3(b) * invn * sp.Rational(1, 3)
          - m * D1(n) * invn * sp.Rational(4, 3) + D1(b) * D2(m) * invn * sp.Rational(1, 3) + D2(b) * D1(m) * invn * sp.Rational(1, 3))
    u = euler_solve(Pu, Ru.mulz(2)) + PL.mono(Uv, tau) + PL.mono(U2, tauP)
    Lu = D2(u) - D1(n) * invn * D1(u) * sp.Rational(1, 3) - D2(n) * invn * u * sp.Rational(1, 3)
    g = -D1(u) - m * 2
    rest2 = m * D1(g) * 2 - D1(m) * g + b * D1(f) + (PL.mono(beta) - D1(b)) * f * 2 - h * u * 3
    kp = -(rest2 * invn) * sp.Rational(1, 3)
    k = kp.integ() + PL.mono(kc)
    T = {6: n * D1(a) * 3 - D1(n) * a * 4,
         5: n * D1(h) * 3 - D1(n) * h * 3 + m * D1(a) * 2 - D1(m) * a * 4,
         4: n * D1(f) * 3 - D1(n) * f * 2 + m * D1(h) * 2 - D1(m) * h * 3 + b * D1(a) + (PL.mono(8 * l - 1) - D1(b) * 4) * a,
         3: n * D1(g) * 3 - D1(n) * g + m * D1(f) * 2 - D1(m) * f * 2 + b * D1(h) + (PL.mono(6 * l - 1) - D1(b) * 3) * h - a * u * 4,
         2: n * D1(k) * 3 + rest2,
         1: m * D1(k) * 2 + b * D1(g) + (PL.mono(2 * l - 1) - D1(b)) * g - f * u * 2,
         0: b * D1(k) - g * u - k}
    pois = [(D2(n) + a * 4), (D2(m) + h * 3), (D2(b) + f * 2 + n * 6), (D1(u) + g + m * 2)]
    return dict(n=n, a=a, m=m, h=h, b=b, f=f, u=u, g=g, k=k, T=T, Lm=Lm, Lb=Lb - Rb, Lu=Lu - Ru, pois=pois)

Fg = family(Bc, Uc)
ok('S7/S8 family: L_m m = 0 for m = mu4 z^-4 + mu7 z^7 (n = K z^-6); L_b b = R_b and L_u u = R_u exactly', Fg['Lm'].iszero() and Fg['Lb'].iszero() and Fg['Lu'].iszero())
ok('S7/S8 family: Poisson (4 eqs) and transport T6, T5, T4, T3, T2 hold exactly', all(p_.iszero() for p_ in Fg['pois']) and all(Fg['T'][i].iszero() for i in (6, 5, 4, 3, 2)))
ok('S8 family: no logarithms in b, u, k (no resonance in this exact family)', not (Fg['b'].has_log() or Fg['u'].has_log()))
print('   b exponents:', sorted({sp.nsimplify(e) for (e, k) in Fg['b'].d}, key=fl), flush=True)
ok('S8 b = B z^r + (3K/4) z^-4 + O(z^-2): coefficient of z^-4 is 3K/4, all other non-B exponents >= -2',
   sp.simplify(Fg['b'].coeff(-4) - 3 * K / 4) == 0 and all(fl(e) >= -2 - 1e-12 for (e, k) in Fg['b'].d if e not in (nx(rB), nx(-4))))
ue = sorted({e for (e, k) in Fg['u'].d}, key=fl)
ok('S8 u = U z^tau + O(z^(r+1)) if B != 0 (all other exponents >= r+1)', all(fl(e) >= fl(rB + 1) - 1e-12 for e in ue if e != nx(tau)))
Lf = Fg['f'].lead_0(); Lk = Fg['k'].lead_0(); Lg = Fg['g'].lead_0()
ok('S9 h = -m\'\'/3 = O(z^-6)', fl(Fg['h'].lead_0()[0]) >= -6 - 1e-12)
ok('S9 f = F z^(r-2) + o, F = -14B', Lf[0] == nx(rB - 2) and Lf[1] == 0 and sp.simplify(Lf[2] + 14 * Bc) == 0)
ok('S9 g = O(z^(tau-1)) (leading exponent tau-1, coefficient -tau U)', Lg[0] == nx(tau - 1) and sp.simplify(Lg[2] + tau * Uc) == 0)
ok('S9 k = k_B z^(2r+4) + o, k_B = -7B^2/(3K)', Lk[0] == nx(2 * rB + 4) and Lk[1] == 0 and sp.simplify(Lk[2] + 7 * Bc**2 / (3 * K)) == 0)
L0 = Fg['T'][0].lead_0()
print('   T0 leading (B general):', (sp.nsimplify(L0[0]), L0[1], sp.factor(L0[2])), flush=True)
ok('S9 T0 = b k\' - g u - k has leading term 7(sqrt113-5)B^3/(3K) z^(3r+3) (all other exponents larger)',
   L0[0] == nx(3 * rB + 3) and L0[1] == 0 and sp.simplify(sp.radsimp(L0[2] - 7 * (s113 - 5) * Bc**3 / (3 * K))) == 0
   and sum(1 for (e, k) in Fg['T'][0].d if abs(fl(e) - fl(3 * rB + 3)) < 1e-20) == 1)
F0 = family(0, Uc)
ok('S10 (B=0) b = (3K/4) z^-4 + O(z^-2)', F0['b'].lead_0()[0] == -4 and sp.simplify(F0['b'].lead_0()[2] - 3 * K / 4) == 0
   and all(fl(e) >= -2 - 1e-12 for (e, k) in F0['b'].d if e != -4))
ok('S10 (B=0) f = F0 z^-6 + O(z^-4), F0 = -21K/2', F0['f'].lead_0()[0] == -6 and sp.simplify(F0['f'].lead_0()[2] + sp.Rational(21, 2) * K) == 0
   and all(fl(e) >= -4 - 1e-12 for (e, k) in F0['f'].d if e != -6))
ok('S10 (B=0) u = U z^tau + O(z^-3); g = -tau U z^(tau-1) + O(z^-4)', all(fl(e) >= -3 - 1e-12 for (e, k) in F0['u'].d if e != nx(tau))
   and F0['g'].lead_0()[0] == nx(tau - 1) and sp.simplify(F0['g'].lead_0()[2] + tau * Uc) == 0 and all(fl(e) >= -4 - 1e-12 for (e, k) in F0['g'].d if e != nx(tau - 1)))
ok('S10 (B=0) k = k0 z^-4 + o(z^-4), k0 = -21K/16', F0['k'].lead_0()[0] == -4 and sp.simplify(F0['k'].lead_0()[2] + sp.Rational(21, 16) * K) == 0)
L0 = F0['T'][0].lead_0()
print('   T0 leading (B=0):', (sp.nsimplify(L0[0]), L0[1], sp.factor(L0[2])), flush=True)
ok('S10 (B=0) T0 leading term tau U^2 z^(2tau-1)', L0[0] == nx(2 * tau - 1) and L0[1] == 0 and sp.simplify(L0[2] - tau * Uc**2) == 0)
F00 = family(0, 0)
L0 = F00['T'][0].lead_0()
print('   T0 leading (B=U=0):', (sp.nsimplify(L0[0]), L0[1], sp.factor(L0[2])), flush=True)
ok('S11 (B=U=0) T0 = b k\' - g u - k = (63K^2/16) z^-9 + o(z^-9)', L0[0] == -9 and L0[1] == 0 and sp.simplify(L0[2] - sp.Rational(63, 16) * K**2) == 0)
ok('S11 (B=U=0) u = O(z^-3), g = O(z^-4) in the family', (F00['u'].lead_0() is None or fl(F00['u'].lead_0()[0]) >= -3 - 1e-12)
   and fl(F00['g'].lead_0()[0]) >= -4 - 1e-12)
L1 = Fg['T'][1].lead_0()
print('   (info) T1 leading (B general):', (sp.nsimplify(L1[0]), L1[1], sp.factor(L1[2])), flush=True)
print('ALL', all(R), len(R), flush=True)
