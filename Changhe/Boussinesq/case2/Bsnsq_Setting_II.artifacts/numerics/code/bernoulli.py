"""Bernoulli / Lyapunov identity residual of a saved state (definitions from the verifier's
Bernoulli residual note, not included). With a = 2 beta - 1, kappa = beta - 2, W = beta X + U,
J(v1, v2) = (-v2, v1):  F = a W + Omega J W - Theta e_2,  B(X) = int_0^1 F(tX).X dt = int_0^r F_r(rho, phi) drho,
L = B + y Theta,  R_L = W.grad L - a |W|^2 - kappa y Theta  (= 0 for an exact profile; exact identity
R_L = y R_Theta - (W.JX) int_0^1 t C(tX) dt, so it is a ray-weighted combination of the PDE defects).
Here grad L is computed INDEPENDENTLY by 4th-order finite differences on a fine (log r, phi) grid, and B by cumulative
Simpson integration along rays; normalization N_L = |W_r L_r| + |W_phi L_phi / r| + a |W|^2 + |kappa y Theta|. Blind spots
(verifier): R_L = 0 identically on both axes and (beta = 2) at every stagnation point, where N_L also vanishes; ratios are
reported only where N_L > 1e-6 max N_L (disclosed)."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state


def main(path, rmin=1e-3, rmax=300.0, nr=1200, nth=64):
    d = load_state(path); beta = float(d['beta']); a = 2 * beta - 1; kappa = beta - 2
    r = np.geomspace(rmin, rmax, nr); th = (np.arange(nth) + 0.5) * np.pi / (2 * nth)
    m, f = eval_state(d, r, th)
    g = {k: f[k].cpu().numpy() for k in ('x', 'y', 'W1', 'W2', 'a', 'G', 'a_x', 'a_y')}
    x, y = g['x'], g['y']; W1, W2 = g['W1'], g['W2']
    Theta = x ** 2 * y * g['a']; Omega = x * y * g['G']
    ct, st = np.cos(th)[None, :], np.sin(th)[None, :]
    Wr = W1 * ct + W2 * st; Wphi = -W1 * st + W2 * ct
    JWr = -W2 * ct + W1 * st                     # (J W) . e_r
    Fr = a * Wr + Omega * JWr - Theta * st
    # B(r, phi) = int_0^r F_r drho; F_r = O(rho) near 0: start from 0 at r = 0 (add the segment 0..rmin by F_r ~ rho: ~ Fr[0]*rmin/2)
    lr = np.log(r)
    B = np.zeros_like(Fr)
    B[0] = 0.5 * Fr[0] * r[0]
    # cumulative trapezoid in rho with the log grid: int F_r drho = int F_r rho dlog rho
    integrand = Fr * r[:, None]
    B[1:] = B[0] + np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(lr)[:, None], axis=0)
    L = B + y * Theta
    # gradients by 4th-order centered differences in log r (uniform) and phi (uniform, even reflection)
    h = lr[1] - lr[0]; dth = th[1] - th[0]
    Lr = np.zeros_like(L); Lr[2:-2] = (-L[4:] + 8 * L[3:-1] - 8 * L[1:-3] + L[:-4]) / (12 * h)
    Lr[:2] = np.nan; Lr[-2:] = np.nan
    Lr = Lr / r[:, None]                           # d/dr = (1/r) d/dlog r
    Le = np.concatenate([L[:, [1, 0]], L, L[:, [-1, -2]]], 1)
    Lphi = (-Le[:, 4:] + 8 * Le[:, 3:-1] - 8 * Le[:, 1:-3] + Le[:, :-4]) / (12 * dth)
    WgradL = Wr * Lr + Wphi * Lphi / r[:, None]
    RL = WgradL - a * (W1 ** 2 + W2 ** 2) - kappa * y * Theta
    NL = np.abs(Wr * Lr) + np.abs(Wphi * Lphi / r[:, None]) + a * (W1 ** 2 + W2 ** 2) + np.abs(kappa * y * Theta)
    ok = np.isfinite(RL) & (NL > 1e-6 * np.nanmax(NL))
    print(f"=== {path}: beta={beta}  grid {nr} x {nth} (r in [{rmin}, {rmax}]); ratios where N_L > 1e-6 max N_L ({ok.sum()}/{RL.size} points)")
    print("   band            max|R_L|      max|R_L|/N_L   at (r, phi)          max N_L")
    for lo, hi in [(0, 0.1), (0.1, 1), (1, 5), (5, 12), (12, 20), (20, 50), (50, 100), (100, 300)]:
        mk = ok & (r[:, None] >= lo) & (r[:, None] < hi)
        if mk.sum() == 0: continue
        ratio = np.where(mk, np.abs(RL) / NL, -1); i, j = np.unravel_index(ratio.argmax(), ratio.shape)
        print(f"   [{lo:5g},{hi:5g})   {np.nanmax(np.abs(RL)[mk]):.3e}     {ratio[i, j]:.3e}      ({r[i]:8.3f}, {th[j]:.3f})    {np.nanmax(NL[mk]):.3e}")
    # also the pointwise check of the identity R_L = y R_Theta - (W.JX) I at a few points (uses the state's R_Theta; I from the state's R_Omega along rays)
    Ra = f['Ra'].cpu().numpy(); RG = f['RG'].cpu().numpy()
    RTheta = x ** 2 * y * Ra; ROmega = x * y * RG
    Cc = ROmega                                   # exact inverse: E_curl = E_div = 0
    # I(X) = int_0^1 t C(tX) dt = (1/r^2) int_0^r rho C(rho, phi) drho
    integ = Cc * r[:, None]
    Icum = np.zeros_like(Cc); Icum[1:] = np.cumsum(0.5 * (integ[1:] * r[1:, None] + integ[:-1] * r[:-1, None]) * np.diff(lr)[:, None], axis=0)
    I = Icum / r[:, None] ** 2
    WJX = W1 * (-y) + W2 * x
    RL_id = y * RTheta - WJX * I
    sel = ok & (r[:, None] > 0.5) & (r[:, None] < 100)
    print(f"   identity check R_L vs y R_Theta - (W.JX) I on 0.5 < r < 100: max|diff|/max|R_L| = {np.nanmax(np.abs(RL - RL_id)[sel]) / np.nanmax(np.abs(RL)[sel]):.3e} (FD/quadrature error of this diagnostic)")


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument('paths', nargs='+'); ap.add_argument('--nr', type=int, default=1200); ap.add_argument('--nth', type=int, default=64)
    args = ap.parse_args()
    for p in args.paths:
        main(p, nr=args.nr, nth=args.nth)
