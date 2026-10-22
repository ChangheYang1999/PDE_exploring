"""Psi-only characteristic fixed point (prototype).
Map G: cO (Omega coefficients, normalized c = -2) -> velocity table -> Omega_char on a polar grid (a0 = 1, linear in a0)
-> midpoint sine projection onto the NO even modes -> weighted radial least squares per mode -> rescale a0 so that
c = -2. A fixed point of G is a profile (Theta, Omega slaved by characteristics to the velocity of Omega).
Usage: python3 picard.py state.npz out_prefix n_iter omega Nr M [qmax]"""
import sys, time, math, numpy as np, torch
from charlib import *
torch.set_num_threads(1)


def cheb_q_nodes(Nr, qmax):
    k = np.arange(Nr)
    x = np.cos(np.pi * (k + 0.5) / Nr)[::-1]          # (-1, 1) increasing
    return 0.5 * qmax * (x + 1.0)


def r_of_q(P, q):
    return P.L * np.sqrt((1.0 - q) ** (-2.0 / P.mu) - 1.0)


def omega_char_grid(P, cO, NO, K, rr, ph, h=0.02, r_stop=1e-3, chunk=None):
    tab = VelTable(P, cO, NO, K, rmin=1e-4, rmax=max(1e10, 2 * rr.max()), per_dec=400)
    R, TH = np.meshgrid(rr, ph, indexing='ij')
    X = torch.tensor(np.stack([(R * np.cos(TH)).ravel(), (R * np.sin(TH)).ravel()], 1), dtype=DT)
    out = reconstruct(tab, X, 1.0, h=h, r_stop=r_stop, S_max=80.0, scale=1.0)
    assert bool(out['done'].all()), 'trajectories not finished'
    return out['Om'].reshape(len(rr), len(ph)).numpy(), tab, out


def project(Om, ph, NO):
    M = len(ph)
    n = np.arange(1, NO + 1)
    S = np.sin(2 * n[:, None] * ph[None, :])          # (NO, M)
    g = (2.0 / M) * Om @ S.T                          # (Nr, NO)
    trunc = Om - g @ S                                # truncation remainder on the grid
    return g, trunc


def radial_fit(P, rr, g, K, scale_r):
    """cO (NO, K) by weighted least squares per mode; weight 1/scale_r (local Omega size)."""
    r_t = torch.tensor(rr, dtype=DT)
    NO = g.shape[1]
    cO = np.zeros((NO, K)); res = np.zeros(NO)
    for n in range(1, NO + 1):
        H, _ = radial_basis(P, r_t, 2 * n, P.gamma_O, K, deriv=False)
        A = H.numpy() / scale_r[:, None]
        b = g[:, n - 1] / scale_r
        cn = np.linalg.norm(A, axis=0); cn[cn == 0] = 1.0
        sol, *_ = np.linalg.lstsq(A / cn, b, rcond=1e-13)
        cO[n - 1] = sol / cn
        res[n - 1] = np.max(np.abs(A @ cO[n - 1] - b))
    return cO, res


def G(P, cO, NO, K, rr, ph, h, r_stop):
    t0 = time.time()
    Om1, tab, out = omega_char_grid(P, torch.tensor(cO, dtype=DT), NO, K, rr, ph, h=h, r_stop=r_stop)
    t1 = time.time()
    g, trunc = project(Om1, ph, NO)
    scale_r = np.max(np.abs(Om1), axis=1) + 1e-300
    cO1, res = radial_fit(P, rr, g, K, scale_r)
    c1 = float(c_row(P, P.gamma_O, K).numpy() @ cO1[0])
    a0 = -2.0 / c1
    info = dict(a0=a0, c_in=tab.c, t_char=t1 - t0, t_all=time.time() - t0, fitres=res.max(),
                trunc=float(np.max(np.abs(trunc) / scale_r[:, None])), gtail=float(np.max(np.abs(g[:, -2:]) / scale_r[:, None])),
                Smax=float(out['S'].max()))
    return a0 * cO1, a0 * Om1, info


def omega_on_grid(P, cO, NO, K, rr, ph):
    r_t = torch.tensor(rr, dtype=DT)
    n = np.arange(1, NO + 1)
    S = np.sin(2 * n[:, None] * ph[None, :])
    gs = np.stack([(radial_basis(P, r_t, 2 * k, P.gamma_O, K, deriv=False)[0].numpy() @ cO[k - 1]) for k in n], 1)
    return gs @ S


if __name__ == '__main__':
    f, pre, nit, om, Nr, M = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    qmax = float(sys.argv[7]) if len(sys.argv) > 7 else 0.99
    h = float(sys.argv[8]) if len(sys.argv) > 8 else 0.02
    P, cT, cO_t, NT, NO, K = load_coefs(f)
    cO = cO_t.numpy().copy()
    c0 = float(c_row(P, P.gamma_O, K).numpy() @ cO[0]); cO *= -2.0 / c0
    rr = r_of_q(P, cheb_q_nodes(Nr, qmax)); ph = (np.arange(M) + 0.5) * np.pi / (2 * M)
    print('grid Nr %d M %d r %.3e..%.3e, NO %d K %d, omega %g, h %g' % (Nr, M, rr[0], rr[-1], NO, K, om, h), flush=True)
    hist = []
    for it in range(nit):
        Om_in = omega_on_grid(P, cO, NO, K, rr, ph)
        cOn, Om_out, info = G(P, cO, NO, K, rr, ph, h, 1e-3)
        sc = np.max(np.abs(Om_out), axis=1)[:, None] + 1e-300
        d = np.abs(Om_out - Om_in) / sc
        # desingularized difference near the y-axis: Omega/(x y) relative
        X = rr[:, None] * np.cos(ph)[None, :]; Y = rr[:, None] * np.sin(ph)[None, :]
        dd = np.abs(Om_out - Om_in) / (np.abs(Om_out) + 1e-300)
        print('it %3d a0 %.6f |dOm|/scale max %.3e (r<10: %.3e) rel-pointwise max(r<10) %.3e  fitres %.1e trunc %.1e gtail %.1e  Smax %.1f  %.0fs'
              % (it, info['a0'], d.max(), d[rr < 10].max(), dd[rr < 10].max(), info['fitres'], info['trunc'], info['gtail'], info['Smax'], info['t_all']), flush=True)
        i, j = np.unravel_index(np.argmax(d), d.shape)
        print('      argmax r %.3e phi %.1f deg; Om/(xy) in %.5e out %.5e; c_in %.10f' % (rr[i], np.degrees(ph[j]), Om_in[i, j] / (X[i, j] * Y[i, j]), Om_out[i, j] / (X[i, j] * Y[i, j]), info['c_in']), flush=True)
        hist.append([it, info['a0'], d.max(), d[rr < 10].max(), dd[rr < 10].max()])
        cO = (1 - om) * cO + om * cOn
        c = float(c_row(P, P.gamma_O, K).numpy() @ cO[0]); cO *= -2.0 / c
        np.savez(pre + '.npz', cO=cO.reshape(-1), cT=np.zeros(NT * K), beta=P.beta, L=P.L, NT=NT, NO=NO, K=K, a0=info['a0'], hist=np.array(hist),
                 gamma_T=P.gamma_T, gamma_O=P.gamma_O, mu=P.mu)
