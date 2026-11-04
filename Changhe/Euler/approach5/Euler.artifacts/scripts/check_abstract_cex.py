"""Check the parameter algebra of the kinematic bracket example in an external referee answer.

Question: for every 0 < c < 1/2, do the constants of the construction satisfy the stated inequalities (4), the
flux/stable matching (3)/(7), the divergence identities, the expansion of the quotient Lorenz map, and the
regularity exponent (a-h)/lambda = 2 at the added saddles?  Also checks [X,W] = aW and div X = -d on the core
box symbolically.  Pass criterion: all checks True on a grid of c values (exact rationals where possible).
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
ok_all = True


def report(name, ok):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS  ' if ok else 'FAIL  ') + name)


cs = sp.symbols('c', positive=True)
a, d = 1 + cs, 3 * cs
k = a - d
b = (a + k) / 2
L = b + k
X = sp.Matrix([L * x, -a * y, -b * z])
W = sp.Matrix([0, 1, 0])
V = sp.Matrix([x, y, z])
jac = lambda F: F.jacobian(V)
br = jac(W) * X - jac(X) * W
report('core: [X,W] = a W (symbolic in c)', sp.simplify(br - a * W) == sp.zeros(3, 1))
report('core: div X = -d (symbolic in c)', sp.simplify(sum(sp.diff(X[i], V[i]) for i in range(3)) + d) == 0)
lam = k / 4
h = d + 2 * lam
report('saddle block: div = 2 lambda - h = -d', sp.simplify(2 * lam - h + d) == 0)
report('saddle block: (a-h)/lambda = 2', sp.simplify((a - h) / lam - 2) == 0)
import mpmath as mpm
mpm.mp.dps = 50
grid_ok = True
for n in range(1, 50):
    cv = mpm.mpf(n) / 100
    av, dv = 1 + cv, 3 * cv
    kv = av - dv
    bv = (av + kv) / 2
    Lv = bv + kv
    q = bv / Lv
    K = (2 + 1 / q) / 2
    T = mpm.log(K * q) / kv
    rho = mpm.exp(-av * T)
    delta = (1 - rho) / 4
    eps = min(delta, 1 / K - mpm.mpf(1) / 2) / 2
    m = (rho * (1 + 2 * delta) + 1 + delta) / 2
    conds = [kv < bv, bv < av, mpm.mpf(1) / 2 < q, q < 1, abs(Lv - av - bv + dv) < mpm.mpf(10) ** -40,
             1 / q < K, K < 2, T > 0, 0 < rho, rho < 1, 0 < eps, eps < delta,
             K * (mpm.mpf(1) / 2 + eps) < 1, rho * (1 + 2 * delta) < m, m < 1 + delta,
             abs(bv * K * rho - Lv * mpm.exp(-dv * T)) < mpm.mpf(10) ** -40,  # flux matching (7)
             K * q > 1]  # quotient Lorenz map expanding: derivative K q |x|^(q-1) >= K q > 1
    if not all(conds):
        grid_ok = False
        print('  failure at c =', cv, conds)
ok_all &= grid_ok
report('parameter inequalities (4), flux matching (7), Kq > 1 for c = 0.01..0.49', grid_ok)
print()
print('ALL PASS' if ok_all else 'SOME FAILED')
