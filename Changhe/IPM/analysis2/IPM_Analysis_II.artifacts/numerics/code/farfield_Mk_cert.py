"""Far-field certificates for the matrix hypotheses (B1), (B2), (B4), (B5), (B6) of S1_CLOSURE section 3, uniform in r >= R, from the exact sector
expansion of the state (farfield_bounds: coefficient bounds |field| <= B_field r^e for all r >= R, e = gamma - 1 for D rho and DU, e = gamma for U).
With P = R^(gamma-1) (all perturbations are <= coefficient * r^(gamma-1) <= coefficient * P for r >= R) and f(r^2) = r^2/(1 + 4 r^2) increasing:
  M_k = (1 + (1-k) c_l + (16/5) c_l f(r^2)) I + (16/5) (U.X)/(1 + 4 r^2) I - k sym DU + A      (omega = (1 + 4 r^2)^(2/5); k = 1 is the unweighted M_1 with f dropped)
  lambda_min(M_k) >= 1 + (1-k) c_l + (16/5) c_l f(R^2) [k >= 2] - (4/5)(B_U1 + B_U2) P - k sqrt(B11^2 + ((B12 + B21)/2)^2) P - (B_rx/2) P
using |U.X| <= r (|U1| + |U2|), (16/5) r^(1+gamma)/(1 + 4 r^2) <= (4/5) r^(gamma-1), lambda_max(sym DU) = sqrt(DU11^2 + ((DU12+DU21)/2)^2) (tr DU = 0),
lambda_min(A) >= -|rho_x|/2. Every bound is monotone in r, so the value at R holds for all r >= R.
  (B1) lambda_min(M) >= 2 c_l + 1 - sqrt(B11^2 + s^2) P - (B_rx/2) P   (M = (2c_l + 1) I + sym DU + A; also computed with the rho_y term in farfield_M_cert.py)
  (B2) rho_x^2 <= (B_rx P)^2 < 1/100 and rho_y > 0.
Usage: farfield_Mk_cert.py state_exact.json R1 R2 ...   (env FARFIELD_MK_OUT for the output JSON)
"""
import sys, os, json, math
from fractions import Fraction as Fr
from flint import arb, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from farfield_bounds import sector_fields, field_bound, sup_trig, A
from farfield_M_cert import inf_trig

if __name__ == '__main__':
    d = json.load(open(sys.argv[1])); cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    ctx.prec = 128
    Q = 6
    sectors, p = sector_fields(cl, a, Q)
    g = Fr(1)/cl; e1 = g - 1
    CL = A(cl)
    out = {}
    def up(v): return math.nextafter(float(v.upper()), math.inf)
    def lo(v): return math.nextafter(float(v.lower()), -math.inf)
    for R in [float(x) for x in sys.argv[2:]]:
        B = {}
        for name in ['rho_x', 'rho_y', 'DU11', 'DU12', 'DU21', 'DU22', 'U1', 'U2']:
            B[name], rows, tail = field_bound(sectors, p, cl, a, name, R, e1 if name not in ('U1', 'U2') else g, Q)
        # rho_y lower bound (as in farfield_M_cert.py): leading sector inf minus the rest and the tail
        e00, T00 = sectors[(0, 0)]['rho_y']; inf00 = inf_trig(T00); rest = arb(0)
        for (j, q), fields in sectors.items():
            if (j, q) == (0, 0): continue
            e, T = fields['rho_y']; rest += sup_trig(T)*arb(R)**A(e - e1)
        Bfull, rows, tail = field_bound(sectors, p, cl, a, 'rho_y', R, e1, Q)
        rho_y_coef = inf00 - rest - arb(tail)
        P = arb(R)**A(e1)                     # R^(gamma-1); every perturbation coefficient * r^(gamma-1) is <= coefficient * P for r >= R
        s_B = (B['DU12'] + B['DU21'])/2
        symdu = (B['DU11']*B['DU11'] + s_B*s_B).sqrt()*P      # (DU22 has the same coefficient bound as DU11 by construction; we use DU11's)
        symdu = symdu.max((B['DU22']*B['DU22'] + s_B*s_B).sqrt()*P)
        rx = B['rho_x']*P
        ux = (arb(4)/5)*(B['U1'] + B['U2'])*P                   # bound of (16/5)|U.X|/(1 + 4 r^2) for r >= R
        fR = arb(R)**2/(1 + 4*arb(R)**2)
        res = {'R': R, 'P=R^(gamma-1)': float(P), 'coef': {k: float(v) for k, v in B.items()}, 'rho_y_coef_lower': lo(rho_y_coef),
               'symDU_upper': up(symdu), 'abs_rho_x_upper': up(rx), 'weight_term_pert_upper': up(ux)}
        res['B1_lambda_min_M_lower'] = lo(2*CL + 1 - symdu - rx/2)
        res['B2_margin_lower'] = math.nextafter(float(Fr(1, 100) - Fr(up(rx*rx))), -math.inf)
        res['B4_lambda_min_M1_lower'] = lo(1 - symdu - rx/2)
        res['B5_lambda_min_M2_lower'] = lo(1 - CL + (arb(16)/5)*CL*fR - ux - 2*symdu - rx/2)
        res['B6_lambda_min_M3_lower'] = lo(1 - 2*CL + (arb(16)/5)*CL*fR - ux - 3*symdu - rx/2)
        print('r >= %g: P = %.4g; |rho_x| <= %.4g, ||sym DU|| <= %.4g, weight pert <= %.4g, rho_y >= %.4g r^(gamma-1); lambda_min: M >= %.5f (target 3.8), M_1 >= %.5f (0.9), M_2 >= %.5f (0.5), M_3 >= %.5f (-1.25); (B2) margin >= %.5g' % (
            R, float(P), res['abs_rho_x_upper'], res['symDU_upper'], res['weight_term_pert_upper'], res['rho_y_coef_lower'], res['B1_lambda_min_M_lower'], res['B4_lambda_min_M1_lower'], res['B5_lambda_min_M2_lower'], res['B6_lambda_min_M3_lower'], res['B2_margin_lower']))
        out[str(R)] = res
    json.dump(out, open(os.environ.get('FARFIELD_MK_OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'farfield_Mk_cert.json')), 'w'), indent=1)
