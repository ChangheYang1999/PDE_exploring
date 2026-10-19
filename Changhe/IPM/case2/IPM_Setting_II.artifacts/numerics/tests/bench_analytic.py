"""Analytic benchmarks (referee note) for the family
   rho_a = x^2 (1 + a y/sqrt(1+r^2))^2 (1+r^2)^{-3/4}   (growth r^{1/2}, exterior expansion in integer powers of r^-2)
 (1) c[rho_a] = psi_xy(0) = a                      (2) (1/pi) int_{r>R} rho_a sin3th r^-3 dX = a (1+R^2)^{-1/4}
 (3) psi_xyy(0) = (a^2-1)/4                        (4) one frozen transport step: zeta = x + (a^2-1)/(8a+2) xy + O(r^3)
 (5) identity int f W[rho].grad(r^-3 sin3th) dX = pi (c[rho]-1/2) c[f] for the frozen output f = zeta^2 (quadrature)
"""
import sys, math; sys.path.insert(0, 'code')
import numpy as np, torch
from torch.func import jacfwd
from ipm2polar import Disc, bary_weights
from zetasolve import weight_zeta, lin_lstsq
torch.set_default_dtype(torch.float64)
dev = 'cuda'

def gl_xi(d, nq=400):
    """Gauss-Legendre nodes in xi on [0, xi_max] and the interpolation matrix from the Radau nodes."""
    xg, wg = np.polynomial.legendre.leggauss(nq)
    xi = 0.5 * d.xi_max * (xg + 1.0); w = 0.5 * d.xi_max * wg
    xx = 2.0 * xi / d.xi_max - 1.0
    wb = bary_weights(d.x)
    T = wb[None, :] / (xx[:, None] - d.x[None, :]); P = T / T.sum(axis=1, keepdims=True)
    return (torch.tensor(xi, device=dev), torch.tensor(w, device=dev), torch.tensor(P, device=dev, dtype=torch.complex128))

def moment_c_interior(d, rho_m):
    """c_int(R) = -2 int_0^R Im rho_3(r) r^-2 dr  (= (1/pi) int_{r<R} rho sin3th r^-3 dX), integrating the interpolant."""
    xi, w, P = gl_xi(d)
    q3 = rho_m[3] / d.rk[3]                         # smooth in xi
    q3g = P @ q3
    s = d.L ** 2 * (torch.exp(xi) - 1.0); r = torch.sqrt(s)
    # Im rho_3 r^-2 dr = Im(r^3 q3) r^-2 dr = Im(q3) r dr = Im(q3) ds/2 = Im(q3) L^2 e^xi dxi / 2
    return float(-2.0 * torch.sum(w * (q3g.imag) * d.L ** 2 * torch.exp(xi) / 2.0))

