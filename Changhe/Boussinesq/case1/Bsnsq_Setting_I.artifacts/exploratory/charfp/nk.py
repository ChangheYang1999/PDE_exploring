"""Newton-Krylov for the Psi-only characteristic fixed point (prototype), fixed beta.
Unknowns: per-mode orthonormal radial coordinates y_n = R_n cO_n, where Q_n R_n = H_n / scale_r is the weighted radial
basis on the grid (so |y| measures weighted grid values of the Omega modes). Residual F(y) = y - y(G(cO(y))).
Jacobian-vector products by forward differences of F; GMRES with restart m; backtracking on |F|.
Usage: python3 nk.py state.npz out_prefix n_newton m_gmres Nr M [qmax] [beta]"""
import sys, time, math, numpy as np, torch
from scipy.sparse.linalg import LinearOperator, gmres
from charlib import *
from picard import cheb_q_nodes, r_of_q, omega_char_grid, project, omega_on_grid
torch.set_num_threads(1)

f, pre = sys.argv[1], sys.argv[2]
nnew, mg, Nr, M = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
qmax = float(sys.argv[7]) if len(sys.argv) > 7 else 0.99
P, cT, cO_t, NT, NO, K = load_coefs(f)
if len(sys.argv) > 8: P.beta = float(sys.argv[8])          # basis exponents stay frozen (stored or beta-3 values)
cO0 = cO_t.numpy().copy()
crow = c_row(P, P.gamma_O, K).numpy()
cO0 *= -2.0 / float(crow @ cO0[0])
rr = r_of_q(P, cheb_q_nodes(Nr, qmax)); ph = (np.arange(M) + 0.5) * np.pi / (2 * M)
r_t = torch.tensor(rr, dtype=DT)
# fixed weights from the initial state's Omega size on each radius
scale_r = np.max(np.abs(omega_on_grid(P, cO0, NO, K, rr, ph)), axis=1) + 1e-300
Hs = [radial_basis(P, r_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_r[:, None] for n in range(1, NO + 1)]
U_, S_, Vt_ = [], [], []
for A in Hs:
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    keep = s > 1e-13 * s[0]
    U_.append(u[:, keep]); S_.append(s[keep]); Vt_.append(vt[keep])
dims = [len(s) for s in S_]; NY = sum(dims)
print('grid Nr %d M %d, NO %d K %d, beta %.6f, unknowns %d (kept singular values per mode %s)' % (Nr, M, NO, K, P.beta, NY, dims[:4]), flush=True)


def y_of_c(cO):
    return np.concatenate([S_[n] * (Vt_[n] @ cO[n]) for n in range(NO)])


def c_of_y(y):
    cO = np.zeros((NO, K)); i = 0
    for n in range(NO):
        d = dims[n]; cO[n] = Vt_[n].T @ (y[i:i + d] / S_[n]); i += d
    return cO


def y_of_g(g):
    """weighted least-squares coordinates of grid mode values g (Nr, NO)."""
    return np.concatenate([U_[n].T @ (g[:, n] / scale_r) for n in range(NO)])


nev = [0]
def F(y):
    cO = c_of_y(y)
    cO = cO * (-2.0 / float(crow @ cO[0]))       # c = -2 (the map is homogeneous of degree 0 after a0 normalization)
    Om1, tab, out = omega_char_grid(P, torch.tensor(cO, dtype=DT), NO, K, rr, ph, h=0.02, r_stop=1e-3)
    g, trunc = project(Om1, ph, NO)
    yg = y_of_g(g)
    c1 = float(crow @ c_of_y(yg)[0]); a0 = -2.0 / c1
    nev[0] += 1
    return y_of_c(cO) - a0 * yg, a0


y = y_of_c(cO0)
t0 = time.time(); Fy, a0 = F(y); nF = np.linalg.norm(Fy)
print('F0 |F| %.6e  |y| %.6e  a0 %.6f  max|F| %.3e  (%.0fs)' % (nF, np.linalg.norm(y), a0, np.abs(Fy).max(), time.time() - t0), flush=True)
for k in range(nnew):
    eps = 1e-5 * max(1.0, np.linalg.norm(y))
    def mv(v):
        nv = np.linalg.norm(v)
        if nv == 0: return np.zeros_like(v)
        Fp, _ = F(y + (eps / nv) * v)
        return (Fp - Fy) * (nv / eps)
    J = LinearOperator((NY, NY), matvec=mv, dtype=float)
    it_log = []
    def cb(rk): it_log.append(float(rk)); print('   gmres it %d rel res %.3e  (%d F evals, %.0fs)' % (len(it_log), rk, nev[0], time.time() - t0), flush=True)
    dy, info = gmres(J, -Fy, restart=mg, maxiter=1, rtol=1e-3, callback=cb, callback_type='pr_norm')
    lam = 1.0
    while lam > 1e-3:
        yn = y + lam * dy; Fn, a0n = F(yn); nFn = np.linalg.norm(Fn)
        print(' newton %d lam %.3g |F| %.6e -> %.6e a0 %.6f max|F| %.3e |dy|/|y| %.3e (%.0fs)' % (k, lam, nF, nFn, a0n, np.abs(Fn).max(), lam * np.linalg.norm(dy) / np.linalg.norm(y), time.time() - t0), flush=True)
        if nFn < nF: break
        lam *= 0.5
    if nFn >= nF:
        print('no decrease; stop', flush=True); break
    y, Fy, nF, a0 = yn, Fn, nFn, a0n
    cO = c_of_y(y); cO *= -2.0 / float(crow @ cO[0])
    np.savez(pre + '.npz', cO=cO.reshape(-1), cT=np.zeros(NT * K), beta=P.beta, L=P.L, NT=NT, NO=NO, K=K, a0=a0,
             gamma_T=P.gamma_T, gamma_O=P.gamma_O, mu=P.mu, Fnorm=nF)
