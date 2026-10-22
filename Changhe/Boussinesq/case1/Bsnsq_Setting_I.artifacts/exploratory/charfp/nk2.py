"""Newton-Krylov for the Psi-only characteristic fixed point with beta as an unknown (prototype).
Unknowns z = (y, beta), y = per-mode weighted radial SVD coordinates of the Omega coefficients (as in nk.py).
Equations: E1 = F(y, beta) + (c(y) + 2) n_c   (F as in nk.py; c-functional of F vanishes identically, so E1 = 0 iff
           F = 0 and c(y) = -2),
           E2 = t . (y - y0)                   (dilation gauge; t = coordinates of r d_r Omega at the initial state).
Dilation Omega(X) -> Omega(L X) preserves beta, a0, c, so at fixed beta the Jacobian has a null direction; the gauge
removes it and beta takes up the corresponding cokernel direction. Basis exponents stay frozen at the stored values.
Usage: python3 nk2.py state.npz out_prefix n_newton m_gmres Nr M [qmax] [beta0]"""
import sys, time, math, numpy as np, torch
from scipy.sparse.linalg import LinearOperator, gmres
from charlib import *
from picard import cheb_q_nodes, r_of_q, omega_char_grid, project, omega_on_grid
torch.set_num_threads(1)

f, pre = sys.argv[1], sys.argv[2]
nnew, mg, Nr, M = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
qmax = float(sys.argv[7]) if len(sys.argv) > 7 else 0.99
P, cT, cO_t, NT, NO, K = load_coefs(f)
if len(sys.argv) > 8: P.beta = float(sys.argv[8])
beta0 = P.beta
cO0 = cO_t.numpy().copy()
crow = c_row(P, P.gamma_O, K).numpy()
cO0 *= -2.0 / float(crow @ cO0[0])
rr = r_of_q(P, cheb_q_nodes(Nr, qmax)); ph = (np.arange(M) + 0.5) * np.pi / (2 * M)
r_t = torch.tensor(rr, dtype=DT)
scale_r = np.max(np.abs(omega_on_grid(P, cO0, NO, K, rr, ph)), axis=1) + 1e-300
Hs = [radial_basis(P, r_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_r[:, None] for n in range(1, NO + 1)]
U_, S_, Vt_ = [], [], []
for A in Hs:
    u, s, vt = np.linalg.svd(A, full_matrices=False)
    keep = s > 1e-13 * s[0]
    U_.append(u[:, keep]); S_.append(s[keep]); Vt_.append(vt[keep])
dims = [len(s) for s in S_]; NY = sum(dims)


def y_of_c(cO):
    return np.concatenate([S_[n] * (Vt_[n] @ cO[n]) for n in range(NO)])


def c_of_y(y):
    cO = np.zeros((NO, K)); i = 0
    for n in range(NO):
        d = dims[n]; cO[n] = Vt_[n].T @ (y[i:i + d] / S_[n]); i += d
    return cO


def y_of_g(g):
    return np.concatenate([U_[n].T @ (g[:, n] / scale_r) for n in range(NO)])


def mode_values(cO, r):
    rt = torch.tensor(r, dtype=DT)
    return np.stack([radial_basis(P, rt, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() @ cO[n - 1] for n in range(1, NO + 1)], 1)


# c-functional in y coordinates and the vector n_c with w . n_c = 1
w = np.zeros(NY); w[:dims[0]] = (Vt_[0] @ crow) / S_[0]
n_c = w / (w @ w)
y0 = y_of_c(cO0)
# dilation tangent r d_r Omega (central difference in log r)
eta = 1e-4
t = y_of_g((mode_values(cO0, rr * (1 + eta)) - mode_values(cO0, rr * (1 - eta))) / (2 * eta))
t /= np.linalg.norm(t)
print('grid Nr %d M %d, NO %d K %d, beta0 %.6f, unknowns %d + beta; c(y0) %.6f; |t.y0|/|y0| %.3e' % (Nr, M, NO, K, beta0, NY, w @ y0, abs(t @ y0) / np.linalg.norm(y0)), flush=True)

nev = [0]
def E(z):
    y, beta = z[:NY], z[NY]
    P.beta = beta
    cO = c_of_y(y)
    cO = cO * (-2.0 / float(crow @ cO[0]))
    Om1, tab, out = omega_char_grid(P, torch.tensor(cO, dtype=DT), NO, K, rr, ph, h=0.02, r_stop=1e-3)
    g, trunc = project(Om1, ph, NO)
    yg = y_of_g(g)
    c1 = float(crow @ c_of_y(yg)[0]); a0 = -2.0 / c1
    nev[0] += 1
    F = y_of_c(cO) - a0 * yg
    return np.concatenate([F + (w @ y + 2.0) * n_c, [t @ (y - y0)]]), a0


z = np.concatenate([y0, [beta0]])
t0 = time.time(); Ez, a0 = E(z); nE = np.linalg.norm(Ez)
print('E0 |E| %.6e  a0 %.6f  beta %.6f  max|E| %.3e  (%.0fs)' % (nE, a0, z[NY], np.abs(Ez).max(), time.time() - t0), flush=True)
for k in range(nnew):
    eps = 1e-5 * max(1.0, np.linalg.norm(z))
    def mv(v):
        nv = np.linalg.norm(v)
        if nv == 0: return np.zeros_like(v)
        Ep, _ = E(z + (eps / nv) * v)
        return (Ep - Ez) * (nv / eps)
    J = LinearOperator((NY + 1, NY + 1), matvec=mv, dtype=float)
    it_log = []
    def cb(rk): it_log.append(float(rk)); print('   gmres it %d rel res %.3e  (%d E evals, %.0fs)' % (len(it_log), rk, nev[0], time.time() - t0), flush=True)
    dz, info = gmres(J, -Ez, restart=mg, maxiter=1, rtol=1e-3, callback=cb, callback_type='pr_norm')
    print('   step: |dy|/|y| %.3e  dbeta %.6e  dy.t %.3e  dy.y/|y|^2 %.3e' % (np.linalg.norm(dz[:NY]) / np.linalg.norm(z[:NY]), dz[NY], dz[:NY] @ t, dz[:NY] @ z[:NY] / (z[:NY] @ z[:NY])), flush=True)
    lam = 1.0
    while lam > 1e-3:
        zn = z + lam * dz; En, a0n = E(zn); nEn = np.linalg.norm(En)
        print(' newton %d lam %.3g |E| %.6e -> %.6e a0 %.6f beta %.6f max|E| %.3e (%.0fs)' % (k, lam, nE, nEn, a0n, zn[NY], np.abs(En).max(), time.time() - t0), flush=True)
        if nEn < nE: break
        lam *= 0.5
    if nEn >= nE:
        print('no decrease; stop', flush=True); break
    z, Ez, nE, a0 = zn, En, nEn, a0n
    cO = c_of_y(z[:NY]); cO *= -2.0 / float(crow @ cO[0])
    np.savez(pre + '.npz', cO=cO.reshape(-1), cT=np.zeros(NT * K), beta=z[NY], beta_basis=beta0, L=P.L, NT=NT, NO=NO, K=K, a0=a0,
             gamma_T=P.gamma_T, gamma_O=P.gamma_O, mu=P.mu, Enorm=nE)
