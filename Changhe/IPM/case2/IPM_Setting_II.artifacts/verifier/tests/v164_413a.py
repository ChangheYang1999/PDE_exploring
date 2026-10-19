"""V164: FR Proposition 4.13a and its proof Section 9.12 (item 25b, candidate 2ad6f815). Symbolic checks (sympy, exact
where possible) of every formula and constant, plus a randomized adversarial check of the restricted gap (d).
Psi_p[A] is the periodic solution of Psi'' + (p+1)^2 Psi = sin th A' - p cos th A (Theorem 3.16), computed here mode by
mode from the exact Fourier coefficients of the forcing (finite trigonometric polynomials A only)."""
import sympy as sp, mpmath as mp, random
ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)
th, t, p, r = sp.symbols('th t p r', real=True)
eps = sp.symbols('eps', positive=True)
def fcoef(f, n, kind):
    if n == 0: return sp.simplify(sp.integrate(f, (th, 0, 2*sp.pi))/(2*sp.pi))
    g = sp.cos(n*th) if kind == 'c' else sp.sin(n*th)
    return sp.simplify(sp.integrate(sp.expand(sp.expand_trig(f*g)), (th, 0, 2*sp.pi))/sp.pi)
def fcoef_fast(f, n, kind, N=12):
    # exact projection via rewriting as exponentials
    fe = sp.expand(sp.expand(f.rewrite(sp.exp)))
    z = sp.exp(sp.I*th)
    c = sp.simplify(sp.expand(fe).coeff(sp.exp(sp.I*n*th)) if n else None)
    return c
def Psi_of(A, pv, N):
    """periodic solution for a trigonometric polynomial A of degree <= N-1 (forcing degree <= N)."""
    F = sp.sin(th)*sp.diff(A, th) - pv*sp.cos(th)*A
    F = sp.expand(sp.fu(sp.expand_trig(F)) if False else F)
    out = 0
    for n in range(0, N + 1):
        an = sp.integrate(sp.expand(F*sp.cos(n*th)), (th, 0, 2*sp.pi))/(sp.pi if n else 2*sp.pi)
        bn = sp.integrate(sp.expand(F*sp.sin(n*th)), (th, 0, 2*sp.pi))/sp.pi if n else 0
        an, bn = sp.simplify(an), sp.simplify(bn)
        if an == 0 and bn == 0: continue
        den = (pv + 1)**2 - n**2
        out += (an*sp.cos(n*th) + bn*sp.sin(n*th))/den
    return sp.simplify(out)

# S1: frequency-2 coefficients of Psi_p for general A with modes 0..5
a = sp.symbols('a0:6', real=True); b = sp.symbols('b0:6', real=True)
A = a[0] + sum(a[n]*sp.cos(n*th) + b[n]*sp.sin(n*th) for n in range(1, 6))
F = sp.sin(th)*sp.diff(A, th) - p*sp.cos(th)*A
c2 = sp.simplify(sp.integrate(sp.expand(F*sp.cos(2*th)), (th, 0, 2*sp.pi))/sp.pi)
s2 = sp.simplify(sp.integrate(sp.expand(F*sp.sin(2*th)), (th, 0, 2*sp.pi))/sp.pi)
rep('S1a frequency-2 forcing: cos 2th coefficient = ((1-p) a_1 - (p+3) a_3)/2', sp.simplify(c2 - ((1 - p)*a[1] - (p + 3)*a[3])/2) == 0, c2)
rep('S1b sin 2th coefficient = ((1-p) b_1 - (p+3) b_3)/2', sp.simplify(s2 - ((1 - p)*b[1] - (p + 3)*b[3])/2) == 0, s2)
rep('S1c (p+1)^2 - 4 = (p-1)(p+3)', sp.expand((p + 1)**2 - 4 - (p - 1)*(p + 3)) == 0)
rep('S1d [Psi_p]_cos2th = a_3/(2(1-p)) - a_1/(2(p+3)) and same for sin',
    sp.simplify(c2/((p + 1)**2 - 4) - (a[3]/(2*(1 - p)) - a[1]/(2*(p + 3)))) == 0 and
    sp.simplify(s2/((p + 1)**2 - 4) - (b[3]/(2*(1 - p)) - b[1]/(2*(p + 3)))) == 0)
