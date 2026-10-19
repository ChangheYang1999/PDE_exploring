"""V42 (notes of the lead analyst 23:45Z item 3): independent strain c = psi_xy(0), b = psi_yy(0) and DV(0) eigenvalues of lead forward states
(g on lr x th, rho = r^p g). Own inverse code/charsolve.py (exact radial Green's function per mode on Gauss-Legendre bands, tail
r^p A beyond L = e^hi, A = last ring), rho interpolated in lr (linear / cubic spline), rho = 0 below the inner grid edge
(or below a raised cut lrcut, to test inner sensitivity). Usage: python3 tests/v42_strain.py FILE p [dev]."""
import numpy as np, torch, sys, math, json
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from charsolve import CharSolver
f = sys.argv[1]; p = float(sys.argv[2]); dev = sys.argv[3] if len(sys.argv) > 3 else 'cuda'
DT = torch.float64; l = 1/p
d = np.load(f, allow_pickle=True)
g, lr, th = d['g'], d['lr'], d['th']
nt = len(th)
assert np.allclose(th, 2*np.pi*np.arange(nt)/nt)
hi = float(lr[-1]); lo = float(lr[0])
for nb in (1, 2):
    L = math.exp(hi); r1 = math.exp(lo)
    edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, int(round(np.log10(0.1/r1)*3*nb)) + 1), np.geomspace(0.1, 10, 25*nb)[1:],
                            np.geomspace(10, L, int(round(np.log10(L/10)*5*nb)) + 1)[1:]])
    S = CharSolver(edges, 8, nt, r1, dev)
    rr = S.r.cpu().numpy(); lrr = np.log(np.maximum(rr, 1e-300))
    for kind in ('linear', 'cubic'):
        for lrcut in (lo, -8.0, -6.0):
            if kind == 'linear' and lrcut != lo:
                continue
            if kind == 'linear':
                G = np.stack([np.interp(lrr, lr, g[:, j]) for j in range(nt)], 1)
            else:
                G = CubicSpline(lr, g, axis=0)(np.clip(lrr, lr[0], lr[-1]))
            G[lrr < lrcut] = 0.0
            rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device=dev)
            c, b = S.moments(rho, p)
            c = float(c); b = float(b)
            M = np.array([[l - c, -b], [-b, l + c]])
            ev = np.linalg.eigvalsh(M)
            print(json.dumps(dict(file=f.split('/')[-1], p=p, bands=nb, nr=len(rr), interp=kind, lrcut=lrcut, c=round(c, 7),
                                  psi_yy=round(b, 7), m1=round(ev[0], 6), m2=round(ev[1], 6))), flush=True)
