# Exploratory (non-rigorous) evaluation of the crude bound F1(alpha,lambda) = 2 W lambda^a/a + sup_beta \int |nu_beta| |w|^a
import numpy as np
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(120)
def gl(a, b):
    return 0.5*(b-a)*xg + 0.5*(b+a), 0.5*(b-a)*wg
def k(z):  # complex kernel 1/(2 pi conj(z)^2)
    return 1.0/(2*np.pi*np.conj(z)**2)
def nu(w, lam):
    x, y = 0.5, -0.5
    ax = np.abs(w-x) >= lam; ay = np.abs(w-y) >= lam
    return np.where(ax, k(x-w), 0) - np.where(ay, k(y-w), 0)
def W(a): return 2**(1+a/2)/(np.pi*(2+a))
def far_integral(a, lam, betas):
    # returns array over beta of \int |Re(e^{-2i beta} nu)| |w|^a dw
    Rbreaks = sorted(set([1e-9, max(1e-9, 0.5-lam), 0.5+lam, 1.0, 2.0, 4.0, 8.0]))
    tot = np.zeros(len(betas))
    for i in range(len(Rbreaks)-1):
        R, wR = gl(Rbreaks[i], Rbreaks[i+1])
        for Rj, wRj in zip(R, wR):
            # angular breakpoints
            bp = [0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]
            c = (Rj**2 + 0.25 - lam**2)/Rj
            if abs(c) < 1:
                pc = np.arccos(c); bp += [pc, 2*np.pi-pc, np.pi-pc, np.pi+pc]
            bp = sorted(set(bp))
            for p0, p1 in zip(bp[:-1], bp[1:]):
                ph, wph = gl(p0, p1)
                w = Rj*np.exp(1j*ph)
                v = nu(w, lam)
                for ib, b in enumerate(betas):
                    tot[ib] += wRj*Rj*np.sum(wph*np.abs(np.real(np.exp(-2j*b)*v)))*Rj**a
    # tail R > 8: |nu| ~ |w|/(pi |w|^4) ; bound with complex modulus, crude
    tail = (1/np.pi)*2*np.pi*8**(a-2)/(2-a)  # \int_8^inf R^{a-3} * 2 R dR ... rough upper estimate
    return tot + tail
if __name__ == "__main__":
    betas = np.linspace(0, np.pi/2, 7)
    for a in [0.05, 0.1, 0.25, 0.5, 0.75, 0.9]:
        best = None
        for lam in [0.2, 0.3, 0.4, 0.5]:
            E = far_integral(a, lam, betas)
            F = 2*W(a)*lam**a/a + E.max()
            print(f"a={a} lam={lam} E(beta)={np.round(E,3)} F={F:.4f} 2/(pi a)={2/(np.pi*a):.4f} F-2/(pi a)={F-2/(np.pi*a):.4f}", flush=True)
