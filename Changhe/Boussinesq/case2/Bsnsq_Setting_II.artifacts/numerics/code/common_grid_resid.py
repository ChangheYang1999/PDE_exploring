"""Region-wise maxima of the Cartesian residuals of several saved states on ONE common sample set that is independent of every state's
collocation grid (fills the 'not measured' cell of the coverage table: residual maxima of different resolutions on one common independent
sample set). Grid: radii r_k = geomspace(0.02, 2000, 200) * (1 + 1e-3 sin(k)), angles theta_j = (j + 0.37) (pi/2) / 50, j = 0..49 (interior
angles only; not the midpoints of any M in use). Fields from the spectral basis (code/diag_state.eval_state); residuals as in code/local_res_Q.py:
R_Theta = x^2 y Ra, R_Omega = x y RG, N_Theta, N_Omega as in PROMPT.md Section 4, ratios |R|/N formed where N > 0 (none undefined in the
logged runs; counted). Regions r < 1, 1 <= r < 10, 10 <= r < 100, r >= 100. Also the desingularized maxima |Ra|, |RG| per region. Sampled
maxima on a finite grid of fitted states; no uniform norms. Usage: python3 code/common_grid_resid.py state1.npz [state2.npz ...]"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def main(paths):
    k = np.arange(200); R = np.geomspace(0.02, 2000, 200) * (1 + 1e-3 * np.sin(k)); T = (np.arange(50) + 0.37) * (np.pi / 2) / 50
    print(f"common grid: {len(R)} radii in [{R.min():.3g}, {R.max():.4g}] x {len(T)} interior angles ({len(R)*len(T)} points); regions r<1, 1-10, 10-100, >=100")
    print("state                     N   M  beta   region   max|R_T|   max|R_T|/N_T  max|R_Om|  max|R_Om|/N_Om  max|Ra|   max|RG|   min N_T   min N_Om  nundef")
    for p in paths:
        d = load_state(p); beta = float(d['beta']); name = p.split('/')[-1].replace('.npz', '')
        m, f = eval_state(d, R, T)
        F = {kk: f[kk].cpu().numpy() for kk in ('W1', 'W2', 'a', 'a_x', 'a_y', 'G', 'G_x', 'G_y', 'Ra', 'RG')}
        X = R[:, None] * np.cos(T)[None, :]; Y = R[:, None] * np.sin(T)[None, :]; RR = np.hypot(X, Y)
        Th = X**2 * Y * F['a']; Thx = 2 * X * Y * F['a'] + X**2 * Y * F['a_x']; Thy = X**2 * F['a'] + X**2 * Y * F['a_y']
        Om = X * Y * F['G']; Omx = Y * F['G'] + X * Y * F['G_x']; Omy = X * F['G'] + X * Y * F['G_y']
        RT = X**2 * Y * F['Ra']; NT = np.abs(F['W1'] * Thx) + np.abs(F['W2'] * Thy) + abs(beta - 2) * np.abs(Th)
        RO = X * Y * F['RG']; NO = np.abs(F['W1'] * Omx) + np.abs(F['W2'] * Omy) + np.abs(Om) + np.abs(Thx)
        with np.errstate(divide='ignore', invalid='ignore'):
            rT = np.where(NT > 0, np.abs(RT) / NT, np.nan); rO = np.where(NO > 0, np.abs(RO) / NO, np.nan)
        for lab, msk in (('r<1', RR < 1), ('1-10', (RR >= 1) & (RR < 10)), ('10-100', (RR >= 10) & (RR < 100)), ('>=100', RR >= 100)):
            nun = int(np.isnan(rT[msk]).sum() + np.isnan(rO[msk]).sum())
            print(f"{name:25s} {int(d['N']):3d} {int(d['M']):3d} {beta:5.3f}  {lab:7s} {np.abs(RT[msk]).max():9.3e}  {np.nanmax(rT[msk]):9.3e}    {np.abs(RO[msk]).max():9.3e}  {np.nanmax(rO[msk]):9.3e}     {np.abs(F['Ra'][msk]).max():8.2e}  {np.abs(F['RG'][msk]).max():8.2e}  {NT[msk].min():8.2e}  {NO[msk].min():8.2e}  {nun}")

if __name__ == '__main__':
    main(sys.argv[1:])
