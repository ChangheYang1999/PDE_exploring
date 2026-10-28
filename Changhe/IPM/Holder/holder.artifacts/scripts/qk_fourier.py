# Fourier coefficients in b of N(b): N(b) = Nbar + sum_k c_k Q_k cos(4 k b), c_k = (2/pi)(-1)^{k+1}/(4k^2-1),
# Q_k = int |F''| cos(2k arg F'') dA_w (p.v. at x,y), F''(w) = (1/pi) w/(w^2-1/4)^2.
# Computed in the s = w^2 - 1/4 plane: Q_k = (1/(2pi)) int_0^inf dsig/sig int_0^{2pi} e^{-4ik phi} q^k |q|^{-k-1/2} dphi,
# q = 1/4 + sig e^{i phi}. Heuristic floating-point quadrature.
import numpy as np
from scipy.integrate import quad
def inner(sig, k, n=4096):
    ph = 2*np.pi*(np.arange(n)+0.5)/n
    q = 0.25 + sig*np.exp(1j*ph)
    v = np.exp(-4j*k*ph)*q**k*np.abs(q)**(-k-0.5)
    return np.real(np.mean(v))*2*np.pi
def Qk(k):
    f = lambda s: inner(s, k)/s
    a = quad(f, 0, 0.25, limit=400, epsabs=1e-13)[0]
    b = quad(f, 0.25, 4.0, limit=400, epsabs=1e-13, points=[0.25])[0]
    c = quad(lambda t: inner(1/t, k)*t/(t*t), 1e-12, 0.25, limit=400, epsabs=1e-13)[0]  # sig=1/t, dsig/sig = -dt/t
    return (a+b+c)/(2*np.pi)
def Nbar_check():
    pass
if __name__ == "__main__":
    tot0 = 0; totp = 0
    for k in range(1, 9):
        Q = Qk(k); ck = (2/np.pi)*(-1)**(k+1)/(4*k*k-1)
        tot0 += ck*Q; totp += ck*Q*(-1)**k
        print(k, f"Q_k={Q:.10f}", f"c_k Q_k={ck*Q:.3e}", flush=True)
    print("N(0)-N(pi/4) from k<=8:", tot0-totp)
