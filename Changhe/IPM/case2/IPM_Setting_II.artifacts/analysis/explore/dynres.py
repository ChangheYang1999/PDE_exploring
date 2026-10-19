"""
Lead's exploratory dynamic-rescaling code (CPU, numpy) for the IPM Setting II profile system.
Full plane, log-polar grid t = log r in [t0,t1], theta Fourier (all modes, NO symmetry imposed).
Evolves  rho_s = rho - (c_l(s) X + W[rho]).grad rho,  c_l(s) = 1/2 + psi_xy(0)(s).
Unknown stored as q = rho / w(r), w = r^2 (1+r^2)^{(p0-2)/2}.
Velocity: canonical once-subtracted Biot-Savart, per Fourier mode (specification 4.2), via exponential
recursions in t; inner part (t<t0) from the jet rho = x^2; outer tail (t>t1) from power law r^{p}, p=1/c_l.
"""
import numpy as np, sys, time, json

class Grid:
    def __init__(s, t0=-10., t1=12., Nt=551, Nth=256, p0=0.5):
        s.t = np.linspace(t0, t1, Nt); s.h = s.t[1]-s.t[0]; s.Nt=Nt; s.Nth=Nth
        s.th = 2*np.pi*np.arange(Nth)/Nth
        s.r = np.exp(s.t)
        s.p0 = p0
        r = s.r[:,None]
        s.w = (r**2)*(1+r**2)**((p0-2)/2)
        s.om = 2 + (p0-2)*r**2/(1+r**2)          # d_t log w
        s.n = np.fft.fftfreq(Nth, 1.0/Nth)        # integer modes
        s.cos = np.cos(s.th)[None,:]; s.sin = np.sin(s.th)[None,:]
        # dealias filter (exponential, 36th order)
        kmax = Nth//2
        s.filt = np.exp(-36*(np.abs(s.n)/kmax)**36)

    def dth(s, f):
        return np.real(np.fft.ifft(1j*s.n[None,:]*np.fft.fft(f, axis=1), axis=1))

    def dt_c4(s, f, left, right):
        """4th-order centred d/dt with 2 ghost rows each side (left: rows t0-2h,t0-h; right: t1+h,t1+2h)."""
        F = np.vstack([left, f, right]); h=s.h
        return (F[0:-4] - 8*F[1:-3] + 8*F[3:-1] - F[4:])/(12*h)

def ghosts(G, q, p):
    """ghost rows for q: inflow from jet rho=x^2 (exact to O(r^3)); outflow: rho ~ r^p along rays."""
    tl = G.t[0] - G.h*np.array([2.,1.]); rl = np.exp(tl)[:,None]
    wl = rl**2*(1+rl**2)**((G.p0-2)/2)
    left = (rl**2*G.cos**2)/wl
    tr = G.t[-1] + G.h*np.array([1.,2.]); rr = np.exp(tr)[:,None]
    wr = rr**2*(1+rr**2)**((G.p0-2)/2)
    rho1 = q[-1:,:]*G.w[-1:,:]
    right = rho1*np.exp(p*(tr[:,None]-G.t[-1]))/wr
    return left, right

def expint_coeffs(kap, h):
    """y_{k+1} = E y_k + A g_k + B g_{k+1} solves y' = -kap y + g, g linear on the cell."""
    kap = np.asarray(kap, float); x = kap*h
    E = np.exp(-x)
    small = np.abs(x) < 1e-4
    xs = np.where(small, 1.0, x)
    phi1 = np.where(small, h*(1 - x/2 + x**2/6), (1-E)/np.where(small,1.0,kap))
    phi2 = np.where(small, h*(0.5 - x/6 + x**2/24), (1/np.where(small,1.0,kap)) - (1-E)/(np.where(small,1.0,kap)**2*h))
    return E, phi1-phi2, phi2

def recur_fwd(gm, kap, h, y0):
    """forward recursion over t index (axis 0) for each mode column."""
    E, A, B = expint_coeffs(kap, h)
    y = np.empty_like(gm); y[0] = y0
    for k in range(gm.shape[0]-1):
        y[k+1] = E*y[k] + A*gm[k] + B*gm[k+1]
    return y

