"""N12: vectorized float evaluation of generator fields (derivatives of the potential up to order NMAX) for generalized generators.

Generator: chi = H_m(x,y) R^beta T(t), q = x^2+y^2, R = 1+q, t = q/R = 1 - 1/R, H_m = Re (x+iy)^{2m}, T(t) a polynomial given either as
 ('mono', h): T = t^h  or  ('leg', w, n): T = t^w P_n(2t-1) (T1 high block; coefficient N_n is folded into the generator coefficient).
Radial jets: d^a/dq^a [R^beta T(t)] = R^(beta-a) F_a, F_a = sum_{l<=a} C(a,l) (beta-l)_(a-l) u^l T^{(l)}(t), u = 1/R   (basis860 formula, verified there).
Cartesian derivatives: d^gamma [H_m g(q)] = sum_{beta<=gamma} C(gamma,beta) d^beta H_m . sum_l g^{(l)}(q) P_{gamma-beta,l}(x,y)  (boxenc2.P_gamma),
 d^a_x d^b_y Re z^n = Re( i^b n!/(n-a-b)! z^(n-a-b) ).
All in float64 numpy, vectorized over points; the T1 form keeps coefficients O(1) (the canonical monomial form of the old 860 would lose accuracy).
Fields from the potential jet J (dict (a,b) -> array): psi = J[1,1]; rho = -(J[2,1] + J[0,3]); U = (-J[1,2], J[2,1]); derivatives by index shifts.
"""
import math, sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from boxenc2 import P_gamma

def falling_prod(beta, l, n):
    """(beta - l)_(n) = prod_{i<n} (beta - l - i)"""
    out = 1.0
    for i in range(n): out *= (beta - l - i)
    return out

def legendre_t_derivs(t, nmax, order):
    """P_n^{(s)}(z) at z = 2t-1 for n<=nmax, s<=order, as d^s/dt^s (includes 2^s). Returns array [n][s] of arrays."""
    z = 2*t - 1
    P = [[None]*(order+1) for _ in range(nmax+1)]
    P[0][0] = np.ones_like(t)
    for s in range(1, order+1): P[0][s] = np.zeros_like(t)
    if nmax >= 1:
        P[1][0] = z; P[1][1] = np.ones_like(t)*2 if order >= 1 else None
        for s in range(2, order+1): P[1][s] = np.zeros_like(t)
    for n in range(1, nmax):
        for s in range(order+1):
            term = z*P[n][s] + (2*s*P[n][s-1] if s else 0)       # d^s/dt^s (z P_n) = z P_n^{(s)} + s * 2 * P_n^{(s-1)}  (dz/dt = 2)
            P[n+1][s] = ((2*n+1)*term - n*P[n-1][s])/(n+1)
    return P

def T_jets(t, spec, order, Pleg=None):
    """t-derivatives T^{(l)}(t), l <= order, for spec ('mono', h) or ('leg', w, n)."""
    if spec[0] == 'mono':
        h = spec[1]
        return [math.perm(h, l)*t**(h-l) if l <= h else np.zeros_like(t) for l in range(order+1)]
    w, n = spec[1], spec[2]
    out = []
    for l in range(order+1):
        acc = np.zeros_like(t)
        for i in range(min(l, w)+1):
            if l - i <= n or True:
                acc += math.comb(l, i)*math.perm(w, i)*t**(w-i)*Pleg[n][l-i]
        out.append(acc)
    return out

def radial_jets(beta, u, T, order):
    """F_a = sum_l C(a,l) (beta-l)_(a-l) u^l T^{(l)}, a <= order; returns list of arrays (d^a g/dq^a = R^(beta-a) F_a)."""
    F = []
    for a in range(order+1):
        acc = np.zeros_like(u)
        for l in range(a+1):
            acc += math.comb(a, l)*falling_prod(beta, l, a-l)*u**l*T[l]
        F.append(acc)
    return F

def harmonic_derivs(x, y, m, order):
    """Angular factors: dH[(a,b)] = (n!/(n-k)!) cos((n-k) theta + b pi/2) with k = a+b, n = 2m; the factor r^(n-k) is applied inside generator_jet
    together with the radial power (log-space), so that no intermediate overflows for large m and r."""
    th = np.arctan2(y, x); n = 2*m; out = {}
    for a in range(order+1):
        for b in range(order+1-a):
            k = a + b
            out[(a, b)] = (math.perm(n, k)*np.cos((n-k)*th + b*math.pi/2)) if k <= n else np.zeros_like(x)
    return out

