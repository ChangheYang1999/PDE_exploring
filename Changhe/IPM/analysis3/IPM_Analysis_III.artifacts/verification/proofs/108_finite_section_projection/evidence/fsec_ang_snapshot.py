"""Angular algebra for the w_a jet realization (floating point; s2-num 05:00Z).
Modes: a function g = e^{3t} sum_N G_N sin((2N+1) theta) (N = 0..Nmax).  Weight w_a = |cos theta|^{-2a} e^{mu_a(log r)}, a = 17/4.
 - A_half(n): Gram of sin((2j+1) theta), j < n, against |cos theta|^{-1/2} on [0, 2 pi] (explicit Gamma-function formula, GR 3.631.9).
 - div_cos4(n): least-squares division by cos^4 theta: modes G (length n) = M4 @ Q (Q length n - 2); returns (M4, solver).
 - remainder/jet split of a mode vector: gamma = -(1/2) sum (-1)^N (2N+1)^2 G_N (axis second-order coefficient of the factor g/(x^2 y));
   axis vanishing check sum (-1)^N G_N; x^2 y = r^3 (sin theta + sin 3 theta)/4.
"""
import numpy as np
from math import gamma, pi, sqrt

def I_half(k):
    """int_0^{2pi} cos(k theta) |cos theta|^{-1/2} dtheta (k even; 0 for k odd)"""
    if k % 2: return 0.0
    k = abs(k); nu = 0.5
    # int_0^{pi/2} cos^{nu-1} cos(k th) = pi Gamma(nu) / (2^nu Gamma((nu+k+1)/2) Gamma((nu-k+1)/2)); Gamma at negative half-odd args via reflection
    from mpmath import mp, gamma as mg, mpf
    mp.dps = 30
    v = mp.pi * mg(mpf(nu)) / (mpf(2) ** nu * mg((mpf(nu) + k + 1) / 2) * mg((mpf(nu) - k + 1) / 2))
    return float(4 * v)

def A_half(n):
    A = np.zeros((n, n))
    for j in range(n):
        for jp in range(n):
            A[j, jp] = 0.5 * (I_half(2 * (j - jp)) - I_half(2 * (j + jp + 1)))
    return A

def mode_index(k):
    """sin(k theta) for odd k: (sign, N) with k = +/-(2N+1)"""
    if k > 0: return 1.0, (k - 1) // 2
    if k < 0: return -1.0, (-k - 1) // 2
    return 0.0, None

def mult_cos2k_matrix(n_out, n_in, k):
    """matrix of multiplication by cos(2k theta) from sin modes (n_in) to sin modes (n_out)"""
    M = np.zeros((n_out, n_in))
    for N in range(n_in):
        for s in (+1, -1):
            kk = 2 * N + 1 + s * 2 * k
            sg, idx = mode_index(kk)
            if idx is not None and idx < n_out: M[idx, N] += 0.5 * sg
    return M

def div_cos4(n):
    """M4: modes Q (n-2) -> G (n) for multiplication by cos^4 = (3 + 4 cos 2th + cos 4th)/8; solver(G) -> (Q, residual norm)"""
    nq = n - 2
    M4 = (3 * np.eye(n, nq) + 4 * mult_cos2k_matrix(n, nq, 1) + mult_cos2k_matrix(n, nq, 2)) / 8
    pinv = np.linalg.pinv(M4)
    def solve(G):
        Q = pinv @ G
        return Q, float(np.linalg.norm(M4 @ Q - G))
    return M4, solve

def jet_split(G):
    """G: mode vector (n). returns gamma (axis coefficient of the factor), the remainder modes G - gamma x^2y-modes, and the axis residual sum (-1)^N G_N"""
    N = np.arange(len(G))
    sgn = (-1.0) ** N
    axis0 = float(np.sum(sgn * G))
    gamma = -0.5 * float(np.sum(sgn * (2 * N + 1) ** 2 * G))
    R = G.copy(); R[0] -= gamma / 4; R[1] -= gamma / 4
    return gamma, R, axis0

def x2y_modes(n):
    v = np.zeros(n); v[0] = 0.25; v[1] = 0.25; return v

def factor_cos2m_modes(n, m):
    """modes of x^2 y cos(2m theta) / r^3 = cos^2 sin cos 2m: (sin th + sin 3th)/4 * cos 2m th"""
    M = mult_cos2k_matrix(n, n, m)
    return M @ x2y_modes(n)

if __name__ == "__main__":
    n = 12
    A = A_half(n); print("A_half diag", np.diag(A)[:4], "sym err", np.abs(A - A.T).max())
    # check I_half(0) = 4 * 2.622
    print("I_half(0)", I_half(0), "expected", 4 * 0.5 * gamma(0.25) * gamma(0.5) / gamma(0.75))
    M4, solve = div_cos4(n)
    # test: G = modes of cos^4 * sin(3 theta) -> Q = e_1
    Q0 = np.zeros(n - 2); Q0[1] = 1.0; G = M4 @ Q0; Q, res = solve(G); print("division test", np.abs(Q - Q0).max(), res)
    # remainder column m=1: x^2y cos 2th - (-1) x^2y = x^2y (cos 2th + 1) = 2 x^2 y cos^2 th: quotient by cos^4 -> 2 r^3 sin th: modes 2 e_0
    G1 = factor_cos2m_modes(n, 1) + x2y_modes(n); Q, res = solve(G1); print("remainder m=1 quotient modes", Q[:3], "res", res)
    g, R, a0 = jet_split(factor_cos2m_modes(n, 0)); print("jet of x2y: gamma", g, "axis0", a0, "R max", np.abs(R).max())
    # numeric check of A_half against quadrature for one entry
    th = np.linspace(0, 2 * np.pi, 400001)[:-1]; dth = th[1] - th[0]
    f = np.sin(th) * np.sin(3 * th) * np.abs(np.cos(th)) ** -0.5
    f[~np.isfinite(f)] = 0
    print("A[0,1] quad", np.sum(f) * dth, "formula", A[0, 1])
