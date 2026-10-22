"""Exploratory dynamic-rescaling (DR) solver for Setting A1 in log-polar coordinates (heuristic).

Unknowns on (rho, phi), rho = log r, phi in (0, pi/2) collocation (Q1, parity by basis):
  Theta = r * Phi,  Phi = sum_m T_m(rho) sin((2m+1) phi)   (Theta even in x, odd in y)
  Omega = sum_m w_n(rho) sin(n phi), n = 2, 4, ..., 2M     (odd-odd)
DR equations (SPEC sec. 4):
  Omega_s + (c_l X + U).grad Omega = c_w Omega + Theta_x
  Theta_s + (c_l X + U).grad Theta = (c_l + 2 c_w) Theta
c_w = Psi_xy(0)/2 keeps a = Theta_y(0) fixed (imposed at the inflow boundary rho_min);
c_l keeps b1 = Theta_xxy(0)/2 fixed: c_l = c - 3 a d1/(2 b1) + kappa (b1 - b1t)/(2 b1).
Full-plane inverse: exact modal Green formula (SPEC (I3)) in log r with a power-law tail beyond rho_max.
A steady state gives beta = c_l/(-c_w) and the (P) profile Theta/c_w^2, Omega/(-c_w).
"""
import numpy as np, sys, time, os
from scipy.signal import lfilter

def build(M, N, rmin, rmax):
    rho = np.linspace(np.log(rmin), np.log(rmax), N)
    h = rho[1] - rho[0]
    phi = (np.arange(M) + 0.5) * np.pi / (2 * M)
    mT = np.arange(M); kT = 2 * mT + 1
    mO = np.arange(1, M + 1); nO = 2 * mO
    ST = np.sin(np.outer(phi, kT)); CT = np.cos(np.outer(phi, kT)) * kT
    SO = np.sin(np.outer(phi, nO)); CO = np.cos(np.outer(phi, nO)) * nO
    COSO = np.cos(np.outer(phi, nO))
    g = dict(M=M, N=N, rho=rho, h=h, phi=phi, kT=kT, nO=nO, ST=ST, CT=CT, SO=SO, CO=CO, COSO=COSO,
             STi=np.linalg.inv(ST), SOi=np.linalg.inv(SO))
    # spectral filter
    g['filT'] = np.exp(-36.0 * (mT / M) ** 16)
    g['filO'] = np.exp(-36.0 * (mO / M) ** 16)
    # exponential-integration weights for the modal Green recursion, 4-point Lagrange per cell
    xg, wg = np.polynomial.legendre.leggauss(20)
    t = 0.5 * h * (xg + 1); wq = 0.5 * h * wg
    def lag(nodes):
        L = np.ones((len(nodes), len(t)))
        for p, tp in enumerate(nodes):
            for q, tq in enumerate(nodes):
                if q != p:
                    L[p] *= (t - tq) / (tp - tq)
        return L
    offs = {'L': np.array([0, 1, 2, 3]), 'C': np.array([-1, 0, 1, 2]), 'R': np.array([-2, -1, 0, 1])}
    Ls = {k: lag(v * h) for k, v in offs.items()}
    W1 = {}; W2 = {}
    for n in nO:
        k1 = n + 2.0; k2 = n - 2.0
        e1 = np.exp(-k1 * (h - t)); e2 = np.exp(-k2 * t)
        W1[n] = {k: (Ls[k] * e1 * wq).sum(1) for k in Ls}
        W2[n] = {k: (Ls[k] * e2 * wq).sum(1) for k in Ls}
    g.update(offs=offs, W1=W1, W2=W2)
    return g

def cell_integrals(g, w, Wd):
    """J[i] = int over cell [rho_i, rho_{i+1}] of kernel * w, for all cells (len N-1)."""
    N = g['N']
    J = np.empty(N - 1)
    i = np.arange(1, N - 2)
    o = g['offs']['C']
    J[1:N - 2] = sum(Wd['C'][p] * w[i + o[p]] for p in range(4))
    J[0] = sum(Wd['L'][p] * w[0 + g['offs']['L'][p]] for p in range(4))
    J[N - 2] = sum(Wd['R'][p] * w[N - 2 + g['offs']['R'][p]] for p in range(4))
    return J

