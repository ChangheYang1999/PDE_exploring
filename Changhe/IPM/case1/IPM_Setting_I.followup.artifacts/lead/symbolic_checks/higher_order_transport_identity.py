# Lead check of the referee's identity (3.4): residual identity for K_n, n = 2, 4, 6, without imposing the equations.
import sympy as S, sys
s, y = S.symbols("s y")
a, b, f = [S.Function(t)(s, y) for t in ("a", "b", "f")]
D = lambda v: a*S.diff(v, s) + b*S.diff(v, y)
E = D(f) - f
V = S.diff(a, s) + S.diff(b, y)
for n in [int(t) for t in sys.argv[1:]]:
    u = S.diff(f, y)/a
    K = S.diff(f, y, n) - u*S.diff(a, y, n-1)
    F = (S.diff(a, y)*S.diff(a, y, n-1)/a - S.diff(a, y, n))*(S.diff(f, s) + b*u)
    F -= sum(S.binomial(n, k)*S.diff(a, y, k)*S.diff(f, s, 1, y, n-k) for k in range(1, n))
    F -= sum(S.binomial(n, k)*S.diff(b, y, k)*S.diff(f, y, n+1-k) for k in range(2, n))
    F += (S.diff(a, s) - (n-1)*S.diff(b, y))*u*S.diff(a, y, n-1)
    rhs = S.diff(E, y, n) - S.diff(a, y, n-1)*S.diff(E, y)/a - S.diff(f, y)*S.diff(V, y, n-1)
    res = S.simplify(S.expand((D(K) + (n*S.diff(b, y) - 1)*K - F - rhs)*a))
    print(n, 'residual*a =', res, flush=True)
