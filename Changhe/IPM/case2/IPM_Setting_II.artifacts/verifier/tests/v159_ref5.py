"""V158 (item 22, ref5 patch on chain 44158225 -> chain_ref5 3b659cd0): checks of the numerical statements in the patch.
R5  5.8(iv)/(v): F(-pi/2) - F(pi/2) = -2(x_1 - x_3 + x_5) from the six-mode coefficients, and the band arithmetic.
O3  5.8(vi): the interpolation pairs, recomputed from the stored m1 / D values of my runs (runs/v83.log, runs/v91.log).
O5  4.2: the derivation of the two Gaussian bounds, step by step:
    F1-F4  Fourier transform of f = x^2 (1 + M y^2) e^{-r^2}, the bound on rho^, the velocity multiplier, sup |DW|;
    T1     the t-representation of f_M against the closed form (Fourier route, as in v157b);
    T2     the t-representation against an independent physical-space quadrature of the canonical law on the axis;
    T3-T8  the elementary bounds, the cancellation, the exact integrals and the final constant 175/639996.
"""
import sys, math, json
import numpy as np
import sympy as sp
import mpmath as mp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

# ---------------- R5 ----------------
xs = [sp.Rational(s) for s in ['0.23901', '-0.71412', '-0.20966', '0.12195', '0.10705', '-0.02705']]
th = sp.symbols('th', real=True)
F = sum(xs[j - 1]*(sp.sin(j*th) if j % 2 else sp.cos(j*th)) for j in range(1, 7))
dF = sp.nsimplify(F.subs(th, -sp.pi/2) - F.subs(th, sp.pi/2))
rep('R5a F(-pi/2) - F(pi/2) = -2(x_1 - x_3 + x_5) = -1.11144 (exact in the printed coefficients)',
    dF == -2*(xs[0] - xs[2] + xs[4]) and dF == sp.Rational('-1.11144'), dF)
rep('R5b -1.11144 + 2(0.84 - 0.47 - 0.17) = -0.71144; 2 x (band sum) is the integral term (n int (1/B_- - 1/B_+) = 2n int w_e/(b_o^2 - w_e^2))',
    sp.Rational('-1.11144') + 2*(sp.Rational('0.84') - sp.Rational('0.47') - sp.Rational('0.17')) == sp.Rational('-0.71144'))
Bp, Bm = sp.symbols('Bp Bm', positive=True)
rep('R5c 1/B_- - 1/B_+ = 2 w_e/(b_o^2 - w_e^2) with b_o = (B_+ + B_-)/2, w_e = (B_+ - B_-)/2',
    sp.simplify(1/Bm - 1/Bp - 2*((Bp - Bm)/2)/(((Bp + Bm)/2)**2 - ((Bp - Bm)/2)**2)) == 0)
rep('R5d the other code\'s outer pair (-0.46, -0.16) with +0.84 gives -0.67144 (so it does not reconstruct -0.716 / -0.720)',
    sp.Rational('-1.11144') + 2*(sp.Rational('0.84') - sp.Rational('0.46') - sp.Rational('0.16')) == sp.Rational('-0.67144'))

# ---------------- O3 ----------------
rec = {}
for fn in ['runs/v83.log', 'runs/v91.log']:
    for L_ in open(fn):
        if L_.startswith('POINT '):
            d = json.loads(L_[6:]); rec[d['state']] = d
need = {'0.0744': 'v83_a2-1.228_c0.0744', '0.0773lo': 'v91_a2-1.228_c0.0773_fromlo', '0.0773hi': 'v91_a2-1.228_c0.0773_fromhi',
        '0.0802': 'v83_a2-1.228_c0.0802'}
have = all(v in rec for v in need.values())
if not have:   # the 0.0802 POINT line is in a per-state log
    for L_ in open('runs/v83_a2-1.228_c0.0802_point.log'):
        if L_.startswith('POINT '):
            d = json.loads(L_[6:]); rec[d['state']] = d
m = {k: rec[v]['m1'] for k, v in need.items()}; D = {k: rec[v]['D_div_fd1'] for k, v in need.items()}
print('   records: m1', m, 'D_div', D)
def lin(c0, m0, c1, m1v): return c0 + (0.5 - m0)*(c1 - c0)/(m1v - m0), 2e-3*(c1 - c0)/(m1v - m0)
ce, se = lin(0.0744, m['0.0744'], 0.0802, m['0.0802'])
rep('O3a endpoint pair (0.0744, 0.0802): crossing %.5f, sensitivity to 2e-3 in m1 %.2e (ref5: 0.07658, 0.00133; FR 5.8(vi) "1.3e-3")' % (ce, se),
    abs(ce - 0.07658) < 5e-6 and abs(se - 1.33e-3) < 5e-6)
