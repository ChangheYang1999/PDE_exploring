"""Verifier: check the q = h_x equation (PROMPT 3B) is d_x(pert) - a_tr*(pert), exactly (generic functions)."""
import sympy as sp
x, y = sp.symbols('x y', real=True)
cl, ch = sp.symbols('c_l c_h')            # bar c_l, c[h]
F = lambda n: sp.Function(n)(x, y)
rb, h, eps, V1, V2, u1, u2 = [F(n) for n in ('rb', 'h', 'eps', 'V1', 'V2', 'u1', 'u2')]
# Vbar = (V1, V2) = cl X + Ubar (generic; no relation needed), U[h] = (u1,u2), V[h] = U[h] + ch X
G = x * sp.diff(rb, x) + y * sp.diff(rb, y)
Vh1, Vh2 = u1 + ch * x, u2 + ch * y
pert = (V1 * sp.diff(h, x) + V2 * sp.diff(h, y) - h + u1 * sp.diff(rb, x) + u2 * sp.diff(rb, y) + ch * G
        + Vh1 * sp.diff(h, x) + Vh2 * sp.diff(h, y) + eps)          # = 0
atr = sp.diff(V2, x) / V2
q = sp.diff(h, x)
W1, W2 = V1 + Vh1, V2 + Vh2
g1, g2 = sp.diff(rb + h, x), sp.diff(rb + h, y)
Uq1, Uq2 = sp.diff(u1, x), sp.diff(u2, x)       # U[q] = d_x U[h]
d = 1 - sp.diff(V1, x) + atr * V1
B1, B2 = sp.diff(rb, x, x) - atr * sp.diff(rb, x), sp.diff(rb, x, y) - atr * sp.diff(rb, y)
C = sp.diff(G, x) - atr * G
R = -sp.diff(eps, x) + atr * eps
qeq = (W1 * sp.diff(q, x) + W2 * sp.diff(q, y) - (d - ch) * q + Uq1 * g1 + Uq2 * g2
       - (R - atr * h - (u1 * B1 + u2 * B2) - ch * C + atr * (Vh1 * sp.diff(h, x) + Vh2 * sp.diff(h, y))))
combo = sp.diff(pert, x) - atr * pert
print('q-equation == d_x(pert) - a_tr*(pert):', sp.simplify(sp.expand(qeq - combo)) == 0)
# strict linearization: drop quadratic terms (V[h].grad q, U[q].grad h, a_tr V[h].grad h, c q)
