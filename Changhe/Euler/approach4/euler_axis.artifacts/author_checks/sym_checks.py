"""Lead symbolic checks of the formulation (SPEC sections 1, 3, 4). Single process, sympy only."""
import sympy as sp, random, json, time
t0 = time.time()
out = {}
r, z, c = sp.symbols('r z c', positive=True)
phi = sp.Function('phi')(r, z); q = sp.Function('q')(r, z); P = sp.Function('P')(r, z)
Ur = -r*sp.diff(phi, z); Uz = 2*phi + r*sp.diff(phi, r); Ut = r*q
Wr = c*r + Ur; Wz = c*z + Uz
D = lambda f: Wr*sp.diff(f, r) + Wz*sp.diff(f, z)
Mr = (1-c)*Ur + D(Ur) - Ut**2/r + sp.diff(P, r)
Mt = (1-c)*Ut + D(Ut) + Ur*Ut/r
Mz = (1-c)*Uz + D(Uz) + sp.diff(P, z)
eta = -(sp.diff(phi, r, 2) + 3/r*sp.diff(phi, r) + sp.diff(phi, z, 2))
Rq = q + D(q) + 2*(Ur/r)*q
Reta = (1+c)*eta + D(eta) - sp.diff(q**2, z)
Gam = r**2*q
RGam = (1-2*c)*Gam + D(Gam)
divU = sp.diff(Ur, r) + Ur/r + sp.diff(Uz, z)
Omt = sp.diff(Ur, z) - sp.diff(Uz, r)
out['divU_identically_zero'] = sp.simplify(divU) == 0
out['Omega_theta_equals_r_eta'] = sp.simplify(Omt - r*eta) == 0
out['M_theta_equals_r_Rq'] = sp.simplify(sp.expand(Mt - r*Rq)) == 0
out['curlM_theta_equals_r_Reta'] = sp.simplify(sp.expand(sp.diff(Mr, z) - sp.diff(Mz, r) - r*Reta)) == 0
out['RGam_equals_r2_Rq'] = sp.simplify(sp.expand(RGam - r**2*Rq)) == 0
# div M = d_iU_j d_jU_i (cylindrical, axisymmetric): sum = (d_r Ur)^2 + 2 d_z Ur d_r Uz + (d_z Uz)^2 + (Ur/r)^2 - 2 d_r(Ut)*Ut/r ... compute generally
divM = sp.diff(Mr, r) + Mr/r + sp.diff(Mz, z)
lapP = sp.diff(P, r, 2) + sp.diff(P, r)/r + sp.diff(P, z, 2)
# grad U in cylindrical (axisymmetric), matrix G[i][j] = (grad U)_{ij} = d_j U_i with basis (r,theta,z)
G = sp.Matrix([[sp.diff(Ur, r), -Ut/r, sp.diff(Ur, z)],
               [sp.diff(Ut, r), Ur/r, sp.diff(Ut, z)],
               [sp.diff(Uz, r), 0, sp.diff(Uz, z)]])
trG2 = sum(G[i, j]*G[j, i] for i in range(3) for j in range(3))
out['divM_equals_lapP_plus_trDU2'] = sp.simplify(sp.expand(divM - lapP - trG2)) == 0
print('reduced system checks', out, round(time.time()-t0, 1), 's', flush=True)

# ---------- far field leading term ----------
R, mu, al = sp.symbols('R mu alpha', positive=True)
Af = sp.Function('A'); Bf = sp.Function('B')
rr, zz = sp.symbols('rr zz', positive=True)
Rexp = sp.sqrt(rr**2 + zz**2)
phi0 = Rexp**(-al)*Af(zz/Rexp); q0 = Rexp**(-al-1)*Bf(zz/Rexp)
Ur0 = -rr*sp.diff(phi0, zz); Uz0 = 2*phi0 + rr*sp.diff(phi0, rr); Ut0 = rr*q0
eta0 = -(sp.diff(phi0, rr, 2) + 3/rr*sp.diff(phi0, rr) + sp.diff(phi0, zz, 2))
th = sp.symbols('vartheta', positive=True)
subs_sph = {rr: R*sp.sin(th), zz: R*sp.cos(th)}
def sph(e):
    e = e.subs(subs_sph)
    e = e.subs(sp.cos(th), mu)  # careful: only after simplification
    return e