def recur_bwd(gm, kap, h, yN):
    """backward: z(t) = int_t^inf e^{-kap (t'-t)} g(t') dt'  =>  z' = kap z - g; march from t1 down."""
    E, A, B = expint_coeffs(kap, h)
    z = np.empty_like(gm); z[-1] = yN
    for k in range(gm.shape[0]-1, 0, -1):
        z[k-1] = E*z[k] + A*gm[k] + B*gm[k-1]
    return z

def velocity(G, q, p):
    """returns a = c_l-part excluded: (Wr/r, Wth/r) on grid, and c, b'=psi_xx(0), plus g modes"""
    left, right = ghosts(G, q, p)
    qt = G.dt_c4(q, left, right)
    qth = G.dth(q)
    rho_t = G.w*(qt + G.om*q)            # r d_r rho
    rho_th = G.w*qth
    g = (G.cos*rho_t - G.sin*rho_th)/G.r[:,None]     # d_x rho
    gm = np.fft.fft(g, axis=1)/G.Nth                 # modes g_n(t), n = G.n
    n = G.n; an = np.abs(n); h = G.h; r0 = G.r[0]
    # inner (t < t0) contributions from jet: g = 2 r cos th -> g_{+-1} = r
    # P~ = int_{-inf}^t e^{-(|n|+2)(t-t')} g dt'
    P0 = np.zeros(G.Nth, complex)
    P0[an==1] = r0/4.0
    P = recur_fwd(gm, an+2.0, h, P0)
    # Q~ : |n|>=2: int_t^inf e^{-(|n|-2)(t'-t)} g ; tail with g ~ e^{(p-1)(t'-t1)}
    QN = np.zeros(G.Nth, complex)
    m2 = an>=2
    QN[m2] = gm[-1, m2]/(an[m2]-1.0-p)
    Q = recur_bwd(gm, np.where(m2, an-2.0, 1.0), h, QN)
    # |n|=1 renormalised: Q~ = - int_{-inf}^t e^{-(t-t')} g dt' ; inner jet part: -r0/2
    Q1init = np.zeros(G.Nth, complex); Q1init[an==1] = -r0/2.0
    Q1 = -recur_fwd(gm, np.ones(G.Nth), h, -Q1init)
    # n=0: psi0'/r = -P~_0 (with kappa=2) ; P computed with an+2=2 for n=0 already
    psi_r2 = np.zeros_like(gm); dpsi_r = np.zeros_like(gm)
    ms = m2
    psi_r2[:, ms] = (P[:, ms] + Q[:, ms])/(2*an[ms])
    dpsi_r[:, ms] = (-P[:, ms] + Q[:, ms])/2
    m1 = an==1
    psi_r2[:, m1] = (P[:, m1] + Q1[:, m1])/2
    dpsi_r[:, m1] = (-P[:, m1] + Q1[:, m1])/2
    m0 = an==0
    dpsi_r[:, m0] = -P[:, m0]
    Wr_r = np.real(np.fft.ifft(-1j*n[None,:]*psi_r2*G.Nth, axis=1))
    Wt_r = np.real(np.fft.ifft(dpsi_r*G.Nth, axis=1))
    # psi_2(r)/r^2 -> (b' - i c)/4 as r->0 : equals (P+Q)/4 at t0 (P~0 there) for n=+2
    i2 = np.where(n==2)[0][0]
    val = (P[0,i2] + Q[0,i2])        # = b' - i c  (times 1)
    c = -val.imag; bp = val.real
    return Wr_r, Wt_r, c, bp, rho_t, rho_th, g

def upwind_dt(G, q, a, left, right):
    """3rd-order upwind-biased d/dt with flux splitting on velocity a (array same shape)."""
    F = np.vstack([left, q, right]); h=G.h
    # indices: F[k+2] = q[k]
    qm2, qm1, q0, qp1, qp2 = F[0:-4], F[1:-3], F[2:-2], F[3:-1], F[4:]
    Dm = (qm2 - 6*qm1 + 3*q0 + 2*qp1)/(6*h)     # left-biased (for a>0)
    Dp = (-2*qm1 - 3*q0 + 6*qp1 - qp2)/(6*h)    # right-biased (for a<0)
    return np.where(a>0, Dm, Dp)

