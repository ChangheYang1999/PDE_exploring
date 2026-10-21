"""verifier: symbolic check of the axis hierarchy to order y^7 (F_3, F_5, F_7 and the div/curl relations)."""
import sympy as sp
x, y, cl = sp.symbols('x y c_l')
f = lambda n: sp.Function(n)(x)
w, g, G3, G5, G7 = f('w'), f('g'), f('G3'), f('G5'), f('G7')
# unknown velocity coefficients, then solved from div W = 2 c_l and curl W = -d_x rho order by order
h, a2, b3, W14, W25, W16, W27 = [f(n) for n in ['h', 'a2', 'b3', 'W14', 'W25', 'W16', 'W27']]
rho = g * y + G3 * y ** 3 + G5 * y ** 5 + G7 * y ** 7
W1 = w + a2 * y ** 2 + W14 * y ** 4 + W16 * y ** 6
W2 = h * y + b3 * y ** 3 + W25 * y ** 5 + W27 * y ** 7
div = sp.expand(sp.diff(W1, x) + sp.diff(W2, y) - 2 * cl)
curl = sp.expand(sp.diff(W2, x) - sp.diff(W1, y) + sp.diff(rho, x))
sol = {}
eqs = [(div, 0, h), (curl, 1, a2), (div, 2, b3), (curl, 3, W14), (div, 4, W25), (curl, 5, W16), (div, 6, W27)]
for e, k, unk in eqs:
    c = e.coeff(y, k).subs(sol)
    s = sp.solve(sp.Eq(c, 0), unk)[0]
    sol[unk] = sp.simplify(s.doit())
    print('%-4s = %s' % (unk.func, sol[unk]))
T = sp.expand(W1 * sp.diff(rho, x) + W2 * sp.diff(rho, y) - rho)
for j, G in [(1, g), (3, G3), (5, G5), (7, G7)]:
    Tj = T.coeff(y, j)
    lead = w * sp.diff(G, x) + (j * h - 1) * G
    Fj = sp.expand(-(Tj - lead))
    print('F_%d = %s' % (j, sp.simplify(Fj)))
# compare with SPEC S2 / this lane's formulas
F3 = -a2 * sp.diff(g, x) - b3 * g
F5 = -a2 * sp.diff(G3, x) - 3 * b3 * G3 - W14 * sp.diff(g, x) - W25 * g
F7 = -(a2 * sp.diff(G5, x) + W14 * sp.diff(G3, x) + W16 * sp.diff(g, x) + 5 * b3 * G5 + 3 * W25 * G3 + W27 * g)
for j, G, Fs in [(3, G3, F3), (5, G5, F5), (7, G7, F7)]:
    Tj = T.coeff(y, j)
    print('T_%d - [w G\' + (jh-1) G - F_%d] =' % (j, j), sp.simplify(Tj - (w * sp.diff(G, x) + (j * h - 1) * G - Fs)))
print('W1_6 - (W2_5\' + G5\')/6:', sp.simplify(sol[W16] - (sp.diff(sol[W25], x) + sp.diff(G5, x)) / 6))
print('W2_7 + W1_6\'/7:', sp.simplify(sol[W27] + sp.diff(sol[W16], x) / 7))
print('W1_4 - (b3\' + G3\')/4:', sp.simplify(sol[W14] - (sp.diff(sol[b3], x) + sp.diff(G3, x)) / 4))
print('W2_5 + W1_4\'/5:', sp.simplify(sol[W25] + sp.diff(sol[W14], x) / 5))
print('b3 + a2\'/3:', sp.simplify(sol[b3] + sp.diff(sol[a2], x) / 3))
