"""V229: own symbolic checks of item 50 (Proposition 2.2 extension, Section 9.19, Steps 15-21, preview 4394dd52).
Independent of the lead analyst's and the referee's check scripts."""
import sympy as sp, random
random.seed(3)
x, y, u, v, w, z, t, S = sp.symbols('x y u v w z t S')
l = sp.Symbol('l', positive=True); beta = 2 * l - sp.Rational(1, 2)
ok = {}
def rpoly(vars_, deg, lo=-3, hi=3):
    terms = [m for m in sp.itermonomials(vars_, deg)]
    return sum(sp.Rational(random.randint(lo, hi), random.randint(1, 3)) * m for m in terms)

# Step 7: resonant set {beta : p/2 + beta q = 1, p + q = k >= 3, beta > 0} = {1/n : n >= 3} (enumerated to k = 40)
res = set()
for k in range(3, 41):
    for p in range(k + 1):
        q = k - p
        if q > 0 and sp.Rational(p, 2) < 1: res.add((1 - sp.Rational(p, 2)) / q)
ok['Step 7 resonances (k <= 40) lie in {1/n: n>=3} and contain 1/n, 3<=n<=40'] = (
    all(b_.p == 1 and b_.q >= 3 for b_ in res) and {sp.Rational(1, n) for n in range(3, 41)} <= res)

# Step 15: T0 F' = 2(T0' - beta)F; residues of F'/F at the simple zeros r: 2 - 2 beta/T0'(r) = k, deg F = 2m
bb = sp.Rational(7, 5)
for m, roots in [(2, [3]), (3, [2, -1]), (3, [sp.Rational(1, 2), 5])]:
    T0 = bb * v * sp.prod([(1 - v / r) for r in roots])
    ks = [2 - 2 * bb / sp.diff(T0, v).subs(v, r) for r in roots]
    if all(kk.is_integer and kk >= 0 for kk in ks):
        F = sp.prod([(1 - v / r)**kk for r, kk in zip(roots, ks)])
        ok['Step 15 example m=%d roots %s: k = %s, ODE holds, deg F = 2m' % (m, roots, ks)] = (
            sp.expand(T0 * sp.diff(F, v) - 2 * (sp.diff(T0, v) - bb) * F) == 0 and sp.degree(F, v) == 2 * m)
    else:
        ok['Step 15 example m=%d roots %s: residues %s, sum = 2m' % (m, roots, ks)] = sp.simplify(sum(ks) - 2 * m) == 0
# general: (2 - k) T0'(r) = 2 beta from the (v - r)^k coefficient, T0 simple at r
a1, a2, f0, f1, r = sp.symbols('a1 a2 f0 f1 r')
okk = True
for kk in range(0, 8):
    T0g = a1 * (v - r) + a2 * (v - r)**2; Fg = (v - r)**kk * (f0 + f1 * (v - r))
    ex = sp.Poly(sp.expand((T0g * sp.diff(Fg, v) - 2 * (sp.diff(T0g, v) - beta) * Fg).subs(v, v + r)), v)
    okk &= all(ex.coeff_monomial(v**j) == 0 for j in range(kk)) and sp.expand(ex.coeff_monomial(v**kk) - f0 * ((kk - 2) * a1 + 2 * beta)) == 0
ok['Step 15 lowest coefficient f0((k-2)T0\'(r) + 2 beta), k = 0..7'] = okk

# Step 18: in (x, S), Dx = xA, DS = (1 - 2A)S/k; k div V = k x A_x - 2 S A_S + (k - 2)A + 1
for k_ in [2, 3, 4, 6]:
    b_ = sp.Rational(random.randint(1, 5), 2); g = 1 + rpoly([x], 3).subs(x, x) - rpoly([x], 0)
    g = 1 + sp.Rational(2, 3) * x - x**2 + sp.Rational(1, 4) * x**3
    Sxy = b_ * y + g
    A = rpoly([x, S], 3)
    Axy = A.subs(S, Sxy)
    V1 = x * Axy; DS = (1 - 2 * Axy) * Sxy / k_
    V2 = (DS - sp.diff(g, x) * V1) / b_
    divxy = sp.expand(sp.diff(V1, x) + sp.diff(V2, y))
    form = sp.expand(((k_ * x * sp.diff(A, x) - 2 * S * sp.diff(A, S) + (k_ - 2) * A + 1) / k_).subs(S, Sxy))
    ok['Step 18 divergence formula k=%d' % k_] = sp.expand(divxy - form) == 0
    # density equation D(x^2 S^k) = x^2 S^k
    rho = x**2 * Sxy**k_
    ok['Step 18 transport identity k=%d' % k_] = sp.expand(V1 * sp.diff(rho, x) + V2 * sp.diff(rho, y) - rho) == 0
