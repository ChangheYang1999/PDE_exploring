# Lead exploration (2026-10-17): forward self-similar IPM evolution at finite p (Setting II profile system as
# the steady state). In self-similar variables d_s rho = V.grad rho - rho, V = l X + W[rho] (canonical once-subtracted
# law, W(0) = 0, so V(0) = 0: the tracked particle is the origin). With rho = r^p g (p = 1/l):
#     d_s g = V.grad g + p (W_r / r) g,
# g = A(theta) imposed at r_max (inflow along -V). Steady states are profiles with growth r^p; their node structure
# (DV(0) eigenvalues m_1 <= m_2, m_1 + m_2 = 2l; Setting II needs m_1 = 1/2 with horizontal eigenvector and rho in C^2)
# is an output, not imposed. Grid: log r x theta (FFT), no symmetry imposed. Exploratory, not verified.
import sys, json, time
import numpy as np
import p0_forward as P1
import p0_forward2 as P2


def velocity_p(rhoD, lr, th, p):
    """Canonical W for density rhoD (growth r^p) on the log-polar grid: as P2.velocity but with tail q ~ s^(p-1)."""
    Nr, Nth = rhoD.shape
    drho = lr[1] - lr[0]
    r = np.exp(lr)
    c, s = np.cos(th)[None, :], np.sin(th)[None, :]
    q = (c * P1.d_rho(rhoD, drho) - s * P1.d_th(rhoD)) / r[:, None]
    Q = np.fft.fft(q, axis=1) / Nth
    m = np.fft.fftfreq(Nth, 1.0 / Nth).astype(int)
    am = np.abs(m).astype(float)
    keep = (np.abs(m) != Nth // 2)
    h = Q * np.exp(2 * lr)[:, None]
    hq = Q * r[:, None]
    lam = np.exp(-am * drho)
    Al = np.zeros((Nr, Nth), complex)
    Al[0] = h[0] / (am + 2.0)
    for k in range(1, Nr):
        Al[k] = lam * Al[k - 1] + 0.5 * drho * (lam * h[k - 1] + h[k])
    I = np.zeros((Nr, Nth), complex)
    I1 = np.zeros((Nr, Nth), complex)
    I[0] = h[0] / 2.0
    I1[0] = hq[0]
    for k in range(1, Nr):
        I[k] = I[k - 1] + 0.5 * drho * (h[k - 1] + h[k])
        I1[k] = I1[k - 1] + 0.5 * drho * (hq[k - 1] + hq[k])
    Ag = np.zeros((Nr, Nth), complex)
    big = am >= 2
    Ag[-1, big] = h[-1, big] / (am[big] - 1.0 - p)
    for k in range(Nr - 2, -1, -1):
        Ag[k, big] = lam[big] * Ag[k + 1, big] + 0.5 * drho * (lam[big] * h[k + 1, big] + h[k, big])
    one = am == 1
    Ag[:, one] = -r[:, None] * I1[:, one]
    Wr = np.zeros((Nr, Nth), complex)
    Wt = np.zeros((Nr, Nth), complex)
    nz = (am >= 1) & keep
    amn = np.where(am >= 1, am, 1.0)
    psi = (Al + Ag) / (2.0 * amn[None, :])
    dpsi = (-Al + Ag) / (2.0 * r[:, None])
    Wr[:, nz] = (-1j * m[None, :] * psi / r[:, None])[:, nz]
    Wt[:, nz] = dpsi[:, nz]
    z = am == 0
    Wt[:, z] = -I[:, z] / r[:, None]
    return np.real(np.fft.ifft(Wr * Nth, axis=1)), np.real(np.fft.ifft(Wt * Nth, axis=1))


def node_matrix(Vr_over_r, Vt_over_r, th):
    # fit V = M X on a ring: V_r/r = n.M n, V_th/r = t.M n, n = (cos, sin), t = (-sin, cos)
    c, s = np.cos(th), np.sin(th)
    rows = []; rhs = []
    for k in range(len(th)):
        n = np.array([c[k], s[k]]); t = np.array([-s[k], c[k]])
        rows.append(np.outer(n, n).ravel()); rhs.append(Vr_over_r[k])
        rows.append(np.outer(t, n).ravel()); rhs.append(Vt_over_r[k])
    M = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)[0].reshape(2, 2)
    return M


