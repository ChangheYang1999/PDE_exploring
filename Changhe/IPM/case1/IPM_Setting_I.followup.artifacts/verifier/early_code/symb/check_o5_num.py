"""verifier: request (o5), numerical parts (own code; definitions of check_fred15_id2.py reused, its driver not run).
(a) items 1, 3: for 1 < A < 2, B_3 on R12 (and R12 + eps x^3 (L^2 - x^2)^2) by two own representations with g rebuilt
    from w by quadrature: (I) the convergent m-form without Q* (beta > 1),
    B_3 = ((beta - 1)/(3 A^beta)) int_0^L (Q - P(m)) m^(beta - 2) (A/g) dx, and (II) the finite part
    B_3 = (1/(3 A^beta)) f.p. int_0^L Q' m^(beta - 1) dx; on R12 against C_A L^(-4-beta) (1 - S_A/L^2).
(b) item 5: delta B_3 by the variation formula of the 6.4 item,
    delta B_3 = -f.p. int_0^L [delta F_3/(w H_3) - (F_3/(w H_3)) (V/w + (3 + beta) eta - beta V/w)] dx,
    at A = 4, L = 4, V = x^3 (L^2 - x^2)^2, against central differences of B_3 computed with (28) (check_fred15_id2)."""
import sys, time
import sympy as sp, mpmath as mp
_src = open(__file__.replace('check_o5_num.py', 'check_fred15_id2.py')).read()
exec(_src[:_src.index('cases = [')])
mp.mp.dps = 45

def extra(S, Av, Lv, eps):
    """Q' and series of Q' m^(beta-1) x^(beta-1) (a Laurent series in x)."""
    Av = sp.nsimplify(Av); Lv = sp.nsimplify(Lv); eps = sp.nsimplify(eps); bev = 2/Av
    ax = Av*x*(Lv + x)/(Lv**2 + x**2) - eps*x**3*(Lv - x)*(Lv + x)**2
    wx = sp.expand(-(Lv - x)*ax); zx = sp.cancel(-wx/(Av*x))
    Eser = sp.integrate(sp.series(sp.cancel((1/zx - 1)/x), x, 0, NS).removeO(), x)
    gser = sp.expand(sp.series(x**2*zx*sp.exp(Eser), x, 0, NS + 2).removeO())
    Qser = sp.series((sp.diff(gser, x) - sp.diff(wx, x, 2))/(2*gser**3), x, 0, NS - 6).removeO()
    # Q' m^(beta-1) = A^(beta-1) x^(1-beta) Q' e^(-(beta-1)E)
    Ks = sp.expand(sp.series(sp.diff(Qser, x)*sp.exp(-(bev - 1)*Eser), x, 0, NS - 8).removeO())
    S['kc'] = {j: mp.mpf(str(sp.N(Ks.coeff(x, j), 55))) for j in range(-6, NS - 8)}
    S['w3'] = sp.lambdify(x, sp.diff(wx, x, 3), 'mpmath')
    S['ratiop'] = sp.lambdify(x, sp.cancel(sp.diff(sp.cancel((sp.diff(wx, x) - Av)/wx), x)), 'mpmath')
    return S

def Qprime(S, g):
    def Qp(xx):
        gg = g(xx); rt = S['ratio'](xx); gp = gg*rt
        return (gp*rt + gg*S['ratiop'](xx) - S['w3'](xx))/(2*gg**3) - 3*(gg*rt - S['wpp'](xx))*gp/(2*gg**4)
    return Qp

def tail_p(S, r, Fs, p):
    """int_r^L s^(p-1) Fs(s) ds with s = L - x, by u = s^p."""
    L = S['L']; ell = L - mp.mpf(r)
    def h(u):
        s = max(u**(1/p), mp.mpf(10)**-18)
        return Fs(s)/p
    return mp.quad(h, [0, ell**p/4, ell**p])

def B3_mform_nosub(S, r='1', x0='0.05'):
    A, be, L = S['A'], S['be'], S['L']
    g, Q = funcs(S); q5, q3, q1 = S['q']
    x0 = mp.mpf(x0)
    RV = {}
    for j in range(0, NS - 8):
        RV[j] = sum((S['qmp'][k] if k >= 1 else 0)*S['vc'][j-k] for k in range(0, j + 1) if (j - k) in S['vc'])
    ser = A**(be-1)*sum(cc*x0**(j+1-be)/(j+1-be) for j, cc in RV.items())
    P = lambda m: q5*m**5 + q3*m**3 + q1*m
    def mid(xx):
        gg = g(xx); m = -S['w'](xx)/gg
        return (Q(xx) - P(m))*m**(be-2)*A/gg
    midv = mp.quad(mid, [x0, (x0 + mp.mpf(r))/2, mp.mpf(r)])
    def Fs(s):     # (Q - P) m^(beta-2) A/g = s^(beta-2) A (Q - P) a^(beta-2) g^(1-beta)
        xx = L - s; gg = g(xx); m = s*S['a'](xx)/gg
        return A*(Q(xx) - P(m))*S['a'](xx)**(be-2)*gg**(1-be)
    tl = tail_p(S, r, Fs, be - 1)
    return (be-1)/(3*A**be)*(ser + midv + tl)

