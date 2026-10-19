"""V158: checks of the full Section 9.2 Step 7 (lead item 18, working draft c55ca0fe), sub-steps 7a-7j.
Symbolic (sympy) checks of every algebraic and geometric claim, and two numerical checks (CPU numpy):
the explicit form of the 7e interpolation inequality on a concrete smooth function, and the vanishing of the omitted
constant of the 7g commutator for a divergence-free field.
"""
import sys, math, itertools
import numpy as np
import sympy as sp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

x, y, s, l, Mm, r, tau, cc, t = sp.symbols('x y s l M r tau c t', real=True)
lp, sp_, mu = sp.symbols('lp sp mu', positive=True)
p = 1/l; lam = l - 1
rho = sp.Function('rho'); W1 = sp.Function('W1'); W2 = sp.Function('W2')

# ---------------- 7a ----------------
E = sp.exp(l*s)
X1, X2 = E*x, E*y
f = sp.exp(-s)*rho(X1, X2)
u1 = sp.exp(-s)*W1(X1, X2); u2 = sp.exp(-s)*W2(X1, X2)
rep('7a(i) d_s f = -f + l Z.grad f', sp.simplify(sp.diff(f, s) + f - l*(x*sp.diff(f, x) + y*sp.diff(f, y))) == 0)
# with the profile defect D := V.grad rho - rho at X = e^{ls} Z: d_s f + e^{-lambda s} u.grad f = e^{-s} D(e^{ls} Z)
a_, b_ = sp.symbols('a b', real=True)
Dfun = ((l*a_ + W1(a_, b_))*sp.diff(rho(a_, b_), a_) + (l*b_ + W2(a_, b_))*sp.diff(rho(a_, b_), b_) - rho(a_, b_))
lhs = sp.diff(f, s) + sp.exp(-lam*s)*(u1*sp.diff(f, x) + u2*sp.diff(f, y))
rep('7a(ii) d_s f + e^{-lambda s} u.grad f = e^{-s} (V.grad rho - rho)(e^{ls} Z), so the profile equation gives d_tau f + u.grad f = 0',
    sp.simplify((lhs - sp.exp(-s)*Dfun.subs({a_: X1, b_: X2}, simultaneous=True)).doit()) == 0)
tt = (1 - sp.exp(-lam*s))/lam
rep('7a(iii) d tau/ds = e^{-lambda s}, tau -> T = 1/lambda', sp.simplify(sp.diff(tt, s) - sp.exp(-lam*s)) == 0 and
    sp.limit(tt.subs(l, sp.Rational(3, 2)), s, sp.oo) == 2)
z1, z2 = sp.symbols('z1 z2', real=True)
K = sp.Matrix([-2*z1*z2, z1**2 - z2**2])/(2*sp.pi*(z1**2 + z2**2)**2)     # (-sin 2th, cos 2th)/(2 pi |z|^2)
rep('7a(iv) K(mu z) = mu^-2 K(z) (so the once-subtracted law and contact term commute with the dilation)',
    sp.simplify(K.subs({z1: mu*z1, z2: mu*z2}, simultaneous=True) - K/mu**2) == sp.zeros(2, 1))
Zr = sp.symbols('Zr', positive=True)
rep('7a(v) scaling of the bounds: e^{-s} (e^{ls} r)^p = r^p, e^{(l-1)s} (e^{ls} r)^{p-1} = r^{p-1} (p = 1/l)',
    sp.simplify(sp.exp(-s)*(sp.exp(l*s)*Zr)**p - Zr**p) == 0 and sp.simplify(sp.exp((l - 1)*s)*(sp.exp(l*s)*Zr)**(p - 1) - Zr**(p - 1)) == 0)
rep('7a(vi) |X| <= R: |X| <= R^{1-p} |X|^p and 1 <= R^{1-p} |X|^{p-1} (bounded sets, p < 1)',
    all(float(Xv) <= float(Rv)**(1 - pv)*float(Xv)**pv + 1e-15 and 1 <= float(Rv)**(1 - pv)*float(Xv)**(pv - 1) + 1e-15
        for Rv in [2, 7.5] for pv in [0.3, 0.8] for Xv in np.linspace(1e-3, Rv, 50)))
