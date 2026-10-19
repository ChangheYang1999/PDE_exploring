"""V151 (p2): with a linear term at the centre the inner boundary terms of the moment identity do not vanish."""
import sympy as sp
r, th, eps, a1, a2 = sp.symbols('r theta epsilon a1 a2', real=True)
f = a1*eps*sp.cos(th) + a2*eps*sp.sin(th)               # linear part of f on r = eps
h = eps**-2*sp.sin(2*th); nx = -sp.cos(th)              # n = -e_r on the inner circle
dens = sp.simplify(sp.integrate(f*h*nx*eps, (th, 0, 2*sp.pi)))
mom = sp.simplify(sp.integrate((a1*sp.cos(th) + a2*sp.sin(th))*sp.sin(3*th), (th, 0, 2*sp.pi)))
gphi = (-3*sp.sin(4*th), 3*sp.cos(4*th))                # r^4 grad phi
quad_freqs = [sp.cos(2*th), sp.sin(2*th), sp.Integer(1)]
qmean = [sp.integrate(qf*g, (th, 0, 2*sp.pi)) for qf in quad_freqs for g in gphi]
print('inner density term oint f h n_x ds =', dens, '(nonzero for a2 != 0):', dens != 0)
print('angular mean of (linear part) * sin 3th =', mom, '; angular means of (quadratic) * r^4 grad phi =', qmean)
print('grad phi = r^-4 (-3 sin 4th, 3 cos 4th):', sp.simplify(sp.diff(r**-3*sp.sin(3*th), r)*sp.cos(th) - sp.diff(r**-3*sp.sin(3*th), th)*sp.sin(th)/r + 3*r**-4*sp.sin(4*th)) == 0)
