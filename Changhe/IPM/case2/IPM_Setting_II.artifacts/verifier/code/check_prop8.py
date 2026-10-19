"""Numerical check of lead structure_v1.1 Proposition 8 (Fourier pairing), identity part valid for any smooth
x-even decaying density:  int h w' dy = -(1/pi) int_0^inf int_0^inf k^2 e^{-kx} Im(rho^(x,k) conj h^(k)) dk dx,
h(y) = rho_xx(0, y), w'(y) = psi_xy(0, y), -Lap psi = d_x rho.
LHS: psi_xy from a 2D FFT on a large periodic box (multiplier -i kx^2 ky/|k|^2, independent of the kernel K_x).
RHS: 1D FFT in y of rho(x, .) and h, quadrature in k and x. Also the physical-space form int_{x>0} rho d_x H."""
import numpy as np
def dens(x, y, a, y0, b2):
    return x**2*((1 + a*y)**2*np.exp(-(x**2 + (y - y0)**2)) + b2*np.exp(-(0.5*x**2 + 2*(y + 1)**2)))
def h_of(y, a, y0, b2):          # rho_xx(0, y)
    return 2*((1 + a*y)**2*np.exp(-(y - y0)**2) + b2*np.exp(-2*(y + 1)**2))
for (a, y0, b2) in [(0.8, 0.3, 0.0), (0.5, -0.4, 0.7), (1.5, 0.0, 0.3), (0.0, 0.0, 0.0)]:
    # LHS by 2D FFT
    Lb, N = 80.0, 1024
    xs = (np.arange(N) - N//2)*(Lb/N); X, Y = np.meshgrid(xs, xs, indexing='ij')
    rho = dens(X, Y, a, y0, b2)
    k = 2*np.pi*np.fft.fftfreq(N, d=Lb/N); KX, KY = np.meshgrid(k, k, indexing='ij'); K2 = KX**2 + KY**2; K2[0, 0] = 1
    pxy = np.real(np.fft.ifft2(-1j*KX**2*KY/K2*np.fft.fft2(rho)))
    i0 = N//2
    wp = pxy[i0, :]; hy = h_of(xs, a, y0, b2)
    lhs = np.sum(hy*wp)*(Lb/N)
    # RHS by 1D FFT in y, quadrature in x (Gauss-Legendre on [0, 12]) and k (FFT grid, k > 0, trapezoid)
    Ly, M = 200.0, 8192
    ys = (np.arange(M) - M//2)*(Ly/M)
    kk = 2*np.pi*np.fft.fftfreq(M, d=Ly/M)
    ph = np.exp(-1j*kk*ys[0])*(Ly/M)                     # continuous FT int e^{-iky} f(y) dy on the grid
    hh = np.fft.fft(h_of(ys, a, y0, b2))*ph
    xg, wg = np.polynomial.legendre.leggauss(200); xg = 6*(xg + 1); wg = 6*wg
    pos = kk > 0
    rhs = 0.0
    for x, w in zip(xg, wg):
        rh = np.fft.fft(dens(x, ys, a, y0, b2))*ph
        f = kk[pos]**2*np.exp(-kk[pos]*x)*np.imag(rh[pos]*np.conj(hh[pos]))
        rhs += w*np.sum(f)*(kk[1] - kk[0])
    rhs *= -1/np.pi
    print(f'a={a} y0={y0} b2={b2}: LHS int h w\' = {lhs:.10f}   RHS Fourier = {rhs:.10f}   diff {lhs - rhs:.2e}')