# choice of M: c = C0 (8M)^p, c T <= M/8 <=> M^{1-p} >= 8^{1+p} C0/lambda
C0 = sp.symbols('C0', positive=True); Mp = sp.symbols('Mp', positive=True)
lv, C0v = sp.Rational(3, 2), 5
Mreq = (8**(1 + 1/lv)*C0v/(lv - 1))**(1/(1 - 1/lv))
rep('7a(vii) c T <= M/8 is achievable: equality at M = (8^{1+p} C0/lambda)^{1/(1-p)} (l = 3/2, C0 = 5 sample)',
    abs(float(C0v*(8*Mreq)**(1/lv)/(lv - 1) - Mreq/8)) < 1e-9*float(Mreq))

# ---------------- 7b ----------------
tv = sp.symbols('tv', real=True)
bb = sp.Piecewise((sp.exp(-1/tv), tv > 0), (0, True))
def hnum(v):
    b1 = math.exp(-1/v) if v > 0 else 0.0; b2 = math.exp(-1/(1 - v)) if 1 - v > 0 else 0.0
    return b1/(b1 + b2)
okh = all(hnum(v) == 0 for v in [-1, -0.1, 0]) and all(hnum(v) == 1 for v in [1, 1.3, 5])
grid = np.linspace(-0.2, 1.2, 1401); hv = np.array([hnum(v) for v in grid])
okh &= bool(np.all(np.diff(hv) >= -1e-15)) and all(abs(hnum(v) + hnum(1 - v) - 1) < 1e-15 for v in grid)
rep('7b(i) h = 0 on t <= 0, 1 on t >= 1, nondecreasing, h(t) + h(1 - t) = 1 (grid)', okh)
# interval bookkeeping, exact rationals, M = 1 (all statements are homogeneous in M), c tau in [0, 1/8]
def factor_in(off, sl, ct):   # h(4(r - off - ct)/M): zero for r <= off + ct, one for r >= off + ct + M/4
    return (off + ct, off + ct + sp.Rational(1, 4))
def factor_out(off, ct):      # h(4(off - ct - r)/M): zero for r >= off - ct, one for r <= off - ct - M/4
    return (off - ct - sp.Rational(1, 4), off - ct)
okb = True
for ct in [sp.Rational(k, 64) for k in range(0, 9)]:
    i2 = factor_in(sp.Rational(1, 2), 1, ct); o2 = factor_out(6, ct)
    i3 = factor_in(sp.Rational(5, 4), 1, ct); o3 = factor_out(4, ct)
    supp2 = (i2[0], o2[1]); one2 = (i2[1], o2[0]); supp3 = (i3[0], o3[1]); one3 = (i3[1], o3[0])
    okb &= supp2[0] >= sp.Rational(1, 2) and supp2[1] <= 6 and one2[0] <= 1 and one2[1] >= 5
    okb &= supp3[0] >= sp.Rational(5, 4) and supp3[1] <= 4 and one3[0] <= sp.Rational(7, 4) and one3[1] >= sp.Rational(7, 2)
    okb &= supp2[0] > sp.Rational(1, 4) and supp2[1] < 8 and supp3[0] > sp.Rational(1, 4) and supp3[1] < 8   # inside Omega
    # chi_2 = 1 near supp psi_3 = [1, 9/2]
    okb &= one2[0] < 1 and one2[1] > sp.Rational(9, 2)
rep('7b(ii) for 0 <= c tau <= M/8: supp chi_2 in [M/2, 6M], chi_2 = 1 on [M, 5M]; supp chi_3 in [5M/4, 4M], chi_3 = 1 on A_0 = (7M/4, 7M/2); '
    'both in Omega; chi_2 = 1 on a neighbourhood of [M, 9M/2] = supp psi_3', okb)
