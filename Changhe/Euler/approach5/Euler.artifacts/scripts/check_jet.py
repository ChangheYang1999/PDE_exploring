"""Exact finite-jet checks; this is not an existence proof for an Euler germ."""
import resource

resource.setrlimit(resource.RLIMIT_AS, (1900 * 1024**2, 1900 * 1024**2))

import sympy as S

x, s, z, c, u, t = S.symbols("x s z c u t", nonzero=True)
v = S.Matrix([x, s, z])
kappa = 1 + c
rho, lam, eta = -2 * kappa, -kappa, 3 * c + 3 * kappa
alpha, beta, gamma = rho - c, lam - c, eta - c
U = S.Matrix(
    [
        u + alpha * x + t * s**2 * z,
        beta * s,
        gamma * z - x**2 / 2 - beta * x * s**2 / (2 * u),
    ]
)
B = U + S.Matrix([c * x - u, c * s, c * z])


def curl(V):
    return S.Matrix(
        [
            S.diff(V[2], s) - S.diff(V[1], z),
            S.diff(V[0], z) - S.diff(V[2], x),
            S.diff(V[1], x) - S.diff(V[0], s),
        ]
    )


def truncate(p, degree):
    return S.expand(
        sum(
            coefficient
            * S.prod(variable**power for variable, power in zip(v, exponents))
            for exponents, coefficient in S.Poly(S.expand(p), x, s, z).terms()
            if sum(exponents) <= degree
        )
    )


Omega = curl(U)
expected = S.Matrix(
    [-beta * x * s / u, x + (beta / (2 * u) + t) * s**2, -2 * t * s * z]
)
assert all(S.simplify(p) == 0 for p in Omega - expected)
assert S.simplify(sum(S.diff(U[i], v[i]) for i in range(3))) == 0
assert truncate(U.dot(Omega), 2) == 0
vorticity_residual = Omega.jacobian(v) * B - B.jacobian(v) * Omega + kappa * Omega
assert all(truncate(p, 2) == 0 for p in vorticity_residual)
force = (1 - c) * U + U.jacobian(v) * B
force3 = force.applyfunc(lambda p: truncate(p, 3))
assert all(S.simplify(p) == 0 for p in curl(force3))
assert S.simplify(Omega[1].subs({x: -beta * s**2 / (2 * u), z: 0}) - t * s**2) == 0
assert S.simplify(2 * lam + eta - (-1 + 2 * c - rho)) == 0
print("PASS: all seven exact endpoint-jet checks.")