def biot_savart(g, Om, lam_tail):
    """Return U_r/r, U_phi/r on the grid, and c = Psi_xy(0), d1 - d2, coefficient arrays."""
    h = g['h']; N = g['N']
    wc = Om @ g['SOi'].T            # (N, M) coefficients of sin(n phi)
    Q = np.empty_like(wc); Qp = np.empty_like(wc)
    for m, n in enumerate(g['nO']):
        w = wc[:, m]
        k1 = n + 2.0; k2 = n - 2.0
        J1 = cell_integrals(g, w, g['W1'][n])
        I1 = np.empty(N)
        I1[0] = w[0] / (2 * n + 2)
        # I1[i+1] = e^{-k1 h} I1[i] + J1[i]
        zi = np.array([np.exp(-k1 * h) * I1[0]])
        I1[1:], _ = lfilter([1.0], [1.0, -np.exp(-k1 * h)], J1, zi=zi)
        J2 = cell_integrals(g, w, g['W2'][n])
        I2 = np.empty(N)
        I2[-1] = w[-1] / (k2 + lam_tail)
        zi = np.array([np.exp(-k2 * h) * I2[-1]])
        rev, _ = lfilter([1.0], [1.0, -np.exp(-k2 * h)], J2[::-1], zi=zi)
        I2[:-1] = rev[::-1]
        Q[:, m] = (I1 + I2) / (2 * n)
        Qp[:, m] = (-(n + 2) * I1 + (n - 2) * I2) / (2 * n)
    g['_Q'] = Q; g['_Qp'] = Qp
    Urr = -(Q * g['nO']) @ g['COSO'].T
    Upr = (Qp + 2 * Q) @ g['SO'].T
    rho = g['rho']
    # c = (1/2) int w_2 drho (left tail w2 ~ e^{2 rho}, right tail ~ e^{-lam rho})
    w2 = wc[:, 0]
    c = 0.5 * (np.trapezoid(w2, dx=h) + w2[0] / 2 + w2[-1] / lam_tail)
    w4 = wc[:, 1] if g['M'] > 1 else 0 * w2
    f4 = np.exp(-2 * rho) * w4
    d1md2 = np.trapezoid(f4, dx=h) + f4[0] / 2 + f4[-1] / (2 + lam_tail)
    return Urr, Upr, c, d1md2, wc

def fit_r2(rho, f, ra, rb):
    sel = (rho >= np.log(ra)) & (rho <= np.log(rb))
    A = np.stack([np.exp(2 * rho[sel]), np.exp(4 * rho[sel])], 1)
    co = np.linalg.lstsq(A, f[sel], rcond=None)[0]
    return co[0]

def ddrho_up(f, speed, h, gl, gr):
    """5th-order upwind-biased d/drho; f (N,M); gl, gr ghost arrays (3,M)."""
    F = np.concatenate([gl, f, gr], 0)
    N = f.shape[0]; i = np.arange(3, 3 + N)
    dp = (-2 * F[i - 3] + 15 * F[i - 2] - 60 * F[i - 1] + 20 * F[i] + 30 * F[i + 1] - 3 * F[i + 2]) / (60 * h)
    dm = (3 * F[i - 2] - 30 * F[i - 1] - 20 * F[i] + 60 * F[i + 1] - 15 * F[i + 2] + 2 * F[i + 3]) / (60 * h)
    return np.where(speed >= 0, dp, dm)

def ddrho_c(f, h, gl, gr):
    F = np.concatenate([gl, f, gr], 0)
    N = f.shape[0]; i = np.arange(3, 3 + N)
    return (-F[i - 3] + 9 * F[i - 2] - 45 * F[i - 1] + 45 * F[i + 1] - 9 * F[i + 2] + F[i + 3]) / (60 * h)

def ghosts(g, f, kind, a):
    h = g['h']
    sphi = np.sin(g['phi'])
    d = np.array([3, 2, 1])[:, None] * h
    if kind == 'Phi':
        base = a * sphi[None, :]
        gl = base + (f[0] - a * sphi)[None, :] * np.exp(-2 * d)
    else:
        gl = f[0][None, :] * np.exp(-2 * d)
    # right: cubic extrapolation
    x = np.arange(4)
    pts = f[-4:]
    gr = []
    for k in (4, 5, 6):
        L = np.ones(4)
        for p in range(4):
            for q in range(4):
                if q != p:
                    L[p] *= (k - x[q]) / (x[p] - x[q])
        gr.append(L @ pts)
    return gl, np.array(gr)

