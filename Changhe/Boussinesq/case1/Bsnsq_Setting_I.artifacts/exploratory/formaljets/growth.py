"""Experiment: growth of the formal centre series (Proposition 17 recursion run forwards, Proposition 26).
Psi = sum h_ij x^(2i+1) y^(2j+1), Theta = sum t_ij x^(2i) y^(2j+1), h_00 = -2, t_00 = a0; free data h_(n,0), n >= 1.
Block n: (P2) at x^(2i) y^(2j+1): L_ij t_ij + a0 (2i+1) h_ij + P_ij = 0; (P1) at x^(2i+1) y^(2j+1), i+j = n-1:
M_ij g_ij - 2(i+1) t_(i+1,j) + Q_ij = 0, g_ij = -A_i h_(i+1,j) - B_j h_(i,j+1). P, Q = residuals with block n set to zero.
Prints max_{i+j=n} |h_ij|^(1/(2n)) (inverse radius estimate) per block. Dense float arithmetic (mpmath optional)."""
import sys, numpy as np
from mpmath import mp, mpf
mp.dps = 50
def run(beta, a0, free, nmax, use_mp=True):
    a = beta + 2; b = beta - 2
    D = 2 * nmax + 3
    Z = (lambda: np.array([[mpf(0)] * (D + 1) for _ in range(D + 1)], dtype=object)) if use_mp else (lambda: np.zeros((D + 1, D + 1)))
    Ps = Z(); Th = Z()
    Ps[1, 1] = mpf(-2) if use_mp else -2.0; Th[0, 1] = mpf(a0) if use_mp else a0
    def dx(F):
        G = Z(); G[:-1, :] = F[1:, :] * np.arange(1, D + 1)[:, None]; return G
    def dy(F):
        G = Z(); G[:, :-1] = F[:, 1:] * np.arange(1, D + 1)[None, :]; return G
    def mul(F, G, maxdeg):
        H = Z()
        nzF = [(p, q) for p in range(D + 1) for q in range(D + 1 - p) if F[p, q] != 0]
        nzG = [(p, q) for p in range(D + 1) for q in range(D + 1 - p) if G[p, q] != 0]
        for (p, q) in nzF:
            fv = F[p, q]
            for (r, s) in nzG:
                if p + r + q + s <= maxdeg:
                    H[p + r, q + s] += fv * G[r, s]
        return H
    X = Z(); X[1, 0] = 1; Y = Z(); Y[0, 1] = 1
    out = []
    for n in range(1, nmax + 1):
        deg = 2 * n + 1
        # residuals with block n zero
        U1 = -dy(Ps); U2 = dx(Ps)
        W1 = U1.copy(); W1[1, 0] += beta; W2 = U2.copy(); W2[0, 1] += beta
        RT = mul(W1, dx(Th), deg) + mul(W2, dy(Th), deg) - b * Th
        Om = -(dx(dx(Ps)) + dy(dy(Ps)))
        RO = mul(W1, dx(Om), deg - 1) + mul(W2, dy(Om), deg - 1) + Om - dx(Th)
        Pc = {(i, n - i): RT[2 * i, 2 * (n - i) + 1] for i in range(n + 1)}
        Qc = {(i, n - 1 - i): RO[2 * i + 1, 2 * (n - 1 - i) + 1] for i in range(n)}
        h = {(n, 0): free(n)}
        L = lambda i, j: 2 * i * a + 2 * j * b
        for i in range(n - 1, -1, -1):
            j = n - 1 - i
            M = (2 * i + 1) * a + (2 * j + 1) * b + 1; A = (2 * i + 3) * (2 * i + 2); B = (2 * j + 3) * (2 * j + 2)
            t_next = -(a0 * (2 * i + 3) * h[(i + 1, j)] + Pc[(i + 1, j)]) / L(i + 1, j)
            # M (-A h_(i+1,j) - B h_(i,j+1)) - 2(i+1) t_(i+1,j) + Q = 0
            h[(i, j + 1)] = (-M * A * h[(i + 1, j)] - 2 * (i + 1) * t_next + Qc[(i, j)]) / (M * B)
        for i in range(n + 1):
            j = n - i
            Ps[2 * i + 1, 2 * j + 1] = h[(i, j)]
            Th[2 * i, 2 * j + 1] = -(a0 * (2 * i + 1) * h[(i, j)] + Pc[(i, j)]) / L(i, j)
        hm = max(abs(h[k]) for k in h); tm = max(abs(Th[2 * i, 2 * (n - i) + 1]) for i in range(n + 1))
        out.append((n, float(hm), float(tm)))
    # check residual of the final truncation
    return out, Ps, Th
if __name__ == '__main__':
    beta = float(sys.argv[1]); a0 = float(sys.argv[2]); nmax = int(sys.argv[3]); mode = sys.argv[4] if len(sys.argv) > 4 else 'h10'
    if mode == 'h10': free = lambda n: mpf(1) if n == 1 else mpf(0)
    elif mode == 'geo': free = lambda n: mpf(1)            # h_(n,0) = 1 for all n
    out, Ps, Th = run(mpf(beta), mpf(a0), free, nmax)
    for n, hm, tm in out:
        print(f"beta {beta} a0 {a0} {mode} n {n:3d} deg {2*n+2:3d} max|h| {hm:.4e} (^1/2n {hm**(1/(2*n)):.4f})  max|t| {tm:.4e} (^1/2n {tm**(1/(2*n)):.4f})", flush=True)
