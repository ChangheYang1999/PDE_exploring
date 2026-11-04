"""Symbolic verification of the rotating self-similar Euler profile equation and its exact identities.

Theoretical question: are the profile equation (PROMPT section 1) and the identities listed in
the coordinator list of identities (EXACT_IDENTITIES.md) exact algebraic consequences of the Euler equations under the rotating
self-similar ansatz?  Pass criterion: every printed residual simplifies to exactly 0.

Part 1 checks the derivation of the profile equation from Euler in physical variables, using a
polynomial test field (the identity is linear in the residual, so a generic polynomial test is a
genuine check of the change of variables, not of a solution).
Part 2 checks the identities for generic smooth functions U1, U2, U3, P (sympy undefined functions),
using div U = 0 where stated.
"""
import sympy as sp

c, w = sp.symbols('c omega', real=True)
y1, y2, y3 = sp.symbols('y1 y2 y3', real=True)
Y = sp.Matrix([y1, y2, y3])
J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
I3 = sp.eye(3)


def grad(f, v=Y):
    return sp.Matrix([sp.diff(f, vi) for vi in v])


def jac(F, v=Y):
    # (jac F)_{ij} = d_j F_i
    return sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], v[j]))


def div(F, v=Y):
    return sum(sp.diff(F[i], v[i]) for i in range(3))


def curl(F, v=Y):
    return sp.Matrix([sp.diff(F[2], v[1]) - sp.diff(F[1], v[2]),
                      sp.diff(F[0], v[2]) - sp.diff(F[2], v[0]),
                      sp.diff(F[1], v[0]) - sp.diff(F[0], v[1])])


def adv(A, F):
    # (A . grad) F
    return jac(F) * A


def profile_residual(U, P):
    B = (c * I3 - w * J) * Y + U
    return (1 - c) * U + adv(B, U) + w * J * U + grad(P)


results = []


def check(name, expr):
    if isinstance(expr, sp.MatrixBase):
        val = [sp.simplify(sp.expand(e)) for e in expr]
        ok = all(v == 0 for v in val)
    else:
        val = sp.simplify(sp.expand(expr))
        ok = (val == 0)
    results.append((name, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"  residual={val}"))


# ---------------- Part 1: derivation of the profile equation ----------------
# u(x,t) = s^{c-1} R(phi) U(R(phi)^T x / s^c), p = s^{2c-2} P(R^T x / s^c), s = T - t, phi = -omega log s.
# Then  s^{2-c} R^T [d_t u + (u.grad)u + grad p] = profile residual at y = R^T x / s^c.
t = sp.symbols('t', real=True)
s = sp.symbols('s', positive=True)
x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
Xv = sp.Matrix([x1, x2, x3])
phi = -w * sp.log(s)
R = sp.Matrix([[sp.cos(phi), -sp.sin(phi), 0], [sp.sin(phi), sp.cos(phi), 0], [0, 0, 1]])
# polynomial test field (not a solution; any field works since the identity is linear in the residual)
a = sp.symbols('a0:12', real=True)
Ut = sp.Matrix([a[0] + a[1] * y2 + a[2] * y1 * y3 + a[9] * y2**2,
                a[3] * y1 + a[4] * y3**2 + a[10] * y1 * y2,
                a[5] + a[6] * y1 * y2 + a[11] * y3])
