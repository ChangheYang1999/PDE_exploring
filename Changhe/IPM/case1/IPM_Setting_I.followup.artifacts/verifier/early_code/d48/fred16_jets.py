"""Own check of fred16 (1): quadratic jets at P, the fifth-log axis equation, the smooth-interaction factor of L, and the
quadratic-order coefficient J and e, derived here from div W = A + 1, curl W = -rho_x and W.grad rho = rho.
Logarithms are carried as a symbol Ly = log|y| with y d_y Ly = 1 (and log s as Ls with s d_s Ls = 1)."""
import sympy as sp
s, y, Ly = sp.symbols('s y Ly')
A, gs, aw, b2, c, g1 = sp.symbols('A g_s a_w b_2 c g_1')
# (a) quadratic jets
W1 = A*s + aw*s**2 + b2*y**2; W2 = y + c*s*y; rho = gs*y + g1*s*y
div = sp.expand(sp.diff(W1, s) + sp.diff(W2, y) - (A + 1))
curl = sp.expand(sp.diff(W2, s) - sp.diff(W1, y) + sp.diff(rho, s))
tr = sp.expand(W1*sp.diff(rho, s) + W2*sp.diff(rho, y) - rho)
eqs = [sp.Poly(div, s, y).coeff_monomial(s), sp.Poly(curl, s, y).coeff_monomial(y), sp.Poly(tr, s, y).coeff_monomial(s*y)]
sol = sp.solve(eqs, [c, g1, b2], dict=True)[0]
print('(a) jets:', sol, ' fred16: c=-2aw, g1=2aw gs/A, b2=aw(gs/A-1):',
      sp.simplify(sol[c] + 2*aw) == 0, sp.simplify(sol[g1] - 2*aw*gs/A) == 0, sp.simplify(sol[b2] - aw*(gs/A - 1)) == 0)

# (b) fifth-log equation from the axis series with log coefficients; derivative rule d/dy Ly = 1/y
x = sp.symbols('x')
w, h, g, B, L, C, D5, E5, a2, a4, a4L, b3, b5, b5L = [sp.Function(n)(x) for n in
    ['w', 'h', 'g', 'B', 'L', 'C', 'D5', 'E5', 'a2', 'a4', 'a4L', 'b3', 'b5', 'b5L']]
def dy(expr):
    expr = sp.expand(expr)
    return sp.expand(sp.diff(expr, y) + sp.diff(expr, Ly)/y)
def dx(expr):
    return sp.expand(sp.diff(expr, x))
rho = g*y + (B + L*Ly)*y**3 + (C + D5*Ly + E5*Ly**2)*y**5
a = w + a2*y**2 + (a4 + a4L*Ly)*y**4
b = h*y + b3*y**3 + (b5 + b5L*Ly)*y**5
divE = sp.expand(dx(a) + dy(b))
curlE = sp.expand(dx(b) - dy(a) + dx(rho))
def coef(expr, n, m):  # coefficient of y^n Ly^m
    e = sp.expand(expr)
    return sp.expand(e.coeff(y, n).coeff(Ly, m)) if m > 0 else sp.expand(e.coeff(y, n).subs(Ly, 0))
s1 = sp.solve([coef(curlE, 3, 1), coef(divE, 4, 1)], [a4L, b5L], dict=True)[0]
print('(b) velocity log coefficients: a4L =', s1[a4L], ' b5L =', s1[b5L])
trE = sp.expand(a*dx(rho) + b*dy(rho) - rho)
e3 = coef(trE, 3, 1); s1[b5L] = s1[b5L].subs(a4L, s1[a4L]).doit()
print('    b5L after substitution:', s1[b5L])
e5 = sp.expand(coef(trE, 5, 1).subs(s1).doit())
print('    y^3 log eq:', sp.simplify(e3 - (w*sp.diff(L, x) + (3*h - 1)*L)) == 0)
target = (w*sp.diff(D5, x) + (5*h - 1)*D5 + 2*h*E5) - (-a2*sp.diff(L, x) - 3*b3*L - sp.diff(g, x)*sp.diff(L, x)/4
                                                       + g*sp.diff(L, x, 2)/20)
print('    y^5 log eq (fred16 form):', sp.simplify(e5 - target) == 0)

# (c) smooth interaction: w = A s + aw s^2, h = A + 1 - w'  =>  L = s^(-beta) (1 + aw (6 + beta)/A s + ...)
sp_ = sp.symbols('sp_', positive=True); Ap = sp.symbols('Ap', positive=True)
bet = 2/Ap
lam1 = sp.symbols('lam1')
Ls = sp_**(-bet)*(1 + lam1*sp_)
ws = Ap*sp_ + aw*sp_**2; hs = Ap + 1 - sp.diff(ws, sp_)
res = sp.expand(sp.powsimp(sp.expand((ws*sp.diff(Ls, sp_) + (3*hs - 1)*Ls)*sp_**bet), force=True))
print('    residual / s^(-beta):', sp.collect(res, sp_))
l1 = sp.solve(res.coeff(sp_, 1), lam1)[0]
print('(c) L factor:', sp.simplify(l1 - aw*(6 + bet)/Ap) == 0, l1)

