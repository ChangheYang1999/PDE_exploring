"""BALL cross-check of a refit potential (exact generator file): evaluate F and rho at sample points with arb (256 bits) through the
branch-series machinery (fcert.FCert.jet_branches with branches built from the exact coefficients: each (m, j) group combined into one
coefficient list over t^h, Legendre functions expanded exactly), and compare with the float evaluator (n12_eval)."""
import sys, os, json, math
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from flint import arb, ctx, fmpq
from fcert import FCert
from n12_eval import make_cache, generator_jet
from n12_fit import F_jets, ORDER
from n12_exact import T_coeffs

def branches_from_file(path, S):
    d = json.load(open(path)); cl = Fr(d['cl']); g = Fr(1)/cl; lam = 1-g; p = [(3+g-j*lam)/2 for j in range(6)]
    groups = {}
    for gen in d['generators']:
        m, j = gen['m'], gen['j']; c = Fr(gen['coef'])
        if c == 0: continue
        ct = T_coeffs(tuple(gen['spec']))
        grp = groups.setdefault((m, j), {})
        for h, v in ct.items(): grp[h] = grp.get(h, Fr(0)) + c*v
    br = []
    for (m, j), grp in groups.items():
        hmax = max(grp); coeffs = [arb(fmpq(grp.get(h, Fr(0)).numerator, grp.get(h, Fr(0)).denominator)) for h in range(hmax+1)]
        br.append((m, arb(fmpq((p[j]-m).numerator, (p[j]-m).denominator)), coeffs))
    return br, cl, d

if __name__ == '__main__':
    path, state88_json, ckpt_json = sys.argv[1:4]
    S = FCert(state88_json, ckpt_json, prec=256)       # only for the series machinery; its own A is not used
    S.cl = None
    br, cl, d = branches_from_file(path, S)
    S.cl = arb(fmpq(cl.numerator, cl.denominator))
    pts = [(0.3, 0.5), (1.0, 2.0), (7.0, 1.0), (30.0, 40.0), (300.0, 100.0), (0.0, 5000.0), (0.01, 0.02)]
    # float side
    gens = [{'m': g_['m'], 'j': g_['j'], 'spec': tuple(g_['spec']), 'coef': float(Fr(g_['coef']))} for g_ in d['generators']]
    gf = 1/float(cl); pf = [(3+gf-j*(1-gf))/2 for j in range(6)]
    x = np.array([q[0] for q in pts]); y = np.array([q[1] for q in pts]); cache = make_cache(x, y, ORDER)
    J = {}
    for gen in gens:
        if gen['coef'] == 0: continue
        gj = generator_jet(x, y, gen['m'], pf[gen['j']]-gen['m'], gen['spec'], ORDER, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + gen['coef']*v
    FJ = F_jets(J, None, float(cl), x, y, K=2)
    for i, (xx, yy) in enumerate(pts):
        ctx.cap = 8
        Jb = S.jet_branches(br, arb(xx), arb(yy), 5)
        rho = -(Jb[(2, 1)] + Jb[(0, 3)]); rx = -(Jb[(3, 1)] + Jb[(1, 3)]); ry = -(Jb[(2, 2)] + Jb[(0, 4)]); U1 = -Jb[(1, 2)]; U2 = Jb[(2, 1)]
        F = (S.cl*arb(xx) + U1)*rx + (S.cl*arb(yy) + U2)*ry - rho
        print('point (%g,%g): F arb %s  float %.12e  diff %.1e | rho arb %s float %.12e' % (xx, yy, F.str(12), FJ[(0, 0)][i], abs(FJ[(0, 0)][i] - float(F.mid())), rho.str(10), -(J[(2, 1)][i] + J[(0, 3)][i])))
