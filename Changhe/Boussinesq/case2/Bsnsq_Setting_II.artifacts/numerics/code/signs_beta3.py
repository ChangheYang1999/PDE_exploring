"""Lead request 2026-10-21T15:49Z (Theorem 77 hypotheses, beta > 2): sampled descriptions of stored beta > 2 states (rejected fitted states,
not profiles). For each state: (i) the fraction of sampled points of Q1 with sgn(a0) Omega < 0 in the radial bands 10-20, 20-50, 50-100,
100-1000, 1000-1e4, 1e4-1e6 (log-spaced radii x 90 interior angles), and whether sampled points with sgn(a0) Omega < 0 occur in the outermost
band; (ii) the sampled angular profile of r^(1/beta) Omega at three selected sampled radii (nearest to 1e3, 1e4 and 1e6; the last is the
outermost row), printed at every fifth of the 90 angles (theta = (5j + 1/2) pi/180) with the number of adjacent-sample sign transitions on the
90-angle row (89 pairs, axes excluded, no wraparound); band membership uses hypot(x, y) in floating point, so the nominal r = 1e6 row partly
falls into [1e4, 1e6); (iii) the numerically located zeros of W in the closed first quadrant from
the state's runs/zjac_<state>.log (x-axis, y-axis and interior zeros with their computed DW data), quoted verbatim. Fields from the spectral
basis (code/diag_state.eval_state). Usage: python3 -u code/signs_beta3.py states/R6_fix3_N176M44.npz ..."""
import sys, re, glob, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def main(paths):
    R = np.geomspace(0.5, 1e6, 400); T = (np.arange(90) + 0.5) * (np.pi / 2) / 90
    bands = ((10, 20), (20, 50), (50, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e6))
    for p in paths:
        d = load_state(p); beta = float(d['beta']); a0 = float(d['a0_target']); sg = np.sign(a0); name = p.split('/')[-1].replace('.npz', '')
        m, f = eval_state(d, R, T); G = f['G'].cpu().numpy()
        X = R[:, None] * np.cos(T)[None, :]; Y = R[:, None] * np.sin(T)[None, :]; RR = np.hypot(X, Y); Om = X * Y * G
        print(f"\n=== {name}: beta = {beta:.4f}, a0 target = {a0:+.0f}, N = {int(d['N'])}, M = {int(d['M'])}; grid {len(R)} log radii in [0.5, 1e6] x {len(T)} interior angles")
        print("  (i) fraction of sampled points with sgn(a0) Omega < 0 by radial band (and the angular range of such points):")
        for lo, hi in bands:
            msk = (RR >= lo) & (RR < hi); neg = (sg * Om < 0) & msk; fr = neg.sum() / max(1, msk.sum())
            ang = np.arctan2(Y[neg], X[neg]) if neg.any() else None
            rng = f"theta in [{ang.min():.3f}, {ang.max():.3f}]" if ang is not None else "none"
            print(f"      [{lo:g}, {hi:g}): {fr:6.3f}  ({int(neg.sum())} of {int(msk.sum())} points; {rng})")
        last = RR >= 1e5; print(f"      sampled points with sgn(a0) Omega < 0 at r >= 1e5: {int(((sg * Om < 0) & last).sum())} of {int(last.sum())}  (the computational domain is the whole plane; 'outer boundary' = largest sampled radius 1e6)")
        print("  (ii) r^(1/beta) Omega at three selected sampled radii (every fifth of the 90 angles; adjacent-sample sign transitions counted on the 90-angle row):")
        for r0 in (1e3, 1e4, 1e6):
            k = int(np.argmin(np.abs(R - r0))); row = R[k] ** (1 / beta) * Om[k]
            sc = int((np.sign(row[1:]) != np.sign(row[:-1])).sum())
            print(f"      r = {R[k]:.3g}: sign changes in (0, pi/2) = {sc}; values at theta = (5j+1/2) pi/180: {np.array2string(row[::5], precision=3, max_line_width=250)}")
        print("  (iii) numerically located zeros of W (from the zjac log; computed stencil data, not enclosures):")
        logs = glob.glob(f'runs/zjac_{name}.log')
        if not logs: print("      no zjac log for this state"); continue
        for line in open(logs[0]):
            if re.search(r'x-axis zeros|y-axis zeros|P1=|P2=|^\s+Q=|Y1=|Y2=|axis zero', line) and 'rho=' not in line:
                print("      " + line.rstrip()[:260])

if __name__ == '__main__':
    main(sys.argv[1:])