# transport derivative of the factors
hf = sp.Function('h'); ur = sp.symbols('u_r', real=True)
inner = hf(4*(r - Mp/2 - cc*tau)/Mp); outer = hf(4*(6*Mp - cc*tau - r)/Mp)
tr_in = sp.diff(inner, tau) + ur*sp.diff(inner, r); tr_out = sp.diff(outer, tau) + ur*sp.diff(outer, r)
rep('7b(iii) (d_tau + u.grad) inner = (u_r - c) d_r inner, d_r inner = (4/M) h\' >= 0; (d_tau + u.grad) outer = (u_r + c) d_r outer, d_r outer = -(4/M) h\' <= 0',
    sp.simplify(tr_in - sp.diff(inner, r)*(ur - cc)) == 0 and sp.simplify(tr_out - sp.diff(outer, r)*(ur + cc)) == 0 and
    sp.simplify(sp.diff(inner, r) - 4/Mp*sp.Subs(sp.Derivative(hf(t), t), t, 4*(r - Mp/2 - cc*tau)/Mp)) == 0 and
    sp.simplify(sp.diff(outer, r) + 4/Mp*sp.Subs(sp.Derivative(hf(t), t), t, 4*(6*Mp - cc*tau - r)/Mp)) == 0)
# fixed cutoffs: psi(r) = h(A r/M - B) h(C - D r/M)
def psi_int(A, B, C, D):   # support and one-region
    return ((sp.Rational(B, A), sp.Rational(C, D)), (sp.Rational(B + 1, A), sp.Rational(C - 1, D)))
ps2 = psi_int(16, 6, 14, 2); ps3 = psi_int(8, 8, 18, 4); ps0 = psi_int(16, 4, 16, 2)
rep('7b(iv) psi_2: support [3M/8, 7M], one on [7M/16, 13M/2]; psi_3: [M, 9M/2], one on [9M/8, 17M/4]; psi_0 (7g): [M/4, 8M], one on [5M/16, 15M/2]',
    ps2 == ((sp.Rational(3, 8), 7), (sp.Rational(7, 16), sp.Rational(13, 2))) and ps3 == ((1, sp.Rational(9, 2)), (sp.Rational(9, 8), sp.Rational(17, 4)))
    and ps0 == ((sp.Rational(1, 4), 8), (sp.Rational(5, 16), sp.Rational(15, 2))), (ps2, ps3, ps0))
gap2 = min(sp.Rational(1, 2) - ps2[1][0], ps2[1][1] - 6); gap3 = min(sp.Rational(5, 4) - ps3[1][0], ps3[1][1] - 4)
rep('7b(v) psi_i = 1 on supp chi_i with gap >= M/16 (gaps %s, %s)' % (gap2, gap3), gap2 >= sp.Rational(1, 16) and gap3 >= sp.Rational(1, 16))

# ---------------- 7c ----------------
chi = sp.Function('chi'); Xa, Xb = sp.symbols('Xa Xb', real=True)
Kc = [K[0], K[1]]
okibp = True
for j, zj in enumerate([z1, z2]):
    # kernel of [chi, T_0] d_j: -d_{Y_j}[K(X - Y)(chi(X) - chi(Y))] with z = X - Y, Y = (Xa - z1, Xb - z2)
    Y1, Y2 = sp.symbols('Y1 Y2', real=True)
    for comp in range(2):
        Kxy = Kc[comp].subs({z1: Xa - Y1, z2: Xb - Y2}, simultaneous=True)
        lhs = -sp.diff(Kxy*(chi(Xa, Xb) - chi(Y1, Y2)), [Y1, Y2][j])
        djK = sp.diff(Kc[comp], zj).subs({z1: Xa - Y1, z2: Xb - Y2}, simultaneous=True)
        rhs = (chi(Xa, Xb) - chi(Y1, Y2))*djK + Kxy*sp.diff(chi(Y1, Y2), [Y1, Y2][j])
        okibp &= sp.simplify(lhs - rhs) == 0
