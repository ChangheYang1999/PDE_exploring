"""Verifier: c = psi_xy(0) = (1/2) int_0^oo f_1(s)/s ds for the X3 trial (canonical, exact formula extended to all r).
Gauss-Legendre in q on knot panels + graded endpoint panels; angular midpoint rule. Convergence study in all parameters."""
import numpy as np, time
from x3rho import Trial
from x3modes import q_panels, nodes_from_edges, u_of_q, fmodes

T = Trial()
print('stored c_l = %.16g, stored c = 3c_l-1 = %.16g' % (T.cl_stored, 3 * T.cl_stored - 1))
res = {}
for npt in (8, 12, 16):
    for nth in (256, 512, 1024):
        for (q_min, tau_min) in ((1e-10, 1e-10), (1e-14, 1e-14)):
            e = q_panels(T, q_min=q_min, tau_min=tau_min)
            qn, wn = nodes_from_edges(e, npt)
            u, dudq = u_of_q(T, qn)
            r = u * T.L
            t0 = time.time()
            f1 = fmodes(T, r, nth, 1)[:, 0]
            integrand = 0.5 * f1 * dudq / u
            c = np.sum(wn * integrand)
            # endpoint pieces: [0,q_min]: integrand ~ const (f_1 ~ s^2... f_1/s ds ~ s ds -> in q: ~ const dq); [1-tau_min,1]
            end0 = abs(integrand[0]) * q_min
            end1 = abs(integrand[-1]) * tau_min
            cl = (1 + c) / 3
            print('npt=%2d nth=%4d qmin=%g taumin=%g nodes=%d: c=%.15f  c_l=(1+c)/3=%.15f  c_l-stored=%+.3e  ends~%.1e,%.1e  (%.1fs)'
                  % (npt, nth, q_min, tau_min, len(qn), c, cl, cl - T.cl_stored, end0, end1, time.time() - t0), flush=True)
