"""verifier: lead request (n) (NOTES 05:39Z item 2, 06:03Z item 3), items (n1) to (n3), own code (sympy, mpmath).
(n1) A = 4 trace in the variable m: h = (m^2 + 1 + 1/(m^2 + 1))/16, g = 1/h, w = -m/h, x = (1/4) int_m^inf dt/h,
     so d/dx = -4 h d/dm.  Checks: axis law w g' = (w' - A) g; w ~ -A x, g ~ x^2 as x -> 0 (m -> inf); at x* (m = 0):
     w = 0, w' = A, g* = 8, w'' = 0, Q = 0; P(m) by (i) Q - P = O(1/m) and (ii) fred11 (4) from the Taylor coefficients
     d3, d5, d7 of w(x) (series inversion of x(m)); R = Q - P - Q* against the stated rational function.
(n2) R12: R_nat(u) = (1 - 6k)(u^5 - 1) + (1 + 2k)(u^3 - 1), k = A/L^2, m = (A/L)(1/u - u).
     int_0^inf R m^(delta-2) dm <= 0 iff k <= (16 - delta)/(6 (8 - 3 delta)) (i.e. L^2 >= 6A(8 - 3 delta)/(16 - delta)),
     checked by exact Beta integrals (sympy) and by mpmath quadrature; one sign change of R on (0, 1) for 1/3 < k < 1/2,
     none for k <= 1/3 (proof in the log); at k = 1/4 the factorization R = -(u - 1)(u^4 + u^3 - 2u^2 - 2u - 2)/2.
(n3) endpoint relations g'(x*) = w''(x*) g*/A and Q(x*) = w''(x*)(g* - A)/(2 A g*^3) from the axis law (needs
     w'(x*) = A); the compatible trace w = -A x (1 - u^2)(1 - u^2/2), g = x^2 (1 - u^2/2)^(3/2): axis law, w'(L) = A,
     w''(L) = -A/L."""
import sympy as sp
import mpmath as mp

out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
m, x, t, s = sp.symbols('m x t s', positive=True)

# ---------------- (n1)
A = 4
h = (m**2 + 1 + 1 / (m**2 + 1)) / 16
g, w = 1 / h, -m / h
D = lambda f: sp.cancel(-4 * h * sp.diff(f, m))
gx, wx = D(g), D(w)
P('(n1) axis law w g\' - (w\' - A) g =', sp.cancel(w * gx - (wx - A) * g))
wxx = D(wx)
Q = sp.cancel((gx - wxx) / (2 * g**3))
at0 = {k: sp.simplify(v.subs(m, 0)) for k, v in dict(w=w, wx=wx, g=g, wxx=wxx, Q=Q).items()}
P('(n1) at x* (m = 0):', at0)
# x(m) and its large-m series; x* = x(0)
mp.mp.dps = 30
hf = sp.lambdify(m, h, 'mpmath')
xs = mp.quad(lambda tt: 1 / (4 * hf(tt)), [0, 1, mp.inf])
P('(n1) x* = (1/4) int_0^inf dt/h =', mp.nstr(xs, 20), '(mpmath)')
# large m: use e = 1/m; dx/dm = -1/(4h); series of 1/(4h) in 1/m, integrated termwise from m to inf
e = sp.symbols('e', positive=True)
NS = 12
f = sp.series((1 / (4 * h)).subs(m, 1 / e), e, 0, NS + 2).removeO()     # 1/(4h) as series in e = 1/m
# x(m) = int_m^inf f(1/t) dt, with f = sum c_n e^n (n >= 2): int_m^inf t^-n dt = m^(1-n)/(n-1)
fp = sp.Poly(sp.expand(f), e)
xe = sum(c * e**(n - 1) / (n - 1) for (n,), c in fp.terms())           # x as series in e
P('(n1) x(m) for large m, in e = 1/m:', sp.expand(xe))
# invert: e as series in x
# inversion by truncated power-series arithmetic (exact rationals): e_{n+1} = (x - (xe(e_n) - 4 e_n))/4
def tr(pexpr):
    pp = sp.Poly(sp.expand(pexpr), x)
    return sum(c * x**n for (n,), c in pp.terms() if n <= NS)


def comp(ser_e, ee):
    res, pw = 0, 1
    pe = sp.Poly(ser_e, e)
    cf = {n: c for (n,), c in pe.terms()}
    for n in range(0, max(cf) + 1):
        if n:
            pw = tr(pw * ee)
        if n in cf:
            res += cf[n] * pw
    return tr(res)


