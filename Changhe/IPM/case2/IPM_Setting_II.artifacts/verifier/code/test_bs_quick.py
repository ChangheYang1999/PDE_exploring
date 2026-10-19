"""Quick manufactured test of the Ewald-split Cartesian BS (localized + growth), several sigma/h."""
import numpy as np, sympy as sp, torch, sys, time
sys.path.insert(0, 'code')
from bs_cartesian import CartesianBS, dev, DT
x, y = sp.symbols('x y', real=True)
def tfun(e):
    f = sp.lambdify((x, y), e, modules=[{'exp': torch.exp, 'sin': torch.sin, 'cos': torch.cos, 'sqrt': torch.sqrt}, 'math'])
    return lambda X, Y: f(X, Y) * torch.ones_like(X)
Q = (x - 0.7)**2 + 2*(y + 0.4)**2 + sp.Rational(1, 2)*(x - 0.7)*(y + 0.4)
tests = {
  'C: localized exp(-Q)': sp.exp(-Q),
  'B: growth k=0.6 (1+Q)^1.3': (1 + Q)**sp.Rational(13, 10),
  'D: growth + oscillation': (1 + Q)**sp.Rational(13, 10) + sp.Rational(3, 10)*sp.sin(2*x)*sp.exp(-(x**2 + y**2)/4),
}
cfgs = [tuple(map(float, a.split(','))) for a in sys.argv[1:]] or [(12, 0.05, 7, 11, 4)]
for name, phi in tests.items():
    rho = -(sp.diff(phi, x, 2) + sp.diff(phi, y, 2))
    fr, f1, f2 = tfun(rho), tfun(-sp.diff(phi, x, y)), tfun(sp.diff(phi, x, 2))
    for (B, h, L1, L2, sgh) in cfgs:
        t0 = time.time()
        S = CartesianBS(B, h, L1, L2, sigma=sgh * h)
        msk, U1, U2, rg, f = S.velocity(fr, region=4.0)
        Xt, Yt = S.X[msk], S.Y[msk]
        z = torch.zeros(1, dtype=DT, device=dev)
        e1 = U1 - (f1(Xt, Yt) - f1(z, z)); e2 = U2 - (f2(Xt, Yt) - f2(z, z))
        rr = torch.sqrt(Xt**2 + Yt**2)
        out = []
        for Rm in (1, 2, 4):
            m = rr < Rm
            out.append(f'|X|<{Rm}: {max(e1[m].abs().max().item(), e2[m].abs().max().item()):.2e}')
        sc = max(U1.abs().max().item(), U2.abs().max().item())
        print(f'{name:28s} B={B:g} h={h:g} L1={L1:g} L2={L2:g} sigma={sgh:g}h: ' + ', '.join(out) + f' (max|U| {sc:.2e}) t={time.time()-t0:.1f}s', flush=True)
