import numpy as np, sympy as sp, torch, sys, time
sys.path.insert(0, 'code')
from bs_cartesian import CartesianBS, dev, DT
x, y = sp.symbols('x y', real=True)
def tfun(e):
    f = sp.lambdify((x, y), e, modules=[{'exp': torch.exp, 'sin': torch.sin, 'cos': torch.cos, 'sqrt': torch.sqrt}, 'math'])
    return lambda X, Y: f(X, Y) * torch.ones_like(X)
Q = (x - 0.7)**2 + 2*(y + 0.4)**2 + sp.Rational(1, 2)*(x - 0.7)*(y + 0.4)
phi = (1 + Q)**sp.Rational(13, 10)
rho = -(sp.diff(phi, x, 2) + sp.diff(phi, y, 2))
fr, f1, f2 = tfun(rho), tfun(-sp.diff(phi, x, y)), tfun(sp.diff(phi, x, 2))
S = CartesianBS(12, 0.05, 7, 11)
for nmid, q in [(8, 16), (32, 16), (64, 24), (128,24)]:
    S.nmid = nmid
    msk, U1, U2, rg, f = S.velocity(fr, region=4.0, q=q)
    Xt, Yt = S.X[msk], S.Y[msk]
    z = torch.zeros(1, dtype=DT, device=dev)
    e1 = U1 - (f1(Xt, Yt) - f1(z, z)); e2 = U2 - (f2(Xt, Yt) - f2(z, z))
    print(nmid, q, max(e1.abs().max().item(), e2.abs().max().item()), flush=True)
