"""Export a reproduced solution as plain arrays for independent checking: polar grid r[Nr] x theta[M] (open quadrant, Radau
radii incl. r = 0), rho, psi, U1, U2, W1, W2, c_l, R, plus the far-field extension parameters. Usage: export_fields.py <npz> <out>"""
import sys, numpy as np, torch
sys.path.insert(0, 'src')
import diag
m, b, cl, d = diag.load(sys.argv[1], device='cuda'); m.k_tail = 1 / cl
fl = m.fields(b); rho = m.rho_from_b(b); psi = m.psi(fl); U1, U2 = m.velocity(fl)
r = m.rad.rR; th = m.ang.theta
W1 = cl * r[:, None] * torch.cos(th)[None, :] + U1; W2 = cl * r[:, None] * torch.sin(th)[None, :] + U2
a = m.wR[:, None] * b
np.savez(sys.argv[2], r=r.cpu().numpy(), theta=th.cpu().numpy(), rho=rho.cpu().numpy(), a=a.cpu().numpy(), psi=psi.cpu().numpy(),
         U1=U1.cpu().numpy(), U2=U2.cpu().numpy(), W1=W1.cpu().numpy(), W2=W2.cpu().numpy(), c_l=cl, c=m.psi_xy0(fl).item(),
         R=float(d['R']), N=m.N, M=m.M, L=m.L, gamma=m.gamma, k_tail=1 / cl, x_star=float(d['x_star']) if 'x_star' in d.files else np.nan,
         note='disk closure (SPEC N3a): unknowns on r<=R, far field rho(r,theta) = (r/R)^(1/c_l) rho(R,theta) for r>R; grid = Chebyshev-Radau radii x midpoint angles on (0, pi/2); rho = x^2 y a')
print("exported", sys.argv[2], "shapes", rho.shape, "c_l", cl, "max rho", rho.max().item())
