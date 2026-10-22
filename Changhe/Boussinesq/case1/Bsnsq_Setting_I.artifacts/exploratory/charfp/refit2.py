"""Refit Omega coefficients of a stored state onto the beta-consistent basis inside the SVD-truncated subspace used by nk3
(same grid Nr, qmax, same per-mode weights and SVTOL), so that the nk3 starting coordinates represent the old field.
Usage: python3 refit2.py in.npz out.npz Nr M qmax [beta]"""
import sys, os, numpy as np, torch
from charlib import *
from picard import cheb_q_nodes, r_of_q, omega_on_grid
torch.set_num_threads(1)
SVTOL = float(os.environ.get("SVTOL", "1e-2"))
fi, fo, Nr, M, qmax = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
P0, cT, cO, NT, NO, K = load_coefs(fi)
beta = float(sys.argv[6]) if len(sys.argv) > 6 else P0.beta
P1 = Params(beta, L=P0.L)
cO = cO.numpy(); crow0 = c_row(P0, P0.gamma_O, K).numpy(); cO *= -2.0 / float(crow0 @ cO[0])
rr = r_of_q(P1, cheb_q_nodes(Nr, qmax)); ph = (np.arange(M) + 0.5) * np.pi / (2 * M)
r_t = torch.tensor(rr, dtype=DT)
G = np.stack([radial_basis(P0, r_t, 2 * n, P0.gamma_O, K, deriv=False)[0].numpy() @ cO[n - 1] for n in range(1, NO + 1)], 1)
S = np.sin(2 * np.arange(1, NO + 1)[:, None] * ph[None, :])
scale = np.abs(G @ S).max(1) + 1e-300
cN = np.zeros((NO, K)); err = []
for n in range(1, NO + 1):
    H = radial_basis(P1, r_t, 2 * n, P1.gamma_O, K, deriv=False)[0].numpy() / scale[:, None]
    u, s, vt = np.linalg.svd(H, full_matrices=False); keep = s > SVTOL * s[0]
    b = G[:, n - 1] / scale
    cN[n - 1] = vt[keep].T @ ((u[:, keep].T @ b) / s[keep])
    err.append(np.abs(H @ cN[n - 1] - b).max())
crow1 = c_row(P1, P1.gamma_O, K).numpy()
print('beta %.6f exps (%.4f,%.4f)->(%.4f,%.4f) fit err per mode %s' % (beta, P0.gamma_O, P0.mu, P1.gamma_O, P1.mu, ' '.join('%.1e' % e for e in err[:8])))
print('c new %.6f' % float(crow1 @ cN[0]))
np.savez(fo, cO=cN.reshape(-1), cT=np.zeros(NT * K), beta=beta, L=P1.L, NT=NT, NO=NO, K=K, gamma_T=P1.gamma_T, gamma_O=P1.gamma_O, mu=P1.mu)
