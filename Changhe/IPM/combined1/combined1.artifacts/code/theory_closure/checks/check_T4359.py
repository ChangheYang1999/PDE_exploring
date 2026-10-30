"""R1-037: independent check of c1-t4 T4-359 (research/annular_moment_adjustment/PROOF.md).

Part A (sympy, exact): the radial solution (5) of the mode-1 Poisson equation, the Cartesian derivatives of y/r^2,
the polar components of the exterior velocity, the endpoint expansion (4) and the scaling exponents of (2), (3), (6).
Part B (numpy, FLOAT): the velocity U[f] = (d_xy v, -d_xx v), Delta v = f, computed by direct quadrature of the
logarithmic kernel at points off the support 1 < r < 2 (no use of formula (5)); the potential itself against (5);
the moments; and the exterior residual change U[h_R].grad rho for an exact power-law rho against (4).
FLOAT values check the algebra; they prove nothing.
Usage (from artifacts/checks): python3 -B check_T4359.py (run_all.sh runs it too); about 7 s.
"""
import json
import time
from datetime import datetime, timezone

import numpy as np
import sympy as sp

t0 = time.time()
out = {'started_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}

# ---------------- Part A: exact algebra ----------------
r, s, th, x, y, gam, m, R = sp.symbols('r s theta x y gamma m R', positive=True)
eta = sp.Function('eta')
A = sp.Integral(s**2 * eta(s), (s, 0, r))
B = sp.Integral(eta(s), (s, r, sp.oo))
phi = -sp.Rational(1, 2) * (A / r + r * B)
ode = sp.diff(phi, r, 2) + sp.diff(phi, r) / r - phi / r**2 - eta(r)
out['A1_radial_ode_residual'] = str(sp.simplify(ode.doit()))

rr = sp.sqrt(x**2 + y**2)
g = y / rr**2
c3 = (x**3 - 3 * x * y**2) / rr**3   # cos 3 theta
s3 = (3 * x**2 * y - y**3) / rr**3   # sin 3 theta
out['A2_dxy_y_over_r2_plus_2cos3_over_r3'] = str(sp.simplify(sp.diff(g, x, y) + 2 * c3 / rr**3))
out['A2_dxx_y_over_r2_minus_2sin3_over_r3'] = str(sp.simplify(sp.diff(g, x, 2) - 2 * s3 / rr**3))
# exterior potential v = -y/(2 pi r^2): U = (v_xy, -v_xx)
v_ext = -g / (2 * sp.pi)
U1, U2 = sp.diff(v_ext, x, y), -sp.diff(v_ext, x, 2)
out['A3_U_ext_minus_formula'] = [str(sp.simplify(U1 - c3 / (sp.pi * rr**3))), str(sp.simplify(U2 - s3 / (sp.pi * rr**3)))]
# polar components of (cos 3t, sin 3t)
ur = sp.cos(3 * th) * sp.cos(th) + sp.sin(3 * th) * sp.sin(th)
ut = -sp.cos(3 * th) * sp.sin(th) + sp.sin(3 * th) * sp.cos(th)
out['A4_polar_components_minus_(cos2t,sin2t)'] = [str(sp.simplify(ur - sp.cos(2 * th))), str(sp.simplify(ut - sp.sin(2 * th)))]
# (4): U[h_R].grad rho for rho = r^gamma Theta(theta)
Th = sp.Function('Theta')
rho = r**gam * Th(th)
grad_r, grad_t = sp.diff(rho, r), sp.diff(rho, th) / r
lhs = m / (sp.pi * r**3) * (sp.cos(2 * th) * grad_r + sp.sin(2 * th) * grad_t)
P = gam * sp.cos(2 * th) * Th(th) + sp.sin(2 * th) * sp.diff(Th(th), th)
out['A5_endpoint_expansion_minus_(m/pi)r^(gamma-4)P'] = str(sp.simplify(lhs - m / sp.pi * r**(gam - 4) * P))
# scaling exponents: ||r^b D^k h_R|| = |m| R^(-3 - k + b + 1) A_(k,b)
k, b = sp.symbols('k b')
out['A6_exponent_r^b_D^k'] = str(sp.simplify(-3 - k + b + 1))
out['A6_exponents_E_w_terms'] = [str(-3 - 2 + sp.Rational(4, 5) + 1), str(-3 - 1 + 1), str(-3 + 1)]
out['A6_exponent_omega_D3'] = str(-3 - 3 + sp.Rational(4, 5) + 1)
out['A6_residual_exponents'] = {'(cX.grad-1)h': str(-3 + 1), 'u.grad h': str(sp.simplify(-3 - 1 + gam + 1)),
                                'U[h].grad rho': str(sp.simplify(-3 + gam - 1 + 1)), 'U[h].grad h': str(-3 - 4 + 1)}
q = sp.symbols('q')
out['A7_Hq_exponent'] = str(sp.simplify(-q - 3))
out['A7_Hq_over_X_exponent'] = str(sp.simplify(-q - 3 + 2))
# sharpw C_w of sharp_l2_audit section 4: max(1 + 32/25 + w1, 1 + w2/w1)
w1, w2 = 2**15, 2**20
out['A8_Cw'] = str(max(sp.Rational(1) + sp.Rational(32, 25) + w1, 1 + sp.Rational(w2, w1)))

# ---------------- Part B: FLOAT quadrature ----------------
def bump(t):
    o = np.zeros_like(t)
    i = (t > 1) & (t < 2)
    o[i] = np.exp(-1.0 / ((t[i] - 1) * (2 - t[i])))
    return o

xg, wg = np.polynomial.legendre.leggauss(600)
rq = 1.5 + 0.5 * xg
wr = 0.5 * wg
nphi = 4096
pq = 2 * np.pi * np.arange(nphi) / nphi
wp = 2 * np.pi / nphi
norm = np.pi * np.sum(wr * rq**2 * bump(rq))
etaq = bump(rq) / norm                      # pi int r^2 eta = 1
RR, PP = np.meshgrid(rq, pq, indexing='ij')
WW = (wr * rq)[:, None] * wp                # polar measure
F = (etaq[:, None] * np.sin(PP))
Yx, Yy = RR * np.cos(PP), RR * np.sin(PP)
out['B1_moments_int_y_f_int_x_f_int_f'] = [float(np.sum(WW * F * Yy)), float(np.sum(WW * F * Yx)), float(np.sum(WW * F))]


def U_quad(X1, X2, Rs=1.0, mm=1.0):
    # U[h_R](X) by the log kernel; h_R(Y) = mm Rs^-3 f(Y/Rs); off the support only
    Zx, Zy = X1 - Rs * Yx, X2 - Rs * Yy
    Z2 = Zx**2 + Zy**2
    Kxy = -2 * Zx * Zy / Z2**2 / (2 * np.pi)
    Kxx = (Zy**2 - Zx**2) / Z2**2 / (2 * np.pi)
    dens = mm * Rs**-3 * F
    meas = WW * Rs**2
    return float(np.sum(meas * dens * Kxy)), float(-np.sum(meas * dens * Kxx))


def v_quad(X1, X2):
    Zx, Zy = X1 - Yx, X2 - Yy
    return float(np.sum(WW * F * np.log(np.sqrt(Zx**2 + Zy**2))) / (2 * np.pi))


err_in, err_out = 0.0, 0.0
for rad in (0.2, 0.5, 0.8, 0.9):
    for al in np.linspace(0.1, 2 * np.pi - 0.1, 7):
        u = U_quad(rad * np.cos(al), rad * np.sin(al))
        err_in = max(err_in, abs(u[0]), abs(u[1]))
for rad in (2.2, 3.0, 5.0, 11.0):
    for al in np.linspace(0.1, 2 * np.pi - 0.1, 7):
        u = U_quad(rad * np.cos(al), rad * np.sin(al))
        ex = (np.cos(3 * al) / (np.pi * rad**3), np.sin(3 * al) / (np.pi * rad**3))
        err_out = max(err_out, abs(u[0] - ex[0]) * rad**3, abs(u[1] - ex[1]) * rad**3)
out['B2_max_|U[f]|_on_r<1'] = err_in
out['B3_max_r^3|U[f]-(cos3a,sin3a)/(pi r^3)|_on_r>2'] = err_out
B0 = 0.5 * np.sum(wg * etaq)  # int_1^2 eta
ev = []
for rad, al in ((0.5, 0.7), (0.9, 2.0), (3.0, 0.4), (7.0, 1.1)):
    vq = v_quad(rad * np.cos(al), rad * np.sin(al))
    v5 = (-0.5 * rad * B0 if rad < 1 else -1.0 / (2 * np.pi * rad)) * np.sin(al)
    ev.append(abs(vq - v5))
out['B4_max_|v_log_kernel-v_(5)|'] = max(ev)
# scaling of U at R = 4, m = 3: exterior value independent of R; interior zero
u_ext = U_quad(13.0 * np.cos(0.3), 13.0 * np.sin(0.3), Rs=4.0, mm=3.0)
out['B5_R4_m3_ext_r^3*pi/m*U_vs_(cos0.9,sin0.9)'] = [u_ext[0] * 13.0**3 * np.pi / 3, u_ext[1] * 13.0**3 * np.pi / 3,
                                                     float(np.cos(0.9)), float(np.sin(0.9))]
u_int = U_quad(3.5 * np.cos(1.3), 3.5 * np.sin(1.3), Rs=4.0, mm=3.0)
out['B5_R4_m3_interior_r=3.5_|U|'] = float(np.hypot(*u_int))
# (4) for rho = r^gamma Theta, Theta = sin t + 0.3 sin 3t, gamma = 0.4, R = 4, m = 3, at r > 8
gm = 0.4
e4 = 0.0
for rad, al in ((9.0, 0.5), (12.0, 1.9), (20.0, 4.0)):
    ux, uy = U_quad(rad * np.cos(al), rad * np.sin(al), Rs=4.0, mm=3.0)
    Tv, Td = np.sin(al) + 0.3 * np.sin(3 * al), np.cos(al) + 0.9 * np.cos(3 * al)
    gr, gt = gm * rad**(gm - 1) * Tv, rad**(gm - 1) * Td
    gx, gy = gr * np.cos(al) - gt * np.sin(al), gr * np.sin(al) + gt * np.cos(al)
    lhs_v = ux * gx + uy * gy
    Pv = gm * np.cos(2 * al) * Tv + np.sin(2 * al) * Td
    e4 = max(e4, abs(lhs_v - 3 / np.pi * rad**(gm - 4) * Pv) / rad**(gm - 4))
out['B6_max_rel_|U[h_R].grad rho-(m/pi)r^(g-4)P|/r^(g-4)'] = e4
out['finished_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
out['seconds'] = round(time.time() - t0, 2)
print(json.dumps(out, indent=1))
