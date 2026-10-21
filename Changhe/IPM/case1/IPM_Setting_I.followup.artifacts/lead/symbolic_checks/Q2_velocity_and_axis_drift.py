import sympy as sp
s, y, t = sp.symbols('s y t', real=True)
A, g = 2, 5
for sign in (1, -1):
    S = sp.Symbol('S', positive=True)   # |s|
    ss = sign*S
    R = sp.sqrt(S**2 + y**2)
    I = (y*R + S**2*(sp.log(y + R) - sp.log(S)))/2
    v0 = ss*I
    # derivatives w.r.t. s: d/ds = sign d/dS
    ds = lambda e: sign*sp.diff(e, S)
    dy = lambda e: sp.diff(e, y)
    D = lambda e: A*ss*ds(e) + y*dy(e)
    # check I_y
    assert sp.simplify(dy(I) - R) == 0
    U2 = -(D(v0) - v0)/g
    lapU2 = sp.simplify(ds(ds(U2)) + dy(dy(U2)))
    print('sign', sign, '-Lap U2 - v0_ss =', sp.simplify(-lapU2 - ds(ds(v0))))
    # U1: dU1/dy = dU2/ds + dv0/ds ; dU1/ds = -dU2/dy
    integrand = sp.simplify(ds(U2) + ds(v0))
    U1y = sp.integrate(integrand.subs(y, t), (t, 0, y))
    U1y = sp.simplify(U1y)
    # axis part: d/ds U1(s,0) = -dU2/dy at y=0
    rhs0 = sp.simplify(-dy(U2).subs(y, 0))
    print(' -dU2/dy(s,0) =', rhs0)
    c = sp.Symbol('c')
    U1 = U1y + c*S**3
    cond = sp.simplify(ds(U1) + dy(U2))
    sol = sp.solve(sp.simplify(cond.subs(y, 0)), c)
    print(' c =', sol)
    U1 = U1.subs(c, sol[0])
    print(' div residual', sp.simplify(ds(U1) + dy(U2)))
    print(' curl residual', sp.simplify(ds(U2) - dy(U1) + ds(v0)))
    print(' U1 at s->0 (y=1):', sp.limit(U1.subs(y, 1), S, 0))
    N = sp.simplify(U1*ds(v0) + U2*dy(v0))
    # singular structure near s = 0 at y = 1: series in S
    print(' v0 series:', sp.series(v0.subs(y, 1), S, 0, 5))
    print(' N series:', sp.series(N.subs(y, 1), S, 0, 4))
