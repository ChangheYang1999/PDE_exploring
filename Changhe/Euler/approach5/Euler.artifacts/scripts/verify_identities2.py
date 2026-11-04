"""Symbolic checks of coordinator identities C1-C4 (a coordinator note section 2).

Question: are the following exact consequences of the profile equation (generic smooth U, P, div U = 0)?
 C1  B.grad(y.U) = (2c-1) y.U + |U|^2 - y.grad P + y.res
 C2  H0 := P + |cy+U|^2/2 + c(c-1)|y|^2/2 (nonrotating Bernoulli function) satisfies
     B.grad H0 = (2c-1)|X|^2 - omega d_theta P + X.res  (X = cy + U; residual pairs with X, not B)
 C3  Htil := P + |U|^2/2 + c y.U - omega (Jy).U satisfies Omega x B = -(1-2c) U - grad Htil + res
     and hence B.grad Htil = (2c-1) U.B + B.res
 C4  for any smooth vector field W: div[B,W] = B.grad(div W) - W.grad(div B) (pure calculus; with div B = 3c
     constant this gives B.grad(div W) = -(1+c) div W whenever [B,W] = -(1+c) W)
Pass criterion: every residual simplifies to 0.
"""
import sympy as sp
import importlib.util, os, sys

c, w = sp.symbols('c omega', real=True)
y1, y2, y3 = sp.symbols('y1 y2 y3', real=True)
Y = sp.Matrix([y1, y2, y3])
J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
I3 = sp.eye(3)


def grad(f):
    return sp.Matrix([sp.diff(f, v) for v in Y])


def jac(F):
    return sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], Y[j]))


def div(F):
    return sum(sp.diff(F[i], Y[i]) for i in range(3))


def curl(F):
    return sp.Matrix([sp.diff(F[2], y2) - sp.diff(F[1], y3),
                      sp.diff(F[0], y3) - sp.diff(F[2], y1),
                      sp.diff(F[1], y1) - sp.diff(F[0], y2)])


U1, U2, U3, Pf, W1, W2, W3 = [sp.Function(n)(y1, y2, y3) for n in ('U1', 'U2', 'U3', 'P', 'W1', 'W2', 'W3')]
U = sp.Matrix([U1, U2, U3])
W = sp.Matrix([W1, W2, W3])
P = Pf
B = (c * I3 - w * J) * Y + U
X = c * Y + U
Om = curl(U)
res = (1 - c) * U + jac(U) * B + w * J * U + grad(P)
M = (J * Y).dot(U)
dthP = (J * Y).dot(grad(P))

results = []


def check(name, expr):
    if isinstance(expr, sp.MatrixBase):
        ok = all(sp.simplify(sp.expand(e)) == 0 for e in expr)
    else:
        ok = sp.simplify(sp.expand(expr)) == 0
    results.append(ok)
    print(('PASS  ' if ok else 'FAIL  ') + name)


check("C1 B.grad(y.U) = (2c-1)y.U + |U|^2 - y.grad P + y.res",
      B.dot(grad(Y.dot(U))) - ((2 * c - 1) * Y.dot(U) + U.dot(U) - Y.dot(grad(P)) + Y.dot(res)))
H0 = P + X.dot(X) / 2 + c * (c - 1) / 2 * Y.dot(Y)
check("C2 B.grad H0 = (2c-1)|X|^2 - omega d_theta P + X.res",
      B.dot(grad(H0)) - ((2 * c - 1) * X.dot(X) - w * dthP + X.dot(res)))
Ht = P + U.dot(U) / 2 + c * Y.dot(U) - w * M
check("C3a Omega x B = -(1-2c)U - grad Htil + res", Om.cross(B) - (-(1 - 2 * c) * U - grad(Ht) + res))
check("C3b B.grad Htil = (2c-1)U.B + B.res", B.dot(grad(Ht)) - ((2 * c - 1) * U.dot(B) + B.dot(res)))
brk = jac(W) * B - jac(B) * W  # [B,W] = B.grad W - W.grad B
check("C4 div[B,W] = B.grad(div W) - W.grad(div B)", div(brk) - (B.dot(grad(div(W))) - W.dot(grad(div(B)))))
print()
print('ALL PASS' if all(results) else 'SOME FAILED')