rep('7c(i) integration by parts: kernel = (chi(X) - chi(Y)) d_j K(z) + K(z) d_j chi(Y)', okibp)
th = sp.symbols('th', real=True); rr = sp.symbols('rr', positive=True)
okm = True; deltas = {}
for j in range(2):
    for k in range(2):
        for comp in range(2):
            zk = [z1, z2][k]; zj = [z1, z2][j]
            G = sp.diff(zk*Kc[comp], zj)
            Gp = sp.simplify(G.subs({z1: rr*sp.cos(th), z2: rr*sp.sin(th)}, simultaneous=True))
            okm &= sp.simplify(Gp*rr**2 - (Gp*rr**2).subs(rr, 1)) == 0           # homogeneous of degree -2
            okm &= sp.simplify(sp.integrate((Gp*rr**2).subs(rr, 1), (th, 0, 2*sp.pi))) == 0   # zero circular mean
            # delta coefficient: flux of z_k K through the unit circle in direction j
            om = [sp.cos(th), sp.sin(th)]
            deltas[(j, k, comp)] = sp.simplify(sp.integrate((zk*Kc[comp]).subs({z1: sp.cos(th), z2: sp.sin(th)}, simultaneous=True)*om[j], (th, 0, 2*sp.pi)))
rep('7c(ii) d_j(z_k K) homogeneous of degree -2 with zero circular mean (all j, k, both components)', okm)
rep('7c(iii) the delta coefficients int_{|w|=1} w_j w_k K(w) are finite (some nonzero, so the delta term is needed)',
    all(v.is_finite for v in deltas.values()) and any(v != 0 for v in deltas.values()), {kk: v for kk, v in deltas.items() if v != 0})
# leading part: with chi a cubic polynomial, (chi(X) - chi(X - z)) d_j K + K d_j chi(X - z) - sum_k d_k chi(X) d_j(z_k K) = O(|z|^-1)
cvec = sp.symbols('c0:10', real=True)
chi_p = lambda A, B: cvec[0] + cvec[1]*A + cvec[2]*B + cvec[3]*A**2 + cvec[4]*A*B + cvec[5]*B**2 + cvec[6]*A**3 + cvec[7]*A**2*B + cvec[8]*A*B**2 + cvec[9]*B**3
eps = sp.symbols('eps', positive=True)
okl = True
for j in range(2):
    zj = [z1, z2][j]
    for comp in range(2):
        full = (chi_p(Xa, Xb) - chi_p(Xa - z1, Xb - z2))*sp.diff(Kc[comp], zj) + Kc[comp]*sp.diff(chi_p(Xa - z1, Xb - z2), [z1, z2][j])*(-1)
        lead = sum(sp.diff(chi_p(Xa, Xb), [Xa, Xb][k])*sp.diff([z1, z2][k]*Kc[comp], zj) for k in range(2))
        rem = sp.simplify((full - lead).subs({z1: eps*sp.cos(th), z2: eps*sp.sin(th)}, simultaneous=True)*eps)
        lim = sp.simplify(sp.limit(rem, eps, 0))
        okl &= not lim.has(sp.oo, -sp.oo, sp.zoo, sp.nan)
rep('7c(iv) remainder after the leading part is O(|z|^-1) (cubic chi; note d_{Y_j} chi(Y) = -d_{z_j} chi(X - z))', okl)
rep('7c(v) far parts: int_{|z|>=1} |z|^-3 dz < inf; (1 + |X|)^-2 in L^q(R^2) for q > 1',
    sp.integrate(rr**-3*rr, (rr, 1, sp.oo)) == 1 and sp.integrate((1 + rr)**(-2*sp.Rational(11, 10))*rr, (rr, 0, sp.oo)).is_finite)

# ---------------- 7d ----------------
pp = sp.symbols('pp', positive=True)
rep('7d(i) far majorant int_{16M}^inf t^{p-1-j} dt finite for j >= 1, p < 1 (p = 0.9 sample: j = 1, 2, 3)',
    all(sp.integrate(t**(sp.Rational(9, 10) - 1 - j), (t, 16, sp.oo)).is_finite for j in [1, 2, 3]))

# ---------------- 7e ----------------
q = sp.symbols('q', positive=True)
rep('7e(i) Holder bookkeeping: (eta^2 A)^{2q-2} eta^4 = eta^{4q} A^{2q-2}; (eta^2 A)^{2q-1} eta = eta^{4q-1} A^{2q-1}; '
    '(2q-2) q/(q-1) = 2q; (q-1)/q + 1/q = 1; (2q-1)/(2q) + 1/(2q) = 1',
    sp.simplify((2*q - 2)*q/(q - 1) - 2*q) == 0 and sp.simplify(2*(2*q - 2) + 4 - 4*q) == 0 and sp.simplify(2*(2*q - 1) + 1 - (4*q - 1)) == 0)
