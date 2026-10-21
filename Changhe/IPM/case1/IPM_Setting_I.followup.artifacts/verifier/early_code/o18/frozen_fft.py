# (o18)(b): numerical check of the fred31 frozen solutions with a cut-off: U_2[chi v] by FFT on a periodic box, compared
# with -E[v]/g near P.  The difference must be harmonic (smooth) near P; tested by a least-squares fit with harmonic
# polynomials of the right parity on R < Rfit.  Controls: the same fit with g replaced by 1.02 g.
import sys, numpy as np, torch
from scipy.special import hyp2f1
dev = 'cuda'
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4096
Lb = 6.0
h = 2*Lb/N
x = -Lb + (np.arange(N) + 0.5)*h          # no node on s = 0 or y = 0
S, Y = np.meshgrid(x, x, indexing='ij')
Rr = np.hypot(S, Y)

def chi(R, r1=1.5, r2=3.0):
    z = np.clip((R - r1)/(r2 - r1), 0, 1)
    f = lambda u: np.where(u > 0, np.exp(-1/np.maximum(u, 1e-300)), 0.0)
    return f(1 - z)/(f(1 - z) + f(z))

def I(m, s, y):
    """int_0^y (s^2 + t^2)^m dt for s != 0."""
    return y*np.abs(s)**(2*m)*hyp2f1(-m, 0.5, 1.5, -(y/s)**2)

def fields(kind, A):
    m = (A - 1)/2 if kind == 'V' else (2*A - 3)/2
    sel = Rr < 3.05
    s, y = S[sel], Y[sel]
    v = np.zeros_like(S); E = np.zeros_like(S)
    if kind == 'V':
        V = I(m, s, y); sVs = (A - 1)*s**2*I(m - 1, s, y)
        v[sel] = V; E[sel] = (A - 1)*(V + sVs); g = A**2 - 1
    else:
        Q = s*I(m, s, y); sQs = Q + (2*A - 3)*s**3*I(m - 1, s, y)
        v[sel] = Q; E[sel] = (A - 1)*(sQs + 2*Q); g = (A - 1)*(2*A + 1)
    return v, E, g

k = 2*np.pi*np.fft.fftfreq(N, d=h)
XI, ETA = np.meshgrid(k, k, indexing='ij')
K2 = XI**2 + ETA**2; K2[0, 0] = 1.0
mult = torch.tensor(-XI**2/K2, device=dev); mult[0, 0] = 0.0
ch = chi(Rr)
fit_sel = Rr < 0.6
sub = np.flatnonzero(fit_sel.ravel())[::7]
for kind, A in [('V', 2.5), ('Q', 1.75), ('Q', 2.0), ('V', 2.2)]:
    v, E, g = fields(kind, A)
    # spot check of the hypergeometric formulas against direct quadrature
    from scipy.integrate import quad
    i0 = np.unravel_index(np.argmin(np.abs(Rr - 0.4) + np.abs(S + 0.1)), S.shape)
    s0, y0 = S[i0], Y[i0]
    m = (A - 1)/2 if kind == 'V' else (2*A - 3)/2
    vq = quad(lambda t: (s0**2 + t**2)**m, 0, y0, epsabs=1e-14, epsrel=1e-13)[0]*(1 if kind == 'V' else s0)
    U2 = torch.fft.ifft2(mult*torch.fft.fft2(torch.tensor(ch*v, device=dev))).real.cpu().numpy()
    for fac in [1.0, 1.02]:
        H = U2 + E/(g*fac)
        s, y = S.ravel()[sub], Y.ravel()[sub]
        z = s + 1j*y
        ns = range(1, 16, 2) if kind == 'V' else range(2, 17, 2)     # Im z^n with the parity of v
        M = np.stack([np.imag(z**n) for n in ns] + [np.ones_like(s)], 1)
        c, *_ = np.linalg.lstsq(M, H.ravel()[sub], rcond=None)
        res = H.ravel()[sub] - M @ c
        print('%s_%s  N = %d  g factor %.2f: max|U_2| on R<0.6 = %.3e, max|U_2 + E/g| = %.3e, harmonic-fit residual = %.3e'
              '  (quad check of v: %.1e)' % (kind, A, N, fac, np.abs(U2.ravel()[sub]).max(), np.abs(H.ravel()[sub]).max(),
                                            np.abs(res).max(), abs(v[i0] - vq)), flush=True)
