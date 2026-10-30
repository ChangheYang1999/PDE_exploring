"""c1-t1 R1-026: FLOAT physical-space check of T4-206, ||w D^k U[h]||_2 <= sqrt(1 + 2/(k+1)) ||w D^k h||_2.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4206.py > check_T4206.out

The review (nonlinear_closure/REVIEWS_v22.md) is analytic; this is an illustration, not part of the proof. It does
not use the Fourier moment identity (4) of T4-206: U[h] = (-R1 R2 h, R1^2 h) (symbol (xi1 xi2, -xi1^2)/|xi|^2) and
the derivative tensors are computed by FFT on a periodic grid [-L, L)^2, N^2 points, and the weighted norms are
Riemann sums in physical space. Reported per test function and k = 0, 1, 2: the worst weighted ratio
q_k = || |X| D^k U[h] ||^2 / || |X| D^k h ||^2 (the R -> 0 limit of the weighted ratio) and
||w D^k U||^2/||w D^k h||^2 at R = 1, against the T4-206 bound 1 + 2/(k+1) and, for centrally even h, the stated
non-odd bound 1 + 2/k (k >= 1). Grid errors are estimated by repeating at (N, L) = (1024, 48) and (2048, 96).
"""
import itertools
import numpy as np


def run(N, L):
    x = (np.arange(N) - N // 2) * (2 * L / N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    k1 = 2 * np.pi * np.fft.fftfreq(N, d=2 * L / N)
    K1, K2 = np.meshgrid(k1, k1, indexing="ij")
    KK = K1**2 + K2**2
    KK[0, 0] = 1.0
    s1, s2 = K1 * K2 / KK, -K1**2 / KK
    s1[0, 0] = s2[0, 0] = 0.0
    r2 = X**2 + Y**2
    tests = {
        "y exp(-r^2)": Y * np.exp(-r2),
        "x exp(-r^2) (odd, not S1)": X * np.exp(-r2),
        "y exp(-x^2/9 - y^2)": Y * np.exp(-X**2 / 9 - Y**2),
        "Im (x+iy)^3 exp(-r^2/2)": (3 * X**2 * Y - Y**3) * np.exp(-r2 / 2),
        "y (1 - x^2) exp(-r^2/4) + x^2 y exp(-4 r^2)": Y * (1 - X**2) * np.exp(-r2 / 4) + X**2 * Y * np.exp(-4 * r2),
        "x y exp(-r^2) (centrally EVEN)": X * Y * np.exp(-r2),
    }
    dA = (2 * L / N) ** 2
    out = {}
    for name, h in tests.items():
        hh = np.fft.fft2(h)
        fields = {"h": [hh], "U": [s1 * hh, s2 * hh]}
        for k in range(3):
            res = {}
            for lab, comps in fields.items():
                tot_w0 = tot_x = 0.0
                for F in comps:
                    for idx in itertools.product((0, 1), repeat=k):
                        G = F.copy()
                        for i in idx:
                            G = G * (1j * (K1 if i == 0 else K2))
                        g = np.real(np.fft.ifft2(G))
                        tot_w0 += np.sum(g * g) * dA
                        tot_x += np.sum(r2 * g * g) * dA
                res[lab] = (tot_w0, tot_x)
            q = res["U"][1] / res["h"][1]
            q1 = (res["U"][0] + res["U"][1]) / (res["h"][0] + res["h"][1])
            out[(name, k)] = (q, q1)
    return out


A = run(1024, 48.0)
B = run(2048, 96.0)
worst = {}
for (name, k), (q, q1) in A.items():
    qb, q1b = B[(name, k)]
    even = "EVEN" in name
    if even and k == 0:
        print(f"{name:45s} k = 0: q_0 = {qb:.6f} (no bound asserted for k = 0 without oddness)")
        continue
    bound = (1 + 2 / k) if even else (1 + 2 / (k + 1))
    print(f"{name:45s} k = {k}: q_k = {qb:.6f} (grid change {abs(q - qb):.1e}), R = 1 ratio {q1b:.6f};"
          f" bound {'1 + 2/k' if even else '1 + 2/(k+1)'} = {bound:.6f}")
    assert qb < bound and q1b < bound
    worst[k] = max(worst.get(k, 0), qb / bound)
print("largest q_k / bound over the test functions:", {k: round(v, 4) for k, v in sorted(worst.items())})
