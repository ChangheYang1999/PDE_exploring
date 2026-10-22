import torch, math
from jets import *
torch.manual_seed(0)
x0 = torch.rand(5, dtype=DT) + 0.3; e0 = torch.rand(5, dtype=DT) + 0.2
X = Jet.var(x0, 0, 4); H = Jet.var(e0, 1, 4)
E = 1 + X * X + H.ipow(6)
F = X * H * E.pow(1/3) * (H * H * E.pow(-1/3))
# compare with autograd derivatives
def f(x, e):
    E = 1 + x**2 + e**6
    return x * e * E**(1/3) * e**2 * E**(-1/3)
D = deriv_values(F)
x = x0.clone().requires_grad_(True); e = e0.clone().requires_grad_(True)
def grads(fun, n_x, n_e):
    g = fun
    for _ in range(n_x): g = torch.autograd.grad(g.sum(), x, create_graph=True)[0]
    for _ in range(n_e): g = torch.autograd.grad(g.sum(), e, create_graph=True)[0]
    return g
mx = 0
for (i, j), v in D.items():
    ref = grads(f(x, e), i, j)
    mx = max(mx, float(((v - ref).abs() / (ref.abs() + 1)).max()))
print('max rel err jets vs autograd', mx)
