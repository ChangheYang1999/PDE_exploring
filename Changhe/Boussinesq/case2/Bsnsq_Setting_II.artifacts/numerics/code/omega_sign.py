"""Sign pattern of the fitted Omega = x y G on the open quadrant (fitted data only): sign of G on a log-polar grid,
sign of G on the x-axis (g = Omega_y(x,0) = x G(x,0)) and on the y-axis (Omega_x(0,y) = y G(0,y)), whether {Omega > 0} is bounded
(positive samples at the largest radii?) and where it meets the axes (sign changes of G along each half-axis)."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
from charcheck import build, find_xstar
for path in sys.argv[1:]:
    d = load_state(path); beta = float(d['beta']); a0 = float(d['a0_target'])
    r = np.geomspace(0.02, 1e4, 240); th = np.concatenate([[1e-7], np.linspace(0.02, np.pi / 2 - 0.02, 61), [np.pi / 2 - 1e-7]])
    m, f = eval_state(d, r, th); G = f['G'].cpu().numpy()
    B = build(d, rmin=1e-3, rmax=1e4, nr=3000); xs, lam = find_xstar(B)
    print(f"=== {path}: beta={beta} a0={a0:+.0f} x1={xs:.4f}")
    def changes(v):
        i = np.where(np.diff(np.sign(v)) != 0)[0]; return [f"{r[j]:.3g}->{'+' if v[j+1] > 0 else '-'}" for j in i]
    gx = G[:, 0]; gy = G[:, -1]
    print(f"  x-axis: sign of g = Omega_y(x,0) = x G(x,0): at x -> 0: {'+' if gx[0] > 0 else '-'}; sign changes (radius -> new sign): {changes(gx)}")
    print(f"          on (0, x1 = {xs:.3f}]: g {'> 0' if (gx[r <= xs] > 0).all() else ('< 0' if (gx[r <= xs] < 0).all() else 'changes sign')} (min G = {gx[r <= xs].min():+.3e}, max G = {gx[r <= xs].max():+.3e})")
    print(f"  y-axis: sign of Omega_x(0,y) = y G(0,y): at y -> 0: {'+' if gy[0] > 0 else '-'}; sign changes: {changes(gy)}")
    pos = G > 0
    frac = pos.mean(axis=1)
    rows = []
    for i in range(0, len(r), 12):
        rows.append(f"r={r[i]:8.3g}: {''.join('+' if v else '-' for v in pos[i, ::3])}")
    print("  sign of Omega over the quadrant (rows r, columns phi from 0 to pi/2 in 21 steps):")
    for l in rows: print("   " + l)
    rmax_pos = r[pos.any(axis=1)].max() if pos.any() else None
    print(f"  {{Omega > 0}}: positive samples up to r = {rmax_pos:.3g} (grid max {r[-1]:.3g}): {'UNBOUNDED on the grid (positive samples at the largest radii)' if rmax_pos == r[-1] else 'bounded on the grid'}; fraction of positive samples on the last 5 radii: {pos[-5:].mean():.2f}")
    neg = G < 0
    rmax_neg = r[neg.any(axis=1)].max() if neg.any() else None
    print(f"  {{Omega < 0}}: negative samples up to r = {rmax_neg:.3g} (grid max {r[-1]:.3g}): {'UNBOUNDED on the grid (negative samples at the largest radii)' if rmax_neg == r[-1] else 'bounded on the grid'}; fraction of negative samples on the last 5 radii: {neg[-5:].mean():.2f}")
    print(f"  {{Omega < 0}} meets the x-axis where G(x,0) < 0: {'yes, x in ' + str([f'{v:.3g}' for v in (r[gx < 0][[0, -1]] if (gx < 0).any() else [])]) if (gx < 0).any() else 'no'}; meets the y-axis where G(0,y) < 0: {'yes, y in ' + str([f'{v:.3g}' for v in (r[gy < 0][[0, -1]] if (gy < 0).any() else [])]) if (gy < 0).any() else 'no'}")
    # per-ray sign sequences at increasing r: count rays containing the patterns + - + and - + - (after merging equal neighbours)
    def runs_of(col):
        sg = np.sign(col); sg = sg[sg != 0]; out = [sg[0]] if len(sg) else []
        for v in sg[1:]:
            if v != out[-1]: out.append(v)
        return out
    n_pmp = n_mpm = 0; n_rays = len(th)
    for j in range(n_rays):
        seq = runs_of(G[:, j]); ss = ''.join('+' if v > 0 else '-' for v in seq)
        if '+-+' in ss: n_pmp += 1
        if '-+-' in ss: n_mpm += 1
    print(f"  rays (fixed angle, increasing r, {n_rays} sampled angles incl. both axes): pattern '+ - +' occurs on {n_pmp} rays; '- + -' on {n_mpm} rays; sign-change counts per ray: {np.bincount([len(runs_of(G[:, j])) - 1 for j in range(n_rays)])} (index = number of sign changes along the ray)")
    rpos = r[frac > 0]; print(f"  {{Omega > 0}} meets the x-axis where G(x,0) > 0: {'yes, x in ' + str([f'{v:.3g}' for v in (r[gx > 0][[0, -1]] if (gx > 0).any() else [])]) if (gx > 0).any() else 'no'}; meets the y-axis where G(0,y) > 0: {'yes, y in ' + str([f'{v:.3g}' for v in (r[gy > 0][[0, -1]] if (gy > 0).any() else [])]) if (gy > 0).any() else 'no'}")
    sys.stdout.flush()
