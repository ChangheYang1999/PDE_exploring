"""V104: numerical checks of the closed forms in specification v4.10 M28 (referee result 19): (b) int_0^pi cos^2 cos 2th = pi/4 and the core velocity
U_core(0) = (0, Sigma R^2/16) by direct quadrature of the subtracted Biot-Savart gradient; (d) K_g = int_0^pi |cos|^g sin 3th / pi
= 2(3g+1)/(pi(g+1)(g+3)); (i) C_g = int_0^2pi |cos|^(2g) sin th sin 3th = (6g/(g+2)) B(3/2, g+1/2), C_1 = pi/4; (i) the inner-flux
identity N_eps + B_eps = pi (l-1) c_>eps on a smooth test density with W computed by quadrature; (a) the circulation bound on a
model field. CPU, scipy."""
import math, numpy as np
from scipy import integrate, special
pi = math.pi
print('(b) int cos^2 cos2th 0..pi =', integrate.quad(lambda t: math.cos(t)**2*math.cos(2*t), 0, pi)[0], 'pi/4 =', pi/4)
# U_core(0): W(0) = (1/2pi) int (-sin2th, cos2th) rho / r^2 dX for rho = G+- x^2 on r < R (half-discs)
Gp, Gm, R = 1.7, 0.6, 0.8
w1 = integrate.dblquad(lambda th, r: (-math.sin(2*th))*(Gp if math.sin(th) > 0 else Gm)*(r*math.cos(th))**2/r**2*r/(2*pi), 0, R, 0, 2*pi, epsabs=1e-12)[0]
w2 = integrate.dblquad(lambda th, r: (math.cos(2*th))*(Gp if math.sin(th) > 0 else Gm)*(r*math.cos(th))**2/r**2*r/(2*pi), 0, R, 0, 2*pi, epsabs=1e-12)[0]
print('(b) W(0) quadrature =', (round(w1, 12), w2), ' Sigma R^2/16 =', (Gp + Gm)*R**2/16)
for g in (0.35, 0.6, 1.0, 1.5, 2.0):
    I = integrate.quad(lambda t: abs(math.cos(t))**g*math.sin(3*t), 0, pi, limit=200)[0]
    Kg = 2*(3*g + 1)/(pi*(g + 1)*(g + 3))
    C = integrate.quad(lambda t: abs(math.cos(t))**(2*g)*math.sin(t)*math.sin(3*t), 0, 2*pi, limit=400)[0]
    Cf = 6*g/(g + 2)*special.beta(1.5, g + 0.5)
    print('g %.2f  K_g quad %.12f formula %.12f | C_g quad %.12f formula %.12f' % (g, I/pi, Kg, C, Cf))
print('K_2 =', 14/(15*pi), ' C_1 formula', 6/3*special.beta(1.5, 1.5), 'pi/4', pi/4)
# (i) direct N_eps for the layer rho = H|x|^g, W = (0, -H|x|^g), phi = r^-3 sin 3th: d_y phi = 3 r^-4 cos 4th, so
# N_eps = -3 H^2 eps^(2g-2)/(2-2g) int_0^2pi |cos|^(2g) cos 4th; compare with +H^2 C_g eps^(2g-2) (H = 1)
for g in (0.35, 0.6, 0.9):
    J = integrate.quad(lambda t: abs(math.cos(t))**(2*g)*math.cos(4*t), 0, 2*pi, limit=400)[0]
    print('g %.2f  N_eps/eps^(2g-2) direct %.12f   C_g %.12f' % (g, -3*J/(2 - 2*g), 6*g/(g + 2)*special.beta(1.5, g + 0.5)))
