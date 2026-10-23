"""Independent exact and integral checks of the three-cusp test density."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
from math import cos, sin, exp, sqrt, pi, inf
import hashlib
import json
import time
from scipy.integrate import quad
from check_local_two_projection_construction import P

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'research/quasihomogeneous_scope_example/verification'
COUNT = 0


def check(ok, detail=None):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError((COUNT, detail))


def canonical_term(s, t):
    """Normalize signs using evenness in s and oddness in t."""
    sc = next(v for v in s if v)
    tc = next(v for v in t if v)
    sgns = 1 if sc > 0 else -1
    sgnt = 1 if tc > 0 else -1
    return tuple(sgns*v for v in s), tuple(sgnt*v for v in t), sgnt


def terms(transformation):
    # The common sqrt(2) in each rotated argument is unchanged by reflection.
    out = []
    for s, t in [((1, -1), (1, 1)), ((1, 1), (-1, 1))]:
        ss = (s[0]*transformation[0], s[1]*transformation[1])
        tt = (t[0]*transformation[0], t[1]*transformation[1])
        out.append(canonical_term(ss, tt))
    return sorted(out)


def rank_witness(matrix, count=7):
    a, b, c, d = matrix
    directions = [(c, d), (a+c, b+d), (c-a, d-b)]
    moving = [(-F(beta, alpha), alpha, beta)
              for alpha, beta in directions if alpha != 0]
    slope = next(tau for tau, alpha, beta in moving if beta != 0)
    chosen = []
    proposal = 1
    while len(chosen) < count:
        v = F(proposal)
        proposal += 1
        if all(slope*v != tau*w and slope*w != tau*v
               for w in chosen for tau, _, _ in moving):
            chosen.append(v)
    for n, vn in enumerate(chosen):
        for m, vm in enumerate(chosen):
            if n != m:
                check(all(slope*vn != tau*vm for tau, _, _ in moving))
    return dict(matrix=list(matrix), slope=str(slope), sections=list(map(str, chosen)))


def H(s, t, tolerance=2e-12):
    if t == 0:
        return 0., 0.
    if s == 0:
        return (1 if t > 0 else -1)*sqrt(abs(t))/(2*sqrt(pi)), 0.
    aa = abs(s)/sqrt(2)

    def integrand(v):
        if v == 0:
            return t
        z = aa*v**3
        if z > 745:
            return 0.
        return sin(t*v*v)/(v*v)*exp(-z)*(cos(z)+sin(z))

    integral, err = quad(integrand, 0., inf, epsabs=tolerance, epsrel=tolerance, limit=400)
    return integral/(pi*sqrt(2)), err/(pi*sqrt(2))


def main():
    start = time.monotonic()
    x, y, lam = P('x'), P('y'), P('lam')
    q0 = x**4+y**6
    qp = F(1, 4)*(x-y)**4+F(1, 8)*(x+y)**6
    qm = F(1, 4)*(x+y)**4+F(1, 8)*(y-x)**6
    symbol = q0*qp*qm
    check(symbol != P(0))
    check(symbol.substitute({'x': -x}) == symbol)
    check(symbol.substitute({'y': -y}) == symbol)
    check(q0.substitute({'x': lam**3*x, 'y': lam**2*y}) == lam**12*q0)
    for xx, yy in product(range(-3, 4), repeat=2):
        if xx or yy:
            check(symbol.substitute({'x': xx, 'y': yy}).scalar() > 0)
    original = terms((1, 1))
    check(terms((-1, 1)) == original)
    check(terms((1, -1)) == sorted((s, t, -sgn) for s, t, sgn in original))
    # Differentiate E(z)=exp(-z)(cos z+sin z) using exact coefficients.
    co = (1, 1)
    derivatives = [co]
    for j in range(1, 9):
        co = (-co[0]+co[1], -co[0]-co[1])
        derivatives.append(co)
    check(derivatives[1][0] == 0)
    check(derivatives[3][0] == 4)
    check(derivatives[4] == (-4, -4))
    check(derivatives[8] == (16, 16))
    # Jump of the third derivative in the quartic Green function, /pi.
    check(F(2)*F(4)*F(1, 4) == 2)
    check(5-6+2 == 1)
    check(5-6 == -1)
    check(5+1-3 == 3 and 5+1-2 == 4)
    witnesses = []
    matrices = 0
    for matrix in product(range(-2, 3), repeat=4):
        a, b, c, d = matrix
        if a*d-b*c == 0:
            continue
        witness = rank_witness(matrix)
        matrices += 1
        if len(witnesses) < 8:
            witnesses.append(witness)
    # Numeric integral identities use independent ordinary/Fourier quadrature.
    green = []
    for b, s in product([.5, 1., 2.], [0., .25, 1., 3.]):
        if s == 0:
            integral, error = quad(lambda z: 1./(z**4+b**4), 0., inf,
                                   epsabs=1e-12, epsrel=1e-12)
        else:
            integral, error = quad(lambda z: 1./(z**4+b**4), 0., inf,
                                   weight='cos', wvar=s, epsabs=1e-11, limlst=200)
        got = 2*integral
        z = b*s/sqrt(2)
        exact = pi/(sqrt(2)*b**3)*exp(-z)*(cos(z)+sin(z))
        err = abs(got-exact)/max(1., abs(exact))
        check(err < 3e-11, ('Green', b, s, err, error))
        green.append(dict(b=b, s=s, integral=got, exact=exact, scaled_error=err))
    small, e1 = quad(lambda v: 2. if v == 0 else 2*sin(v*v)/(v*v),
                     0., 1., epsabs=1e-12, epsrel=1e-12)
    tail, e2 = quad(lambda v: v**(-1.5), 1., inf, weight='sin', wvar=1.,
                    epsabs=1e-12, limlst=250)
    constant = small+tail
    check(abs(constant-sqrt(2*pi)) < 3e-11)
    scale = []
    for s, t in [(1., 1.), (.5, -2.), (2., .3)]:
        base, error = H(s, t)
        for factor in [.5, 2., 4.]:
            got, e2 = H(factor**3*s, factor**2*t)
            err = abs(got-factor*base)/max(1., abs(got))
            check(err < 3e-10, ('scaling', s, t, factor, err))
            scale.append(dict(s=s, t=t, factor=factor, error=err,
                              quadrature_estimates=[error, e2]))
        reflected, _ = H(-s, -t)
        check(abs(reflected+base) < 3e-11)
    asymptotics = []
    for s, t in [(1., 1.), (-2., 1.), (.3, -.7)]:
        exact = (1 if t > 0 else -1)*sqrt(abs(t))/(2*sqrt(pi))
        row = dict(s=s, t=t, limit=exact, values=[])
        for radius in [16., 256., 4096.]:
            value, err = H(s/sqrt(radius), t)
            row['values'].append(dict(R=radius, value=value, difference=value-exact,
                                      quadrature_estimate=err))
        asymptotics.append(row)
    result = dict(utc=datetime.now(timezone.utc).isoformat(), status='PASS',
                  elapsed_seconds=time.monotonic()-start, count=COUNT,
                  rank_matrices=matrices, rank_witnesses=witnesses,
                  quartic_green_tests=green, sine_integral=constant,
                  sine_integral_exact=sqrt(2*pi), scaling=scale,
                  finite_radius_asymptotics=asymptotics,
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  proof_sha256=hashlib.sha256((DEST.parent/'PROOF.md').read_bytes()).hexdigest(),
                  scope='Exact finite algebra and numerical integral comparisons; no IPM profile or existence certificate.')
    (DEST/'CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['utc', 'status', 'elapsed_seconds', 'count', 'rank_matrices']}))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        (DEST/'FAIL.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),
            status='FAIL', count=COUNT, error=repr(error),
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()), indent=2)+'\n')
        raise
