"""V39b (referee result 12 results/03-moments, Section 1): numerical check of the cusp strain identity
    -d_x W1(0) = (1/pi) lim int_{r>eps} rho r^-3 sin 3th,   d_y W1(0) = (1/pi) lim int_{r>eps} rho r^-3 cos 3th
for a test density with a CURVED zero line (not a profile; this checks the kernel/IBP/differentiability steps):
    rho = |xi|^g exp(-r^2),  xi = x + mu x y + kap y^2   (normalized jet xi = x + O(r^2)).
(A) absolutely convergent potential form  D_j = int d_1 d_j G(-Y) d_y rho(Y) dY, G = log|Z|/(2 pi);
(B) renormalized moments with the subtraction 1_{r<1}|x|^g;
(C) finite differences [W1(h e_j) - W1(0)]/h with W1(X) = (1/2pi) int cos(phi) int_0^inf d_y rho(X - s e_phi) ds dphi
    (ray form of W1 = (d_1 G) * d_y rho; no singular kernel left), including the direction e_2 tangent to the cusp line.
Run: OMP_NUM_THREADS=1 python3 tests/v39b_strain_num.py"""
import sys
import time
import numpy as np
from scipy import integrate, optimize

MU, KAP = 0.4, 0.5
LIM = 400


def make(g):
    def xi(x, y):
        return x + MU*x*y + KAP*y**2

    def rho(x, y):
        return abs(xi(x, y))**g*np.exp(-(x*x + y*y))

    def s(x, y):  # d_y rho
        q = xi(x, y)
        e = np.exp(-(x*x + y*y))
        if q == 0.0:
            return 0.0
        return e*(g*np.sign(q)*abs(q)**(g - 1)*(MU*x + 2*KAP*y) - 2*y*abs(q)**g)
    return xi, rho, s


def ray_coeffs(X1, X2, c, sn):
    # xi(X - t e) = C0 - B1 t + A2 t^2
    C0 = X1 + MU*X1*X2 + KAP*X2**2
    B1 = c + MU*(c*X2 + sn*X1) + 2*KAP*sn*X2
    A2 = MU*c*sn + KAP*sn**2
    return A2, B1, C0


def ray_roots(X1, X2, phi, tmax):
    c, sn = np.cos(phi), np.sin(phi)
    A2, B1, C0 = ray_coeffs(X1, X2, c, sn)
    rts = []
    if abs(A2) < 1e-14:
        if abs(B1) > 1e-14:
            rts = [C0/B1]
    else:
        D = B1*B1 - 4*A2*C0
        if D >= 0:
            sq = np.sqrt(D)
            rts = [(B1 - sq)/(2*A2), (B1 + sq)/(2*A2)]
    return sorted(t for t in rts if 1e-15 < t < tmax)


def W1(X1, X2, s, tmax=9.0):
    def inner(phi):
        c, sn = np.cos(phi), np.sin(phi)
        pts = [0.0] + ray_roots(X1, X2, phi, tmax) + [tmax]
        tot = 0.0
        for a, b in zip(pts[:-1], pts[1:]):
            if b - a > 0:
                tot += integrate.quad(lambda t: s(X1 - t*c, X2 - t*sn), a, b, limit=LIM, epsabs=1e-13, epsrel=1e-12)[0]
        return np.cos(phi)*tot
    # breakpoints in phi: tangency (discriminant zero) and A2 = 0 directions
    grid = np.linspace(0, 2*np.pi, 20001)

    def disc(phi):
        A2, B1, C0 = ray_coeffs(X1, X2, np.cos(phi), np.sin(phi))
        return B1*B1 - 4*A2*C0

    def a2(phi):
        return ray_coeffs(X1, X2, np.cos(phi), np.sin(phi))[0]
    bps = {0.0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi}
    for fn in (disc, a2):
        v = np.array([fn(p) for p in grid])
        for i in np.nonzero(np.sign(v[:-1]) != np.sign(v[1:]))[0]:
            bps.add(optimize.brentq(fn, grid[i], grid[i + 1], xtol=1e-15))
    bps = sorted(bps)
    tot = 0.0
    for a, b in zip(bps[:-1], bps[1:]):
        if b - a > 1e-14:
            tot += integrate.quad(inner, a, b, limit=LIM, epsabs=1e-12, epsrel=1e-11)[0]
    return tot/(2*np.pi)


