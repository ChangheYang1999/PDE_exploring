"""nk4: Newton-Krylov for the Psi-only characteristic fixed point with beta as an unknown and beta-CONSISTENT basis
exponents (gamma_O = -1/beta, mu = 1/beta, recomputed at every evaluation), unknowns = weighted grid values of the
NO odd-odd sine modes on a FIXED polar grid (independent of beta), plus beta.
Fit operator (per mode, beta-dependent): weighted basis matrix H = U S V^T, filtered pseudo-inverse
fit(b) = V diag(phi/s) U^T b, phi(s) = 1/(1 + (SVTOL s0/s)^4) (smooth in beta), Q b = H fit(b).
c(Y) = c_row . fit(Y)[mode 1]. Velocity from fit(Yn), Yn = Y (-2/c(Y)). g = sine projection of Omega_char (a0 = 1),
gw = g / scale. a0 = -2/c(Q gw).
E1 = Yn - a0 Q gw + (c(Y) + 2) n_c, n_c with c(n_c) = 1; E2 = t . (Y - Y0) (dilation gauge).
E1 = 0 => c(Y) = -2 and Y = a0 Q gw. Reported separately: true weighted residual max |H fit(Yn) - a0 gw| on the grid.
Usage: python3 nk4.py state.npz out_prefix n_newton m_gmres Nr M [qmax] [beta0]"""
import sys, os, time, math, numpy as np, torch
from scipy.sparse.linalg import LinearOperator, gmres
from charlib import *
from picard import cheb_q_nodes, r_of_q, omega_char_grid, project
torch.set_num_threads(1)
SVTOL = float(os.environ.get("SVTOL", "1e-2"))
f, pre = sys.argv[1], sys.argv[2]
nnew, mg, Nr, M = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
qmax = float(sys.argv[7]) if len(sys.argv) > 7 else 0.99
P0, cT, cO_t, NT, NO, K = load_coefs(f)
beta0 = float(sys.argv[8]) if len(sys.argv) > 8 else P0.beta
L0 = P0.L
cO0 = cO_t.numpy().copy()
crow0 = c_row(P0, P0.gamma_O, K).numpy(); cO0 *= -2.0 / float(crow0 @ cO0[0])
rr = r_of_q(P0, cheb_q_nodes(Nr, qmax)); ph = (np.arange(M) + 0.5) * np.pi / (2 * M)
r_t = torch.tensor(rr, dtype=DT)


