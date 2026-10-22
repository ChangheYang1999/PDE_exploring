"""Least-squares fits of the misfit sequence RMS(N): (a) pure power c N^-p (log-log line), (b) power plus floor c N^-p + f (3 parameters,
nonlinear, floor constrained >= 0). With 4-5 points the floor is poorly determined; both fits and their residuals are printed so that
the reader can judge. Fitted misfits of least-squares states only; nothing here is a statement about profiles."""
import sys, numpy as np
from scipy.optimize import least_squares
def fit(N, F, label):
    N = np.array(N, float); F = np.array(F, float)
    A = np.vstack([np.ones_like(N), -np.log(N)]).T; coef, *_ = np.linalg.lstsq(A, np.log(F), rcond=None)
    c, p = np.exp(coef[0]), coef[1]; pred = c * N**-p
    print(f"{label}: N = {N.astype(int).tolist()}, RMS = {[f'{v:.3e}' for v in F]}")
    print(f"   (a) c N^-p: p = {p:.3f}, c = {c:.3e}; relative fit residuals {np.array2string((pred - F)/F, precision=3)}; local slopes {np.array2string(-np.diff(np.log(F))/np.diff(np.log(N)), precision=2)}")
    if len(N) >= 4:
        def res(q): return (q[0] * N**-q[1] + abs(q[2]) - F) / F
        best = None
        for f0 in [0.0, 0.3 * F[-1], 0.6 * F[-1], 0.9 * F[-1]]:
            r = least_squares(res, [c, p, f0]); 
            if best is None or r.cost < best.cost: best = r
        q = best.x; print(f"   (b) c N^-p + f: p = {q[1]:.3f}, c = {q[0]:.3e}, floor f = {abs(q[2]):.3e} ({abs(q[2])/F[-1]*100:.0f} percent of the last RMS); relative fit residuals {np.array2string(res(q), precision=3)}")
        print(f"       extrapolations (a)/(b) to N = 240, 300, 400: " + ", ".join(f"{n}: {c*n**-p:.3e}/{q[0]*n**-q[1]+abs(q[2]):.3e}" for n in (240, 300, 400)))
if __name__ == '__main__':
    fit([112, 144, 176, 208], [5.889e-3, 3.593e-3, 2.209e-3, 1.500e-3], "beta = 2, a0 = -1 (TL_B2m_N112, B2_m_gauss_N144, TL_B2m_N176, TL_B2m_N208)")
    fit([112, 176, 208], [5.867e-3, 2.711e-3, 1.883e-3], "beta = 2, a0 = +1 (TL_B2p_N112, N176, N208)")
    fit([112, 144, 176, 208], [3.115e-3, 2.479e-3, 1.938e-3, 1.547e-3], "control beta = 1.9431 (K3, K4, TL_K5, TL_K6)")
    fit([112, 144, 176, 208], [7.29e-3, 5.79e-3, 4.40e-3, 3.471e-3], "beta = 3, a0 = +1 (R4, R5, R6, TL_R7)")
    if len(sys.argv) > 2 and sys.argv[2] == 'neg': fit([112, 144, 176, 208, 240], [5.889e-3, 3.593e-3, 2.209e-3, 1.500e-3, float(sys.argv[1])], "beta = 2, a0 = -1 with N240")
    if len(sys.argv) > 2 and sys.argv[2] == 'pos': fit([112, 176, 208, 240], [5.867e-3, 2.711e-3, 1.883e-3, float(sys.argv[1])], "beta = 2, a0 = +1 with N240 (TL_B2p_N112, N176, N208, N240)")
