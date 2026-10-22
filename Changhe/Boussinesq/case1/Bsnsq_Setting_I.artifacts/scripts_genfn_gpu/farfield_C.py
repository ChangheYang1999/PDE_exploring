"""Algebraic far-field coefficient of the generating-function residual (external review, review farfield2/answer.md (b)), outer basis only (m = 3).
G = x eta E^(1/3) H(t, w), t = E^(-1/6), w = (eta/se)^2 E^(-1/3); with rho = (x^2 + (eta/se)^6)^(1/2), q = rho^(-1/3), v = (eta/se)^2 rho^(-2/3):
G = sum_j G_j + O(q^6 corrections), G_j = x eta rho^((2-j)/3) h_j(v), h_j(v) = (1/j!) d_t^j H(0, v) (chain-ruled through the alpha radial map).
Leading chart A* = (G0)_x eta, B* = (G0)_xx, Dx* = d_x - (B*/A*) d_eta, Dy* = (1/A*) d_eta; P1 = -G1, P2 = -2 G2 + (G1)_eta (G1)_x / A*;
omega_0 = -Lap* P1, omega_1 = -Lap* P2, u0 = (-Dy* P1, Dx* P1).  R = rho^(-2/3) C(v) + O(rho^-1),
C(v) = -omega_1 + u0 . grad* omega_0 + a0 B*/A*,  N20(v) = |omega_1| + |u0_1 Dx* omega_0| + |u0_2 Dy* omega_0| + |a0 B*/A*|.
Everything is evaluated with the order-4 bivariate jets of jets.py at points of the curve rho = 1 (homogeneity).
Usage: farfield_C.py state.npz [--nv 25] [--check]   (--check: compare C rho^(-2/3) with the actual R from model.fields along rays at
rho = 1e4..1e7, where float64 is still accurate; the core patch is ignored (it is superexponentially small there))."""
import sys, math, numpy as np, torch
import jets
from jets import Jet, monos, DT
DEV = jets.DEV
from model import Model, fields
d = np.load(sys.argv[1]); J, Kw = int(d['J']), int(d['Kw']); c = d['c'].reshape(J + 1, Kw + 1); a0 = float(d['a0'])
alpha = float(d['alpha']); se = float(d['se']); m_ = int(d['m']); assert m_ == 3
nv = int(sys.argv[sys.argv.index('--nv') + 1]) if '--nv' in sys.argv else 25
p = 4
# t-derivative coefficients of H at t = 0 as Chebyshev sums in the angular variable: H(t, w) = F(tau(t), w), tau = 1 - log(1 + (1-t) kap')/alpha
# (model.basis_jets: t <- 1 - log((1 - t) ea + 1)/alpha), tau(0) = 0, tau'(0) = d = (1 - e^-alpha)/alpha, tau''(0) = kap^2/alpha, kap = 1 - e^-alpha
if alpha > 0:
    kap = 1 - math.exp(-alpha); dd = kap / alpha; ee = kap ** 2 / (2 * alpha)
else:
    dd = 1.0; ee = 0.0
# T_n(2 tau - 1) at tau = 0: T_n(-1) = (-1)^n; d/dtau T_n(2 tau - 1) = 2 T_n'(-1) = 2 (-1)^(n-1) n^2; d^2/dtau^2 = 4 T_n''(-1) = 4 (-1)^n n^2 (n^2 - 1)/3
n = np.arange(J + 1)
T0 = (-1.0) ** n; T1 = 2 * (-1.0) ** (n - 1) * n ** 2; T2 = 4 * (-1.0) ** n * n ** 2 * (n ** 2 - 1) / 3.0
Fv0 = T0 @ c; Ftau = T1 @ c; Ftautau = T2 @ c           # Chebyshev-in-w coefficient vectors (length Kw+1)
h0c = Fv0; h1c = dd * Ftau; h2c = ee * Ftau + 0.5 * dd ** 2 * Ftautau
def cheb_sum(coefs, z):   # sum_k coefs[k] T_k(2 z - 1) for a Jet z
    s = 2 * z - 1
    T = [Jet.const(1.0, p, z.c.shape[1], dev=z.c.device), s]
    for k in range(2, len(coefs)): T.append(2 * s * T[-1] - T[-2])
    out = T[0] * float(coefs[0])
    for k in range(1, len(coefs)): out = out + T[k] * float(coefs[k])
    return out
