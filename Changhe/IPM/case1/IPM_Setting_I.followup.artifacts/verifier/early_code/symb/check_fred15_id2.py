"""verifier: fred15 (28) for B_3, robust version, cross-checked against an independent representation.
Trace: w = w_R12 + eps x^3 (L^2 - x^2)^2 (odd, w'(0) = -A, w(L) = 0, w'(L) = A); a = -w/(L - x) in closed form.
(i)  (28) with the finite part (10) at split radius r (must not depend on r);
(ii) the m-polynomial representation B_3 = ((beta-1)/(3 A^beta)) int_0^L (Q - P(m) - Q*) m^(beta-2) (A/g) dx,
     P from fred11 (4) with the trace's d3, d5, d7, [0, x0] by power series (x^5 (Q - P(m)) checked to vanish through x^5),
     m^(beta-2)/g = A^(beta-2) x^(-beta) V.
Tails [r, L]: s = L - x = u^(1/beta), integrand s^(beta-1) F(s) ds = F du / beta, s clamped >= 1e-18 (dps 45).
g = x^2 exp(int_0^x ((w'-A)/w - 2/t) dt) = x^2 z e^E."""
import sys, time
import sympy as sp, mpmath as mp
mp.mp.dps = 45
x = sp.Symbol('x', positive=True)
EE = sp.Symbol('EE')
NS = 18

def setup(Av, Lv, eps):
    Av = sp.nsimplify(Av); Lv = sp.nsimplify(Lv); eps = sp.nsimplify(eps)
    bev = 2/Av
    ax = Av*x*(Lv + x)/(Lv**2 + x**2) - eps*x**3*(Lv - x)*(Lv + x)**2
    wx = sp.expand(-(Lv - x)*ax)
    zx = sp.cancel(-wx/(Av*x))
    Eser = sp.integrate(sp.series(sp.cancel((1/zx - 1)/x), x, 0, NS).removeO(), x)
    Dzx = x*sp.diff(zx, x); Jx = 2*sp.diff(zx, x)/x + sp.diff(zx, x, 2)
    Tx = zx**-4/2*(sp.exp(-(bev+1)*EE)*(1 + zx + Dzx) + Av*sp.exp(-(bev+2)*EE)*Jx)
    Tser = sp.expand(sp.series(Tx.subs(EE, Eser), x, 0, NS).removeO())
    ratio = sp.cancel((sp.diff(wx, x) - Av)/wx)
    # Laurent series of Q and of m for the P(m) representation
    gser = sp.expand(sp.series(x**2*zx*sp.exp(Eser), x, 0, NS + 2).removeO())
    Qser = sp.expand(sp.series((sp.diff(gser, x) - sp.diff(wx, x, 2))/(2*gser**3), x, 0, NS - 6).removeO())
    mser = sp.expand(sp.series(Av*sp.exp(-Eser)/x, x, 0, NS - 4).removeO())
    wjet = sp.expand(sp.series(wx, x, 0, 9).removeO())
    d3, d5, d7 = [wjet.coeff(x, k) for k in (3, 5, 7)]
    A_ = Av
    q5 = (1 - 3*d3)/A_**5
    q3 = -(10*A_*d5 + 12*d3**2 - 3*d3)/A_**4
    q1 = -(168*A_**2*d7 + 324*A_*d3*d5 - 10*A_*d5 + 144*d3**3 - 21*d3**2)/(8*A_**3)
    Pm = q5*mser**5 + q3*mser**3 + q1*mser
    QmP = sp.expand(sp.series(Qser - Pm, x, 0, NS - 8).removeO())
    Vser = sp.expand(sp.series(sp.exp((1 - bev)*Eser)/zx, x, 0, NS - 6).removeO())
    lam = lambda e: sp.lambdify(x, e, 'mpmath')
    S = dict(A=mp.mpf(sp.N(Av, 60)), be=mp.mpf(sp.N(bev, 60)), L=mp.mpf(sp.N(Lv, 60)),
             a=lam(ax), w=lam(wx), z=lam(zx), Dz=lam(Dzx), J=lam(Jx), wpp=lam(sp.diff(wx, x, 2)),
             ratio=lam(ratio), rr=lam(sp.cancel(ratio - 2/x)),
             Tc={j: mp.mpf(str(sp.N(Tser.coeff(x, j), 55))) for j in range(NS)},
             qmp={j: mp.mpf(str(sp.N(QmP.coeff(x, j), 55))) for j in range(-6, NS - 8)},
             vc={j: mp.mpf(str(sp.N(Vser.coeff(x, j), 55))) for j in range(NS - 6)},
             q=(q5, q3, q1), d=(d3, d5, d7))
    S['q'] = tuple(mp.mpf(str(sp.N(v, 55))) for v in S['q'])
    return S

def funcs(S):
    A, be, L = S['A'], S['be'], S['L']
    def g(xx): return xx**2*mp.e**mp.quad(S['rr'], [0, xx])
    def Q(xx):
        gg = g(xx); return (gg*S['ratio'](xx) - S['wpp'](xx))/(2*gg**3)
    return g, Q