adj = []
for k in ['0.0773lo', '0.0773hi']:
    c_, s_ = lin(0.0744, m['0.0744'], 0.0773, m[k]); tt_ = (c_ - 0.0744)/0.0029
    Dc = D['0.0744'] + tt_*(D[k] - D['0.0744']); dD = s_*abs(D[k] - D['0.0744'])/0.0029
    adj.append((c_, s_, Dc, dD))
print('   adjacent pairs (0.0744, 0.0773 from lo / from hi): crossing, d eta13, D_div, d D:', [tuple(round(v, 6) for v in a) for a in adj])
rep('O3b adjacent pair (0.0744, 0.0773): crossings 0.07582 / 0.07590 ("about 0.0759"), sensitivities 8.7e-4 / 9.2e-4 ("about 9e-4"), '
    'D_div -0.239 / -0.241 ("about -0.240"), D sensitivity 6e-4 / 1.4e-3 ("1e-3")',
    abs(adj[0][0] - 0.07582) < 5e-6 and abs(adj[1][0] - 0.07590) < 5e-6 and all(8.5e-4 < a[1] < 9.5e-4 for a in adj)
    and all(abs(a[2] + 0.240) < 1.5e-3 for a in adj) and all(5e-4 < a[3] < 1.5e-3 for a in adj))
rr = [lin(0.0744, 0.49673, 0.0773, v)[0] for v in (0.5034, 0.5031)]
rep('O3c ref5 values from the printed (rounded) m1: 0.07582 / 0.07589', abs(rr[0] - 0.07582) < 5e-6 and abs(rr[1] - 0.07589) < 5e-6, [round(v, 5) for v in rr])

# ---------------- O5 ----------------
X1, X2, t, s, M_, Ls, k_ = sp.symbols('xi1 xi2 t s M L k', real=True)
Lp, kp, sP = sp.symbols('Lp kp sP', positive=True)
g1 = sp.sqrt(sp.pi)*(sp.Rational(1, 2) - X1**2/4)*sp.exp(-X1**2/4)
assert sp.simplify(sp.integrate(sp.exp(-sp.I*X1*s)*s**2*sp.exp(-s**2), (s, -sp.oo, sp.oo)) - g1) == 0
g2 = lambda M: sp.sqrt(sp.pi)*(1 + M*(sp.Rational(1, 2) - X2**2/4))*sp.exp(-X2**2/4)
for M in [0, 3]:
    assert sp.simplify(sp.integrate(sp.exp(-sp.I*X2*s)*(1 + M*s**2)*sp.exp(-s**2), (s, -sp.oo, sp.oo)) - g2(M)) == 0
fhat = sp.pi*sp.exp(-(X1**2 + X2**2)/4)*(sp.Rational(1, 2) - X1**2/4)*(1 + M_/2 - M_*X2**2/4)
rep('F1 f^ = pi e^{-|xi|^2/4} (1/2 - xi_1^2/4)(1 + M/2 - M xi_2^2/4) (1-D transforms by sympy, M = 0, 3)',
    all(sp.simplify(fhat.subs(M_, M) - g1*g2(M)) == 0 for M in [0, 3]))
# scaling: rho(X) = L^2 f(X/L) => rho^(k) = L^4 f^(L k) (substitution X = L Y in the transform)
rep('F2a rho^(k) = L^4 f^(L k) for rho = L^2 f(X/L) (1-D factor check: int e^{-ik x} L^2 (x/L)^2 e^{-x^2/L^2} dx = L^3 g_1(L k))',
    sp.simplify(sp.integrate(sp.exp(-sp.I*X1*s)*Lp**2*(s/Lp)**2*sp.exp(-s**2/Lp**2), (s, -sp.oo, sp.oo)) - Lp**3*g1.subs(X1, Lp*X1)) == 0)
# |f^| <= pi e^{-|xi|^2/4}(1/2 + |xi|^2/4)(1 + M/2 + M|xi|^2/4) for M >= 0 (triangle inequality on each factor); grid check
okb = True
for M in [0, 3]:
    for a1 in np.linspace(-12, 12, 121):
        for a2 in np.linspace(-12, 12, 121):
            q2 = a1*a1 + a2*a2
            lhs = abs(math.pi*math.exp(-q2/4)*(0.5 - a1*a1/4)*(1 + M/2 - M*a2*a2/4))
            okb &= lhs <= math.pi*math.exp(-q2/4)*(0.5 + q2/4)*(1 + M/2 + M*q2/4)*(1 + 1e-14)
