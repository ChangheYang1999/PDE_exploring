"""Sampled constants for the verifier's conditional robust critical-zero obstruction at beta = 2 at the
interior zero Q+ of a saved state. On the closed ball B = B(Q+, R): A = DW(Q+) (polar stencil, code/zero_jac.py),
K = ||A^-1||_2, e = |W(Q+)|, k(R) = sup_B ||I - A^-1 DW||_2, gamma(R) = inf_B |grad Theta|. The obstruction: if
c = k + K d1 < 1, K (e + d0) < (1 - c) R and dtheta < gamma, no C^1 pair (W, Theta) with sup_B |W - Wbar| <= d0,
sup_B ||DW - DWbar|| <= d1, sup_B |grad Theta - grad Thetabar| <= dtheta solves W.grad Theta = 0 near B.
DW on the ball is formed by central differences of the directly evaluated W on a polar product grid covering the ball
(spacing h; the trace defect |tr DW - 2 beta| over the ball is reported as the FD accuracy check). SAMPLED maxima/minima over
the grid: numerical constants, not certified bounds."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
from charcheck import build
from zero_jac import find_zeros, point_data_batch

def ball_constants(d, Q, A, R, n=121, pad=1.05):
    beta = float(d['beta']); x0, y0 = Q; r0 = np.hypot(x0, y0); t0 = np.arctan2(y0, x0)
    Rg = pad * R; dth = np.arcsin(min(Rg / r0, 0.999))
    rr = np.linspace(r0 - Rg, r0 + Rg, n)
    if y0 < 1e-6:
        # point on the x-axis: by the parities (W1, Theta_x even in y; W2, Theta_y odd in y) the norms ||I - A^-1 DW|| (A diagonal
        # there) and |grad Theta| at (x, -y) equal those at (x, y), so the upper half-ball represents the full ball exactly
        tt = np.linspace(1e-9, dth, n)
    else:
        tt = np.linspace(t0 - dth, t0 + dth, n)
    if rr[0] <= 0 or tt[0] <= 0 or tt[-1] >= np.pi / 2 or Rg >= r0:
        raise ValueError(f"ball of radius {R} about ({x0:.4f},{y0:.4f}) is not inside the open quadrant's polar rectangle: no clipping is done; use a smaller R")
    m, f = eval_state(d, rr, tt)
    g = {k: f[k].cpu().numpy() for k in ('W1', 'W2', 'a', 'a_x', 'a_y', 'x', 'y')}
    X, Y = g['x'], g['y']; Rm, Tm = np.meshgrid(rr, tt, indexing='ij'); c, s = np.cos(Tm), np.sin(Tm)
    def grad(F):
        F_r = np.gradient(F, rr, axis=0); F_t = np.gradient(F, tt, axis=1)
        return c * F_r - s * F_t / Rm, s * F_r + c * F_t / Rm
    W1x, W1y = grad(g['W1']); W2x, W2y = grad(g['W2'])
    inside = (X - x0) ** 2 + (Y - y0) ** 2 <= R ** 2   # for an axis point this is the upper half-ball (see above)
    # exclude the 2 outermost grid layers (one-sided differences) from the ball evaluation by construction (pad > 1)
    Ainv = np.linalg.inv(A); K = np.linalg.norm(Ainv, 2)
    DW = np.stack([np.stack([W1x, W1y], -1), np.stack([W2x, W2y], -1)], -2)      # [..., 2, 2]
    M = np.eye(2) - np.einsum('ij,...jk->...ik', Ainv, DW)
    kk = np.linalg.norm(M[inside], 2, axis=(-2, -1)).max()
    tr_def = np.abs(W1x + W2y - 2 * beta)[inside].max()
    Thx = 2 * X * Y * g['a'] + X * X * Y * g['a_x']; Thy = X * X * g['a'] + X * X * Y * g['a_y']
    gT = np.hypot(Thx, Thy); gamma = gT[inside].min(); gTmax = gT[inside].max()
    Wmax = np.hypot(g['W1'], g['W2'])[inside].max()
    Th = X * X * Y * g['a']; Thmin = np.abs(Th)[inside].min(); Thmax = np.abs(Th)[inside].max()
    return dict(K=K, k=kk, gamma=gamma, gTmax=gTmax, Wmax=Wmax, tr_def=tr_def, npts=int(inside.sum()), h=rr[1] - rr[0], Thmin=Thmin, Thmax=Thmax)

def main(path, Qgiven=None):
    d = load_state(path); beta = float(d['beta'])
    if Qgiven is None:
        B = build(d, rmin=1e-3, rmax=1e4, nr=4000)
        zx, zy, zs = find_zeros(d, B)
        P = np.array([zx[0], 0.0]) if zx else None
        far = [z for z in zs if P is None or np.hypot(z[0] - P[0], z[1] - P[1]) > 2.0]
        Q = point_data_batch(d, far)
        x, y, q = max(zip([z[0] for z in far], [z[1] for z in far], Q), key=lambda t: abs(t[2]['Theta']))
    else:
        x, y = Qgiven; q = point_data_batch(d, [(x, y)])[0]
    A = q['DW']; e = np.hypot(q['W1'], q['W2'])
    print(f"=== {path}: beta={beta}; Q+=({x:.6f},{y:.6f}); A=DW(Q+)={np.round(A,5).tolist()}; eig={np.round(q['ev'],5)}; e=|W(Q+)|={e:.2e}; |grad Theta(Q+)|={np.hypot(q['Theta_x'],q['Theta_y']):.4f}; K=||A^-1||={np.linalg.norm(np.linalg.inv(A),2):.4f}; ||A||={np.linalg.norm(A,2):.4f}", flush=True)
    print("   R    k=sup||I-A^-1 DW||  gamma=inf|gradTheta|  sup|gradTheta|  sup|W|   FD trace defect  grid h   | with c=(1+k)/2: d1=(1-k)/(2K) (c = k + K d1 exactly), d0 threshold (1-c)R/K-e (strict), dtheta<gamma (strict)", flush=True)
    for R in [0.05, 0.1, 0.25, 0.5, 1.0]:
        try:
            cst = ball_constants(d, (x, y), A, R, n=121)
        except ValueError as ex:
            print(f"  {R:5.2f}  skipped: {ex}", flush=True); continue
        K, k, gamma = cst['K'], cst['k'], cst['gamma']
        if not all(np.isfinite([k, gamma, cst['tr_def']])): print(f"  {R:5.2f}  skipped: non-finite constants", flush=True); continue
        if k < 1:
            c = (1 + k) / 2; d1 = (1 - k) / (2 * K); d0 = (1 - c) * R / K - e
            adm = f"d1={d1:.4f}  d0<{d0:.4f} (threshold, strict)  dtheta<{gamma:.4f}"
        else:
            adm = "k >= 1: no admissible perturbation at this R (take a smaller ball)"
        extra = f"  inf_B|Theta|={cst['Thmin']:.3f} sup_B|Theta|={cst['Thmax']:.3f}" if abs(beta - 2) > 1e-12 else ""
        print(f"  {R:5.2f} {k:8.4f}            {gamma:10.4f}        {cst['gTmax']:9.4f}   {cst['Wmax']:8.4f}   {cst['tr_def']:.2e}       {cst['h']:.4f}  | {adm}{extra}", flush=True)

if __name__ == '__main__':
    # usage: robust_zero.py state.npz [x y]   (x y: known Q+ coordinates; otherwise the zero search of zero_jac.py is run)
    if len(sys.argv) >= 4: main(sys.argv[1], (float(sys.argv[2]), float(sys.argv[3])))
    else: main(sys.argv[1])
