import numpy as np, sys
sys.path.insert(0, 'explore')
import p0_forward as P
from scipy.interpolate import RectBivariateSpline
def rhof(X, Y):
    return (X**2 + 0.7*X*Y - 0.4*Y**2 + 0.9*X**2*Y + 0.5*Y**3 - 0.3*X**3) * np.exp(-((X-0.3)**2 + (Y+0.2)**2)/2)
L = 40.; N = 1024
x = (np.arange(N) - N//2) * (L/N); XX, YY = np.meshgrid(x, x, indexing='ij')
Rh = np.fft.fft2(rhof(XX, YY))
k = 2*np.pi*np.fft.fftfreq(N, L/N); KX, KY = np.meshgrid(k, k, indexing='ij'); K2 = KX**2 + KY**2; K2[0, 0] = 1
psih = 1j*KX*Rh/K2; psih[0, 0] = 0
U1 = np.real(np.fft.ifft2(-1j*KY*psih)); U2 = np.real(np.fft.ifft2(1j*KX*psih))
s1 = RectBivariateSpline(x, x, U1); s2 = RectBivariateSpline(x, x, U2)
u10, u20 = s1(0, 0)[0, 0], s2(0, 0)[0, 0]
for Nr, Nth in [(241, 64), (481, 128)]:
    rho, th = P.make_grid(Nr, Nth, -6.0, 3.0)
    r = np.exp(rho)
    X = r[:, None]*np.cos(th)[None, :]; Y = r[:, None]*np.sin(th)[None, :]
    wr, wt = P.velocity(rhof(X, Y), rho, th)
    w1 = wr*np.cos(th) - wt*np.sin(th); w2 = wr*np.sin(th) + wt*np.cos(th)
    err = 0
    for (i, j) in [(Nr//2, 3), (Nr//2 + 40, Nth//3), (Nr - 60, Nth//2 + 5), (Nr//3, 7*Nth//8)]:
        e1 = s1(X[i, j], Y[i, j])[0, 0] - u10; e2 = s2(X[i, j], Y[i, j])[0, 0] - u20
        err = max(err, abs(w1[i, j] - e1), abs(w2[i, j] - e2))
        print(Nr, Nth, 'r=%.3g' % r[i], w1[i, j], e1, w2[i, j], e2)
    print('maxerr', err)
# strain test: x^2(1+a y)^2 e^{-r^2}, c = a/4
a = 0.7
for Nr, Nth in [(241, 64), (481, 128)]:
    rho, th = P.make_grid(Nr, Nth, -8.0, 3.0)
    r = np.exp(rho)
    X = r[:, None]*np.cos(th)[None, :]; Y = r[:, None]*np.sin(th)[None, :]
    wr, wt = P.velocity(X**2*(1+a*Y)**2*np.exp(-r[:, None]**2), rho, th)
    w2 = wr*np.sin(th) + wt*np.cos(th)
    k = 5
    # d_y w_2 at 0 from th = pi/2 ray
    j = Nth//4
    print('c est', w2[k, j]/r[k], 'exact', a/4)