rep('F2b |f^(xi)| <= pi e^{-|xi|^2/4} (1/2 + |xi|^2/4)(1 + M/2 + M |xi|^2/4) (grid, M = 0, 3)', okb)
# velocity multiplier: U^ = m(k) rho^, m = (k1 k2, -k1^2)/|k|^2: div U = 0, curl U = -rho_x, |m| = |k1|/|k| <= 1
a_, b_ = sp.symbols('a b', real=True); mvec = sp.Matrix([a_*b_, -a_**2])/(a_**2 + b_**2)
rep('F3 m = (k1 k2, -k1^2)/|k|^2: i k.m = 0, i(k1 m2 - k2 m1) = -i k1, |m| = |k1|/|k| <= 1, |k (x) m| = |k| |m|',
    sp.simplify(a_*mvec[0] + b_*mvec[1]) == 0 and sp.simplify(sp.I*(a_*mvec[1] - b_*mvec[0]) + sp.I*a_) == 0
    and sp.simplify(mvec.dot(mvec) - a_**2/(a_**2 + b_**2)) == 0)
# sup |DW| <= (2 pi)^-2 int |k| |rho^(k)| dk with the bound of F2b, in polar coordinates
rad = sp.symbols('rad', positive=True)
bound_int = (1/(4*sp.pi**2))*2*sp.pi*sp.integrate(rad*rad*sp.pi*Lp**4*sp.exp(-Lp**2*rad**2/4)*(sp.Rational(1, 2) + Lp**2*rad**2/4)
                                                   *(1 + M_/2 + M_*Lp**2*rad**2/4), (rad, 0, sp.oo))
bound_int = sp.simplify(bound_int)
rep('F4 (2 pi)^-2 int |k| pi L^4 e^{-L^2|k|^2/4}(1/2 + L^2|k|^2/4)(1 + M/2 + M L^2|k|^2/4) dk = L sqrt(pi)(2 + 11M/2)',
    sp.simplify(bound_int - Lp*sp.sqrt(sp.pi)*(2 + sp.Rational(11, 2)*M_)) == 0, bound_int)
v0 = bound_int.subs({Lp: sp.Rational(1, 100), M_: 0}); v3 = bound_int.subs({Lp: sp.Rational(1, 100), M_: 3})
rep('F4b L = 1/100: sqrt(pi)/50 (M = 0), 37 sqrt(pi)/200 (M = 3), both < l = 2',
    sp.simplify(v0 - sp.sqrt(sp.pi)/50) == 0 and sp.simplify(v3 - 37*sp.sqrt(sp.pi)/200) == 0 and float(v3) < 2, (float(v0), float(v3)))

# closed form of w_f (Fourier route, as in v157b) for T1
up = sp.symbols('up', positive=True)
T1i = sp.simplify(sp.integrate(X1**2*sp.exp(-t*X1**2)*g1, (X1, -sp.oo, sp.oo), conds='none'))
wcl = {}
for M in [0, 3]:
    T2i = sp.simplify(sp.integrate(sp.exp(-t*X2**2)*g2(M)*(sp.cos(X2*sP) - 1), (X2, -sp.oo, sp.oo), conds='none'))
    Ie = sp.simplify(T1i*T2i)
    wcl[M] = sp.simplify(-sp.integrate(sp.expand(Ie.subs(t, up - sp.Rational(1, 4))), (up, sp.Rational(1, 4), sp.oo), conds='none')/(4*sp.pi**2))
mp.mp.dps = 30
def frep(M, sv):
    sv = mp.mpf(sv)
    g = lambda tv: (3*tv - 1)*((1 + mp.mpf(M)/2 - M*tv/2)*(mp.exp(-tv*sv**2) - 1) + M*tv**2*sv**2*mp.exp(-tv*sv**2))
    return mp.quad(g, [0, mp.mpf(1)/3, 1])/4
errs = []
for M in [0, 3]:
    fcl = sp.lambdify(sP, wcl[M], 'mpmath')
    for sv in ['0.3', '0.7', '1.5', '2.5', '6', '20']:
        with mp.workdps(60):
            ref = fcl(mp.mpf(sv))
        errs.append(abs(frep(M, sv) - ref)/max(abs(ref), mp.mpf('1e-30')))
rep('T1 t-representation f_M(s) = closed form (Fourier route) at s = 0.3, 0.7, 1.5, 2.5, 6, 20 (M = 0, 3; relative)',
    max(errs) < mp.mpf('1e-20'), mp.nstr(max(errs), 3))

