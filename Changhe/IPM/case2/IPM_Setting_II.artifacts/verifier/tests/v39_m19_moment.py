"""V39 (referee result 12 item 3, exact shear): for rho = |x|^g, W = (0, -|x|^g), phi = r^-3 sin 3th, l = 1/g:
Q_eps = -3 eps^(2g-2)/(2-2g) I, B_eps = -eps^(2g-2) (J - I)/2, I = int |cos|^(2g) cos 4th, J = int |cos|^(2g) cos 2th.
Claim (own derivation): Q_eps + B_eps = (l-1) int_{r>eps} rho phi = 0 for every eps, C_g = -3 I/(2-2g) > 0; at g = 1 B = -pi/4.
Numerical quadrature of the 2D integrals on an annulus as an independent check of the closed forms."""
import numpy as np
from scipy import integrate
for g in (0.3, 0.5, 0.8, 1.0):
    I = integrate.quad(lambda t: abs(np.cos(t))**(2*g)*np.cos(4*t), 0, 2*np.pi, limit=400)[0]
    J = integrate.quad(lambda t: abs(np.cos(t))**(2*g)*np.cos(2*t), 0, 2*np.pi, limit=400)[0]
    eps = 0.01
    # direct B_eps from its definition
    l = 1/g
    Bd = eps**-2*integrate.quad(lambda t: (eps*abs(np.cos(t)))**g*(l*eps - (eps*abs(np.cos(t)))**g*np.sin(t))*np.sin(3*t), 0, 2*np.pi, limit=400)[0]
    Bf = -eps**(2*g - 2)*(J - I)/2
    if g < 1:
        # direct Q_eps: int_{r>eps} rho W.grad phi, grad_y phi = 3 r^-4 cos 4th; radial integral to R with exact tail
        Rm = 1e3
        rad = integrate.quad(lambda r: r**(2*g - 3), eps, Rm)[0] + Rm**(2*g - 2)/(2 - 2*g)
        ang = integrate.quad(lambda t: -abs(np.cos(t))**(2*g)*3*np.cos(4*t), 0, 2*np.pi, limit=400)[0]
        Qd = rad*ang
        Qf = -3*eps**(2*g - 2)/(2 - 2*g)*I
        print(f"g={g}: I={I:.10f} J={J:.10f} I/J={I/J:.10f} (g-1)/(g+2)={(g-1)/(g+2):.10f} Q_direct={Qd:.8e} Q_formula={Qf:.8e} "
              f"B_direct={Bd:.8e} B_formula={Bf:.8e} Q+B={Qd+Bd:.3e} C_g={-3*I/(2-2*g):.6f}")
    else:
        print(f"g=1: B_direct={Bd:.10f} -pi/4={-np.pi/4:.10f}")
