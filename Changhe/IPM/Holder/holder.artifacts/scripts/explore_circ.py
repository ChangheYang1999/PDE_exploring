# Exploratory: F2(a,lam) = 2 W lam^a / a + \int_0^inf (1/2)(2R)^a N(R) dR, N(R) = \int_{|w|=R} |nu| ds (complex modulus version
# and sup over beta version). Uses zero circle mean of nu on circles centred at the midpoint.
import numpy as np
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(200)
def gl(a, b):
    return 0.5*(b-a)*xg + 0.5*(b+a), 0.5*(b-a)*wg
def k(z): return 1.0/(2*np.pi*np.conj(z)**2)
def nu(w, lam):
    x, y = 0.5, -0.5
    return np.where(np.abs(w-x) >= lam, k(x-w), 0) - np.where(np.abs(w-y) >= lam, k(y-w), 0)
def W(a): return 2**(1+a/2)/(np.pi*(2+a))
def Ncirc(R, lam, betas):
    bp = [0, np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]
    c = (R**2 + 0.25 - lam**2)/R
    if abs(c) < 1:
        pc = np.arccos(c); bp += [pc, 2*np.pi-pc, np.pi-pc, np.pi+pc]
    bp = sorted(set(bp))
    out = np.zeros(len(betas)+1); mean = 0
    for p0, p1 in zip(bp[:-1], bp[1:]):
        ph, wph = gl(p0, p1)
        v = nu(R*np.exp(1j*ph), lam)
        mean += R*np.sum(wph*v)
        out[-1] += R*np.sum(wph*np.abs(v))
        for ib, b in enumerate(betas):
            out[ib] += R*np.sum(wph*np.abs(np.real(np.exp(-2j*b)*v)))
    return out, mean
def F2(a, lam, betas, Rmax=50.0):
    Rb = sorted(set([1e-6, max(1e-6, 0.5-lam), abs(lam-0.5)+1e-9, 0.5, 0.5+lam, 1.0, 2.0, 5.0, 12.0, Rmax]))
    Rb = [r for r in Rb if r >= 1e-6]
    tot = np.zeros(len(betas)+1); maxmean = 0
    for r0, r1 in zip(Rb[:-1], Rb[1:]):
        R, wR = gl(r0, r1)
        for Rj, wj in zip(R, wR):
            n, mean = Ncirc(Rj, lam, betas)
            maxmean = max(maxmean, abs(mean))
            tot += wj*0.5*(2*Rj)**a*n
    # tail beyond Rmax: N(R) = 2R^2/(R^4-1/16) for complex modulus; use it as bound for all
    tail = 2**a*sum(16.0**(-n)*Rmax**(a-1-4*n)/(4*n+1-a) for n in range(5))
    tot += tail
    loc = 2*W(a)*lam**a/a
    return loc, tot, maxmean
if __name__ == "__main__":
    betas = np.linspace(0, np.pi/2, 5)
    for a in [0.02, 0.1, 0.25, 0.5, 0.75]:
        for lam in [0.3, 0.4, 0.5, 0.6, 0.7]:
            loc, tot, mm = F2(a, lam, betas)
            Fb = loc + tot[:-1].max(); Fc = loc + tot[-1]
            print(f"a={a} lam={lam} loc={loc:.4f} far(beta)={np.round(tot[:-1],4)} far(mod)={tot[-1]:.4f} F_beta-2/(pi a)={Fb-2/(np.pi*a):.4f} F_mod-2/(pi a)={Fc-2/(np.pi*a):.4f} maxmean={mm:.1e}", flush=True)
