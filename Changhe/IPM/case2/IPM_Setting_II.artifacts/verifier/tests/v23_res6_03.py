"""V23(i): referee result 6 03 algebra: identity (8) coefficient, residues (10), (11), coefficient sign."""
import sympy as sp
r, th, m, l, c, r0 = sp.symbols('r theta m l c r0', positive=True)
x, y = r*sp.cos(th), r*sp.sin(th)
# (8): (1+2l) int y eta rho = bdry - int rho eta V_2 - int y rho V.grad eta, V_2 = l y + W_2, V.grad eta = -m l eta + W.grad eta
eta = r**-m
XgradEta = sp.simplify(r*sp.diff(eta, r))          # X.grad eta = r d_r eta
print('X.grad eta / eta =', sp.simplify(XgradEta/eta))
# collect coefficient of int y eta rho on the right after moving: int eta rho W_2 = bdry - K int y eta rho - int y rho W.grad eta
K = (1 + 2*l) + l - m*l      # from -(1+2l) - l (from V_2) + m l (from V.grad eta)
print('K - (1 + 3l - ml) =', sp.simplify(K - (1 + 3*l - m*l)), '; K/l at l = 1/p:', sp.simplify((K/l).subs(l, 1/sp.Symbol('p'))))
# residues: P = c/2 r^2 cos 2th, W = (-c x, c y): |W|^2 = c^2 r^2, W.X = -c r^2 cos 2th
W1, W2 = -c*x, c*y
print('|W|^2 =', sp.simplify(W1**2 + W2**2), '; W.X =', sp.simplify(W1*x + W2*y), '; P =', sp.simplify(c/2*(x**2 - y**2)))
E = sp.integrate(sp.integrate(r**-m*c**2*r**2*r, (th, 0, 2*sp.pi)), (r, 0, r0), conds='none')
Pt = sp.integrate(sp.integrate(-m*r**(-m-2)*(c/2*r**2*sp.cos(2*th))*(-c*r**2*sp.cos(2*th))*r, (th, 0, 2*sp.pi)), (r, 0, r0), conds='none')
print('(4-m) E_inner =', sp.simplify((4 - m)*E), ' -> m=4:', sp.limit(sp.simplify((4-m)*E), m, 4))
print('(4-m) P_inner =', sp.simplify((4 - m)*Pt), ' -> m=4:', sp.limit(sp.simplify((4-m)*Pt), m, 4))
