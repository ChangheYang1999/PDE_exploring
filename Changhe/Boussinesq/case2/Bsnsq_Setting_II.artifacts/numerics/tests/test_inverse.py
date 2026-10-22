"""Manufactured-solution tests of the modal full-plane Green inverse.
T1: Psi = xy/(1+r^2)^2  -> Omega = 24 xy/(1+r^2)^4 (k=2 only), G = 1.5(1-xi)^4, sigma_G = 3, L = 1.
T2: Psi = xy(x^2-y^2)/(1+r^2)^4 -> Omega = 20 r^4 sin4th/(1+r^2)^6 (k=4 only), G = 2.5 rho^2 (1-xi)^5 cos2th, sigma_G=5.
T3: non-polynomial q (G = (1-xi)^3 exp(xi)): compare with scipy.quad of the Green formula, N = 16..96.
T4: same with mismatched sigma (true decay (1-xi)^{3.3}, basis sigma_G=3): algebraic convergence rate.
T5: between-node evaluation of h.
"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from a2core import A2Model, cheb_gauss_nodes, cheb_T, DT
from scipy.integrate import quad
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def run(N, M, L, sG, sa, ca_fn, cG_fn, xi_eval=None):
    m = A2Model(N, M, L, sa, sG, device=dev, xi_eval=xi_eval)
    ca = torch.zeros((M, N), dtype=DT, device=dev); cG = torch.zeros((M, N), dtype=DT, device=dev)
    ca_fn(ca); cG_fn(cG)
    f = m.fields(ca, cG, 1.0)
    return m, f

# ---- T1
N, M = 32, 8
def cG1(c): c[0, 0] = 1.5; c[0, 1] = -1.5
m, f = run(N, M, 1.0, 3.0, 2.0, lambda c: None, cG1)
r = m.r
h2_ex = r**2 / (2 * (1 + r**2)**2)
h2d_ex = np.gradient  # placeholder
h2d_ex = (2*r*(1+r**2) - 4*r**3) / (2*(1+r**2)**3)   # d/dr of r^2/(2(1+r^2)^2) = r/(1+r^2)^2 - 2 r^3/(1+r^2)^3
h2 = f['h'][0].cpu().numpy(); h2d = f['hd'][0].cpu().numpy()
print("T1 k=2: max|h-h_ex| = %.3e (max|h| %.3e), max|h'-h'_ex| = %.3e, |c-1| = %.3e, others max|h_k| = %.3e" % (
    np.abs(h2-h2_ex).max(), np.abs(h2_ex).max(), np.abs(h2d-h2d_ex).max(), abs(float(f['c'])-1.0),
    f['h'][1:].abs().max().item()))
# Psi on grid vs exact xy/(1+r^2)^2
Psi_ex = (f['x']*f['y']).cpu().numpy() / (1 + r[:, None]**2)**2
print("T1 Psi grid max err = %.3e" % np.abs(f['Psi'].cpu().numpy() - Psi_ex).max())
# velocity: U1 = -Psi_y = -(x/(1+r^2)^2 - 4 x y^2/(1+r^2)^3), U2 = Psi_x = y/(1+r^2)^2 - 4 x^2 y/(1+r^2)^3
x = f['x'].cpu().numpy(); y = f['y'].cpu().numpy(); rr = r[:, None]
U1_ex = -(x/(1+rr**2)**2 - 4*x*y**2/(1+rr**2)**3); U2_ex = y/(1+rr**2)**2 - 4*x**2*y/(1+rr**2)**3
print("T1 U1 err %.3e, U2 err %.3e" % (np.abs(f['U1'].cpu().numpy()-U1_ex).max(), np.abs(f['U2'].cpu().numpy()-U2_ex).max()))

# ---- T2
def cG2(c): c[1, 0] = 2.5
m, f = run(N, M, 1.0, 5.0, 2.0, lambda c: None, cG2)
r = m.r
h4_ex = r**4 / (4 * (1 + r**2)**4)
h4d_ex = r**3/(1+r**2)**4 - 2*r**5/(1+r**2)**5
h4 = f['h'][1].cpu().numpy(); h4d = f['hd'][1].cpu().numpy()
print("T2 k=4: max|h-h_ex| = %.3e (max|h| %.3e), max|h'-h'_ex| = %.3e, |c| = %.3e, other modes max = %.3e" % (
    np.abs(h4-h4_ex).max(), np.abs(h4_ex).max(), np.abs(h4d-h4d_ex).max(), abs(float(f['c'])),
    max(f['h'][0].abs().max().item(), f['h'][2:].abs().max().item())))

# ---- T3 / T4: reference by quadrature in r of the Green formula for k=2 with b_2(r) = (r^2/2) gamma_0(r)
def ref_h2(r_e, gamma0):
    b = lambda s: 0.5 * s**2 * gamma0(s)
    I_in = quad(lambda s: s**3 * b(s), 0, r_e, limit=200, epsabs=1e-14, epsrel=1e-13)[0]
    I_out = quad(lambda s: s**(-1) * b(s), r_e, np.inf, limit=200, epsabs=1e-14, epsrel=1e-13)[0]
    return (r_e**-2 * I_in + r_e**2 * I_out) / 4.0
for label, sG_true, sG_basis in [("T3 exact sigma", 3.0, 3.0), ("T4 sigma mismatch 0.3", 3.3, 3.0), ("T4b mismatch 0.5", 3.5, 3.0)]:
    gamma0 = lambda s: (2.0/(1+s**2))**sG_true * np.exp((s**2-1)/(s**2+1))
    r_test = np.array([0.1, 0.5, 1.0, 3.0, 10.0, 50.0])
    xi_test = (r_test**2-1)/(r_test**2+1)
    ref = np.array([ref_h2(re, gamma0) for re in r_test])
    out = []
    for Nn in [16, 24, 32, 48, 64, 96]:
        # coefficients of q_0 = gamma_0 / (1-xi)^{sG_basis} = (1-xi)^{sG_true - sG_basis} exp(xi): interpolate at Gauss nodes
        xi_n = cheb_gauss_nodes(Nn)
        qv = (1-xi_n)**(sG_true-sG_basis) * np.exp(xi_n)
        Tn = cheb_T(xi_n, Nn); coef = np.linalg.solve(Tn, qv)
        mm = A2Model(Nn, 4, 1.0, 2.0, sG_basis, device=dev, xi_eval=xi_test)
        ca = torch.zeros((4, Nn), dtype=DT, device=dev); cG = torch.zeros((4, Nn), dtype=DT, device=dev)
        cG[0] = torch.tensor(coef, dtype=DT, device=dev)
        ff = mm.fields(ca, cG, 1.0)
        h2 = ff['h'][0].cpu().numpy()
        out.append((Nn, np.abs(h2-ref).max(), np.abs((h2-ref)/ref).max()))
    print(label, " ref h2 =", np.array2string(ref, precision=3))
    for Nn, ea, er in out: print("   N=%3d  abs err %.2e  rel err %.2e" % (Nn, ea, er))
