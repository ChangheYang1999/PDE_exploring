"""Tests for code/charsolve.py: (1) marching on a manufactured transport problem with exact solution;
(2) torch per-mode Biot-Savart matrices vs code/polar_inverse.py and vs an exact growth field; (3) moments."""
import numpy as np, torch, sys, time, sympy as sp
sys.path.insert(0, 'code')
from charsolve import CharSolver
from polar_inverse import PolarGrid
dev = 'cuda'
# (1) manufactured transport: V = (x(1/2 - kap*lam*(y/3) sech^2(y/3)), lam*y), xi = x exp(kap tanh(y/3)) solves V.grad xi = xi/2
for q, nt in ((8, 32), (8, 64), (12, 64), (8, 128)):
    for r1 in (1e-4, 1e-6):
        edges = np.concatenate([[0.0], np.geomspace(r1, 0.5, 14), np.linspace(0.5, 10, 30)[1:]])
        S = CharSolver(edges, q, nt, r1, dev)
        kap, lam = 0.4, 2.0
        X, Y = S.X, S.Y
        V1 = X*(0.5 - kap*lam*(Y/3)/torch.cosh(Y/3)**2); V2 = lam*Y
        Vr = V1*S.cs + V2*S.sn; Vt_r = (-V1*S.sn + V2*S.cs)/S.R
        z0 = r1*torch.cos(S.th)
        t0 = time.time(); z = S.march(Vr, Vt_r, z0); torch.cuda.synchronize(); dt = time.time()-t0
        ex = (X*torch.exp(kap*torch.tanh(Y/3)))[S.p0*q:]
        err = (z-ex).abs().max().item()
        print(f'march q={q} nt={nt} r1={r1:.0e}: max|xi-exact| (r<=10) = {err:.2e}, max|xi| {ex.abs().max().item():.1f}, {dt:.2f}s')
# (2) BS matrices vs polar_inverse numpy, growth field phi = (1+Q)^1.3 (rho ~ r^0.6)
x, y = sp.symbols('x y', real=True)
Q = (x-0.7)**2 + 2*(y+0.4)**2 + 0.5*(x-0.7)*(y+0.4)
phi = (1+Q)**sp.Rational(13, 10)
rho_e = -(sp.diff(phi, x, 2)+sp.diff(phi, y, 2)); U1e = -sp.diff(phi, x, y); U2e = sp.diff(phi, x, 2)
fr, f1, f2 = [sp.lambdify((x, y), e, 'numpy') for e in (rho_e, U1e, U2e)]
edges = np.concatenate([[0.0], np.geomspace(1e-6, 0.25, 12), np.linspace(0.25, 8, 30)[1:], np.geomspace(8, 1e10, 50)[1:]])
S = CharSolver(edges, 12, 128, 1e-6, dev)
G = S.G
rho = fr(G.X, G.Y)
t0 = time.time()
W1, W2 = S.velocity(torch.tensor(rho, device=dev), 0.6); torch.cuda.synchronize(); dt = time.time()-t0
U1n, U2n = G.velocity(rho)
d = max(np.abs(W1.cpu().numpy()-U1n).max(), np.abs(W2.cpu().numpy()-U2n).max())
for Rm in (2, 5, 10, 100):
    msk = G.R < Rm
    # charsolve.velocity returns 2 Re W - rho/2 (valid for rho(0) = 0); this test field has rho(0) != 0: add rho(0)/2
    E = max(np.abs(W1.cpu().numpy()-(f1(G.X, G.Y)-f1(0., 0.)))[msk].max(), np.abs(W2.cpu().numpy()+fr(0., 0.)/2-(f2(G.X, G.Y)-f2(0., 0.)))[msk].max())
    print(f'BS torch vs exact, |X|<{Rm}: {E:.2e}')
print(f'BS torch vs numpy polar_inverse (no tail there): {d:.2e}  time {dt:.3f}s  Nr={S.Nr}')
# (3) moments: lead's test density rho = x^2 (1+0.5y+0.3x)^2 (1+r^2)^{(p-4)/2}, p = 1/2: exact c = 1/6, b = psi_yy(0) = -0.1
#     (V12(c)); and rho = x^2 (1+a y)^2 e^{-r^2}: c = a/4, b = 0 (V11)
X, Y = G.X, G.Y
for name, rho, ce, be in (('lead r^1/2', X**2*(1+0.5*Y+0.3*X)**2*(1+X**2+Y**2)**((0.5-4)/2), 1/6, -0.1),
                          ('gauss a=0.7', X**2*(1+0.7*Y)**2*np.exp(-(X**2+Y**2)), 0.175, 0.0)):
    c, b = S.moments(torch.tensor(rho, device=dev), 0.5)
    print(f'moments {name}: c = {c.item():.13f} (exact {ce:.13f}), b = {b.item():.13f} (exact {be})')
