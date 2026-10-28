"""Certified far-field bound of the residual: |F(X)| <= B_F(R) r^{p_2} for all r >= R, p_2 = 2 gamma - 1, from the exact sector expansion.

F = c_l r d_r rho - rho + U.grad rho, with rho = rho_Q + rho_T (sectors q <= Q and the tail q > Q), U = U_Q + U_T.
Exact part: E_{h,q} for q <= Q (farfield_exact.expand with qmax = Q): all terms of F whose total q-order is <= Q.
Remainder: (a) linear tail (c_l alpha - 1) rho_T sectors: bounded by field tails of rho and of r d_r rho (= alpha rho per sector);
           (b) cross terms U_u . grad rho_v with u + v > Q, u, v <= Q: exact sector sups (sup|U| sup|grad rho| per pair);
           (c) U_Q.grad rho_T + U_T.grad rho_Q + U_T.grad rho_T: tail bounds times sector sup bounds.
All sector functions are trig polynomials whose sup over theta is bounded rigorously (grid + Bernstein). The rules and tails are those
of farfield_bounds.py.  Output: B_F(R) and the split; also sup|E_1| exactly (the limit as R -> infinity).
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, ctx
from farfield_bounds import sector_fields, sup_trig, A, canon, binom_fr, dx, dy, lap, scale, tadd
import farfield_exact as FE

def tail_coeff_bound(cl, a, p, j, q, d):
    """Upper bound on the sum of |coefficients| of the order-d derivative field of the potential sector (j,q): sum_m [sum_k |a_mkj| C(B_k+q-1,q)] prod_{i<d}(|s|+n+2+2i)."""
    pj = p[j]; s = 2*pj - 2*q; tot = arb(0)
    for m in range(10):
        cm = arb(0)
        for k in range(m, 26):
            ak = a[canon(j, m, k)]
            if ak == 0: continue
            Bk = math.ceil(abs(float(pj - k))) + 1
            cm += abs(A(ak))*math.comb(Bk+q-1, q)
        fac = arb(1); n = 2*m
        for i in range(d): fac *= (abs(A(s)) + n + 2 + 2*i)
        tot += cm*fac
    return tot

def tail_sum(cl, a, p, j, d, Q, R, e_target):
    """sum_{q>Q} tail_coeff_bound(j,q,d) R^{s_jq - d - e_target}, with geometric closure."""
    acc = arb(0)
    for q in range(Q+1, Q+41):
        s = 2*p[j] - 2*q
        acc += tail_coeff_bound(cl, a, p, j, q, d)*arb(R)**A(s - d - e_target)
    qq = Q+41; s = 2*p[j] - 2*qq
    ratio = (1 + arb(27)/(qq+1))*(1 + arb(2)/(2*qq - 2))**d*arb(R)**-2
    if not ratio < 1: raise ValueError('R too small')
    acc += tail_coeff_bound(cl, a, p, j, qq, d)*arb(R)**A(s - d - e_target)/(1 - ratio)
    return acc

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    ctx.prec = 128
    Q = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    g = Fr(1)/cl; lam = 1-g; p2 = 2*g-1
    def alpha(h, q): return g - h*lam - 2*q
    X = FE.expand(cl, a, qmax=Q, hmax=7)
    sectors, p = sector_fields(cl, a, Q)
    out = {}
    for R in [float(x) for x in sys.argv[3:]]:
        Rz = arb(R)
        # (exact part) sum over (h,q) of sup|E_{h,q}| R^{alpha - p2}
        exact = arb(0); lead = None; rows = []
        for (h, q), S in X['E'].items():
            if not S: continue
            T = {('s', k): v for k, v in S.items()}
            sup = sup_trig(T); e = alpha(h, q)
            if e > p2 + Fr(1, 10**9): raise ValueError('sector above p2: (%d,%d)' % (h, q))
            contrib = sup*Rz**A(e - p2) if (h, q) != (1, 0) else sup
            if (h, q) == (1, 0): lead = float(sup)
            exact += contrib; rows.append(((h, q), float(e), float(sup), float(contrib)))
        # (a) linear tail: |(c_l alpha - 1) rho_T|: per j, tail of rho (d = 3) with factor (c_l|alpha|+1) <= c_l(|gamma| + 3 lam + 2q) + 1 ... bound alpha by |s - 3| + 1
        lin = arb(0)
        for j in range(4):
            for q in range(Q+1, Q+41):
                s = 2*p[j] - 2*q; al = s - 3
                lin += (A(cl)*abs(A(al)) + 1)*tail_coeff_bound(cl, a, p, j, q, 3)*Rz**A(al - p2)
            qq = Q+41; s = 2*p[j] - 2*qq; al = s - 3
            ratio = (1 + arb(27)/(qq+1))*(1 + arb(2)/(2*qq - 2))**4*Rz**-2
            lin += (A(cl)*abs(A(al)) + 1)*tail_coeff_bound(cl, a, p, j, qq, 3)*Rz**A(al - p2)/(1 - ratio)
        # sector sups of |U| and |grad rho| per (j,q): |U| <= sup|U1| + sup|U2|, |grad rho| <= sup|rho_x| + sup|rho_y|
        supU = {}; supG = {}
        for (j, q), f in sectors.items():
            supU[(j, q)] = sup_trig(f['U1'][1]) + sup_trig(f['U2'][1]); supG[(j, q)] = sup_trig(f['rho_x'][1]) + sup_trig(f['rho_y'][1])
        # (b) cross terms with u + v > Q (exponents (alpha_iu + 1) + (alpha_jv + 1) - 2 ... U exponent = alpha+1? no: U sector exponent s-3 = alpha; grad rho exponent alpha - 1; product exponent alpha_iu + alpha_jv - 1)
        cross = arb(0)
        for (i, u) in sectors:
            for (jj, v) in sectors:
                if u + v <= Q: continue
                e = alpha(i, u) + alpha(jj, v) - 1
                cross += supU[(i, u)]*supG[(jj, v)]*Rz**A(e - p2)
        # (c) tails: U_Q.grad rho_T + U_T.grad rho_Q + U_T.grad rho_T ; U tail: d = 3 (exponent s-3), grad rho tail: d = 4 (exponent s-4)
        tails = arb(0)
        UT = {j: None for j in range(4)}; GT = {j: None for j in range(4)}
        for j in range(4):
            # tail sums as functions: sum_q coeff R^{s_jq - d}; we need them combined with the other factor's exponent: bound each tail by its value at R times r^{e_tail}, e_tail = 2p_j - 2(Q+1) - d (largest exponent in the tail), valid since all later terms decay faster
            UT[j] = (tail_sum(cl, a, p, j, 3, Q, R, 2*p[j] - 2*(Q+1) - 3), 2*p[j] - 2*(Q+1) - 3)
            GT[j] = (tail_sum(cl, a, p, j, 4, Q, R, 2*p[j] - 2*(Q+1) - 4), 2*p[j] - 2*(Q+1) - 4)
        for (i, u) in sectors:
            for j in range(4):
                tails += supU[(i, u)]*GT[j][0]*Rz**A(alpha(i, u) + GT[j][1] - p2)
                tails += UT[j][0]*supG[(i, u)]*Rz**A(UT[j][1] + alpha(i, u) - 1 - p2)
        for i in range(4):
            for j in range(4):
                tails += UT[i][0]*GT[j][0]*Rz**A(UT[i][1] + GT[j][1] - p2)
        B = exact + lin + cross + tails
        print('R = %g (Q = %d): |F| <= %.6f r^p2 for all r >= R  [exact sectors %.6f (sup|E_1| = %.6f), linear tail %.2e, cross %.2e, nonlinear tails %.2e]' % (R, Q, float(B.upper()), float(exact), lead, float(lin), float(cross), float(tails)))
        out[str(R)] = {'B_F': float(B.upper()), 'exact_part': float(exact), 'sup_E1': lead, 'linear_tail': float(lin), 'cross': float(cross), 'nonlinear_tails': float(tails), 'Q': Q}
    json.dump(out, open(os.environ.get('FARFIELD_F_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'farfield_F_cert_088.json')), 'w'), indent=1)
