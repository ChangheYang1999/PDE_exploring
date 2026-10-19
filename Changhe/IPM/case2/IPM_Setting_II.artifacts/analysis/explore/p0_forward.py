# Lead exploration (2026-10-17): forward self-similar IPM evolution for the limit problem (P0).
# (P0): Y = Z + w[f], w canonical (once-subtracted, w(0) = 0), div Y = 2, curl Y = -f_x, Y.grad f = 0.
# Reversed in time, (P0) is the forward self-similar IPM problem from degree-0 data; in the variable s = log t the
# density obeys d_s f = Y.grad f (f carried inward by -Y), with f = A(theta) imposed at r = r_max (inflow).
# A steady state is a (P0) solution in the frame w(0) = 0. Exploratory, not verified.
# Grid: rho = log r uniform on [rmin_log, rmax_log], theta uniform (Nth, FFT). No symmetry imposed by the code.
import sys, json, time
import numpy as np
from scipy.ndimage import map_coordinates


def make_grid(Nr, Nth, lo, hi):
    rho = np.linspace(lo, hi, Nr)
    th = 2 * np.pi * np.arange(Nth) / Nth
    return rho, th


def d_rho(f, drho):
    # fourth-order centred differences in rho (axis 0), one-sided second order at the ends
    g = np.empty_like(f)
    g[2:-2] = (-f[4:] + 8 * f[3:-1] - 8 * f[1:-3] + f[:-4]) / (12 * drho)
    g[1] = (f[2] - f[0]) / (2 * drho)
    g[-2] = (f[-1] - f[-3]) / (2 * drho)
    g[0] = (-3 * f[0] + 4 * f[1] - f[2]) / (2 * drho)
    g[-1] = (3 * f[-1] - 4 * f[-2] + f[-3]) / (2 * drho)
    return g


