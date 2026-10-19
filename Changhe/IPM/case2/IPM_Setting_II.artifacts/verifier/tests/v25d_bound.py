"""V25(i)/lead 21:38Z item 1(d): numerical check of the elementary strain bound
    |c| <= (1/pi) int |rho| r^-3 |sin 3th| dX <= (4/pi)(H + C/(1 - gamma)),
H = sup_{r<=1} |rho|/r^2, C = sup_{r>=1} |rho|/r^gamma, on the benchmark rho_a = x^2 (1 + a y/<r>)^2 <r>^{-3/2}
(gamma = 1/2, c = a) and on asymmetric densities x^2 (1 + a y/<r> + e x/<r>)^2 <r>^{-3/2}, x^2 (1 + a y/<r>)^2 (1 + e x y/<r>^2) <r>^{-3/2}.
Quadrature: composite Gauss-Legendre in log r on [1e-8, 1e12] (tail beyond 1e12 omitted: relative 1e-6 in c), trapezoid in th."""
import numpy as np
xg, wg = np.polynomial.legendre.leggauss(16)
u = np.linspace(np.log(1e-8), np.log(1e12), 401)
a_, b_ = u[:-1, None], u[1:, None]
U = ((a_ + b_)/2 + (b_ - a_)/2*xg[None]).ravel(); WU = ((b_ - a_)/2*wg[None]).ravel()
r = np.exp(U); wr = WU*r
nt = 2048; th = 2*np.pi*np.arange(nt)/nt
R, T = r[:, None], th[None]
X, Y = R*np.cos(T), R*np.sin(T)
br = np.sqrt(1 + R*R)
gam = 0.5
def run(name, rho):
    s3 = np.sin(3*T)
    I = lambda F: np.sum(wr[:, None]*(2*np.pi/nt)*R*F)
    c = I(rho*s3/R**3)/np.pi; b = I(rho*np.cos(3*T)/R**3)/np.pi
    absI = I(np.abs(rho)*np.abs(s3)/R**3)/np.pi
    rr = np.abs(rho).max(1)
    H = (rr[r <= 1]/r[r <= 1]**2).max(); C = (rr[r >= 1]/r[r >= 1]**gam).max()
    bnd = 4/np.pi*(H + C/(1 - gam))
    print(f'{name}: c = {c:.10f}, b = {b:.3e}, (1/pi) int|rho||sin3th|r^-3 = {absI:.6f}, H = {H:.6f}, C = {C:.6f}, '
          f'bound (4/pi)(H + C/(1-gamma)) = {bnd:.6f}, holds: {abs(c) <= absI <= bnd}', flush=True)
for a in (0.5, 1.5, 3.0):
    run(f'rho_a a={a}', X**2*(1 + a*Y/br)**2*br**-1.5)
for a, e in ((1.5, 0.4), (3.0, 1.0)):
    run(f'asym1 a={a} e={e}', X**2*(1 + a*Y/br + e*X/br)**2*br**-1.5)
    run(f'asym2 a={a} e={e}', X**2*(1 + a*Y/br)**2*(1 + e*X*Y/br**2)*br**-1.5)
