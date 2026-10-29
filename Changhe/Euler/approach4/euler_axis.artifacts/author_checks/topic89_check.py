"""Lead cross-review checks for the critical first-correction compatibility proof (c_l = 1/2, alpha = 1).
(1) spherical components of U from phi = R^-k A(mu), q = R^-(k+1) B(mu) (k = 1, 3);
(2) N = (U . grad) U components N_R, S V, S W for the leading field;
(3) f = div N = R^-4 (-N_R - (S^2 V)'), f_1 = -(3/2) int N_z dmu = 0 for sample A, B;
(4) [checked by hand, not here] the l = 1 moment identity int_{B_R} z div N = 2 pi [R^3 int mu N_R - R^2 int U_R U_z];
(5) G = H is divergence-free: G_R + (S^2 (V - Q'))' = 0 once Q_l solve [l(l+1)-2] Q_l = f_l (l != 1)."""
import sympy as sp
r, z, R, mu, th = sp.symbols('r z R mu theta', positive=True)
out = []
def sph(Ur, Uz):
    # cylindrical (r, z) -> spherical (R, theta) with mu = cos theta, S = sin theta
    S = sp.sqrt(1 - mu**2)
    return sp.simplify(S*Ur + mu*Uz), sp.simplify(mu*Ur - S*Uz)
for k in (1, 3):
    A = sp.Function('A')
    Rr = sp.sqrt(r**2 + z**2)
    phi = Rr**(-k)*A(z/Rr)
    Ur = -r*sp.diff(phi, z); Uz = 2*phi + r*sp.diff(phi, r)
    sub = {r: R*sp.sqrt(1 - mu**2), z: R*mu}
    UR, Uth = sph(Ur.subs(sub), Uz.subs(sub))
    S = sp.sqrt(1 - mu**2)
    a = sp.Symbol('a'); ap = sp.Symbol('ap')
    def clean(e):
        e = e.doit()
        e = e.replace(lambda x: isinstance(x, sp.Subs), lambda x: x.doit())
        return sp.simplify(e)
    UR = clean(UR); Uth = clean(Uth)
    FR_claim = R**(-k)*(2*mu*A(mu) - (1 - mu**2)*sp.diff(A(mu), mu))
    Fth_claim = R**(-k)*((k - 2)*S*A(mu))
    d1 = sp.simplify(UR - FR_claim); d2 = sp.simplify(Uth - Fth_claim)
    out.append(f"k={k}: U_R - R^-k(2 mu A - S^2 A') = {d1};  U_theta - R^-k (k-2) S A = {d2}")
# (2)-(4) concrete leading field
S = sp.sqrt(1 - mu**2)
Aex = mu**2/3 - sp.Rational(1, 5) + mu**4/7   # sample smooth angular data (regular potential)
Bex = 1 + mu**2/2 - mu**3/4
FR = 2*mu*Aex - S**2*sp.diff(Aex, mu); C = -Aex; Fth = S*C; Fph = S*Bex
# Cartesian-free spherical formulas for (U . grad)U with U = R^-1 F(theta)
UR_, Uth_, Uph_ = FR/R, Fth/R, Fph/R
dth = lambda e: -S*sp.diff(e, mu)
NR = UR_*sp.diff(UR_, R) + Uth_/R*dth(UR_) - (Uth_**2 + Uph_**2)/R
Nth = UR_*sp.diff(Uth_, R) + Uth_/R*dth(Uth_) + UR_*Uth_/R - Uph_**2*(mu/S)/R
Nph = UR_*sp.diff(Uph_, R) + Uth_/R*dth(Uph_) + UR_*Uph_/R + Uth_*Uph_*(mu/S)/R
NR_c = -FR**2 - S**2*C*sp.diff(FR, mu) - S**2*(C**2 + Bex**2)
V = mu*C**2 - S**2*C*sp.diff(C, mu) - mu*Bex**2
W = 2*mu*C*Bex - S**2*C*sp.diff(Bex, mu)
out.append(f"N_R check: {sp.simplify(R**3*NR - NR_c)}; N_theta check: {sp.simplify(R**3*Nth - S*V)}; N_phi check: {sp.simplify(R**3*Nph - S*W)}")
f = -NR_c - sp.diff(S**2*V, mu)
Nz = mu*NR_c - S**2*V
f1 = sp.Rational(3, 2)*sp.integrate(sp.expand(f*mu), (mu, -1, 1))
out.append(f"f_1 = {sp.simplify(f1)}; int N_z dmu = {sp.simplify(sp.integrate(sp.expand(Nz), (mu, -1, 1)))}")
# (5) solve the pressure modes and test div G = 0
L = 12
Ql = {}
for l in range(0, L + 1):
    fl = sp.Rational(2*l + 1, 2)*sp.integrate(sp.expand(f*sp.legendre(l, mu)), (mu, -1, 1))
    if l == 1:
        assert sp.simplify(fl) == 0
        Ql[1] = sp.Symbol('Q1'); continue
    Ql[l] = sp.simplify(fl/(l*(l + 1) - 2))
Q = sum(Ql[l]*sp.legendre(l, mu) for l in Ql)
resid_f = sp.simplify(sp.expand(f - sum(((l*(l+1)-2)*Ql[l] if l != 1 else 0)*sp.legendre(l, mu) for l in Ql)))
out.append(f"f minus its Legendre synthesis through degree {L}: {resid_f}")
GR = NR_c - 2*Q
divG = sp.simplify(sp.expand(GR + sp.diff(S**2*(V - sp.diff(Q, mu)), mu)))
out.append(f"G_R + (S^2 (V - Q'))' = {divG}")
intGR = sp.simplify(sp.integrate(sp.expand(GR), (mu, -1, 1)))
out.append(f"int G_R dmu = {intGR}")
open(__file__.replace('.py', '_output.txt'), 'w').write("\n".join(out) + "\n")
print("\n".join(out))
