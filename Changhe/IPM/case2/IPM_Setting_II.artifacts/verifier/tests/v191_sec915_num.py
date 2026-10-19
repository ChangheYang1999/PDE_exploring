"""Numerical check of Remark 4.11 / SEC915 Step 14 for a non-polynomial C^2 A: spectral solution of
Psi'' + (p+1)^2 Psi = sin A' - p cos A, the exact first-mode formulas, and the rate of
(p/(1-p)) J_p[A] -> -(1/2) P_2 A' as p -> 0 (expected O(p))."""
import numpy as np
N = 512
th = 2 * np.pi * np.arange(N) / N
k = np.fft.fftfreq(N, 1.0 / N)
def d(u, m=1):
    return np.real(np.fft.ifft((1j * k)**m * np.fft.fft(u)))
for name, A in [('exp', np.exp(np.cos(th) + 0.3 * np.sin(2 * th) - 0.2 * np.cos(3 * th))),
                ('C2', np.abs(np.sin(th - 0.4))**3.5 + 0.5 + 0.1 * np.cos(2 * th)),
                ('noa2', 1 + 0.4 * np.cos(th) + 0.3 * np.cos(3 * th) + 0.2 * np.sin(4 * th))]:
    Ap = d(A)
    Abar = A.mean(); a2 = 2 * np.mean(A * np.cos(2 * th)); b2 = 2 * np.mean(A * np.sin(2 * th))
    P2 = a2 * np.cos(th) + b2 * np.sin(th)
    print(name, 'Abar %.6f a2 %.6f b2 %.6f' % (Abar, a2, b2))
    for p in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        g = np.sin(th) * Ap - p * np.cos(th) * A
        Psi = np.real(np.fft.ifft(np.fft.fft(g) / ((p + 1)**2 - k**2)))
        res = np.max(np.abs(d(Psi, 2) + (p + 1)**2 * Psi - g))
        pc = 2 * np.mean(Psi * np.cos(th)); ps = 2 * np.mean(Psi * np.sin(th))
        e1 = abs(pc - (-Abar / (p + 2) - a2 / (2 * p))); e2 = abs(ps + b2 / (2 * p))
        J = (p + 1) * Psi * Ap - p * d(Psi) * A
        lim = -0.5 * P2 * Ap
        err = np.max(np.abs(p / (1 - p) * J - lim))
        Rp = Psi + P2 / (2 * p)
        print('  p %.3f ODE res %.1e  coeff err %.1e %.1e  sup|pJ/(1-p) - lim| %.3e  ratio/p %.3f  |R_p|,|R_p\'| %.3f %.3f'
              % (p, res, e1, e2, err, err / p, np.max(np.abs(Rp)), np.max(np.abs(d(Rp)))))