FR = sp.simplify(((Ur0*rr + Uz0*zz)/Rexp).subs(subs_sph)*R**al)
Fth = sp.simplify(((Ur0*zz - Uz0*rr)/Rexp).subs(subs_sph)*R**al)
Fph = sp.simplify(Ut0.subs(subs_sph)*R**al)
A = Af(sp.cos(th)); B = Bf(sp.cos(th))
Ap = sp.Subs(sp.Derivative(Af(mu), mu), mu, sp.cos(th)).doit()
FR_claim = 2*sp.cos(th)*A - sp.sin(th)**2*sp.diff(Af(mu), mu).subs(mu, sp.cos(th))
Fth_claim = (al-2)*sp.sin(th)*A
Fph_claim = sp.sin(th)*B
def num_eq(e1, e2, reps=4):
    """numeric comparison for expressions in th, alpha with A,B replaced by concrete polynomials"""
    Ac = lambda m: 1 + m/3 + m**2/2 - m**3/5 + m**4/7
    Bc = lambda m: sp.Rational(1, 2) - m/4 + m**3
    mm = sp.symbols('mm')
    ok = True
    for _ in range(reps):
        vals = {th: sp.Rational(random.randint(1, 300), 101), al: sp.Rational(random.randint(34, 99), 100), R: sp.Rational(random.randint(50, 500), 37)}
        f1 = e1.replace(Af, sp.Lambda(mm, Ac(mm))).replace(Bf, sp.Lambda(mm, Bc(mm))).doit()
        f2 = e2.replace(Af, sp.Lambda(mm, Ac(mm))).replace(Bf, sp.Lambda(mm, Bc(mm))).doit()
        d = sp.N((f1 - f2).subs(vals), 30)
        s = sp.N(abs(f1.subs(vals)) + 1, 30)
        ok = ok and abs(d) < 1e-20*s
    return bool(ok)
out2 = {}
out2['F_R'] = num_eq(FR, FR_claim)
out2['F_vartheta'] = num_eq(Fth, Fth_claim)
out2['F_theta'] = num_eq(Fph, Fph_claim)
E_claim = -(al*(al-3)*Af(mu) + (1-mu**2)*sp.diff(Af(mu), mu, 2) - 4*mu*sp.diff(Af(mu), mu))
E_num = sp.simplify(eta0.subs(subs_sph)*R**(al+2))
out2['E'] = num_eq(E_num, E_claim.subs(mu, sp.cos(th)))
print('far-field leading', out2, round(time.time()-t0, 1), 's', flush=True)
out.update(out2)

# ---------- N formulas against Cartesian, concrete A, B ----------
x, y, Z = sp.symbols('x y Z', real=True)
alv = sp.Rational(3, 7)
Ac = lambda m: 1 + m/3 + m**2/2 - m**3/5 + m**4/7
Bc = lambda m: sp.Rational(1, 2) - m/4 + m**3
Rc = sp.sqrt(x**2 + y**2 + Z**2); rc = sp.sqrt(x**2 + y**2); muc = Z/Rc
phic = Rc**(-alv)*Ac(muc); qc = Rc**(-alv-1)*Bc(muc)
# Cartesian velocity: U^r = -r d_z phi, U^z = 2 phi + r d_r phi; r d_r = x d_x + y d_y for axisymmetric phi
Urc_over_r = -sp.diff(phic, Z)
Uzc = 2*phic + x*sp.diff(phic, x) + y*sp.diff(phic, y)
Ux = x*Urc_over_r - y*qc; Uy = y*Urc_over_r + x*qc
Ucart = sp.Matrix([Ux, Uy, Uzc])
Xv = sp.Matrix([x, y, Z])
adv = (Ucart.jacobian(Xv))*Ucart
pt = {x: sp.Rational(7, 10), y: sp.Rational(0), Z: sp.Rational(-4, 10)}
pt2 = {x: sp.Rational(3, 10), y: sp.Rational(0), Z: sp.Rational(9, 10)}
th_s = sp.symbols('ths')
def Fcomp(t):
    m = sp.cos(t); s = sp.sin(t)
    FRv = 2*m*Ac(m) - s**2*sp.diff(Ac(mu), mu).subs(mu, m)
    Ftv = (alv-2)*s*Ac(m)
    Fpv = s*Bc(m)
    return FRv, Ftv, Fpv