def d_th(f):
    Nth = f.shape[1]
    m = np.fft.fftfreq(Nth, 1.0 / Nth)
    F = np.fft.fft(f, axis=1)
    F[:, Nth // 2] = 0.0
    return np.real(np.fft.ifft(1j * m[None, :] * F, axis=1))


def velocity(f, rho, th):
    """Canonical velocity w = U - U(0), U = (-psi_y, psi_x), -Lap psi = d_x f, for bounded f
    (degree-0 far field allowed). Returns (w_r, w_th) on the grid."""
    Nr, Nth = f.shape
    drho = rho[1] - rho[0]
    r = np.exp(rho)
    c, s = np.cos(th)[None, :], np.sin(th)[None, :]
    q = (c * d_rho(f, drho) - s * d_th(f)) / r[:, None]          # d_x f
    Q = np.fft.fft(q, axis=1) / Nth                                # q = sum_m Q_m e^{i m th}
    m = np.fft.fftfreq(Nth, 1.0 / Nth).astype(int)
    e2 = np.exp(2 * rho)
    Wr = np.zeros((Nr, Nth), complex)
    Wt = np.zeros((Nr, Nth), complex)
    for j, mm in enumerate(m):
        if mm == Nth // 2 or mm == -(Nth // 2):
            continue
        qm = Q[:, j]
        h = qm * e2                                                # integrand of int q s ds in d rho
        am = abs(mm)
        if am == 0:
            # psi_0' = -(1/r) int_0^r q_0 s ds ; w_th = psi_0', w_r = 0
            I = np.zeros(Nr, complex)
            I[0] = h[0] / 2.0                                       # int_0^{r0} ~ q(r0) r0^2 / 2
            for k in range(1, Nr):
                I[k] = I[k - 1] + 0.5 * drho * (h[k - 1] + h[k])
            Wt[:, j] = -I / r
            continue
        lam = np.exp(-am * drho)
        # A_< (r) = r^{-am} int_0^r s^{am} q s ds
        Al = np.zeros(Nr, complex)
        Al[0] = h[0] / (am + 2.0)
        for k in range(1, Nr):
            Al[k] = lam * Al[k - 1] + 0.5 * drho * (lam * h[k - 1] + h[k])
        if am == 1:
            # subtracted: A_> = -r int_0^r q ds  (removes the uniform velocity U(0))
            hq = qm * r                                             # q ds = q r d rho
            I = np.zeros(Nr, complex)
            I[0] = hq[0] / 1.0                                      # int_0^{r0} q ds ~ q(r0) r0 (q ~ const near 0)
            for k in range(1, Nr):
                I[k] = I[k - 1] + 0.5 * drho * (hq[k - 1] + hq[k])
            Ag = -r * I
        else:
            # A_> (r) = r^{am} int_r^inf s^{-am} q s ds, tail q ~ q(R) R/s beyond R
            Ag = np.zeros(Nr, complex)
            Ag[-1] = h[-1] / (am - 1.0)
            for k in range(Nr - 2, -1, -1):
                Ag[k] = lam * Ag[k + 1] + 0.5 * drho * (lam * h[k + 1] + h[k])
        psi = (Al + Ag) / (2.0 * am)
        dpsi = (-Al + Ag) / (2.0 * r)
        Wr[:, j] = -1j * mm * psi / r
        Wt[:, j] = dpsi
    wr = np.real(np.fft.ifft(Wr * Nth, axis=1))
    wt = np.real(np.fft.ifft(Wt * Nth, axis=1))
    return wr, wt


def interp(f, ci, cj, Nth):
    # periodic in theta (axis 1) by padding, clamped in rho (axis 0)
    P = 4
    fp = np.concatenate([f[:, -P:], f, f[:, :P]], axis=1)
    ci = np.clip(ci, 0, f.shape[0] - 1)
    cj = np.mod(cj, Nth) + P
    return map_coordinates(fp, [ci, cj], order=3, mode='nearest')


def data_A(th, kind, par):
    c, s = np.cos(th), np.sin(th)
    if kind == 'cos2':
        return c ** 2
    if kind == 'cosk':            # |cos|^k, zero order k at +-90 deg
        return np.abs(c) ** par
    if kind == 'rhoa':            # far field of rho_a: cos^2 (1 + a sin)^2
        return c ** 2 * (1 + par * s) ** 2
    if kind == 'plateau':         # tanh(k cos^2)/tanh(k): plateaus near th = 0, pi
        return np.tanh(par * c ** 2) / np.tanh(par)
    if kind == 'plateau_a':       # plateau times (1 + 0.5 sin)^2 (heavier above)
        return np.tanh(par * c ** 2) / np.tanh(par) * (1 + 0.5 * s) ** 2
    if kind == 'asym':            # x-odd perturbation: cos^2 (1 + 0.5 sin + par cos sin)^2
        return c ** 2 * (1 + 0.5 * s + par * c * s) ** 2
    raise ValueError(kind)


def run(args):
    Nr, Nth = args['Nr'], args['Nth']
    rho, th = make_grid(Nr, Nth, args['lo'], args['hi'])
    drho = rho[1] - rho[0]
    r = np.exp(rho)
    A = data_A(th, args['kind'], args['par'])
    R2 = (r ** 2 / (args['core'] ** 2 + r ** 2))[:, None]
    f = R2 * A[None, :]
    ds = args['ds']
    hist = []
    t0 = time.time()
    for n in range(args['nsteps']):
        wr, wt = velocity(f, rho, th)
        ar = 1.0 + wr / r[:, None]           # Y_r / r   (d rho / d tau)
        at = wt / r[:, None]                 # Y_th / r  (d th / d tau)
        # midpoint departure: f(s+ds, x) = f(s, x + ds a(x + ds a/2))
        ci0 = np.arange(Nr)[:, None] + 0.5 * ds * ar / drho
        cj0 = np.arange(Nth)[None, :] + 0.5 * ds * at / (2 * np.pi / Nth)
        arm = interp(ar, ci0, cj0, Nth)
        atm = interp(at, ci0, cj0, Nth)
        ci = np.arange(Nr)[:, None] + ds * arm / drho
        cj = np.arange(Nth)[None, :] + ds * atm / (2 * np.pi / Nth)
        fn = interp(f, ci, cj, Nth)
        out = ci > Nr - 1
        if out.any():
            thd = cj * (2 * np.pi / Nth)
            fn[out] = data_A(thd[out], args['kind'], args['par'])
        dfn = np.max(np.abs(fn - f)) / ds
        f = fn
        if n % args['every'] == 0 or n == args['nsteps'] - 1:
            # residual Y.grad f, centre data
            res = ar * d_rho(f, drho) + at * d_th(f)
            k1 = np.searchsorted(r, 1.0)
            kR = np.searchsorted(r, 0.3 * r[-1])
            rec = dict(n=n, s=n * ds, dfds=float(dfn),
                       res_in=float(np.max(np.abs(res[:k1]))), res_mid=float(np.max(np.abs(res[:kR]))),
                       fmin=float(f.min()), fmax=float(f.max()),
                       f_r0=float(f[0].mean()), wall=float(time.time() - t0))
            hist.append(rec)
            print(json.dumps(rec), flush=True)
    np.savez(args['out'], f=f, rho=rho, th=th, A=A, hist=json.dumps(hist), args=json.dumps(args))
    return f


if __name__ == '__main__':
    args = dict(Nr=241, Nth=128, lo=-5.0, hi=5.0, kind='cos2', par=0.0, core=1.0, ds=0.05, nsteps=400,
                every=20, out='runs/p0f_test.npz')
    for a in sys.argv[1:]:
        k, v = a.split('=')
        if k in ('Nr', 'Nth', 'nsteps', 'every'):
            args[k] = int(v)
        elif k in ('kind', 'out'):
            args[k] = v
        else:
            args[k] = float(v)
    print(json.dumps(args), flush=True)
    run(args)