def polar_int(F, g, rmax=9.0, extra_r=()):
    """int_0^{2pi} int_0^rmax F(r, th) dr dth with breakpoints at the ray root of xi and at extra_r."""
    def inner(th):
        c, sn = np.cos(th), np.sin(th)
        A2 = MU*c*sn + KAP*sn**2
        pts = {0.0, rmax} | {r for r in extra_r if r < rmax}
        if abs(A2) > 1e-15:
            rr = -c/A2
            if 0 < rr < rmax:
                pts.add(rr)
        pts = sorted(pts)
        return sum(integrate.quad(lambda r: F(r, th), a, b, limit=LIM, epsabs=1e-13, epsrel=1e-12)[0]
                   for a, b in zip(pts[:-1], pts[1:]))
    bps = [0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]
    return sum(integrate.quad(inner, a, b, limit=LIM, epsabs=1e-12, epsrel=1e-11)[0] for a, b in zip(bps[:-1], bps[1:]))


def main(g):
    xi, rho, s = make(g)
    t0 = time.time()
    # (A) potential form
    DA_x = polar_int(lambda r, th: -np.cos(2*th)/(2*np.pi)*s(r*np.cos(th), r*np.sin(th))/r, g)
    DA_y = polar_int(lambda r, th: -np.sin(2*th)/(2*np.pi)*s(r*np.cos(th), r*np.sin(th))/r, g)
    # (B) renormalized moments
    def mom(trig):
        return polar_int(lambda r, th: (rho(r*np.cos(th), r*np.sin(th)) - (abs(r*np.cos(th))**g if r < 1 else 0.0))
                         * trig(3*th)/r**2, g, extra_r=(1.0,))/np.pi
    Ms, Mc = mom(np.sin), mom(np.cos)
    print(f'g={g}: (A) D_x = {DA_x:.10f}  D_y = {DA_y:.10f}   (B) -M_sin/pi = {-Ms:.10f}  M_cos/pi = {Mc:.10f}'
          f'   [{time.time() - t0:.0f}s]')
    okA = abs(DA_x + Ms) < 1e-7 and abs(DA_y - Mc) < 1e-7
    print(('PASS' if okA else 'FAIL'), f'g={g}: IBP identity (A) = (B), diffs {DA_x + Ms:.2e}, {DA_y - Mc:.2e}')
    # (C) finite differences
    W0 = W1(0.0, 0.0, s)
    hs = [3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]
    out = {}
    for j, (ex, ey) in enumerate(((1, 0), (0, 1))):
        ref = DA_x if j == 0 else DA_y
        errs = []
        for h in hs:
            d = (W1(h*ex, h*ey, s) - W0)/h
            errs.append(abs(d - ref))
            print(f'   dir e{j+1} h={h:.0e}: FD = {d:.8f}  |FD - (A)| = {errs[-1]:.3e}')
        # observed decay rate of the error between the last two decades
        rate = np.log(errs[1]/errs[-1])/np.log(hs[1]/hs[-1]) if errs[-1] > 0 else np.inf
        out[j] = (errs, rate)
        ok = errs[-1] < 0.05*max(abs(ref), 1e-3) and errs[-1] < errs[0]
        print(('PASS' if ok else 'FAIL'), f'g={g}: FD derivative along e{j+1} converges to (A); error rate ~ h^{rate:.2f}'
              f' (expected about h^{g} or faster)')
    print(f'   W1(0) = {W0:.10f}   total {time.time() - t0:.0f}s')
    sys.stdout.flush()


if __name__ == '__main__':
    for g in (0.4, 0.75):
        main(g)