# kernel solution and the degree count for k = 2m
for m_, d_, n_ in [(2, 2, 0), (2, 2, 1), (2, 3, 2), (3, 2, 1), (2, 2, 3)]:
    lv = sp.Rational(7, 10); bv = 2 * lv - sp.Rational(1, 2); k_ = 2 * m_
    C = (4 * m_ * lv - 1) / (2 * m_ - 2)
    Hc = [1 - C - sp.Rational(1, 2)] + [sp.Rational(random.randint(1, 4), 3) for _ in range(n_)]
    Hc[0] = sp.Rational(1, 2) - C
    zz = sp.Symbol('zz'); H = sum(c * zz**i for i, c in enumerate(Hc))
    A = C + S**(m_ - 1) * H.subs(zz, x * S**m_)
    ok['Step 18 H(0) = -m beta/(m-1) (m=%d)' % m_] = sp.simplify(Hc[0] + m_ * bv / (m_ - 1)) == 0
    opA = sp.expand(k_ * x * sp.diff(A, x) - 2 * S * sp.diff(A, S) + (k_ - 2) * A)
    ok['Step 18 kernel solution solves div = 2l (m=%d n=%d)' % (m_, n_)] = sp.expand(opA - (2 * k_ * lv - 1)) == 0
    ok['Step 18 A(0,1) = 1/2 (m=%d n=%d)' % (m_, n_)] = A.subs({x: 0, S: 1}) == sp.Rational(1, 2)
    g = 1 + x + sp.Rational(3, 2) * x**d_; b_ = 2; Sxy = b_ * y + g
    Axy = sp.expand(A.subs(S, Sxy)); V1 = sp.expand(x * Axy)
    V2 = sp.expand(((1 - 2 * Axy) * Sxy / k_ - sp.diff(g, x) * V1) / b_)
    curl = sp.expand(sp.diff(V2, x) - sp.diff(V1, y)); rhox = sp.expand(sp.diff(x**2 * Sxy**k_, x))
    pred = (m_ * d_ + 1) * n_ + m_ * d_ - 1
    ok['Step 18 deg curl V = (md+1)n+md-1 = %d, deg rho_x = 2md+1 = %d (m=%d d=%d n=%d)' % (pred, 2 * m_ * d_ + 1, m_, d_, n_)] = (
        sp.Poly(curl, x, y).total_degree() == pred and sp.Poly(rhox, x, y).total_degree() == 2 * m_ * d_ + 1)
    ok['  (md+1)n = md+2 has no integer n (m=%d d=%d)' % (m_, d_)] = sp.Rational(m_ * d_ + 2, m_ * d_ + 1).q != 1

# Step 20: rho = u^2 (1 + u w), Du = uA, Dw = Y with A = 1/2 + uB, Y = -2B - w/2 - 3uwB (constant Jacobian coordinates)
B = rpoly([u, w], 3)
A = sp.Rational(1, 2) + u * B; Y = -2 * B - w / 2 - 3 * u * w * B
rho = u**2 * (1 + u * w)
ok['Step 20 transport identity'] = sp.expand(u * A * sp.diff(rho, u) + Y * sp.diff(rho, w) - rho) == 0
div = sp.expand(sp.diff(u * A, u) + sp.diff(Y, w))
ok['Step 20 divergence = u^2 B_u - uB - (2 + 3uw)B_w'] = sp.expand(div - (u**2 * sp.diff(B, u) - u * B - (2 + 3 * u * w) * sp.diff(B, w))) == 0
Hz = rpoly([z], 4); Bw = w * Hz.subs(z, u * w)
opB = sp.expand(u**2 * sp.diff(Bw, u) - u * Bw - (2 + 3 * u * w) * sp.diff(Bw, w))
ok['Step 20 weight -1 part: operator = -2 (z(z+1)H)\''] = sp.expand(opB - (-2 * sp.diff(z * (z + 1) * Hz, z)).subs(z, u * w)) == 0
# weights: each term raises weight by one
mon = u**3 * w**5
for term in [u**2 * sp.diff(mon, u), u * mon, sp.diff(mon, w), u * w * sp.diff(mon, w)]:
    pw = sp.Poly(term, u, w).monoms()[0]
    ok.setdefault('Step 20 weight raised by one', True); ok['Step 20 weight raised by one'] &= (pw[0] - pw[1]) == (3 - 5 + 1)