NORM = {'mode': 'b1'}

def xaxis_tau(g, Phi):
    """tau(rho) = Theta_y(x, 0) = sum_m (2m+1) T_m."""
    return (Phi @ g['STi'].T) @ g['kT']

def cl_xh(g, Phi, cw, a):
    """c_l that keeps tau = Theta_y(x,0) fixed at the node i0 (N2-type normalization):
    tau_s = -(c_l x + U1) tau_x - (d_y U2 - 2 c_w) tau on the x-axis."""
    i0 = NORM['i0']; h = g['h']
    tau = xaxis_tau(g, Phi)
    r0 = np.exp(g['rho'][i0])
    st = np.array([1, -8, 0, 8, -1]) / (12 * h)
    tau_rho = st @ tau[i0 - 2:i0 + 3]
    tau_x = tau_rho / r0
    Q = g['_Q'][i0]; Qp = g['_Qp'][i0]; n = g['nO']
    U1 = -r0 * np.sum(n * Q)
    dyU2 = np.sum(n * (Qp + Q))
    k = NORM['kappa']
    cl = (-U1 * tau_x - (dyU2 - 2 * cw) * tau[i0] + k * (tau[i0] - NORM['tau_t'])) / (r0 * tau_x)
    return cl, tau[i0]

def rhs(g, Phi, Om, a, b1t, kappa, lam_tail):
    h = g['h']
    Urr, Upr, c, d1md2, wc = biot_savart(g, Om, lam_tail)
    rho = g['rho']
    # local coefficients at the origin
    Tc = Phi @ g['STi'].T
    alpha0 = fit_r2(rho, Tc[:, 0] - a, 1e-3, 2e-2)
    alpha1 = fit_r2(rho, Tc[:, 1], 1e-3, 2e-2)
    b1 = alpha0 + 3 * alpha1
    gco = 2 * fit_r2(rho, wc[:, 0], 1e-3, 2e-2)
    d1pd2 = -gco / 6
    d1 = 0.5 * (d1pd2 + d1md2)
    cw = c / 2
    if NORM['mode'] == 'b1':
        cl = c - 3 * a * d1 / (2 * b1) + kappa * (b1 - b1t) / (2 * b1)
    else:
        cl, _ = cl_xh(g, Phi, cw, a)
    Wr = cl + Urr
    glP, grP = ghosts(g, Phi, 'Phi', a)
    glO, grO = ghosts(g, Om, 'Om', a)
    Phi_r = ddrho_up(Phi, Wr, h, glP, grP)
    Om_r = ddrho_up(Om, Wr, h, glO, grO)
    Phi_rc = ddrho_c(Phi, h, glP, grP)
    Phi_p = (Phi @ g['STi'].T) @ g['CT'].T
    Om_p = (Om @ g['SOi'].T) @ g['CO'].T
    cph = np.cos(g['phi'])[None, :]; sph = np.sin(g['phi'])[None, :]
    Thx = cph * (Phi + Phi_rc) - sph * Phi_p
    dOm = -Wr * Om_r - Upr * Om_p + cw * Om + Thx
    dPhi = -Wr * Phi_r - Upr * Phi_p + (2 * cw - Urr) * Phi
    diag = dict(c=c, cw=cw, cl=cl, b1=b1, d1=d1, g=gco, maxW=np.abs(Wr).max(), maxUp=np.abs(Upr).max())
    return dPhi, dOm, diag

def filt(g, Phi, Om):
    Tc = (Phi @ g['STi'].T) * g['filT']
    Wc = (Om @ g['SOi'].T) * g['filO']
    return Tc @ g['ST'].T, Wc @ g['SO'].T