def rhs(G, q):
    # p from current c_l: need c first (velocity uses p in the tail only)
    global P_CUR
    Wr_r, Wt_r, c, bp, rho_t, rho_th, g = velocity(G, q, P_CUR)
    cl = 0.5 + c
    a = cl + Wr_r
    b = Wt_r
    left, right = ghosts(G, q, P_CUR)
    qt = upwind_dt(G, q, a, left, right)
    qth = G.dth(q)
    dq = q - a*(qt + G.om*q) - b*qth
    return dq, dict(c=c, bp=bp, cl=cl, amin=a.min())

def filt(G, q):
    return np.real(np.fft.ifft(np.fft.fft(q,axis=1)*G.filt[None,:], axis=1))

P_CUR = 0.5
if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=float, default=1.0)
    ap.add_argument('--eps', type=float, default=0.0)   # asymmetric perturbation
    ap.add_argument('--p0', type=float, default=0.5)
    ap.add_argument('--T', type=float, default=40.0)
    ap.add_argument('--ds', type=float, default=0.004)
    ap.add_argument('--Nt', type=int, default=551)
    ap.add_argument('--Nth', type=int, default=256)
    ap.add_argument('--t0', type=float, default=-10.)
    ap.add_argument('--t1', type=float, default=12.)
    ap.add_argument('--out', type=str, default='runs/dyn0')
    ap.add_argument('--init', type=str, default='')
    ap.add_argument('--shape', type=str, default='poly')   # 'poly' (old) or 'pos' (positive off x=0)
    ap.add_argument('--L', type=float, default=2.0)
    args = ap.parse_args()
    G = Grid(args.t0, args.t1, args.Nt, args.Nth, args.p0)
    r = G.r[:,None]; X = r*G.cos; Y = r*G.sin
    if args.init:
        d = np.load(args.init); q = d['q']; P_CUR = float(d['p'])
    elif args.shape == 'pos':
        # rho0 = x^2 (1 + a y / sqrt(L^2+r^2)) (1 + r^2/L^2)^{(p0-2)/2}, |a|<1: rho0 > 0 off x=0, jet x^2,
        # c(rho0) = a L / (4 (1-p0)) exactly (I2).  eps: x-odd perturbation eps x^3/(L^2+r^2) * same radial factor
        F = (1+r**2/args.L**2)**((args.p0-2)/2)
        rho0 = X**2*(1 + args.a*Y/np.sqrt(args.L**2+r**2))*F + args.eps*X**3*F/np.sqrt(args.L**2+r**2)
        q = rho0/G.w
        P_CUR = args.p0
    else:
        rho0 = X**2*(1+args.a*Y)**2*(1+r**2)**((args.p0-4)/2) + args.eps*X**2*Y*X*(1+r**2)**((args.p0-4)/2)
        q = rho0/G.w
        P_CUR = args.p0
    s = 0.0; ds = args.ds; hist = []
    tw = time.time(); k = 0
    while s < args.T:
        # SSP-RK3
        k1, info = rhs(G, q)
        q1 = q + ds*k1
        k2, _ = rhs(G, q1)
        q2 = 0.75*q + 0.25*(q1 + ds*k2)
        k3, _ = rhs(G, q2)
        q = q/3 + 2/3*(q2 + ds*k3)
        q = filt(G, q)
        s += ds; k += 1
        P_CUR = 1.0/max(info['cl'], 1e-3) if info['cl']>1 else P_CUR
        if k % 125 == 0:
            res = np.abs(k1*G.w)/(np.abs(q*G.w)+1e-300)
            # odd part in x: theta -> pi - theta
            idx = (G.Nth//2 - np.arange(G.Nth)) % G.Nth
            odd = np.abs(q - q[:, idx]).max()/np.abs(q).max()
            mask = (G.t > -6) & (G.t < 6)
            rk = np.abs(k1[mask]).max()/np.abs(q[mask]).max()
            hist.append(dict(s=s, cl=info['cl'], c=info['c'], bp=info['bp'], amin=info['amin'], res=rk, odd=odd, qmax=float(np.abs(q).max())))
            print(json.dumps(hist[-1]), flush=True)
            np.savez(args.out+'.npz', q=q, p=P_CUR, s=s, t=G.t, th=G.th, p0=G.p0)
            if not np.isfinite(q).all() or np.abs(q).max() > 1e8:
                print('blew up'); break
    print('wall', time.time()-tw)
