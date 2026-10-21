# Request (o3) item 1: even imaginary Phi = i phi, phi even, phi = beta1 - beta2 on t > 0 (equal masses, int phi = 0),
# beta1 = bump on (1,2), beta2 = the same bump shifted to (2,3). Then
#   v(s,y) = -(1/pi^2) int_0^inf phi(t) int_0^inf eta^-2 (1+t^2 eta^q)^-b cos(s t eta^A) sin(y eta) d eta dt,  q = 2A-2,
#   G3(s) = (1/(6 pi^2)) int phi int eta (1+t^2 eta^q)^-b cos(s t eta^A) d eta dt.
# Predictions: G3(0) = (1/(6 pi^2 q)) B(2/q, (g-2)/q) int_0^inf phi t^(-2/(A-1)) dt  [lead/fred17 formula, j = 3],
#   G3(s) - G3(0) = Ke s^p* + ...,  Ke = (1/(6 pi^2 A)) Gamma(p) cos(pi p/2) int phi t^(-2b+p*) dt, p = (2-g)/A.
import sys, json, numpy as np, mpmath as mp
sys.path.insert(0, 'code/frozen')
from g3_axis import _panels, _GX, _GW
def bump(t, a):
    t = np.asarray(t, float); out = np.zeros_like(t); m = (t > a) & (t < a+1)
    out[m] = np.exp(-1/((t[m]-a)*(a+1-t[m]))); return out
x, w = np.polynomial.legendre.leggauss(200)
t1 = 0.5*x+1.5; t2 = 0.5*x+2.5; w = 0.5*w
tn = np.concatenate([t1, t2]); tw = np.concatenate([w, w]); ph = np.concatenate([bump(t1, 1), -bump(t2, 2)])

def alt_tail_cos(h, U1, n=48):
    # int_{U1}^inf h(u) cos u du for U1 = (m+1/2) pi
    k = np.arange(n); a = U1 + k*np.pi; bb = a+np.pi
    xx = (0.5*(bb-a))[:, None]*_GX[None, :] + (0.5*(bb+a))[:, None]; ww = (0.5*(bb-a))[:, None]*_GW[None, :]
    ak = np.sum(ww*h(xx.ravel()).reshape(xx.shape)*np.cos(xx), axis=1); bk = ak*(-1.0)**k
    d = (3+np.sqrt(8))**n; d = (d+1/d)/2; bc = -1.0; c = -d; s = 0.0
    for j in range(n):
        c = bc-c; s += c*bk[j]; bc = (j+n)*(j-n)*bc/((j+0.5)*(j+1))
    return s/d

def J_ct(c, t, A, g):
    # int_0^inf eta (1+t^2 eta^q)^-b (cos(c eta^A) - 1) d eta  in u = c eta^A
    b = g/(2*(A-1)); e = (2*A-2)/A; lc = np.log(c)
    def h(u):
        u = np.atleast_1d(np.asarray(u, float))
        return (1/A)*c**(-2/A)*u**(2/A-1)*np.exp(-b*np.log1p(np.exp(2*np.log(t)+e*(np.log(u)-lc))))
    lo = 1e-12*min(c, 1.0)
    e1 = list(np.geomspace(lo, 1.0, int(8*np.log10(1/lo))+2))
    U1 = 40.5*np.pi
    e2 = list(np.arange(1, 81)*(np.pi/2)) + [U1]
    edges = [0.0] + sorted(set(e1 + [c*f for f in (0.3, 1, 3) if lo < c*f < 1] + [z for z in e2 if 1.0 < z <= U1]))
    xx, ww = _panels(edges)
    u = xx; cm1 = np.where(u < 0.05, -u**2/2*(1-u**2/12*(1-u**2/30*(1-u**2/56))), np.cos(u)-1)
    tot = np.sum(ww*h(xx)*cm1) + alt_tail_cos(h, U1)
    from scipy import integrate
    tot -= integrate.quad(lambda uu: h(uu)[0], U1, np.inf, epsabs=0, epsrel=1e-13, limit=400)[0]
    return tot

out = []
for (A, g) in [(3.0, 3.5), (10.15, 29.75)]:
    b = g/(2*(A-1)); q = 2*A-2; ps = (g-2)/A; p = (2-g)/A
    B = float(mp.beta(2/q, (g-2)/q))
    G0_formula = B/(6*np.pi**2*q)*np.sum(tw*ph*tn**(-2/(A-1)))
    # direct G3(0): int eta (1+t^2 eta^q)^-b = (1/q) t^(-2/(A-1)) B(2/q, b-2/q) is the same Beta; check it by quadrature
    from scipy import integrate
    G0_quad = sum(wt*pt*integrate.quad(lambda e_: e_*(1+tt**2*e_**q)**(-b), 0, np.inf, epsabs=0, epsrel=1e-13, limit=400)[0]
                  for tt, wt, pt in zip(tn, tw, ph))/(6*np.pi**2)
    Ke = (1/(6*np.pi**2*A))*float(mp.gamma(p)*mp.cos(mp.pi*p/2))*np.sum(tw*ph*tn**(-2*b+ps))
    print('A=%g g=%g  G3(0) formula %.12e  quadrature %.12e   Ke pred %.10e  mass check int phi = %.1e' %
          (A, g, G0_formula, G0_quad, Ke, np.sum(tw*ph)), flush=True)
    rows = []
    for s in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        D = np.sum(tw*ph*np.array([J_ct(s*tt, tt, A, g) for tt in tn]))/(6*np.pi**2)
        rows.append(dict(s=s, G3=G0_formula+D, G3_minus_G0=D, ratio=D/s**ps))
        print('   s=%.0e  G3=%.12e  (G3-G3(0))/s^p* = %.10e' % (s, G0_formula+D, D/s**ps), flush=True)
    out.append(dict(A=A, g=g, G0_formula=G0_formula, G0_quad=G0_quad, Ke=Ke, rows=rows))
json.dump(out, open('runs/frozen_g3_even.json', 'w'), indent=1)
