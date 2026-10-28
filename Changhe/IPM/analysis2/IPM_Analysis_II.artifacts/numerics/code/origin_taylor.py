"""Exact (rational) Taylor expansion at the origin of phi, psi, rho, U, V and the residual F = V.grad rho - rho
for an 860-generator case-4 state. All arithmetic in Fractions; the truncation is exact: the binomial series
(1+q)^{p-k} = sum_l C(p-k,l) q^l converges for q = r^2 < 1, and we keep every term of total degree <= DEG in (x,y).

Output: polynomial dictionaries {(ix,iy): Fraction} and the derived origin data.
"""
import json, math, sys
from fractions import Fraction as Fr

def canon(j, m, k): return 215*j + 26*m - m*(m-1)//2 + (k-m)

def binom_fr(p, l):
    out = Fr(1)
    for i in range(l): out = out*(p-i)/(i+1)
    return out

def padd(P, key, v):
    if v == 0: return
    P[key] = P.get(key, 0) + v
    if P[key] == 0: del P[key]

def pmul(P, Q, deg):
    out = {}
    for (a, b), u in P.items():
        for (c, d), v in Q.items():
            if a+b+c+d <= deg: padd(out, (a+c, b+d), u*v)
    return out

def pdx(P): return {(a-1, b): a*v for (a, b), v in P.items() if a > 0}
def pdy(P): return {(a, b-1): b*v for (a, b), v in P.items() if b > 0}
def pscale(P, c): return {k: c*v for k, v in P.items()} if c != 0 else {}
def psum(*Ps):
    out = {}
    for P in Ps:
        for k, v in P.items(): padd(out, k, v)
    return out

def harmonic(m):
    """H_m = Re (x+iy)^{2m} = sum_l (-1)^l C(2m,2l) x^{2m-2l} y^{2l}."""
    return {(2*m-2*l, 2*l): Fr((-1)**l*math.comb(2*m, 2*l)) for l in range(m+1)}

def qpow(n):
    return {(2*i, 2*(n-i)): Fr(math.comb(n, i)) for i in range(n+1)}

def phi_taylor(cl, a, DEG):
    g = Fr(1)/cl; lam = 1-g
    p = [(3+g-j*lam)/2 for j in range(4)]
    phi = {}
    for j in range(4):
        for m in range(10):
            if 2*m > DEG: continue
            # radial coefficient of q^n (n >= 0) multiplying H_m: sum_k a_{mkj} C(p_j-k, n-(k-m)) with k-m <= n
            nmax = (DEG-2*m)//2
            rad = {}
            for k in range(m, 26):
                c = a[canon(j, m, k)]
                if c == 0: continue
                for n in range(k-m, nmax+1):
                    rad[n] = rad.get(n, 0) + c*binom_fr(p[j]-k, n-(k-m))
            Hm = harmonic(m)
            for n, c in rad.items():
                if c == 0: continue
                for key, v in pmul(Hm, qpow(n), DEG).items(): padd(phi, key, c*v)
    return phi, p

def all_fields(cl, a, DEG):
    phi, p = phi_taylor(cl, a, DEG)
    psi = pdy(pdx(phi))
    lap = psum(pdx(pdx(phi)), pdy(pdy(phi)))
    rho = pscale(pdy(lap), -1)
    U1 = pscale(pdy(psi), -1); U2 = pdx(psi)
    V1 = psum({(1, 0): cl}, U1); V2 = psum({(0, 1): cl}, U2)
    rx, ry = pdx(rho), pdy(rho)
    # exact degrees: phi exact to DEG, rho to DEG-3, grad rho to DEG-4, U to DEG-3; F exact to DEG-4
    Fdeg = DEG-4
    F = psum(pmul(V1, rx, Fdeg), pmul(V2, ry, Fdeg), pscale({k: v for k, v in rho.items() if sum(k) <= Fdeg}, -1))
    return {'phi': phi, 'psi': psi, 'rho': rho, 'U1': U1, 'U2': U2, 'F': F, 'F_exact_degree': Fdeg, 'p': p}

def fr_str(v): return '%d/%d' % (v.numerator, v.denominator)

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); DEG = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    R = all_fields(cl, a, DEG)
    rho, psi, F = R['rho'], R['psi'], R['F']
    a0 = rho.get((0, 1), Fr(0)); c = psi.get((1, 1), Fr(0))
    print('a0 = rho_y(0) =', float(a0), fr_str(a0)[:60])
    print('c[rho] = psi_xy(0) =', float(c), '; cl + c - 1 =', cl + c - 1)
    print('rho Taylor terms up to degree 5:')
    for key in sorted(rho, key=lambda k: (sum(k), k)):
        if sum(key) <= 5: print('  x^%d y^%d : %.17g' % (key[0], key[1], float(rho[key])))
    print('F = V.grad rho - rho, exact to degree', R['F_exact_degree'], '; terms:')
    for key in sorted(F, key=lambda k: (sum(k), k)):
        if sum(key) <= R['F_exact_degree']: print('  x^%d y^%d : %.6e' % (key[0], key[1], float(F[key])))
    print('stored five_Taylor:', d.get('five_Taylor'))
    out = {'cl': d['cl'], 'DEG': DEG, 'F_exact_degree': R['F_exact_degree'],
           'rho': {'%d,%d' % k: fr_str(v) for k, v in rho.items()}, 'psi': {'%d,%d' % k: fr_str(v) for k, v in psi.items()},
           'phi': {'%d,%d' % k: fr_str(v) for k, v in R['phi'].items()},
           'F': {'%d,%d' % k: fr_str(v) for k, v in F.items() if sum(k) <= R['F_exact_degree']},
           'a0': fr_str(a0), 'c_rho': fr_str(c)}
    json.dump(out, open(sys.argv[2], 'w'))
