"""Refit the Omega coefficients of a stored state onto the beta-consistent basis (gamma_O = -1/beta, mu = 1/beta).
Usage: python3 refit.py in.npz out.npz [beta]  (beta default: the stored beta). Theta coefficients are not refitted (zeroed)."""
import sys, math, numpy as np, torch
from charlib import *
from picard import cheb_q_nodes, r_of_q
torch.set_num_threads(1)
fi, fo = sys.argv[1], sys.argv[2]
P0, cT, cO, NT, NO, K = load_coefs(fi)
beta = float(sys.argv[3]) if len(sys.argv) > 3 else P0.beta
P1 = Params(beta, L=P0.L)
cO = cO.numpy()
crow0 = c_row(P0, P0.gamma_O, K).numpy(); cO *= -2.0 / float(crow0 @ cO[0])
rr = r_of_q(P1, cheb_q_nodes(400, 0.995))
r_t = torch.tensor(rr, dtype=DT)
G = np.stack([radial_basis(P0, r_t, 2 * n, P0.gamma_O, K, deriv=False)[0].numpy() @ cO[n - 1] for n in range(1, NO + 1)], 1)
ph = (np.arange(64) + 0.5) * np.pi / 128
S = np.sin(2 * np.arange(1, NO + 1)[:, None] * ph[None, :])
scale = np.abs(G @ S).max(1) + 1e-300
cN = np.zeros((NO, K)); err = []
for n in range(1, NO + 1):
    H = radial_basis(P1, r_t, 2 * n, P1.gamma_O, K, deriv=False)[0].numpy() / scale[:, None]
    b = G[:, n - 1] / scale
    cn = np.linalg.norm(H, axis=0); cn[cn == 0] = 1
    sol, *_ = np.linalg.lstsq(H / cn, b, rcond=1e-12)
    cN[n - 1] = sol / cn; err.append(np.abs(H @ cN[n - 1] - b).max())
crow1 = c_row(P1, P1.gamma_O, K).numpy()
print('beta %.6f  old exps (%.4f, %.4f) -> new (%.4f, %.4f); max weighted fit error per mode: %s' % (beta, P0.gamma_O, P0.mu, P1.gamma_O, P1.mu, ' '.join('%.1e' % e for e in err[:8])))
print('c old -2, c new %.6f; r range %.3g..%.3g' % (float(crow1 @ cN[0]), rr.min(), rr.max()))
np.savez(fo, cO=cN.reshape(-1), cT=np.zeros(NT * K), beta=beta, L=P1.L, NT=NT, NO=NO, K=K, gamma_T=P1.gamma_T, gamma_O=P1.gamma_O, mu=P1.mu)
