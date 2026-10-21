# Verifier check of request (o2), part 1: the y^3 axis coefficient of the frozen packet
#   v(s,y) = -(1/pi^2) int_1^2 phi(t) int_0^inf eta^-2 (1+t^2 eta^(2A-2))^-b sin(s t eta^A) sin(y eta) d eta dt,
#   phi(t) = exp(-1/((t-1)(2-t))), Phi odd extension, b = g/(2(A-1)).
# G3(s) = (1/(6 pi^2)) int phi(t) I(st,t) dt,  I(c,t) = int_0^inf eta (1+t^2 eta^(2A-2))^-b sin(c eta^A) d eta.
# Route: u = c eta^A, oscillatory tail by QUADPACK QAWF; subtraction of c eta^A when g > A+2.
# Predictions: G3 = c1 s + K s^p* + ..., p* = (g-2)/A,
#   K  = (1/(6 pi^2 A)) Gamma(p) sin(pi p/2) int phi t^(-2b+p*) dt, p = (2-g)/A,
#   c1 = (1/(6 pi^2)) int phi t (1/(2A-2)) t^(-(A+2)/(A-1)) B(q, b-q), q = (A+2)/(2A-2) (analytic continuation),
#   resonant g = A+2: G3 = Klog s log(1/s) + O(s), Klog = (1/(6 pi^2 A)) int phi t^(1-2b) dt.
import sys, json, numpy as np
from scipy import integrate, special
import mpmath as mp

def phi(t):
    return np.exp(-1.0/((t-1.0)*(2.0-t)))

def gl(n, a=1.0, b=2.0):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b-a)*x+0.5*(b+a), 0.5*(b-a)*w

def sin_minus_u(u):
    u = np.atleast_1d(np.asarray(u, float))
    out = np.sin(u) - u
    sm = np.abs(u) < 0.05
    us = u[sm]; u2 = us*us
    out[sm] = -us**3/6*(1 - u2/20*(1 - u2/42*(1 - u2/72*(1 - u2/110))))
    return out

_GX, _GW = np.polynomial.legendre.leggauss(30)

def _panels(edges):
    a = np.asarray(edges[:-1]); bb = np.asarray(edges[1:])
    x = (0.5*(bb-a))[:, None]*_GX[None, :] + (0.5*(bb+a))[:, None]
    w = (0.5*(bb-a))[:, None]*_GW[None, :]
    return x.ravel(), w.ravel()

def alt_tail(h, U1, n=48):
    # int_{U1}^inf h(u) sin u du, U1 a multiple of pi: alternating sum over half-periods [U1+k pi, U1+(k+1) pi],
    # each by 30-point Gauss-Legendre, summed by the Cohen-Rodriguez Villegas-Zagier acceleration (n terms).
    k = np.arange(n)
    a = U1 + k*np.pi; bb = a + np.pi
    x = (0.5*(bb-a))[:, None]*_GX[None, :] + (0.5*(bb+a))[:, None]
    w = (0.5*(bb-a))[:, None]*_GW[None, :]
    ak = np.sum(w*h(x.ravel()).reshape(x.shape)*np.sin(x), axis=1)
    bk = ak*(-1.0)**k
    d = (3+np.sqrt(8))**n; d = (d+1/d)/2
    bc = -1.0; c = -d; s = 0.0
    for j in range(n):
        c = bc - c; s += c*bk[j]
        bc = (j+n)*(j-n)*bc/((j+0.5)*(j+1))
    return s/d

def I_ct(c, t, A, g, sub, U0=40*np.pi):
    b = g/(2*(A-1)); e = (2*A-2)/A
    lc = np.log(c)
    def h(u):
        u = np.atleast_1d(np.asarray(u, float))
        X = np.exp(2*np.log(t) + e*(np.log(u) - lc))
        return (1/A)*c**(-2/A)*u**(2/A-1)*np.exp(-b*np.log1p(X))
    # geometric panels from 1e-12 min(c,1) to 1, then half-periods to U0
    lo = 1e-12*min(c, 1.0)
    e1 = list(np.geomspace(lo, 1.0, int(8*np.log10(1.0/lo))+2))
    e2 = list(np.arange(1, int(U0/(np.pi/2))+1)*(np.pi/2))
    edges = [0.0] + sorted(set(e1 + [c*f for f in (0.3, 1, 3) if lo < c*f < 1] + [x for x in e2 if x > 1.0]))
    x, w = _panels(edges)
    hx = h(x)
    tot = np.sum(w*hx*(sin_minus_u(x) if sub else np.sin(x)))
    U1 = edges[-1]
    tot += alt_tail(h, U1)
    if sub:
        rr2 = integrate.quad(lambda u: h(u)[0]*u, U1, np.inf, epsabs=0, epsrel=1e-13, limit=400, full_output=1)
        tot -= rr2[0]
    return tot

def run(A, g, svals, nt=120):
    b = g/(2*(A-1)); ps = (g-2)/A; p = (2-g)/A
    tn, tw = gl(nt); ph = phi(tn)
    sub = g > A+2 + 1e-12
    res = abs(g-(A+2)) < 1e-12
    q = (A+2)/(2*A-2)
    Bq = float(mp.gamma(q)*mp.gamma(b-q)/mp.gamma(b)) if not res else float("nan")
    c1 = np.sum(tw*ph*tn*(1/(2*A-2))*tn**(-(A+2)/(A-1)))*Bq/(6*np.pi**2) if not res else float('nan')
    K = (1/(6*np.pi**2*A))*float(mp.gamma(p)*mp.sin(mp.pi*p/2))*np.sum(tw*ph*tn**(-2*b+ps)) if not res else float('nan')
    Klog = (1/(6*np.pi**2*A))*np.sum(tw*ph*tn**(1-2*b))
    out = dict(A=A, g=g, b=b, pstar=ps, c1_pred=c1, K_pred=K, Klog_pred=Klog, rows=[])
    for s in svals:
        Is = np.array([I_ct(s*t, t, A, g, sub) for t in tn])
        G = np.sum(tw*ph*Is)/(6*np.pi**2)          # if sub: G3 - c1 s
        row = dict(s=s)
        if sub:
            row['G3'] = G + c1*s; row['G3_minus_c1s'] = G; row['ratio_K'] = G/s**ps
        else:
            row['G3'] = G
            if not res:
                row['ratio_K'] = (G - c1*s)/s**ps; row['G3_over_sps'] = G/s**ps
            else:
                row['G3_over_s'] = G/s
        out['rows'].append(row)
    return out

if __name__ == '__main__':
    cases = [(3.0, 3.5), (3.0, 5.5), (3.0, 5.0), (10.15, 29.75)]
    svals = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    allres = []
    for A, g in cases:
        r = run(A, g, svals)
        # nt check at one s
        r2 = run(A, g, [1e-3], nt=200)
        r['nt_check_G3_1e-3'] = [r['rows'][2]['G3'], r2['rows'][0]['G3']]
        allres.append(r)
        print(json.dumps(r, indent=1), flush=True)
    json.dump(allres, open(sys.argv[1] if len(sys.argv) > 1 else 'runs/frozen_g3.json', 'w'), indent=1)
