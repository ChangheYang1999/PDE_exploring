"""Between-node check of the penalty regions of the localized refits : evaluate the Cartesian temperature and
vorticity residuals of a saved state (a) on the penalty nodes of the refit (ANN: r_i = 14.5 + 5.5 cos(pi (i+1/2)/24),
theta_j = (j+1/2) pi/48, 0 <= i,j < 24; PATCH: r_i = r_c + cos(pi (i+1/2)/12), theta_j = theta_c + cos(pi (j+1/2)/12)/r_c about
Q+ = (12.42884, 5.77296) of B2_m_gauss_N144) and (b) on uniform midpoint tensor grids in (r, theta) over the same polar rectangle at
three sizes. Fields are evaluated directly from the spectral basis (code/diag_state.eval_state), residuals as in
code/local_res_Q.py: R_Theta = x^2 y Ra, R_Omega = x y RG; N_Theta, N_Omega as in PROMPT.md Section 4 (no floor; ratios where N > 0).
Reports sampled maxima, equal-node RMS values and maximal normalized ratios for both residuals, and the location of the sampled
temperature-residual maximum. Sampled maxima on finite grids, not
uniform norms. Usage: python3 code/annulus_between.py <region: ann|patch> state1.npz [state2.npz ...]"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def region(kind):
    if kind == 'ann':
        i = np.arange(24); rn = 14.5 + 5.5 * np.cos(np.pi * (i + 0.5) / 24); tn = (i + 0.5) * np.pi / 48
        return (9.0, 20.0, 0.0, np.pi / 2), np.sort(rn), np.sort(tn)
    qx, qy = 12.42884, 5.77296; rc = np.hypot(qx, qy); tc = np.arctan2(qy, qx); i = np.arange(12)
    rn = rc + np.cos(np.pi * (i + 0.5) / 12); tn = tc + np.cos(np.pi * (i + 0.5) / 12) / rc
    return (rc - 1, rc + 1, tc - 1 / rc, tc + 1 / rc), np.sort(rn), np.sort(tn)

def resid(d, R, T):
    beta = float(d['beta'])
    m, f = eval_state(d, R, T)
    F = {k: f[k].cpu().numpy() for k in ('W1', 'W2', 'a', 'a_x', 'a_y', 'G', 'G_x', 'G_y', 'Ra', 'RG')}
    X = R[:, None] * np.cos(T)[None, :]; Y = R[:, None] * np.sin(T)[None, :]
    Th = X**2 * Y * F['a']; Thx = 2 * X * Y * F['a'] + X**2 * Y * F['a_x']; Thy = X**2 * F['a'] + X**2 * Y * F['a_y']
    Om = X * Y * F['G']; Omx = Y * F['G'] + X * Y * F['G_x']; Omy = X * F['G'] + X * Y * F['G_y']
    RT = X**2 * Y * F['Ra']; NT = np.abs(F['W1'] * Thx) + np.abs(F['W2'] * Thy) + abs(beta - 2) * np.abs(Th)
    RO = X * Y * F['RG']; NO = np.abs(F['W1'] * Omx) + np.abs(F['W2'] * Omy) + np.abs(Om) + np.abs(Thx)
    RT_dir = F['W1'] * Thx + F['W2'] * Thy - (beta - 2) * Th
    return X, Y, RT, NT, RO, NO, np.abs(RT - RT_dir).max()

def report(label, d, R, T):
    X, Y, RT, NT, RO, NO, disc = resid(d, R, T)
    with np.errstate(divide='ignore', invalid='ignore'):
        rT = np.where(NT > 0, np.abs(RT) / NT, np.nan); rO = np.where(NO > 0, np.abs(RO) / NO, np.nan)
    k = np.unravel_index(np.argmax(np.abs(RT)), RT.shape)
    print(f"  {label:28s} n={RT.size:6d} max|R_T|={np.abs(RT).max():10.4f} at ({X[k]:.4f},{Y[k]:.4f}) r={np.hypot(X[k],Y[k]):.3f}"
          f"  rms|R_T|={np.sqrt((RT**2).mean()):9.4f}  max|R_T|/N_T={np.nanmax(rT):.3f} minN_T={np.nanmin(NT):.2e} nundef={int(np.isnan(rT).sum())}"
          f" | max|R_Om|={np.abs(RO).max():8.4f} rms={np.sqrt((RO**2).mean()):8.4f} max|R_Om|/N_Om={np.nanmax(rO):.3f} | form-discrepancy {disc:.1e}")

def main(kind, paths):
    (r0, r1, t0, t1), rn, tn = region(kind)
    print(f"region {kind}: {r0:.4f} <= r <= {r1:.4f}, {t0:.4f} <= theta <= {t1:.4f}; penalty nodes {len(rn)} x {len(tn)}")
    for p in paths:
        d = load_state(p); print(f"state {p}: N={int(d['N'])} M={int(d['M'])} beta={float(d['beta']):.6f}")
        report('penalty nodes', d, rn, tn)
        for nr, nt in ((33, 49), (65, 97), (129, 193)):
            R = r0 + (r1 - r0) * (np.arange(nr) + 0.5) / nr; T = t0 + (t1 - t0) * (np.arange(nt) + 0.5) / nt
            report(f'midpoint grid {nr}x{nt}', d, R, T)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
