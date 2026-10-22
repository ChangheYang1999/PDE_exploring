"""Lead 15:37Z: e(R) = int_{R<|X|<2R} |U|^2 dX / R^{4-4/beta} for R = 25..800 (full plane = 4 x quadrant), fitted slope.
Formal tail |U| ~ r^{1-1/beta} gives e(R) ~ R^{2/beta}; EN-R (pending audit) excludes e(R) -> 0."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW
for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-3, rmax=1e5, nr=5000); beta = B['beta']
    Rs = np.array([25, 50, 100, 200, 400, 800, 1600], float); es = []
    th = np.linspace(1e-4, np.pi / 2 - 1e-4, 240)
    for R0 in Rs:
        rg = np.linspace(R0, 2 * R0, 161)
        RR, TH = np.meshgrid(rg, th, indexing='ij')
        o = evalW(B, (RR * np.cos(TH)).ravel(), (RR * np.sin(TH)).ravel())
        U2 = (o['U1'] ** 2 + o['U2'] ** 2).reshape(RR.shape)
        I = 4 * np.trapz(np.trapz(U2 * RR, th, axis=1), rg)
        es.append(I / R0 ** (4 - 4 / beta))
    es = np.array(es); slope = np.polyfit(np.log(Rs), np.log(es), 1)[0]; loc = np.diff(np.log(es)) / np.diff(np.log(Rs))
    print(f"=== {path}: beta={beta}  e(R) for R = {Rs.astype(int).tolist()}:")
    print("   e(R) = " + " ".join(f"{v:.4e}" for v in es))
    print(f"   global slope {slope:+.3f}; local slopes {np.array2string(loc, precision=3)}; formal 2/beta = {2/beta:.3f}")
