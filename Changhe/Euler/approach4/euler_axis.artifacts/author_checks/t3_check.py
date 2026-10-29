"""Lead check of the T3 referee claims (referee answer 't3', 2026-10-28T21:03Z).
(A) saddle jets (4): phi = -(1+2c)/2 z + h z^3 + p s z, q = Q z^2 + a4 z^4 + b4 s z^2, eta = -Delta_5 phi;
(B) equatorial normal ODEs and the identity E = (K gamma/delta) A/(c - f);
(C) S1 source jets at z0 = 1 with h2 != 0 and the general curvature identity (8);
(D) the even saddle resonances inside (1/2, 3/4) by weight."""
import sympy as sp, json, time
from fractions import Fraction
t0 = time.time()
s, z, x, c, K, Q, h, p, a4, b4 = sp.symbols('s z x c K Q h p a4 b4')
d = 1 + c; gam = 1 + 4*c; eps = c - sp.Rational(1, 2)
L5 = lambda f, zz: 4*s*sp.diff(f, s, 2) + 8*sp.diff(f, s) + sp.diff(f, zz, 2)
def Rq(P, q, zz, zc): return sp.expand(q + 2*s*(c - sp.diff(P, zz))*sp.diff(q, s) + (c*zc + 2*P + 2*s*sp.diff(P, s))*sp.diff(q, zz) - 2*sp.diff(P, zz)*q)
def Re(P, q, e, zz, zc): return sp.expand(d*e + 2*s*(c - sp.diff(P, zz))*sp.diff(e, s) + (c*zc + 2*P + 2*s*sp.diff(P, s))*sp.diff(e, zz) - 2*q*sp.diff(q, zz))
def wpart(expr, var, wmax):
    P_ = sp.Poly(sp.expand(expr), s, var)
    return [(i, j, sp.factor(co)) for (i, j), co in P_.terms() if 2*i + j <= wmax]
res = {}
# (A) saddle jets
P = -(1 + 2*c)/2*z + h*z**3 + p*s*z
q = Q*z**2 + a4*z**4 + b4*s*z**2
e = -L5(P, z)
res['A_e'] = str(sp.factor(e))  # = -(6h + 8p) z
rq = wpart(Rq(P, q, z, z), z, 4)
sol = sp.solve([co for (_, _, co) in rq], [a4, b4], dict=True)
res['A_a4_b4'] = str(sol)
ee = sp.Symbol('ee')
psol = sp.solve(sp.Eq(-(6*h + 8*p), ee), p)[0]
res['A_p_matches'] = sp.simplify(psol + (ee + 6*h)/8) == 0
res['A_a4_matches'] = sp.simplify(sol[0][a4] + Q*h/d) == 0
res['A_b4_matches'] = sp.simplify(sol[0][b4] + 6*Q*p/gam) == 0
# (B) equatorial ODEs
f, g, A, E = [sp.Function(n)(s) for n in ('f', 'g', 'A', 'E')]
PB = z*f + z**3*g; qB = z**2*A; eB = z*E
res['B_q_z2'] = sp.simplify(sp.expand(Rq(PB, qB, z, z)).coeff(z, 2) - (2*s*(c - f)*sp.diff(A, s) + (1 + 2*c + 2*f + 4*s*sp.diff(f, s))*A)) == 0
res['B_e_z1'] = sp.simplify(sp.expand(Re(PB, qB, eB, z, z)).coeff(z, 1) - (2*s*(c - f)*sp.diff(E, s) + (1 + 2*c + 2*f + 2*s*sp.diff(f, s))*E)) == 0
# identity: d/ds log(E (c - f)/A) = 0 given the two ODEs
Ap = -(1 + 2*c + 2*f + 4*s*sp.diff(f, s))*A/(2*s*(c - f))
Ep = -(1 + 2*c + 2*f + 2*s*sp.diff(f, s))*E/(2*s*(c - f))
expr = (Ep/E) - (Ap/A) - sp.diff(f, s)/(c - f)
res['B_identity'] = sp.simplify(expr) == 0
res['B_constant_at_0'] = str(sp.simplify((2*K*Q/d)*(c + (1 + 2*c)/2)/Q))  # should be K gamma/delta
# (C) S1 source at z = 1 (x = z - 1), general h2
h2, p2, h3, p3, a1, b2, d2 = sp.symbols('h2 p2 h3 p3 a1 b2 d2')
Pc = -c/2 + x/2 + h2*x**2 + p2*s + h3*x**3 + p3*s*x
qc = K + a1*x + b2*x**2 + d2*s
ec = -L5(Pc, x)
zc = 1 + x
eqs = [co for (_, _, co) in wpart(Rq(Pc, qc, x, zc), x, 2)] + [co for (_, _, co) in wpart(Re(Pc, qc, ec, x, zc), x, 1)]
# Poisson: eta has no free part here; eta jets come from phi. Solve for (a1, b2, d2, p2, p3).
solc = sp.solve(eqs, [a1, b2, d2, p2, p3], dict=True)
res['C_n_solutions'] = len(solc)
if solc:
    S = solc[0]
    res['C_a1'] = sp.simplify(S[a1] - 4*K*h2/d) == 0
    res['C_p2'] = sp.simplify(S[p2] + h2*(sp.Rational(1, 4) + K**2/d**2)) == 0
    res['C_eta01'] = sp.simplify(ec.subs(S).subs({s: 0, x: 0}) - 8*K**2*h2/d**2) == 0
    res['C_b2'] = sp.simplify(S[b2] - K*(3*d*h3 + 4*h2**2)/d**2) == 0
    res['C_p3'] = sp.simplify(S[p3] + 3*(d*(K**2 + d**2)*h3 + 4*K**2*h2**2)/(4*d**3)) == 0
    res['C_d2'] = sp.simplify(S[d2] - K*(-3*d*(K**2 + d**2)*h3 + (20*K**2 + 8*d**2)*h2**2)/(2*d**3*(2*c - 1))) == 0
    qz, qzz, qrr = S[a1], 2*S[b2], 2*S[d2]
    res['C_curvature_identity'] = sp.simplify(4*eps*d*qrr + (d**2 + K**2)*qzz - 3*(d**2 + 2*K**2)/(2*K)*qz**2) == 0
# (D) even resonances (b - 2)(1 + c) = a (1 + 4c), q even (b even), c in (1/2, 3/4)
found = []
for a_ in range(1, 20):
    for b_ in range(0, 60, 2):
        if b_ - 2 - 4*a_ == 0: continue
        cc = Fraction(a_ - (b_ - 2), (b_ - 2) - 4*a_)
        if Fraction(1, 2) < cc < Fraction(3, 4):
            found.append((2*a_ + b_, a_, b_, str(cc)))
found.sort()
res['D_first_even_resonances'] = found[:5]
res['seconds'] = round(time.time() - t0, 2)
print(json.dumps(res, indent=1, default=str))
json.dump(res, open('author_checks/t3_check_output.json', 'w'), indent=1, default=str)