aa, BB, b3, dd, Cq = sp.symbols('aa BB b3 dd Cq', positive=True)
root = (Cq*BB*dd + sp.sqrt(Cq**2*BB**2*dd**2 + 4*Cq*BB*b3))/2
rep('7e(ii) a^2 <= C B (b_3 + d a) gives a <= positive root <= C B d + (C B b_3)^{1/2}',
    sp.simplify((root**2 - Cq*BB*(b3 + dd*root))) == 0 and
    all(float(root.subs({Cq: cv, BB: bv, dd: dv, b3: b3v})) <= cv*bv*dv + math.sqrt(cv*bv*b3v) + 1e-12
        for cv in [0.5, 3] for bv in [0.1, 2] for dv in [0.01, 5] for b3v in [1e-3, 10]))
# numerical: a^{2q} <= B [(2q - 1) sqrt(2) a^{2q-2} b_3 + 4q d a^{2q-1}] (Frobenius norms) for a concrete v, eta = eta_3 at tau = 0, M = 1
def hvec(v):
    v = np.asarray(v, float); b1 = np.where(v > 0, np.exp(-1/np.where(v > 0, v, 1)), 0.0); b2 = np.where(1 - v > 0, np.exp(-1/np.where(1 - v > 0, 1 - v, 1)), 0.0)
    return b1/(b1 + b2)
n = 1601; g = np.linspace(-4.2, 4.2, n); hstep = g[1] - g[0]; XX, YY = np.meshgrid(g, g, indexing='ij'); RR = np.hypot(XX, YY)
eta = hvec(4*(RR - 1.25)) * hvec(4*(4 - RR))
vv = np.sin(1.3*XX + 0.4*YY**2) + 0.5*np.cos(0.7*XX*YY) + 0.2*XX**3/(1 + RR**2)
def D(F, ax): return np.gradient(F, hstep, axis=ax, edge_order=2)
Dv = [D(vv, 0), D(vv, 1)]
D2 = [[D(Dv[i], j) for j in range(2)] for i in range(2)]
D3 = [[[D(D2[i][j], k) for k in range(2)] for j in range(2)] for i in range(2)]
n2 = np.sqrt(sum(D2[i][j]**2 for i in range(2) for j in range(2))); n3 = np.sqrt(sum(D3[i][j][k]**2 for i in range(2) for j in range(2) for k in range(2)))
Deta = [D(eta, 0), D(eta, 1)]; neta = np.hypot(*Deta)
inside = RR <= 4.05
Bn = np.hypot(*Dv)[inside].max()
okint = True; vals = []
for qv in [2.5, 3.0, 4.0]:
    av = ((eta**2*n2)**(2*qv)).sum()**(1/(2*qv))*hstep**(1/qv)
    b3v = ((eta**4*n3)**qv).sum()**(1/qv)*hstep**(2/qv)
    dv = ((eta*neta)**(2*qv)).sum()**(1/(2*qv))*hstep**(1/qv)
    lhs = av**(2*qv); rhs = Bn*((2*qv - 1)*math.sqrt(2)*av**(2*qv - 2)*b3v + 4*qv*dv*av**(2*qv - 1))
    okint &= lhs <= rhs; vals.append('q %g: a^{2q} %.3e <= %.3e' % (qv, lhs, rhs))
rep('7e(iii) numerical: the integrated-by-parts inequality with explicit constants on a concrete smooth v and eta = eta_3', okint, '; '.join(vals))

# ---------------- 7f ----------------
F = sp.Function('F'); U1 = sp.Function('U1'); U2 = sp.Function('U2')
fx = F(x, y); uu = [U1(x, y), U2(x, y)]
def dbeta(expr, beta):
    for v_, m in zip([x, y], beta):
        if m: expr = sp.diff(expr, v_, m)
    return expr
