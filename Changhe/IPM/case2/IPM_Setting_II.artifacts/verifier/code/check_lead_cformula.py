"""Accurate I2 moments for the lead's general test density (explore/test_vel.py):
rho = (x^2+0.7xy-0.4y^2+0.9x^2y+0.5y^3-0.3x^3) exp(-((x-0.3)^2+(y+0.2)^2)/2).
Lead reports c: FFT 0.0960932, formula 0.0960920, polar 0.0960918737, I2 quadrature 0.0960919552.
Also compares psi_xy(0), psi_xx(0) from my Cartesian Ewald inverse (code/bs_cartesian.py) by finite differences of U."""
import numpy as np, sys
sys.path.insert(0, 'code')
from polar_inverse import gl_panels, PolarGrid
def rhof(X, Y):
    return (X**2 + 0.7*X*Y - 0.4*Y**2 + 0.9*X**2*Y + 0.5*Y**3 - 0.3*X**3)*np.exp(-((X - 0.3)**2 + (Y + 0.2)**2)/2)
for q, nt in ((16, 128), (32, 256)):
    edges = np.concatenate([[0.0], np.geomspace(1e-4, 0.5, 12), np.linspace(0.6, 14, 60)])
    r, w = gl_panels(edges, q)[:2]
    th = 2*np.pi*np.arange(nt)/nt
    R, T = r[:, None], th[None, :]
    rho = rhof(R*np.cos(T), R*np.sin(T))
    c = np.sum(w[:, None]*(2*np.pi/nt)*rho*np.sin(3*T)/R**2)/np.pi
    b = np.sum(w[:, None]*(2*np.pi/nt)*rho*np.cos(3*T)/R**2)/np.pi
    print(f'moments q={q} nt={nt}: c = {c:.13f}, psi_xx(0) = {b:.13f}')
# my polar inverse: grad U at 0 via U - U(0) at small radius (U1 = -psi_y, U2 = psi_x)
edges = np.concatenate([[0.0], np.geomspace(1e-4, 0.5, 12), np.linspace(0.6, 14, 60)])
G = PolarGrid(edges, 24, 256)
W1, W2 = G.velocity(rhof(G.X, G.Y))
i = 3  # small radius node
rr = G.R[i, 0]
# psi_xy = d_x U1 ... U1 = -psi_y -> d_x U1 = -psi_xy; U2 = psi_x -> d_x U2 = psi_xx
m1 = np.fft.fft(W1[i])/G.nt; m2 = np.fft.fft(W2[i])/G.nt
# linear part: W ~ rr*(A cos + B sin) => A = d_x W, B = d_y W ; mode 1 coefficient = rr*(A - iB)/2
dxW1 = 2*np.real(m1[1])/rr; dxW2 = 2*np.real(m2[1])/rr
print(f'polar inverse at r={rr:.2e}: psi_xy(0) ~ {-dxW1:.10f}, psi_xx(0) ~ {dxW2:.10f}')
