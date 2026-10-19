"""First-order far-field consistency of a trial (lead, analysis section 14).
rho = r^k Theta0 (1 + r^(k-1) Theta1 + ...). The order r^(2k-1) of (c_l X + U).grad rho = rho gives
(1 - c_l) rho_1 + U_0.grad rho_0 = 0, so Theta1_exact = [(k+1) F Theta0'/Theta0 - k F'] / (c_l - 1),
psi_0 = r^(k+1) F(theta), F_n = G_n / (4 n^2 - (k+1)^2), G_n the sin(2 n theta) coefficients of
g = k cos Theta0 - sin Theta0' (d_x rho_0 = r^(k-1) g). Compares with the formula's Theta1."""
import sys, json
import numpy as np
from numpy.polynomial.chebyshev import chebval, chebder
import os
_here = os.path.dirname(os.path.abspath(__file__))
for _d in ('c7', os.path.join(_here, '..', 'b_fit_domain')):
    if os.path.isdir(_d): sys.path.insert(0, _d)
from trial import Trial

def run(path, N=1 << 15, verbose=True):
    t = Trial(path); k, L = t.k, t.L; cl = 1/k; a = t.p3-2
    b1 = t.spline(1.0); bp1 = t.spline(1.0, nu=1)
    T1 = chebval(1.0, t.singular); Tp1 = chebval(1.0, chebder(t.singular))
    th = 2*np.pi*np.arange(N)/N
    m = np.arange(t.angular+1)
    c, s = np.cos(th), np.sin(th); ac = np.abs(c)
    cosm = np.cos(2*np.outer(th, m)); sinm = np.sin(2*np.outer(th, m))
    ang = ac**a*s**2
    ang_t = 2*ac**(a+1)*np.sign(c)*s-a*ac**(a-1)*np.sign(c)*s**3
    E = cosm@b1+T1*ang; Ep = sinm@(-2*m*b1)+T1*ang_t
    pre = L**(3-k)*np.exp(E)
    Th0 = pre*c*c*s
    Th0p = pre*((c**3-2*c*s*s)+c*c*s*Ep)
    g = k*c*Th0-s*Th0p
    # sin(2 n theta) coefficients by FFT (periodic trapezoid)
    Gh = np.fft.rfft(g)/N
    n2 = np.arange(len(Gh))            # frequency index j; sin(j theta) coeff = -2 Im(Gh_j)
    sinco = -2*Gh.imag
    j = n2[2::2]; Gn = sinco[2::2]; n = j//2
    Fn = Gn/(4*n*n-(k+1)**2)
    F = np.sin(np.outer(th, j))@Fn if N <= 1 << 13 else None
    # synthesize via inverse FFT for speed
    spec = np.zeros(len(Gh), complex); spec[j] = -0.5j*Fn*N
    F = np.fft.irfft(spec, n=N)
    specp = np.zeros(len(Gh), complex); specp[j] = 0.5*(j*Fn)*N
    Fp = np.fft.irfft(specp, n=N)
    # check: odd modes of g only even j? report energy in odd j and cos parts
    leak = np.max(np.abs(sinco[1::2]))/np.max(np.abs(Gn))
    cosleak = np.max(np.abs(Gh.real[1:]))/np.max(np.abs(Gn))
    sel = (th > 1e-3) & (th < np.pi/2-1e-3)
    Th1e = ((k+1)*F*Th0p/Th0-k*Fp)/(cl-1)
    Th1f = -L**(1-k)*(cosm@bp1+2*Tp1*ang)
    d = Th1f-Th1e
    tt = th[sel]
    out = dict(path=path, k=k, c_l=cl, L=L, N=N, mmax=int(t.angular), leak_odd=float(leak), leak_cos=float(cosleak),
               Gn_tail=float(np.max(np.abs(Gn[-200:]))/np.max(np.abs(Gn))),
               Th1e_max=float(np.max(np.abs(Th1e[sel]))), Th1f_max=float(np.max(np.abs(Th1f[sel]))),
               diff_max=float(np.max(np.abs(d[sel]))), diff_at=float(tt[np.argmax(np.abs(d[sel]))]),
               coef_RNv=float((cl-1)/(1+k)), )
    # predicted leading normalized residual (c_l-1)|dTh1| r^(k-1)/(1+k) at r = 3.6e4 and 1e4 L
    for r in [1000*L, 3.6e4, 1e4*L, 1e6*L]:
        out['pred_r%.3g' % r] = float(out['coef_RNv']*out['diff_max']*r**(k-1))
    if verbose:
        for th0 in [0.0, 0.3, 0.6, 0.84, 1.0, 1.3, 1.5, 1.55, 1.565]:
            i = np.argmin(np.abs(th-th0)) if th0 > 0 else 1
            print('theta %.4f  Th0 %.6e  Th1_formula %+.6e  Th1_exact %+.6e  diff %+.3e' % (th[i], Th0[i], Th1f[i], Th1e[i], d[i]))
    return out, (th, Th0, Th1f, Th1e)

if __name__ == '__main__':
    for p in sys.argv[1:]:
        o, _ = run(p)
        print(json.dumps(o, indent=1))
