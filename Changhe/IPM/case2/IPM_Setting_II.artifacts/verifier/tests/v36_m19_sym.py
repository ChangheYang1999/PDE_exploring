"""V36 symbolic part: specification M19 identities (x > 0 and x < 0 separately; sympy)."""
import sympy as sp
x, y, g, phi = sp.symbols('x y gamma phi', real=True)
out = []
def chk(n, e):
    v = sp.simplify(e); out.append((n, v)); print(n, ':', v)
for sg, xx in ((1, sp.Symbol('xp', positive=True)), (-1, -sp.Symbol('xp', positive=True))):
    X = sp.Symbol('X', real=True)
    rho = (sg*X)**g                                  # |x|^gamma on the side sgn x = sg
    psi = -sg*(sg*X)**(g + 1)/(g + 1)
    U = (-sp.diff(psi, y), sp.diff(psi, X))
    l = 1/g
    chk('side %+d: -Lap psi - d_x rho' % sg, -(sp.diff(psi, X, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, X))
    chk('side %+d: U - (0, -|x|^g)' % sg, sp.Matrix(U) - sp.Matrix([0, -rho]))
    chk('side %+d: (l X + U).grad rho - rho' % sg, (l*X + U[0])*sp.diff(rho, X) + (l*y + U[1])*sp.diff(rho, y) - rho)
    eta = y - g*rho/(1 - g)
    V0 = (l*X, l*y - rho)
    chk('side %+d: V0.grad eta - l eta' % sg, V0[0]*sp.diff(eta, X) + V0[1]*sp.diff(eta, y) - l*eta)
    chk('side %+d: det D(x, eta) - 1' % sg, sp.diff(eta, y) - 1)
# rotations: rho = |a.X|^g, a = (cos phi, sin phi), side s = a.X > 0; claimed U = a1 |s|^g (a2, -a1)
s = sp.Symbol('s', positive=True)
a1, a2 = sp.cos(phi), sp.sin(phi)
S = a1*x + a2*y
rho = S**g
psi = -a1*S**(g + 1)/(g + 1)
U = (-sp.diff(psi, y), sp.diff(psi, x))
chk('rotation: -Lap psi - d_x rho', -(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x))
Ssym = sp.Symbol('S', positive=True)
rr = sp.expand_trig(sp.expand(((x/g + U[0])*sp.diff(rho, x) + (y/g + U[1])*sp.diff(rho, y) - rho)*S**(1 - g)))
chk('rotation: (X/g + U).grad rho - rho (times S^(1-g))', sp.trigsimp(sp.expand(rr.subs(S**g, Ssym**g))))
chk('rotation: U - a1 S^g (a2, -a1)', sp.Matrix(U) - a1*S**g*sp.Matrix([a2, -a1]))
# physical reading: rho(t,x) = A(t)|x1 - z(t)|^g, u = (0, -rho) => rho_t + u.grad rho = A'|x1 - z|^g - A z' d|.|^g, u1 = 0
A = sp.Function('A'); z = sp.Function('z'); t = sp.Symbol('t')
rp = A(t)*(x - z(t))**g
chk('steady: rho_t + u.grad rho with u = (0, -rho), z\' = 0, A\' = 0', (sp.diff(rp, t) + 0*sp.diff(rp, x) - rp*sp.diff(rp, y)).subs({sp.Derivative(A(t), t): 0, sp.Derivative(z(t), t): 0}))
bad = [n for n, v in out if not (v == 0 or v == sp.zeros(2, 1) or v is True)]
print('ALL', len(out), 'checks; nonzero:', bad)
