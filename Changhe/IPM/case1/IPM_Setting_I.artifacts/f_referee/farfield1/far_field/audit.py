"""Single-threaded read-only source audit; outputs only inside this workspace."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_AS, (1900 * 1024**2, 1900 * 1024**2))
import sys
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.chebyshev import chebval, chebder
sys.path.insert(0, "c7")
from trial import Trial

PATH = "c6g_shape.npz"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 32768
t = Trial(PATH)
k, L, cl = t.k, t.L, 1 / t.k
theta = np.arange(N) * (2 * np.pi / N)
c, s = np.cos(theta), np.sin(theta)
ac, sg = np.abs(c), np.sign(c)
v = ac**(t.p3-2) * s*s
vp = 2*ac**(t.p3-1)*sg*s-(t.p3-2)*ac**(t.p3-3)*sg*s**3
m = np.arange(t.angular+1)
E = np.zeros(N); Ep = E.copy(); B = E.copy(); Bp = E.copy(); D = E.copy()
Dp = E.copy(); J = E.copy()
h0 = np.full(N, (k-3)/2)
for j in range(t.angular+1):
    cj, sj = np.cos(2*j*theta), np.sin(2*j*theta)
    b0, b1, b2, b3 = (float(t.spline(1., nu=d)[j]) for d in range(4))
    E += b0*cj; Ep -= 2*j*b0*sj
    B += b1*cj; Bp -= 2*j*b1*sj; D += b2*cj
    Dp -= 2*j*b2*sj; J += b3*cj
    h0 -= t.origin**2*max(j-1,0)*b0*cj
T = [float(chebval(1., chebder(t.singular, d))) for d in range(4)]
E += T[0]*v; Ep += T[0]*vp
B += 2*T[1]*v; Bp += 2*T[1]*vp; D += 4*T[2]*v
Dp += 4*T[2]*vp; J += 8*T[3]*v
h0 -= t.p3/2*T[0]*v
pre = L**(3-k)*np.exp(E)
A = pre*c*c*s
Ap = pre*(c**3-2*c*s*s+c*c*s*Ep)
a = -L**(1-k)*B; ap = -L**(1-k)*Bp
b = L**(2-2*k)*(D+B*B)/2
bp = L**(2-2*k)*(Dp+2*B*Bp)/2
d = -L**(3-3*k)*(J+3*B*D+B**3)/6
h = L*L*h0

def inverse(alpha, aa, aa_prime):
    g = alpha*c*aa-s*aa_prime
    gh = np.fft.rfft(g)/N
    j = np.arange(len(gh))
    fh = np.zeros_like(gh)
    fh[2::2] = -1j*(-gh[2::2].imag)/(j[2::2]**2-(alpha+1)**2)
    f = np.fft.irfft(fh*N, n=N)
    fp = np.fft.irfft(1j*j*fh*N, n=N)
    return f, fp

F, Fp = inverse(k, A, Ap)
F1, F1p = inverse(2*k-1, A*a, Ap*a+A*ap)
F2, F2p = inverse(3*k-2, A*b, Ap*b+A*bp)
axes = np.arange(0, N, N//4)
good = np.ones(N, bool); good[axes] = False

def log_product(f, fp):
    out = np.empty(N)
    out[good] = f[good]*(c[good]/s[good]-2*s[good]/c[good]+Ep[good])
    out[axes[::2]] = fp[axes[::2]]
    out[axes[1::2]] = 2*fp[axes[1::2]]
    return out

Fe = log_product(F, Fp)
F1e = log_product(F1, F1p)
F2e = log_product(F2, F2p)
e = ((k+1)*Fe-k*Fp)/(cl-1)
C = (cl-1)*(e-a)
C2 = 2*(1-cl)*b-(2*k-1)*Fp*a+(k+1)*(Fe*a+F*ap)-k*F1p+2*k*F1e
D1 = C2-2*(1-cl)*b
D2 = (-(3*k-2)*Fp*b+(k+1)*(Fe*b+F*bp)
      -(2*k-1)*F1p*a+2*k*(F1e*a+F1*ap)-k*F2p+(3*k-1)*F2e)
C3 = 3*(1-cl)*d+D2
D0 = (cl-1)*e
n1 = 2*k*a+np.abs(D0)
n2 = (3*k-1)*b+np.sign(D0)*D1
coef = C/(1+k)
coef2 = C2/(1+k)-C*n1/(1+k)**2
coef3 = C3/(1+k)-C2*n1/(1+k)**2+C*(n1*n1/(1+k)**3-n2/(1+k)**2)
geom = -2*cl*h/(1+k)

qh = np.fft.rfft(e)/N
vh = np.fft.rfft(v)/N
cut = 2*t.angular
tail = np.arange(cut+2, min(N//2, 4000)+1, 2)
singcoef = np.real(np.vdot(vh[tail], qh[tail]))/np.real(np.vdot(vh[tail], vh[tail]))
fit = singcoef*v
keep = (qh-singcoef*vh).copy()
keep[cut+1:] = 0
fit += np.fft.irfft(keep*N, n=N)
plain = qh.copy(); plain[cut+1:] = 0
plain_fit = np.fft.irfft(plain*N, n=N)
qsel = (theta >= 0) & (theta <= np.pi/2)
sel = (theta > .001) & (theta < np.pi/2-.001)
bulk = (theta > .05) & (theta < 1.4)
axisband = (theta > 1.4) & (theta <= np.pi/2)
err = np.abs(e-a)
def interp(arr, th):
    return float(np.interp(th, theta[:N//4+1], arr[:N//4+1]))

out = dict(N=N, k=k, L=L, cl=cl, T=T,
           last_knot=float(np.unique(t.knots)[-2]),
           max_error=float(err[sel].max()),
           max_at=float(theta[sel][err[sel].argmax()]),
           max_bulk=float(err[bulk].max()),
           axis_error=float((e-a)[N//4]),
           axis_e=float(e[N//4]), axis_f=float(a[N//4]),
           C_1565=interp(C, 1.565),
           projection=dict(singular_coefficient=float(singcoef),
               global_error=float(np.abs(e-fit)[qsel].max()),
               axisband_error=float(np.abs(e-fit)[axisband].max()),
               plain_global_error=float(np.abs(e-plain_fit)[qsel].max()),
               plain_axisband_error=float(np.abs(e-plain_fit)[axisband].max())))
out["columns"] = {}
for th in [0, .818, 1.565, 1.5681, np.pi/2]:
    cols = dict(e=interp(e,th), a=interp(a,th), b=interp(b,th), d=interp(d,th), h=interp(h,th),
                A=interp(A,th), leading_coefficient=interp(coef,th),
                second_coefficient=interp(coef2,th), third_coefficient=interp(coef3,th),
                geometric_coefficient=interp(geom,th))
    rows = []
    for u in [1000,2000,4701,7998,9503,1e4,1e5,1e6]:
        r = u*L; delta = r**(k-1)
        terms = [cols["leading_coefficient"]*delta,
                 cols["second_coefficient"]*delta**2,
                 cols["geometric_coefficient"]/r**2,
                 cols["third_coefficient"]*delta**3]
        rows.append(dict(r_over_L=u, terms=terms, sum=sum(terms)))
    cols["rows"] = rows
    out["columns"][str(th)] = cols
Path(__file__).with_name(f"results_{N}.json").write_text(json.dumps(out, indent=2))
np.savez(Path(__file__).with_name(f"endpoint_{N}.npz"),
         theta=theta, A=A, Ap=Ap, a=a, ap=ap, b=b, h=h,
         F=F, Fp=Fp, F1=F1, F1p=F1p, e=e, fit=fit, coef=coef, coef2=coef2, geom=geom)
print(json.dumps(out, indent=2))
