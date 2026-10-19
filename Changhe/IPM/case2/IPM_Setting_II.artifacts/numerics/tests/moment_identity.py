"""Finite-radius moment identity (referee protocol item 5) for a saved zeta state (optionally forced with lambda f0):
   (alpha - 1) M(R') - Q(R') + B(R') - 2 lambda int_{B_R'} zeta f0 phi = 2 int_{B_R'} zeta E phi,
with phi = r^-3 sin 3th, M = int rho phi, Q = int rho W.grad phi, B = boundary flux int rho phi V.n, E = F_zeta - lambda f0.
All terms are evaluated with the same quadrature (GL in xi on the interpolant; exact in theta) at several radii R'.
Usage: python3 tests/moment_identity.py state.pt [Nr Nth R] [lambda seed_cl0 seed_ay]"""
import sys, math; sys.path.insert(0, 'code'); sys.path.insert(0, 'tests')
import torch, numpy as np
from ipm2polar import Disc, bary_weights
from zetasolve import initial_zeta
torch.set_default_dtype(torch.float64)
dev = 'cuda'
fn = sys.argv[1]
st = torch.load(fn, map_location=dev, weights_only=False)
a = st['args']; Nr, Nth, R = a['Nr'], a['Nth'], a['R']
d = Disc(Nr, Nth, R, K=2, tail='power2', device=dev, smooth=a.get('smooth', False))
q = st['q'].to(dev); cl = float(st['cl']); lam = float(st.get('lam', 0.0))
v = d.pack(q, cl); qz, _ = d.unpack(v)
out = d.zeta_residual_modes(qz, torch.tensor(cl, device=dev), return_all=True)
f0_phys = None
if lam != 0.0:
    v0 = initial_zeta(d, a['cl0'], eps=0.0, ay=a['ay'])
    qz0, cl0 = d.unpack(v0)
    f0_phys = d.to_phys(d.zeta_residual_modes(qz0, cl0))
zeta, rho, Ur, Ut, Rz = out['zeta'], out['rho'], out['Ur'], out['Ut'], out['Rz']
thp = d.theta_p[:, None]; rr = d.r[None, :]
phi = rr ** -3 * torch.sin(3 * thp); phi_r = -3 * rr ** -4 * torch.sin(3 * thp); phi_t_over_r = 3 * rr ** -4 * torch.cos(3 * thp)
Wgphi = Ur * phi_r + Ut * phi_t_over_r
E = Rz - (lam * f0_phys if f0_phys is not None else 0.0)
# radial integration of theta-averaged integrands via GL on the interpolant
xg, wg = np.polynomial.legendre.leggauss(600)
def cum_int(h_r, Rp):
    """int_0^Rp h(r) r dr for h at the nodes."""
    xi_max_p = math.log(1 + Rp ** 2 / d.L ** 2)
    xi = 0.5 * xi_max_p * (xg + 1.0); w = 0.5 * xi_max_p * wg
    xx = 2.0 * xi / d.xi_max - 1.0
    wb = bary_weights(d.x); T = wb[None, :] / (xx[:, None] - d.x[None, :]); P = T / T.sum(axis=1, keepdims=True)
    P = torch.tensor(P, device=dev); xi_t = torch.tensor(xi, device=dev); w_t = torch.tensor(w, device=dev)
    hg = P @ h_r
    return float(torch.sum(w_t * hg * d.L ** 2 * torch.exp(xi_t) / 2.0))
def tmean(f): return f.mean(dim=0) * 2 * math.pi
c = float(d.taylor_psi(out['p'])[2])
print("state %s: c_l = %.6f, c = %.6f, lambda = %.3f, compat. defect c_l - 1/2 - c = %.2e" % (fn, cl, c, lam, cl - 0.5 - c))
print("R'      (a-1)M      -Q        +B(flux)   -2lam int zeta f0 phi   | LHS        RHS=2 int zeta E phi   | LHS-RHS")
for Rp in (1.0, 3.0, 10.0, 30.0, 100.0, R):
    M = cum_int(tmean(rho * phi), Rp); Q = cum_int(tmean(rho * Wgphi), Rp)
    # boundary flux at r = Rp: int rho phi (c_l r + Ur) Rp dtheta ; interpolate rho*phi*Vr to Rp
    Vr = cl * rr + Ur
    g = tmean(rho * phi * Vr)        # function of r: int over theta of rho phi V_r
    xi_p = math.log(1 + Rp ** 2 / d.L ** 2); xp = 2 * xi_p / d.xi_max - 1
    wb = bary_weights(d.x); tt = wb / (xp - d.x) if not np.any(np.abs(xp - d.x) < 1e-14) else None
    if tt is None:
        gR = float(g[int(np.argmin(np.abs(xp - d.x)))])
    else:
        gR = float((torch.tensor(tt / tt.sum(), device=dev) @ g))
    Bf = gR * Rp
    Fterm = -2 * lam * cum_int(tmean(zeta * f0_phys * phi), Rp) if f0_phys is not None else 0.0
    LHS = (cl - 1) * M - Q + Bf + Fterm
    RHS = 2 * cum_int(tmean(zeta * E * phi), Rp)
    print("%6.1f  %9.4f  %9.4f  %9.4f   %9.4f              | %9.4f   %9.4f              | %9.2e" % (Rp, (cl - 1) * M, -Q, Bf, Fterm, LHS, RHS, LHS - RHS))
