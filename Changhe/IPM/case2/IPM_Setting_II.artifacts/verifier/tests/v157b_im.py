"""V157b: FR 4.2, the L-family rho = x^2 (1 + M y^2/L^2) e^{-r^2/L^2}, L = 1/100, l = 2, M = 0, 3 (replaces part N3b of
v157_app910.py, whose cross-check tolerance 1e-15 on a nested quadrature at 20 digits was too tight; N4 repeated here).
By scaling (rho = L^2 f(X/L), f = x^2 (1 + M y^2) e^{-r^2}) the axis velocity is w(y) = L^2 w_f(y/L), w_f even in y, and
    I_M = int_0^inf w_e/(B_+ B_-) dr = L int_0^inf w_f(s)/(l^2 s^2 - L^2 w_f(s)^2) ds.
w_f in closed form: U_2^ = -xi_1^2/|xi|^2 rho^, 1/|xi|^2 = int_0^inf e^{-t|xi|^2} dt, both Gaussian integrals and the t-integral
exact in sympy; checked against the nested quadrature of the t-integral at two heights.
Prints, besides the FR claims, the quantities a derivation of the 3/9999 bound would need: Q = sup_s |w_f(s)/s| and
R = int |w_f|/s^2 / |int w_f/s^2|. With q = L Q/l, |I_M - I_M^0| <= (q^2/(1 - q^2)) (L/l^2) int |w_f|/s^2.
"""
import sys
import sympy as sp
import mpmath as mp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

X1, X2, t, s = sp.symbols('xi1 xi2 t s', real=True); up = sp.symbols('up', positive=True); sP = sp.symbols('sP', positive=True)
g1 = sp.sqrt(sp.pi)*(sp.Rational(1, 2) - X1**2/4)*sp.exp(-X1**2/4)            # FT of x^2 e^{-x^2}
assert sp.simplify(sp.integrate(sp.exp(-sp.I*X1*s)*s**2*sp.exp(-s**2), (s, -sp.oo, sp.oo)) - g1) == 0
g2e = lambda M: sp.sqrt(sp.pi)*(1 + M*(sp.Rational(1, 2) - X2**2/4))*sp.exp(-X2**2/4)   # FT of (1 + M y^2) e^{-y^2}
for M in [0, 3]:
    assert sp.simplify(sp.integrate(sp.exp(-sp.I*X2*s)*(1 + M*s**2)*sp.exp(-s**2), (s, -sp.oo, sp.oo)) - g2e(M)) == 0
T1 = sp.simplify(sp.integrate(X1**2*sp.exp(-t*X1**2)*g1, (X1, -sp.oo, sp.oo), conds='none'))
def integrand(M):
    T2 = sp.simplify(sp.integrate(sp.exp(-t*X2**2)*g2e(M)*(sp.cos(X2*sP) - 1), (X2, -sp.oo, sp.oo), conds='none'))
    return sp.simplify(T1*T2)
