"""Project an Omega-basis state (solve_gn npz: cT, cO) onto the Psi basis of charlib2.
psi_n(r) (exact modal inverse of the stored Omega, radial_profiles) is sampled on a dense q-grid; psi_n/env_n (env_n the
basis envelope (u^2/E)^n E^{gamma_P/2}) is fitted by least squares as a Chebyshev series in q.  Reports the relative error
in units of the envelope, the centre strain c of the projection, and saves cP, a0, beta, basis parameters."""
import sys, argparse, math, numpy as np, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import Params, DT, dev
from evalfields import load_coefs, radial_profiles
from charlib2 import PsiBasis, cheb_all
ap = argparse.ArgumentParser(); ap.add_argument('npz'); ap.add_argument('out'); ap.add_argument('--NO', type=int, default=None); ap.add_argument('--K', type=int, default=None)
ap.add_argument('--qmax', type=float, default=0.9999); ap.add_argument('--qfit', type=float, default=0.999, help='fit only radii with q <= qfit (the stored far field beyond the fit domain is unconstrained junk)'); ap.add_argument('--a0', type=float, default=None)
args = ap.parse_args()
dv = dev()
P, cT, cO, NT, NO, K = load_coefs(args.npz); beta = P.beta
NOp = args.NO or NO; Kp = args.K or K
bas = PsiBasis(beta, NOp, Kp, L=P.L)
q = torch.linspace(0, args.qmax, 4000, dtype=DT, device=dv)[1:]
r = torch.cat([torch.logspace(-5, -1, 400, dtype=DT, device=dv) * P.L, bas.u_of_q(q) * P.L]); r, _ = torch.sort(torch.unique(r))
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
H, dH, env = bas.radial_matrices(r)
u = r / P.L; E = 1 + u * u; qq = 1 - E ** (-bas.mu / 2)
T, _, _ = cheb_all(qq, Kp)
cP = torch.zeros(NOp, Kp, dtype=DT, device=dv); errs = []
# exact centre data of the stored state from the (exact) modal inverse at tiny radii: psi_1 = (c/2) r^2 + alpha r^4 + ..., psi_2 = gam r^4 + ...
rt = torch.tensor([1e-3, 2e-3], dtype=DT, device=dv) * P.L
pt = radial_profiles(P, cT, cO, rt, NT, NO, K)
c_state = pt['c']
alpha = float(((pt['psi'][0] - 0.5 * c_state * rt ** 2) / rt ** 4)[0]); gam = float((pt['psi'][1] / rt ** 4)[0]) if NO > 1 else 0.0
h10_state = 2 * alpha + 4 * gam; h01_state = 2 * alpha - 4 * gam
print(f'stored state centre data: c {c_state:.10f}  h10 (=d1) {h10_state:.6e}  h01 (=d2) {h01_state:.6e}  [alpha check at 2e-3: {float(((pt["psi"][0] - 0.5 * c_state * rt ** 2) / rt ** 4)[1]):.6e}]')
sgnK = torch.tensor([(-1.0) ** k for k in range(Kp)], dtype=DT, device=dv); dsgnK = torch.tensor([(-1.0) ** (k + 1) * k * k * 2.0 for k in range(Kp)], dtype=DT, device=dv)
a1 = (bas.gamma_P - 2) / 2.0
WCON = 1e4
for n in range(1, min(NO, NOp) + 1):
    psi = prof['psi'][n - 1]; dpsi = prof['dpsi'][n - 1]; e = env[:, n - 1]
    g = psi / e
    sel = qq <= args.qfit
    A = T[sel]; b = g[sel]
    if n == 1:   # constraints: P1(0) = c L^2 / 2 ; alpha = (a1 P1(0) + (mu/2) P1'(0)) / L^4
        rows = torch.stack([sgnK, a1 * sgnK + 0.5 * bas.mu * dsgnK]) * WCON
        rhs = torch.tensor([0.5 * c_state * P.L ** 2, alpha * P.L ** 4], dtype=DT, device=dv) * WCON
        A = torch.cat([A, rows]); b = torch.cat([b, rhs])
    if n == 2:   # constraint: P2(0) = gam L^4
        A = torch.cat([A, (sgnK * WCON)[None, :]]); b = torch.cat([b, torch.tensor([gam * P.L ** 4 * WCON], dtype=DT, device=dv)])
    sol = torch.linalg.lstsq(A, b[:, None]).solution[:, 0]
    cP[n - 1] = sol
    fit = H[:, n - 1, :] @ sol; dfit = dH[:, n - 1, :] @ sol
    scale = g.abs().max()
    e0 = ((fit - psi) / e)[sel].abs().max().item() / scale; e1 = ((dfit - dpsi).abs() / (dpsi.abs() + 1e-6 * (e * scale / r)))[sel].max().item()
    errs.append((n, float(e0), float(e1))); print(f'mode n={n}: max |psi/env| {scale:.4e}; rel fit error (units of env*max|psi/env|) {e0:.2e}; psi\' rel {e1:.2e}')
F = bas.centre_functionals(dv); cf = cP.reshape(-1)
c_proj = float(cf @ F['c']); c_state = prof['c']
print(f'c (strain) of projection {c_proj:.10f}   c of the stored state {c_state:.10f}')
print(f'h10 {float(cf @ F["h10"]):.6e}  h01 {float(cf @ F["h01"]):.6e}')
sgn = torch.tensor([(-1.0) ** k for k in range(K)], dtype=DT, device=dv)
a0 = float(cT[0].to(dv) @ sgn) / P.L if args.a0 is None else args.a0
print(f'a0 {a0:.6f}')
np.savez(args.out, cP=cP.cpu().numpy(), a0=a0, beta=beta, L=P.L, NO=NOp, K=Kp, gamma_P=bas.gamma_P, mu=bas.mu, source=args.npz, fit_errors=np.array(errs))
print('saved', args.out)
