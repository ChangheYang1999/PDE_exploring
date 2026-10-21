# Request (o2), part 2: L_g v = 0 at points (finite differences for D, Fourier quadrature for U2), smoothness on
# circles (spectrum of v(r cos th, r sin th)), and quasi-homogeneity at A = 3 (direct subtraction of the Taylor terms
# of quasi-degree < 1+g, coefficients by Beta integrals) against u_0 from the finite-part leading-symbol integral.
import sys, json, time, numpy as np, mpmath as mp
sys.path.insert(0, 'code/frozen')
import vpacket as V
from math import factorial

def taylor_coef(A, g, j, k):
    b = g/(2*(A-1)); m = A*j+k-2; q = (m+1)/(2*A-2)
    x, w = np.polynomial.legendre.leggauss(200); t = 0.5*x+1.5; w = 0.5*w
    ph = np.exp(-1/((t-1)*(2-t)))
    M = np.sum(w*ph*t**j*t**(-(m+1)/(A-1)))/(2*A-2)
    B = float(mp.gamma(q)*mp.gamma(b-q)/mp.gamma(b))
    return -(1/np.pi**2)*(-1)**((j+k)//2-1)/(factorial(j)*factorial(k))*M*B

def u0(A, g, s, y, Tterms):
    # -(1/pi^2) int phi t^-2b int_0^inf eta^(-2-g) [sin(s t eta^A) sin(y eta) - T] d eta dt  (finite part)
    b = g/(2*(A-1))
    x, w = np.polynomial.legendre.leggauss(16)
    tt, tw = V.comp_gl(np.linspace(1, 2, 401)); ph = np.exp(-1/((tt-1)*(2-tt)))*tt**(-2*b)*tw
    # eta in (0,1]: geometric panels, series-safe f - T
    e1 = np.concatenate([[0.0], np.geomspace(1e-6, 1, 120)])
    ex, ew = V.comp_gl(e1)
    St = s*tt[None, :]*ex[:, None]**A; Y = y*ex[:, None]
    def sinm(x, n):   # sin x minus its Taylor polynomial through degree n-2 (n odd = first kept degree), by series
        out = np.zeros_like(x); term = None
        for kk in range(n, n+60, 2):
            out = out + (-1)**((kk-1)//2)*x**kk/factorial(kk)
        return out
    if Tterms == 'g55':     # T = (st eta^A)(y eta - (y eta)^3/6)
        fT = sinm(St, 3)*np.sin(Y) + St*sinm(Y, 5)
    else:                   # resonant g = 5: only T = (st eta^A)(y eta); the s y^3 term is kept (log divergence cut at 1e-6)
        fT = sinm(St, 3)*np.sin(Y) + St*sinm(Y, 3)
    inner = np.sum((ew*ex**(-2-g))[:, None]*fT, axis=0)
    # eta > 1: plain f, cut where s eta^A > OMC
    ee = (V.OMC/abs(s))**(1/A)
    e2 = np.arange(1.0, ee+1e-12, 0.01); e2[-1] = ee
    ex2, ew2 = V.comp_gl(e2)
    f2 = np.sin(s*tt[None, :]*ex2[:, None]**A)*np.sin(y*ex2)[:, None]
    outer = np.sum((ew2*ex2**(-2-g))[:, None]*f2, axis=0)
    # minus int_1^inf eta^(-2-g) T
    if Tterms == 'g55':
        Tint = s*tt*(y/(g+1-(A+1)) - y**3/6/(g+1-(A+3)))
    else:
        Tint = s*tt*(y/(g+1-(A+1)))
    return float(-(1/np.pi**2)*np.sum(ph*(inner+outer-Tint)))

