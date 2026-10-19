"""V23 numerical checks of referee result 6 01 Theorem 1 and 02 (8) (CPU, own code).
(a) H_p[A] from (1) equals the canonical velocity of F = r^p A (code/charsolve.py velocity, per-mode exact Green's function).
(b) W[rho] r^-p -> H on a test density with rho - F = O(r^{p-2}) (01 (3)).
(c) Manufactured exterior flow V = l X + H (H exact, divergence free), rho = F o S (stationary transport by construction):
    R^{1-2p}[rho(R w) - R^p A(w)] -> J_p[A](w)/(l-1), error O(R^{p-1}) (02 (3), (8), Lagrangian form 01 (4))."""
import numpy as np, torch, sys, math
sys.path.insert(0, 'code')
from scipy.integrate import solve_ivp
torch.set_num_threads(1)
N = 256
thg = 2*np.pi*np.arange(N)/N
def A_of(th, k=(0.3, 0.2)):
    return np.cos(th)**2*(1 + k[0]*np.sin(th) + k[1]*np.cos(th))
def psi_coef(p, Avals):
    """Fourier solution of Psi'' + (p+1)^2 Psi = (sin A)' - (p+1) cos A on the grid thg; returns callables Psi, Psi', A, A'."""
    m = np.fft.fftfreq(N, 1/N)
    Ah = np.fft.fft(Avals); sA = np.fft.fft(np.sin(thg)*Avals); cA = np.fft.fft(np.cos(thg)*Avals)
    rhs = 1j*m*sA - (p+1)*cA
    Ph = rhs/((p+1)**2 - m**2)
    def ev(coef, th, d=0):
        th = np.atleast_1d(th)
        return np.real(np.exp(1j*np.outer(th, m)) @ (coef*(1j*m)**d))/N
    return (lambda th: ev(Ph, th), lambda th: ev(Ph, th, 1), lambda th: ev(Ah, th), lambda th: ev(Ah, th, 1))
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
for p in (0.6, 0.5, 0.4):
    l = 1/p
    Psi, dPsi, Af, dAf = psi_coef(p, A_of(thg))
    print('p =', p, ' check (1) residual on grid:', end=' ')
    m = np.fft.fftfreq(N, 1/N); Ph = np.fft.fft(Psi(thg))
    lhs = np.real(np.fft.ifft(-(m**2)*Ph)) + (p+1)**2*Psi(thg)
    rhs = np.real(np.fft.ifft(1j*m*np.fft.fft(np.sin(thg)*A_of(thg)))) - (p+1)*np.cos(thg)*A_of(thg)
    print('%.2e' % np.abs(lhs - rhs).max(), flush=True)
    Hr = lambda th: -dPsi(th); Ht = lambda th: (p+1)*Psi(th)
    if mode in ('all', 'vel'):
        from charsolve import CharSolver
        r1 = 1e-6; L = 1e10
        edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12), np.geomspace(0.1, 10, 25)[1:],
                                np.geomspace(10, L, int(round(np.log10(L/10)*5)) + 1)[1:]])
        S = CharSolver(edges, 8, 64, r1, 'cpu')
        TH = S.TH.numpy(); Rr = S.R.numpy()
        for name, rho in (('F = r^p A', Rr**p*A_of(TH)),
                          ('rho = x^2 (1+ky/<r>+k2 x/<r>) <r>^{p-2}', (Rr*np.cos(TH))**2*(1 + 0.3*Rr*np.sin(TH)/np.sqrt(1+Rr**2)
                           + 0.2*Rr*np.cos(TH)/np.sqrt(1+Rr**2))*(1 + Rr**2)**((p-2)/2))):
            W1, W2 = S.velocity(torch.tensor(rho, dtype=torch.float64), p)
            W1 = W1.numpy(); W2 = W2.numpy()
            Wr = W1*np.cos(TH) + W2*np.sin(TH); Wt = -W1*np.sin(TH) + W2*np.cos(TH)
            line = []
            for r0 in (1.0, 1e2, 1e4, 1e8):
                i = np.argmin(np.abs(S.r.numpy() - r0)); rr = S.r.numpy()[i]
                e = max(np.abs(Wr[i]/rr**p - Hr(TH[i])).max(), np.abs(Wt[i]/rr**p - Ht(TH[i])).max())
                line.append('r=%.3g: %.2e' % (rr, e))
            print('  (a/b) %s: max |W r^-p - H| / max|H| = ' % name, ', '.join(line), ' (max|H| %.3f)' % max(np.abs(Hr(thg)).max(), np.abs(Ht(thg)).max()), flush=True)
    if mode in ('all', 'scat'):
        def rhs_ode(t, y):
            s, sig, th = y; u = math.exp((p - 1)*s)
            return [l - u*float(dPsi(th)[0]), -u*float(dPsi(th)[0]), (p+1)*u*float(Psi(th)[0])]
        J = lambda th: (p+1)*Psi(th)*dAf(th) - p*dPsi(th)*Af(th)
        ths = np.array([0.3, 1.2, 2.0, 3.5, 4.4, 5.9])
        print('  (c) J_p[A](w)/(l-1) at w =', np.round(ths, 2), ':', np.round(J(ths)/(l-1), 6))
        Ds = {}
        for R in (1e3, 1e5, 1e7, 1e9):
            D = []
            for th0 in ths:
                s0 = math.log(R); tmax = (40/(1 - p) - s0)/l + 5
                sol = solve_ivp(rhs_ode, (0, tmax), [s0, s0, th0], rtol=1e-12, atol=1e-13, method='DOP853')
                sig, thf = sol.y[1, -1], sol.y[2, -1]
                rho = math.exp(p*sig)*float(Af(thf)[0])
                D.append(R**(1 - 2*p)*(rho - R**p*float(Af(th0)[0])))
            Ds[R] = np.array(D)
            err = np.abs(Ds[R] - J(ths)/(l-1)).max()
            print('    R = %.0e: D =' % R, np.round(Ds[R], 6), ' max|D - J/(l-1)| = %.2e, R^{p-1} = %.2e' % (err, R**(p-1)), flush=True)
