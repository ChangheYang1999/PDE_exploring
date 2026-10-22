"""Verifier: second formula for c = psi_xy(0): integrating by parts in x,
c = (4/pi) int_0^oo ds/s^2 int_0^{pi/2} rho(s,th) sin(3 th) dth   (uses rho only, not rho_x)."""
import numpy as np
from x3rho import Trial
from x3modes import q_panels, nodes_from_edges, u_of_q, theta_grid
T = Trial()
for npt, nth in ((12, 512), (16, 1024)):
    e = q_panels(T, q_min=1e-14, tau_min=1e-14)
    qn, wn = nodes_from_edges(e, npt)
    u, dudq = u_of_q(T, qn); r = u * T.L
    th = theta_grid(nth)
    acc = np.zeros(len(r))
    for i0 in range(0, len(r), 512):
        F = T.fields(r[i0:i0 + 512], th)
        acc[i0:i0 + 512] = (F['rho'] * np.sin(3 * th)[None, :]).sum(1) * (np.pi / 2 / nth)
    integrand = (4 / np.pi) * acc / r ** 2 * T.L * dudq     # ds = L du
    c = np.sum(wn * integrand) + integrand[0] * 1e-14
    print('IBP formula npt=%d nth=%d: c = %.15f, c_l = %.15f, c_l - stored = %+.4e' % (npt, nth, c, (1 + c) / 3, (1 + c) / 3 - T.cl_stored))
