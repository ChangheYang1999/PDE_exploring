# Heuristic evaluation of J(beta) and Lambda_0(beta) = -(1+log 2)/pi + J(beta),
# J = int_{H \ B_{1/2}(x)} |nu| + int_{B_{1/2}(x)} (|nu| - |K(x-.)|),
# nu = K_b(x-w) - K_b(y-w), x=(1/2,0), y=(-1/2,0), K_b(z)=cos(2 arg z - 2b)/(2 pi |z|^2), H={w1>0}.
import numpy as np, sys
def K(z1, z2, b):
    r2 = z1*z1 + z2*z2
    th = np.arctan2(z2, z1)
    return np.cos(2*th - 2*b)/(2*np.pi*r2)
def nu(w1, w2, b):
    return K(0.5-w1, -w2, b) - K(-0.5-w1, -w2, b)
def J(b, Nth=8192, Nr=400, R=4000.0):
    # outer: polar about x, r in [1/2, R], theta in allowed arc r cos th > -1/2
    gx, gw = np.polynomial.legendre.leggauss(40)
    # pieces in t=log r
    edges = np.linspace(np.log(0.5), np.log(R), Nr+1)
    tot = 0.0
    for a, c in zip(edges[:-1], edges[1:]):
        t = 0.5*(c-a)*gx + 0.5*(c+a); wt = 0.5*(c-a)*gw
        for ti, wi in zip(t, wt):
            r = np.exp(ti)
            thmax = np.pi if r <= 0.5 else np.arccos(-0.5/r)
            h = 2*thmax/Nth
            th = -thmax + h*(np.arange(Nth)+0.5)
            w1 = 0.5 + r*np.cos(th); w2 = r*np.sin(th)
            tot += wi*r*r*h*np.sum(np.abs(nu(w1, w2, b)))
    # tail beyond R: |nu| ~ c/|w|^3; estimate by last-shell scaling
    # inner: B_{1/2}(x)
    edges = np.linspace(0.0, 0.5, 200+1)
    inn = 0.0
    th = 2*np.pi*(np.arange(Nth)+0.5)/Nth; h = 2*np.pi/Nth
    for a, c in zip(edges[:-1], edges[1:]):
        rr = 0.5*(c-a)*gx + 0.5*(c+a); wr = 0.5*(c-a)*gw
        for r, wi in zip(rr, wr):
            w1 = 0.5 + r*np.cos(th); w2 = r*np.sin(th)
            kx = K(0.5-w1, -w2, b)
            inn += wi*r*h*np.sum(np.abs(nu(w1, w2, b)) - np.abs(kx))
    return tot, inn
if __name__ == "__main__":
    for b in [float(s) for s in sys.argv[1:]]:
        o, i = J(b)
        Jb = o + i
        print(f"beta={b:.4f} outer={o:.7f} inner={i:.7f} J={Jb:.7f} Lambda0={-(1+np.log(2))/np.pi + Jb:.7f}", flush=True)
