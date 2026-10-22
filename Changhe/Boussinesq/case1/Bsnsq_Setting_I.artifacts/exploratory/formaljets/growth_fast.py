"""Float64 version of growth.py with 2D convolutions (same recursion: Proposition 17 coefficient equations run forwards).
Prints per block n: max|h| over the block and its (2n)-th root; also the ratio of successive maxima."""
import sys, numpy as np
from scipy.signal import convolve2d
def run(beta, a0, free, nmax):
    a = beta + 2; b = beta - 2; D = 2 * nmax + 4
    Ps = np.zeros((D, D)); Th = np.zeros((D, D)); Ps[1, 1] = -2.0; Th[0, 1] = a0
    ar = np.arange(D, dtype=float)
    dx = lambda F: np.vstack([F[1:, :] * ar[1:, None], np.zeros((1, D))])
    dy = lambda F: np.hstack([F[:, 1:] * ar[None, 1:], np.zeros((D, 1))])
    def mul(F, G):
        return convolve2d(F, G)[:D, :D]
    out = []
    for n in range(1, nmax + 1):
        U1 = -dy(Ps); U2 = dx(Ps)
        W1 = U1.copy(); W1[1, 0] += beta; W2 = U2.copy(); W2[0, 1] += beta
        RT = mul(W1, dx(Th)) + mul(W2, dy(Th)) - b * Th
        Om = -(dx(dx(Ps)) + dy(dy(Ps)))
        RO = mul(W1, dx(Om)) + mul(W2, dy(Om)) + Om - dx(Th)
        Pc = {(i, n - i): RT[2 * i, 2 * (n - i) + 1] for i in range(n + 1)}
        Qc = {(i, n - 1 - i): RO[2 * i + 1, 2 * (n - 1 - i) + 1] for i in range(n)}
        h = {(n, 0): free(n)}
        L = lambda i, j: 2 * i * a + 2 * j * b
        for i in range(n - 1, -1, -1):
            j = n - 1 - i
            M = (2 * i + 1) * a + (2 * j + 1) * b + 1; A = (2 * i + 3) * (2 * i + 2); B = (2 * j + 3) * (2 * j + 2)
            t_next = -(a0 * (2 * i + 3) * h[(i + 1, j)] + Pc[(i + 1, j)]) / L(i + 1, j)
            h[(i, j + 1)] = (-M * A * h[(i + 1, j)] - 2 * (i + 1) * t_next + Qc[(i, j)]) / (M * B)
        for i in range(n + 1):
            j = n - i
            Ps[2 * i + 1, 2 * j + 1] = h[(i, j)]
            Th[2 * i, 2 * j + 1] = -(a0 * (2 * i + 1) * h[(i, j)] + Pc[(i, j)]) / L(i, j)
        hm = max(abs(h[k]) for k in h); tm = max(abs(Th[2 * i, 2 * (n - i) + 1]) for i in range(n + 1))
        out.append((n, hm, tm))
    return out, Ps, Th
if __name__ == '__main__':
    beta = float(sys.argv[1]); a0 = float(sys.argv[2]); nmax = int(sys.argv[3]); mode = sys.argv[4]
    free = {'h10': (lambda n: 1.0 if n == 1 else 0.0), 'geo': (lambda n: 1.0)}[mode]
    out, Ps, Th = run(beta, a0, free, nmax)
    prev = None
    for n, hm, tm in out:
        r = '' if prev is None else f" ratio {hm/prev:.3e}"
        print(f"beta {beta} a0 {a0} {mode} n {n:3d} max|h| {hm:.4e} root {hm**(1/(2*n)):.4f}{r}  max|t| {tm:.4e} root {tm**(1/(2*n)):.4f}", flush=True)
        prev = hm
