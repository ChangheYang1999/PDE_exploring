"""Energy matrix on the symmetry axis x = 0. By parity (rho even in x, psi odd in x): rho_x(0,y) = 0, psi_xx(0,y) = psi_yy(0,y) = 0, so
M(0,y) = diag(2c_l + 1 - psi_xy + rho_y, 2c_l + 1 + psi_xy) exactly (SPEC S9 matrix), and lambda_min(M)(0,y) = 2c_l + 1 + psi_xy(0,y) whenever
psi_xy <= rho_y/2 (always here). The condition M >= (19/5) I on the axis is therefore EQUIVALENT to psi_xy(0,y) >= 19/5 - 2c_l - 1, i.e. the shear
-d_y U1(0,y) = d_x U2(0,y) = psi_xy(0,y) may not fall below 1 - c_l - (c_l + 2 - 19/5) = (1 - c_l) - 0.010319... (c_l = 1.8103192102).
Near the origin psi_xy(0,y) = (1 - c_l) + 3 c_(1,3) y^2 + 5 c_(1,5) y^4 + ... with psi = sum c_(a,b) x^a y^b, so the first requirement is c_(1,3) >= 0
(for state 131: c_(1,3) = 0.19312 > 0; equivalently phi_(2,4) = c_(1,3)/8 > 0).
Prints the axis profiles for the exact state 131 (BALL, ipm_arb) and for n12 candidate files (FLOAT, n12_eval), plus the Taylor coefficient.
Usage: axis_profile.py state131_exact.json state131_origin_taylor.json [n12 files...]"""
import sys, os, json, math
sys.set_int_max_str_digits(0)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
import numpy as np
ys = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
st, tay = sys.argv[1], sys.argv[2]
from ipm_arb import State
from flint import ctx
ctx.prec = 128
S = State(st, prec=128); cl = float(Fr(json.load(open(st))['cl'])); thr = 19/5 - 2*cl - 1
print('c_l = %.10f ; 2c_l + 1 = %.6f ; axis condition M >= 19/5  <=>  psi_xy(0,y) >= %.6f  (origin value 1 - c_l = %.6f, margin %.6f)' % (cl, 2*cl+1, thr, 1-cl, (1-cl) - thr))
T = json.load(open(tay)); psi = {tuple(int(v) for v in k.split(',')): Fr(v_) for k, v_ in T['psi'].items()}
print('state 131 exact Taylor of psi_xy(0,y): coefficients of y^0, y^2, y^4, y^6: %s' % [float(b*psi.get((1, b), Fr(0))) for b in (1, 3, 5, 7)])
print('\nstate 131 (BALL, 128 bits): y, psi_xy(0,y), rho_y(0,y), M11, M22 = lambda_min')
for y in ys:
    f = S.fields(0.0, y, 4); J = S.phi_jet(0.0, y, 4)
    pxy = J[(2, 2)]; rhoy = -(J[(2, 2)] + J[(0, 4)])
    print('  y = %5.2f : psi_xy %s  rho_y %s  M11 %.6f  M22 %.6f' % (y, pxy.str(10), rhoy.str(8), float((2*cl+1) - pxy + rhoy), float((2*cl+1) + pxy)))
from n12_eval import make_cache, generator_jet
from n12_norms import load_gens
from n12_run import gen_taylor
for path in sys.argv[3:]:
    gens, coefs, clq, p = load_gens(path); clf = float(clq)
    x = np.zeros(len(ys)); yv = np.array(ys); cache = make_cache(x, yv, 4); J = {}
    c24 = 0.0
    for gen, c in zip(gens, coefs):
        c = float(c)
        if c == 0: continue
        gj = generator_jet(x, yv, gen['m'], gen['beta'], gen['spec'], 4, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
        c24 += c*gen_taylor(gen, 6).get((2, 4), 0.0)
    pxy = J[(2, 2)]; rhoy = -(J[(2, 2)] + J[(0, 4)])
    # Taylor data at the origin (float): a_0 = rho_(0,1), r03 = rho_(0,3), r21 = rho_(2,1), c13 = psi_(1,3), c31 = psi_(3,1); F_3 = (2 r03 + a0 c13) y^3 + (2 lambda r21 + 3 a0 c31) x^2 y
    from n12_run import fields_taylor, pdx, pdy
    phiT = {}
    for gen, c in zip(gens, coefs):
        c = float(c)
        if c == 0: continue
        for k, v in gen_taylor(gen, 6).items(): phiT[k] = phiT.get(k, 0.0) + c*v
    FT = fields_taylor(phiT); psiT = pdy(pdx(phiT))
    a0 = FT['rho'].get((0, 1), 0.0); r03 = FT['rho'].get((0, 3), 0.0); r21 = FT['rho'].get((2, 1), 0.0); c13 = psiT.get((1, 3), 0.0); c31 = psiT.get((3, 1), 0.0); lam = 2*clf - 1
    print('\n%s (FLOAT): a_0 = %.6f, rho y^3 coefficient r03 = %.6f, psi x y^3 coefficient c13 = %.6f (3 c13 = %.6f = y^2 coefficient of psi_xy(0,y); 24 phi_(2,4) = %.6f);' % (os.path.basename(path), a0, r03, c13, 3*c13, 24*c24))
    print('   degree-3 stationarity: -2 r03/a0 = %.6f vs c13 = %.6f ; F_3 coefficients: y^3: %.4f, x^2 y: %.4f' % (-2*r03/a0, c13, 2*r03 + a0*c13, 2*lam*r21 + 3*a0*c31))
    for i, y in enumerate(ys):
        print('  y = %5.2f : psi_xy %.8f  rho_y %.6f  M11 %.6f  M22 %.6f  %s' % (y, pxy[i], rhoy[i], (2*clf+1) - pxy[i] + rhoy[i], (2*clf+1) + pxy[i], 'BELOW 19/5' if (2*clf+1) + pxy[i] < 3.8 else ''))
