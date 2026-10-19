"""Independent check of lead's explore/test_tail.py claim: for rho = x^2 (1+0.5y+0.3x)^2 (1+r^2)^{(p-4)/2}, p=1/2,
the lead's modal Biot-Savart gives c = psi_xy(0) -> 0.166666668 as t1 grows. Here c and psi_xx(0) are computed by
the I2 moment integrals c = (1/pi) int rho r^-3 sin3th, psi_xx(0) = (1/pi) int rho r^-3 cos3th (integrand ~ r^{p-2}),
with composite Gauss-Legendre in r out to 1e12 plus analytic tail, trapezoid (exact for trig polys) in theta."""
import numpy as np, sys
sys.path.insert(0, 'code')
from polar_inverse import gl_panels
p = 0.5
def moments(edges, q, nt):
    r, w = gl_panels(edges, q)[:2]
    th = 2*np.pi*np.arange(nt)/nt
    R, T = r[:, None], th[None, :]
    X, Y = R*np.cos(T), R*np.sin(T)
    rho = X**2*(1 + 0.5*Y + 0.3*X)**2*(1 + R**2)**((p - 4)/2)
    dth = 2*np.pi/nt
    c = np.sum(w[:, None]*dth*R*rho*np.sin(3*T)/R**3)/np.pi
    b = np.sum(w[:, None]*dth*R*rho*np.cos(3*T)/R**3)/np.pi
    # tail beyond Rmax: rho r^-2 ~ r^{p-2} A(th); A's sin3 moment: integrate leading term analytically
    Rm = edges[-1]
    Rt = np.array([[Rm]])
    rhoT = (np.cos(T))**2*(0.5*np.sin(T) + 0.3*np.cos(T))**2  # rho/r^p at r->inf
    ct = np.sum(dth*rhoT*np.sin(3*T))*Rm**(p - 1)/(1 - p)/np.pi
    bt = np.sum(dth*rhoT*np.cos(3*T))*Rm**(p - 1)/(1 - p)/np.pi
    return c, b, c + ct, b + bt
for q in (16, 32):
    edges = np.concatenate([[0.0], np.geomspace(1e-3, 0.5, 10), np.linspace(0.6, 10, 30), np.geomspace(11, 1e12, 60)])
    print(q, ['%.12f' % v for v in moments(edges, q, 64)])
