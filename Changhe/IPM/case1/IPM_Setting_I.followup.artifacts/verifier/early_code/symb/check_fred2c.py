"""verifier: checks for the converse of FINAL_REPORT 6.3.1 (a) (lead request 03:08Z 3 (d); fred2 saddle/PROOF.md).
 (1) flat-extension lemma: xi^(a - b l + r) d_xi^r d_eta^l {xi^(-a) F(eta xi^b)} is a combination of I^m F^(l+m)(I), 0 <= m <= r
     (no explicit xi left after eta = I xi^(-b)), for r, l <= 4.
 (2) p_j = (j B - 1)/A = 2j + (j-1)/A, B = 2A + 1.
 (3) symmetric vector-field resonances for rational A = p/q by enumeration, against fred2's formulas; smooth scalar
     Taylor orders (p_j even integer) against j = 1 + 2 p l.
 (4) C_(0,j) = phi_j on an exact example: W = L (linear), rho = |x|^(-1/A) Phi(y |x|^(B/A)), Phi(I) = I + f3 I^3 + f5 I^5;
     G_j/H_j - fp int_0^x (G_j/H_j)' is the constant phi_j (j = 3, 5).
"""
from fractions import Fraction
import sympy as sp

out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))

# (1)
xi, eta, a, b, I = sp.symbols('xi eta a b I', positive=True)
F = sp.Function('F')
ok = True
for r in range(5):
    for l in range(5):
        expr = sp.diff(xi**(-a) * F(eta * xi**b), xi, r, eta, l) * xi**(a - b * l + r)
        e2 = sp.simplify(sp.expand(expr.subs(eta, I * xi**(-b))))
        if e2.has(xi):
            ok = False
            P('(1) r = %d, l = %d: explicit xi remains' % (r, l))
        # orders of F derivatives present and powers of I
        Ds = sp.symbols('D0:%d' % (l + r + 2))
        e3 = e2.doit()
        for k in range(l + r + 1, 0, -1):
            e3 = e3.subs(sp.Derivative(F(I), (I, k)), Ds[k])
        e3 = e3.subs(F(I), Ds[0])
        ders = {k for k in range(l + r + 2) if e3.has(Ds[k])}
        if e3.has(F):
            ok = False
            P('(1) r = %d, l = %d: unresolved F terms' % (r, l))
        # powers of I attached to D_k: I^m D_(l+m)
        for k in ders:
            cpoly = sp.Poly(sp.expand(e3).coeff(Ds[k]), I)
            if any(mon[0] != k - l for mon in cpoly.monoms()):
                ok = False
                P('(1) r = %d, l = %d: F^(%d) carries I-powers %s' % (r, l, k, cpoly.monoms()))
        if ders and (min(ders) < l or max(ders) > l + r):
            ok = False
            P('(1) r = %d, l = %d: derivative orders %s outside [l, l + r]' % (r, l, sorted(ders)))
P('(1) flat-extension structure for r, l <= 4:', ok)

# (2)
A = sp.symbols('A', positive=True)
j = sp.symbols('j', positive=True)
P('(2) (j B - 1)/A - (2j + (j-1)/A):', sp.simplify((j * (2 * A + 1) - 1) / A - (2 * j + (j - 1) / A)))

# (3)
for p_, q_ in [(3, 2), (5, 2), (7, 3), (4, 3), (203, 20)]:
    Af = Fraction(p_, q_)
    lim = 2 * (2 * p_ + q_) * 3 + 2
    r1 = sorted((m, n) for m in range(0, lim) for n in range(0, lim) if m + n >= 2 and m % 2 == 1 and n % 2 == 0
                and Af * (-m + 2 * n + 1) + n == 0)
    r2 = sorted((m, n) for m in range(0, lim) for n in range(0, lim) if m + n >= 2 and m % 2 == 0 and n % 2 == 1
                and Af * (-m + 2 * n - 2) + (n - 1) == 0)
    f1 = sorted((1 + 2 * (2 * p_ + q_) * l, 2 * p_ * l) for l in range(1, 4) if 1 + 2 * (2 * p_ + q_) * l < lim and 2 * p_ * l < lim)
    f2 = sorted((2 * (2 * p_ + q_) * l, 1 + 2 * p_ * l) for l in range(1, 4) if 2 * (2 * p_ + q_) * l < lim and 1 + 2 * p_ * l < lim)
    jl = [jj for jj in range(1, 6 * p_ + 2, 2) if (2 * jj + Fraction(jj - 1) / Af).denominator == 1 and (2 * jj + Fraction(jj - 1) / Af).numerator % 2 == 0]
    P('(3) A = %d/%d: resonances comp 1 %s = formula %s; comp 2 match %s; smooth odd orders %s = 1 + 2pl %s' % (
        p_, q_, r1[:3], r1 == f1, r2 == f2, jl[:4], jl[:3] == [1 + 2 * p_ * l for l in range(0, 3)]))

# (4)
x, y, f3, f5 = sp.symbols('x y f3 f5', positive=True)
Av = sp.Rational(10150725, 1000000)
Bv = 2 * Av + 1
Phi = lambda s: s + f3 * s**3 + f5 * s**5
rho = x**(-1 / Av) * Phi(y * x**(Bv / Av))
w, g = -Av * x, sp.diff(rho, y).subs(y, 0)
for jj in (3, 5):
    Gj = sp.diff(rho, y, jj).subs(y, 0) / sp.factorial(jj)
    qj = sp.Rational(jj - 1) / Av
    Hj = Av**qj * g**(jj + qj) * sp.Abs(w)**(-qj)
    ratio = sp.simplify(sp.powsimp(Gj / Hj, force=True))
    P('(4) j = %d: g = %s, G_j/H_j = %s (constant: the finite part of int (G_j/H_j)\' is 0; C_(0,j) = phi_j)' % (jj, sp.simplify(g), ratio))

open('verifier/early_runs/check_fred2c.log', 'w').write('\n'.join(out) + '\n')