# T2: canonical law on the axis by physical-space quadrature (own polar quadrature, smooth near/far partition)
def smooth_step(v):
    v = np.clip(v, 0, 1)
    with np.errstate(divide='ignore', over='ignore'):
        A = np.where(v > 0, np.exp(-1/np.maximum(v, 1e-300)), 0.0); B_ = np.where(v < 1, np.exp(-1/np.maximum(1 - v, 1e-300)), 0.0)
    return A/(A + B_)
def phi(u): return smooth_step((1 - u)/0.5)
gl = np.polynomial.legendre.leggauss(20)
def gl_panels(edges, glw=gl):
    xs_, ws = glw; T = []; Wt = []
    for i in range(len(edges) - 1):
        c = 0.5*(edges[i] + edges[i + 1]); hw = 0.5*(edges[i + 1] - edges[i]); T.append(c + hw*xs_); Wt.append(hw*ws)
    return np.concatenate(T), np.concatenate(Wt)
def W_canon(rho_f, X0, Y0, Rmax=12.0, arad=0.5):
    xi = complex(X0, Y0)
    gn = np.polynomial.legendre.leggauss(100)
    sn = 0.5*arad*(gn[0] + 1); swn = 0.5*arad*gn[1]; na = 256; al = 2*math.pi*np.arange(na)/na
    Z = sn[:, None]*np.exp(1j*al[None, :]); eta = xi - Z
    rN = rho_f(eta.real, eta.imag)
    with np.errstate(divide='ignore', invalid='ignore'):
        near = (phi(sn/arad)[:, None]*(rN/Z**2 - np.where(np.abs(eta) > 0, rN/eta**2, 0))*(sn*swn)[:, None]).sum()*(2*math.pi/na)
    rg, rw = gl_panels(np.concatenate([[0.0], np.geomspace(1e-4, 0.0625, 10), np.linspace(0.0625, 4.0, 64)[1:], np.linspace(4.0, Rmax, 65)[1:]]))
    nth = 2048; thv = 2*math.pi*np.arange(nth)/nth
    E = rg[:, None]*np.exp(1j*thv[None, :])
    rr_ = rho_f(E.real, E.imag); cut = 1 - phi(np.abs(E - xi)/arad)
    with np.errstate(divide='ignore', invalid='ignore'):
        integ = np.where(cut > 0, cut*(1/(xi - E)**2 - 1/E**2)*rr_, 0)
    far = (integ*(rg*rw)[:, None]).sum()*(2*math.pi/nth)
    Om = (near + far)/(2*math.pi) - rho_f(X0, Y0)/2
    return Om.imag, Om.real   # (W_1, W_2)
errs2 = []; vals = []
for M in [0, 3]:
    rho_f = lambda x, y, M=M: x**2*(1 + M*y**2)*np.exp(-(x**2 + y**2))
    for sv in [0.7, 2.5, -0.7]:
        w1, w2 = W_canon(rho_f, 0.0, sv); fr = float(frep(M, abs(sv)))
        errs2.append(max(abs(w2 - fr), abs(w1))); vals.append('%d,%.1f: %.10f/%.10f' % (M, sv, w2, fr))
rep('T2 canonical law by physical-space quadrature: W_1(0, s) = 0, W_2(0, s) = W_2(0, -s) = f_M(|s|) (M = 0, 3; s = 0.7, 2.5, -0.7)',
    max(errs2) < 1e-9, '(%s; max err %.1e)' % ('; '.join(vals), max(errs2)))

# T3-T8 elementary bounds
tp = sp.symbols('tp', positive=True)
J = sp.integrate((1 - 3*tp)*sp.sqrt(tp), (tp, 0, sp.Rational(1, 3))) + sp.integrate((3*tp - 1)*sp.sqrt(tp), (tp, sp.Rational(1, 3), 1))
rep('T3 int_0^1 |3t - 1| t^{1/2} dt = (8/15)(1 + 3^{-3/2}) = %.6f < 2/3' % float(J),
    sp.simplify(J - sp.Rational(8, 15)*(1 + 3**sp.Rational(-3, 2))) == 0 and float(J) < 2/3)
zg = np.linspace(0, 10, 200001)
rep('T4 z e^{-z^2} <= e^{-1/2}/sqrt 2 = %.4f <= 1/2; 1 - e^{-z^2} <= min(z^2, 1) <= z for z >= 0 (grid)' % (math.exp(-0.5)/math.sqrt(2)),
    (zg*np.exp(-zg**2)).max() <= math.exp(-0.5)/math.sqrt(2) + 1e-15 and np.all(1 - np.exp(-zg**2) <= np.minimum(zg**2, 1) + 1e-15)
    and np.all(np.minimum(zg**2, 1) <= zg + 1e-15))
