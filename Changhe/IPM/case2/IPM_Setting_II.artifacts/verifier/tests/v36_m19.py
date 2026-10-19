"""V36: specification M19 (notes of the lead analyst 22:46Z item 2). rho = |x|^gamma, claimed canonical once-subtracted W = (0, -|x|^gamma).
Own inverse: code/charsolve.py (exact radial Green's function per Fourier mode, tail r^p A beyond L = 1e10, p = gamma;
for this exactly homogeneous rho the tail model is exact). Compares W on the polar grid with (0, -|x|^gamma), by radial
band, away from the angular cusp (|cos th| > 0.2) and everywhere, for nt = 256, 1024, 2048 (rho has a |cos th|^gamma
cusp at th = +-pi/2, so the angular truncation converges slowly there). Also the angular L2 error of W2 + |x|^gamma.
usage: python3 tests/v36_m19.py"""
import numpy as np, torch, sys, json, math
sys.path.insert(0, 'code')
from charsolve import CharSolver
dev = 'cuda'


def solver(nt, L=1e10, q=8):
    r1 = 1e-6
    edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12), np.geomspace(0.1, 10, 25)[1:],
                            np.geomspace(10, L, int(round(np.log10(L/10)*5)) + 1)[1:]])
    return CharSolver(edges, q, nt, r1, dev)


for nt in (256, 1024, 2048):
    S = solver(nt)
    r = S.r.cpu().numpy(); cs = S.cs.cpu().numpy()
    for g in (0.3, 0.5, 0.8):
        rho = torch.abs(S.X)**g
        W1, W2 = S.velocity(rho, g)
        W1 = W1.cpu().numpy(); W2 = W2.cpu().numpy(); ex = -np.abs(S.X.cpu().numpy())**g
        rows = {}
        for lo, hi in [(1e-3, 0.1), (0.1, 1), (1, 10), (10, 1e3), (1e3, 1e6)]:
            sb = (r > lo) & (r <= hi)
            sc = r[sb, None]**g
            far = np.abs(cs[sb]) > 0.2
            e1 = np.abs(W1[sb])/sc; e2 = np.abs(W2[sb] - ex[sb])/sc
            rows['%g-%g' % (lo, hi)] = dict(W1_far=float(e1[far].max()), W2_far=float(e2[far].max()),
                                           W1_all=float(e1.max()), W2_all=float(e2.max()),
                                           W2_L2=float(np.sqrt(np.mean(e2**2))))
        print(json.dumps(dict(nt=nt, gamma=g, rel_to_r_gamma=rows)), flush=True)
