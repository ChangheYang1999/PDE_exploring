"""Lead's request (Note 6, item 1): sup of the alpha-Hoelder ratio of the projection cusp
   g(u) = (1/2) [ |u|^alpha + sign(u1 u2) (2|u1 u2|/|u|)^alpha ],  u in R^2,
i.e. S(alpha) = sup_{p != q} |g(p) - g(q)| / |p - q|^alpha.  By homogeneity (g is alpha-homogeneous) fix |p| = 1:
S = sup over (theta_p, q in R^2).  Method: coarse grid over theta_p in [0, pi/2] (symmetry), q = r e^{i phi} with r in a log grid,
then local refinement by Nelder-Mead from the best grid points.  Float; purely exploratory (to compare with the lead's script)."""
import numpy as np, sys
from scipy.optimize import minimize
def g(x, y, alpha):
    r = np.hypot(x, y)
    with np.errstate(divide='ignore', invalid='ignore'):
        v = 0.5*(r**alpha + np.sign(x*y)*(2*np.abs(x*y)/np.where(r > 0, r, 1))**alpha)
    return np.where(r > 0, v, 0.0)
def ratio(theta, r, phi, alpha):
    px, py = np.cos(theta), np.sin(theta); qx, qy = r*np.cos(phi), r*np.sin(phi)
    d = np.hypot(px - qx, py - qy)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(d > 1e-300, np.abs(g(px, py, alpha) - g(qx, qy, alpha))/d**alpha, 0.0)
def sup_ratio(alpha, nth=241, nr=161, nphi=720):
    th = np.linspace(0, np.pi/2, nth); r = np.exp(np.linspace(np.log(1e-3), np.log(1e3), nr)); phi = np.linspace(0, 2*np.pi, nphi, endpoint=False)
    TH, R, PH = np.meshgrid(th, r, phi, indexing='ij')
    V = ratio(TH, R, PH, alpha)
    idx = np.argsort(V.ravel())[-40:]
    best = V.ravel()[idx[-1]]; bestx = None
    for i in idx:
        t0, r0, p0 = TH.ravel()[i], R.ravel()[i], PH.ravel()[i]
        res = minimize(lambda v: -ratio(v[0], np.exp(v[1]), v[2], alpha), [t0, np.log(r0), p0], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-13, maxiter=4000))
        if -res.fun > best: best = -res.fun; bestx = res.x
    return best, bestx
if __name__ == "__main__":
    for alpha in [0.02, 0.05, 0.1, 0.25, 0.5, 0.75]:
        s, x = sup_ratio(alpha)
        if x is not None:
            print(f"alpha={alpha}: sup ratio = {s:.8f}  (excess {s-1:.3e}, excess/alpha^2 {(s-1)/alpha**2:.4f})  at theta_p={x[0]:.5f}, |q|={np.exp(x[1]):.5f}, phi_q={x[2]:.5f}", flush=True)
        else:
            print(f"alpha={alpha}: sup ratio = {s:.8f} (grid)", flush=True)