rep('T5 coefficient 1 + M/2 - Mt/2 >= 1 on [0, 1] (M >= 0) and the cancellation (1 + M/2 - Mt/2) t^{1/2} + (M/2) t^{3/2} = (1 + M/2) t^{1/2}',
    sp.simplify((1 + M_/2 - M_*tp/2)*sp.sqrt(tp) + M_/2*tp**sp.Rational(3, 2) - (1 + M_/2)*sp.sqrt(tp)) == 0)
Qb = {M: float((1 + sp.Rational(M, 2))*J/4) for M in [0, 3]}
Qn = {}
for M in [0, 3]:
    Qn[M] = max(abs(float(frep(M, z/50)))/(z/50) for z in range(1, 1001))
rep('T5b |f_M(s)|/s <= (1/4)(1 + M/2) int|3t - 1| t^{1/2} = %.4f / %.4f < 1/2 (M = 0 / 3); grid sup s <= 20: %.4f / %.4f'
    % (Qb[0], Qb[3], Qn[0], Qn[3]), all(Qn[M] <= Qb[M] < 0.5 for M in [0, 3]))
I1 = sp.integrate((1 - sp.exp(-tp*sP**2))/sP**2, (sP, 0, sp.oo)); I2 = sp.integrate(sp.exp(-tp*sP**2), (sP, 0, sp.oo))
rep('T6 int_0^inf (1 - e^{-t s^2})/s^2 ds = sqrt(pi t), int_0^inf e^{-t s^2} ds = sqrt(pi/t)/2',
    sp.simplify(I1 - sp.sqrt(sp.pi*tp)) == 0 and sp.simplify(I2 - sp.sqrt(sp.pi/tp)/2) == 0)
Ab = {M: float(sp.sqrt(sp.pi)*(1 + sp.Rational(M, 2))*J/4) for M in [0, 3]}
An = {}
for M in [0, 3]:
    An[M] = float(mp.quad(lambda sv: abs(frep(M, sv))/sv**2, [mp.mpf('1e-12'), 0.5, 1, 2, 4, 8, 20, 60]) + mp.quad(lambda sv: abs(frep(M, sv))/sv**2, [60, mp.inf]))
rep('T6b int_0^inf |f_M|/s^2 <= (sqrt(pi)/4)(1 + M/2) int|3t - 1| t^{1/2} = %.4f / %.4f < sqrt(pi)(1 + M/2)/6 = %.4f / %.4f; quadrature %.4f / %.4f'
    % (Ab[0], Ab[3], math.sqrt(math.pi)/6, math.sqrt(math.pi)*2.5/6, An[0], An[3]),
    all(An[M] <= Ab[M] < math.sqrt(math.pi)*(1 + M/2)/6 for M in [0, 3]))
# exact value of int f_M/s^2 from the t-representation
sp_int = sp.Rational(1, 4)*sp.integrate((3*tp - 1)*((1 + M_/2 - M_*tp/2)*(-sp.sqrt(sp.pi*tp)) + M_*tp**2*sp.sqrt(sp.pi/tp)/2), (tp, 0, 1))
rep('T7 int_0^inf f_M/s^2 ds from the t-representation = sqrt(pi)(5M - 14)/105', sp.simplify(sp_int - sp.sqrt(sp.pi)*(5*M_ - 14)/105) == 0)
# final constant: q = (L/l) |f_M|/s < (1/100)/(2*2) = 1/400, q^2/(1 - q^2) <= 1/159999
qmax = sp.Rational(1, 100)/2*sp.Rational(1, 2); fac = qmax**2/(1 - qmax**2)
rat = {M: sp.nsimplify(fac*(sp.Rational(1) + sp.Rational(M, 2))*sp.Rational(105, 6)/abs(5*M - 14)) for M in [0, 3]}
rep('T8 (L/l) sup|f_M|/s < 1/400, q^2/(1 - q^2) <= 1/159999, relative bound 5/639996 (M = 0) and 175/639996 (M = 3) < 3/9999',
    fac == sp.Rational(1, 159999) and rat[0] == sp.Rational(5, 639996) and rat[3] == sp.Rational(175, 639996)
    and rat[3] < sp.Rational(3, 9999), (rat[0], rat[3], float(rat[3]), float(sp.Rational(3, 9999))))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