def _main():
  for (Nr, Nth, R) in ((40, 24, 100.0), (64, 32, 300.0), (96, 48, 1000.0), (64, 32, 3000.0)):
      for a in (1.5, 3.0):
          p_in = 0.5
          d = Disc(Nr, Nth, R, K=2, tail='power2', tail_exps=(p_in, p_in - 2.0), device=dev)
          th = d.theta_p[:, None]; r = d.r[None, :]
          X, Y = r * torch.cos(th), r * torch.sin(th)
          z0 = X * (1 + a * Y / (1 + r ** 2) ** 0.5) * (1 + r ** 2) ** ((p_in / 2 - 1) / 2)
          qz = d.to_modes(z0) / d.rk
          cl_dummy = torch.tensor(0.5 + a, device=dev)
          out = d.zeta_residual_modes(qz, cl_dummy, return_all=True)
          U0, pxx, pxy, pyy = d.taylor_psi(out['p'])
          c_num = float(pxy)
          # (2) exterior moment
          c_int = moment_c_interior(d, out['rho_m'])
          c_ext_exact = a * (1 + R ** 2) ** (-0.25)
          # (3) psi_xyy(0) = 4 Re p1s(0) - 12 Re p3(0)   (K=2 -> kappa_1 = 1, kappa_3 = 3)
          p = out['p']
          p1s = (p[1] @ d.ell0dc) / d.L ** 2
          p3 = p[3] @ d.ell0c
          psi_xyy = float(4 * p1s.real - 12 * p3.real)
          psi_xxy = float(-4 * p1s.imag - 12 * p3.imag)
          print("Nr=%3d Nth=%2d R=%6g a=%.1f | (1) c=%.6f (exact %.1f) | (2) c_int(R)=%.6f + ext_exact %.6f = %.6f | (3) psi_xyy0=%.6f (exact %.4f) psi_xxy0=%.1e psi_yy0=%.1e" %
                (Nr, Nth, R, a, c_num, a, c_int, c_ext_exact, c_int + c_ext_exact, psi_xyy, (a * a - 1) / 4, psi_xxy, float(pyy)), flush=True)
          # (4) one frozen transport step with V = (1/2 + c) X + W[rho_a]
          cl_new = 0.5 + c_num
          Ur, Ut = out['Ur'], out['Ut']
          wz = weight_zeta(d, 1.0 / cl_new); res_w = 1.0 / wz ** 2
          def Flin(vz):
              qq = d.unpack(torch.cat([vz, torch.zeros(1, device=dev)]))[0]
              z_m, dz_m, tz_m = d.rho_modes(qq)
              z = d.to_phys(z_m); dz = d.to_phys(dz_m); tz = d.to_phys(tz_m)
              Rz = cl_new * d.r[None, :] * dz + Ur * dz + Ut * tz - 0.5 * z
              Rz_m = d.to_modes(Rz) * res_w[None, :]
              zz0, zx, zy, _, _, _ = d.taylor_rho(qq)
              return torch.cat([Rz_m[0].real, Rz_m[1:].real.reshape(-1), Rz_m[1:].imag.reshape(-1), torch.stack([zz0, zx - 1.0, zy])])
          vz = d.pack(qz, cl_dummy)[:-1]
          L = jacfwd(Flin)(vz); b0 = Flin(torch.zeros_like(vz))
          sol, lres = lin_lstsq(L, -b0)
          qz1 = d.unpack(torch.cat([sol, torch.zeros(1, device=dev)]))[0]
          xy_coef = float(-4 * (qz1[2] @ d.ell0c).imag)
          q_out = 1.0 / cl_new
          # output moment with frozen-consistent tail exponents (q, q + p_in - 1)
          d.tail_exps = (q_out, q_out + p_in - 1.0)
          out1 = d.zeta_residual_modes(qz1, torch.tensor(cl_new, device=dev), return_all=True)
          c1 = float(d.taylor_psi(out1['p'])[2])
          c1_int = moment_c_interior(d, out1['rho_m'])
          # (5) identity: int f W[rho_in].grad(phi) dX = pi (c_in - 1/2) c[f], phi = r^-3 sin 3th
          # W[rho_in].grad phi = Ur phi_r + (Ut/r) phi_th ; phi_r = -3 r^-4 sin3th, phi_th = 3 r^-3 cos3th
          f = out1['rho']                                     # on padded grid [Np, Nr]
          thp = d.theta_p[:, None]; rr = d.r[None, :]
          Wgp = Ur * (-3 * rr ** -4 * torch.sin(3 * thp)) + Ut / rr * (3 * rr ** -3 * torch.cos(3 * thp))
          integrand_theta_mean = (f * Wgp).mean(dim=0) * 2 * math.pi        # int over theta -> function of r
          # integrate over r dr using the interpolant in xi
          xi, w, P = gl_xi(d)
          gi = (P.real @ integrand_theta_mean)
          s = d.L ** 2 * (torch.exp(xi) - 1.0)
          I5 = float(torch.sum(w * gi * d.L ** 2 * torch.exp(xi) / 2.0))     # r dr = ds/2
          d.tail_exps = (p_in, p_in - 2.0)
          print("      (4) frozen step: lres=%.1e  xy coef of zeta1 = %.6f (exact %.6f) | c1 = %.5f (interior part %.5f) q_out=%.3f | (5) I=%.5f vs pi(c-1/2)c1=%.5f" %
                (lres, xy_coef, (a * a - 1) / (8 * a + 2), c1, c1_int, q_out, I5, math.pi * (c_num - 0.5) * c1), flush=True)


if __name__ == '__main__':
    _main()
