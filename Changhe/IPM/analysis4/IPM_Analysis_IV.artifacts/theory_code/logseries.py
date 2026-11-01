"""Lead: logarithmic (polynomial-in-t, t = log r) far-field series at rational delta.

rho = sum_n r^{p_n} f_n(t, theta), psi = sum_n r^{P_n} g_n(t, theta), f_n, g_n polynomials in t.
Recursion (lead derivation; identical to the verifier's research note on logarithmic channels):
  [(n-1)(c-1) - c T] f_n = S_n,  S_n = sum_{i+j=n} [ -(D g_i)(p_j + T) f_j + ((P_i + T) g_i)(D f_j) ],
  [m^2 - (P_n + T)^2] g_{n,m} = rhs_m,  rhs = cos(th) (p_n + T) f_n - sin(th) D f_n,
with T = d/dt, D = d/dtheta, m the angular frequency. At an exact resonance m^2 = P_n^2 (P_n = -|m|):
  T (2|m| - T) g = rhs  ->  g = beta + int_0^t (2|m| - T)^{-1} rhs.
Representation: complex Fourier coefficients c[m] (function = sum c[m] e^{i m th}), array shape (2M+1, K+1),
axis 0 frequency -M..M, axis 1 power of t. Double precision (divisors are >= 1/B off resonance, no cancellation issue).
"""
import sys, json, time
import numpy as np
from fractions import Fraction
from scipy.signal import fftconvolve


def tder(h):
    """T = d/dt on the t-axis (axis 1)."""
    K = h.shape[1]
    out = np.zeros_like(h)
    if K > 1:
        out[:, :-1] = h[:, 1:] * np.arange(1, K)[None, :]
    return out


def tint(h):
    """int_0^t on the t-axis; grows the t-degree by one."""
    K = h.shape[1]
    out = np.zeros((h.shape[0], K + 1), dtype=h.dtype)
    out[:, 1:] = h / np.arange(1, K + 1)[None, :]
    return out


def pad(h, M, K):
    """embed h (frequency half-width h.shape[0]//2) into half-width M and t-length K."""
    m0 = h.shape[0] // 2
    out = np.zeros((2 * M + 1, K), dtype=complex)
    out[M - m0:M + m0 + 1, :h.shape[1]] = h
    return out


def trim(h, tol=0.0):
    """drop trailing zero t-columns and zero outer frequencies."""
    nz_t = np.nonzero(np.any(np.abs(h) > tol, axis=0))[0]
    K = (nz_t[-1] + 1) if len(nz_t) else 1
    h = h[:, :K]
    M = h.shape[0] // 2
    nz_m = np.nonzero(np.any(np.abs(h) > tol, axis=1))[0]
    if len(nz_m) == 0:
        return np.zeros((1, 1), dtype=complex)
    mm = max(abs(nz_m[0] - M), abs(nz_m[-1] - M))
    return h[M - mm:M + mm + 1, :]


def mulD(h):
    M = h.shape[0] // 2
    return h * (1j * np.arange(-M, M + 1))[:, None]


def conv(u, v):
    """product of two (frequency x t-power) arrays: exact angular convolution by FFT on a grid with no aliasing,
    done separately for each pair of t-powers (so rounding is relative to each column, not to the largest column)."""
    Mu, Mv = u.shape[0] // 2, v.shape[0] // 2
    M = Mu + Mv
    Q = 1
    while Q < 2 * M + 1:
        Q *= 2
    def to_grid(h, Mh):
        a = np.zeros((Q, h.shape[1]), dtype=complex)
        a[:Mh + 1, :] = h[Mh:, :]
        if Mh > 0:
            a[Q - Mh:, :] = h[:Mh, :]
        return np.fft.ifft(a, axis=0) * Q
    U, V = to_grid(u, Mu), to_grid(v, Mv)
    K = u.shape[1] + v.shape[1] - 1
    W = np.zeros((Q, K), dtype=complex)
    for k1 in range(u.shape[1]):
        W[:, k1:k1 + v.shape[1]] += U[:, k1:k1 + 1] * V
    w = np.fft.fft(W, axis=0) / Q
    out = np.zeros((2 * M + 1, K), dtype=complex)
    out[M:, :] = w[:M + 1, :]
    if M > 0:
        out[:M, :] = w[Q - M:, :]
    return out


def sym(h, parity):
    """enforce the S1 structure: parity 'sin' -> c(-m) = -c(m), c imaginary; 'cos' -> c(-m) = c(m), c real."""
    if parity == 'sin':
        h = (h - h[::-1, :]) / 2
        return 1j * h.imag
    h = (h + h[::-1, :]) / 2
    return h.real.astype(complex)


