"""V27 (audit of referee result 8), numerical parts, own code only (no lead code imported or copied).
(a) trial seed (25): f = x^2 (1+r^2/L^2)^{(p-2)/2} [(1 + a y/sqrt(L^2+r^2))^2 + eps x y/(L^2+r^2)], L = 4(1-p)(1-p/2),
    a = 1/2, eps = 1/4, p = 1/l, l = 3, 4, 6, 10.  Claims: c = psi_xy(0) = L a/(2(1-p)) = 1 - p/2, psi_xx(0) = psi_yy(0) = 0
    (referee result 8 (25)); notes of the lead analyst 21:49Z item 1(iii): kappa = Q/(pi c^2) = -0.88, -1.02, -1.16, -1.28 vs profile values
    2(1-p)/(2-p) = 0.80, 0.857, 0.909, 0.947.  Methods: c, psi_xx(0) by direct polar quadrature (composite Gauss-Legendre
    in r to 1e10 + exact r^p tail, trapezoid in th) and by code/charsolve.py moments; Q = int rho W.grad(r^-3 sin 3th) with W
    from code/charsolve.py (exact radial Green's function per Fourier mode, tail r^p A beyond L); min V_r/r of
    b_p = Z + W[f_p] (original variables are a dilation: V_r/r = (b_p)_r/(p r); kappa is scale invariant).
(b) referee result 8 01-exterior (3)/(12): bounded manufactured density f = x^2 (1 + a y/<r>)^2/(1 + r^2) + eps x^3 y/(1+r^2)^2
    (A = cos^2 th[(1 + a sin th)^2 + eps cos th sin th], f - A = O(r^-2)); claim w = C_A log r + B(th) + d + o(1),
    C_A = (b_2/2, -a_2/2), B = -Psi' e_r + (Psi + Q) e_th, Psi'' + Psi = sin th A' - 2Q (first harmonics 0),
    Q = -(a_2 cos th + b_2 sin th)/2.  W from code/charsolve.py with tail exponent 0; Psi by FFT.
usage: python3 tests/v27_seed.py [seed|log]"""
import numpy as np, torch, sys, math, json
sys.path.insert(0, 'code')
from charsolve import CharSolver
dev = 'cuda'; DT = torch.float64


def seed(X, Y, p, a=0.5, eps=0.25):
    L = 4*(1 - p)*(1 - p/2)
    r2 = X*X + Y*Y
    return X*X*(1 + r2/L**2)**((p - 2)/2)*((1 + a*Y/torch.sqrt(L**2 + r2))**2 + eps*X*Y/(L**2 + r2))


def quad_moments(f, p, nt=1024, r1=1e-6, Lq=1e10, ratio=1.1, q=8):
    n = int(np.ceil(np.log(Lq/r1)/np.log(ratio)))
    e = np.concatenate([[0.0], np.geomspace(r1, Lq, n + 1)])
    xg, wg = np.polynomial.legendre.leggauss(q)
    a_, b_ = e[:-1, None], e[1:, None]
    r = torch.tensor(((a_ + b_)/2 + (b_ - a_)/2*xg[None]).ravel(), dtype=DT, device=dev)
    w = torch.tensor(((b_ - a_)/2*wg[None]).ravel(), dtype=DT, device=dev)
    th = 2*math.pi*torch.arange(nt, dtype=DT, device=dev)/nt
    X = r[:, None]*torch.cos(th)[None]; Y = r[:, None]*torch.sin(th)[None]
    e3 = torch.exp(-3j*th.to(torch.complex128))
    r3 = (f(X, Y).to(torch.complex128)*e3[None]).mean(1)
    I = torch.sum(w*r3/r**2)
    r3L = (f(Lq*torch.cos(th), Lq*torch.sin(th)).to(torch.complex128)*e3).mean()
    I = I + r3L/(Lq*(1 - p))
    return float(-2*I.imag), float(2*I.real)      # c = psi_xy(0), psi_xx(0)


def solver(nt=256, L=1e10, q=8):
    r1 = 1e-6
    edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12), np.geomspace(0.1, 10, 25)[1:],
                            np.geomspace(10, L, int(round(np.log10(L/10)*5)) + 1)[1:]])
    return CharSolver(edges, q, nt, r1, dev)


