# Independent check (lead) of the axis coefficients G_5, G_7 of the multi-seed cone solutions of 6.3.1 (r):
# local system W.grad f = f, div W = A + 1, curl W = -f_s with f = g y + v, W = (A s, y) + V, V = 0 on the axis.
import sympy as sp
r, A, g, C3, C5, C7, y = sp.symbols('r A g C3 C5 C7 y', positive=True)
s = -r
lam = 2 / A
b = g / (2 * (A - 1))
N = 9
# unknown G_j(r) for odd j; V_1 = sum a_k y^k (k even, a_0 = 0), V_2 = sum b_k y^k (k odd)
G3 = C3 * r**(-lam)
G5 = -b * lam * (lam + 1) * C3 * r**(-lam - 2) / 20 + C5 * r**(-2 * lam)
G7c = (b * (b + 1) * lam * (lam + 1) * (lam + 2) * (lam + 3) * C3 * r**(-lam - 4) / 1680
       - ((2 * lam) * (2 * lam + 1) * b * C5 / 42 + lam * (3 - 2 * lam) * C3**2 / (40 * (A - 1))) * r**(-2 * lam - 2)
       + C7 * r**(-3 * lam))
dds = lambda F: -sp.diff(F, r)          # d/ds with s = -r
G = {1: 0, 3: G3, 5: G5, 7: G7c}
a = {0: 0}; bb = {}
# div: a_k' + (k+1) b_{k+1} = 0 (k even); curl: b_j' - (j+1) a_{j+1} = -G_j' (j odd)
for k in range(0, 8, 2):
    bb[k + 1] = -dds(a[k]) / (k + 1)
    j = k + 1
    a[j + 1] = (dds(bb[j]) + dds(G[j])) / (j + 1)
V1 = sum(a[k] * y**k for k in a)
V2 = sum(bb[k] * y**k for k in bb)
f = g * y + sum(G[j] * y**j for j in G)
res = (A * s + V1) * dds(f) + (y + V2) * sp.diff(f, y) - f
res = sp.expand(res)
for j in (1, 3, 5, 7):
    c = sp.simplify(res.coeff(y, j))
    print('y^%d residual:' % j, c)
# check div and curl exactly up to the truncation order
div = sp.expand(dds(V1) + sp.diff(V2, y))
curl = sp.expand(dds(V2) - sp.diff(V1, y) + dds(f))
print('div coeffs', [sp.simplify(div.coeff(y, k)) for k in range(0, 7)])
print('curl coeffs', [sp.simplify(curl.coeff(y, k)) for k in range(0, 8)])