Pt = a[7] * y1**2 + a[8] * y2 * y3
yofx = (R.T * Xv) / s**c
subs_y = {y1: yofx[0], y2: yofx[1], y3: yofx[2]}
u = s**(c - 1) * R * Ut.subs(subs_y)
p = s**(2 * c - 2) * Pt.subs(subs_y)
# d/dt = - d/ds
dudt = -sp.Matrix([sp.diff(ui, s) for ui in u])
euler = dudt + jac(u, Xv) * u + grad(p, Xv)
lhs = s**(2 - c) * R.T * euler
rhs = profile_residual(Ut, Pt).subs(subs_y)
diff_expr = (lhs - rhs)
# evaluate at random rational parameter values with 60-digit precision (trig simplification is too slow)
import random
random.seed(1)
maxerr = 0
for trial in range(5):
    vals = {ai: sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for ai in a}
    vals.update({c: sp.Rational(random.randint(1, 49), 100), w: sp.Rational(random.randint(-30, 30), 7),
                 s: sp.Rational(random.randint(1, 40), 9), x1: sp.Rational(random.randint(-9, 9), 4),
                 x2: sp.Rational(random.randint(-9, 9), 4), x3: sp.Rational(random.randint(-9, 9), 4)})
    for e in diff_expr:
        v = abs(sp.N(e.subs(vals), 60))
        maxerr = max(maxerr, v)
okp1 = maxerr < 1e-45
results.append(("Part1: Euler under rotating ansatz == profile residual (numeric, 60 digits)", okp1))
print(('PASS' if okp1 else 'FAIL') + f'  Part1: Euler under rotating ansatz == profile residual '
      f'(max |difference| over 5 random rational points, 60 digits: {maxerr})')

# ---------------- Part 2: identities for generic functions ----------------
U1, U2, U3, Pf = [sp.Function(n)(y1, y2, y3) for n in ('U1', 'U2', 'U3', 'P')]
U = sp.Matrix([U1, U2, U3])
P = Pf
B = (c * I3 - w * J) * Y + U
Xs = c * Y + U
Om = curl(U)
res = profile_residual(U, P)
divU = div(U)
# substitution enforcing div U = 0: d3 U3 = -d1 U1 - d2 U2 (and its derivatives)
d3U3 = -sp.diff(U1, y1) - sp.diff(U2, y2)


def enforce_div(expr):
    # replace d_y3 U3 and its derivatives using div U = 0
    rep = {}
    for k1 in range(3):
        for k2 in range(3):
            for k3 in range(3):
                order = (k1, k2, k3)
                base = sp.Derivative(U3, y3)
                target = sp.diff(U3, y3)
                for _ in range(k1):
                    target = sp.diff(target, y1)
                for _ in range(k2):
                    target = sp.diff(target, y2)
                for _ in range(k3):
                    target = sp.diff(target, y3)
                val = d3U3
                for _ in range(k1):
                    val = sp.diff(val, y1)
                for _ in range(k2):
                    val = sp.diff(val, y2)
                for _ in range(k3):
                    val = sp.diff(val, y3)
                rep[target] = val
    # apply highest-order first
    keys = sorted(rep.keys(), key=lambda d: -sum(n for _, n in d.variable_count))
    out = expr
    for k_ in keys:
        out = out.subs(k_, rep[k_])
    return out


# (a) Bernoulli: (1-2c) X + Omega x B + grad H == residual, identically (no div needed?)
H = P + Xs.dot(Xs) / 2 + c * (c - 1) / 2 * Y.dot(Y) - w * (J * Y).dot(Xs)
bern = (1 - 2 * c) * Xs + Om.cross(B) + grad(H)
check("Bernoulli: (1-2c)X + Omega x B + grad H - residual == 0", bern - res)

# (b) B.grad H = (2c-1) X.B + (residual terms): B.grad H + (1-2c) X.B = B.res  (since (Omega x B).B = 0)
check("Bernoulli transport: B.grad H - (2c-1) X.B - B.res == 0",
      B.dot(grad(H)) - (2 * c - 1) * Xs.dot(B) - B.dot(res))

# (c) X.B = |X|^2 - omega (Jy).U
check("X.B = |X|^2 - omega (Jy).U", Xs.dot(B) - (Xs.dot(Xs) - w * (J * Y).dot(U)))

# (d) rotating-frame form: (B.grad)B + 2 omega J B + (1-2c) X + grad(P - c(1-c)|y|^2/2 - omega^2|y_h|^2/2) == residual
yh2 = y1**2 + y2**2
rotform = adv(B, B) + 2 * w * J * B + (1 - 2 * c) * Xs + grad(P - c * (1 - c) / 2 * Y.dot(Y) - w**2 / 2 * yh2)
check("Rotating-frame form == residual", rotform - res)