def generator_jet(x, y, m, beta, spec, order, cache):
    """dict (a,b) -> array of d^a_x d^b_y chi at the points, for a+b <= order (chi = H_m R^beta T(t))."""
    q, R, u, t, logR, logr = cache['q'], cache['R'], cache['u'], cache['t'], cache['logR'], cache['logr']
    T = T_jets(t, spec, order, cache.get('Pleg'))
    F = radial_jets(beta, u, T, order)
    dH = cache['H'][m] if m in cache['H'] else harmonic_derivs(x, y, m, order)
    xp = [np.ones_like(x)]; yp = [np.ones_like(y)]
    for i in range(order+1): xp.append(xp[-1]*x); yp.append(yp[-1]*y)
    n = 2*m
    # combined scale factors exp((beta-l) log R + (n-k) log r) for l, k <= order
    scale = {}
    for l in range(order+1):
        for k in range(order+1):
            if k <= n: scale[(l, k)] = np.exp((beta-l)*logR + (n-k)*logr)
    out = {}
    for a in range(order+1):
        for b in range(order+1-a):
            acc = np.zeros_like(x)
            for b1 in range(min(a, n)+1):
                for b2 in range(min(b, n-b1)+1):
                    k = b1 + b2; dh = dH[(b1, b2)]
                    sacc = np.zeros_like(x)
                    for l, poly in P_gamma((a-b1, b-b2)).items():
                        pv = np.zeros_like(x)
                        for (i, jj), c in poly.items(): pv += c*xp[i]*yp[jj]
                        sacc += F[l]*scale[(l, k)]*pv
                    acc += math.comb(a, b1)*math.comb(b, b2)*dh*sacc
            out[(a, b)] = acc
    return out

def make_cache(x, y, order, nleg=25):
    q = x*x + y*y; R = 1 + q; u = 1/R; t = q*u; logR = np.log1p(q); logr = 0.5*np.log(np.maximum(q, 1e-300))
    cache = {'q': q, 'R': R, 'u': u, 't': t, 'logR': logR, 'logr': logr, 'Pleg': legendre_t_derivs(t, nleg, order), 'H': {}}
    for m in range(0, 60): cache['H'][m] = harmonic_derivs(x, y, m, order)
    return cache

def fields_from_jet(J, order):
    """rho, U1, U2 and their derivatives up to order-3 from the potential jet J (needs J to order)."""
    def sh(a, b, i, j): return J[(a+i, b+j)]
    out = {}
    K = order - 3
    for i in range(K+1):
        for j in range(K+1-i):
            out[('rho', i, j)] = -(sh(2, 1, i, j) + sh(0, 3, i, j))
            out[('U1', i, j)] = -sh(1, 2, i, j); out[('U2', i, j)] = sh(2, 1, i, j)
    return out

if __name__ == '__main__':
    # test against the arb evaluator (state 131 potential in T1 form)
    import time
    from fractions import Fraction as Fr
    from ipm_arb import State
    ck = json.load(open(sys.argv[2])); S = State(sys.argv[1], prec=192)
    cl = float(Fr(ck['input_exact_for_checkpoint']['cl_exact'])); g = 1/cl
    p = [(3 + g - j*(1-g))/2 for j in range(4)]
    low = [float.fromhex(h) for h in ck['P_hex']]; num, den = ck['input_exact_for_checkpoint']['a000_exact'].split('/'); low[0] = int(num)/int(den)
    high = [float.fromhex(h) for h in ck['high_hex']]; NN = [float.fromhex(h) for h in ck['frozen_Nn_hex']]
    LOW = [(m, k, j) for j in range(4) for m in range(5) for k in range(m, 5)]; HIGH = [(m, n, j) for j in range(4) for m in range(10) for n in range(26-max(5, m))]
    gens = [(c, m, p[j]-m, ('mono', k-m)) for c, (m, k, j) in zip(low, LOW)] + [(c*NN[n], m, p[j]-m, ('leg', max(5-m, 0), n)) for c, (m, n, j) in zip(high, HIGH)]
    pts = np.array([[0.3, 0.5], [1.0, 2.0], [7.0, 1.0], [0.0, 50.0], [300.0, 100.0], [0.01, 0.02]])
    x, y = pts[:, 0].copy(), pts[:, 1].copy()
    order = 6
    t0 = time.time(); cache = make_cache(x, y, order)
    J = {}
    for (c, m, beta, spec) in gens:
        if c == 0: continue
        gj = generator_jet(x, y, m, beta, spec, order, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
    print('float evaluation of 860 generators at %d points to order %d: %.2f s' % (len(x), order, time.time()-t0))
    for i, (xx, yy) in enumerate(pts):
        f = S.fields(xx, yy, 5)
        Jc = S.phi_jet(xx, yy, 6)
        worst = max(abs(float(J[k][i]) - float(Jc[k].mid()))/max(abs(float(Jc[k].mid())), 1e-300) for k in J)
        print('point (%g,%g): rho float %.12e arb %s ; worst relative error over all jets to order 6: %.1e' % (xx, yy, -(J[(2, 1)][i] + J[(0, 3)][i]), f['rho'].str(12), worst))
