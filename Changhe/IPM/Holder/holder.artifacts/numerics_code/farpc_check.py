"""Restricted (per-circle) versus unrestricted exterior transport LP on a well-conditioned region (heuristic; NUM_REPORT 9c).
For each radial shell of otlp.far_cells the per-shell LP is solved on the shell rescaled to the unit circle with masses normalised to unit L1 norm
(value = rho^alpha |m|_1 LP), which avoids the ill-conditioning of shells at radius above about 1e3 (potentials of size rho^alpha against masses of
size 1/rho). The sum over shells is the best bound obtainable by per-circle couplings on this discretisation; the unrestricted LP couples all shells.
Expected order: restricted >= unrestricted. Output of the run of 2026-10-28T14:00Z: runs/midext/farpc_check.log (agreement to 6 decimals on
1 <= |w - m| <= 1e3 at alpha 1/2 and 3/4, phi = 0 and pi/2). Usage: python3 farpc_check.py  (about 1 minute)."""
import sys, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
from otlp import far_cells, solve_lp

def per_shell_normalized(nf, mf, ntheta, Jf, alpha):
    tot = 0.0
    for j in range(Jf):
        sl = slice(j*ntheta, (j+1)*ntheta); nodes = nf[sl]; m = mf[sl] - mf[sl].mean()
        rho = np.sqrt((nodes**2).sum(axis=1)).mean(); L1 = np.abs(m).sum()
        if L1 == 0: continue
        u, v, h, _, _ = solve_lp(nodes/rho, m/L1, alpha, idx_fix=0, verbose=False, max_add=5000, max_iter=100)
        tot += rho**alpha*L1*v
    return tot

if __name__ == '__main__':
    cases = [(0.5, 0.0, 1e3), (0.5, 0.7854, 1e3), (0.5, 0.0, 1e6), (0.75, 0.0, 1e3), (0.75, 0.7854, 1e3)]
    for (alpha, beta, rmax) in cases:
        qf, ntheta = 1.5, 48; Jf = int(np.ceil(np.log(rmax)/np.log(qf)))
        nf, mf, cf = far_cells((0.5, 0.0), 1.0, qf, Jf, ntheta, beta)
        u, val, hist, h, plan = solve_lp(nf, mf, alpha, idx_fix=0, verbose=False, max_add=30000, max_iter=300)
        s = 30.0; u2, val2, hist2, _, _ = solve_lp(nf/s, mf, alpha, idx_fix=0, verbose=False, max_add=30000, max_iter=300); val2 *= s**alpha
        pc = per_shell_normalized(nf, mf, ntheta, Jf, alpha)
        print(f"alpha {alpha} beta {beta:.4f} rho_max {rmax:.0e} ({Jf} shells): unrestricted {val:.6f} (rescaled check {val2:.6f}, viol {hist[-1]['nviol']}); "
              f"per-shell normalized {pc:.6f}; restricted - unrestricted = {pc - val:+.6f}", flush=True)
