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
msk, U1, U2, rg, f = S.velocity(fr, region=4.0)
Xt, Yt = S.X[msk], S.Y[msk]
z = torch.zeros(1, dtype=DT, device=dev)
e1 = U1 - (f1(Xt, Yt) - f1(z, z)); e2 = U2 - (f2(Xt, Yt) - f2(z, z))
A = torch.stack([torch.ones_like(Xt), Xt, Yt, Xt**2, Xt*Yt, Yt**2], 1)
for e in (e1, e2):
    c = torch.linalg.lstsq(A, e[:, None]).solution.ravel()
    print('fit const,x,y,xx,xy,yy:', c.cpu().numpy(), ' resid', (e - A @ c).abs().max().item())
i = e1.abs().argmax()
print('spike at', Xt[i].item(), Yt[i].item(), e1[i].item())
top = torch.topk(e1.abs(), 8)
for j in top.indices: print(Xt[j].item(), Yt[j].item(), e1[j].item())