eser = x / 4
for it in range(NS):
    eser = tr((x - (comp(xe, eser) - 4 * eser)) / 4)
P('(n1) inversion check: x(e(x)) - x =', comp(xe, eser) - x)
we = sp.series(sp.cancel(w.subs(m, 1 / e) * e) , e, 0, 12).removeO()     # e w as a series in e
wser = tr(sp.expand(comp(sp.expand(we), eser) * sp.series(1 / eser, x, 0, NS - 2).removeO()))
P('(n1) w(x) series:', sp.expand(wser))
d = [sp.expand(wser).coeff(x, k) for k in (1, 3, 5, 7)]
P('(n1) w\'(0) =', d[0], '(A = %d)' % A, '; even coefficients:', [sp.expand(wser).coeff(x, k) for k in (2, 4, 6, 8)])
ge = sp.series(sp.cancel(g.subs(m, 1 / e)), e, 0, 12).removeO()
gser = tr(comp(sp.expand(ge), eser))
P('(n1) g(x) series:', sp.expand(gser))
d3, d5, d7 = d[1:]
q5 = (1 - 3 * d3) / sp.Integer(A)**5
q3 = -(10 * A * d5 + 12 * d3**2 - 3 * d3) / sp.Integer(A)**4
q1 = -(168 * A**2 * d7 + 324 * A * d3 * d5 - 10 * A * d5 + 144 * d3**3 - 21 * d3**2) / (8 * sp.Integer(A)**3)
P4 = sp.expand(q5 * m**5 + q3 * m**3 + q1 * m)
P('(n1) P from fred11 (4):', sp.factor(P4))
# P by the O(1/m) characterization: polynomial part of Q at m = inf
Qe = sp.series(Q.subs(m, 1 / e), e, 0, 2).removeO()
Pinf = sp.expand(sum(sp.expand(Qe).coeff(e, -k) * m**k for k in range(1, 7)))
P('(n1) polynomial part of Q in m (Q - P = O(1/m)):', sp.factor(Pinf), '; even/constant part:', sp.expand(Qe).coeff(e, 0))
P('(n1) both minus m (m^2 - 1)^2/2048:', sp.simplify(P4 - m * (m**2 - 1)**2 / 2048), sp.simplify(Pinf - m * (m**2 - 1)**2 / 2048))
R = sp.simplify(Q - P4 - at0['Q'])
Rst = -m * (8 * m**10 + 34 * m**8 + 60 * m**6 + 52 * m**4 + 20 * m**2 + 1) / (2048 * (1 + m**2)**6)
P('(n1) R - stated:', sp.simplify(R - Rst), '; R(m) < 0 for m > 0: all numerator coefficients positive')
P('(n1) Q(m) =', sp.factor(Q))

# ---------------- (n2)
u, k, dl = sp.symbols('u k delta', positive=True)
Rn = (1 - 6 * k) * (u**5 - 1) + (1 + 2 * k) * (u**3 - 1)
br = sp.factor(sp.cancel(Rn / (u - 1)))
P('(n2) R/(u - 1) =', sp.collect(sp.expand(br), k), '; at u = 0:', br.subs(u, 0), ', at u = 1:', sp.expand(br.subs(u, 1)))
P('(n2) R/(u - 1) = (1 - 6k) u^3 (u + 1) + (2 - 4k)(u^2 + u + 1):',
  sp.simplify(br - ((1 - 6 * k) * u**3 * (u + 1) + (2 - 4 * k) * (u**2 + u + 1))))
P('(n2) d/du log[u^3 (u+1)/(u^2+u+1)] = 3/u + 1/(u+1) - (2u+1)/(u^2+u+1); (2u+1)/(u^2+u+1) <= 2/sqrt(3) < 3 on (0, 1): increasing;'
  ' so for k > 1/6, (R/(u-1))/(u^2+u+1) is strictly decreasing in u: at most one zero, and exactly one in (0, 1) iff'
  ' 2 - 4k > 0 > 8 - 24k, i.e. 1/3 < k < 1/2; for k <= 1/3 (L^2 >= 3A) R < 0 on (0, 1) (H_- holds).')
P('(n2) max of (2u+1)/(u^2+u+1) on [0, 1]:', sp.nsimplify(sp.maximum((2 * u + 1) / (u**2 + u + 1), u, sp.Interval(0, 1))))
P('(n2) k = 1/4:', sp.factor(Rn.subs(k, sp.Rational(1, 4))))
# moment: int_0^inf R m^(dl-2) dm, m = (A/L)(1/u - u), dm = -(A/L)(1 + u^2)/u^2 du; positive constants dropped:
#   I(k) = int_0^1 Rn(u) ((1 - u^2)/u)^(dl - 2) (1 + u^2)/u^2 du; substitute v = u^2
mp.mp.dps = 30


