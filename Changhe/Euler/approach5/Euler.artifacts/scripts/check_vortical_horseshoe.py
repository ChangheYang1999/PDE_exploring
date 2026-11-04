"""Independent sympy check of the explicit formulas in an external referee answer (sections 2, 5, 6).

Cartesian coordinates throughout (the referee worked in cylindrical ones). k = 1-2c, lam = 1+c, A = cI - omega J.
Checks:
 (1) cylindrical family U_r = -r/2 + C/r, U_theta = kappa r + D/r, U_z = z: div U = 0, curl U = 2 kappa e_z,
     [B, Omega] = -(1+c) Omega for all C, D;
 (2) alpha - k beta = dH_* - (2 kappa C + k D) dtheta, alpha = (B x Omega).dy, beta = U.dy;
 (3) with C = k a^2/2, D = -kappa a^2 the displayed P makes (U, P) an exact profile (all three residuals zero);
 (4) the (F6) carrier: q = r^2 - a^2 obeys dq/ds = -k q, dz/ds = lam z, dtheta/ds = kappa - omega - kappa a^2/r^2;
 (5) harmonic cubic phi = -x^3/3 + x y^2 at omega = 0 with P = -k phi - c y.grad phi - |grad phi|^2/2 is an exact
     profile, and the segment {(x,0,0): 0 <= x <= c} is invariant with dx/ds = x(c - x);
 (6) the Lyapunov identity B.grad H0 = -k |X|^2 - omega (Jy).grad P for the cubic (omega = 0 and general omega
     with the omega-dependent pressure of a harmonic gradient).
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
c, om, ka, C, D, a = sp.symbols('c omega kappa C D a', real=True)
k = 1 - 2 * c
lam = 1 + c
Y = sp.Matrix([x, y, z])
J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
A = c * sp.eye(3) - om * J
r2 = x ** 2 + y ** 2


def grad(f):
    return sp.Matrix([sp.diff(f, v) for v in (x, y, z)])


def div(V):
    return sum(sp.diff(V[i], v) for i, v in enumerate((x, y, z)))


def curl(V):
    return sp.Matrix([sp.diff(V[2], y) - sp.diff(V[1], z), sp.diff(V[0], z) - sp.diff(V[2], x),
                      sp.diff(V[1], x) - sp.diff(V[0], y)])


def dirder(V, W):
    """(V.grad) W"""
    return sp.Matrix([sum(V[j] * sp.diff(W[i], v) for j, v in enumerate((x, y, z))) for i in range(3)])


def residual(U, P):
    B = A * Y + U
    return sp.simplify((1 - c) * U + dirder(B, U) + om * J * U + grad(P))


ok = True
er = sp.Matrix([x, y, 0])            # r e_r
et = sp.Matrix([-y, x, 0])           # r e_theta
U = (-sp.Rational(1, 2) + C / r2) * er + (ka + D / r2) * et + sp.Matrix([0, 0, z])
Om = sp.simplify(curl(U))
B = A * Y + U
br = sp.simplify(dirder(B, Om) - dirder(Om, B) + lam * Om)
c1 = sp.simplify(div(U)) == 0 and Om == sp.Matrix([0, 0, 2 * ka]) and br == sp.zeros(3, 1)
print('(1) div U = 0, curl U = 2 kappa e_z, bracket:', c1)
ok &= c1

alpha = B.cross(Om)
form = alpha - k * U                    # components of alpha - k beta
Hs = (ka * (ka - om) + k / 4) * r2 + (2 * ka * D - k * C) * sp.log(sp.sqrt(r2)) - k * z ** 2 / 2
dtheta = sp.Matrix([-y / r2, x / r2, 0])
c2 = sp.simplify(form - grad(Hs) + (2 * ka * C + k * D) * dtheta) == sp.zeros(3, 1)
print('(2) alpha - k beta = dH_* - (2 kappa C + k D) dtheta:', c2)
ok &= c2

sub = {C: k * a ** 2 / 2, D: -ka * a ** 2}
U6 = U.subs(sub)
lr = sp.log(sp.sqrt(r2))
P6 = (ka ** 2 / 2 + sp.Rational(1, 8)) * r2 - (2 * ka ** 2 + k ** 2 / 2) * a ** 2 * lr \
    - (ka ** 2 / 2 + k ** 2 / 8) * a ** 4 / r2 - z ** 2
res6 = residual(U6, P6)
c3 = res6 == sp.zeros(3, 1)
print('(3) (F6) with the displayed pressure is an exact profile:', c3, '' if c3 else res6.T)
ok &= c3

B6 = A * Y + U6
q = r2 - a ** 2
dq = sp.simplify((grad(q).T * B6)[0])
dz = sp.simplify(B6[2])
th = sp.atan2(y, x)
dth = sp.simplify((grad(th).T * B6)[0])
c4 = sp.simplify(dq + k * q) == 0 and sp.simplify(dz - lam * z) == 0 and \
    sp.simplify(dth - (ka - om - ka * a ** 2 / r2)) == 0
print('(4) dq/ds = -k q, dz/ds = lam z, dtheta/ds = kappa - omega - kappa a^2/r^2:', c4)
ok &= c4

phi = -x ** 3 / 3 + x * y ** 2
assert sp.simplify(sum(sp.diff(phi, v, 2) for v in (x, y, z))) == 0
Uc = grad(phi)
# pressure of a harmonic gradient for general omega: P = -k phi - (Ay).grad phi - |grad phi|^2/2
Pc = -k * phi - ((A * Y).T * grad(phi))[0] - (Uc.T * Uc)[0] / 2
resc = residual(Uc, Pc)
c5a = resc == sp.zeros(3, 1)
Bc0 = (A * Y + Uc).subs(om, 0)
c5b = sp.simplify(Bc0.subs({y: 0, z: 0}) - sp.Matrix([x * (c - x), 0, 0])) == sp.zeros(3, 1)
print('(5) cubic harmonic gradient is an exact profile for every omega:', c5a,
      '; at omega = 0 the x-axis is invariant with dx/ds = x(c-x):', c5b)
ok &= c5a and c5b

X = c * Y + Uc
Q = Pc + c * (c - 1) * r2 / 2 + c * (c - 1) * z ** 2 / 2
H0 = Q + (X.T * X)[0] / 2
Bc = A * Y + Uc
lhs = (Bc.T * grad(H0))[0]
rhs = -k * (X.T * X)[0] - om * ((J * Y).T * grad(Pc))[0]
c6 = sp.simplify(lhs - rhs) == 0
print('(6) B.grad H0 = -k|X|^2 - omega (Jy).grad P for the cubic, every omega:', c6)
ok &= c6
print()
print('ALL PASS' if ok else 'SOME FAILED')
