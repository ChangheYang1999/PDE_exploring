"""beta = 2 diagnostics: map of |W|/(beta r) near the x-axis stagnation point P and along the
closed quadrant; local minima of |W| along circles around P (trace of an approximate stagnation curve); Theta, Omega there."""
import sys, numpy as np
sys.path.insert(0, 'code')
from lm_solve import load_state
from charcheck import build, evalW, find_xstar
for path in sys.argv[1:]:
    d = load_state(path); B = build(d, rmin=1e-3, rmax=1e4, nr=4000); beta = B['beta']
    xs, lam = find_xstar(B)
    print(f"=== {path}: beta={beta} x*={xs:.5f} W1'(x*)={lam:.5f} (beta+2={beta+2})")
    # W2 along the y-axis and W1 along the x-axis
    for r in [1, 5, 10, 20, 30, 50, 80, 120, 200]:
        o1 = evalW(B, np.array([float(r)]), np.array([1e-9])); o2 = evalW(B, np.array([1e-9]), np.array([float(r)]))
        print(f"   r={r:5.0f}: W1/x(x-axis)={o1['W1'][0]/r:+.4f}   W2/y(y-axis)={o2['W2'][0]/r:+.4f}")
    # circles around P: minimum of |W| / (beta * rho) over angle, for radii rho
    print("  circles around P=(x*,0): angle (deg from +x) of the minimal |W| and its value, plus Theta, Omega there")
    for rho in [0.2, 0.5, 1, 2, 4, 8, 12, 16]:
        ang = np.linspace(0.5, 179.5, 359) * np.pi / 180
        X = xs + rho * np.cos(ang); Y = rho * np.sin(ang)
        ok = (X > 1e-6) & (Y > 1e-6)
        o = evalW(B, X[ok], Y[ok], need_fields=True)
        mag = np.hypot(o['W1'], o['W2']) / (beta * rho)
        i = np.argmin(mag)
        # also second local minimum if any
        loc = [j for j in range(1, len(mag) - 1) if mag[j] < mag[j - 1] and mag[j] < mag[j + 1]]
        locs = ", ".join(f"{ang[ok][j]*180/np.pi:5.1f}deg:{mag[j]:.2e}" for j in sorted(loc, key=lambda j: mag[j])[:3])
        print(f"   rho={rho:5.1f}: min |W|/(beta rho) = {mag[i]:.3e} at {ang[ok][i]*180/np.pi:6.1f} deg, Theta={o['Theta'][i]:+.3e} Omega={o['Omega'][i]:+.3e} | local minima: {locs}")
    # grid search for interior points with tiny |W| (r < 100)
    r = np.geomspace(0.3, 100, 200); th = np.linspace(0.01, np.pi / 2 - 0.01, 120)
    R, TH = np.meshgrid(r, th, indexing='ij'); X, Y = R * np.cos(TH), R * np.sin(TH)
    o = evalW(B, X.ravel(), Y.ravel(), need_fields=True)
    mag = (np.hypot(o['W1'], o['W2']) / (beta * R.ravel())).reshape(R.shape)
    idx = np.argsort(mag.ravel())[:8]
    print("  smallest |W|/(beta r) on the interior grid (r<100):")
    for k in idx:
        i, j = divmod(k, R.shape[1])
        print(f"   ({X[i,j]:8.3f},{Y[i,j]:8.3f}) r={R[i,j]:7.3f}: |W|/(beta r)={mag[i,j]:.3e} Theta={o['Theta'][k]:+.3e} Omega={o['Omega'][k]:+.3e}")
