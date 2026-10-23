"""Symbolic checks of EQUATIONS.md (lead). Run: nice -n 19 python3 check_equations.py > check_equations.out
Each check prints PASS/FAIL. Generic functions are used where feasible; otherwise concrete random fields."""
import random
import sympy as sp

random.seed(0)
res = []


def report(name, ok):
    res.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name, flush=True)


def is_zero(e):
    return sp.simplify(sp.expand(e)) == 0


y1, y2, y3 = Y = sp.symbols('y1 y2 y3', real=True)
yv = sp.Matrix(Y)
cl, C = sp.symbols('c_l C', positive=True)


def grad_mat(Uv, X=Y):  # G_ij = d_j U_i
    return sp.Matrix(3, 3, lambda i, j: sp.diff(Uv[i], X[j]))


def curl(Uv, X=Y):
    return sp.Matrix([sp.diff(Uv[2], X[1]) - sp.diff(Uv[1], X[2]),
                      sp.diff(Uv[0], X[2]) - sp.diff(Uv[2], X[0]),
                      sp.diff(Uv[1], X[0]) - sp.diff(Uv[0], X[1])])


def div(Uv, X=Y):
    return sum(sp.diff(Uv[i], X[i]) for i in range(3))


def grad(f, X=Y):
    return sp.Matrix([sp.diff(f, x) for x in X])


# ---------------------------------------------------------------- 1.1 / 1.2 similarity reduction
x1, x2, x3, t, T, zs = sp.symbols('x1 x2 x3 t T z_s', real=True)
X = (x1, x2, x3)
tau = T - t
Uf = [sp.Function('U%d' % i) for i in range(3)]
Pf = sp.Function('P')
# concrete smooth test fields (generic-function simplification is unreliable for compositions)
def concrete_fields(Yv):
    a1, a2, a3 = Yv
    Uc_ = [sp.sin(a1 + 2 * a2) * sp.exp(-a3 ** 2 / 3) + a1 * a3, a2 ** 2 - sp.cos(a1 * a3), sp.atan(a1 - a2 + a3)]
    Pc_ = sp.exp(-a1 ** 2) * (a2 + a3 ** 3) + sp.sin(a1 * a2)
    return Uc_, Pc_
for withC in (False, True):
    zc = zs + (C / cl) * tau ** cl if withC else zs
    yy = [x1 / tau ** cl, x2 / tau ** cl, (x3 - zc) / tau ** cl]
    Ux, Px = concrete_fields(yy)
    u = sp.Matrix([tau ** (cl - 1) * Ux[i] for i in range(3)])
    p = tau ** (2 * cl - 2) * Px
    mom = [sp.diff(u[i], t) + sum(u[j] * sp.diff(u[i], X[j]) for j in range(3)) + sp.diff(p, X[i]) for i in range(3)]
    Uy, Py = concrete_fields(Y)
    Uy = sp.Matrix(Uy)
    V = cl * yv + (C if withC else 0) * sp.Matrix([0, 0, 1]) + Uy
    Rm_ = (1 - cl) * Uy + grad_mat(Uy) * V + grad(Py)
    ok = True
    for k in range(4):
        pt = {x1: sp.Rational(random.randint(-9, 9), 7), x2: sp.Rational(random.randint(-9, 9), 7),
              x3: sp.Rational(random.randint(-9, 9), 7), t: sp.Rational(random.randint(0, 9), 10), T: 1,
              zs: sp.Rational(1, 3), cl: sp.Rational(random.randint(41, 49), 100), C: sp.Rational(2, 3)}
        sub = {y1: yy[0].subs(pt), y2: yy[1].subs(pt), y3: yy[2].subs(pt), cl: pt[cl], C: pt[C]}
        for i in range(3):
            lhs = sp.N(mom[i].subs(pt), 30)
            rhs = sp.N((tau ** (cl - 2)).subs(pt) * Rm_[i].subs(sub), 30)
            ok = ok and abs(lhs - rhs) < 1e-20 * (1 + abs(lhs))
    report('1.%d similarity reduction %s (concrete field, 4 points)' % (2 if withC else 1,
           '(E_C), z_c = z_* + (C/c)tau^c' if withC else '(E)'), ok)