okL = True
for m in [2, 3]:
    for beta in [(i, m - i) for i in range(m + 1)]:
        lhs = dbeta(uu[0]*sp.diff(fx, x) + uu[1]*sp.diff(fx, y), beta) - (uu[0]*sp.diff(dbeta(fx, beta), x) + uu[1]*sp.diff(dbeta(fx, beta), y))
        rhs = 0
        for nu in itertools.product(range(beta[0] + 1), range(beta[1] + 1)):
            if nu == (0, 0): continue
            cf = sp.binomial(beta[0], nu[0])*sp.binomial(beta[1], nu[1])
            rest = (beta[0] - nu[0], beta[1] - nu[1])
            rhs += cf*(dbeta(uu[0], nu)*sp.diff(dbeta(fx, rest), x) + dbeta(uu[1], nu)*sp.diff(dbeta(fx, rest), y))
        okL &= sp.simplify(lhs - rhs) == 0
rep('7f(i) Leibniz: d^beta(u.grad f) - u.grad d^beta f = sum_{0<nu<=beta} binom(beta,nu) (d^nu u).grad d^{beta-nu} f (|beta| = 2, 3), i.e. G_beta', okL)
chs, Fs, Gs, Ws = sp.symbols('chi Fv Gv w', positive=True)
chf = sp.Function('ch')(tau, x); Ff = sp.Function('Fq')(tau, x); uf = sp.Function('uq')(x)
trn = lambda e: sp.diff(e, tau) + uf*sp.diff(e, x)
qq = sp.Rational(7, 2)
expr = trn(chf**qq*Ff**qq)/qq - (chf**(qq - 1)*trn(chf)*Ff**qq + chf**qq*Ff**(qq - 1)*trn(Ff))
rep('7f(ii) (1/q)(d_tau + u.grad)(chi^q |F|^q) = chi^{q-1}(d_tau + u.grad)chi |F|^q + chi^q |F|^{q-2} F (d_tau + u.grad) F (F > 0 branch, q = 7/2)',
    sp.simplify(expr) == 0)
Ev, Cv = sp.symbols('Ev Cv', positive=True)
rep('7f(iii) E >= 1: (sqrt(C E) + 1)(sqrt(E) + 1) <= 2 (sqrt(C) + 1)^2 E (grid)',
    all((math.sqrt(cv*ev) + 1)*(math.sqrt(ev) + 1) <= 2*(math.sqrt(cv) + 1)**2*ev for cv in [0.01, 1, 50] for ev in [1, 1.5, 10, 1e6]))

# ---------------- 7g ----------------
U_ = (sp.Rational(7, 16), sp.Rational(25, 4)); Up = (sp.Rational(3, 8), sp.Rational(13, 2)); Om = (sp.Rational(1, 4), 8)
rep('7g(i) energy supports [M/2, 6M], [5M/4, 4M] in U = (7M/16, 25M/4); closure U in U_+ = (3M/8, 13M/2); closure U_+ in Omega; '
    'U + B_eps in U_+ for eps < M/64; U_+ at distance >= M/16 from supp(1 - psi_0)',
    U_[0] < sp.Rational(1, 2) and 6 < U_[1] and Up[0] < U_[0] and U_[1] < Up[1] and Om[0] < Up[0] and Up[1] < Om[1]
    and min(U_[0] - Up[0], Up[1] - U_[1]) > sp.Rational(1, 64) and min(Up[0] - ps0[1][0], ps0[1][1] - Up[1]) >= sp.Rational(1, 16))
# C_zeta = int |Y| |grad zeta_eps(Y)| dY independent of eps (radial zeta)
zr = sp.Function('zr')
ep = sp.symbols('ep', positive=True)
integrand_eps = rr*sp.Abs(sp.diff(zr(rr/ep), rr))*ep**-2*rr          # |Y| |grad zeta_eps| times the polar weight r
sub = sp.simplify(integrand_eps.subs(rr, ep*sp.Symbol('rho_', positive=True))*ep)   # dr = eps d rho_
rep('7g(ii) C_zeta scale-invariant: |Y| |grad zeta_eps(Y)| dY = |Y\'| |grad zeta(Y\')| dY\' under Y = eps Y\'', not sub.has(ep), sub)
# numerical: int (u(X) - u(X - Y)) . grad zeta_eps(Y) dY h(X) term: int u(X - Y).grad zeta_eps(Y) dY = (div u * zeta_eps)(X) = 0 for div u = 0
psi_s = lambda A, B: np.sin(A + 0.3*B**2) + A*B/(1 + A**2)
def u_df(A, B, hh=1e-5):   # u = (-psi_y, psi_x) by central differences (div-free to O(h^2))
    return (-(psi_s(A, B + hh) - psi_s(A, B - hh))/(2*hh), (psi_s(A + hh, B) - psi_s(A - hh, B))/(2*hh))