# Step 21 (kappa != 0): coefficients in t (t = x, v = 1 + b0 y, K = b0^2)
kap, al, de, Cc, b0, M_ = sp.symbols('kappa alpha delta C b0 M')
q = sp.Function('q')
s_ = al * v + de
f4 = kap**2 * v; f3 = 2 * kap * s_ * v
# top coefficient t^(M'+3): M' q f4' - 4 q' f4 -> M' q = 4 v q'
qq = sp.Function('qq')(v)
ok['Step 21 top bracket coefficient'] = sp.simplify((M_ * qq * sp.diff(f4, v) - 4 * sp.diff(qq, v) * f4) / kap**2 - (M_ * qq - 4 * v * sp.diff(qq, v))) == 0
c0, c1 = sp.symbols('c0 c1')
sol = sp.solve(sp.Poly(sp.expand(M_ * (c0 + c1 * v) - 4 * v * c1), v).coeffs(), [c0, c1], dict=True)
ok['Step 21 deg<=1 solutions of M q = 4 v q\' need M = 4 or q = 0'] = all(s.get(c0, c0) == 0 for s in sol)
# t^6 coefficient with q4 = C v and general cubic q3
q30, q31, q32, q33 = sp.symbols('q30:34'); q3 = q30 + q31 * v + q32 * v**2 + q33 * v**3; q4 = Cc * v
c6 = 4 * q4 * sp.diff(f3, v) - 3 * sp.diff(q4, v) * f3 + 3 * q3 * sp.diff(f4, v) - 4 * sp.diff(q3, v) * f4
ok['Step 21 t^6 identity: 4 v q3\' - 3 q3 = (C/kappa)(10 alpha v^2 + 2 delta v)'] = sp.expand(
    -c6 / kap**2 - (4 * v * sp.diff(q3, v) - 3 * q3 - (Cc / kap) * (10 * al * v**2 + 2 * de * v))) == 0
# direct check of the t^6 coefficient from the full bracket: psi = q3 t^3 + q4 t^4 + ..., rho = f4 t^4 + f3 t^3 + ...
rho_t = f4 * t**4 + f3 * t**3; psi_t = q3 * t**3 + q4 * t**4
br = sp.expand(sp.diff(psi_t, t) * sp.diff(rho_t, v) - sp.diff(psi_t, v) * sp.diff(rho_t, t))
ok['Step 21 t^6 coefficient of {psi, rho}_(t,v)'] = sp.expand(sp.Poly(br, t).coeff_monomial(t**6) - c6) == 0
# Poisson coefficient of t^3: rho_x = d_t rho (t = x) -> 4 f4 t^3
ok['Step 21 x^3 Poisson coefficient: 4 kappa^2 v'] = sp.expand(sp.Poly(sp.diff(rho_t, t), t).coeff_monomial(t**3) - 4 * kap**2 * v) == 0
# Laurent case: P = v w + c, area form v^-1 dP dv: div in (w, v) equals d_P(DP) + d_v(Dv) - Dv/v
cc = sp.Symbol('c', nonzero=True)
Vw = rpoly([w, v], 2); Vv = rpoly([w, v], 2)
div_wv = sp.diff(Vw, w) + sp.diff(Vv, v)
Pp = sp.Symbol('Pp')
DP = sp.expand(v * Vw + w * Vv)            # D(vw + c)
subsw = {w: (Pp - cc) / v}
DPpv = sp.simplify(DP.subs(subsw)); Dvpv = sp.simplify(Vv.subs(subsw))
div_pv = sp.diff(DPpv, Pp) + sp.diff(Dvpv, v) - Dvpv / v
ok['Step 21 divergence in (P, v) with area form v^-1 dP dv'] = sp.simplify(div_pv - div_wv.subs(subsw)) == 0
# Laurent ODE Y' - (3/2)Y/v = beta: only Y = -2 beta v
ys = sp.symbols('yy0:7'); Yl = sum(c * v**j for c, j in zip(ys, range(-3, 4)))
eqs = sp.Poly(sp.expand((sp.diff(Yl, v) - sp.Rational(3, 2) * Yl / v - beta) * v**4), v).coeffs()
ss = sp.solve(eqs, ys, dict=True)
ok['Step 21 Laurent solution Y = -2 beta v'] = len(ss) == 1 and sp.simplify(Yl.subs(ss[0]) + 2 * beta * v) == 0
# s constant case: 1 - a(0,v) - 2 v a'(0,v) = 2l has only the constant solution 1 - 2l
as_ = sp.symbols('a0:5'); ap = sum(c * v**j for j, c in enumerate(as_))
ss = sp.solve(sp.Poly(sp.expand(1 - ap - 2 * v * sp.diff(ap, v) - 2 * l), v).coeffs(), as_, dict=True)
ok['Step 21 a_1(0,v) = 1 - 2l'] = len(ss) == 1 and sp.simplify(ap.subs(ss[0]) - (1 - 2 * l)) == 0
# Step 2.2 statement: l > 5/12 iff beta > 1/3 (so NR holds)
ok['l > 5/12 <=> beta > 1/3'] = sp.solve(beta - sp.Rational(1, 3), l) == [sp.Rational(5, 12)]
for kk_, vv in ok.items(): print('%-100s %s' % (kk_, vv))
print('ALL PASS' if all(ok.values()) else 'FAILURES')