# ---------------------------------------------------------------- 1.3 identities with generic (non-solenoidal) U
Us = sp.Matrix([Uf[i](y1, y2, y3) for i in range(3)])
Ps = Pf(y1, y2, y3)
V = cl * yv + C * sp.Matrix([0, 0, 1]) + Us
G = grad_mat(Us)
Rm = (1 - cl) * Us + G * V + grad(Ps)
delta = div(Us)
Om = curl(Us)
trG2 = sum(G[i, j] * G[j, i] for i in range(3) for j in range(3))
lapP = sum(sp.diff(Ps, y, 2) for y in Y)
RP = -lapP - trG2
report('1.3a div R_m = delta + V.grad delta + tr(G^2) + Lap P',
       is_zero(div(Rm) - (delta + (V.T * grad(delta))[0] + trG2 + lapP)))
report('1.3a R_P = -div R_m + delta + V.grad delta',
       is_zero(RP - (-div(Rm) + delta + (V.T * grad(delta))[0])))
Rom = Om + grad_mat(Om) * V - G * Om
report('1.3b curl R_m = R_omega + delta Omega', all(is_zero(e) for e in (curl(Rm) - Rom - delta * Om)))
Yc = yv + (C / cl) * sp.Matrix([0, 0, 1])
H = (V.T * V)[0] / 2 + Ps + cl * (cl - 1) * (Yc.T * Yc)[0] / 2
lhs = (1 - 2 * cl) * V + Om.cross(V) + grad(H)
report('1.3c Bernoulli: (1-2c)V + Omega x V + grad H = R_m', all(is_zero(e) for e in (lhs - Rm)))
report('1.3c V.grad H = (2c-1)|V|^2 + V.R_m', is_zero((V.T * grad(H))[0] - (2 * cl - 1) * (V.T * V)[0] - (V.T * Rm)[0]))
# 1.3d: Omega.R_omega = |Omega|^2 + V.grad |Omega|^2 / 2 - Omega.G Omega
report('1.3d Omega.R_omega = |Om|^2 + (1/2) V.grad|Om|^2 - Om.G Om',
       is_zero((Om.T * Rom)[0] - ((Om.T * Om)[0] + (V.T * grad((Om.T * Om)[0]))[0] / 2 - (Om.T * G * Om)[0])))

# ---------------------------------------------------------------- 1.4 scaling
a = sp.symbols('a', positive=True)
Ua = sp.Matrix([a * Uf[i](y1 / a, y2 / a, y3 / a) for i in range(3)])
Pa = a ** 2 * Pf(y1 / a, y2 / a, y3 / a)
Va = cl * yv + a * C * sp.Matrix([0, 0, 1]) + Ua
Rma = (1 - cl) * Ua + grad_mat(Ua) * Va + grad(Pa)
sub = {y1: y1 / a, y2: y2 / a, y3: y3 / a}
report('1.4 scaling: R_m[U_a,P_a,aC](y) = a R_m[U,P,C](y/a)',
       all(sp.simplify((Rma[i] - a * Rm[i].subs(sub, simultaneous=True)).doit()) == 0 for i in range(3)))

# ---------------------------------------------------------------- 1.2 removal of C by Y = y + (C/c) e3
sh = C / cl
Uh = sp.Matrix([Uf[i](y1, y2, y3 - sh) for i in range(3)])  # U_hat(Y) = U(Y - sh e3) where U solves (E_C)
Ph = Pf(y1, y2, y3 - sh)
V0 = cl * yv + Uh
Rm0 = (1 - cl) * Uh + grad_mat(Uh) * V0 + grad(Ph)
subs_back = {y3: y3 - sh}
report('1.2 (E) residual of shifted field = (E_C) residual at y = Y - (C/c) e3',
       all(sp.simplify((Rm0[i] - Rm[i].subs(subs_back, simultaneous=True)).doit()) == 0 for i in range(3)))

