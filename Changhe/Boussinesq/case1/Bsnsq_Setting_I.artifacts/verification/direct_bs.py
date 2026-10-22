"""Second, independent full-plane Biot-Savart evaluator (independent verifier): target-centred polar quadrature.
U1(X) = -(1/2pi) int_0^inf int_0^2pi sin(a) Omega(X + rho e_a) da drho,
U2(X) =  (1/2pi) int_0^inf int_0^2pi cos(a) Omega(X + rho e_a) da drho.
No symmetry is used (full plane), the kernel singularity is removed by the polar Jacobian.
Use on compactly supported (smoothly cut off) vorticity, or with an explicit tail correction.
"""
import numpy as np

def direct_velocity(Om, X0, rho_min=1e-9, rho_max=1e3, npan=160, npg=16, Na=512, extra_breaks=()):
    xg, wg = np.polynomial.legendre.leggauss(npg)
    br = np.unique(np.concatenate([np.geomspace(rho_min, rho_max, npan + 1), np.asarray(extra_breaks, float)]))
    br = br[(br >= rho_min) & (br <= rho_max)]
    sb = np.log(br)
    a = sb[:-1, None]; b = sb[1:, None]
    s = (0.5 * (b - a) * xg + 0.5 * (b + a)).ravel()
    w = (0.5 * (b - a) * wg).ravel()
    rho = np.exp(s); w = w * rho
    al = 2 * np.pi * np.arange(Na) / Na
    ca, sa = np.cos(al), np.sin(al)
    out = []
    for (x0, y0) in np.atleast_2d(X0):
        U1 = 0.0; U2 = 0.0
        for i0 in range(0, len(rho), 256):
            r = rho[i0:i0 + 256, None]
            v = Om(x0 + r * ca[None, :], y0 + r * sa[None, :])
            # trapezoid in angle (spectral for periodic integrand)
            I1 = v @ sa * (2 * np.pi / Na); I2 = v @ ca * (2 * np.pi / Na)
            U1 += -np.sum(w[i0:i0 + 256] * I1) / (2 * np.pi)
            U2 += np.sum(w[i0:i0 + 256] * I2) / (2 * np.pi)
        out.append((U1, U2))
    return np.array(out)
