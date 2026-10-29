"""Lead check of the referee's leading-jet recursion at a T1 source (S1 at the origin, class E):
first nonconstant q terms of degree 2m, phi deviation of degree 2m + 1. Checks m = 1, 2, 3 against
a_j = K n_j p_j / d_j, p_{j+1} = -n_j (n_j - 1)/(4 (j + 1)(j + 2)) (1 + K^2/d_j^2) p_j,
n_j = 2m + 1 - 2j, d_j = eps j + delta (m - j), eps = c - 1/2, delta = c + 1, and the sign rule."""
import sympy as sp, json, time
t0 = time.time()
s, z, c, K, lam = sp.symbols('s z c K lam')
eps = c - sp.Rational(1, 2); delta = c + 1
def wpart(expr, d):
    e = sp.expand(expr.subs({s: lam**2*s, z: lam*z}))
    return sp.expand(e.coeff(lam, d))
out = {}
for m in (1, 2, 3):
    p = sp.symbols(f'p0:{m + 1}'); a = sp.symbols(f'a0:{m + 1}')
    Phi = z/2 + sum(p[j]*s**j*z**(2*m + 1 - 2*j) for j in range(m + 1))
    Q = K + sum(a[j]*s**j*z**(2*m - 2*j) for j in range(m + 1))
    eta = -(4*s*sp.diff(Phi, s, 2) + 8*sp.diff(Phi, s) + sp.diff(Phi, z, 2))
    Pz = sp.diff(Phi, z); Ps = sp.diff(Phi, s)
    Wsd = 2*s*(c - Pz); Wz = c*z + 2*Phi + 2*s*Ps
    Rq = sp.expand(Q + Wsd*sp.diff(Q, s) + Wz*sp.diff(Q, z) - 2*Pz*Q)
    Re = sp.expand((1 + c)*eta + Wsd*sp.diff(eta, s) + Wz*sp.diff(eta, z) - 2*Q*sp.diff(Q, z))
    eqs = sp.Poly(wpart(Rq, 2*m), s, z).coeffs() + sp.Poly(wpart(Re, 2*m - 1), s, z).coeffs()
    unk = list(p[1:]) + list(a)
    sol = sp.solve(eqs, unk, dict=True); assert len(sol) == 1; sol = sol[0]; sol[p[0]] = p[0]
    ok = True
    for j in range(m + 1):
        n = 2*m + 1 - 2*j; d = eps*j + delta*(m - j)
        ok &= sp.simplify(sol[a[j]] - K*n*sol[p[j]]/d) == 0
        if j < m:
            ok &= sp.simplify(sol[p[j + 1]] + sp.Rational(n*(n - 1), 4*(j + 1)*(j + 2))*(1 + K**2/d**2)*sol[p[j]]) == 0
    sign_ratio = sp.simplify(sol[a[m]]/sol[a[0]])
    num = float(sign_ratio.subs({c: sp.Rational(3, 5), K: 1}))
    out[f'm={m}'] = {'recursion_matches': bool(ok), 'a_m/a_0 at c=3/5,K=1': num,
                     'sign(a_m/a_0) == (-1)^m': (num > 0) == (m % 2 == 0)}
out['seconds'] = round(time.time() - t0, 1)
print(json.dumps(out, indent=1)); json.dump(out, open('t1_jet_recursion_check_output.json', 'w'), indent=1)