# ---------------------------------------------------------------- 2 cylindrical form (concrete random field)
r, th, z = sp.symbols('r theta z', positive=True)


def randpoly(deg=3):
    mons = [y1 ** i * y2 ** j * y3 ** k for i in range(deg + 1) for j in range(deg + 1) for k in range(deg + 1)
            if i + j + k <= deg]
    return sum(sp.Rational(random.randint(-5, 5), 3) * m for m in mons)


Uc = sp.Matrix([randpoly(), randpoly(), randpoly()])
Pc = randpoly()
cv, Cv = sp.Rational(9, 20), sp.Rational(1, 3)
Vc = cv * yv + Cv * sp.Matrix([0, 0, 1]) + Uc
Rmc = (1 - cv) * Uc + grad_mat(Uc) * Vc + grad(Pc)
cyl = {y1: r * sp.cos(th), y2: r * sp.sin(th), y3: z}
er = sp.Matrix([sp.cos(th), sp.sin(th), 0])
et = sp.Matrix([-sp.sin(th), sp.cos(th), 0])
Ur = (er.T * Uc.subs(cyl))[0]
Ut = (et.T * Uc.subs(cyl))[0]
Uz = Uc[2].subs(cyl)
Pcy = Pc.subs(cyl)
Br = cv * r + Ur
Bz = cv * z + Cv + Uz
D = lambda f: Br * sp.diff(f, r) + (Ut / r) * sp.diff(f, th) + Bz * sp.diff(f, z)
eqr = (1 - cv) * Ur + D(Ur) - Ut ** 2 / r + sp.diff(Pcy, r)
eqt = (1 - cv) * Ut + D(Ut) + Ur * Ut / r + sp.diff(Pcy, th) / r
eqz = (1 - cv) * Uz + D(Uz) + sp.diff(Pcy, z)
eqd = sp.diff(Ur, r) + Ur / r + sp.diff(Ut, th) / r + sp.diff(Uz, z)
Rcart = Rmc.subs(cyl)
ok = True
for k in range(5):
    pt = {r: sp.Rational(random.randint(1, 30), 10), th: sp.Rational(random.randint(0, 62), 10),
          z: sp.Rational(random.randint(-20, 20), 10)}
    vals = [sp.N(e.subs(pt), 30) for e in (eqr - (er.T * Rcart)[0], eqt - (et.T * Rcart)[0], eqz - Rcart[2],
                                            eqd - div(Uc).subs(cyl))]
    ok = ok and all(abs(v) < 1e-20 for v in vals)
report('2 cylindrical residuals = rotated Cartesian residuals (random cubic field, 5 points)', ok)
Om_c = curl(Uc).subs(cyl)
Omr = sp.diff(Uz, th) / r - sp.diff(Ut, z)
Omt = sp.diff(Ur, z) - sp.diff(Uz, r)
Omz = sp.diff(r * Ut, r) / r - sp.diff(Ur, th) / r
ok = True
for k in range(3):
    pt = {r: sp.Rational(random.randint(1, 30), 10), th: sp.Rational(random.randint(0, 62), 10),
          z: sp.Rational(random.randint(-20, 20), 10)}
    vals = [sp.N(e.subs(pt), 30) for e in (Omr - (er.T * Om_c)[0], Omt - (et.T * Om_c)[0], Omz - Om_c[2])]
    ok = ok and all(abs(v) < 1e-20 for v in vals)
report('2 cylindrical vorticity components', ok)

