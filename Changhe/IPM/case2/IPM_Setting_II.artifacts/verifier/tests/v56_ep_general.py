"""V56(c): check of the general far-field coefficient formula of specification M25(h) / referee result 17,
    e_p = -((p+1)/sin(pi p/2)) int_0^{pi/2} A_e cos((p+2) th) dth,   w_e(r) = (V_2(0, r) + V_2(0, -r))/2 ~ e_p r^p,
independently of the stationary solver. For rho = r^p A(th), the stream function psi = r^(p+1) Phi(th) of Delta psi = -d_x rho solves
Phi'' + (p+1)^2 Phi = -(p cos th A - sin th A') (2 pi periodic, Fourier division); U_2 = psi_x = r^p ((p+1) cos th Phi - sin th Phi'),
so w_e / r^p = (Phi'(-pi/2) - Phi'(pi/2))/2. The overall sign of the velocity law is calibrated on A = cos^2 th against the closed form
e_p(cos^2) = -2(p+1)/(p(p+2)(p+4)) (V54(iii)); then the formula is tested on other x-even data, with and without zeros at +-pi/2, and on
data with a y-odd part (which the formula says does not contribute). Usage: python3 tests/v56_ep_general.py"""
import numpy as np
from scipy.integrate import quad
N = 1 << 14
th = 2*np.pi*np.arange(N)/N - np.pi
n = np.fft.fftfreq(N, 1.0/N)
def we_ratio(A, p):
    a = A(th)
    ap = np.real(np.fft.ifft(1j*n*np.fft.fft(a)))
    f = -(p*np.cos(th)*a - np.sin(th)*ap)
    Ph = np.fft.fft(f)/((p + 1)**2 - n**2)
    def dPhi(t):
        return float(np.real(np.sum(1j*n*Ph*np.exp(1j*n*(t - th[0]))))/N)
    return 0.5*(dPhi(-np.pi/2) - dPhi(np.pi/2))
def formula(A, p):
    Ae = lambda t: 0.5*(A(t) + A(-t))
    return -((p + 1)/np.sin(np.pi*p/2))*quad(lambda t: Ae(t)*np.cos((p + 2)*t), 0, np.pi/2, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
P = (0.2, 0.35, 0.49568, 0.7)
cos2 = lambda t: np.cos(t)**2
sgn = {}
for p in P:
    num = we_ratio(cos2, p); cf = -2*(p + 1)/(p*(p + 2)*(p + 4))
    sgn[p] = np.sign(num/cf)
    print('calib p %.5f  w_e/r^p %+.10f  closed form %+.10f  ratio %+.10f' % (p, num, cf, num/cf))
s = np.sign(np.mean(list(sgn.values())))
assert all(v == s for v in sgn.values())
par = (0.239, -0.7141, -0.2097, 0.122, 0.107, -0.027)
def Fx(t):            # x-even basis: a_j sin(j th) for odd j, cos(j th) for even j, j = 1..6
    return sum(a*(np.sin(j*t) if j % 2 else np.cos(j*t)) for j, a in zip(range(1, 7), par))
tests = {'N6 datum cos^2 e^F': lambda t: np.cos(t)**2*np.exp(Fx(t)),
         'cos^2 e^(0.4 cos 2th)': lambda t: np.cos(t)**2*np.exp(0.4*np.cos(2*t)),
         'cos^2 e^(0.3 sin th) (y-odd F)': lambda t: np.cos(t)**2*np.exp(0.3*np.sin(t)),
         '1 + 0.5 cos 2th (no zeros)': lambda t: 1 + 0.5*np.cos(2*t),
         '|cos|^3 (C^2 zeros)': lambda t: np.abs(np.cos(t))**3,
         'cos^4 + 0.2 sin 3th (y-odd part)': lambda t: np.cos(t)**4 + 0.2*np.sin(3*t),
         'cos^2 (1 + 0.3 cos 4th)': lambda t: np.cos(t)**2*(1 + 0.3*np.cos(4*t))}
for name, A in tests.items():
    for p in P:
        num = s*we_ratio(A, p); fm = formula(A, p)
        print('%-34s p %.5f  spectral %+.10f  formula %+.10f  diff %.2e' % (name, p, num, fm, abs(num - fm)))
# boundary term for data without zeros at +-pi/2: spectral - formula against -A_e(pi/2)
for name, A in {'1': lambda t: np.ones_like(t), '1 + 0.3 sin th': lambda t: 1 + 0.3*np.sin(t),
                '0.2 + cos^2 e^(0.4 cos 2th)': lambda t: 0.2 + np.cos(t)**2*np.exp(0.4*np.cos(2*t))}.items():
    for p in (0.2, 0.49568):
        num = s*we_ratio(A, p); fm = formula(A, p); Ae90 = 0.5*(A(np.array(np.pi/2)) + A(np.array(-np.pi/2)))
        print('boundary %-28s p %.5f  spectral - formula %+.10f  -A_e(pi/2) %+.10f' % (name, p, num - fm, -float(Ae90)))