def tail(S, r, Fs):
    be, L = S['be'], S['L']
    ell = L - mp.mpf(r)
    def h(u):
        s = max(u**(1/be), mp.mpf(10)**-18)
        return Fs(s)/be
    return mp.quad(h, [0, ell**be/4, ell**be])

def B3_28(S, r):
    A, be, L = S['A'], S['be'], S['L']; Tc = S['Tc']
    g, Q = funcs(S); Qst = Q(L); rm = mp.mpf(r)
    def Efun(xx): return mp.log(g(xx)/(xx**2*S['z'](xx)))
    def Tfun(xx):
        Ee = Efun(xx); zz = S['z'](xx)
        return zz**-4/2*(mp.e**(-(be+1)*Ee)*(1 + zz + S['Dz'](xx)) + A*mp.e**(-(be+2)*Ee)*S['J'](xx))
    def Vfun(xx): return mp.e**((1-be)*Efun(xx))/S['z'](xx)
    a0 = rm*mp.mpf('0.03')
    FP = sum(Tc[j]*rm**(j-4-be)/(j-4-be) for j in (0, 2, 4))
    FP += sum(Tc[j]*a0**(j-4-be)/(j-4-be) for j in range(6, NS, 2))
    FP += mp.quad(lambda xx: xx**(-5-be)*(Tfun(xx) - Tc[0] - Tc[2]*xx**2 - Tc[4]*xx**4), [a0, rm/3, rm])
    origin = FP - Qst*mp.quad(lambda xx: xx**(-be)*Vfun(xx), [0, rm])
    def Fs(s):
        xx = L - s; gg = g(xx)
        return (Q(xx) - Qst)/s*S['a'](xx)**(be-2)*gg**(1-be)
    return (be-1)/(3*A)*origin + (be-1)*A**(1-be)/3*tail(S, r, Fs)

def B3_Pm(S, r, x0='0.05'):
    A, be, L = S['A'], S['be'], S['L']
    g, Q = funcs(S); Qst = Q(L); q5, q3, q1 = S['q']
    neg = max(abs(S['qmp'][j]) for j in range(-6, 1))
    # series part on [0, x0]: (Q - P(m) - Q*) V x^(-beta)
    x0 = mp.mpf(x0)
    RV = {}
    for j in range(0, NS - 8):
        RV[j] = sum((S['qmp'][k] if k >= 1 else (-Qst if k == 0 else 0))*S['vc'][j-k] for k in range(0, j + 1) if (j - k) in S['vc'])
    ser = A**(be-1)*sum(c*x0**(j+1-be)/(j+1-be) for j, c in RV.items())
    def P(m): return q5*m**5 + q3*m**3 + q1*m
    def mid(xx):
        gg = g(xx); m = -S['w'](xx)/gg
        return (Q(xx) - P(m) - Qst)*m**(be-2)*A/gg
    midv = mp.quad(mid, [x0, (x0 + mp.mpf(r))/2, mp.mpf(r)])
    def Fs(s):
        xx = L - s; gg = g(xx); m = s*S['a'](xx)/gg
        return A*(Q(xx) - P(m) - Qst)/s*S['a'](xx)**(be-2)*gg**(1-be)
    tl = tail(S, r, Fs)
    return (be-1)/(3*A**be)*(ser + midv + tl), neg

def closed(Av, Lv):
    Am, Lm = mp.mpf(Av), mp.mpf(Lv); bm = 2/Am
    C = (16-bm)/(3*Am*(4+bm))*mp.beta(2-bm/2, bm); S = 6*Am*(4*Am-3)/(8*Am-1)
    return C*Lm**(-4-bm)*(1 - S/Lm**2)

cases = [('4', '4', '0'), ('10.15', '8.6', '0'), ('4', '4', '0.0001'), ('4', '4', '0.001'), ('10.15', '8.6', '0.00001')]
for Av, Lv, ep in cases:
    t0 = time.time(); S = setup(Av, Lv, ep)
    ref = closed(Av, Lv) if ep == '0' else None
    print('A=%s L=%s eps=%s  d3,d5,d7 = %s  (setup %.0fs)' % (Av, Lv, ep, [str(sp.N(v, 8)) for v in S['d']], time.time()-t0), flush=True)
    if ref is not None:
        print('   closed (38)-(39)          = %s' % mp.nstr(ref, 22))
    for r in ('0.25', '0.5', '1'):
        t0 = time.time(); v = B3_28(S, r)
        print('   (28) r=%-4s               = %s%s  [%.0fs]' % (r, mp.nstr(v, 22), ('   rel %s' % mp.nstr(abs(v/ref - 1), 3)) if ref else '', time.time()-t0), flush=True)
    t0 = time.time(); v, neg = B3_Pm(S, '1')
    print('   P(m) representation        = %s%s  [max |coef of x^k, k<=0, in Q-P(m)| = %s, %.0fs]' % (mp.nstr(v, 22), ('   rel %s' % mp.nstr(abs(v/ref - 1), 3)) if ref else '', mp.nstr(neg, 3), time.time()-t0), flush=True)