# (e) Vorticity: curl(res) == Omega + B.grad Omega - (Omega.grad)U + omega J Omega + (terms vanishing when div U = 0)
vort = Om + adv(B, Om) - adv(Om, U) + w * J * Om
check("Vorticity eq: curl(res) - [Omega + B.grad Omega - (Omega.grad)U + omega J Omega] == 0 using div U = 0",
      enforce_div(curl(res) - vort))

# (f) Lie bracket form: [B,Omega] = B.grad Omega - Omega.grad B ; vort - (B.grad Omega - (grad B - (1+c)I) Omega)
gradB = jac(B)
check("Vorticity eq equals [B,Omega] + (1+c) Omega", vort - (adv(B, Om) - gradB * Om + (1 + c) * Om))

# (g) curl(Omega x B) = (2c-1) Omega - ( [B,Omega] + (1+c) Omega )  using div Omega = 0, div B = 3c + div U
cOB = curl(Om.cross(B))
check("curl(Omega x B) = (2c-1)Omega + vort  (using div U = 0)",
      enforce_div(cOB - ((2 * c - 1) * Om + vort)))

# (h) circulation form: (B.grad)U + (grad B)^T U - (2c-1) U - grad(|U|^2/2 - P) == res
circ = adv(B, U) + gradB.T * U - (2 * c - 1) * U - grad(U.dot(U) / 2 - P)
check("Circulation form: L_B U^flat - (2c-1) U - grad(|U|^2/2-P) == res", circ - res)

# (i) energy: div(B|U|^2/2 + P U) - (5c/2 - 1)|U|^2 == U.res  (div U = 0)
en = div(B * U.dot(U) / 2 + P * U) - (sp.Rational(5, 2) * c - 1) * U.dot(U)
check("Energy: div(B|U|^2/2 + P U) - (5c/2-1)|U|^2 == U.res (div U=0)", enforce_div(en - U.dot(res)))

# (j) angular momentum M = (Jy).U: B.grad M - (2c-1) M + d_theta P == (Jy).res,  d_theta = (Jy).grad
M = (J * Y).dot(U)
dthP = (J * Y).dot(grad(P))
am = B.dot(grad(M)) - (2 * c - 1) * M + dthP
check("Angular momentum: B.grad M - (2c-1)M + d_theta P == (Jy).res", am - (J * Y).dot(res))
check("div(P Jy) == d_theta P", div(P * (J * Y)) - dthP)

# (k) helicity: div(B U.Omega - (|U|^2/2 - P) Omega) - (4c-2) U.Omega == Omega.res + U.curl(res)-ish
hel = div(B * U.dot(Om) - (U.dot(U) / 2 - P) * Om) - (4 * c - 2) * U.dot(Om)
# expected: equals Omega.res + U.(curl res) up to div terms; test with residual-free combination
check("Helicity: hel - [Omega.res + U.(curl res)] == 0 (div U=0)",
      enforce_div(hel - (Om.dot(res) + U.dot(curl(res)))))

# (l) curl(Jy) = 2 e_z and curl B = Omega - 2 omega e_z
check("curl B = Omega - 2 omega e_z", curl(B) - (Om - 2 * w * sp.Matrix([0, 0, 1])))

# (m) div B = 3c + div U
check("div B = 3c + div U", div(B) - 3 * c - divU)

# (n) |Omega|^2 growth: d/ds |Omega|^2 along B = 2 Omega.(S - I) Omega when vort = 0
S = (jac(U) + jac(U).T) / 2
grow = 2 * Om.dot(adv(B, Om)) - (2 * Om.dot((S - I3) * Om) + 2 * Om.dot(vort))
check("B.grad|Omega|^2 = 2 Omega.(S-I)Omega + 2 Omega.vort", grow)

print()
print("ALL PASS" if all(ok for _, ok in results) else "SOME FAILED")