epsv = 0.2; ng = 401; gg = np.linspace(-epsv, epsv, ng); hg = gg[1] - gg[0]; YA, YB = np.meshgrid(gg, gg, indexing='ij'); RY = np.hypot(YA, YB)
with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
    zv = np.where(RY < epsv, np.exp(-1/(1 - (RY/epsv)**2)), 0.0)
zv = zv/(zv.sum()*hg**2)
gz = np.gradient(zv, hg, axis=0), np.gradient(zv, hg, axis=1)
X0 = (0.7, -0.4); ua, ub = u_df(X0[0] - YA, X0[1] - YB)
val = ((ua*gz[0] + ub*gz[1]).sum()*hg**2)
scale = ((np.abs(ua)*np.abs(gz[0]) + np.abs(ub)*np.abs(gz[1])).sum()*hg**2)
rep('7g(iii) numerical: int u(X - Y).grad zeta_eps(Y) dY = 0 for div u = 0 (the omitted constant term)', abs(val) < 1e-5*scale, '(%.2e vs scale %.2e)' % (val, scale))

# ---------------- 7h ----------------
rep('7h(i) (2l - 1)/l = 2 - p; D^2 f = e^{(2l-1)s} D^2 rho; Holder: e^{-(2l-1)s} e^{-alpha l s} = (r/2M)^{p-2-alpha} when e^{ls} = r/(2M)',
    sp.simplify((2*l - 1)/l - (2 - p)) == 0 and
    sp.simplify(sp.diff(sp.exp(-s)*rho(E*x, E*y), x, 2) - sp.exp((2*l - 1)*s)*sp.Subs(sp.Derivative(rho(a_, b_), a_, 2), (a_, b_), (E*x, E*y)).doit()) == 0
    and sp.simplify(sp.expand_log(sp.log(sp.exp(-(2*l - 1)*s - sp.Symbol('al')*l*s).subs(s, sp.log(Zr)/l)), force=True)
                    - sp.expand_log(sp.log(Zr**(p - 2 - sp.Symbol('al'))), force=True)) == 0)
rep('7h(ii) e^{-ls} B(X, r/32) = B(Z_0, M/16), |Z_0| = 2M, lies in A_0 = (7M/4, 7M/2): [31M/16, 33M/16]',
    sp.Rational(7, 4) < 2 - sp.Rational(1, 16) and 2 + sp.Rational(1, 16) < sp.Rational(7, 2) and 2*sp.Rational(1, 32) == sp.Rational(1, 16))
rep('7h(iii) Morrey W^{1,q} -> C^{0,1-2/q} in 2D: exponent 1 - 2/q -> 1 as q -> inf, > alpha for q > 2/(1 - alpha)',
    sp.limit(1 - 2/q, q, sp.oo) == 1 and sp.simplify((1 - 2/(2/(1 - sp.Symbol('al')))) - sp.Symbol('al')) == 0)

# ---------------- 7i ----------------
al = sp.symbols('alpha', positive=True); av_ = sp.symbols('a_', positive=True)
rep('7i(i) xi(Y) = h(2 - |Y - X|/a): one for |Y - X| <= a, zero for |Y - X| >= 2a', hnum(2 - 0.999) == 1 and hnum(2 - 1.0) == 1 and hnum(2 - 2.0) == 0 and hnum(2 - 2.5) == 0)
rep('7i(ii) int_0^a t^{alpha-1} dt = a^alpha/alpha, so r^{p-2-alpha} a^alpha = 64^{-alpha} r^{p-2} for a = r/64',
    sp.simplify(sp.integrate(t**(al - 1), (t, 0, av_)) - av_**al/al) == 0 and sp.simplify(Zr**(p - 2 - al)*(Zr/64)**al - 64**(-al)*Zr**(p - 2)) == 0)