# S2: frequency-1 forcing coefficient -p a_0 - (p+2) a_2/2 (cos), and multiplier 1/(p(p+2))
c1 = sp.simplify(sp.integrate(sp.expand(F*sp.cos(th)), (th, 0, 2*sp.pi))/sp.pi)
rep('S2 cos th forcing coefficient = -p a_0 - (p+2) a_2/2; (p+1)^2 - 1 = p (p+2)',
    sp.simplify(c1 - (-p*a[0] - (p + 2)*a[2]/2)) == 0 and sp.expand((p + 1)**2 - 1 - p*(p + 2)) == 0, c1)

# S3: A_f
Af = sp.cos(th)**2*(1 + 16*sp.sin(th)**6)
Aff = sp.Rational(9, 8) - sp.cos(4*th)/2 + sp.cos(6*th)/2 - sp.cos(8*th)/8
rep('S3a A_f = 9/8 - cos 4th/2 + cos 6th/2 - cos 8th/8', sp.simplify(sp.expand_trig(Af - Aff)) == 0 or
    max(abs(float((Af - Aff).subs(th, x))) for x in [0.1*k for k in range(63)]) < 1e-14)
ser = sp.series(Af.subs(th, sp.pi/2 + t), t, 0, 6).removeO()
ser3 = sp.series(Af.subs(th, 3*sp.pi/2 + t), t, 0, 6).removeO()
rep('S3b A_f(pi/2 + t) = 17 t^2 - 161 t^4/3 + O(t^6), same at 3pi/2', sp.simplify(ser - (17*t**2 - sp.Rational(161, 3)*t**4)) == 0 and sp.simplify(ser3 - ser) == 0, ser)
rep('S3c A_f(pi/2 + t) = sin^2 t (1 + 16 cos^6 t)', sp.simplify(Af.subs(th, sp.pi/2 + t) - sp.sin(t)**2*(1 + 16*sp.cos(t)**6)) == 0)
PsiAf = Psi_of(Aff, p, 9)
print('   Psi_p[A_f] =', PsiAf)
mods = {}
for n in range(0, 10):
    cn = sp.simplify(sp.integrate(sp.expand(PsiAf*sp.cos(n*th)), (th, 0, 2*sp.pi))/sp.pi)
    sn = sp.simplify(sp.integrate(sp.expand(PsiAf*sp.sin(n*th)), (th, 0, 2*sp.pi))/sp.pi)
    if cn != 0 or sn != 0: mods[n] = (cn, sn)
print('   modes of Psi_p[A_f]:', mods)
rep('S3d Psi_p[A_f] has only odd modes 1..9, cos only; mode-1 coefficient -9/(8(p+2))',
    set(mods) <= {1, 3, 5, 7, 9} and all(v[1] == 0 for v in mods.values()) and sp.simplify(mods[1][0] + sp.Rational(9, 8)/(p + 2)) == 0)
pg = [mp.mpf(k)/1000 for k in range(1, 1000)]
mx = max(sum(abs(float(v[0].subs(p, pv))) for v in mods.values()) for pv in pg[::7])
rep('S3e sum of |coefficients| of Psi_p[A_f] bounded on 0 < p < 1 (max over grid)', mx < 10, mx)
rep('S3f |(p+1)^2 - n^2| >= 5 for odd n >= 3, 0 < p < 1 (min at n = 3, p -> 1: 9 - 4)', all(abs((pv + 1)**2 - n**2) >= 5 for pv in pg for n in [3, 5, 7, 9]))
# check Psi_of solves the ODE
res = sp.simplify(sp.diff(PsiAf, th, 2) + (p + 1)**2*PsiAf - (sp.sin(th)*sp.diff(Aff, th) - p*sp.cos(th)*Aff))
rep('S3g Psi_p[A_f] solves the angular equation', sp.simplify(sp.expand_trig(res)) == 0 or max(abs(float(res.subs({p: 0.37, th: x}))) for x in [0.3*k for k in range(21)]) < 1e-12)

# S4: (c) expansion for a fixed A with a nonzero third mode: A = cos^2 th (1 + cos th/2 + sin th/3)  (positive bracket)
A4 = sp.expand(sp.cos(th)**2*(1 + sp.cos(th)/2 + sp.sin(th)/3))
A4t = sp.fu(A4)
A4c = sp.expand(sp.Rational(1, 2) + sp.cos(2*th)/2 + (3*sp.cos(th) + sp.cos(3*th))/8 + (sp.sin(th) + sp.sin(3*th))/12)
rep('S4a A = cos^2 th (1 + cos th/2 + sin th/3) as a trigonometric polynomial (a_3 = 1/8, b_3 = 1/12)',
    max(abs(float((A4 - A4c).subs(th, x))) for x in [0.1*k for k in range(63)]) < 1e-14)
