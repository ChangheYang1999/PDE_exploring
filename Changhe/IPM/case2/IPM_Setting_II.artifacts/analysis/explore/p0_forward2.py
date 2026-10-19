# Lead exploration (2026-10-17): forward self-similar evolution for (P0), version 2.
# Same model as p0_forward.py (d_s f = Y.grad f, Y = Z + w[f], canonical once-subtracted w, inflow f = A at r_max), with
# (i) the radial recurrences of the velocity vectorised over Fourier modes, (ii) a quasi-monotone semi-Lagrangian step
# (cubic interpolation clipped to the min/max of the surrounding 2x2 grid values), (iii) restart from a saved state.
# Exploratory, not verified. No symmetry imposed by the code.
import sys, json, time
import numpy as np
from scipy.ndimage import map_coordinates
import p0_forward as P1


def velocity(f, rho, th):
    Nr, Nth = f.shape
    drho = rho[1] - rho[0]
    r = np.exp(rho)
    c, s = np.cos(th)[None, :], np.sin(th)[None, :]
    q = (c * P1.d_rho(f, drho) - s * P1.d_th(f)) / r[:, None]
    Q = np.fft.fft(q, axis=1) / Nth
    m = np.fft.fftfreq(Nth, 1.0 / Nth).astype(int)
    am = np.abs(m).astype(float)
    keep = (np.abs(m) != Nth // 2)
    h = Q * np.exp(2 * rho)[:, None]
    hq = Q * r[:, None]
    lam = np.exp(-am * drho)[None, :][0]
    Al = np.zeros((Nr, Nth), complex)
    Al[0] = h[0] / (am + 2.0)
    for k in range(1, Nr):
        Al[k] = lam * Al[k - 1] + 0.5 * drho * (lam * h[k - 1] + h[k])
    I = np.zeros((Nr, Nth), complex)            # int_0^r q ds (m = +-1) and int_0^r q s ds (m = 0)
    I1 = np.zeros((Nr, Nth), complex)
    I[0] = h[0] / 2.0
    I1[0] = hq[0]
    for k in range(1, Nr):
        I[k] = I[k - 1] + 0.5 * drho * (h[k - 1] + h[k])
        I1[k] = I1[k - 1] + 0.5 * drho * (hq[k - 1] + hq[k])
    Ag = np.zeros((Nr, Nth), complex)
    big = am >= 2
    Ag[-1, big] = h[-1, big] / (am[big] - 1.0)
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
    wr = np.real(np.fft.ifft(Wr * Nth, axis=1))
    wt = np.real(np.fft.ifft(Wt * Nth, axis=1))
    return wr, wt


def interp_qm(g, ci, cj, Nth):
    Pd = 24   # periodic pad; must exceed the cubic B-spline prefilter decay length (0.268^24 ~ 2e-14)
    Nr = g.shape[0]
    gp = np.concatenate([g[:, -Pd:], g, g[:, :Pd]], axis=1)
    ci = np.clip(ci, 0, Nr - 1)
    cjp = np.mod(cj, Nth) + Pd
    v3 = map_coordinates(gp, [ci, cjp], order=3, mode='nearest')
    i0 = np.clip(np.floor(ci).astype(int), 0, Nr - 2)
    j0 = np.floor(cjp).astype(int)
    c00 = gp[i0, j0]; c01 = gp[i0, j0 + 1]; c10 = gp[i0 + 1, j0]; c11 = gp[i0 + 1, j0 + 1]
    lo = np.minimum(np.minimum(c00, c01), np.minimum(c10, c11))
    hi = np.maximum(np.maximum(c00, c01), np.maximum(c10, c11))
    return np.clip(v3, lo, hi)


def run(args):
    if args.get('restart'):
        d = np.load(args['restart'])
        f, rho, th = d['f'], d['rho'], d['th']
        Nr, Nth = f.shape
    else:
        Nr, Nth = args['Nr'], args['Nth']
        rho, th = P1.make_grid(Nr, Nth, args['lo'], args['hi'])
        r = np.exp(rho)
        A = P1.data_A(th, args['kind'], args['par'])
        f = (r ** 2 / (args['core'] ** 2 + r ** 2))[:, None] * A[None, :]
    drho = rho[1] - rho[0]
    r = np.exp(rho)
    dth = 2 * np.pi / Nth
    ds = args['ds']
    hist = []
    t0 = time.time()
    for n in range(args['nsteps']):
        wr, wt = velocity(f, rho, th)
        ar = 1.0 + wr / r[:, None]
        at = wt / r[:, None]
        ci0 = np.arange(Nr)[:, None] + 0.5 * ds * ar / drho
        cj0 = np.arange(Nth)[None, :] + 0.5 * ds * at / dth
        arm = interp_qm(ar, ci0, cj0, Nth)
        atm = interp_qm(at, ci0, cj0, Nth)
        ci = np.arange(Nr)[:, None] + ds * arm / drho
        cj = np.arange(Nth)[None, :] + ds * atm / dth
        fn = interp_qm(f, ci, cj, Nth)
        out = ci > Nr - 1
        if out.any():
            fn[out] = P1.data_A(cj[out] * dth, args['kind'], args['par'])
        dfn = np.max(np.abs(fn - f)) / ds
        f = fn
        if n % args['every'] == 0 or n == args['nsteps'] - 1:
            res = ar * P1.d_rho(f, drho) + at * P1.d_th(f)
            k1 = np.searchsorted(r, 1.0)
            rec = dict(n=n, dfds=float(dfn), res_in=float(np.max(np.abs(res[:k1]))),
                       res_all=float(np.max(np.abs(res[:-5]))), fmin=float(f.min()), fmax=float(f.max()),
                       wall=round(time.time() - t0, 1))
            hist.append(rec)
            print(json.dumps(rec), flush=True)
    np.savez(args['out'], f=f, rho=rho, th=th, A=P1.data_A(th, args['kind'], args['par']), hist=json.dumps(hist),
             args=json.dumps(args))


if __name__ == '__main__':
    args = dict(Nr=241, Nth=128, lo=-5.0, hi=5.0, kind='cos2', par=0.0, core=1.0, ds=0.05, nsteps=400,
                every=50, out='../runs/p0f2_test.npz', restart='')
    for a in sys.argv[1:]:
        k, v = a.split('=')
        if k in ('Nr', 'Nth', 'nsteps', 'every'):
            args[k] = int(v)
        elif k in ('kind', 'out', 'restart'):
            args[k] = v
        else:
            args[k] = float(v)
    print(json.dumps(args), flush=True)
    run(args)
