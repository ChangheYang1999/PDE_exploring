# Lead check of the verifier's example (log primitive at A = j - 1), inner region chi = 1, in (s, v) coordinates.
import sympy as sp
s, v = sp.symbols('s v')
for j in (5, 7):
    A = j - 1
    r = -s
    F = -sp.log(r) * v**j
    Fs, Fv = sp.diff(F, s), sp.diff(F, v)
    J = 1 + sp.diff(F, s, v)
    a = (A*(s + Fv) - v*sp.diff(F, v, 2))/J
    b = J*v + sp.diff(F, s, 2)*a
    y = v + Fs
    # derivatives in (s, y): d/dy = (1/y_v) d/dv, d/ds|_y = d/ds|_v - (y_s/y_v) d/dv
    yv, ys = sp.diff(y, v), sp.diff(y, s)
    Dy = lambda g: sp.diff(g, v)/yv
    Ds = lambda g: sp.diff(g, s) - ys/yv*sp.diff(g, v)
    f = v
    tr = sp.simplify(a*Ds(f) + b*Dy(f) - f)
    dv = sp.simplify(Ds(a) + Dy(b) - (A + 1))
    print('j', j, 'A', A, 'y =', sp.simplify(y), ' J =', sp.simplify(J))
    print('  transport residual', tr, ' div residual', dv)
    print('  a - As/J:', sp.simplify(a - A*s/J), '  b - y - A j r^-2 v^(2j-1)/J:', sp.simplify(b - y - A*j*v**(2*j-1)/(r**2*J)))
    # frozen transport (A s d_s + y d_y) f - f
    print('  frozen transport residual', sp.simplify(A*s*Ds(f) + y*Dy(f) - f))
    # series of f in y at fixed s: invert y = v + v^j / r
    Y, R = sp.symbols('Y R', positive=True)
    vs = Y
    for it in range(4):
        vs = sp.expand(sp.series(Y - vs**j/R, Y, 0, 2*j+1).removeO())
    print('  f(y) =', sp.series(vs, Y, 0, 2*j).removeO())
    # curl defect b_s - a_y + f_s, leading term in v at fixed s
    cd = sp.simplify(Ds(b) - Dy(a) + Ds(f))
    print('  curl defect series in v:', sp.series(cd, v, 0, j).removeO())
