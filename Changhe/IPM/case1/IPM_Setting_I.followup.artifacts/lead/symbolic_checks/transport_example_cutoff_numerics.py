# Lead's independent check of the referee's transport example (section 3): explicit C^inf cutoff, A = 6/5 and 5/4.
# Checks, at points of the cutoff layer and the inner region: transport a f_s + b f_y = f, divergence a_s + b_y = A + 1,
# curl defect b_s - a_y + f_s != 0; scaling of the third derivatives of a - A s, f - y, b - y (sup over the layer) as
# r -> 0; the axis value d_y^5 f(-r, 0) = -120 r^(-q). Coordinates: s = -r, F = F(r, v); d_y = (1/J) d_v,
# d_s = -d_r - (F_rr/J) d_v at fixed y, J = 1 - F_rv.
import sympy as S, mpmath as mp, itertools, sys
mp.mp.dps = 30
r, v, z = S.symbols('r v z', positive=True)
def chi_expr(z):
    p = lambda t: S.exp(-1/t)
    return p(2 - z)/(p(2 - z) + p(z - 1))     # = 1 at z <= 1, 0 at z >= 2 (used for 1 < z < 2)
for A in (S.Rational(6, 5), S.Rational(5, 4)):
    q = 4/A
    c = 1/(q - 1)
    for region in ('layer', 'inner'):
        ch = chi_expr(v/r**3) if region == 'layer' else 1
        F = c*r**(1 - q)*v**5*ch
        J = 1 - S.diff(F, r, v)
        Frr = S.diff(F, r, 2)
        a = (A*(-r + S.diff(F, v)) - v*S.diff(F, v, 2))/J
        b = J*v + Frr*a
        f = v
        Dy = lambda e: S.diff(e, v)/J
        Ds = lambda e: -S.diff(e, r) - Frr*S.diff(e, v)/J
        tr = a*Ds(f) + b*Dy(f) - f
        dv = Ds(a) + Dy(b) - (A + 1)
        cu = Ds(b) - Dy(a) + Ds(f)
        ftr, fdv, fcu = [S.lambdify((r, v), e, 'mpmath') for e in (tr, dv, cu)]
        mx = [0, 0]; cmax = 0
        for rr in (mp.mpf('0.05'), mp.mpf('0.02')):
            for zz in ([1.1, 1.3, 1.5, 1.7, 1.9] if region == 'layer' else [0.3, 0.6, 0.9]):
                vv = mp.mpf(zz)*rr**3
                mx[0] = max(mx[0], abs(ftr(rr, vv))); mx[1] = max(mx[1], abs(fdv(rr, vv)))
                cmax = max(cmax, abs(fcu(rr, vv)))
        print('A=%s %s: max|transport residual| %.1e, max|div residual| %.1e, max|curl defect| %.3e'
              % (A, region, mx[0], mx[1], cmax))
        sys.stdout.flush()
    # third derivatives in the layer: d_s^i d_y^j with i + j = 3, of a - A s (s = -r), f - y, b - y; y = v - F_r
    F = c*r**(1 - q)*v**5*chi_expr(v/r**3)
    J = 1 - S.diff(F, r, v); Frr = S.diff(F, r, 2)
    a = (A*(-r + S.diff(F, v)) - v*S.diff(F, v, 2))/J
    b = J*v + Frr*a
    yv = v - S.diff(F, r)
    Dy = lambda e: S.diff(e, v)/J
    Ds = lambda e: -S.diff(e, r) - Frr*S.diff(e, v)/J
    fields = {'a-As': a + A*r, 'f-y': v - yv, 'b-y': b - yv}
    for name, e in fields.items():
        for (i, j) in [(0, 3), (3, 0)]:
            d = e
            for _ in range(i): d = Ds(d)
            for _ in range(j): d = Dy(d)
            fd = S.lambdify((r, v), d, 'mpmath')
            sups = []
            for rr in (mp.mpf('0.04'), mp.mpf('0.01'), mp.mpf('0.0025')):
                sups.append(max(abs(fd(rr, mp.mpf(zz)*rr**3)) for zz in [1 + k/20 for k in range(1, 20)]))
            slopes = [mp.log(sups[k + 1]/sups[k])/mp.log(mp.mpf(1)/4) for k in range(2)]
            print('A=%s %s d_s^%d d_y^%d: sup over layer at r = 0.04, 0.01, 0.0025: %s; exponents %s'
                  % (A, name, i, j, [mp.nstr(x, 4) for x in sups], [mp.nstr(x, 4) for x in slopes]))
            sys.stdout.flush()
    print('A=%s predicted exponents: a-As d_y^3: %s, d_s^3: %s; f-y, b-y d_y^3: %s, d_s^3: %s'
          % (A, 13 - q - 9, 13 - q - 3, 15 - q - 9, 15 - q - 3))
    # axis fifth derivative: inner region, y = v + r^(-q) v^5; series inversion
    y = S.symbols('y')
    vser = y
    for _ in range(3):
        vser = S.series(y - r**(-q)*vser**5, y, 0, 8).removeO()
    print('A=%s fifth Taylor coefficient of f(-r, y) in y: %s (expected -r^(-q), q = %s)'
          % (A, S.simplify(vser.coeff(y, 5)), q))
