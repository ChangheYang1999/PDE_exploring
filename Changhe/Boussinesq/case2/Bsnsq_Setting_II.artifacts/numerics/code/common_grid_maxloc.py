"""Maximizer of |R_Theta| and |R_Omega| on the common 10000-point grid of code/common_grid_resid.py by sub-band (10-20, 20-30, 30-100, >= 100),
with its location (sampled maxima of fitted states; same format as the original run log runs/common_grid_ann96_maxloc.log).
Usage: python3 code/common_grid_maxloc.py state1.npz [state2.npz ...]"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def main(paths):
    k = np.arange(200); R = np.geomspace(0.02, 2000, 200) * (1 + 1e-3 * np.sin(k)); T = (np.arange(50) + 0.37) * (np.pi / 2) / 50
    print("maximizer of |R_Theta| on the common grid by sub-region (sampled)")
    for p in paths:
        d = load_state(p); name = p.split('/')[-1]
        m, f = eval_state(d, R, T)
        Ra = f['Ra'].cpu().numpy(); RG = f['RG'].cpu().numpy()
        X = R[:, None] * np.cos(T)[None, :]; Y = R[:, None] * np.sin(T)[None, :]; RR = np.hypot(X, Y); TH = np.arctan2(Y, X)
        RT = np.abs(X**2 * Y * Ra); RO = np.abs(X * Y * RG)
        for lo, hi in ((10, 20), (20, 30), (30, 100), (100, 1e9)):
            msk = (RR >= lo) & (RR < hi)
            iT = np.argmax(np.where(msk, RT, -1)); iO = np.argmax(np.where(msk, RO, -1))
            print(f"{name:28s} {lo:g}-{hi:g}  max|R_Theta|={RT.flat[iT]:8.3f} at r={RR.flat[iT]:.2f} theta={TH.flat[iT]:.3f} | max|R_Omega|={RO.flat[iO]:7.3f} at r={RR.flat[iO]:.2f}")

if __name__ == '__main__':
    main(sys.argv[1:])
