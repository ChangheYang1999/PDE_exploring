# Heuristic evaluation of Lambda(alpha, b) = (1/2) int |nu_b| (2 d_Z)^alpha for b = pi/4,
# Z = real axis U {|X| = bc(Y)}, bc(Y)^2 = (a^2 - Y^2 + 2 sqrt(Y^4 + a^2 Y^2 + a^4))/3, a = 1/2.
# Integration: by oddness, Lambda = int_{H} |nu| (2d)^alpha (H = right half plane), polar grid about x.
import numpy as np, sys
from scipy.spatial import cKDTree
a = 0.5
def bc(Y):
    return np.sqrt((a*a - Y*Y + 2*np.sqrt(Y**4 + a*a*Y*Y + a**4))/3)
def K(z1, z2, b):
    return np.cos(2*np.arctan2(z2, z1) - 2*b)/(2*np.pi*(z1*z1 + z2*z2))
def nu(w1, w2, b):
    return K(0.5-w1, -w2, b) - K(-0.5-w1, -w2, b)
Y = np.concatenate([np.geomspace(1e-7, 1e4, 400000)])
pts = []
for sx in (1, -1):
    for sy in (1, -1):
        pts.append(np.stack([sx*bc(Y), sy*Y], 1))
P = np.concatenate(pts)
tree = cKDTree(P)
def dZ(w1, w2):
    d1, _ = tree.query(np.stack([w1.ravel(), w2.ravel()], 1), workers=1)
    d = np.minimum(d1.reshape(w1.shape), np.abs(w2))
    return d
def Lam(alphas, b=np.pi/4, Nth=2048, Nr=240, R=2000.0):
    gx, gw = np.polynomial.legendre.leggauss(8)
    out = np.zeros(len(alphas))
    # r from 1e-8 to R in log scale, polar about x; restrict to w1>0
    edges = np.linspace(np.log(1e-8), np.log(R), Nr+1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        t = 0.5*(hi-lo)*gx + 0.5*(hi+lo); wt = 0.5*(hi-lo)*gw
        for ti, wi in zip(t, wt):
            r = np.exp(ti)
            thmax = np.pi if r <= 0.5 else np.arccos(-0.5/r)
            h = 2*thmax/Nth
            th = -thmax + h*(np.arange(Nth)+0.5)
            w1 = 0.5 + r*np.cos(th); w2 = r*np.sin(th)
            m = np.abs(nu(w1, w2, b)); d = dZ(w1, w2)
            for j, al in enumerate(alphas):
                out[j] += wi*r*r*h*np.sum(m*(2*d)**al)
    return out
if __name__ == "__main__":
    alphas = [float(s) for s in sys.argv[1:]]
    L = Lam(alphas)
    for al, v in zip(alphas, L):
        print(f"alpha={al} Lambda={v:.5f} minus 2/(pi a)={v-2/(np.pi*al):.5f}", flush=True)
