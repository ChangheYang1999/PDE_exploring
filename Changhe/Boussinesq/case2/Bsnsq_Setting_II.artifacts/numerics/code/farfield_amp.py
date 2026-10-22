"""Far-field amplitude and relative residual of saved states at large radii . For each state, evaluates on r = 1e2 .. 1e10 and
8 angles: A_a = a r^(2 + 2/beta_map) and A_G = G r^(2 + 1/beta_map) (the amplitudes of the basis's leading far-field powers, beta_map = stored
map exponent), the relative residuals R_a / a and R_G / G there, and the prediction 2 (beta_map - beta) / beta_map for R_a / a from the leading
dilation balance when beta differs from beta_map (derivation: with W ~ beta X and a ~ A r^(-p), p = 2 + 2/beta_map, the leading terms of
R_a = W.grad a + (2 w_1 + w_2 - beta + 2) a are (-beta p + 2 beta + 2) a = 2 (beta_map - beta) / beta_map a; for R_G / G the same algebra with
p_G = 2 + 1/beta_map and coefficient (w_1 + w_2 + 1) gives (-beta p_G + 2 beta + 1) G - 2 a - x a_x, i.e. (beta_map - beta) / beta_map G plus the
temperature forcing). The outermost collocation node of the N208 fits (Ne = 416 Chebyshev-Gauss nodes in 2t - 1) lies at t about 3.6e-6, r about 8e10, and the tail rows
sit at t = 1e-5 and 2e-5 (r = 1e10 and 2.5e9); radii beyond 1e11 are outside every row of the objective. Sampled values of fitted states; nothing about profiles. Usage: python3 code/farfield_amp.py state1.npz [state2.npz ...]"""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state

def main(paths):
    rs = np.array([1e2, 1e3, 1e4, 1e6, 1e8, 1e10, 1e12, 1e14, 1e16, 1e20, 1e30]); th = np.linspace(0.1, np.pi / 2 - 0.1, 8)
    for p in paths:
        d = load_state(p); beta = float(d['beta']); bm = float(d['beta_map']) if 'beta_map' in d else beta
        m, f = eval_state(d, rs, th)
        a = f['a'].cpu().numpy(); G = f['G'].cpu().numpy(); Ra = f['Ra'].cpu().numpy(); RG = f['RG'].cpu().numpy()
        pa = 2 + 2 / bm; pG = 2 + 1 / bm
        print(f"=== {p}: beta={beta:.6f} beta_map={bm:.6f}; predicted leading relative residual R_a/a -> 2(beta_map-beta)/beta_map = {2*(bm-beta)/bm:+.5f}, R_G/G -> (beta_map-beta)/beta_map = {(bm-beta)/bm:+.5f} (plus temperature forcing); angles phi = " + ", ".join(f"{t:.2f}" for t in th))
        for i, r in enumerate(rs):
            print(f"  r={r:8.0e} A_a = a r^{pa:.3f}: " + " ".join(f"{v:+.3e}" for v in a[i] * r ** pa))
            print(f"  {'':10s} A_G = G r^{pG:.3f}: " + " ".join(f"{v:+.3e}" for v in G[i] * r ** pG))
            print(f"  {'':10s} R_a / a           : " + " ".join(f"{v:+.3e}" for v in Ra[i] / a[i]))
            print(f"  {'':10s} R_G / G           : " + " ".join(f"{v:+.3e}" for v in RG[i] / G[i]))
        sys.stdout.flush()

if __name__ == '__main__':
    main(sys.argv[1:])
