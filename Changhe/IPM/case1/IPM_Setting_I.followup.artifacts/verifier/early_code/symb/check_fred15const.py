"""verifier: fred15 03-quantitative-exclusion, numeric evaluation of every constant (13)-(36) for the reference
w0 = -4x(1-(x/4)^2)/(1+(x/4)^2), A0 = 4, L = 4, r = 1/4, sigma = 1, theta = 3/4, d = 1e-4, h = 1/2,
(I) with the reference inputs stated in Section 6, (II) with the reference norms computed here (sup by dense sampling,
Hoelder seminorms bounded above by ||f'||_inf ell^(1-theta) and also estimated from below by pair sampling).
Each claimed bound of Section 6 is compared with the value (natural logs for the huge ones)."""
import mpmath as mp, sympy as sp
mp.mp.dps = 30
X = sp.Symbol('x', positive=True)
A0, L, r, sig, th, d, hA = 4, 4, mp.mpf(1)/4, 1, mp.mpf(3)/4, mp.mpf('1e-4'), mp.mpf(1)/2
A = mp.mpf(A0); be = 2/A; p = 4 + sig; ell = L - r
w0 = -4*X*(1 - (X/4)**2)/(1 + (X/4)**2)
z0 = sp.cancel(-w0/(4*X)); D0 = sp.cancel(X*sp.diff(z0, X)); J0 = sp.cancel(-sp.diff(w0, X, 2)/(4*X))
a0 = sp.cancel(-w0/(L - X))

def normA(f):
    ser = sp.series(f, X, 0, 6).removeO()
    c = [mp.mpf(str(sp.N(ser.coeff(X, j), 40))) for j in (0, 2, 4)]
    fl = sp.lambdify(X, f, 'mpmath')
    R = lambda xx: abs(fl(xx) - c[0] - c[1]*xx**2 - c[2]*xx**4)/(xx/r)**p
    sup = max(R(r*mp.mpf(k)/4000) for k in range(40, 4001))
    return abs(c[0]) + abs(c[1])*r**2 + abs(c[2])*r**4 + sup

def sup_on(f, a, b, n=20000):
    fl = sp.lambdify(X, f, 'mpmath')
    return max(abs(fl(a + (b - a)*mp.mpf(k)/n)) for k in range(n + 1))

def hoelder_low(f, a, b, n=400):
    fl = sp.lambdify(X, f, 'mpmath'); xs = [a + (b - a)*mp.mpf(k)/n for k in range(n + 1)]; v = [fl(t) for t in xs]
    return max(abs(v[i] - v[j])/abs(xs[i] - xs[j])**th for i in range(n + 1) for j in range(i))

def C0th(f):   # upper bound and pair-sampled lower estimate of ||f||_{C^{0,theta}([r,L])}
    s = sup_on(f, r, L); s1 = sup_on(sp.diff(f, X), r, L)
    return s + s1*ell**(1 - th), s + hoelder_low(f, r, L), s, s1

eta0 = normA(z0 - 1); D0s = normA(D0); J0s = normA(J0)
q = r**2/16
print('eta0 = %s  (claim <= 2q+2q^2+2q^3 = %s)' % (mp.nstr(eta0, 12), mp.nstr(2*q + 2*q**2 + 2*q**3, 12)))
print('D0*  = %s  (claim <= 4q/(1-q)^2 = %s)' % (mp.nstr(D0s, 12), mp.nstr(4*q/(1 - q)**2, 12)))
print('J0*  = %s  (claim <= (3+q)/(4(1-q)^3) = %s)' % (mp.nstr(J0s, 12), mp.nstr((3 + q)/(4*(1 - q)**3), 12)))
astar = min(sp.lambdify(X, a0, 'mpmath')(r + ell*mp.mpf(k)/20000) for k in range(20001))
print('a_*  = %s  (exact 68/257 = %s, claim >= 1/4)' % (mp.nstr(astar, 12), mp.nstr(mp.mpf(68)/257, 12)))
a0n = C0th(a0); w2n = C0th(sp.diff(w0, X, 2)); w1n = C0th(sp.diff(w0, X)); w0n = C0th(w0)
print('||a0||_C0th  upper %s  pair-sampled %s  (sup %s, sup|a0prime| %s; claims < 13, sup <= 8, sup|a0prime| <= 3)' % tuple(mp.nstr(v, 8) for v in a0n))
print('||w0pp||_C0th upper %s  pair-sampled %s  (sup %s, sup|w0ppp| %s; claims < 43.5, <= 12, <= 21)' % tuple(mp.nstr(v, 8) for v in w2n))
print('||w0p||_C0th upper %s  ||w0||_C0th upper %s  (claims < 30, < 34)' % (mp.nstr(w1n[0], 8), mp.nstr(w0n[0], 8)))
ser = sp.series(w0, X, 0, 9).removeO()
jet = sum(abs(sp.N(ser.coeff(X, k))) for k in (1, 3, 5, 7))
Rw = sp.cancel(w0 - ser)
print('R_w0 = %s  (claim -x^9/(8192(1+x^2/16)))' % sp.factor(Rw))
rem = 0
for i in range(3):
    fl = sp.lambdify(X, sp.diff(Rw, X, i), 'mpmath')
    rem += max(abs(fl(r*mp.mpf(k)/2000))*(r*mp.mpf(k)/2000)**(i - 7 - sig) for k in range(1, 2001))