pq = sp.Rational(2, 3)
near_far = sp.simplify(Zr**-4*2*sp.pi*sp.integrate(t**pq*t, (t, 0, 2*Zr))/Zr**(pq - 2))
far = sp.simplify(sp.integrate(t**(pq - 4)*t, (t, 2*Zr, sp.oo))/Zr**(pq - 2))
rep('7i(iii) r^-4 int_{|Y|<=2r} |Y|^p dY and int_{2r}^inf t^{p-3} dt are constant multiples of r^{p-2} (p = 2/3)',
    near_far.is_number and far.is_number, (near_far, far))
rep('7i(iv) Leibniz terms: r^{-1} r^{p-1} = r^{p-2}, r^p r^{-2} = r^{p-2}; transition int_a^{2a} dt/t = log 2',
    sp.simplify(Zr**-1*Zr**(p - 1) - Zr**(p - 2)) == 0 and sp.simplify(sp.expand_log(sp.integrate(1/t, (t, av_, 2*av_)), force=True) - sp.log(2)) == 0)

# ---------------- 7j ----------------
aS, sS = sp.symbols('aS sS', real=True)
G1 = sp.Function('G1'); G2 = sp.Function('G2')
Xf = [G1(aS), G2(aS)]          # X_a(s) at fixed s, as a function of a
w1 = lambda A, B: A**2*B - 3*B**3 + A*B + sp.sin(A - 2*B); w2 = lambda A, B: -A**3 + 2*A*B**2 + B**2 + sp.exp(A*B/3)
A_, B_ = sp.symbols('A_ B_', real=True)
Wm = sp.Matrix([w1(A_, B_), w2(A_, B_)]); DWm = Wm.jacobian([A_, B_])
at = {A_: Xf[0], B_: Xf[1]}
Wv = Wm.subs(at, simultaneous=True)
Qv = sp.exp(-l*sS)*sp.diff(sp.Matrix(Xf), aS, 2)                 # Q_s = d_a^2 F_s, F_s = e^{-ls} X_a(s)
dF = sp.exp(-l*sS)*sp.diff(sp.Matrix(Xf), aS)
# d_s Q_s = -l Q_s + e^{-ls} d_a^2 (l X + W(X)) = e^{-ls} d_a^2 W(X_a(s))   (flow equation differentiated twice in a, C^2 flow)
dQ = -l*Qv + sp.exp(-l*sS)*sp.diff(l*sp.Matrix(Xf) + Wv, aS, 2)
D2W = sp.Matrix([sum(sp.diff(Wm[i], [A_, B_][j], [A_, B_][k]).subs(at, simultaneous=True)*dF[j]*dF[k] for j in range(2) for k in range(2)) for i in range(2)])
rhs = DWm.subs(at, simultaneous=True)*Qv + sp.exp(l*sS)*D2W
rep('7j(i) d_s Q_s = DW(X_a) Q_s + e^{ls} D^2 W(X_a)[d_a F_s, d_a F_s] for F_s = e^{-ls} X_a(s), d_s X = l X + W(X) (concrete nonpolynomial W)',
    sp.simplify(sp.expand(dQ - rhs)) == sp.zeros(2, 1))
Rr = sp.symbols('Rr', positive=True)
rep('7j(ii) Q_0 = d_a^2 (R e_a) = -R e_a; forcing e^{ls} (e^{ls})^{p-2} = e^{-lambda s}; coefficient (e^{ls})^{p-1} = e^{-lambda s}',
    sp.simplify(sp.diff(Rr*sp.Matrix([sp.cos(aS), sp.sin(aS)]), aS, 2) + Rr*sp.Matrix([sp.cos(aS), sp.sin(aS)])) == sp.zeros(2, 1)
    and sp.simplify(sp.exp(l*s)*sp.exp(l*s*(p - 2)) - sp.exp(-lam*s)) == 0 and sp.simplify(sp.exp(l*s*(p - 1)) - sp.exp(-lam*s)) == 0)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
