"""verifier: independent symbolic check of SPEC v5.3 S2 (h), the explicit H_j and (C2'), and the C^(2,alpha) example."""
import sympy as sp
x, y, s, A = sp.symbols('x y s A', positive=True)
k = sp.sqrt(2 / A)
cl = (A + 1) / 2
w = -(A / k) * sp.sin(k * x)
g = A * (1 - sp.cos(k * x))
rho = g * y
psi = (cl * x - w) * y
U1, U2 = -sp.diff(psi, y), sp.diff(psi, x)
W1, W2 = cl * x + U1, cl * y + U2
out = {}
out['W1 - w'] = sp.simplify(W1 - w)
out['W2 - (A+1-w\')y'] = sp.simplify(W2 - (A + 1 - sp.diff(w, x)) * y)
out['-Lap psi - rho_x'] = sp.simplify(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x))
out['W.grad rho - rho'] = sp.simplify(sp.expand_trig(W1 * sp.diff(rho, x) + W2 * sp.diff(rho, y) - rho))
DW0 = sp.Matrix([[sp.diff(W1, x), sp.diff(W1, y)], [sp.diff(W2, x), sp.diff(W2, y)]]).subs({x: 0, y: 0})
xP = sp.pi / k
DWP = sp.Matrix([[sp.diff(W1, x), sp.diff(W1, y)], [sp.diff(W2, x), sp.diff(W2, y)]]).subs({x: xP, y: 0})
out['DW(0)'] = sp.simplify(DW0)
out['w(P)'] = sp.simplify(w.subs(x, xP))
out['DW(P)'] = sp.simplify(DWP)
out['g(P)'] = sp.simplify(g.subs(x, xP))
out['rho/(x^2 y) series'] = sp.series(sp.simplify(rho / (x ** 2 * y)), x, 0, 5)
out['psi_xy(0) - (3 c_l - 1)'] = sp.simplify(sp.diff(psi, x, y).subs({x: 0, y: 0}) - (3 * cl - 1))
xi = (2 / k) * sp.tan(k * x / 2)
eta = y * sp.cos(k * x / 2) ** 2
out['W.grad xi + A xi'] = sp.simplify(W1 * sp.diff(xi, x) + W2 * sp.diff(xi, y) + A * xi)
out['W.grad eta - (2A+1) eta'] = sp.simplify(sp.expand_trig(W1 * sp.diff(eta, x) + W2 * sp.diff(eta, y) - (2 * A + 1) * eta))
out['rho - xi^2 eta'] = sp.simplify(sp.expand_trig(rho - xi ** 2 * eta))
out['a2 = (g\' - w\'\')/2'] = sp.simplify((sp.diff(g, x) - sp.diff(w, x, 2)) / 2)
out['W1 y^2 coefficient (= a2)'] = sp.simplify(sp.diff(W1, y, 2).subs(y, 0) / 2)
for kk, v in out.items():
    print('%-28s %s' % (kk, v))

# explicit H_j: H = A^q g^(j+q) |w|^(-q), q = (j-1)/A, with a general solution pair (w, g) of T_1 = 0: g'/g = (w' - A)/w
j = sp.symbols('j', positive=True)
X = sp.symbols('X')
wf = sp.Function('w')(X)
gf = sp.Function('g')(X)
q = (j - 1) / A
logH = q * sp.log(A) + (j + q) * sp.log(gf) - q * sp.log(-wf)          # on (0, x*), w < 0
h = A + 1 - sp.diff(wf, X)
dlogH = sp.diff(logH, X).subs(sp.Derivative(gf, X), gf * (sp.diff(wf, X) - A) / wf)
print("H'/H - (1 - j h)/w =", sp.simplify(dlogH - (1 - j * h) / wf))
# normalization at 0: g = x^2 (1 + O(x^2)), w = -A x (1 + O(x^2)) -> H = x^(2j+q) (1 + O(x^2))
print('p_j = 2j + q =', sp.simplify(2 * j + q), '; check against (j(4c_l-1)-1)/A with c_l = (A+1)/2:',
      sp.simplify((j * (4 * (A + 1) / 2 - 1) - 1) / A - (2 * j + q)))
# (C2'): u = G/H solves w H u' = F when T_j = 0
G = sp.Function('G')(X); F = sp.Function('F')(X); Hf = sp.Function('H')(X)
Tj = wf * sp.diff(G, X) + (j * h - 1) * G - F
u = G / Hf
expr = (wf * Hf * sp.diff(u, X) - F).subs(sp.Derivative(Hf, X), Hf * (1 - j * h) / wf)
print("w H (G/H)' - F - T_j =", sp.simplify(sp.expand(expr - Tj)))

# C^(2,alpha) example f = y^3 (s^2 + y^2)^(-1/A)
f = y ** 3 * (s ** 2 + y ** 2) ** (-1 / A)
lam = sp.symbols('lam', positive=True)
print('homogeneity f(lam s, lam y)/f(s,y) =', sp.simplify(f.subs({s: lam * s, y: lam * y}, simultaneous=True) / f))
print('d_y^3 f / 6 at y = 0:', sp.simplify(sp.diff(f, y, 3).subs(y, 0) / 6))
