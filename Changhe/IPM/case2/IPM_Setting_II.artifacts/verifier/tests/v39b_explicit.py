"""V39b (referee result 12 results/01-explicit): algebra behind the classification and the parameter limits.
Each identity prints PASS/FAIL. Run: OMP_NUM_THREADS=1 python3 tests/v39b_explicit.py"""
import sympy as sp

x, y, s, t, g, l, a1, a2, C = sp.symbols('x y s t gamma l a1 a2 C', real=True)
xp = sp.symbols('xp', positive=True)
gp = sp.symbols('gp', positive=True)
res = []


def chk(name, expr):
    e = sp.simplify(expr)
    ok = (e == 0)
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), name, '' if ok else e)


# (1) tilted shear on the side s > 0 (s = a.X): f(s) = s^g; W = -(a1/|a|^2) a_perp f(s)
f = sp.Function('f')
S = a1*x + a2*y
A2 = a1**2 + a2**2
W1 = -(a1/A2)*(-a2)*f(S)
W2 = -(a1/A2)*(a1)*f(S)
rho = f(S)
chk('tilted: div W = 0', sp.diff(W1, x) + sp.diff(W2, y))
chk('tilted: curl W + rho_x = 0', sp.diff(W2, x) - sp.diff(W1, y) + sp.diff(rho, x))
chk('tilted: a.W = 0', a1*W1 + a2*W2)
# transport of a 1D coordinate H(s): V.grad H = l s H'(s) since a.W = 0
H = sp.Function('H')
VH = (l*x + W1)*sp.diff(H(S), x) + (l*y + W2)*sp.diff(H(S), y)
chk('1D: V.grad H(s) = l s H\'(s)', VH - l*S*sp.diff(H(S), x)/a1)

# (2) 1D ODE l s H' = H/g with H(0)=0, H'(0)!=0 forces l g = 1; then H = C s on each side
Hs = sp.Function('Hs')
sol = sp.dsolve(sp.Eq(l*s*Hs(s).diff(s), Hs(s)/g), Hs(s))
print('INFO 1D ODE solution:', sol)
chk('1D: solution is C s^(1/(l g)) (exponent 1 iff l g = 1)', sp.simplify(sol.rhs.subs(sp.Symbol('C1'), 1) - s**(1/(l*g))))
# density ODE l s rho' = rho: rho = C s^(1/l); root jet |x|^g forces 1/l = g
Rs = sp.Function('Rs')
solr = sp.dsolve(sp.Eq(l*s*Rs(s).diff(s), Rs(s)), Rs(s))
chk('1D density: solution C s^(1/l)', sp.simplify(solr.rhs.subs(sp.Symbol('C1'), 1) - s**(1/l)))

# (3) homogeneity: t^{-q} |t x + t^2 e|^g = t^{g-q} |x + t e|^g (x>0 side); limit t->0 constant iff q = g
e, q = sp.symbols('e q', real=True)
expr = t**(-q)*(t*xp + t**2*e)**g
chk('homog: t^-q rho(tX) = t^(g-q) (x + t e)^g', sp.simplify(expr/(t**(g - q)*(xp + t*e)**g) - 1).subs({t: sp.Rational(1, 3)}))

# (4) conjugation: V0 = (l x, l y - |x|^g), l = 1/g, x > 0 and x < 0 separately
for sgn in (1, -1):
    X = sgn*xp
    ax = xp  # |x|
    # derivative of |x|^g w.r.t. x on the side sgn: sgn * g * xp^(g-1)
    def Dx(F):
        return sp.diff(F, xp)*sgn  # d/dx = sgn d/dxp
    lv = 1/gp
    V0 = (lv*X, lv*y - ax**gp)
    eta = y - gp/(1 - gp)*ax**gp
    Veta = V0[0]*Dx(eta) + V0[1]*sp.diff(eta, y)
    chk(f'conj: V0 eta = eta/g (side {sgn})', Veta - eta/gp)
    V0abs = V0[0]*Dx(ax)
    chk(f'conj: V0 |x| = |x|/g (side {sgn})', V0abs - ax/gp)
    etat = y - gp/(1 - gp)*(ax**gp - ax)
    Vetat = V0[0]*Dx(etat) + V0[1]*sp.diff(etat, y)
    chk(f'conj: V0 eta~ = eta~/g (side {sgn})', Vetat - etat/gp)
    # gamma = 1 identity: (x d_x + (y - |x|) d_y)(y + |x| log|x|) = y + |x| log|x|
    F1 = y + ax*sp.log(ax)
    chk(f'g=1: (x dx + (y-|x|) dy)(y+|x|log|x|) = same (side {sgn})', X*Dx(F1) + (y - ax)*sp.diff(F1, y) - F1)
# limit of eta~ as gamma -> 1
lim = sp.limit(-gp/(1 - gp)*(xp**gp - xp), gp, 1)
chk('limit g->1 of -g/(1-g)(|x|^g-|x|) = |x| log|x|', lim - xp*sp.log(xp))
# uniformity remark: d/dx eta at x->0+ for g<1 is unbounded (not C^1)
print('INFO d_x eta (x>0):', sp.simplify(sp.diff(y - gp/(1 - gp)*xp**gp, xp)))

# (5) Section 5 local exponent-two solution (Prop 3.15 of the report)
lp = sp.symbols('lp', positive=True)
beta = 2*lp - sp.Rational(1, 2)
z = beta + y
xi = x*(beta/z)**2
rho2 = x**2*(beta/z)**4
b = beta*z/3 - beta**4/(3*z**2)
psi = x*(b - lp*y)
U = (-sp.diff(psi, y), sp.diff(psi, x))
U0 = [u.subs({x: 0, y: 0}) for u in U]
chk('sec5: b(0) = 0', b.subs(y, 0))
chk('sec5: U(0) = 0', U0[0]**2 + U0[1]**2)
chk('sec5: b\' formula', sp.diff(b, y) - (beta/3 + 2*beta**4/(3*z**3)))
chk('sec5: b\'\' formula', sp.diff(b, y, 2) + 2*beta**4/z**4)
chk('sec5: -Lap psi = rho_x', -(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho2, x))
V = (lp*x + U[0] - U0[0], lp*y + U[1] - U0[1])
chk('sec5: V = (x(2l - b\'), b)', (V[0] - x*(2*lp - sp.diff(b, y)))**2 + (V[1] - b)**2)
chk('sec5: V.grad xi = xi/2', V[0]*sp.diff(xi, x) + V[1]*sp.diff(xi, y) - xi/2)
chk('sec5: V.grad rho = rho', V[0]*sp.diff(rho2, x) + V[1]*sp.diff(rho2, y) - rho2)
chk('sec5: jet xi_x(0)=1', sp.diff(xi, x).subs({x: 0, y: 0}) - 1)
chk('sec5: jet xi_y(0)=0', sp.diff(xi, y).subs({x: 0, y: 0}))

print(f'SUMMARY {sum(res)}/{len(res)} PASS')
