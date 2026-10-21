"""verifier: own checks of lead notes S-9 (b), (e), (f) and S-10 (a), (b), (d) (fred4, fred5)."""
import sympy as sp
import math
A, g, x, y, s, c3, c5, c7, P, Q = sp.symbols('A g x y s c3 c5 c7 P Q', positive=True)
# S-9 (b): thresholds; (P - P*)/(2i) for P = -i L, L = A s d_s + y d_y - 1 - g M(D)
An, gs = 10.150725, 29.749491          # g* from B2 (trace value); an earlier run used 29.749 (truncated)
print('S-9 (b) sigma_dx = (A+3+2g)/(2A) =', (An + 3 + 2 * gs) / (2 * An), ' sigma_dy = (A+3)/2 =', (An + 3) / 2)
# anisotropic packet |y|^a Phi(s/|y|^A): L^2-Sobolev limit along dx: sigma < (2a + A + 1)/(2A), a = 1 + g
a = 1 + g
print('S-9 (b) packet limit along dx minus sigma_dx:', sp.simplify((2 * a + A + 1) / (2 * A) - (A + 3 + 2 * g) / (2 * A)))
print('S-9 (f) (1+g*)/A =', (1 + gs) / An)
# S-9 (e) resonance: A = P/Q, j = 2P + 1
j = 2 * P + 1
print('S-9 (e) p_j at A = P/Q, j = 2P+1:', sp.simplify(2 * j + (j - 1) * Q / P))
# S-10 (d): f = x^(6+beta) y^3, (-A x, (2A+1) y).grad f - f
be = 2 / A
f = x ** (6 + be) * y ** 3
print('S-10 (d) residual:', sp.simplify((-A * x * sp.diff(f, x) + (2 * A + 1) * y * sp.diff(f, y) - f) / f))
# S-10 (a): origin expansions for w = -A x + c3 x^3 + c5 x^5 + c7 x^7, (log g)' = (w' - A)/w, g ~ x^2
w = -A * x + c3 * x ** 3 + c5 * x ** 5 + c7 * x ** 7
e = sp.series((sp.diff(w, x) - A) / w - 2 / x, x, 0, 8).removeO()
G = sp.series(sp.exp(sp.integrate(e, x)), x, 0, 7).removeO()
print('S-10 (a) G = g/x^2:', sp.expand(G))
print('   claim x^2:', sp.simplify(G.coeff(x, 2) + c3 / (2 * A)), ' x^4:', sp.simplify(G.coeff(x, 4) + (6 * A * c5 + c3 ** 2) / (8 * A ** 2)))
gg = x ** 2 * G
a2 = sp.expand((sp.diff(gg, x) - sp.diff(w, x, 2)) / 2)
ax = sp.expand(sp.series(a2 / x, x, 0, 6).removeO())
print('S-10 (a) a2/x:', ax)
print('   claim x^0:', sp.simplify(ax.coeff(x, 0) - (1 - 3 * c3)), ' x^2:', sp.simplify(ax.coeff(x, 2) - (-10 * c5 - c3 / A)),
      ' x^4:', sp.simplify(ax.coeff(x, 4) - (-21 * c7 - 9 * c5 / (4 * A) - 3 * c3 ** 2 / (8 * A ** 2))))
# S-10 (b) law vs this lane's D9 exact responses (R12, A = 10.150725, L = 8.6)
bn = 2 / An
xs = 8.6
D9 = {(0.3, 0.5): -4.63170e6, (0.3, 1): -6.36862e4, (0.3, 2): -896.490, (0.3, 3): -75.7308, (0.6, 1.5): -1.371995e5,
      (0.6, 3): -1.903542e3, (1.0, 1): -1.3027e9, (1.0, 2): -1.7807e7, (1.0, 3): -1.444626e6}
for (sg, x0), ex in D9.items():
    law = -xs ** (4 + bn) * (1 - bn) * (6 + bn) * (7 + bn) / 6 * x0 ** (-(6 + bn)) * sg * math.sqrt(math.pi) * math.exp(((6 + bn) * sg) ** 2 / 4)
    print('S-10 (b) sig %.1f x0 %.1f: exact (D9) %.6e  law %.6e  ratio %.4f' % (sg, x0, ex, law, ex / law))