# ---------------------------------------------------------------- 3/5 symmetry projection and curl
Q = sp.diag(-1, -1, 1)
Ff = [sp.Function('F%d' % i) for i in range(3)]
F = sp.Matrix([Ff[i](y1, y2, y3) for i in range(3)])
Qy = Q * yv
FQ = sp.Matrix([Ff[i](*Qy) for i in range(3)])
SF = (F + Q * FQ) / 2
curlF = curl(F)
curlF_Q = curlF.subs({y1: -y1, y2: -y2}, simultaneous=True)
S_curlF = (curlF + Q * curlF_Q) / 2
report('5.2 curl(S F) = S curl F for Q = diag(-1,-1,1)', all(sp.simplify((curl(SF) - S_curlF)[i].doit()) == 0 for i in range(3)))
Rf = sp.diag(-1, 1, 1)  # improper
FR = sp.Matrix([Ff[i](*(Rf * yv)) for i in range(3)])
lhsR = curl(Rf * FR)
rhsR = Rf * curlF.subs({y1: -y1}, simultaneous=True)
report('5.2 improper O = diag(-1,1,1): curl(O F(O^T y)) = -O curl F(O^T y)',
       all(sp.simplify((lhsR + rhsR)[i].doit()) == 0 for i in range(3)))
# equation invariance under Q: R_m[QU(Qy)](y) = Q R_m[U](Qy)
UQ = Q * sp.Matrix([Uf[i](*Qy) for i in range(3)])
PQ = Pf(*Qy)
VQ = cl * yv + C * sp.Matrix([0, 0, 1]) + UQ
RmQ = (1 - cl) * UQ + grad_mat(UQ) * VQ + grad(PQ)
target = Q * Rm.subs({y1: -y1, y2: -y2}, simultaneous=True)
report('3.1 (E_C) is equivariant under Q', all(sp.simplify((RmQ - target)[i].doit()) == 0 for i in range(3)))
# Sigma_z maps (E_C) to (E_{-C})
Sz = sp.diag(1, 1, -1)
Szy = Sz * yv
US = Sz * sp.Matrix([Uf[i](*Szy) for i in range(3)])
PS = Pf(*Szy)
VS = cl * yv - C * sp.Matrix([0, 0, 1]) + US
RmS = (1 - cl) * US + grad_mat(US) * VS + grad(PS)
targetS = Sz * Rm.subs({y3: -y3}, simultaneous=True)
report('3.4 Sigma_z maps (E_C) to (E_{-C})', all(sp.simplify((RmS - targetS)[i].doit()) == 0 for i in range(3)))

# ---------------------------------------------------------------- 4.1 axis expansion divergence
aa, bb, cc, dd, ww = [sp.Function(n)(y3) for n in ('a', 'b', 'c', 'd', 'w')]
Uax = sp.Matrix([aa * y1 + bb * y2, cc * y1 + dd * y2, ww])
report('4.1 div of axis expansion = a + d + w\'', is_zero(div(Uax) - (aa + dd + sp.diff(ww, y3))))

# ---------------------------------------------------------------- 7.1 affine family
pa, pb, pc = sp.symbols('p_a p_b p_c', real=True)
M = sp.Matrix([[pa, pb, 0], [pc, -1 - pa, 0], [0, 0, 1]])
MM = M + M * M
report('7.1/10 tr M = 0 and M + M^2 = diag(k,k,2), k = a + a^2 + bc', M.trace() == 0 and
       all(is_zero(e) for e in (MM - sp.diag(pa + pa ** 2 + pb * pc, pa + pa ** 2 + pb * pc, 2))))
