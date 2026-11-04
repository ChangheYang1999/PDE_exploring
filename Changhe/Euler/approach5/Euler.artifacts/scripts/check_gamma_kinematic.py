"""Checks of explicit identities in an external referee answer (coordinator check, 2026-11-02).

X = -B is the generator of Psi, div X = -d, [X, W] = kappa W, delta = kappa - d.
(1) Monomial saddle: X = h x d_x - b y d_y - a z d_z, W = x^p y^q d_z. With div X = -d, the bracket [X, W] = kappa W
    holds iff (p+1) h - (q+1) b = delta.
(2) Triangular model X = (F(q), H(q, z)), W = w(q) d_z, q in R^2: div X = -d and [X, W] = kappa W imply
    div(w F) = delta w (checked symbolically for general F, w, with H solved from the divergence condition).
(3) Multiplying a solution W0 by f: [X, f W0] - kappa f W0 = (X f) W0 and div(f W0) = W0.grad f when div W0 = 0.
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
V = (x, y, z)


def bracket(Xv, Wv):
    return [sum(Xv[j] * sp.diff(Wv[i], V[j]) - Wv[j] * sp.diff(Xv[i], V[j]) for j in range(3)) for i in range(3)]


def div(Xv):
    return sum(sp.diff(Xv[i], V[i]) for i in range(3))


ok = True
h, b, d, kap = sp.symbols('h b d kappa', positive=True)
p, q = sp.symbols('p q', nonnegative=True)
a = h - b + d                      # forced by div X = -d
X = [h * x, -b * y, -a * z]
assert sp.simplify(div(X) + d) == 0
W = [0, 0, x ** p * y ** q]
br = bracket(X, W)
res = sp.simplify(br[2] / W[2] - kap)
cond = sp.simplify(res - ((p + 1) * h - (q + 1) * b - (kap - d)))
print('(1) [X,W]_z / W_z - kappa =', sp.factor(res), '; equals (p+1)h-(q+1)b-delta:', cond == 0)
ok = ok and cond == 0 and br[0] == 0 and br[1] == 0 and div(W) == 0

F1, F2, w = sp.Function('F1')(x, y), sp.Function('F2')(x, y), sp.Function('w')(x, y)
Hz = -d - sp.diff(F1, x) - sp.diff(F2, y)          # d_z H from div X = -d
H = Hz * z + sp.Function('H0')(x, y)
X = [F1, F2, H]
assert sp.simplify(div(X) + d) == 0
W = [0, 0, w]
br = bracket(X, W)
lhs = sp.simplify(br[2] - kap * w)                  # must vanish for the bracket equation
divwF = sp.diff(w * F1, x) + sp.diff(w * F2, y)
chk = sp.simplify(lhs - (divwF - (kap - d) * w))
print('(2) bracket residual equals div(wF) - delta w:', chk == 0)
ok = ok and chk == 0 and br[0] == 0 and br[1] == 0

f = sp.Function('f')(x, y, z)
W0 = [sp.Function('W%d' % i)(x, y, z) for i in range(3)]
Xg = [sp.Function('X%d' % i)(x, y, z) for i in range(3)]
lhs = [sp.expand(e) for e in bracket(Xg, [f * c for c in W0])]
rhs = [sp.expand(f * e + sum(Xg[j] * sp.diff(f, V[j]) for j in range(3)) * W0[i]) for i, e in enumerate(bracket(Xg, W0))]
c3 = all(sp.simplify(l - r) == 0 for l, r in zip(lhs, rhs))
c4 = sp.simplify(div([f * c for c in W0]) - f * div(W0) - sum(W0[j] * sp.diff(f, V[j]) for j in range(3))) == 0
print('(3) [X, f W0] = f [X, W0] + (X f) W0:', c3, '; div(f W0) = f div W0 + W0.grad f:', c4)
ok = ok and c3 and c4
print('ALL PASS' if ok else 'SOME FAILED')
