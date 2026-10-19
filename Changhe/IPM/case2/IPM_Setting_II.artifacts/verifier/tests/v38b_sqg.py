"""v38b: checks for referee result 11 05-comparison (critical SQG, theta = Re(t + i x)^p / cos(pi p/2)).
Lambda and R_1 on growing data are evaluated by their singular-integral forms (symmetrized), not as
Fourier multipliers: |D|f(x) = (1/pi) int_0^inf [2f(x) - f(x+s) - f(x-s)]/s^2 ds,
Hf(x) = (1/pi) int_0^inf [f(x-s) - f(x+s)]/s ds (symbol -i sgn k), which converge for growth |x|^p, p<1."""
import numpy as np
from scipy.integrate import quad

res = []
def rep(ok, name, extra=""):
    res.append(bool(ok)); print(("PASS" if ok else "FAIL"), name, extra)

def theta(x, t, p): return ((t + 1j*x)**p).real/np.cos(np.pi*p/2)
def u2(x, t, p): return -((t + 1j*x)**p).imag/np.cos(np.pi*p/2)
def dtheta_dt(x, t, p): return (p*(t + 1j*x)**(p - 1)).real/np.cos(np.pi*p/2)

for p in [0.3, 0.75]:
    # trace
    xs = np.linspace(-3, 3, 13)
    err = max(abs(theta(xx, 0.0, p) - abs(xx)**p) for xx in xs)
    rep(err < 1e-12, f"05 trace Re(ix)^p/cos = |x|^p (p={p})", f"{err:.1e}")
    for (x0, t0) in [(0.9, 0.7), (-1.7, 0.2), (0.0, 1.3)]:
        # Poisson representation
        f = lambda z: t0*abs(z)**p/(t0**2 + (x0 - z)**2)/np.pi
        pts = sorted(set([0.0, x0]))
        I = 0.0
        edges = [-np.inf] + pts + [np.inf]
        for a_, b_ in zip(edges[:-1], edges[1:]):
            I += quad(f, a_, b_, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
        rep(abs(I - theta(x0, t0, p)) < 1e-8, f"05 Poisson integral = formula at (x,t)=({x0},{t0}), p={p}", f"{I:.10f} vs {theta(x0, t0, p):.10f}")
        # theta_t + |D_1| theta = 0
        g = lambda s: (2*theta(x0, t0, p) - theta(x0 + s, t0, p) - theta(x0 - s, t0, p))/s**2/np.pi
        LD = quad(g, 0, 1, limit=400, epsabs=1e-13)[0] + quad(g, 1, np.inf, limit=400, epsabs=1e-13)[0]
        rep(abs(LD + dtheta_dt(x0, t0, p)) < 1e-7, f"05 theta_t + |D|theta = 0 at ({x0},{t0}), p={p}", f"{LD:.10f} vs {-dtheta_dt(x0, t0, p):.10f}")
        # R_1 theta = Hilbert transform (symbol -i sgn k) equals -Im(t+ix)^p/cos; anchored value at 0 is 0
        hfun = lambda s: (theta(x0 - s, t0, p) - theta(x0 + s, t0, p))/s/np.pi
        HT = quad(hfun, 0, 1, limit=400, epsabs=1e-13)[0] + quad(hfun, 1, np.inf, limit=400, epsabs=1e-13)[0]
        rep(abs(HT - u2(x0, t0, p)) < 1e-7, f"05 R_1 theta = -Im(t+ix)^p/cos at ({x0},{t0}), p={p}", f"{HT:.10f} vs {u2(x0, t0, p):.10f}")
    # similarity theta = t^p Theta(x/t)
    t1, t2, xx = 0.4, 1.9, 0.77
    lhs = theta(xx*t2/t1, t2, p); rhs = (t2/t1)**p*theta(xx, t1, p)
    rep(abs(lhs - rhs) < 1e-12, f"05 similarity t^p Theta(x/t) (p={p})")
    rep(theta(0.0, 0.5, p) > 0, f"05 theta(0,t) = t^p/cos(pi p/2) > 0 (p={p})")
# sanity of the Hilbert convention on cos x -> sin x
hf = lambda s: (np.cos(0.4 - s) - np.cos(0.4 + s))/s/np.pi
val = quad(hf, 0, 200, limit=2000)[0]
rep(abs(val - np.sin(0.4)) < 2e-3, "05 Hilbert convention H cos = sin (symbol -i sgn k)", f"{val:.5f} vs {np.sin(0.4):.5f}")
print("SUMMARY: %d/%d PASS" % (sum(res), len(res)))