Ua_ = M * yv
Pa_ = -(yv.T * MM * yv)[0] / 2
Rm_aff = (1 - cl) * Ua_ + grad_mat(Ua_) * (cl * yv + Ua_) + grad(Pa_)
report('7.1 affine U = My, P = -y.(M+M^2)y/2 solves (E) for all c', all(is_zero(e) for e in Rm_aff))
tt = sp.symbols('t_s', real=True)
sk = (tt * M + tt ** 2 * M * M) - (tt * M + tt ** 2 * M * M).T
report('7.1 skew(tM + t^2 M^2) = (t - t^2) skew M', all(is_zero(e) for e in (sk - (tt - tt ** 2) * (M - M.T))))
# general Q-equivariant N: N + N^2 symmetric iff N symmetric or tr N = -1
n11, n12, n21, n22 = sp.symbols('n11 n12 n21 n22', real=True)
N = sp.Matrix([[n11, n12], [n21, n22]])
skN = (N + N * N)[0, 1] - (N + N * N)[1, 0]
report('7.1 skew part of N+N^2 = (1 + tr N)(n12 - n21)', is_zero(skN - (1 + n11 + n22) * (n12 - n21)))

# ---------------------------------------------------------------- 10 seed
R2 = (yv.T * yv)[0]
chi = (1 + R2) ** (-1 / (2 * cl))
A0 = -(yv.cross(M * yv)) / 3
report('10 curl(-(1/3) y x My) = My for tr M = 0', all(is_zero(e) for e in (curl(A0) - M * yv)))
Aseed = chi * A0
Useed = curl(Aseed)
formula = chi * M * yv + (chi / (3 * cl * (1 + R2))) * ((yv.T * M * yv)[0] * yv - R2 * M * yv)
report('10 explicit U_seed formula', all(is_zero(e) for e in (Useed - formula)))
report('10 div U_seed = 0', is_zero(div(Useed)))
UQs = Q * Useed.subs({y1: -y1, y2: -y2}, simultaneous=True)
report('10 U_seed(Qy) = Q U_seed(y)', all(is_zero(e) for e in (UQs - Useed)))
UI = -Useed.subs({y1: -y1, y2: -y2, y3: -y3}, simultaneous=True)
report('10 seed is odd: -U_seed(-y) = U_seed(y)', all(is_zero(e) for e in (UI - Useed)))
USz = Sz * Useed.subs({y3: -y3}, simultaneous=True)
report('10 seed has Sigma_z symmetry', all(is_zero(e) for e in (USz - Useed)))
# tail: R^{-d} U_seed(R n) -> (1 - 1/(3c)) M n + (n.Mn) n/(3c)
lam = sp.symbols('lambda', positive=True)
nvec = sp.Matrix([sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)])
num = {pa: sp.Rational(1, 5), pb: -sp.Rational(2, 5), pc: sp.Rational(7, 10), cl: sp.Rational(9, 20)}
dval = 1 - 1 / num[cl]
Uray = formula.subs(num).subs({y1: lam * nvec[0], y2: lam * nvec[1], y3: lam * nvec[2]}, simultaneous=True)
Mnum = M.subs(num)
Ainf = (1 - 1 / (3 * num[cl])) * Mnum * nvec + (nvec.T * Mnum * nvec)[0] * nvec / (3 * num[cl])
ok = True
for i in range(3):
    lim = sp.limit(Uray[i] * lam ** (-dval), lam, sp.oo)
    ok = ok and sp.simplify(lim - Ainf[i]) == 0
report('10 seed tail coefficient A_inf', ok)

# ---------------------------------------------------------------- 8.1/8.2 homogeneity and tail divergence
qd = sp.symbols('q', real=True)
Rr = sp.sqrt(R2)
Ahom = sp.Matrix([sp.sin(y1 / Rr) * (y3 / Rr), sp.exp(y2 / Rr), (y1 * y2 - y3 ** 2) / R2])
Uhom = Rr ** qd * Ahom
lin = (1 - cl) * Uhom + cl * grad_mat(Uhom) * yv
ptq = {y1: sp.Rational(3, 10), y2: -sp.Rational(7, 10), y3: sp.Rational(11, 10), qd: -sp.Rational(11, 9), cl: sp.Rational(9, 20)}
report('8.1 (1-c)U + c y.grad U = (1-c+cq)U for U homogeneous of degree q (test field)',
       all(abs(sp.N((lin - (1 - cl + cl * qd) * Uhom)[i].subs(ptq), 30)) < 1e-25 for i in range(3)))