def B3_fp(S, r='1'):
    A, be, L = S['A'], S['be'], S['L']
    g, Q = funcs(S); Qp = Qprime(S, g); rm = mp.mpf(r)
    a0 = rm*mp.mpf('0.03')
    # [0, a0]: A^(beta-1) x^(1-beta) sum kc_j x^j, finite part
    ser = A**(be-1)*sum(cc*a0**(j+2-be)/(j+2-be) for j, cc in S['kc'].items())
    def mid(xx):
        gg = g(xx); m = -S['w'](xx)/gg
        return Qp(xx)*m**(be-1)
    midv = mp.quad(mid, [a0, rm/3, rm])
    def Fs(s):     # m^(beta-1) = s^(beta-1) (a/g)^(beta-1)
        xx = L - s; gg = g(xx)
        return Qp(xx)*(S['a'](xx)/gg)**(be-1)
    tl = tail_p(S, r, Fs, be)
    return (ser + midv + tl)/(3*A**be)

def closedA(Av, Lv):
    Am, Lm = mp.mpf(Av), mp.mpf(Lv); bm = 2/Am
    J = lambda n: n/(n + bm - 1)*mp.beta((n - bm + 1)/2, bm - 1)
    CA = (bm - 1)*(J(5) + J(3))/(3*Am); SA = 6*Am*(4*Am - 3)/(8*Am - 1)
    return CA*Lm**(-4-bm)*(1 - SA/Lm**2), SA

part = sys.argv[1] if len(sys.argv) > 1 else 'ab'
if 'a' in part:
    print('(a) 1 < A < 2', flush=True)
    for Av in ('1.25', '1.5', '1.8'):
        SA = 6*sp.nsimplify(Av)*(4*sp.nsimplify(Av) - 3)/(8*sp.nsimplify(Av) - 1)
        for Lv, ep in ((sp.sqrt(SA), '0'), (sp.Rational(3, 2), '0'), (sp.Rational(3, 2), '0.01')):
            t0 = time.time()
            Lnum = sp.N(Lv, 50)
            S = setup(Av, Lnum, ep); S = extra(S, Av, Lnum, ep)
            v1 = B3_mform_nosub(S); v2 = B3_fp(S)
            ref, SAn = closedA(Av, mp.mpf(str(Lnum))) if ep == '0' else (None, None)
            print('A=%s L=%s eps=%s: m-form %s, f.p. form %s, diff %s%s  [neg coef %s, %.0fs]' % (
                Av, mp.nstr(mp.mpf(str(Lnum)), 12), ep, mp.nstr(v1, 20), mp.nstr(v2, 20), mp.nstr(v1 - v2, 3),
                ('' if ref is None else ', closed %s, diff %s' % (mp.nstr(ref, 20), mp.nstr(v1 - ref, 3))),
                mp.nstr(max(abs(S['qmp'][j]) for j in range(-6, 1)), 2), time.time() - t0), flush=True)
