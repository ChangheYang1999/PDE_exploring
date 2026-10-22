"""Fit Psi samples on a polar grid (r (Nr,), phi (Nphi,) midpoint angles in (0, pi/2), Psi flattened (Nr, Nphi)) into the Psi basis of
charlib2: angular projection onto sin(2n phi) (midpoint rule, exact for frequencies < 2 Nphi), then per-mode least squares of
psi_n(r)/env_n(r) as a Chebyshev series in q, with the constraint P_1(0) = c L^2/2 (c from the small-r limit of psi_1/r^2).
Input: the authors' gphys.py output (keys r, phi, Psi, a0, beta).  Output: npz usable by charsolve.py / char_eval.py (cP, a0, beta, L, ...).
Reports the fit error of Psi and the induced U against the samples (U1, U2 keys if present)."""
import sys, os, argparse, math, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from charlib2 import PsiBasis, cheb_all, DT, dev
ap = argparse.ArgumentParser(); ap.add_argument('samples'); ap.add_argument('out'); ap.add_argument('--NO', type=int, default=16); ap.add_argument('--K', type=int, default=48)
ap.add_argument('--L', type=float, default=1.0); ap.add_argument('--rmax-fit', type=float, default=1e6)
args = ap.parse_args(); dv = dev()
d = np.load(args.samples, allow_pickle=True)
r = torch.tensor(d['r'], dtype=DT, device=dv); ph = torch.tensor(d['phi'], dtype=DT, device=dv); Nr, Nphi = r.shape[0], ph.shape[0]
Psi = torch.tensor(d['Psi'], dtype=DT, device=dv).reshape(Nr, Nphi); beta = float(d['beta']); a0 = float(d['a0'])
bas = PsiBasis(beta, args.NO, args.K, L=args.L)
# angular projection: psi_n(r) = (4/pi) int_0^{pi/2} Psi sin(2n phi) dphi, midpoint rule with weight (pi/2)/Nphi
ms = torch.tensor(bas.ms, dtype=DT, device=dv)
S = torch.sin(ph[:, None] * ms[None, :])                                  # (Nphi, NO)
psi_n = (4.0 / math.pi) * (Psi @ S) * (math.pi / 2 / Nphi)                 # (Nr, NO)
# check the angular truncation: reconstruct Psi from NO modes
Psi_rec = psi_n @ S.T
ang_err = float(((Psi_rec - Psi).abs() / (Psi.abs().max(1, keepdim=True).values + 1e-300)).max())
H, dH, env = bas.radial_matrices(r)
u = r / bas.L; E = 1 + u * u; q = 1 - E ** (-bas.mu / 2); T, _, _ = cheb_all(q, args.K)
sel = r <= args.rmax_fit * bas.L
# c from the smallest radii: psi_1 ~ (c/2) r^2
c_est = float((2 * psi_n[:3, 0] / r[:3] ** 2).mean()); print(f'c estimate from psi_1/r^2 at the 3 smallest radii: {c_est:.6f} (values {[float(v) for v in 2 * psi_n[:3, 0] / r[:3] ** 2]})')
sgnK = torch.tensor([(-1.0) ** k for k in range(args.K)], dtype=DT, device=dv)
cP = torch.zeros(args.NO, args.K, dtype=DT, device=dv)
for n in range(1, args.NO + 1):
    p = psi_n[:, n - 1]
    # weighted direct fit (no division by the envelope: sampled Psi has absolute noise ~1e-13 |Psi| which the envelope u^{2n} would amplify at small r)
    wgt = 1.0 / (p.abs() + 1e-9 * p.abs().max())
    A = (H[:, n - 1, :] * wgt[:, None])[sel]; b = (p * wgt)[sel]
    if n == 1:
        A = torch.cat([A, (sgnK * 1e4)[None, :]]); b = torch.cat([b, torch.tensor([0.5 * (-2.0) * bas.L ** 2 * 1e4], dtype=DT, device=dv)])   # impose c = -2 exactly
    sol = torch.linalg.lstsq(A, b[:, None]).solution[:, 0]; cP[n - 1] = sol
    fit = H[:, n - 1, :] @ sol
    print(f'mode n={n}: max|psi_n| {float(p[sel].abs().max()):.3e}; max rel fit error (floor 1e-9 max) {float(((fit - p) * wgt)[sel].abs().max()):.2e}')
F = bas.centre_functionals(dv); cf = cP.reshape(-1)
print(f'angular truncation error of Psi at {args.NO} modes: {ang_err:.2e} (relative to max over phi at each r)')
print(f'c of the fit {float(cf @ F["c"]):.10f}  h10 {float(cf @ F["h10"]):.6e}  h01 {float(cf @ F["h01"]):.6e}  a0 {a0:.5f}')
# velocity check against the samples
X = torch.tensor(d['X'], dtype=DT, device=dv); Y = torch.tensor(d['Y'], dtype=DT, device=dv)
fb = bas.fields(cP[None], X, Y)
U1 = -fb['Psi_y'][0]; U2 = fb['Psi_x'][0]
if 'U1' in d.files:
    U1s = torch.tensor(d['U1'], dtype=DT, device=dv); U2s = torch.tensor(d['U2'], dtype=DT, device=dv)
    R = torch.sqrt(X * X + Y * Y); m = R <= args.rmax_fit * bas.L
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e6)]:
        mm = m & (R >= lo) & (R < hi)
        if mm.any():
            e1 = float(((U1 - U1s).abs() / (beta * R))[mm].max()); e2 = float(((U2 - U2s).abs() / (beta * R))[mm].max())
            print(f'   velocity fit error / (beta r) in r [{lo:g}, {hi:g}): U1 {e1:.2e}  U2 {e2:.2e}')
if 'Omega' in d.files:
    Om_s = torch.tensor(d['Omega'], dtype=DT, device=dv); Om_b = fb['Om'][0]
    R = torch.sqrt(X * X + Y * Y)
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e6)]:
        mm = (R >= lo) & (R < hi)
        if mm.any(): print(f'   Omega: -Lap Psi_fit vs sampled Omega in r [{lo:g}, {hi:g}): max |diff| {float((Om_b - Om_s)[mm].abs().max()):.3e} vs max |Omega| {float(Om_s[mm].abs().max()):.3e}')
np.savez(args.out, cP=cP.cpu().numpy(), a0=a0, beta=beta, L=args.L, NO=args.NO, K=args.K, gamma_P=bas.gamma_P, mu=bas.mu, source=args.samples)
print('saved', args.out)
