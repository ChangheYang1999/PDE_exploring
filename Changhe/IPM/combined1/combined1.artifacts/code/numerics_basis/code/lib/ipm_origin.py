"""Exact Taylor expansion at the origin for the S1/IPM generator family (lane c1-n1).

Generator (m, k, p): chi = r^(2k) R^(p-k) cos(2m th) = H_m(x,y) (x^2+y^2)^(k-m) sum_l binom(p-k, l) (x^2+y^2)^l,  H_m = Re (x+iy)^(2m).
Polynomials are dicts {(i,j): coef} with i = x-degree, j = y-degree (coef mpq or float).
Fields: psi = chi_xy, rho = -d_y Lap chi, f = rho/y, q = c-1 + psi_x/y, R_f = (c x - psi_y) f_x + (c y + psi_x) f_y + q f.
Center relation: R_f(0) = 0  <=>  sum_i a_i chi_i,xxyy(0) = 1 - c  (strain sum).
Five Taylor equations: the degree-2 (2) and degree-4 (3) coefficients of R_f vanish.
"""
import math
from gmpy2 import mpq

def padd(P, key, v):
    if v == 0: return
    nv = P.get(key, 0)+v
    if nv == 0: P.pop(key, None)
    else: P[key] = nv

def pscale(P, f): return {k: v*f for k, v in P.items()} if f != 0 else {}
def psum(*Ps):
    out = {}
    for P in Ps:
        for k, v in P.items(): padd(out, k, v)
    return out
def pmul(P, Q, degmax=None):
    out = {}
    for (i, j), a in P.items():
        for (k, l), b in Q.items():
            if degmax is not None and i+j+k+l > degmax: continue
            padd(out, (i+k, j+l), a*b)
    return out
def dx(P):
    out = {}
    for (i, j), a in P.items():
        if i > 0: padd(out, (i-1, j), i*a)
    return out
def dy(P):
    out = {}
    for (i, j), a in P.items():
        if j > 0: padd(out, (i, j-1), j*a)
    return out
def div_y(P):
    out = {}
    for (i, j), a in P.items():
        assert j >= 1, 'not divisible by y'
        padd(out, (i, j-1), a)
    return out
def truncate(P, degmax): return {k: v for k, v in P.items() if k[0]+k[1] <= degmax}

def binom_q(p, l):
    out = mpq(1)
    for i in range(l): out = out*(p-i)/(i+1)
    return out

def H_poly(m):
    """Re (x+iy)^(2m) as polynomial"""
    out = {}
    for l in range(m+1): padd(out, (2*m-2*l, 2*l), mpq((-1)**l*math.comb(2*m, 2*l)))
    return out

def r2_power(n):
    out = {}
    for i in range(n+1): padd(out, (2*i, 2*(n-i)), mpq(math.comb(n, i)))
    return out

def chi_taylor(m, k, p, degmax):
    """Taylor polynomial of chi_(m,k,p) up to total degree degmax (exact mpq; p mpq)."""
    H = H_poly(m); out = {}
    l = 0
    while 2*k+2*l <= degmax:
        term = pscale(pmul(H, r2_power(k-m+l)), binom_q(p-k, l))
        out = psum(out, term); l += 1
    return out

def fields_taylor(chi):
    """psi = chi_xy, f = -(d_y Lap chi)/y, qpart = psi_x/y (polynomials)"""
    psi = dx(dy(chi))
    lap = psum(dx(dx(chi)), dy(dy(chi)))
    rho = pscale(dy(lap), -1)
    f = div_y(rho); qpart = div_y(dx(psi))
    return psi, f, qpart

def Rf_taylor(c, psi, f, qpart, degmax):
    """R_f = (c x - psi_y) f_x + (c y + psi_x) f_y + (c - 1 + psi_x/y) f, truncated"""
    wx = psum({(1, 0): c}, pscale(dy(psi), -1)); wy = psum({(0, 1): c}, dx(psi)); q = psum({(0, 0): c-1}, qpart)
    return truncate(psum(pmul(wx, dx(f), degmax), pmul(wy, dy(f), degmax), pmul(q, f, degmax)), degmax)

TAYLOR_KEYS = [(0, 0), (2, 0), (0, 2), (4, 0), (2, 2), (0, 4)]      # center + five Taylor equations (coefficients of R_f)

class OriginJets:
    """Taylor data of a generator list (m, k, p): for each generator, polynomials psi_i, f_i, qpart_i up to the needed degree."""
    def __init__(self, terms, degmax=4, exact=True):
        self.terms = terms; self.degmax = degmax
        self.jets = []
        for t in terms:
            m, k = int(t['m']), int(t['k']); p = t['p'] if exact else float(t['p'])
            if 2*k > degmax+4:
                self.jets.append(None); continue
            chi = chi_taylor(m, k, mpq(p) if exact else p, degmax+4)
            if not exact: chi = {kk: float(v) for kk, v in chi.items()}
            self.jets.append(fields_taylor(chi))
    def strains(self):
        """chi_xxyy(0) for each generator = coefficient of x^2 y^2 times 4 ... equivalently psi_xy(0) = coefficient (0,0) of psi after d_x d_y: psi = chi_xy, psi_xy(0) = 4 * chi[(2,2)]"""
        out = []
        for jt in self.jets:
            if jt is None: out.append(0); continue
            psi = jt[0]; out.append(dx(dy(psi)).get((0, 0), 0))
        return out
    def total(self, coefs):
        psi = {}; f = {}; qp = {}
        for a, jt in zip(coefs, self.jets):
            if jt is None or a == 0: continue
            psi = psum(psi, pscale(jt[0], a)); f = psum(f, pscale(jt[1], a)); qp = psum(qp, pscale(jt[2], a))
        return psi, f, qp
    def Rf_coeffs(self, c, coefs):
        psi, f, qp = self.total(coefs)
        R = Rf_taylor(c, psi, f, qp, self.degmax)
        return [R.get(key, 0) for key in TAYLOR_KEYS]
    def Rf_coeffs_jacobian(self, c, coefs):
        """d(R_f Taylor coefficients)/d a_i (exact or float), list over generators of lists over TAYLOR_KEYS"""
        psi, f, qp = self.total(coefs)
        wx = psum({(1, 0): c}, pscale(dy(psi), -1)); wy = psum({(0, 1): c}, dx(psi)); q = psum({(0, 0): c-1}, qp)
        fx = dx(f); fy = dy(f); d = self.degmax
        cols = []
        for jt in self.jets:
            if jt is None: cols.append([0]*len(TAYLOR_KEYS)); continue
            psi_i, f_i, qp_i = jt
            dR = psum(pmul(wx, dx(f_i), d), pmul(wy, dy(f_i), d), pmul(q, f_i, d),
                      pmul(pscale(dy(psi_i), -1), fx, d), pmul(dx(psi_i), fy, d), pmul(qp_i, f, d))
            cols.append([dR.get(key, 0) for key in TAYLOR_KEYS])
        return cols
    def a0(self, coefs):
        return self.total(coefs)[1].get((0, 0), 0)