if 'b' in part:
    print('(b) variation formula at A = 4, L = 4, V = x^3 (L^2 - x^2)^2', flush=True)
    Av, Lv = sp.Integer(4), sp.Integer(4); bev = sp.Rational(1, 2)
    w0 = -Av*x*(Lv**2 - x**2)/(Lv**2 + x**2); g0 = x**2/(1 + x**2/Lv**2); V = x**3*(Lv**2 - x**2)**2
    assert sp.simplify(w0*sp.diff(g0, x) - (sp.diff(w0, x) - Av)*g0) == 0
    etap = sp.cancel((sp.diff(V, x) - sp.diff(g0, x)/g0*V)/w0)
    etapp = sp.cancel(sp.diff(etap, x))
    ETA, ETAP, ETAPP = sp.symbols('ETA ETAP ETAPP')
    a2 = (sp.diff(g0, x) - sp.diff(w0, x, 2))/2; a2p = sp.diff(a2, x)
    F3 = -a2*sp.diff(g0, x) + a2p*g0/3
    dg = g0*ETA; dgp = sp.diff(g0, x)*ETA + g0*ETAP; dgpp = sp.diff(g0, x, 2)*ETA + 2*sp.diff(g0, x)*ETAP + g0*ETAPP
    da2 = (dgp - sp.diff(V, x, 2))/2; da2p = (dgpp - sp.diff(V, x, 3))/2
    dF3 = -da2*sp.diff(g0, x) - a2*dgp + (da2p*g0 + a2p*dg)/3
    H3 = Av**bev*g0**(3 + bev)*(-w0)**(-bev)
    Psi = dF3/(w0*H3) - F3/(w0*H3)*(V/w0 + (3 + bev)*ETA - bev*V/w0)
    # series at 0: Psi x^(5 + beta) is a power series once eta is replaced by its series
    NSV = 16
    etaser = sp.integrate(sp.series(etap, x, 0, NSV + 2).removeO(), x)
    t = sp.Symbol('t', positive=True)        # x = t^2 makes x^(1/2) powers polynomial
    Psis = (Psi*x**(5 + bev)).subs({ETA: etaser, ETAP: sp.diff(etaser, x), ETAPP: sp.diff(etaser, x, 2)})
    Psis = sp.series(sp.simplify(Psis.subs(x, t**2)), t, 0, 2*NSV).removeO()
    pc = {}
    for k in range(0, 2*NSV):
        cc = Psis.coeff(t, k)
        if cc != 0: pc[sp.Rational(k, 2)] = mp.mpf(str(sp.N(cc, 50)))
    print('   powers of x in Psi x^(5+beta) near 0:', sorted(float(k) for k in pc)[:8])
    lam = lambda e: sp.lambdify(x, e, 'mpmath')
    P0 = lam(Psi.subs({ETA: 0, ETAP: etap, ETAPP: etapp}))
    P1 = lam(sp.diff(Psi, ETA))
    etapf = lam(etap)
    a0 = mp.mpf('0.03'); Lm = mp.mpf(4); bm = mp.mpf(1)/2
    def eta(xx):    # series on [0, 0.5], quadrature beyond
        x1 = mp.mpf('0.5')
        if xx <= x1:
            return sp.N(etaser.subs(x, sp.Float(str(xx), 50)), 50)
        return eta_half + mp.quad(etapf, [x1, xx])
    eta_half = mp.mpf(str(sp.N(etaser.subs(x, sp.Rational(1, 2)), 50)))
    def Psif(xx):
        return P0(xx) + P1(xx)*mp.mpf(str(eta(xx)))
    FP = sum(cc*a0**(k - 4 - bm)/(k - 4 - bm) for k, cc in pc.items())
    t0 = time.time()
    mid = mp.quad(Psif, [a0, mp.mpf('0.5'), 2, 3.5, 3.9])
    # near L: Psi ~ s^(beta - 1); u = s^beta
    tl = mp.quad(lambda u: Psif(Lm - max(u**2, mp.mpf(10)**-30))*2*u, [0, mp.mpf('0.1')**bm])
    dB_formula = -(FP + mid + tl)
    print('   delta B_3 (formula)          = %s  [%.0fs]' % (mp.nstr(dB_formula, 20), time.time() - t0), flush=True)
    # base value by the same route: B_3 = -f.p. int F3/(w H3)
    Bse = sp.series(sp.simplify((F3/(w0*H3)*x**(5 + bev)).subs(x, t**2)), t, 0, 2*NSV).removeO()
    bc = {sp.Rational(k, 2): mp.mpf(str(sp.N(Bse.coeff(t, k), 50))) for k in range(0, 2*NSV) if Bse.coeff(t, k) != 0}
    Bf = lam(F3/(w0*H3))
    B0 = -(sum(cc*a0**(k - 4 - bm)/(k - 4 - bm) for k, cc in bc.items()) + mp.quad(Bf, [a0, 0.5, 2, 3.9])
           + mp.quad(lambda u: Bf(Lm - max(u**2, mp.mpf(10)**-30))*2*u, [0, mp.mpf('0.1')**bm]))
    print('   B_3 = -f.p. int F3/(w H3)    = %s  (closed form %s)' % (mp.nstr(B0, 22), mp.nstr(closed('4', '4'), 22)), flush=True)
    for h in ('1e-7', '1e-8'):
        t0 = time.time()
        Sp = setup('4', '4', h); Sm = setup('4', '4', '-' + h)
        bp = B3_28(Sp, '1'); bmn = B3_28(Sm, '1')
        print('   central difference h=%s     = %s  [%.0fs]' % (h, mp.nstr((bp - bmn)/(2*mp.mpf(h)), 20), time.time() - t0), flush=True)