# (d) quadratic order: frozen background (A s, y), g = gs; mode V on the right with T1 V(s,0) = c s^q
be, k, cc = sp.symbols('beta k c', positive=True)
Ab = 2/be; q = 3 - be
gam = -q*cc                       # div at y^0
c1 = gs*q*cc/(Ab*(q - 1))         # frozen transport at order y
alp = (q - 1)*(c1 - q*cc)/2       # curl at order y: T1 V = c s^q + alp s^(q-2) y^2
dlt = -(q - 2)*alp/3              # div at order y^2: T2 V = gam s^(q-1) y + dlt s^(q-3) y^3
d5 = -gs*k*be*(be + 1)/(40*(Ab - 1))   # first-order y^5 log coefficient of V: s^(q-5)
# check d5 from the frozen y^5 log equation: A s D' + 4 D = gs L''/20 with L = k s^(-beta), D = d5 s^(q-5)
chk = sp.simplify(Ab*(q - 5)*d5 + 4*d5 - gs*k*(-be)*(-be - 1)/20)
print('(d) d5 from frozen eq:', chk == 0)
lamL = (cc*be - 3*gam)*k/(2*(Ab - 1))   # order-l^2 y^3 log coefficient lamL s^(2-2beta)
chkL = sp.simplify(Ab*(2 - 2*be)*lamL + 2*lamL - (cc*be - 3*gam)*k)
print('    L2 from y^3 log eq:', chkL == 0)
# order-l^2 part of the y^5 log equation, all at s^(-2 beta): A s D2' + 4 D2 + 2 E2 = J s^(-2 beta)
Jown = (-(cc*(q - 5)*d5) - 5*gam*d5                          # -dw D1' - 5 dh D1
        + alp*be*k - 3*dlt*k                                  # -a2 L' - 3 b3 L  (L' = -beta k s^(-beta-1))
        + (q - 1)*c1*be*k/4                                   # -g' L'/4
        + (c1*k*be*(be + 1) + gs*lamL*(2 - 2*be)*(1 - 2*be))/20)  # + g L''/20 (dg L1'' + gs L2'')
Jf = -(cc*k*(be - 3)/(20*(be - 2)))*(11*be**2*gs + 10*be**2 - 13*be*gs - 40*be + 40)
print('    J own:', sp.factor(sp.simplify(Jown)))
print('    J fred16:', sp.factor(Jf))
print('    J own - fred16 =', sp.simplify(Jown - Jf))
# e from the angular alternative e s^(-2b) y^5 log^2|y/s|
e = sp.symbols('e')
print('    e = -J/(2(A-1)):', sp.solve(2*(1 - Ab)*e - Jf, e)[0], ' check', sp.simplify(sp.solve(2*(1 - Ab)*e - Jf, e)[0] + Jf/(2*(Ab - 1))) == 0)
# numerical value at the computed parameters
An, gn = 10.150725, 29.74949
print('    J/(c k) at A, g* =', sp.N((Jf/(cc*k)).subs({be: 2/An, gs: gn})), ' own', sp.N((Jown/(cc*k)).subs({be: 2/An, gs: gn})))

# (e) constant c of T_1 V(s,0) = c s_+^q: the eta-integral and the triple antiderivative
import mpmath as mp
mp.mp.dps = 30
for (An, gn) in [(10.150725, 29.74949), (4.0, 10.5), (3.0, 7.0)]:
    bb = gn/(2*(An - 1))
    I = 2*mp.quad(lambda t: t**(2*bb - 3)*(1 + t**2)**(-bb - 1), [0, 1, mp.inf])
    print('(e) A, g* =', An, gn, ' b =', mp.nstr(bb, 12), ' int |t|^(2b-3)(1+t^2)^(-b-1) =', mp.nstr(I, 20),
          ' 1/(b(b-1)) =', mp.nstr(1/(bb*(bb - 1)), 20))
# (i xi)^(-3) is the symbol of the third antiderivative: i xi |xi|^(-4) = (i xi)^(-3) for real xi != 0
xi = sp.symbols('xi', real=True, nonzero=True)
print('    i xi |xi|^-4 == (i xi)^-3:', sp.simplify(sp.I*xi/xi**4 - (sp.I*xi)**(-3)) == 0)
sq = sp.symbols('sq', positive=True)
print('    d^3/ds^3 s^q/(q(q-1)(q-2)) = s^(-beta):', sp.simplify(sp.diff(sq**q/(q*(q - 1)*(q - 2)), sq, 3) - sq**(-be)) == 0)
# (f) weak characteristic through P: s = sigma y^2, ds/dy = W1/W2 with W = (A s + aw s^2 + b2 y^2, y + c s y)
sig = sp.symbols('sigma')
W1c = A*sig*y**2 + aw*sig**2*y**4 + b2*y**2; W2c = y + c*sig*y**3
ex = sp.expand(sp.series(W1c/W2c - 2*sig*y, y, 0, 3).removeO())
print('(f) weak characteristic sigma =', sp.solve(ex.coeff(y, 1), sig), ' (fred16: -b2/(A-2))')
