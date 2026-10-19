"""Sign test of the quadratic form Q3(rho) = int rho U[rho].grad(sin 3theta / r^3) dX on decaying test densities
(even in x, odd in y, positive in the open first quadrant, rho ~ x^2 y at 0). For profiles R8 gives
Q3 = pi (c_l - 1)(3 c_l - 1), so a NO argument via R8 would need Q3 <= 0 on profiles. FFT on a periodic box."""
import numpy as np, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
Lb = 40.0
x = (np.arange(N) - N // 2) * (2 * Lb / N)
X, Y = np.meshgrid(x, x, indexing='ij')
k = np.fft.fftfreq(N, d=2 * Lb / N) * 2 * np.pi
K1, K2 = np.meshgrid(k, k, indexing='ij')
KK = K1 ** 2 + K2 ** 2; KK[0, 0] = 1.0
R2 = X ** 2 + Y ** 2; R = np.sqrt(R2); R[R == 0] = 1.0
TH = np.arctan2(Y, X)
dA = (2 * Lb / N) ** 2

def forms(rho):
    rh = np.fft.fft2(rho)
    U1 = np.real(np.fft.ifft2(K1 * K2 / KK * rh))
    U2 = np.real(np.fft.ifft2(-K1 ** 2 / KK * rh))
    w = 3 / R ** 4
    q3 = np.sum(rho * w * (-np.sin(4 * TH) * U1 + np.cos(4 * TH) * U2)) * dA
    c = np.sum(rho * np.sin(3 * TH) / R ** 3) * dA / np.pi
    # c from the velocity: c = -d_x U1(0)
    i0 = N // 2; h = 2 * Lb / N
    c_vel = -(U1[i0 + 1, i0] - U1[i0 - 1, i0]) / (2 * h)
    return q3, c, c_vel

rng = np.random.default_rng(0)
print(f"N={N}, box [-{Lb},{Lb}]^2")
for sx, sy in [(1, 1), (2, 1), (4, 1), (1, 2), (1, 4), (3, 0.5), (0.5, 3)]:
    rho = X ** 2 * Y * np.exp(-(X / sx) ** 2 - (Y / sy) ** 2)
    q3, c, cv = forms(rho)
    print(f"gauss sx={sx} sy={sy}: Q3={q3:+.5e}  c={c:+.5e} (vel {cv:+.5e})  Q3/c^2={q3/c**2:+.4f}")
# two-bump: x^2 y core plus a positive far blob near the x-axis (raises c) or near the y-axis
for (bx, by, amp) in [(5, 1, 1.0), (5, 1, 10.0), (1, 5, 1.0), (1, 5, 10.0), (4, 4, 5.0)]:
    core = X ** 2 * Y * np.exp(-R2)
    blob = amp * (np.exp(-((np.abs(X) - bx) ** 2 + (Y - by) ** 2)) - np.exp(-((np.abs(X) - bx) ** 2 + (Y + by) ** 2)))
    rho = core + blob * np.tanh(X ** 2) * np.tanh(Y ** 2 * 4) * np.sign(Y) ** 2
    rho = core + amp * (np.exp(-((np.abs(X) - bx) ** 2 + (Y - by) ** 2)) - np.exp(-((np.abs(X) - bx) ** 2 + (Y + by) ** 2))) * (1 - np.exp(-X ** 2 * 4))
    q3, c, cv = forms(rho)
    print(f"core+blob at ({bx},{by}) amp {amp}: min rho in Q {rho[(X>0)&(Y>0)].min():+.2e}  Q3={q3:+.5e}  c={c:+.5e} (vel {cv:+.5e})")