# tail divergence: take concrete A_r, A_T on the sphere via extension; check div(R^d A) = R^{d-1}[(d+2)A_r + div_S2 A_T]
# test with A = grad_S2 f + g n for f = n1 n2 n3 + n1^2, g = n3^2 - n1 n2: div_S2 grad_S2 f = Lap_S2 f
n = yv / Rr
f_s = n[0] * n[1] * n[2] + n[0] ** 2
g_s = n[2] ** 2 - n[0] * n[1]
gradS = Rr * grad(f_s)  # tangential gradient of a degree-0 function = R grad f
Afield = gradS + g_s * n
divfield = div(Rr ** qd * Afield)
# Laplace-Beltrami of degree-0 f: R^2 Lap f
LapS = sp.simplify(R2 * sum(sp.diff(f_s, y, 2) for y in Y))
pred = Rr ** (qd - 1) * ((qd + 2) * g_s + LapS)
pt = {y1: sp.Rational(3, 10), y2: -sp.Rational(7, 10), y3: sp.Rational(11, 10), qd: -sp.Rational(11, 9)}
report('8.2 div(R^d A) = R^{d-1}[(d+2)A_r + div_S2 A_T] (test field)', abs(sp.N((divfield - pred).subs(pt), 30)) < 1e-25)

# ---------------------------------------------------------------- 9.2 stagnation-point algebra
ga, gb, gc, gd0, ge = sp.symbols('g_a g_b g_c g_d g_e', real=True)
G0 = sp.Matrix([[ga, gb, 0], [gc, gd0, 0], [0, 0, ge]])
Om0 = sp.Matrix([G0[2, 1] - G0[1, 2], G0[0, 2] - G0[2, 0], G0[1, 0] - G0[0, 1]])
report('9.2 Omega(0) = (0,0,c-b) for block G', all(is_zero(e) for e in (Om0 - sp.Matrix([0, 0, gc - gb]))))
eq = (G0 * Om0 - Om0)[2]
report('9.2 G Omega = Omega with Omega_3 != 0 forces e = 1', is_zero(sp.factor(eq) - (gc - gb) * (ge - 1)))


# ---------------------------------------------------------------- 10 seed cylindrical formulas
Useed_c = formula.subs(cyl)
chi_c = chi.subs(cyl)
eta = 1 / (3 * cl * (1 + r ** 2 + z ** 2))
fth = -sp.Rational(1, 2) + (pa + sp.Rational(1, 2)) * sp.cos(2 * th) + ((pb + pc) / 2) * sp.sin(2 * th)
gth = (pc - pb) / 2 + ((pb + pc) / 2) * sp.cos(2 * th) - (pa + sp.Rational(1, 2)) * sp.sin(2 * th)
pred_r = chi_c * r * ((1 - eta * z ** 2) * fth + eta * z ** 2)
pred_t = chi_c * r * (1 - eta * (r ** 2 + z ** 2)) * gth
pred_z = chi_c * z * (1 + eta * r ** 2 * (fth - 1))
ok = True
for k in range(4):
    pt = {r: sp.Rational(random.randint(1, 30), 10), th: sp.Rational(random.randint(0, 62), 10),
          z: sp.Rational(random.randint(-20, 20), 10), pa: sp.Rational(1, 5), pb: -sp.Rational(2, 5),
          pc: sp.Rational(7, 10), cl: sp.Rational(9, 20)}
    vals = [sp.N(e.subs(pt), 30) for e in ((er.T * Useed_c)[0] - pred_r, (et.T * Useed_c)[0] - pred_t,
                                            Useed_c[2] - pred_z)]
    ok = ok and all(abs(v) < 1e-20 for v in vals)
report('10 seed cylindrical components (4 points)', ok)

npass = sum(1 for _, ok in res if ok)
print('SUMMARY %d/%d passed' % (npass, len(res)))