def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 32
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 512
    smax = float(sys.argv[3]) if len(sys.argv) > 3 else 20.0
    A = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    tag = sys.argv[5] if len(sys.argv) > 5 else 'run'
    rmin, rmax = 1e-4, 1e6
    g = build(M, N, rmin, rmax)
    r = np.exp(g['rho'])[:, None]
    phi = g['phi'][None, :]
    a = A; b1t = -A
    Phi = A * np.sin(phi) * np.exp(-r ** 2) + 0 * r
    B = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
    Om = -B * A * 0.5 * r ** 2 * np.sin(2 * phi) * np.exp(-r ** 2)
    kappa = 2.0
    NORM['mode'] = sys.argv[6] if len(sys.argv) > 6 else 'b1'
    if NORM['mode'] == 'xh':
        r_n = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
        NORM['i0'] = int(np.argmin(np.abs(g['rho'] - np.log(r_n))))
        NORM['tau_t'] = xaxis_tau(g, Phi)[NORM['i0']]
        NORM['kappa'] = 1.0
        print('xh normalization at r =', np.exp(g['rho'][NORM['i0']]), 'tau target', NORM['tau_t'], flush=True)
    lam_tail = 1.0 / 3.0
    s = 0.0; it = 0
    outdir = os.path.dirname(os.path.abspath(__file__))
    t0 = time.time()
    hist = []
    while s < smax:
        dPhi, dOm, dg = rhs(g, Phi, Om, a, b1t, kappa, lam_tail)
        dt = 0.4 * min(g['h'] / max(dg['maxW'], 1e-3), 1.0 / (max(dg['maxUp'], 1e-3) * 2 * M))
        k1 = (dPhi, dOm)
        k2 = rhs(g, Phi + 0.5 * dt * k1[0], Om + 0.5 * dt * k1[1], a, b1t, kappa, lam_tail)[:2]
        k3 = rhs(g, Phi + 0.5 * dt * k2[0], Om + 0.5 * dt * k2[1], a, b1t, kappa, lam_tail)[:2]
        k4 = rhs(g, Phi + dt * k3[0], Om + dt * k3[1], a, b1t, kappa, lam_tail)[:2]
        Phi = Phi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        Om = Om + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        Phi, Om = filt(g, Phi, Om)
        s += dt; it += 1
        beta = dg['cl'] / (-dg['cw']) if dg['cw'] < 0 else np.nan
        if np.isfinite(beta) and 2.05 < beta < 20:
            lam_tail = 1.0 / beta
        if it % 10 == 0 or s >= smax:
            res = (np.abs(dPhi).max(), np.abs(dOm).max())
            hist.append([s, dg['c'], dg['cw'], dg['cl'], beta, dg['b1'], dg['d1'], np.abs(Om).max(), res[0], res[1]])
            print(f"it {it} s {s:.4f} dt {dt:.2e} c {dg['c']:.6f} cl {dg['cl']:.6f} beta {beta:.5f} "
                  f"a0P {a/dg['cw']**2 if dg['cw']!=0 else np.nan:.5f} b1 {dg['b1']:.5f} d1 {dg['d1']:.5f} "
                  f"max|Om| {np.abs(Om).max():.4e} |dPhi| {res[0]:.2e} |dOm| {res[1]:.2e} wall {time.time()-t0:.0f}s",
                  flush=True)
            if not np.all(np.isfinite(Phi)) or not np.all(np.isfinite(Om)):
                print('NaN, stop'); break
        if int(s / 5.0) > int((s - dt) / 5.0):
            np.savez(os.path.join(outdir, f'dr_{tag}_s{int(s/5.0)*5:03d}.npz'), Phi=Phi, Om=Om, rho=g['rho'], phi=g['phi'],
                     hist=np.array(hist), a=a, M=M, N=N)
        if it % 10 == 0 and (np.abs(dOm).max() > 1e3 or dt < 1e-6):
            print('blow-up of the discrete solution, stop', flush=True); break
        if it % 1000 == 0 or s >= smax:
            np.savez(os.path.join(outdir, f'dr_{tag}.npz'), Phi=Phi, Om=Om, rho=g['rho'], phi=g['phi'],
                     hist=np.array(hist), a=a, M=M, N=N)
    np.savez(os.path.join(outdir, f'dr_{tag}.npz'), Phi=Phi, Om=Om, rho=g['rho'], phi=g['phi'],
             hist=np.array(hist), a=a, M=M, N=N)

if __name__ == '__main__':
    main()
