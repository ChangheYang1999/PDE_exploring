"""Independent Cartesian check of the local saddle model in an external referee answer.

Question: does the field U_r = -r/2 + k a^2/(2r), U_theta = kappa (r - a^2/r), U_z = z (k = 1-2c), with the stated P,
solve the rotating profile equation (1-c)U + (B.grad)U + omega J U + grad P = 0 exactly on r > 0, with div U = 0,
Omega = 2 kappa e_z, and does the circle r = a, z = 0 carry a B-periodic orbit with zero U-circulation and Floquet
exponents 2c-1 (radial) and 1+c (axial)?  Pass criterion: every printed residual simplifies to 0.
"""
import sympy as sp

c, w, kap = sp.symbols('c omega kappa', real=True)
a = sp.symbols('a', positive=True)
x, y, z = sp.symbols('x y z', real=True)
k = 1 - 2 * c
Y = sp.Matrix([x, y, z])
r2 = x**2 + y**2
r = sp.sqrt(r2)
er = sp.Matrix([x / r, y / r, 0])
et = sp.Matrix([-y / r, x / r, 0])
ez = sp.Matrix([0, 0, 1])
Ur = -r / 2 + k * a**2 / (2 * r)
Ut = kap * (r - a**2 / r)
U = sp.simplify(Ur * er + Ut * et + z * ez)
P = (sp.Rational(1, 8) + kap**2 / 2) * r2 - (k**2 / 2 + 2 * kap**2) * a**2 * sp.log(r / a) \
    - (k**2 / 8 + kap**2 / 2) * a**4 / r2 - z**2
J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
B = (c * sp.eye(3) - w * J) * Y + U


def jac(F):
    return sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], Y[j]))


def grad(f):
    return sp.Matrix([sp.diff(f, v) for v in Y])


def curl(F):
    return sp.Matrix([sp.diff(F[2], y) - sp.diff(F[1], z), sp.diff(F[0], z) - sp.diff(F[2], x),
                      sp.diff(F[1], x) - sp.diff(F[0], y)])


ok = True


def check(name, e):
    global ok
    e = sp.Matrix(e) if isinstance(e, sp.MatrixBase) else sp.Matrix([e])
    res = [sp.simplify(sp.expand(t)) for t in e]
    good = all(t == 0 for t in res)
    ok = ok and good
    print(('PASS  ' if good else 'FAIL  ') + name + ('' if good else '  ' + str(res)))


check('div U = 0', sum(sp.diff(U[i], Y[i]) for i in range(3)))
check('curl U = 2 kappa e_z', curl(U) - 2 * kap * ez)
check('profile equation', (1 - c) * U + jac(U) * B + w * J * U + grad(P))
pt = {x: a, y: 0, z: 0}
check('B = -omega a e_theta on the circle', B.subs(pt) - sp.Matrix([0, -w * a, 0]))
# zero U-circulation: U_theta vanishes on r = a
check('U_theta = 0 on r = a', sp.simplify(Ut.subs({x: a, y: 0})))
# Floquet: the circle is a relative equilibrium of the (r, z) reduction; radial and axial derivatives of B_r, B_z
Br = sp.simplify(B.dot(er))
Bz = B[2]
check('d B_r / d r at r = a equals 2c - 1', sp.simplify(sp.diff(Br.subs(y, 0), x).subs(pt) - (2 * c - 1)))
check('d B_z / d z equals 1 + c', sp.diff(Bz, z) - (1 + c))
check('B_r independent of z, B_z independent of (x, y)', sp.Matrix([sp.diff(Br, z), sp.diff(Bz, x), sp.diff(Bz, y)]))
print()
print('ALL PASS' if ok else 'SOME FAILED')
