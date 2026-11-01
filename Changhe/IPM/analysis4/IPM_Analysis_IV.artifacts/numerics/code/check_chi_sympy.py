"""Direct substitution check: build chi = sum_{n<=N} r^{p_n+3} C_n(theta) from the recursion output (exact rationals),
compute rho = -d_y Delta chi, psi = chi_xy, u = (-psi_y, psi_x) with sympy via the polar chain rule, and verify that
the stationary residual (c_l X + u).grad rho - rho has vanishing coefficient at every exponent p_n, n <= N.
Independent of the Fourier bookkeeping of ffcore.products / poisson: only the coefficient lists C_n are shared."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
import sympy as sp

def run(cl_str, f1, N, label):
    t0 = time.time()
    R = RingQ(); ff = FarField(R, cl_str, [R.scalar(x) for x in f1])
    for n in range(2, N + 1): ff.step()
    cl = sp.Rational(cl_str); gamma = 1 / cl; delta = 1 - gamma
    q = sp.fraction(delta)[1]                         # delta = num/q ; use r = s^q so that r^{p_n} = s^{q - num n}
    s, th = sp.symbols('s theta', positive=True)
    r = s ** q
    def pn(n): return 1 - n * delta
    chi = 0
    for n in range(1, N + 1):
        c = ff.chi_coeffs(n)
        Cn = sum(sp.Rational(str(x)) * sp.cos(2 * m * th) for m, x in enumerate(c))
        chi += r ** (pn(n) + 3) * Cn
    # Cartesian derivatives via polar chain rule, with d/dr = (1/(q s^{q-1})) d/ds
    def dr(e): return sp.diff(e, s) / (q * s ** (q - 1))
    def dx(e): return sp.cos(th) * dr(e) - sp.sin(th) / r * sp.diff(e, th)
    def dy(e): return sp.sin(th) * dr(e) + sp.cos(th) / r * sp.diff(e, th)
    lap = lambda e: dx(dx(e)) + dy(dy(e))
    rho = -dy(lap(chi))
    psi = dx(dy(chi))
    ux, uy = -dy(psi), dx(psi)
    X_grad = cl * (r * sp.cos(th) * dx(rho) + r * sp.sin(th) * dy(rho))
    Res = X_grad + ux * dx(rho) + uy * dy(rho) - rho
    Res = sp.expand(Res)
    # collect powers of s
    Res = sp.expand(Res.rewrite(sp.exp))              # trig -> exponentials, exact Laurent polynomial in exp(i theta)
    P = sp.Poly(sp.expand(Res * s ** (10 * q * N)), s)   # shift to make exponents nonnegative integers
    terms = P.terms()
    # map exponents back: coefficient of s^e corresponds to r^{(e - 10 q N)/q}
    out = {}
    for (e,), coef in terms:
        rexp = sp.Rational(e - 10 * q * N, q)
        c2 = sp.simplify(coef)
        if c2 != 0: out[rexp] = c2
    exps_expected = sorted(out.keys())
    print(f'[{label}] c_l={cl_str} f1={f1} N={N}: nonzero residual exponents: {[str(e) for e in exps_expected][:12]}  (time {time.time()-t0:.1f}s)')
    ok = True
    for n in range(1, N + 1):
        e = pn(n)
        if e in out: ok = False; print(f'   FAIL: residual at r^{{p_{n}}} = r^{e} nonzero: {sp.N(out[e], 8)}')
    first = min(out.keys()) if out else None
    print(f'   all orders 1..{N} vanish: {ok}; first surviving exponent {first} (p_{N+1} = {pn(N+1)})  [exponents present: {sorted(set(float(e) for e in out))[-6:]}]')
    # cross-check: the first surviving sector must equal (N)(c_l-1) f_{N+1} ... i.e. forcing of order N+1
    ff.step(); fN1 = ff.f[N + 1]
    # residual sector at p_{N+1} is  -(N)(c_l - 1) f_{N+1}... check sign and value numerically at a few theta
    import mpmath
    e = pn(N + 1)
    if e in out:
        expr = out[e]; fn = sp.lambdify(th, expr, 'mpmath')
        thv = [0.3, 0.9, 1.7]
        vals = [complex(fn(t)) for t in thv]
        fv = [sum(float(x) * math.sin((2 * k + 1) * t) for k, x in enumerate(fN1)) for t in thv]
        fac = [v.real / w for v, w in zip(vals, fv)]
        print(f'   first surviving sector / f_{N+1}(theta) at three angles: {fac}  expected {(N) * float(cl - 1)} = +N(c_l-1) (residual of the truncation at order N+1 is the forcing N(c_l-1) f_(N+1))')
    return ok

if __name__ == '__main__':
    ok1 = run('9/5', ['1', '1/3'], 4, 'A')          # delta = 4/9, two-mode f_1
    ok2 = run('7/4', ['2', '-1/5', '1/7'], 3, 'B')   # delta = 3/7, three-mode f_1
    ok3 = run('2', ['1', '1/2'], 3, 'C')             # delta = 1/2, two modes; n = 4 has p_4 = -1 (chi gauge degeneracy), so stop at N = 3
    print('ALL PASS' if ok1 and ok2 and ok3 else 'SOME FAIL')