def mode_values(P, cO, r):
    rt = torch.tensor(r, dtype=DT)
    return np.stack([radial_basis(P, rt, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() @ cO[n - 1] for n in range(1, NO + 1)], 1)


G0 = mode_values(P0, cO0, rr)
Sang = np.sin(2 * np.arange(1, NO + 1)[:, None] * ph[None, :])
scale_r = np.abs(G0 @ Sang).max(1) + 1e-300
Y0 = (G0 / scale_r[:, None]).T.reshape(-1)          # mode-major: Y[n*Nr:(n+1)*Nr]
NY = NO * Nr
eta = 1e-4
t = ((mode_values(P0, cO0, rr * (1 + eta)) - mode_values(P0, cO0, rr * (1 - eta))) / (2 * eta) / scale_r[:, None]).T.reshape(-1)
t /= np.linalg.norm(t)

_cache = {}
def ops(beta):
    if beta in _cache: return _cache[beta]
    P = Params(beta, L=L0)
    Us, Ws, Hs = [], [], []
    for n in range(1, NO + 1):
        H = radial_basis(P, r_t, 2 * n, P.gamma_O, K, deriv=False)[0].numpy() / scale_r[:, None]
        u, s, vt = np.linalg.svd(H, full_matrices=False)
        phi = 1.0 / (1.0 + (SVTOL * s[0] / s) ** 4)
        Us.append(u); Ws.append(vt.T * (phi / s)[None, :] @ u.T)   # fit matrix (K, Nr)
        Hs.append(H)
    crow = c_row(P, P.gamma_O, K).numpy()
    wc = crow @ Ws[0]                                   # c functional on mode-1 weighted grid values
    out = (P, Ws, Hs, crow, wc)
    if len(_cache) > 8: _cache.clear()
    _cache[beta] = out
    return out


def fit(Ws, Yg):
    return np.stack([Ws[n] @ Yg[n] for n in range(NO)])  # (NO, K)


nev = [0]
def E(z, diag=False):
    Y, beta = z[:NY], z[NY]
    P, Ws, Hs, crow, wc = ops(beta)
    Yg = Y.reshape(NO, Nr)
    cY = float(wc @ Yg[0])
    Yn = Yg * (-2.0 / cY)
    cOn = fit(Ws, Yn)
    Om1, tab, out = omega_char_grid(P, torch.tensor(cOn, dtype=DT), NO, K, rr, ph, h=0.02, r_stop=1e-3)
    g, trunc = project(Om1, ph, NO)
    gw = (g / scale_r[:, None]).T                       # (NO, Nr)
    Qg = np.stack([Hs[n] @ (Ws[n] @ gw[n]) for n in range(NO)])
    a0 = -2.0 / float(wc @ Qg[0])
    nc = np.zeros((NO, Nr)); nc[0] = wc / (wc @ wc)
    E1 = Yn - a0 * Qg + (cY + 2.0) * nc
    nev[0] += 1
    Ez = np.concatenate([E1.reshape(-1), [t @ (Y - Y0)]])
    if not diag: return Ez, a0
    HcO = np.stack([Hs[n] @ cOn[n] for n in range(NO)])
    true = np.abs(HcO - a0 * gw).max()
    rel_trunc = np.abs(trunc).max() / np.abs(Om1).max()
    return Ez, a0, dict(true=true, rel_trunc=rel_trunc, cY=cY, fiterr=np.abs(HcO - Yn).max())


z = np.concatenate([Y0, [beta0]])
t0 = time.time(); Ez, a0, d = E(z, diag=True); nE = np.linalg.norm(Ez)
print('nk4 SVTOL %g grid Nr %d M %d qmax %g NO %d K %d unknowns %d + beta, beta0 %.6f' % (SVTOL, Nr, M, qmax, NO, K, NY, beta0), flush=True)
print('E0 |E| %.6e a0 %.6f beta %.6f max|E| %.3e true %.3e fiterr %.3e angtrunc %.2e c(Y) %.6f (%.0fs)' % (
    nE, a0, beta0, np.abs(Ez).max(), d['true'], d['fiterr'], d['rel_trunc'], d['cY'], time.time() - t0), flush=True)
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
    print('   step: |dY|/|Y| %.3e  dbeta %.6e  dY.t %.3e' % (np.linalg.norm(dz[:NY]) / np.linalg.norm(z[:NY]), dz[NY], dz[:NY] @ t), flush=True)
    lam = 1.0
    while lam > 1e-3:
        zn = z + lam * dz; En, a0n, dn = E(zn, diag=True); nEn = np.linalg.norm(En)
        print(' newton %d lam %.3g |E| %.6e -> %.6e a0 %.6f beta %.6f max|E| %.3e true %.3e fiterr %.3e angtrunc %.2e (%.0fs)' % (
            k, lam, nE, nEn, a0n, zn[NY], np.abs(En).max(), dn['true'], dn['fiterr'], dn['rel_trunc'], time.time() - t0), flush=True)
        if nEn < nE: break
        lam *= 0.5
    if nEn >= nE:
        print('no decrease; stop', flush=True); break
    z, Ez, nE, a0 = zn, En, nEn, a0n
    P, Ws, Hs, crow, wc = ops(z[NY])
    Yg = z[:NY].reshape(NO, Nr); cOn = fit(Ws, Yg * (-2.0 / float(wc @ Yg[0])))
    np.savez(pre + '.npz', cO=cOn.reshape(-1), cT=np.zeros(NT * K), beta=z[NY], L=P.L, NT=NT, NO=NO, K=K, a0=a0,
             gamma_T=P.gamma_T, gamma_O=P.gamma_O, mu=P.mu, Enorm=nE, Y=z[:NY], rr=rr, scale_r=scale_r)