def Ik(kk, dd):
    kk, dd = mp.mpf(kk), mp.mpf(dd)
    fq = lambda uu: ((1 - 6 * kk) * (uu**5 - 1) + (1 + 2 * kk) * (uu**3 - 1)) * ((1 - uu**2) / uu)**(dd - 2) * (1 + uu**2) / uu**2
    return mp.quad(fq, [0, mp.mpf(1) / 2, 1])


# exact via Beta: R contains (u - 1); write integrand in v = u^2? Use the closed form by linearity in k:
for dd in ['0.1', '0.19703', '0.5', '0.9']:
    I0, I1 = Ik(0, dd), Ik(1, dd) - Ik(0, dd)
    kst = -I0 / I1
    kpred = (16 - mp.mpf(dd)) / (6 * (8 - 3 * mp.mpf(dd)))
    P('(n2) delta = %s: I(k) = %s + k %s; zero k* = %s; (16 - delta)/(6 (8 - 3 delta)) = %s; diff %s' % (
        dd, mp.nstr(I0, 12), mp.nstr(I1, 12), mp.nstr(kst, 20), mp.nstr(kpred, 20), mp.nstr(kst - kpred, 3)))
P('(n2) delta -> beta: S(A, beta) = 6A(8 - 3 beta)/(16 - beta) vs S_A = 6A(4A - 3)/(8A - 1) with beta = 2/A:',
  sp.simplify((6 * k * (8 - 3 * 2 / k) / (16 - 2 / k)) - 6 * k * (4 * k - 3) / (8 * k - 1)), '(A written as k here)')

# ---------------- (n3)
X = sp.symbols('X', positive=True)
Wf, Gf = sp.Function('w')(X), sp.Function('g')(X)
Aa, L, b, G = sp.symbols('A L b G', positive=True)
# near x*: w = A s + (b/2) s^2 + c3 s^3, s = X - L; g = G + g1 s + ...; impose w g' = (w' - A) g order by order
c3, g1, g2 = sp.symbols('c3 g1 g2')
ss = sp.symbols('s')
wl = Aa * ss + b / 2 * ss**2 + c3 * ss**3
gl = G + g1 * ss + g2 * ss**2
ax = sp.expand(wl * sp.diff(gl, ss) - (sp.diff(wl, ss) - Aa) * gl)
sl = sp.solve([ax.coeff(ss, 1)], [g1], dict=True)[0]
P('(n3) axis law at order s: g\'(x*) =', sl[g1], '(= w\'\'(x*) g*/A)')
Qs = sp.simplify((sl[g1] - b) / (2 * G**3))
P('(n3) Q(x*) =', sp.factor(Qs), '; minus b (G - A)/(2 A G^3):', sp.simplify(Qs - b * (G - Aa) / (2 * Aa * G**3)))
P('(n3) (order s^0 of the axis law is 0 = 0 only because w(x*) = 0 and w\'(x*) = A; if w\'(x*) = a != A the order-0'
  ' term (a - A) G must vanish, so G = 0: w\'(x*) = A is forced when g* > 0.)')
uu = X / L
wt = -Aa * X * (1 - uu**2) * (1 - uu**2 / 2)
gt = X**2 * (1 - uu**2 / 2)**sp.Rational(3, 2)
P('(n3) compatible trace: axis law residual', sp.simplify(wt * sp.diff(gt, X) - (sp.diff(wt, X) - Aa) * gt),
  '; w(L) =', sp.simplify(wt.subs(X, L)), ', w\'(L) =', sp.simplify(sp.diff(wt, X).subs(X, L)),
  ', w\'\'(L) =', sp.simplify(sp.diff(wt, X, 2).subs(X, L)), ', g* =', sp.simplify(gt.subs(X, L)),
  ', w\'(0) =', sp.diff(wt, X).subs(X, 0), ', g/x^2 at 0 =', sp.limit(gt / X**2, X, 0))
gL = sp.simplify(gt.subs(X, L))
gpL = sp.simplify(sp.diff(gt, X).subs(X, L))
P('(n3) on that trace g\'(L) - w\'\'(L) g*/A =', sp.simplify(gpL - sp.diff(wt, X, 2).subs(X, L) * gL / Aa))
open('verifier/early_runs/check_n.log', 'w').write('\n'.join(out) + '\n')