pp = 1 - eps
Psi4 = Psi_of(A4c, pp, 4)
J4 = sp.expand((pp + 1)*Psi4*sp.diff(A4c, th) - pp*sp.diff(Psi4, th)*A4c)
B4 = J4*pp/eps
P3 = sp.cos(2*th)/8 + sp.sin(2*th)/12
lead = (2*P3*sp.diff(A4c, th) - sp.diff(P3, th)*A4c)/(2*eps**2)
rem = eps*(B4 - lead)      # must stay bounded as eps -> 0, uniformly in th (evaluated at 50 digits, no simplify)
frem = sp.lambdify((eps, th), rem, 'mpmath')
mp.mp.dps = 50
vals = {e: [frem(mp.mpf(e), mp.mpf(k)/5) for k in range(32)] for e in ['1e-4', '1e-6', '1e-8']}
mxr = max(abs(x) for e in vals for x in vals[e])
dif = max(abs(x - y) for x, y in zip(vals['1e-6'], vals['1e-8']))
rep('S4b eps (B_p - (2 P_3 A\' - P_3\' A)/(2 eps^2)) bounded as eps -> 0 (grid max over eps = 1e-4..1e-8, 32 angles)', mxr < 50, mp.nstr(mxr, 6))
rep('S4c it converges as eps -> 0 (max change from eps = 1e-6 to 1e-8: %s)' % mp.nstr(dif, 3), dif < mp.mpf('1e-4'))
mp.mp.dps = 30
L3 = sp.simplify(2*P3*sp.diff(A4c, th) - sp.diff(P3, th)*A4c)
rep('S4d 2 P_3 A\' - P_3\' A is not identically zero', max(abs(float(L3.subs(th, x))) for x in [0.1*k for k in range(63)]) > 1e-3)
# (P_3/A^2)' = -(2 P_3 A' - P_3' A)/A^3
Ag = sp.Function('Ag')(th); Pg = sp.Function('Pg')(th)
rep('S4e (P/A^2)\' = -(2 P A\' - P\' A)/A^3', sp.simplify(sp.diff(Pg/Ag**2, th) + (2*Pg*sp.diff(Ag, th) - sp.diff(Pg, th)*Ag)/Ag**3) == 0)
# Corollary-4.8 normalisation: bounded [Psi]_cos2 forces a_3 = O(eps): [Psi]_cos2 = a_3/(2 eps) - a_1/(2(4 - eps))
# S5: (d) constants
A0 = sp.cos(th)**2; Pr = -5*sp.cos(th)/12 - sp.cos(3*th)/20
Psi1A0 = (-(3*p + 2)/(4*p*(p + 2))*sp.cos(th) - sp.cos(3*th)/(4*(p + 4))).subs(p, 1)
rep('S5a Psi_ref = Psi_1[A_0] from 4.7(iii) at p = 1', sp.simplify(Psi1A0 - Pr) == 0)
PsiA0 = Psi_of(sp.Rational(1, 2) + sp.cos(2*th)/2, p, 3)
rep('S5b 4.7(iii) formula Psi_p[cos^2 th] = -(3p+2)/(4p(p+2)) cos th - cos 3th/(4(p+4)) (re-derived)',
    sp.simplify(PsiA0 - (-(3*p + 2)/(4*p*(p + 2))*sp.cos(th) - sp.cos(3*th)/(4*(p + 4)))) == 0)
xs = [mp.mpf(k)*2*mp.pi/20000 for k in range(20000)]
fP = sp.lambdify(th, Pr, 'mpmath'); fPd = sp.lambdify(th, sp.diff(Pr, th), 'mpmath'); fA0d = sp.lambdify(th, sp.diff(A0, th), 'mpmath')
mP = max(abs(fP(x)) for x in xs); mPd = max(abs(fPd(x)) for x in xs); mA0d = max(abs(fA0d(x)) for x in xs)
rep('S5c sup|Psi_ref| = %s <= 7/15 (attained at th = 0), sup|Psi_ref\'| = %s <= 17/30, sup|A_0\'| = %s = 1' % (mp.nstr(mP, 8), mp.nstr(mPd, 8), mp.nstr(mA0d, 8)),
    mP <= mp.mpf(7)/15 + mp.mpf('1e-25') and abs(fP(0) + mp.mpf(7)/15) < mp.mpf('1e-25') and mPd <= mp.mpf(17)/30 and abs(mA0d - 1) < 1e-8)