wX = jet + rem + a0n[0]*0 + w0n[0] + w1n[0] + w2n[0]
print('||w0||_X  jet %s + remainder %s + tail %s = %s  (claim < 116)' % (mp.nstr(jet, 8), mp.nstr(rem, 4), mp.nstr(w0n[0] + w1n[0] + w2n[0], 8), mp.nstr(wX, 8)))

def chain(inp, label):
    eta0, D0s, J0s, astar, a0th, w2th, wX = inp
    out = {}
    Z1 = (r**2 + r**4 + r**6 + r**(6 + sig))/A
    D1 = (2*r**2 + 4*r**4 + 6*r**6 + 2*r**(6 + sig))/A
    J1 = (6 + 20*r**2 + 42*r**4 + r**(4 + sig))/A
    dmax = min(1, (mp.mpf(1)/2 - eta0)/(2*Z1), astar/2)
    eta = eta0 + Z1*d; Z = 1 + eta; Ds = D0s + D1*d; Js = J0s + J1*d; N = 1/(1 - eta)
    Es = eta/(2*(1 - eta)); LE = N**2*Z1/2
    e1 = mp.e**((be + 1)*Es); e2 = mp.e**((be + 2)*Es); S = e1*(1 + Z + Ds) + A*e2*Js
    Ts = N**4*S/2; Vs = N*mp.e**((1 - be)*Es)
    LT = (4*N**5*Z1*S + N**4*(e1*(Z1 + D1) + (be + 1)*e1*LE*(1 + Z + Ds) + A*e2*J1 + A*(be + 2)*e2*LE*Js))/2
    LV = mp.e**((1 - be)*Es)*(N**2*Z1 + N*(1 - be)*LE)
    F = r**(-4 - be)*max(1/be, 1/(sig - be)); I = r**(1 - be)/(1 - be)
    Ca = 1 + ell**(1 - th)/2; amin = astar/2; Ath = a0th + Ca*d; Na = 1/amin + Ath/amin**2; W2 = w2th + d
    K = W2*Na; LK = Na + W2*Na**2*Ca
    grp = r**2*Z*mp.e**Es; grm = r**2*(1 - eta)*mp.e**(-Es); Lr = r**2*mp.e**Es*(Z1 + Z*LE)
    H = ell + ell**(1 - th); G = grp*mp.e**(H*K); gmin = grm*mp.e**(-ell*K); LG = mp.e**(H*K)*(Lr + grp*H*LK)
    Ng = 1/gmin + G/gmin**2
    Qth = (K*Ng**2 + W2*Ng**3)/2
    LQ = (LK*Ng**2 + 2*K*Ng**3*LG + Ng**3 + 3*W2*Ng**4*LG)/2
    M = amin**(be - 2)*G**(1 - be)
    LM = (2 - be)*amin**(be - 3)*G**(1 - be) + (1 - be)*amin**(be - 2)*gmin**(-be)*LG
    CB1 = (1 - be)/(3*A)*(F*LT + I*(Qth*LV + LQ*Vs))
    CB2 = (1 - be)*A**(1 - be)/3*ell**(th + be - 1)/(th + be - 1)*(LQ*M + Qth*LM)
    CB = CB1 + CB2
    # Section 5
    Am, Ap = A - hA, A + hA; bm, bp = 2/Ap, 2/Am
    N0 = (A + wX)/Am
    Tp = N**4*(mp.e**((bp + 1)*Es)*(1 + Z + Ds) + Ap*mp.e**((bp + 2)*Es)*Js)/2
    Tfp = N**4*mp.e**((bp + 2)*Es)*Js/2; Vp = N*mp.e**((1 - bm)*Es)
    Qp = (K*Ng**2 + (Ap/A)*W2*Ng**3)/2; qfp = W2/(2*A)*Ng**3
    atm, atp = amin/A, Ath/A
    Mp = max(atm**(b - 2)*G**(1 - b) for b in (bm, bp))
    Lam = max(abs(mp.log(atm/G)), abs(mp.log(atp/gmin)))
    do = min(bm, sig - bp); lr = abs(mp.log(r))
    Fp = r**(-4 - bp)/do; Flp = r**(-4 - bp)*(lr/do + 1/do**2)
    Ip = r**(1 - bp)/(1 - bp); Ilp = r**(1 - bp)*(lr/(1 - bp) + 1/(1 - bp)**2)
    pm, pp = th + bm - 1, th + bp - 1; H0 = max(ell**pm, ell**pp)
    Hp = H0/pm; Hlp = H0*(abs(mp.log(ell))/pm + 1/pm**2)
    Jp = Fp*Tp + Qp*Ip*Vp + Hp*Qp*Mp
    JAp = Fp*Tfp + qfp*Ip*Vp + Hp*qfp*Mp
    Jbp = (Flp + Fp*Es)*Tp + Qp*(Ilp + Ip*Es)*Vp + Qp*Mp*(Hlp + Hp*Lam)
    cp = (1 - bm)/(3*Am); cAp = 2/(3*Am**3) + (1 - bm)/(3*Am**2)
    CA = cAp*Jp + cp*(JAp + 2*Jbp/Am**2)
    Call = N0*CB + CA
    loc = dict(locals())
    print('--- %s' % label)
    ln = lambda v: mp.nstr(mp.log(v), 12)
    claims = [('d=1e-4 <= (15) max', d, dmax, 'le'), ('eta', eta, mp.mpf('.01'), 'lt'), ('N', N, 2, 'lt'), ('E_*', Es, mp.mpf('.01'), 'lt'),
              ('Z1', Z1, 1, 'lt'), ('D1', D1, 1, 'lt'), ('J1', J1, 3, 'lt'), ('D_*', Ds, 2, 'lt'), ('J_*', Js, 2, 'lt'),
              ('a_min', amin, mp.mpf(1)/8, 'ge'), ('A_theta', Ath, 14, 'lt'), ('N_a', Na, 904, 'le'), ('W_2', W2, 44, 'lt'),
              ('K', K, 40000, 'lt'), ('L_K', LK, mp.mpf(10)**8, 'lt'), ('H', H, 6, 'lt'), ('g_r^+', grp, 1, 'lt'),
              ('g_r^-', grm, mp.mpf(1)/32, 'gt'), ('L_r', Lr, 1, 'lt')]
    for nm, v, c, rel in claims:
        ok = {'lt': v < c, 'le': v <= c, 'gt': v > c, 'ge': v >= c}[rel]
        print('  %-20s = %-22s claim %s %s : %s' % (nm, mp.nstr(v, 10), rel, mp.nstr(c, 10), 'OK' if ok else 'FAILS'))
    big = [('G', G, 240000, 1), ('g_min', gmin, -150004, -1), ('L_G', LG, 240021, 1), ('N_g', Ng, 540009, 1),
           ('Q_theta', Qth, 1620050, 1), ('L_Q', LQ, 2400100, 1), ('M', M, 120004, 1), ('L_M', LM, 315030, 1),
           ('C_B', CB, 2600000, 1), ('Q^+', Qp, 1620050, 1), ('q_f^+', qfp, 1620050, 1), ('M^+', Mp, 133340, 1),
           ('C_A', CA, 1800000, 1), ('C_all', Call, 3000000, 1)]
    for nm, v, c, sg in big:
        lv = mp.log(v); ok = (lv < c) if sg > 0 else (lv > c)
        print('  log %-16s = %-22s claim %s %s : %s' % (nm, mp.nstr(lv, 12), '<' if sg > 0 else '>', c, 'OK' if ok else 'FAILS'))
    for nm, v, c in [('Lambda', Lam, 250000), ('N_0', N0, 100)]:
        print('  %-20s = %-22s claim < %s : %s' % (nm, mp.nstr(v, 12), c, 'OK' if v < c else 'FAILS'))
    core = dict(F=F, I=I, L_T=LT, L_V=LV, V_star=Vs)
    print('  core factors < e^20:', ', '.join('%s=%s' % (k, mp.nstr(v, 6)) for k, v in core.items()), ':', 'OK' if max(core.values()) < mp.e**20 else 'FAILS')
    oth = dict(Tp=Tp, Tfp=Tfp, Vp=Vp, Fp=Fp, Flp=Flp, Ip=Ip, Ilp=Ilp, Hp=Hp, Hlp=Hlp)
    print('  other A-factors < 1e5:', ', '.join('%s=%s' % (k, mp.nstr(v, 6)) for k, v in oth.items()), ':', 'OK' if max(oth.values()) < 1e5 else 'FAILS')
    lC = mp.log(Call)
    print('  (43): log(N_0 delta / d) at delta = e^-1e7: %s ; log(C_all delta) = %s (< log(1/20000) = %s): %s' % (
        mp.nstr(mp.log(N0) - 10**7 - mp.log(d), 10), mp.nstr(lC - 10**7, 10), mp.nstr(-mp.log(20000), 6), 'OK' if lC - 10**7 < -mp.log(20000) else 'FAILS'))
    print('  eps_fix = min(d, 1/(20000 C_B)): log = %s ;  eps_all (42): log = %s' % (
        mp.nstr(mp.log(min(d, 1/(20000*CB))), 12), mp.nstr(mp.log(min(mp.mpf(1)/2, d/N0, 1/(20000*Call))), 12)))

chain((2*q + 2*q**2 + 2*q**3, 4*q/(1 - q)**2, (3 + q)/(4*(1 - q)**3), mp.mpf(1)/4, mp.mpf(13), mp.mpf('43.5'), mp.mpf(116)),
      '(I) inputs as stated in Section 6 (a_* = 1/4, ||a0|| = 13, ||w0pp|| = 43.5, ||w0||_X = 116, algebra bounds)')
chain((eta0, D0s, J0s, astar, a0n[0], w2n[0], wX), '(II) inputs computed here (upper bounds)')
