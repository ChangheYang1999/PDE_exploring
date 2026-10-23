"""Independent Cartesian rational-polynomial audit of the local theorem.

No external verification.py, producer inverse, or producer differentiation.
The small formal-polynomial class P was written by this verifier earlier.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from functools import lru_cache
from math import comb, prod, ceil
import hashlib
import json
import time
from check_local_two_projection_construction import P

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'research/all_projection_local_audit/verification'
COUNT = 0


def check(ok, detail=None):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError((COUNT, detail))


def add(*polys):
    out = {}
    for p in polys:
        for mon, co in p.items():
            out[mon] = out.get(mon, F(0))+co
    return {k: v for k, v in out.items() if v}


def scale(p, co):
    return {k: v*co for k, v in p.items() if v*co}


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            mon = i+k, j+l
            out[mon] = out.get(mon, F(0))+a*b
    return {k: v for k, v in out.items() if v}


def deriv(p, axis):
    out = {}
    for mon, co in p.items():
        if mon[axis]:
            dest = list(mon)
            dest[axis] -= 1
            out[tuple(dest)] = co*mon[axis]
    return out


def hom(p, degree):
    return {k: v for k, v in p.items() if sum(k) == degree}


@lru_cache(None)
def sine(n, p):
    if p == 0:
        return {}
    if p < 0:
        return scale(sine(n, -p), -1)
    assert p <= n and (n-p) % 2 == 0
    z = (n-p)//2
    radial = {(2*k, 2*(z-k)): F(comb(z, k)) for k in range(z+1)}
    harmonic = {(p-j, j): F((-1)**((j-1)//2)*comb(p, j))
                for j in range(1, p+1, 2)}
    return mul(radial, harmonic)


def stream(n, p):
    out = scale(sine(n+1, p+1), -F(1, 2*(n+p+2)))
    if p > 1:
        out = add(out, scale(sine(n+1, p-1), -F(1, 2*(n-p+2))))
    return out


def solve(matrix, rhs):
    rows = [list(map(F, r))+[F(v)] for r, v in zip(matrix, rhs)]
    n = len(rows)
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        v = rows[col][col]
        rows[col] = [x/v for x in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                v = rows[i][col]
                rows[i] = [x-v*y for x, y in zip(rows[i], rows[col])]
    return [r[-1] for r in rows]


def det(matrix):
    rows = [list(map(F, r)) for r in matrix]
    ans = F(1)
    for col in range(len(rows)):
        pivot = next((i for i in range(col, len(rows)) if rows[i][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            ans = -ans
        val = rows[col][col]
        ans *= val
        for i in range(col+1, len(rows)):
            factor = rows[i][col]/val
            if factor:
                for k in range(col+1, len(rows)):
                    rows[i][k] -= factor*rows[col][k]
    return ans


@lru_cache(None)
def cartesian_change(n):
    mon = [(n-j, j) for j in range(1, n+1, 2)]
    return [[sine(n, p).get(m, F(0)) for p in range(1, n+1, 2)] for m in mon]


def modes(p, n):
    return solve(cartesian_change(n), [p.get((n-j, j), F(0)) for j in range(1, n+1, 2)])


def linear(n, p, c, a):
    h = sine(n, p)
    return add(scale(mul({(1, 0): F(1)}, deriv(h, 0)), 2*c-1),
               mul({(0, 1): F(1)}, deriv(h, 1)), scale(h, -1),
               scale(deriv(stream(n, p), 0), a))


def direct_matrix(j, d, c, a):
    n = 2*j+1
    cols = [modes(linear(n, p, c, a), n)[:d] for p in range(1, 2*d, 2)]
    return list(map(list, zip(*cols)))


def claimed_matrix(j, d, c, a):
    lam = 2*j
    D = c-1
    out = [[F(0) for _ in range(d)] for _ in range(d)]
    for i in range(d):
        out[i][i] = (c+1)*lam/2-a/4 if i == 0 else c*lam+D-a/2
    for i in range(d-1):
        out[i][i+1] = F(lam+2*i+4, 4*(lam-2*i))*(2*D*(lam-2*i)-a)
        out[i+1][i] = F(lam-2*i, 4*(lam+2*i+4))*(2*D*(lam+2*i+4)-a)
    return out


def characteristic(d, lam, c, a):
    D = c-1
    values = [F(1), (c+1)*lam/2-a/4]
    for k in range(2, d+1):
        q = ((2*D*(lam+2)-a)**2-16*D*D*(k-1)**2)/16
        values.append((c*lam+D-a/2)*values[-1]-q*values[-2])
    return values[d]


def complex_coeffs(p, n):
    """Exact substitution x=(w+v)/2,y=(w-v)/(2i)."""
    out = [[F(0), F(0)] for _ in range(n+1)]
    phases = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))]
    for (i, j), co in p.items():
        assert i+j == n
        phase = phases[(-j) % 4]
        for h in range(i+1):
            for l in range(j+1):
                v = co*F(comb(i, h)*comb(j, l)*(-1)**(j-l), 2**n)
                out[h+l][0] += phase[0]*v
                out[h+l][1] += phase[1]*v
    return out


def norm(p, n):
    out = complex_coeffs(p, n)
    check(all(not (re and im) for re, im in out), 'definite parity has a single phase')
    return max((abs(re)+abs(im))/comb(n, k) for k, (re, im) in enumerate(out))


def mixed(n):
    co = [F((-1)**i*(i+2), i+3) for i in range((n+1)//2)]
    return add(*(scale(sine(n, 2*i+1), v) for i, v in enumerate(co))), \
        add(*(scale(stream(n, 2*i+1), v) for i, v in enumerate(co)))


def general_equations(N):
    f = [P('f%d' % i) for i in range(N)]
    J = [P('J%d' % i) for i in range(N)]
    T = [P('T%d' % i) for i in range(1, N)]+[P(0)]
    df = [P('df%d' % i) for i in range(N)]
    c = P('c')
    out = [c*df[i]+(c-1)*f[i] for i in range(N)]

    def term(mode, value):
        if mode and abs(mode) <= 2*N-1:
            out[(abs(mode)-1)//2] += (1 if mode > 0 else -1)*value

    for m in range(1, N+1):
        V = (T[m-1]-J[m-1])/2
        dT = (2*m-2)*T[m-1]-(f[m] if m < N else P(0))
        dJ = f[m-1]-(2*m+2)*J[m-1]
        dV = (dT-dJ)/2
        for k in range(N):
            p = 2*k+1
            one = -m*V*(f[k]+df[k])
            term(p+2*m, one)
            term(p-2*m, one)
            two = p*(2*V+dV)*f[k]/2
            term(2*m+p, two)
            term(2*m-p, two)
    names = ['f%d' % i for i in range(N)]+['J%d' % i for i in range(N)]+['T%d' % i for i in range(1, N)]
    return out, names


def value(p, subs):
    v = P(p).substitute(subs)
    assert not any(v.d.keys())
    return v.d.get((), F(0))


def full_characteristic_checks():
    for N in range(2, 6):
        equations, names = general_equations(N)
        for c, a in [(F(2), F(211, 7)), (F(13, 10), F(4001, 10))]:
            base = {name: F(0) for name in names}
            base.update(c=c, f0=a, J0=a/4, T1=a/4-(c-1))
            base.update({'df%d' % i: F(0) for i in range(N)})
            mat = [[value(e.derivative({'df%d' % k: 1}), base) for k in range(N)]
                   for e in equations]
            check(all(value(e, base) == 0 for e in equations))
            expected = [[((c+1)/2 if i == 0 else c) if i == k
                         else ((c-1)/2 if abs(i-k) == 1 else F(0))
                         for k in range(N)] for i in range(N)]
            check(mat == expected)
            jac = [[value(e.derivative({name: 1}), base) for name in names] for e in equations]
            for j in range(N+4):
                size = len(names)
                Q = [[jac[i][k]+(2*j*mat[i][k] if k < N else 0)
                      for k in range(size)] for i in range(N)]
                for i in range(N):
                    row = [F(0)]*size
                    row[i] = F(-1, 2)
                    row[N+i] = j+i+2
                    Q.append(row)
                for m in range(1, N):
                    row = [F(0)]*size
                    row[m] = F(1, 2)
                    row[2*N+m-1] = j-m+1
                    Q.append(row)
                rhs = prod(j+i+2 for i in range(N))*prod(j-m+1 for m in range(1, N))
                rhs *= characteristic(N, F(2*j), c, a)
                check(det(Q) == rhs, ('full characteristic', N, j, c, a))


def residual(rho, psi, c):
    return add(scale(mul({(1, 0): F(1)}, deriv(rho, 0)), c),
               scale(mul({(0, 1): F(1)}, deriv(rho, 1)), c),
               scale(mul(deriv(psi, 1), deriv(rho, 0)), -1),
               mul(deriv(psi, 0), deriv(rho, 1)), scale(rho, -1))


def jet_checks():
    rows = []
    for N, c, a in [(2, F(2), F(211, 7)), (3, F(3), F(225, 7)),
                    (5, F(2), F(211, 7)), (None, F(2), F(211, 7)),
                    (None, F(13, 10), F(3001, 100))]:
        H = F(1)
        rho = {(0, 1): a}
        psi = add({(1, 1): -(c-1)}, scale(sine(4, 4), H/2))
        stages = []
        for j in range(1, 7):
            n = 2*j+1
            d = min(N, j+1) if N is not None else j+1
            force = modes(hom(residual(rho, psi, c), n), n)[:d]
            co = solve(direct_matrix(j, d, c, a), [-f for f in force])
            hj = add(*(scale(sine(n, 2*i+1), v) for i, v in enumerate(co)))
            rho = add(rho, hj)
            psi = add(psi, *(scale(stream(n, 2*i+1), v) for i, v in enumerate(co)))
            R = residual(rho, psi, c)
            for k in range(1, j+1):
                allowed = min(N, k+1) if N is not None else k+1
                check(all(v == 0 for v in modes(hom(R, 2*k+1), 2*k+1)[:allowed]))
            check(add(scale(deriv(deriv(psi, 0), 0), -1),
                      scale(deriv(deriv(psi, 1), 1), -1), scale(deriv(rho, 0), -1)) == {})
            check(psi.get((1, 1)) == -(c-1) and rho.get((0, 1)) == a)
            if j == 1:
                FF = a*a-(4*c+20)*a+128*c-64
                check(rho[(2, 1)] == -192*H*a/FF)
                check(rho[(0, 3)] == -32*H*a*(a-4*c+2)/FF)
                check(rho[(2, 1)] < 0 and rho[(0, 3)] < 0)
            stages.append(dict(j=j, density_mode_coefficients=list(map(str, co)),
                               binomial_norm=str(norm(hj, n))))
        rows.append(dict(N=N, c=str(c), a=str(a), H=str(H), stages=stages,
                         scope='Exact finite jets, not an evaluation of the convergent local function.'))
    return rows


def main():
    start = time.monotonic()
    for n in range(3, 22, 2):
        j = (n-1)//2
        for p in range(1, n+1, 2):
            ps = stream(n, p)
            check(add(scale(deriv(deriv(ps, 0), 0), -1),
                      scale(deriv(deriv(ps, 1), 1), -1),
                      scale(deriv(sine(n, p), 0), -1)) == {})
            check(norm(sine(n, p), n) == F(1, 2*comb(n, (n-p)//2)))
        # The matrix depends affinely on c,a; these three evaluations determine it.
        for c, a in [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]:
            full = direct_matrix(j, j+1, c, a)
            for d in range(1, j+2):
                matrix = [r[:d] for r in full[:d]]
                check(matrix == claimed_matrix(j, d, c, a))
                check(det(matrix) == characteristic(d, F(2*j), c, a))
        for d in range(1, j+2):
            c, a = F(7, 3), F(0)
            matrix = direct_matrix(j, d, c, a)
            weights = [comb(n, j-i) for i in range(d)]
            weighted = [[matrix[i][k]*F(weights[k], weights[i]) for k in range(d)] for i in range(d)]
            for i, row in enumerate(weighted):
                margin = row[i]-sum(abs(v) for k, v in enumerate(row) if k != i)
                expected = 2*j if i < d-1 else 2*j+(c-1)*(2*j-2*d+2)/2
                check(margin == expected)
            one = claimed_matrix(j, d, c, F(1))
            diff = [[(one[i][k]-matrix[i][k])*F(weights[k], weights[i]) for k in range(d)] for i in range(d)]
            check(max(sum(abs(v) for v in row) for row in diff) <= 1)
        h, ps = mixed(n)
        nh = norm(h, n)
        check(norm(deriv(h, 0), n-1) <= 2*n*nh)
        check(norm(deriv(h, 1), n-1) <= 2*n*nh)
        check(norm(deriv(ps, 0), n) <= F(3, 2)*nh)
        check(norm(deriv(ps, 1), n) <= F(3, 2)*nh)
        q, _ = mixed(5)
        check(norm(mul(h, q), n+5) <= nh*norm(q, 5))
    # Formal symbolic equality to the earlier three-projection determinant.
    c, a, j = map(P, ['c', 'a', 'j'])
    D = c-1
    E = 2*c*j+D-a/2
    BC = D*D*j*(j+2)-D*a*(j+1)/2+a*a/16
    VW = D*D*(j+3)*(j-1)-D*a*(j+1)/2+a*a/16
    delta = ((c+1)*j-a/4)*(E*E-VW)-BC*E
    p3 = characteristic(3, 2*j, c, a)
    check(p3 == delta)
    for d in range(1, 10):
        pp = characteristic(d, 2*j, c, a)
        check(pp.coeff('a', d) == F(-1, 4)**d)
        integral = (4**d*pp).substitute({'c': 2, 'j': 11})
        check(all(v.denominator == 1 for v in integral.d.values()))
    full_characteristic_checks()
    jets = jet_checks()
    # Exact checks of the contraction and the extension constants.
    check(F(1, 2)+F(1, 4)+F(1, 8) == F(7, 8))
    check(F(1, 4)+2*F(1, 8) == F(1, 2))
    check(F(16, 9)*F(1, 16) == F(1, 9))
    for x in [F(1, 32), F(1, 4), F(1, 2)]:
        check((5-3*x)/(1-x)**2 <= 20)
    # Exact finite geometric-tail identity, including the omitted tail.
    x = P('x')
    for degree in range(3, 13):
        partial = sum(((2*k+1)*x**k for k in range(3, degree+1)), P(0))
        tail = x**(degree+1)*((2*degree+3)-(2*degree+1)*x)
        check((1-x)**2*partial == x**3*(7-5*x)-tail)
    result = dict(utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.monotonic()-start,
                  status='PASS', count=COUNT, jets=jets,
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  proof_sha256=hashlib.sha256((DEST.parent/'PROOF.md').read_bytes()).hexdigest(),
                  scope='Exact finite algebra tests. The separate written estimates prove convergence and extension; no global-profile claim.')
    (DEST/'CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['utc', 'elapsed_seconds', 'status', 'count']}))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        (DEST/'FAIL.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),
                                                    status='FAIL', count=COUNT, error=repr(error),
                                                    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()), indent=2)+'\n')
        raise
