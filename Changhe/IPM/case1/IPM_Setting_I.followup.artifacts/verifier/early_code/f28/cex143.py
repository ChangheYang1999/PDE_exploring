# fred28 (1.43): Q(r) = r^b1 sin(r^-k1), b1 = alpha (k1 + 1), (1 - alpha)(k1 + 1) > q, q + alpha > 1.
# Checks: (i) the Hoelder quotient |Q(r) - Q(t)|/|r - t|^alpha stays bounded on a fine sample near 0;
# (ii) int_eps^1 r^(q-1) |Q'| dr grows without bound as eps -> 0 (power law eps^(-(-(p+1))/... ) predicted);
# (iii) the signed improper integral int_eps^1 r^(q-1) Q' dr converges.
import numpy as np
A = 10.150725; q = 4/A; alpha = 0.7; k1 = 1.0; b1 = alpha*(k1 + 1)
assert (1 - alpha)*(k1 + 1) > q and q + alpha > 1
Q = lambda r: r**b1*np.sin(r**(-k1))
dQ = lambda r: b1*r**(b1 - 1)*np.sin(r**(-k1)) - k1*r**(b1 - k1 - 1)*np.cos(r**(-k1))
# (i) Hoelder quotient on random pairs in (0, 0.1), including very close pairs
rng = np.random.default_rng(1)
r = 10**rng.uniform(-6, -1, 400000); t = r*(1 + 10**rng.uniform(-9, 0.5, 400000)*rng.choice([-1, 1], 400000))
t = np.abs(t)
hq = np.abs(Q(r) - Q(t))/np.abs(r - t)**alpha
print('Hoelder quotient sup over %d pairs in (1e-6, 0.3): %.4f' % (len(r), hq.max()))
# (ii), (iii) in the variable z = r^(-k1): r^(q-1) Q'(r) dr integrated on [z_0, Z] by Gauss-Legendre per half period
x, w = np.polynomial.legendre.leggauss(40)
def integrals(eps):
    Z = eps**(-k1); edges = np.arange(1.0, Z + np.pi/2, np.pi/2); edges[-1] = min(edges[-1], Z)
    lo, hi = edges[:-1], edges[1:]
    zz = (0.5*(hi - lo)[:, None]*x[None, :] + 0.5*(hi + lo)[:, None]); ww = 0.5*(hi - lo)[:, None]*w[None, :]
    rr = zz**(-1/k1); jac = (1/k1)*zz**(-1/k1 - 1)
    g = rr**(q - 1)*dQ(rr)*jac
    return float(np.sum(ww*np.abs(g))), float(np.sum(ww*g))
p = q + b1 - k1 - 2
print('power of the oscillatory part p = %.4f (< -1 required); predicted growth of the absolute integral ~ eps^(%.4f)' % (p, p + 1))
for e in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]:
    ab, sg = integrals(e)
    print('eps = %.0e  int |r^(q-1) Q\'| = %.6e   (times eps^%.4f = %.4e)   signed int = %.10f' % (e, ab, -(p + 1), ab*e**(-(p+1)), sg))