_TAB = {}


def datum(th, args):
    # kind='table': periodic linear interpolation of a tabulated datum (npz with A, thA), e.g. from gfix.py
    if args['kind'] == 'table':
        if args['Afile'] not in _TAB:
            d = np.load(args['Afile']); _TAB[args['Afile']] = (d['thA'], d['A'])
        thA, AA = _TAB[args['Afile']]
        return np.interp(np.mod(th, 2 * np.pi), thA, AA, period=2 * np.pi)
    return P1.data_A(th, args['kind'], args['par'])


def run(args):
    p = args['p']; l = 1.0 / p
    if args.get('restart'):
        d = np.load(args['restart']); g, lr, th = d['g'], d['lr'], d['th']
        Nr, Nth = g.shape
    else:
        Nr, Nth = args['Nr'], args['Nth']
        lr, th = P1.make_grid(Nr, Nth, args['lo'], args['hi'])
        r = np.exp(lr)
        A = datum(th, args)
        g = ((r ** 2 / (1.0 + r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]   # rho ~ r^2 A near 0, r^p A far
    drho = lr[1] - lr[0]; r = np.exp(lr); dth = 2 * np.pi / Nth; ds = args['ds']
    hist = []; t0 = time.time()
    for n in range(args['nsteps']):
        rhoD = (r ** p)[:, None] * g
        wr, wt = velocity_p(rhoD, lr, th, p)
        ar = l + wr / r[:, None]          # V_r / r
        at = wt / r[:, None]              # V_th / r
        src = p * wr / r[:, None]
        ci0 = np.arange(Nr)[:, None] + 0.5 * ds * ar / drho
        cj0 = np.arange(Nth)[None, :] + 0.5 * ds * at / dth
        arm = P2.interp_qm(ar, ci0, cj0, Nth); atm = P2.interp_qm(at, ci0, cj0, Nth)
        srm = P2.interp_qm(src, ci0, cj0, Nth)
        ci = np.arange(Nr)[:, None] + ds * arm / drho
        cj = np.arange(Nth)[None, :] + ds * atm / dth
        gn = P2.interp_qm(g, ci, cj, Nth) * np.exp(ds * srm)
        out = ci > Nr - 1
        if out.any():
            gn[out] = datum(cj[out] * dth, args)
        dgn = np.max(np.abs(gn - g)) / ds
        g = gn
        if n % args['every'] == 0 or n == args['nsteps'] - 1:
            k0 = int(args.get('kring', 8))
            M = node_matrix(ar[k0], at[k0], th)
            Ms = 0.5 * (M + M.T); ev, evec = np.linalg.eigh(Ms)
            e1 = evec[:, 0]
            rec = dict(n=n, s=round(n * ds, 3), dgds=float(dgn), gmin=float(g.min()), gmax=float(g.max()),
                       r_ring=float(r[k0]), M=[round(float(v), 4) for v in M.ravel()],
                       m1=round(float(ev[0]), 4), m2=round(float(ev[1]), 4),
                       e1_angle_deg=round(float(np.degrees(np.arctan2(e1[1], e1[0])) % 180), 2),
                       wall=round(time.time() - t0, 1))
            hist.append(rec); print(json.dumps(rec), flush=True)
    np.savez(args['out'], g=g, lr=lr, th=th, hist=json.dumps(hist), args=json.dumps(args))


if __name__ == '__main__':
    args = dict(p=0.5, Nr=361, Nth=128, lo=-6.0, hi=10.0, kind='cos2', par=0.0, ds=0.02, nsteps=1000,
                every=100, out='../runs/pf_test.npz', restart='', kring=8, Afile='')
    for a in sys.argv[1:]:
        k, v = a.split('=')
        if k in ('Nr', 'Nth', 'nsteps', 'every', 'kring'):
            args[k] = int(v)
        elif k in ('kind', 'out', 'restart', 'Afile'):
            args[k] = v
        else:
            args[k] = float(v)
    print(json.dumps(args), flush=True)
    run(args)
