# K'_0 sign test on the x-axis (model study, w only).
# z = exp((beta+2) s) in (0,inf) along the axis orbit from P (z=0) to O (z=inf); v = beta+2 - w' = 2(beta+2) R(z).
# K'_0 = 0 iff F = f.p. int_0^inf R(z) z^{-a-1} e^{V(z)} dz = 0, a = 3/(beta+2), V(z) = 2 int_1^z R(t)/t dt.
import numpy as np
from scipy.integrate import quad
def F_of(R, beta):
    a = 3.0/(beta+2)
    V = lambda z: 2*quad(lambda t: R(t)/t, 1, z, limit=200)[0]
    Vinf = 2*quad(lambda t: (R(t)-1)/t, 1, np.inf, limit=200)[0]   # V(z) - 2 log z -> Vinf
    I1 = quad(lambda z: R(z)*z**(-a-1)*np.exp(V(z)), 0, 1, limit=200)[0]
    I2 = quad(lambda z: R(z)*z**(-a-1)*np.exp(V(z)) - np.exp(Vinf)*z**(1-a), 1, np.inf, limit=200)[0]
    return I1 + I2 - np.exp(Vinf)/(2-a), np.exp(Vinf)/(2-a)
models = {
 'z/sqrt(1+z^2)': lambda z: z/np.sqrt(1+z*z),
 'z^2/(1+z^2)':   lambda z: z*z/(1+z*z),
 'z^4/(1+z^4)':   lambda z: z**4/(1+z**4),
 'overshoot 1':   lambda z: z*z*(1+3*z*z)/(1+z*z)**2 * (1+0.0),
}
for beta in [2.0, 3.0, 6.0, 20.0]:
    for name, R in models.items():
        F, sub = F_of(R, beta)
        print(f"beta={beta:5.1f} {name:16s} F={F:+.5e}  (subtracted {sub:.4e}) F/sub={F/sub:+.4f}")