Lr = mp.mpf(1)/100; lr = mp.mpf(2)
mp.mp.dps = 40
res = {}
for M in [0, 3]:
    Ie = integrand(M)
    wcl = sp.simplify(-sp.integrate(sp.expand(Ie.subs(t, up - sp.Rational(1, 4))), (up, sp.Rational(1, 4), sp.oo), conds='none')/(4*sp.pi**2))
    print('   M = %d: w_f(s) =' % M, wcl, flush=True)
    wf_cl = sp.lambdify(sP, wcl, 'mpmath')
    f = sp.lambdify((t, sP), Ie, 'mpmath')
    errs = []
    for sv in [mp.mpf('0.7'), mp.mpf('2.5')]:
        wq = -mp.quad(lambda tv: f(tv, sv), [0, 1, 10, mp.inf])/(4*mp.pi**2)
        errs.append(abs(wq - wf_cl(sv)))
    rep('C%d closed form w_f = nested t-quadrature at s = 0.7, 2.5 (M = %d)' % (M, M), max(errs) < mp.mpf('1e-25'), mp.nstr(max(errs), 3))
    # series at 0 for small s (the closed form has 1/s^6 cancellations)
    ser = sp.series(wcl, sP, 0, 26).removeO()   # truncation error O(s^26): below 1e-30 relative for s <= 0.05 (order 10 gave 1e-13)
    wser = sp.lambdify(sP, ser, 'mpmath')
    def wf(sv):
        with mp.workdps(80):
            return wf_cl(mp.mpf(sv)) if sv > mp.mpf('0.05') else wser(mp.mpf(sv))
    rep('C%d series and closed form agree at s = 0.05 (M = %d)' % (M, M), abs(wser(mp.mpf('0.05')) - wf_cl(mp.mpf('0.05'))) < mp.mpf('1e-15'))
    lim = sp.limit(wcl, sP, sp.oo)
    print('   M = %d: w_f(0) = %s, w_f\'\'(0)/2 = %s, w_f(inf) = %s' % (M, sp.nsimplify(ser.subs(sP, 0)), sp.simplify(ser.coeff(sP, 2)), lim))
    br = [0, mp.mpf('0.05'), 0.5, 1, 2, 4, 8, 20, 100, mp.inf]
    IM = Lr*mp.quad(lambda sv: wf(sv)/(lr**2*sv**2 - Lr**2*wf(sv)**2), br)
    IM0 = (Lr/lr**2)*mp.sqrt(mp.pi)*(5*M - 14)/105
    chk0 = Lr/lr**2*mp.quad(lambda sv: wf(sv)/sv**2, br)
    absint = mp.quad(lambda sv: abs(wf(sv))/sv**2, sorted(set(br[:-1] + [mp.mpf(z)/20 for z in range(1, 200)])) + [mp.inf])
    Q = max(abs(wf(mp.mpf(z)/50))/(mp.mpf(z)/50) for z in range(1, 2000))
    rel = abs(IM - IM0)/abs(IM0)
    rep('N3b M = %d: int_0^inf w_f/s^2 by quadrature = sqrt(pi)(5M - 14)/105 (relative error < 1e-25)' % M,
        abs(chk0 - IM0) < mp.mpf('1e-25')*abs(IM0), mp.nstr(abs(chk0 - IM0)/abs(IM0), 3))
    rep('N3c M = %d: I_M = %s, I_M^0 = %s, |I_M - I_M^0|/|I_M^0| = %s < 3/9999; sign as stated' % (M, mp.nstr(IM, 10), mp.nstr(IM0, 10), mp.nstr(rel, 4)),
        rel < mp.mpf(3)/9999 and ((M == 0 and IM < 0) or (M == 3 and IM > 0)))
    q = Lr*Q/lr
    print('   M = %d: Q = sup |w_f(s)/s| (grid s <= 40) = %s, q = L Q/l = %s, R = int|w_f|/s^2 / |int w_f/s^2| = %s, a priori bound (q^2/(1-q^2)) R = %s'
          % (M, mp.nstr(Q, 8), mp.nstr(q, 6), mp.nstr(absint/abs(chk0*lr**2/Lr), 6), mp.nstr(q**2/(1 - q**2)*absint/abs(chk0*lr**2/Lr), 6)), flush=True)
    res[M] = (IM, IM0, rel)

# N4: |DW| <= (1/4 pi^2) int |xi_1| |rho^| dxi; DU^ = i xi (x) (xi_1 xi_2, -xi_1^2) rho^/|xi|^2 has operator norm |xi_1| |rho^|
mp.mp.dps = 30
a1 = sp.lambdify(X1, g1, 'mpmath')
int1 = 2*mp.quad(lambda z: z*abs(a1(z)), [0, mp.sqrt(2), 6, 20, mp.inf])
for M in [0, 3]:
    a2 = sp.lambdify(X2, g2e(M), 'mpmath')
    br = [0, mp.sqrt(2 + mp.mpf(4)/M), 8, 20, mp.inf] if M > 0 else [0, 8, 20, mp.inf]
    int2 = 2*mp.quad(lambda z: abs(a2(z)), br)
    bnd = int1*int2/(4*mp.pi**2)
    rep('N4 M = %d: (1/4 pi^2) int |xi_1| |rho_f^| = %s <= 37 sqrt(pi)/2 = %s (so |DW| <= L times it < l = 2)' % (M, mp.nstr(bnd, 10), mp.nstr(37*mp.sqrt(mp.pi)/2, 10)),
        bnd <= 37*mp.sqrt(mp.pi)/2 and Lr*bnd < lr)
# the operator norm of the rank-one matrix a b^T is |a||b|: |xi| |(xi_1 xi_2, -xi_1^2)|/|xi|^2 = |xi_1|
a_, b_ = sp.symbols('a b', real=True)
rep('N4b |xi| |(xi_1 xi_2, -xi_1^2)| / |xi|^2 = |xi_1|', sp.simplify(sp.sqrt(a_**2 + b_**2)*sp.sqrt((a_*b_)**2 + a_**4)/(a_**2 + b_**2) - sp.Abs(a_)) == 0)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
