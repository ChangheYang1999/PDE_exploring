# Smoothness of the frozen packet across the line s = 0 at height y0: v(s,y0) = -(1/pi^2) int_0^inf K(xi) sin(s xi) d xi,
#   K(xi) = int sin(y0 eta) phi(xi/eta^A) eta^(2b-A-2) (xi^2+eta^2)^(-b) d eta
#         = (1/A) xi^(1/A) int_1^2 sin(y0 (xi/t)^(1/A)) phi(t) eta^(2b-A-2) (xi^2+eta^2)^(-b) t^(-1/A-1) dt, eta = (xi/t)^(1/A).
# v is C^infinity in s near s = 0 iff K decays faster than any power. Pre-asymptotic power law: xi^(-1-(1+g)/A).
import sys, json, mpmath as mp
mp.mp.dps = 60
def phi(t): return mp.exp(-1/((t-1)*(2-t)))
def K(xi, A, g, y0):
    b = mp.mpf(g)/(2*(A-1)); A = mp.mpf(A); xi = mp.mpf(xi)
    def f(t):
        eta = (xi/t)**(1/A)
        return mp.sin(y0*eta)*phi(t)*eta**(2*b-A-2)*(xi**2+eta**2)**(-b)*t**(-1/A-1)
    L = y0*xi**(1/A)*(1-2**(-1/A))
    n = int(max(8, float(L)/2))
    return (1/A)*xi**(1/A)*mp.quad(f, mp.linspace(1, 2, n+1))
out = []
for (A, g, y0, ks) in [(3, 5.5, 1, range(0, 19)), (3, 5.5, 0.5, range(0, 19, 2)), (10.15, 29.75, 1, range(0, 61, 4))]:
    for k in ks:
        xi = mp.mpf(10)**k
        val = K(xi, A, g, y0)
        pl = val*xi**(1+mp.mpf(1+g)/A)
        L = y0*xi**(1/mp.mpf(A))*(1-2**(-1/mp.mpf(A)))
        out.append(dict(A=A, g=g, y0=y0, log10xi=k, K=float(val), K_times_powerlaw=float(pl), L=float(L)))
        print('A=%g g=%g y0=%g xi=1e%d  L=%.3g  K=%.6e  K*xi^(1+(1+g)/A)=%.6e' % (A, g, y0, k, float(L), float(val), float(pl)), flush=True)
json.dump(out, open('runs/frozen_kxi.json', 'w'), indent=1)
