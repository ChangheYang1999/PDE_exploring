"""Exact rational check of T4-229 section 3 (c1-t1 R1-029).

For random rational data: W = Q^m with a positive-definite Gram G, an onto redundant parameterization K (m x d,
d > m), J (p x m), f in Q^p, lambda > 0. Checks that the pullback normal matrix M = K^T (J^T J + lambda G) K has
kernel exactly ker K, that the right side -K^T J^T f lies in its range, that every solution z gives K z = w*, with
w* = -(J^T J + lambda G)^(-1) J^T f the unique physical minimizer, and that w* is the same for two different onto
parameterizations. Also checks the two-coordinate counterexample of section 2 (steps 1/2 and 2/3 at lambda = 1) and
the lambda -> 0 limit: w*(lambda) tends to the G-minimum-norm least-squares solution.
"""
import random
import sympy as sp

random.seed(20261029)


def rmat(r, c, lo=-4, hi=4):
    return sp.Matrix(r, c, lambda i, j: sp.Rational(random.randint(lo, hi), random.randint(1, 3)))


def check_case(m, d, p, lam):
    while True:
        K = rmat(m, d)
        if K.rank() == m:
            break
    A = rmat(m, m)
    G = A.T * A + sp.eye(m) / 7
    J = rmat(p, m)
    f = rmat(p, 1)
    H = J.T * J + lam * G
    wstar = -H.inv() * J.T * f
    M = K.T * H * K
    rhs = -K.T * J.T * f
    assert M.rank() == m, "rank of pullback matrix"
    nsM = M.nullspace()
    nsK = K.nullspace()
    assert len(nsM) == len(nsK) == d - m
    for v in nsM:
        assert K * v == sp.zeros(m, 1)
    for v in nsK:
        assert (v.T * rhs)[0] == 0, "rhs orthogonal to ker K"
    sol, params = M.gauss_jordan_solve(rhs)
    z0 = sol.subs({t: 0 for t in params})
    assert sp.simplify(K * z0 - wstar) == sp.zeros(m, 1)
    z1 = sol.subs({t: random.randint(-5, 5) for t in params})
    assert sp.simplify(K * z1 - wstar) == sp.zeros(m, 1)
    # second onto parameterization
    while True:
        K2 = rmat(m, d + 2)
        if K2.rank() == m:
            break
    M2 = K2.T * H * K2
    sol2, params2 = M2.gauss_jordan_solve(-K2.T * J.T * f)
    z2 = sol2.subs({t: 0 for t in params2})
    assert sp.simplify(K2 * z2 - wstar) == sp.zeros(m, 1)
    return wstar


for (m, d, p) in [(3, 5, 4), (4, 7, 2), (5, 9, 6)]:
    for lam in [sp.Rational(1, 3), sp.Rational(5, 2)]:
        check_case(m, d, p, lam)
print("pullback kernel = ker K, consistency, invariance of K z: PASS (6 cases)")

# two-coordinate counterexample: objective (x - 1)^2/2 at x = 0, Euclidean damping lambda
lam = sp.Integer(1)
x1 = 1 / (1 + lam)
Jab = sp.Matrix([[1, 1]])
ab = (Jab.T * Jab + lam * sp.eye(2)).inv() * Jab.T * sp.Matrix([1])
x2 = ab[0] + ab[1]
assert (x1, x2) == (sp.Rational(1, 2), sp.Rational(2, 3))
ls = sp.symbols('lambda', positive=True)
diff = sp.simplify(2 / (2 + ls) - 1 / (1 + ls) - ls / ((1 + ls) * (2 + ls)))
assert diff == 0
print("Euclidean damping counterexample: steps", x1, x2, "difference formula PASS")

# lambda -> 0 limit: G-minimum-norm least squares solution, J rank deficient
m, p = 4, 2
J = rmat(p, m)
A = rmat(m, m)
G = A.T * A + sp.eye(m)
f = rmat(p, 1)
Ginv = G.inv()
# G-min-norm LS solution of min |f + J w|: w = -G^-1 J^T (J G^-1 J^T)^+ f
wls = -Ginv * J.T * (J * Ginv * J.T).pinv() * f
wl = -(J.T * J + ls * G).inv() * J.T * f
lim = sp.Matrix([sp.limit(sp.simplify(e), ls, 0) for e in wl])
assert sp.simplify(lim - wls) == sp.zeros(m, 1)
print("lambda -> 0 limit equals the G-minimum-norm least-squares step: PASS")
print("ALL CHECKS PASS")