def Qkappa(S, rho, p):
    c, b = S.moments(rho, p)
    W1, W2 = S.velocity(rho, p)
    g1 = 3*S.R**-4*(-torch.sin(3*S.TH)*S.cs - torch.cos(3*S.TH)*S.sn)
    g2 = 3*S.R**-4*(-torch.sin(3*S.TH)*S.sn + torch.cos(3*S.TH)*S.cs)
    wq = S.w[:, None]*S.r[:, None]*(2*math.pi/S.nt)
    Q = float(torch.sum(wq*rho*(W1*g1 + W2*g2)))
    Vr_r = 1 + (W1*S.cs + W2*S.sn)/S.R            # (b_p)_r/r, b_p = Z + W[f_p]; original V_r/r = (b_p)_r/(p r)
    k0 = S.p0*S.q
    return float(c), float(b), Q, Q/(math.pi*float(c)**2), float(Vr_r[k0:].min())


def run_seed():
    for ntv in (128, 256):
        S = solver(ntv)
        for l in (3.0, 4.0, 6.0, 10.0):
            p = 1/l
            for eps in (0.0, 0.25):
                f = lambda X, Y: seed(X, Y, p, 0.5, eps)
                cq, pxx = quad_moments(f, p)
                rho = f(S.X, S.Y)
                c, b, Q, kap, mvr = Qkappa(S, rho, p)
                print(json.dumps(dict(l=l, p=p, eps=eps, ntv=ntv, c_quad=cq, c_claim=1 - p/2, psixx_quad=pxx, c_cs=c, b_cs=b,
                                      Q=Q, kappa=kap, kappa_profile=2*(1 - p)/(2 - p), min_bpr_over_r=mvr,
                                      rho_min=float(rho.min()))), flush=True)


def run_log(a=0.5, eps=0.25):
    nt = 256
    S = solver(nt, L=1e10)
    f = lambda X, Y: X*X*(1 + a*Y/torch.sqrt(1 + X*X + Y*Y))**2/(1 + X*X + Y*Y) + eps*X**3*Y/(1 + X*X + Y*Y)**2
    rho = f(S.X, S.Y)
    W1, W2 = S.velocity(rho, 0.0)
    W1 = W1.cpu().numpy(); W2 = W2.cpu().numpy(); r = S.r.cpu().numpy(); th = S.th.cpu().numpy()
    # exterior angular data
    A = np.cos(th)**2*((1 + a*np.sin(th))**2 + eps*np.cos(th)*np.sin(th))
    a2 = 2*np.mean(A*np.cos(2*th)); b2 = 2*np.mean(A*np.sin(2*th))
    CA = np.array([b2/2, -a2/2])
    m = np.fft.fftfreq(nt, 1.0/nt)
    Ap = np.fft.ifft(1j*m*np.fft.fft(A)).real
    Qf = -0.5*(a2*np.cos(th) + b2*np.sin(th))
    rhs = np.sin(th)*Ap - 2*Qf
    Rh = np.fft.fft(rhs)
    res_first = np.abs(Rh[np.abs(m) == 1]).max()/nt
    Ph = np.where(np.abs(m) == 1, 0, Rh/np.where(np.abs(m) == 1, 1, 1 - m**2))
    Psi = np.fft.ifft(Ph).real; Psip = np.fft.ifft(1j*m*Ph).real
    Br = -Psip; Bt = Psi + Qf
    B1 = Br*np.cos(th) - Bt*np.sin(th); B2 = Br*np.sin(th) + Bt*np.cos(th)
    out = dict(a2=a2, b2=b2, CA=list(CA), solvability_first_harmonic=res_first, rows=[])
    for rr in (1e2, 1e3, 1e4, 1e5, 1e6, 1e7):
        k = int(np.argmin(np.abs(r - rr)))
        D1 = W1[k] - CA[0]*np.log(r[k]) - B1; D2 = W2[k] - CA[1]*np.log(r[k]) - B2
        out['rows'].append(dict(r=float(r[k]), d=[float(D1.mean()), float(D2.mean())],
                                dev_from_const=float(max(np.abs(D1 - D1.mean()).max(), np.abs(D2 - D2.mean()).max())),
                                W_max=float(max(np.abs(W1[k]).max(), np.abs(W2[k]).max()))))
    # log slope from two radii: (W(r2) - W(r1))/log(r2/r1), angular mean
    k1 = int(np.argmin(np.abs(r - 1e4))); k2 = int(np.argmin(np.abs(r - 1e7)))
    sl = [float(np.mean((W1[k2] - W1[k1])/np.log(r[k2]/r[k1]))), float(np.mean((W2[k2] - W2[k1])/np.log(r[k2]/r[k1])))]
    out['slope_1e4_1e7'] = sl
    print(json.dumps(out), flush=True)


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'seed'
    if mode == 'seed':
        run_seed()
    else:
        run_log()
