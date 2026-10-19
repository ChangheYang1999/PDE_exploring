"""V149: checks for lead item 15 (ref4 corrections).
G1-G4: the x^2 example of FR 4.4 (ii): which 'strain contractions' change sign.
G5: h(t) = |t|^(7/2) is C^3, not C^4, two live sides of order 7/2 (9.6 Step 3 parenthesis).
G6: rectangular Arnoldi bound sigma_min(B) <= sigma_min(Hbar) + ||E|| (random test of the inequality).
"""
import sympy as sp, numpy as np
x, y = sp.symbols('x y', real=True); l = sp.symbols('l', positive=True)
ok = []
def rep(n, c, extra=''):
    ok.append(bool(c)); print(('OK   ' if c else 'FAIL ') + n + ((' ' + str(extra)) if extra != '' else ''), flush=True)
b = 2*l - sp.Rational(1, 2); h = 1/(b - 1)
W = sp.Matrix([(sp.Rational(1, 2) - l)*x, (l - sp.Rational(1, 2))*y - x**2]); V = l*sp.Matrix([x, y]) + W
DW = W.jacobian([x, y]); DV = V.jacobian([x, y])
Y1 = sp.Matrix([x, 2*h*x**2]); Y2 = sp.Matrix([0, y - h*x**2])
c1 = sp.simplify((Y1.T*DW*Y1)[0]); c2 = sp.simplify((Y2.T*DW*Y2)[0])
rep('G1 Y_1^T DW Y_1 = -(l - 1/2) x^2 - 4(l - 1) x^4/(b - 1)^2', sp.simplify(c1 - (-(l - sp.Rational(1, 2))*x**2 - 4*(l - 1)*x**4/(b - 1)**2)) == 0)
rep('G2 Y_2^T DW Y_2 = (l - 1/2)(y - x^2/(b - 1))^2', sp.simplify(c2 - (l - sp.Rational(1, 2))*(y - x**2/(b - 1))**2) == 0)
d1 = sp.simplify((Y1.T*DV*Y1)[0]); d2 = sp.simplify((Y2.T*DV*Y2)[0])
rep('G3 Y_1^T DV Y_1 = x^2/2 + 4 h^2 x^4 >= 0 and Y_2^T DV Y_2 = (2l - 1/2)(y - h x^2)^2 >= 0',
    sp.simplify(d1 - (x**2/2 + 4*h**2*x**4)) == 0 and sp.simplify(d2 - b*(y - h*x**2)**2) == 0)
# sign: for l > 1 each Y^T DW Y contraction has a fixed sign
okfix = True
for lv in [1.1, 2, 5]:
    for xv in np.linspace(-3, 3, 13):
        for yv in np.linspace(-3, 3, 13):
            okfix &= float(c1.subs({l: lv, x: xv, y: yv})) <= 1e-12 and float(c2.subs({l: lv, x: xv, y: yv})) >= -1e-12
rep('G4a for l = 1.1, 2, 5 on a grid: Y_1^T DW Y_1 <= 0 and Y_2^T DW Y_2 >= 0 everywhere (fixed signs)', okfix)
S1 = (Y1.jacobian([x, y]) + Y1.jacobian([x, y]).T)/2; S2 = (Y2.jacobian([x, y]) + Y2.jacobian([x, y]).T)/2
e1 = sp.expand((V.T*S1*V)[0]); e2 = sp.expand((V.T*S2*V)[0])
rep('G4b V.S_1 V = x^2 (1/4 + 2 h b y - 2 h x^2), V.S_2 V = (b y - x^2)(b y - (1 + h) x^2)',
    sp.simplify(e1 - x**2*(sp.Rational(1, 4) + 2*h*b*y - 2*h*x**2)) == 0 and sp.simplify(e2 - (b*y - x**2)*(b*y - (1 + h)*x**2)) == 0)
sg = True
for lv in [1.1, 2, 5]:
    for f in (e1, e2):
        vals = [float(f.subs({l: lv, x: 1, y: yv})) for yv in np.linspace(-5, 5, 2001)]
        sg &= min(vals) < 0 < max(vals)
rep('G4c each V.S_i V takes both signs at x = 1 as y varies (l = 1.1, 2, 5)', sg)
t = sp.symbols('t', real=True)
hp = sp.Rational(7, 2)*sp.Rational(5, 2)*sp.Rational(3, 2)  # coefficient of |t|^(1/2) in h'''
rep('G5 h = |t|^(7/2): h\'\'\' = (105/8)|t|^(1/2) sgn t (continuous, 0 at 0); h\'\'\'\' ~ |t|^(-1/2) unbounded: C^3 not C^4',
    hp == sp.Rational(105, 8) and sp.limit(sp.diff(t**sp.Rational(7, 2), t, 3), t, 0, '+') == 0 and sp.limit(sp.diff(t**sp.Rational(7, 2), t, 4), t, 0, '+') == sp.oo)
rng = np.random.default_rng(3); okb = True
for _ in range(200):
    n, k = 40, 8
    B = rng.normal(size=(n, n)); B[:, 0] *= 1e-3
    Q, _r = np.linalg.qr(rng.normal(size=(n, k + 1)))
    Qk = Q[:, :k]
    BQ = B@Qk; Hb = Q.T@BQ; E = BQ - Q@Hb
    smin = np.linalg.svd(B, compute_uv=False)[-1]; sH = np.linalg.svd(Hb, compute_uv=False)[-1]
    okb &= smin <= sH + np.linalg.norm(E, 2) + 1e-12
rep('G6 sigma_min(B) <= sigma_min(Hbar) + ||E||_2 for B Q = Q_+ Hbar + E (200 random cases)', okb)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
