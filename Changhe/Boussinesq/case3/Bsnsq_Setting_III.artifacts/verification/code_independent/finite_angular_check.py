"""Exact Cartesian-polynomial checks of the finite-angular proof formulas."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as s

root = Path('research/83_finite_angular_support/verification')
root.mkdir(parents=True, exist_ok=True)
start = time.monotonic()
out = {'started_utc': datetime.now(timezone.utc).isoformat(), 'checks': []}
x, y, r = s.symbols('x y r', real=True)
r2 = x*x + y*y
I = s.I


def polar_coefficient(expr, n):
    """Expand Cartesian monomials using x=r(z+z^-1)/2,y=r(z-z^-1)/(2i).

    This uses exact binomial coefficients instead of polar differentiation.
    """
    ans = 0
    for (a, b), coefficient in s.Poly(s.expand(expr), x, y).terms():
        degree = a + b
        if degree < n or (degree - n) % 2:
            continue
        jplusk = (degree - n) // 2
        angular = sum(s.binomial(a, j) * s.binomial(b, jplusk-j) * (-1)**(jplusk-j)
                      for j in range(max(0, jplusk-b), min(a, jplusk)+1))
        ans += coefficient * angular * r**degree / (2**degree * I**b)
    return s.expand(ans)


def check(name, expression):
    reduced = s.simplify(s.expand(expression))
    ok = reduced == 0
    out['checks'].append({'name': name, 'passed': bool(ok),
                          'remainder': str(reduced)})
    if not ok:
        raise AssertionError((name, reduced))


for n in range(2, 7):
    m = 2*n - 1
    eps = 1 if n % 2 else I
    plus, minus = (x+I*y)**n, (x-I*y)**n
    psi = s.expand((eps*plus+s.conjugate(eps)*minus) * (1+2*r2+3*r2*r2) + x*r2)
    theta = s.expand(I*eps**2*((x+I*y)**m-(x-I*y)**m) * (2+5*r2+7*r2*r2) + x*x)
    omega = -s.diff(psi, x, 2)-s.diff(psi, y, 2)
    vx, vy = -s.diff(psi, y), s.diff(psi, x)
    bracket_theta = vx*s.diff(theta, x)+vy*s.diff(theta, y)
    bracket_omega = vx*s.diff(omega, x)+vy*s.diff(omega, y)
    f = r**n*(1+2*r*r+3*r**4)
    h = r**m*(2+5*r*r+7*r**4)
    g = -s.diff(f, r, 2)-s.diff(f, r)/r+n*n*f/(r*r)
    check(f'N{n} stream coefficient', polar_coefficient(psi, n)-eps*f)
    check(f'N{n} vorticity coefficient', polar_coefficient(omega, n)-eps*g)
    check(f'N{n} forcing coefficient', polar_coefficient(s.diff(theta, x), 2*n)
          - I*eps**2*(s.diff(h, r)-m*h/r)/2)
    check(f'N{n} top temperature bracket', polar_coefficient(bracket_theta, n+m)
          - I*(m*eps*s.diff(f, r)*I*eps**2*h
               - n*eps*f*I*eps**2*s.diff(h, r))/r)
    check(f'N{n} top vorticity bracket', polar_coefficient(bracket_omega, 2*n)
          - I*n*eps**2*(s.diff(f, r)*g-f*s.diff(g, r))/r)
    print('Cartesian checks N', n, 'passed', flush=True)

ap, bp = s.Function('a')(r), s.Function('b')(r)
C, K, D = s.symbols('C K D', real=True)
for n in range(2, 9):
    m = 2*n-1
    q = s.Rational(m, n)
    p = q-1
    f, g, h = r**n*ap, r**n*bp, C*r**m*ap**q
    check(f'N{n} radial rescaling',
          (2*n*(s.diff(f,r)*g-f*s.diff(g,r))-(r*s.diff(h,r)-m*h))/r**(2*n)
          -(2*n*(s.diff(ap,r)*bp-ap*s.diff(bp,r))-C*q*ap**(q-1)*s.diff(ap,r)))
    bsol = K*ap+C*q*ap**p/2
    check(f'N{n} first integral',
          2*n*(s.diff(ap,r)*bsol-ap*s.diff(bsol,r))-C*q*ap**(q-1)*s.diff(ap,r))
    energy = s.diff(ap,r)**2/2+K*ap**2/2+D*ap**(p+1)/(p+1)
    derivative = s.diff(energy,r).subs(s.diff(ap,r,2),-(2*n+1)*s.diff(ap,r)/r-K*ap-D*ap**p)
    check(f'N{n} energy dissipation', derivative+(2*n+1)*s.diff(ap,r)**2/r)
    check(f'N{n} endpoint indicial exponent', 2*n-2-2*n*p)

out.update(status='COMPLETE', ended_utc=datetime.now(timezone.utc).isoformat(),
           elapsed_seconds=time.monotonic()-start,
           scope='Exact algebra only. The ODE inequalities and global extension argument require the informal proof.')
(root/'symbolic_checks.json').write_text(json.dumps(out, indent=2)+'\n')
print('COMPLETE', len(out['checks']), 'checks', out['elapsed_seconds'], flush=True)