def Gj_jets(x0, e0):
    X = Jet.var(x0, 0, p); H = Jet.var(e0, 1, p); Hs = H * (1.0 / se)
    rho2 = X * X + Hs.ipow(6); rho = rho2.pow(0.5)
    v = Hs * Hs * rho.pow(-2.0 / 3.0)
    pre = X * H
    G0 = pre * rho.pow(2.0 / 3.0) * cheb_sum(h0c, v)
    G1 = pre * rho.pow(1.0 / 3.0) * cheb_sum(h1c, v)
    G2 = pre * cheb_sum(h2c, v)
    return G0, G1, G2, v
def C_and_N20(x0, e0):
    G0, G1, G2, v = Gj_jets(x0, e0)
    Gx0 = G0.dx(); A = Gx0.de(); B = Gx0.dx(); iA = A.pow(-1.0); BA = B * iA
    Dx = lambda f: f.dx() - BA * f.de()
    Dy = lambda f: iA * f.de()
    P1 = -G1; P2 = -2.0 * G2 + (G1.de() * G1.dx()) * iA
    om0 = -(Dx(Dx(P1)) + Dy(Dy(P1))); om1 = -(Dx(Dx(P2)) + Dy(Dy(P2)))
    u1 = -Dy(P1); u2 = Dx(P1)
    t1 = -om1.val(); t2 = u1.val() * Dx(om0).val(); t3 = u2.val() * Dy(om0).val(); t4 = a0 * (B * iA).val()
    C = t1 + t2 + t3 + t4; N20 = t1.abs() + t2.abs() + t3.abs() + t4.abs()
    return C, N20, v.val(), A.val()
# angular grid on rho = 1: v in (0, 1): x = sqrt(1 - v^3), eta = se v^(1/2)
vs = torch.tensor(0.5 * (1 - np.cos(np.pi * (np.arange(nv) + 0.5) / nv)), dtype=DT, device=DEV)
x0 = torch.sqrt(1 - vs ** 3); e0 = se * torch.sqrt(vs)
C, N20, vchk, Astar = C_and_N20(x0, e0)
print('state %s a0 %.4f: far-field coefficient C(v)/N20(v) on rho = 1 (v = (eta/se)^2 rho^(-2/3)); min A* %.4f' % (sys.argv[1], a0, float(Astar.min())))
for i in range(nv): print('  v %.4f  C %+.4e  N20 %.4e  C/N20 %+.4e' % (float(vchk[i]), float(C[i]), float(N20[i]), float(C[i] / N20[i])))
print('  max |C/N20| = %.4e' % float((C / N20).abs().max()))
if '--check' in sys.argv:
    # actual residual along rays at finite rho vs rho^(-2/3) C(v): fields() of the full model (outer basis; core ignored)
    mod = Model(J, Kw, m=m_, alpha=alpha, se=se); cc = torch.tensor(d['c'], dtype=DT, device=DEV)
    for vv in [0.2, 0.5, 0.8]:
        vt = torch.tensor([vv], dtype=DT, device=DEV); Cv, Nv, _, _ = C_and_N20(torch.sqrt(1 - vt ** 3), se * torch.sqrt(vt))
        row = '  v %.1f: C/N20 %+.4e;  R rho^(2/3) / N20 at rho = ' % (vv, float(Cv[0] / Nv[0]))
        for rho in [1e3, 1e4, 1e5, 1e6, 1e7]:
            x = torch.tensor([rho * math.sqrt(1 - vv ** 3)], dtype=DT, device=DEV); e = torch.tensor([se * math.sqrt(vv) * rho ** (1 / 3)], dtype=DT, device=DEV)
            F = fields(mod.basis_matrix(x, e) @ cc, x, e, a0, mod.beta)
            row += '%.0e: %+.4e  ' % (rho, float(F['R'][0]) * rho ** (2 / 3) / float(Nv[0]))
        print(row)
