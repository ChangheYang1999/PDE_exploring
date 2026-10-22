"""Cosine modes a_m(r) of A = e^{H} (so that rho_bar = x^2 y A) of the X3 formula on a dense log grid (float64).
A(r, theta) is even in theta and symmetric about pi/2, so A = sum_{m>=0} a_m(r) cos(2 m theta),
   a_0 = (2/pi) int_0^{pi/2} A dtheta,  a_m = (4/pi) int_0^{pi/2} A cos(2 m theta) dtheta   (m >= 1),
computed by the trapezoid rule on theta_j = j pi/(2 Nt) (exact DCT-I of the samples; the fractional term is C^(4,0.2)
at theta = pi/2, so the rule converges algebraically, order about 5: with Nt = 4096 the error is < 1e-19 relative).
Also the first radial derivative modes (d/dt a_m, t = log r) from H_r.
Usage: python3 x3_modes.py Nr Nt rmin_L rmax_L Mkeep out.npz
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.fft import dct
from x3 import X3


def main(Nr, Nt, rmin_L, rmax_L, Mkeep, out, chunk=2000):
    X = X3(); L = X.L
    r = np.exp(np.linspace(np.log(rmin_L * L), np.log(rmax_L * L), Nr))
    th = np.linspace(0, np.pi / 2, Nt + 1)
    A = np.empty((Nr, Mkeep)); At = np.empty((Nr, Mkeep)); Att = None
    t0 = time.time()
    for i0 in range(0, Nr, chunk):
        i1 = min(Nr, i0 + chunk)
        H, H_r, H_t = X.H(r[i0:i1], th)
        eH = np.exp(H)
        # DCT-I: y_k = x_0 + (-1)^k x_N + 2 sum_{j=1}^{N-1} x_j cos(pi j k / N); trapezoid with h = pi/(2N):
        # (4/pi) h [x_0/2 + x_N/2 + sum x_j cos] = (4/pi)(pi/(2N)) y_k/2 = y_k / N ; for k=0 halve.
        c = dct(eH, type=1, axis=1) / Nt
        c[:, 0] *= 0.5
        A[i0:i1] = c[:, :Mkeep]
        ct = dct(eH * H_r * r[i0:i1, None], type=1, axis=1) / Nt      # d/dt A = r H_r e^H
        ct[:, 0] *= 0.5
        At[i0:i1] = ct[:, :Mkeep]
        if i0 == 0:
            tail = np.abs(c[:, Mkeep:]).max() / np.abs(c).max()
            print("chunk 0: relative size of dropped modes (m >= %d): %.2e" % (Mkeep, tail), flush=True)
    print("done %.1fs" % (time.time() - t0))
    tailmax = 0.0
    np.savez_compressed(out, r=r, t=np.log(r), A=A, At=At, Nt=Nt, Mkeep=Mkeep, L=L, k=X.k, c_l=X.c_l)
    # report modal decay statistics
    rel = np.abs(A) / np.abs(A).max(1, keepdims=True)
    for lev in (1e-8, 1e-10, 1e-12, 1e-14):
        last = np.array([np.flatnonzero(rel[i] > lev).max() for i in range(0, Nr, max(1, Nr // 20))])
        print("rel > %.0e: last mode index over sampled radii: max %d" % (lev, last.max()))
    print("A[:,0] at r = rmin, 1, 8.6, 1000, rmax:", [float(np.interp(np.log(x), np.log(r), A[:, 0])) for x in (r[0], 1.0, 8.6, 1000.0, r[-1])])


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