J1 = 2*Pr*sp.diff(A0, th) - sp.diff(Pr, th)*A0
rep('S5d J_1(A_0, Psi_ref)(pi/4) = 9 sqrt(2)/40', sp.simplify(J1.subs(th, sp.pi/4) - 9*sp.sqrt(2)/40) == 0, sp.nsimplify(J1.subs(th, sp.pi/4)))
d = sp.symbols('delta', positive=True)
rep('S5e 2 d(1+d) + 2(7/15) d + d(1+d) + (17/30) d = (9/2 + 3 d) d; 7/15 + 17/30 = 31/30',
    sp.expand(2*d*(1 + d) + 2*sp.Rational(7, 15)*d + d*(1 + d) + sp.Rational(17, 30)*d - (sp.Rational(9, 2) + 3*d)*d) == 0 and sp.Rational(7, 15) + sp.Rational(17, 30) == sp.Rational(31, 30))
Jp_ref = (p + 1)*Pr*sp.diff(A0, th) - p*sp.diff(Pr, th)*A0
rep('S5f J_p(A_0, Psi_ref) - J_1(A_0, Psi_ref) = (p - 1)(Psi_ref A_0\' - Psi_ref\' A_0)', sp.simplify(Jp_ref - J1 - (p - 1)*(Pr*sp.diff(A0, th) - sp.diff(Pr, th)*A0)) == 0)
v = sp.Rational(63, 200) - sp.Rational(453, 10000) - sp.Rational(31, 3000)
rep('S5g 63/200 - 453/10000 - 31/3000 = 1/4 + 281/30000; sqrt 2 > 7/5; (9/2 + 3/100)/100 = 453/10000; 9 (7/5)/40 = 63/200',
    v - sp.Rational(1, 4) == sp.Rational(281, 30000) and sp.sqrt(2) > sp.Rational(7, 5) and (sp.Rational(9, 2) + sp.Rational(3, 100))/100 == sp.Rational(453, 10000)
    and 9*sp.Rational(7, 5)/40 == sp.Rational(63, 200), v)
# randomized adversarial check of (d): perturb a and psi in C^1 by <= delta (smooth perturbations), p in (0.99, 1)
random.seed(1)
fA = lambda x: mp.cos(x)**2; fAd = lambda x: -mp.sin(2*x)
minsup = mp.inf
grid = [mp.mpf(k)*2*mp.pi/400 for k in range(400)]
for trial in range(300):
    pv = mp.mpf('0.99') + mp.mpf('0.01')*random.random()
    # perturbations g(x) = sum c_k cos(k x + phi_k), scaled so that max(sup|g|, sup|g'|) <= delta
    def mk():
        K = random.randint(1, 4); cs = [(random.uniform(-1, 1), random.randint(0, 3), random.uniform(0, 6.3)) for _ in range(K)]
        g = lambda x: sum(c*mp.cos(k*x + ph) for c, k, ph in cs); gd = lambda x: sum(-c*k*mp.sin(k*x + ph) for c, k, ph in cs)
        s = max(max(abs(g(x)) for x in grid), max(abs(gd(x)) for x in grid))
        s = s*(1 + mp.mpf('1e-3'))
        return (lambda x: g(x)/s/100), (lambda x: gd(x)/s/100)
    ga, gad = mk(); gp, gpd = mk()
    sgn = random.choice([-1, 1])
    J = lambda x: (pv + 1)*(fP(x) + gp(x))*(fAd(x) + gad(x)) - pv*(fPd(x) + gpd(x))*(fA(x) + ga(x))
    sup = max(abs(J(x)) for x in grid)
    minsup = min(minsup, sup)
rep('N1 (d) randomized: min over 300 perturbed pairs of sup |J_p(a, psi)| = %s > 1/4' % mp.nstr(minsup, 6), minsup > mp.mpf(1)/4)
# worst case at pi/4 by the bound: J_1(pi/4) - (9/2 + 3 delta) delta - 31/3000
print('   bound at pi/4: %s' % mp.nstr(9*mp.sqrt(2)/40 - (mp.mpf(9)/2 + mp.mpf(3)/100)/100 - mp.mpf(31)/3000, 10))

