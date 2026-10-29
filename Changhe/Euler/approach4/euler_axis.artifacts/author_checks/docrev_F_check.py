"""Checks for the v8 revision of FAR_FIELD_ANALYSIS.md (independent mathematical review, findings 17, 18, 19, 29, 31).

Independent route: all far-field computations are done in cylindrical components written in the variables (R, mu),
mu = z/R, with the potential convention U^r = -r phi_z, U^z = 2 phi + r phi_r, U^theta = r q. A velocity is stored as
the triple (a, b, w) = (U^r/r, U^z, U^theta/r). Only the operators d_z, r d_r and (1/r) d_r are needed, so every
angular coefficient is a polynomial in mu (no square roots). The pressure source is tr(DU DV) in cylindrical form,
not the divergence of a spherical convective derivative. Single-threaded sympy; prints PASS/FAIL lines and writes
checks/docrev_F_check_output.json.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_CPU, (58, 58))
import json
import time
import sympy as sp

t0 = time.process_time()
R = sp.Symbol('R', positive=True)
mu = sp.Symbol('mu', real=True)
out = {}
allok = True


def report(name, ok, value=None):
    global allok
    allok = allok and bool(ok)
    out[name] = {"pass": bool(ok), "value": None if value is None else str(value)}
    print(("PASS " if ok else "FAIL ") + name + ("" if value is None else ": " + str(value)) + "  [cpu %.1f]" % (time.process_time() - t0), flush=True)


# ---------- operators in (R, mu) ----------
def Dz(e):
    return mu*sp.diff(e, R) + (1 - mu**2)/R*sp.diff(e, mu)


def rDr(e):
    return R*(1 - mu**2)*sp.diff(e, R) - mu*(1 - mu**2)*sp.diff(e, mu)


def Dr_r(e):  # (1/r) d_r
    return sp.diff(e, R)/R - mu/R**2*sp.diff(e, mu)


def vel_pot(phi, q):
    return (-Dz(phi), 2*phi + rDr(phi), q)


def grad_p(P):
    return (Dr_r(P), Dz(P), sp.Integer(0))


def add(U, V, k=1):
    return tuple(u + k*v for u, v in zip(U, V))


def conv(U, V):  # (U . grad) V in the triple convention
    aU, bU, wU = U
    aV, bV, wV = V
    return (aU*(aV + rDr(aV)) + bU*Dz(aV) - wU*wV,
            aU*rDr(bV) + bU*Dz(bV),
            aU*(wV + rDr(wV)) + bU*Dz(wV) + wU*aV)


def trDD(U, V):  # tr(DU DV), cylindrical, axisymmetric
    aU, bU, wU = U
    aV, bV, wV = V
    return ((aU + rDr(aU))*(aV + rDr(aV)) + aU*aV + Dz(bU)*Dz(bV) + Dz(aU)*rDr(bV) + Dz(aV)*rDr(bU)
            - wU*(wV + rDr(wV)) - wV*(wU + rDr(wU)))


def div(U):
    a, b, _ = U
    return 2*a + rDr(a) + Dz(b)


def coef(e, deg):
    """Angular coefficient of a homogeneous expression of degree -deg; asserts homogeneity."""
    c = sp.expand(sp.simplify(sp.expand(e*R**deg)))
    assert sp.diff(c, R) == 0, ("not homogeneous", deg)
    return c


def mode(poly, l):
    return sp.Rational(2*l + 1, 2)*sp.integrate(sp.expand(poly*sp.legendre(l, mu)), (mu, -1, 1))


def pressure(src, p):
    """Decaying homogeneous solution R^-p Q of -Delta P = R^(-p-2) src (all modes nonresonant)."""
    Q = 0
    for l in range(sp.degree(src, mu) + 1):
        den = l*(l + 1) - p*(p - 1)
        fl = mode(src, l)
        if fl == 0:
            continue
        assert den != 0
        Q += fl/den*sp.legendre(l, mu)
    return sp.expand(Q)


def sph_R(U):  # spherical radial component U_R = sin U^r + mu U^z
    a, b, _ = U
    return R*(1 - mu**2)*a + mu*b


# ---------- 1. leading-term and prompt nonlinear formulas, general A, B, alpha (finding 31, F:31, F:46) ----------
al = sp.Symbol('alpha', positive=True)
Af, Bf = sp.Function('A')(mu), sp.Function('B')(mu)
U0g = vel_pot(R**(-al)*Af, R**(-al - 1)*Bf)
FR = 2*mu*Af - (1 - mu**2)*sp.diff(Af, mu)
Fvt_s = (al - 2)*Af          # F_vartheta / sin
Fth_s = Bf                    # F_theta / sin
ok = sp.simplify(sph_R(U0g)*R**al - FR) == 0
ok = ok and sp.simplify((mu*R*U0g[0] - U0g[1])*R**al - Fvt_s) == 0   # U_vartheta/sin = mu r a/sin - U^z ... /sin
ok = ok and sp.simplify(R*U0g[2]*R**al - Fth_s) == 0                # U_theta/sin = R w
report("F:31 F_R, F_vartheta, F_theta from the potentials (general A, B, alpha)", ok)
report("F:34 div U_0 = 0 (general A, B, alpha)", sp.simplify(div(U0g)) == 0)
Ng = conv(U0g, U0g)
dvt = lambda e: -sp.diff(e, mu)  # d_vartheta e / sin for a function of mu
# prompt formulas divided by the appropriate power of sin (s^2 = 1 - mu^2)
NR_prompt = -al*FR**2 + (1 - mu**2)*Fvt_s*dvt(FR) - (1 - mu**2)*(Fvt_s**2 + Fth_s**2)
Nvt_prompt = (1 - al)*FR*Fvt_s + Fvt_s*(mu*Fvt_s - (1 - mu**2)*sp.diff(Fvt_s, mu)) - mu*Fth_s**2
Nth_prompt = (1 - al)*FR*Fth_s + Fvt_s*(mu*Fth_s - (1 - mu**2)*sp.diff(Fth_s, mu)) + mu*Fvt_s*Fth_s
d1 = sp.simplify(sp.expand(sph_R(Ng)*R**(2*al + 1) - NR_prompt))
d2 = sp.simplify(sp.expand((mu*R*Ng[0] - Ng[1])*R**(2*al + 1) - Nvt_prompt))
d3 = sp.simplify(sp.expand(R*Ng[2]*R**(2*al + 1) - Nth_prompt))
report("F:46 prompt N_R, N_vartheta, N_theta equal the cylindrical computation (exact, general A, B, alpha)",
       d1 == 0 and d2 == 0 and d3 == 0)

# ---------- 2. c = 3/5: resonant quadrupole, log velocity, propagated log (findings 17, 18) ----------
c = sp.Rational(3, 5)
alpha = (1 - c)/c
A = sp.Rational(42, 100) - sp.Rational(23, 100)*mu - sp.Rational(4, 100)*mu**2
B = sp.Rational(34, 100) + sp.Rational(19, 100)*mu + sp.Rational(13, 100)*mu**2
U0 = vel_pot(R**(-alpha)*A, R**(-alpha - 1)*B)
f0 = coef(trDD(U0, U0), 2*alpha + 2)
Q = pressure(f0, 2*alpha)
U1 = add(conv(U0, U0), grad_p(R**(-2*alpha)*Q))       # momentum at degree 2 alpha + 1: -U1 + N + grad P = 0
report("c=3/5: div of the first correction vanishes", sp.simplify(div(U1)) == 0)
src2 = coef(2*trDD(U0, U1), 3*alpha + 3)
f2 = mode(src2, 2)
report("c=3/5: resonant quadrupole f_2 = -125460142/437653125", f2 == sp.Rational(-125460142, 437653125), f2)
Lcoef = f2/5
lnR = sp.log(R)
# 3D: -Delta(R^-3 log R P_2) = 5 R^-5 P_2
lap3 = lambda e, l: sp.diff(e, R, 2) + 2*sp.diff(e, R)/R - l*(l + 1)*e/R**2
report("-Delta(R^-3 log R P_2) = 5 R^-5 P_2", sp.simplify(-lap3(R**-3*lnR, 2) - 5*R**-5) == 0)
Lang = Lcoef*sp.legendre(2, mu)
Y = tuple(sp.Rational(1, 2)*g for g in grad_p(R**-3*Lang))   # log-coefficient velocity
# log part of (1-c)U + c y.grad U + grad P for U = log R * Y, P = R^-3 log R L (no nonlinear log forcing at degree 4)
Ulog = tuple(lnR*g for g in Y)
ydg = (Ulog[0] + R*sp.diff(Ulog[0], R), R*sp.diff(Ulog[1], R), Ulog[2] + R*sp.diff(Ulog[2], R))
bal = add(add(tuple((1 - c)*u for u in Ulog), tuple(c*v for v in ydg)), grad_p(R**-3*lnR*Lang))
okb = all(sp.simplify(sp.expand(comp).coeff(lnR)) == 0 for comp in bal)
report("c=3/5: log velocity R^-4 log R Y with Y = grad(R^-3 L)/2 balances the log pressure", okb)
report("c=3/5: div Y = 0", sp.simplify(div(Y)) == 0)
YR = coef(sph_R(Y), 4)
report("c=3/5: radial log velocity coefficient equals -3L/2 (reviewer convention)", sp.simplify(YR + 3*Lang/2) == 0)
# potential of the log velocity: phi = kappa R^-4 mu (Gegenbauer C_1^{3/2} = 3 mu)
V1 = vel_pot(R**-4*mu, 0)
kv = sp.simplify(coef(Y[1], 4)/coef(V1[1], 4))
okk = kv.is_number and kv != 0 and all(sp.simplify(coef(y - kv*x, d)) == 0
                                       for x, y, d in ((V1[0], Y[0], 5), (V1[1], Y[1], 4)))
report("c=3/5: the log velocity has potential kappa R^-4 log R mu with kappa != 0", okk, kv)
report("c=3/5: relative power of R^-4 against R^-alpha in t = R^(-1/c) is 2 (t^2 log t)", (4 - alpha)*c == 2, (4 - alpha)*c)
Slog = coef(2*trDD(U0, Y), alpha + 6)
s0 = mode(Slog, 0)
report("c=3/5: propagated log source monopole nonzero, equals reviewer value -63482831852/492359765625",
       s0 != 0 and s0 == sp.Rational(-63482831852, 492359765625), s0)
k = alpha + 4
lap0 = lambda e: sp.diff(e, R, 2) + 2*sp.diff(e, R)/R
aL, bL = sp.symbols('aL bL')
resid = sp.expand(sp.simplify((-lap0(aL*R**-k*lnR + bL*R**-k) - s0*R**(-k - 2)*lnR)*R**(k + 2)))
sol = sp.solve([resid.coeff(lnR), resid.subs(lnR, 0)], [aL, bL], dict=True)[0]
report("c=3/5: pressure monopole R^(-14/3) log R has nonzero coefficient (nonresonant degree 14/3)",
       k == sp.Rational(14, 3) and sol[aL] != 0, sol[aL])
report("c=3/5: velocity multiplier 1 - c - c d at d = alpha + 5 is nonzero", 1 - c - c*(alpha + 5) != 0, 1 - c - c*(alpha + 5))

# ---------- 3. c = 7/10: mixed product with the l = 2 irrotational multipole (finding 18) ----------
c = sp.Rational(7, 10)
alpha = (1 - c)/c
report("c=7/10: alpha = 3/7", alpha == sp.Rational(3, 7))
U0 = vel_pot(R**(-alpha)*A, R**(-alpha - 1)*B)
M = grad_p(R**-3*sp.legendre(2, mu))                      # velocity multipole of degree l + 2 = 4
Vm = vel_pot(R**-4*3*mu, 0)                               # potential d_1 R^-4 C_1^{3/2}
ratio = sp.simplify(coef(Vm[1], 4)/coef(M[1], 4))
okm = ratio.is_number and all(sp.simplify(coef(x - ratio*y, d)) == 0 for x, y, d in ((Vm[0], M[0], 5), (Vm[1], M[1], 4)))
report("irrotational l=2 velocity is the velocity of phi = R^-4 C_1^{3/2} (m = l - 1)", okm, ratio)
d = alpha + 4 + 1
X = add(conv(U0, M), conv(M, U0))
Xw = coef(X[2], d + 1)
curl_m = coef(Dz(X[0]) - Dr_r(X[1]), d + 2)              # (azimuthal vorticity)/r of the meridional forcing
report("c=7/10: forced degree d = 38/7", d == sp.Rational(38, 7), d)
report("c=7/10: swirl forcing at degree 38/7 nonzero (q gets the term)", sp.expand(Xw) != 0)
report("c=7/10: meridional forcing at degree 38/7 is not a gradient (phi gets the term)", sp.expand(curl_m) != 0)
mult = 1 - c - c*d
report("c=7/10: multiplier 1 - c - c d nonzero at d = 38/7", mult != 0, mult)
rel = (d - alpha)*c
report("c=7/10: relative power in t = R^(-1/c) is 7/2 (not an integer)", rel == sp.Rational(7, 2), rel)
chain = [alpha + sp.Integer(j)/c for j in range(0, 6)]
report("c=7/10: 38/7 is neither a chain degree alpha + k/c nor an integer", d not in chain and not d.is_integer)

# ---------- 4. c = 3/4, A = 1, B = 0: source dipole moment and pressure coefficient (finding 29) ----------
c = sp.Rational(3, 4)
alpha = (1 - c)/c
U0 = vel_pot(R**(-alpha), 0)
f0 = coef(trDD(U0, U0), 2*alpha + 2)
Q = pressure(f0, 2*alpha)
U1 = add(conv(U0, U0), grad_p(R**(-2*alpha)*Q))
H = add(conv(U0, U1), conv(U1, U0))
FRc, Fzc = coef(sph_R(U0), alpha), coef(U0[1], alpha)
GRc, Gzc = coef(sph_R(U1), 2*alpha + 1), coef(U1[1], 2*alpha + 1)
HRc = coef(sph_R(H), 3*alpha + 2)
report("c=3/4: G_R = 2/3 - 2 mu^2 (record value)", sp.expand(GRc - (sp.Rational(2, 3) - 2*mu**2)) == 0, GRc)
I1 = sp.Rational(3, 2)*sp.integrate(sp.expand(mu*HRc - Fzc*GRc - Gzc*FRc), (mu, -1, 1))
report("c=3/4: normalized source dipole moment constant = 136/135", I1 == sp.Rational(136, 135), I1)
report("c=3/4: pressure dipole coefficient of R^-2 P_1 = I1/3 = 136/405", I1/3 == sp.Rational(136, 405), I1/3)
f1loc = mode(coef(2*trDD(U0, U1), 3*alpha + 3), 1)
report("c=3/4: local degree-one forcing at the resonance vanishes", sp.simplify(f1loc) == 0, f1loc)

# ---------- 5. first-correction radius (finding 19) ----------
c = sp.Rational(3, 5)
Rstar = sp.Integer(1000)**c
report("c=0.6: R^(-1/c) = 1e-3 at R = 1000^(3/5) = 63.0957", abs(float(Rstar) - 63.0957) < 1e-4, float(Rstar))
v180 = float(sp.Integer(180)**(-1/c))
report("c=0.6: 180^(-5/3) = 1.7427e-4 (not 1e-3)", abs(v180 - 1.7427e-4) < 1e-8, v180)
L_, a_, F_, G_ = sp.symbols('L a_eff Fn Gn', positive=True)
alg = sp.Symbol('alpha', positive=True)
cg = 1/(1 + alg)
CG = G_/F_*a_**(-1/cg)
CG_L = (L_**(2*alg + 2)*G_)/(L_**(1 + alg)*F_)*(L_*a_)**(-1/cg)
report("C_G = (|G|/|F|) a_eff^(-1/c) is invariant under U_L(y) = L U(y/L)", sp.simplify(CG_L - CG) == 0)

out["all_pass"] = allok
out["cpu_seconds"] = time.process_time() - t0
print(("PASS" if allok else "FAIL") + " all checks; cpu seconds %.1f" % out["cpu_seconds"])
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "docrev_F_check_output.json"), "w") as fh:
    json.dump(out, fh, indent=1)