def run(A, Bd, f1, N, beta=None, out=None, chop=1e-300):
    """delta = A/Bd (Fractions ok); f1: dict odd frequency -> real sine amplitude."""
    dl = Fraction(A, Bd)
    c = 1 / (1 - dl)
    cf, dlf = float(c), float(dl)
    p = lambda n: 1 - n * dl
    M1 = max(f1)
    h = np.zeros((2 * M1 + 1, 1), dtype=complex)
    for m, a in f1.items():
        h[M1 + m, 0] += a / 2j
        h[M1 - m, 0] -= a / 2j
    F = {1: h}
    G = {}
    res_info = []

    def poisson(n):
        f = F[n]
        pn = p(n)
        Pn = pn + 1
        M = f.shape[0] // 2 + 1
        K = f.shape[1]
        fp = pad(f, M, K + 1)
        pf = float(pn) * fp + tder(fp)
        # cos(th) * X: shift +-1 with 1/2 ; sin(th) * X: (shift+1 - shift-1)/(2i)
        Df = mulD(fp)
        rhs = np.zeros_like(fp)
        rhs[1:, :] += pf[:-1, :] / 2
        rhs[:-1, :] += pf[1:, :] / 2
        rhs[1:, :] -= Df[:-1, :] / 2j
        rhs[:-1, :] += Df[1:, :] / 2j
        g = np.zeros((2 * M + 1, K + 2), dtype=complex)
        Pf = float(Pn)
        for idx in range(2 * M + 1):
            m = idx - M
            r = rhs[idx, :]
            if m == 0 or not np.any(r != 0):
                continue
            lam_exact = m * m - Pn * Pn
            if lam_exact != 0:
                lam = float(lam_exact)
                # [lam - 2 P T - T^2] x = r  ->  x = sum_h ((2PT + T^2)/lam)^h r / lam
                x = r / lam
                term = x.copy()
                for _ in range(K + 1):
                    t1 = np.zeros_like(term)
                    t1[:-1] = term[1:] * np.arange(1, len(term))
                    t2 = np.zeros_like(term)
                    t2[:-1] = t1[1:] * np.arange(1, len(term))
                    term = (2 * Pf * t1 + t2) / lam
                    if not np.any(term != 0):
                        break
                    x = x + term
                g[idx, :K + 1] = x
            else:
                if m == 0:
                    raise RuntimeError('m=0 resonance')
                am = abs(m)
                # T (2|m| - T) g = r : w = (2|m| - T)^{-1} r = sum_h (T/(2|m|))^h r / (2|m|)
                w = r / (2 * am)
                term = w.copy()
                for _ in range(K + 1):
                    t1 = np.zeros_like(term)
                    t1[:-1] = term[1:] * np.arange(1, len(term))
                    term = t1 / (2 * am)
                    if not np.any(term != 0):
                        break
                    w = w + term
                gi = np.zeros(K + 2, dtype=complex)
                gi[1:] = w / np.arange(1, K + 2)
                b0 = 0.0
                if beta is not None and m > 0:
                    b0 = beta.get((n, m), 0.0) / 2j
                    gi[0] = b0
                elif beta is not None and m < 0:
                    gi[0] = -beta.get((n, -m), 0.0) / 2j
                g[idx, :] = gi
                if m > 0:
                    res_info.append(dict(n=n, m=m, forcing_t0=float(abs(r[0])), forcing_norm=float(np.abs(r).sum())))
        return trim(sym(g, 'sin'))

    G[1] = poisson(1)
    stats = []
    t0 = time.time()
    for n in range(2, N + 1):
        acc = None
        for i in range(1, n):
            j = n - i
            gi, fj = G[i], F[j]
            Pi = float(p(i) + 1)
            pj = float(p(j))
            term = -conv(mulD(gi), pj * fj + tder(fj)) + conv(Pi * gi + tder(gi), mulD(fj))
            if acc is None:
                acc = term
            else:
                if term.shape[0] > acc.shape[0] or term.shape[1] > acc.shape[1]:
                    MM = max(term.shape[0], acc.shape[0]) // 2
                    KK = max(term.shape[1], acc.shape[1])
                    acc = pad(acc, MM, KK)
                    term = pad(term, MM, KK)
                elif term.shape != acc.shape:
                    term = pad(term, acc.shape[0] // 2, acc.shape[1])
                acc = acc + term
        lamd = (n - 1) * (cf - 1)
        x = acc / lamd
        term = x.copy()
        for _ in range(acc.shape[1] + 1):
            term = cf * tder(term) / lamd
            if not np.any(term != 0):
                break
            x = x + term
        F[n] = trim(sym(x, 'sin'))
        G[n] = poisson(n)
        f = F[n]
        colnorm = np.abs(f).sum(axis=0)  # l1 over frequency of each t-power coefficient
        st = dict(n=n, Kt=int(f.shape[1] - 1), maxfreq=int(f.shape[0] // 2),
                  col=[float(v) for v in colnorm],
                  gKt=int(G[n].shape[1] - 1))
        stats.append(st)
        if out:
            with open(out, 'a') as fh:
                fh.write(json.dumps(st) + '\n')
    return F, G, stats, res_info


if __name__ == '__main__':
    A, Bd, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    out = sys.argv[4] if len(sys.argv) > 4 else None
    if out:
        open(out, 'w').close()
    t0 = time.time()
    F, G, stats, res = run(A, Bd, {1: 1.0}, N, out=out)
    print('time', time.time() - t0)
    for st in stats:
        col = st['col']
        print(st['n'], st['Kt'], ' '.join('%.3e' % v for v in col))
    print('resonances', res[:10])
