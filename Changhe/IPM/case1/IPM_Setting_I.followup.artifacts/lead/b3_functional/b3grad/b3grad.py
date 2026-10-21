"""Gradient of the axis B_3 estimator (original form of R10, lead tool b3core.b3_one, one configuration) with respect
to the input arrays w, w', w'' on the trial's axis grid, by central differences, one grid value at a time.
Use: the row (B_3[w] - target) in a least-squares fit needs grad_z B_3 = (d(w, w', w'')/dz)^T (gw, gwp, gwpp), i.e. a
vector-Jacobian product of the trial's axis-velocity map with the three arrays returned here.
The forward product (J_B3 v) is cheaper: central difference of b3_one along (dw, dw', dw'') = d(w, w', w'')/dz . v.
Caution: the estimator's finite part at 0 fits an even polynomial on [0.02, 0.35] x*; perturbations
that are not smooth on that window move the estimator without moving the true B_3. Grad entries inside the window are
therefore large and oscillatory; they are correct for smooth perturbations only. After any B_3-constrained fit,
recompute B_3 by the 32-variant median (b3core.b3_median) and by the verifier's estimator.
Usage: python3 b3grad.py traces.npz out.npz [xmax_over_xstar=1.02]   (traces.npz: x, w, wp, wpp_ode, c_l)"""
import sys, time
import numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'b3infl'))
import b3core


def b3grad(x, w, wp, wpp, cl, xmax_rel=1.02, rel=1e-6):
    B0, d = b3core.b3_one(x, w, wp, wpp, cl)
    xs = d['xs']
    idx = np.nonzero(x <= xmax_rel * xs)[0]
    arrs = [w.copy(), wp.copy(), wpp.copy()]
    grads = [np.zeros_like(w) for _ in range(3)]
    for k in range(3):
        a = arrs[k]
        sc = np.max(np.abs(a[idx]))
        for i in idx:
            h = rel * max(abs(a[i]), 1e-3 * sc)
            v = a[i]
            a[i] = v + h; bp = b3core.b3_one(x, *arrs, cl)[0]
            a[i] = v - h; bm = b3core.b3_one(x, *arrs, cl)[0]
            a[i] = v
            grads[k][i] = (bp - bm) / (2 * h)
    return B0, xs, grads


if __name__ == '__main__':
    x, w, wp, wpp, cl = b3core.load(sys.argv[1])
    xr = float(sys.argv[3]) if len(sys.argv) > 3 else 1.02
    t = time.time()
    B0, xs, (gw, gwp, gwpp) = b3grad(x, w, wp, wpp, cl, xr)
    # check against central differences along smooth directions
    chk = []
    for name, dw, dwp, dwpp in [
            ('x^3 e^-x', x ** 3 * np.exp(-x), (3 * x ** 2 - x ** 3) * np.exp(-x), (6 * x - 6 * x ** 2 + x ** 3) * np.exp(-x)),
            ('x sin(x/2)', x * np.sin(x / 2), np.sin(x / 2) + x * np.cos(x / 2) / 2, np.cos(x / 2) - x * np.sin(x / 2) / 4)]:
        for eps in (1e-5, 5e-6):
            bp = b3core.b3_one(x, w + eps * dw, wp + eps * dwp, wpp + eps * dwpp, cl)[0]
            bm = b3core.b3_one(x, w - eps * dw, wp - eps * dwp, wpp - eps * dwpp, cl)[0]
            fd = (bp - bm) / (2 * eps)
            lin = float(gw @ dw + gwp @ dwp + gwpp @ dwpp)
            chk.append((name, eps, fd, lin))
            print('%-12s eps %.0e  FD %.8e  grad.dir %.8e  rel diff %.2e' % (name, eps, fd, lin, abs(fd - lin) / abs(fd)), flush=True)
    np.savez(sys.argv[2], x=x, gw=gw, gwp=gwp, gwpp=gwpp, B3=B0, xs=xs, c_l=cl, seconds=time.time() - t)
    print('B3 %.8f  x* %.8f  done in %.0f s' % (B0, xs, time.time() - t))
