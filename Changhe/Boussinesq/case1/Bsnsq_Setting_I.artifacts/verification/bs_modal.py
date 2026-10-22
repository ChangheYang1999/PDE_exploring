"""Independent full-plane Biot-Savart for odd-odd vorticity (independent verifier).

Convention of the task: -Lap Psi = Omega, U = (-Psi_y, Psi_x).
Omega odd in x and odd in y  =>  Omega(r,phi) = sum_{k>=1} w_k(r) sin(2 k phi).
Mode m = 2k: psi_k'' + psi_k'/r - m^2 psi_k / r^2 = -w_k, canonical solution
  psi_k(r) = (1/2m) [ r^-m int_0^r rho^(m+1) w_k + r^m int_r^inf rho^(1-m) w_k ],
the unique solution regular at 0 with psi_k = o(r^2) (no harmonic r^m sin(m phi) added).
With J1(r) = int_0^r (rho/r)^(m+1) w_k drho, J2(r) = int_r^inf (r/rho)^(m-1) w_k drho:
  psi_k' = (J2 - J1)/2,  psi_k / r = (J1 + J2)/(2m).
Radial integrals: composite Gauss-Legendre panels in s = log(rho), stable two-sided recursion;
angular projection: midpoint rule on (0, pi/2) (DST-II), exact for trig polynomials of degree < 2M.
Far tail beyond R_max: optional power-law model w_k(rho) = sum_j c_kj rho^(-alpha_j) integrated exactly.
"""
import numpy as np
from scipy.fft import dst

def gl_panels(breaks, npg):
    """Gauss-Legendre nodes/weights in s=log(rho) for panels between consecutive radii in `breaks`."""
    xg, wg = np.polynomial.legendre.leggauss(npg)
    sb = np.log(breaks)
    a = sb[:-1, None]; b = sb[1:, None]
    s = 0.5 * (b - a) * xg[None, :] + 0.5 * (b + a)
    w = 0.5 * (b - a) * wg[None, :]
    rho = np.exp(s)
    return rho, w * rho  # d rho = rho ds

def angular_modes(vals, K):
    """vals[..., M] samples at phi_j=(j+1/2) pi/(2M), j<M. Returns w_k, k=1..K, shape [..., K]."""
    M = vals.shape[-1]
    X = dst(vals, type=2, axis=-1)  # X_k' = 2 sum x_n sin(pi (k'+1)(2n+1)/(2M))
    return X[..., :K] / M

class ModalBS:
    def __init__(self, breaks, npg=16, M=256, K=None):
        self.breaks = np.asarray(breaks, float)
        self.npg = npg; self.M = M; self.K = K if K is not None else M // 2
        self.rho, self.w = gl_panels(self.breaks, npg)       # [P, npg]
        self.phi = (np.arange(M) + 0.5) * (np.pi / 2) / M

    def set_omega_modes(self, wk):
        """wk: [P, npg, K] modal coefficients at the quadrature radii."""
        self.wk = wk

    def set_omega_func(self, Om):
        r = self.rho[..., None]; ph = self.phi[None, None, :]
        vals = Om(r * np.cos(ph), r * np.sin(ph))
        self.wk = angular_modes(vals, self.K)
        return self.wk

    def solve(self, tail=None):
        """Compute J1, J2 at all panel breakpoints for each mode. tail: callable(k_array, R) -> J2 tail at R."""
        P = self.rho.shape[0]; K = self.K
        m = 2.0 * np.arange(1, K + 1)
        rb = self.breaks
        J1 = np.zeros((P + 1, K)); J2 = np.zeros((P + 1, K))
        # inner integral from 0 to breaks[0]: assume w_k ~ c rho^(m)... use leading power from first panel:
        # we simply require breaks[0] tiny; contribution int_0^r0 (rho/r0)^(m+1) w drho ~ r0 * w(r0) / (m+2+...)
        w0 = self.wk[0, 0, :]
        J1[0] = self.rho[0, 0] * w0 / (m + 2.0 + m)  # w_k ~ rho^m near 0 for smooth Omega -> exact for pure power
        for p in range(P):
            ratio = (rb[p] / rb[p + 1]) ** (m + 1)
            q = (self.rho[p][:, None] / rb[p + 1]) ** (m[None, :] + 1)
            J1[p + 1] = ratio * J1[p] + np.sum(self.w[p][:, None] * q * self.wk[p], axis=0)
        if tail is not None:
            J2[P] = tail(np.arange(1, K + 1), rb[P])
        for p in range(P - 1, -1, -1):
            ratio = (rb[p] / rb[p + 1]) ** (m - 1)
            q = (rb[p] / self.rho[p][:, None]) ** (m[None, :] - 1)
            J2[p] = ratio * J2[p + 1] + np.sum(self.w[p][:, None] * q * self.wk[p], axis=0)
        self.J1, self.J2, self.m = J1, J2, m
        return J1, J2

    def velocity(self, ib, phi):
        """Velocity at radius breaks[ib] (array of indices) and angles phi (same shape). Returns U1, U2, Psi."""
        ib = np.asarray(ib); phi = np.asarray(phi)
        J1 = self.J1[ib]; J2 = self.J2[ib]; m = self.m
        r = self.breaks[ib]
        dpsi = 0.5 * (J2 - J1)                 # psi_k'(r)
        psir = (J1 + J2) / (2 * m)             # psi_k(r)/r
        S = np.sin(m * phi[..., None]); C = np.cos(m * phi[..., None])
        Psi_r = np.sum(dpsi * S, -1)
        Psi_phi_over_r = np.sum(m * psir * C, -1)
        Psi = r * np.sum(psir * S, -1)
        cph, sph = np.cos(phi), np.sin(phi)
        Psi_x = cph * Psi_r - sph * Psi_phi_over_r
        Psi_y = sph * Psi_r + cph * Psi_phi_over_r
        return -Psi_y, Psi_x, Psi

    def strain0(self):
        """Psi_xy(0) = (1/2) int_0^inf w_1(rho)/rho drho = lim_{r->0} J2_1(r)/r ... computed as J2 of mode 1 at r0 / r0
        plus the (tiny) inner part."""
        # Psi_xy(0): psi_1(r) ~ (r^2/4) * int_0^inf w_1/rho ; Psi = psi_1 sin 2phi = 2 psi_1 xy / r^2  => Psi_xy = int w_1/rho / 2
        r0 = self.breaks[0]
        return 0.5 * self.J2[0, 0] / r0
