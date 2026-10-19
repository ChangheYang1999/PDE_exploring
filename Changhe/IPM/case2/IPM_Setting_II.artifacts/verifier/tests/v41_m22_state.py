"""V41 (specification M22, lead request 23:13Z item 2): independent DV(0) of the lead forward state analysis/runs/pf_cos2_p05_deep.npz
(g on lr x th, rho = r^p g, p = 0.5, l = 2). Own inverse code/charsolve.py (exact radial Green's function per Fourier mode,
Gauss-Legendre bands, tail r^p A beyond L = e^10 with A the last ring), rho interpolated in lr (linear and cubic spline;
no angular interpolation, nt = 128 = lead grid), rho = 0 for r < e^-12. DV(0) = [[l - c, -b], [-b, l + c]], c = psi_xy(0),
b = psi_yy(0) (W1 = -psi_y, W2 = psi_x, psi_xx + psi_yy = -rho_x(0) = 0)."""
import numpy as np, torch, sys, math, json
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from charsolve import CharSolver
dev = 'cuda'; DT = torch.float64
d = np.load('runs/pf_cos2_p05_deep.npz')
g, lr, th = d['g'], d['lr'], d['th']; p = 0.5; l = 1/p
nt = len(th)
assert np.allclose(th, 2*np.pi*np.arange(nt)/nt)
for nb in (1, 2):
    L = math.exp(10.0); r1 = 1e-6
    edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12*nb), np.geomspace(0.1, 10, 25*nb)[1:],
                            np.geomspace(10, L, int(round(np.log10(L/10)*5*nb)) + 1)[1:]])
    S = CharSolver(edges, 8, nt, r1, dev)
    rr = S.r.cpu().numpy(); lrr = np.log(np.maximum(rr, 1e-300))
    for kind in ('linear', 'cubic'):
        if kind == 'linear':
            G = np.stack([np.interp(lrr, lr, g[:, j]) for j in range(nt)], 1)
        else:
            G = CubicSpline(lr, g, axis=0)(np.clip(lrr, lr[0], lr[-1]))
        G[lrr < lr[0]] = 0.0
        rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device=dev)
        c, b = S.moments(rho, p)
        c = float(c); b = float(b)
        M = np.array([[l - c, -b], [-b, l + c]])
        ev = np.linalg.eigvalsh(M)
        print(json.dumps(dict(bands=nb, interp=kind, c=c, psi_yy=b, DV0=M.tolist(), eig=ev.tolist(),
                              lead=[0.6085, 3.3915])), flush=True)