# S6: (a), (b) algebra
rep('S6a int_0^{2pi} (sin 3th)_+ = 2, int |sin 3th| = 4', abs(mp.quad(lambda x: max(mp.sin(3*x), 0), mp.linspace(0, 2*mp.pi, 7)) - 2) < 1e-20 and abs(mp.quad(lambda x: abs(mp.sin(3*x)), mp.linspace(0, 2*mp.pi, 7)) - 4) < 1e-20)
H2, Cp, Hs, Cs, gm = sp.symbols('H2 Cp H C gamma', positive=True)
pq = sp.symbols('q', positive=True)   # stands for p in (0,1)
R = (Cp/H2)**(1/(2 - pq))
rep('S6b H_2 R^2 = C_p R^p at R = (C_p/H_2)^(1/(2-p))', sp.simplify(sp.powsimp(sp.expand_power_base(H2*R**2 - Cp*R**pq, force=True), force=True)) == 0
    or all(abs(float((H2*R**2 - Cp*R**pq).subs({H2: h, Cp: c, pq: q}))) < 1e-9 for h, c, q in [(1.3, 2.1, 0.4), (5, 0.2, 0.9)]))
val = H2*R + Cp*R**(pq - 1)/(1 - pq); tgt = (2 - pq)/(1 - pq)*H2**((1 - pq)/(2 - pq))*Cp**(1/(2 - pq))
rep('S6c int M r^{-2} = H_2 R + C_p R^{p-1}/(1-p) = ((2-p)/(1-p)) H_2^((1-p)/(2-p)) C_p^(1/(2-p)) (numeric, 3 points)',
    all(abs(float((val - tgt).subs({H2: h, Cp: c, pq: q}))) < 1e-9*float(tgt.subs({H2: h, Cp: c, pq: q})) for h, c, q in [(1.3, 2.1, 0.4), (5, 0.2, 0.9), (1, 7, 0.05)]))
for h, c, q in [(1.3, 2.1, 0.4), (5, 0.2, 0.9)]:
    lR = mp.log((mp.mpf(c)/h)**(1/(2 - mp.mpf(q))))   # r = e^u: int min(H r^2, C r^p) r^{-1} du, split at log R
    I = mp.quad(lambda u: min(h*mp.exp(2*u), c*mp.exp(q*u))*mp.exp(-u), [-mp.inf, lR, lR + 50, mp.inf])
    rep('S6d direct quadrature of int min(H_2 r^2, C_p r^p) r^{-2} at (%s, %s, %s)' % (h, c, q), abs(I - float(tgt.subs({H2: h, Cp: c, pq: q}))) < 1e-8*I, mp.nstr(I, 10))
X = sp.symbols('X', positive=True)
# (2-p)/(2p) <= (2/pi)((2-p)/(1-p)) X  <=>  (1-p)/p <= (4/pi) X ;  (1-p)/p = l - 1
rep('S6e (2/pi)((2-p)/(1-p)) X / ((2-p)/(2p)) = (4/pi) X / ((1-p)/p); (1-p)/p = l - 1 for l = 1/p',
    sp.simplify((2/sp.pi)*((2 - pq)/(1 - pq))*X/((2 - pq)/(2*pq)) - (4/sp.pi)*X/((1 - pq)/pq)) == 0 and sp.simplify((1 - pq)/pq - (1/pq - 1)) == 0)
e1 = 2*(1 - pq)/(2 - pq); e2 = pq/(2 - pq)
rep('S6f exponents 2(1-p)/(2-p) + p/(2-p) = 1 and H^((1-p)/(2-p)) C^(1/(2-p)) = sqrt(HC)^e1 C^e2', sp.simplify(e1 + e2 - 1) == 0 and
    all(abs(float((Hs**((1 - pq)/(2 - pq))*Cs**(1/(2 - pq)) - sp.sqrt(Hs*Cs)**e1*Cs**e2).subs({Hs: h, Cs: c, pq: q}))) < 1e-12 for h, c, q in [(2, 3, 0.3), (9, 0.5, 0.8)]))
lv = sp.symbols('lv', positive=True)
expr = Hs**(1/lv - 1)*(sp.pi/4)**(2 - 1/lv)*(lv - 1)**(2 - 1/lv)/lv**2
rep('S6g H^(p-1) (pi/4)^(2-p) (l-1)^(2-p)/l^2 -> pi^2/(16 H) as l -> infinity (p = 1/l)', sp.simplify(sp.limit(expr, lv, sp.oo) - sp.pi**2/(16*Hs)) == 0)
# the c = l - 1/2 identity with p
rep('S6h l - 1/2 = (2-p)/(2p) for l = 1/p', sp.simplify(1/pq - sp.Rational(1, 2) - (2 - pq)/(2*pq)) == 0)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