FRs, Fts, Fps = Fcomp(th_s)
NR = -alv*FRs**2 + Fts*sp.diff(FRs, th_s) - Fts**2 - Fps**2
Nt = (1-alv)*FRs*Fts + Fts*sp.diff(Fts, th_s) - sp.cot(th_s)*Fps**2
Np = (1-alv)*FRs*Fps + Fts*sp.diff(Fps, th_s) + sp.cot(th_s)*Fts*Fps
okN = True
for p in (pt, pt2):
    Rv = sp.sqrt(p[x]**2 + p[Z]**2); tv = sp.acos(p[Z]/Rv)
    a = [sp.N(adv[i].subs(p), 30) for i in range(3)]
    # spherical components at y=0: e_R = (sin, 0, cos), e_th = (cos, 0, -sin), e_phi = (0,1,0)
    s_, m_ = sp.sin(tv), sp.cos(tv)
    aR = a[0]*s_ + a[2]*m_; aT = a[0]*m_ - a[2]*s_; aP = a[1]
    sc = Rv**(2*alv+1)
    for got, claim in ((aR, NR), (aT, Nt), (aP, Np)):
        d = sp.N(got*sc - claim.subs(th_s, tv), 30)
        okN = okN and abs(d) < 1e-20
out['N_formulas_vs_cartesian'] = bool(okN)
print('N vs Cartesian', okN, round(time.time()-t0, 1), 's', flush=True)

# ---------- G and Q balance: substitute expansion into momentum, collect degree -(2 alpha+1) ----------
# Linear operator on R^{-d} G: (1-c) - c d ; with d = 2 alpha + 1 and c = 1/(1+alpha)
cc = 1/(1+al)
coef = sp.simplify((1-cc) - cc*(2*al+1))
out['linear_coefficient_on_G'] = str(coef)
print('coefficient of G in balance:', coef, flush=True)

# ---------- l=0 and l=1 projections of the pressure source, generic quartic A, B ----------
a = sp.symbols('a0:5'); b = sp.symbols('b0:5')
Ap_ = sum(a[i]*mu**i for i in range(5)); Bp_ = sum(b[i]*mu**i for i in range(5))
sinv = sp.sqrt(1-mu**2)
FRm = 2*mu*Ap_ - (1-mu**2)*sp.diff(Ap_, mu)
# d/dvartheta = -sin d/dmu
dth = lambda f: -sinv*sp.diff(f, mu)
Ftm = (al-2)*sinv*Ap_; Fpm = sinv*Bp_
NRm = sp.expand(-al*FRm**2 + Ftm*dth(FRm) - Ftm**2 - Fpm**2)
Ntm = sp.expand((1-al)*FRm*Ftm + Ftm*dth(Ftm) - (mu/sinv)*Fpm**2)
src = sp.expand((1-2*al)*NRm - sp.diff(sp.expand(sinv*Ntm), mu))
mono = sp.factor(sp.integrate(src, (mu, -1, 1)))
dip = sp.factor(sp.integrate(sp.expand(mu*src), (mu, -1, 1)))
out['monopole_has_factor_(1-2alpha)'] = bool(sp.simplify(mono.subs(al, sp.Rational(1, 2))) == 0)
out['dipole_vanishes_at_alpha_1'] = bool(sp.simplify(dip.subs(al, 1)) == 0)
print('monopole factored:', str(mono)[:300], flush=True)
print('dipole at alpha=1:', sp.simplify(dip.subs(al, 1)), flush=True)
dipq = sp.factor(sp.cancel(dip/(al-1))) if sp.simplify(dip.subs(al, 1)) == 0 else None
out['dipole_over_(alpha-1)_polynomial'] = dipq is not None and sp.denom(sp.together(dipq)) .free_symbols <= set()
# Q_0 = <N_R>/(2 alpha): monopole of Q from operator -[2a(2a-1)]Q0 = mean(src)
Q0 = sp.simplify(sp.integrate(src, (mu, -1, 1))/2 / (-(2*al*(2*al-1))))
out['Q0_equals_meanNR_over_2alpha'] = bool(sp.simplify(Q0 - sp.integrate(NRm, (mu, -1, 1))/2/(2*al)) == 0)
# check div G = 0 consequence of Q equation: (1-2a)G_R + (1/sin) d(sin G_th) with G = N + (-2aQ, dQ) is
# (1-2a)N_R + Div N + [2a(2a-1) + Lap_S] Q : identical rearrangement, verify symbolically for generic Q(mu)
Qf = sp.Function('Q')(mu)
GR = NRm - 2*al*Qf; Gt = Ntm + dth(Qf)
divG = (1-2*al)*GR - sp.diff(sinv*Gt, mu)
lapS = sp.diff((1-mu**2)*sp.diff(Qf, mu), mu)
out['divG_identity'] = bool(sp.simplify(sp.expand(divG - (src + (2*al*(2*al-1))*Qf + lapS))) == 0)
print(out, round(time.time()-t0, 1), 's', flush=True)
json.dump({k: (v if isinstance(v, (bool, str)) else str(v)) for k, v in out.items()}, open('author_checks/sym_checks_result.json', 'w'), indent=1)
