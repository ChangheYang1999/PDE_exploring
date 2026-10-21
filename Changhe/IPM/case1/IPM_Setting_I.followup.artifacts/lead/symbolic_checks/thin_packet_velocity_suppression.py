# Lead check of the packet estimate (referee's (21)): for p = F(S, Y), F(S, Y) = Y exp(-S^2 - Y^2) (odd in Y), rescaled
# multipliers m1 = eps xi eta/(eps^2 xi^2 + eta^2), m2 = -eps^2 xi^2/(eps^2 xi^2 + eta^2). Fourier transform in S only
# (exact for the Gaussian), Y-convolution formula (22) by quadrature in Z; sup over a Y grid and the S grid.
import numpy as np
def sup_U(eps, Ymax=60.0):
    xi = np.linspace(-12, 12, 481)                    # Fhat(xi, Z) = sqrt(pi) exp(-xi^2/4) Z exp(-Z^2)
    Z = np.linspace(-7, 7, 1401); dZ = Z[1] - Z[0]
    Y = np.concatenate([np.linspace(-Ymax, -8, 105), np.linspace(-8, 8, 321), np.linspace(8, Ymax, 105)])
    FZ = Z*np.exp(-Z**2)
    T1 = np.zeros((len(xi), len(Y)), complex); T2 = np.zeros((len(xi), len(Y)))
    for i, x in enumerate(xi):
        k = eps*abs(x); A = np.sqrt(np.pi)*np.exp(-x**2/4)
        D = Y[:, None] - Z[None, :]
        K = np.exp(-k*np.abs(D))
        T1[i] = 0.5j*eps*x*A*(np.sign(D)*K) @ FZ*dZ
        T2[i] = -0.5*eps*abs(x)*A*(K @ FZ)*dZ
    S = np.linspace(-6, 6, 121); dxi = xi[1] - xi[0]
    E = np.exp(1j*np.outer(S, xi))/(2*np.pi)*dxi       # inverse transform in S
    u1 = np.real(E @ T1); u2 = np.real(E @ T2)
    return np.abs(u1).max(), np.abs(u2).max()
for eps in (0.2, 0.1, 0.05, 0.025, 0.0125):
    a, b = sup_U(eps)
    print('eps %.4f  sup|U1| %.4e  /eps %.4f   sup|U2| %.4e  /eps^2 %.4f' % (eps, a, a/eps, b, b/eps**2), flush=True)
