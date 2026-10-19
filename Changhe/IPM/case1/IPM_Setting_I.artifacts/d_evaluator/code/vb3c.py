"""Verifier's corrected finite-part estimator for the w-only B_3 (verifier), replacing the endpoint treatment of
vb3w.closed_form (whose degree-5 extrapolation of the noisy factor next to x* gave a spurious +0.3 natural units).
Input: a callable q(x) with -F3/(wH) = x^(1-p3) q(x) on (0, x*) (physical x), the exponent beta = 2/A and x*.
In u = x/x*:  B_nat = f.p. int_0^1 u^(1-p3) Phi(u) du, Phi(u) = q(x* u) = (1-u)^(beta-1) phi(u), phi smooth.
  [0, uc]: Phi fitted by an even polynomial in u on sample points u in [u_lo, uc] (u_lo outside the origin layer),
           exact finite part of the polynomial;
  [uc, ue]: Gauss-Legendre of the data;
  [ue, 1]: phi fitted by a polynomial of degree dE on [uf, ux] (ux < 1 excludes the points next to x*, where the pole
           regularization of the w-only traces is not smooth), integrated with Gauss-Jacobi weight (1-u)^(beta-1).
"""
import numpy as np
from scipy.special import roots_jacobi


def fp_clean(qfun, xs, p3, beta, u_lo=0.04, uc=0.3, K=6, ue=0.8, uf=0.6, ux=0.97, dE=6, npts=600, nq=400):
    a = 1 - p3
    # near 0
    uu = np.linspace(u_lo, uc, npts)
    Ph = qfun(xs * uu)
    M = np.stack([uu ** (2 * k) for k in range(K + 1)], 1)
    ck, *_ = np.linalg.lstsq(M, Ph, rcond=None)
    fit0 = float(np.abs(M @ ck - Ph).max() / np.abs(Ph).max())
    fp0 = float(sum(ck[k] * uc ** (2 * k + 2 - p3) / (2 * k + 2 - p3) for k in range(K + 1)))
    # middle
    gx, gw = np.polynomial.legendre.leggauss(nq)
    um = uc + (ue - uc) * (gx + 1) / 2
    mid = float(np.sum(gw * um ** a * qfun(xs * um)) * (ue - uc) / 2)
    # end
    ub = np.linspace(uf, ux, npts)
    ph = qfun(xs * ub) * (1 - ub) ** (1 - beta)
    pc = np.polynomial.polynomial.polyfit(ub - 1, ph, dE)
    fitE = float(np.abs(np.polynomial.polynomial.polyval(ub - 1, pc) - ph).max() / np.abs(ph).max())
    tj, wj = roots_jacobi(80, beta - 1, 0.0)            # weight (1-t)^(beta-1) on [-1, 1]
    ue_ = ue + (1 - ue) * (tj + 1) / 2
    endp = float(((1 - ue) / 2) ** beta * np.sum(wj * ue_ ** a * np.polynomial.polynomial.polyval(ue_ - 1, pc)))
    return dict(B=fp0 + mid + endp, fp0=fp0, mid=mid, endp=endp, fit0=fit0, fitE=fitE, phi1=float(pc[0]))
