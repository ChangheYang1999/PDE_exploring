"""All scalar constants of the background with exact rationals and arb enclosures (state 88): c_l, gamma, lambda = 2c_l-1, sigma = a_0/(lambda-1),
a_0, c[rho_bar] = 1 - c_l, p_j, exponents p_n = n/c_l - (n-1), ||Theta_0||_{L2(0,pi)}^2 = 2 pi sum g_k^2/4 ... , ell_inf(K_bar) = (1-gamma)||Theta_0||^2_{L2(0,pi)},
||E_N||_{L2(0,pi/2)}, sup|E_1| (rigorous), the five Taylor defects, the degree-7 residual sup."""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import arb, ctx, fmpq
from farfield_bounds import sup_trig
ctx.prec = 200
def A(fr): return arb(fmpq(fr.numerator, fr.denominator))
def fs(fr): return '%d/%d' % (fr.numerator, fr.denominator)
d = json.load(open(sys.argv[1])); ff = json.load(open(sys.argv[2])); og = json.load(open(sys.argv[3]))
cl = Fr(d['cl']); a0 = Fr(og['a0']); g = 1/cl; lam = 2*cl - 1; sigma = a0/(lam - 1)
out = {'state': d['label'], 'cl': {'exact': fs(cl), 'float': float(cl)}, 'gamma': {'exact': fs(g), 'arb': A(g).str(40)}, 'lambda_2cl_minus_1': {'exact': fs(lam), 'float': float(lam)},
       'a0': {'exact': fs(a0), 'arb': A(a0).str(40)}, 'sigma_a0_over_lambda_minus_1': {'exact': fs(sigma), 'arb': A(sigma).str(40)}, 'c_rho_bar': {'exact': fs(1 - cl), 'float': float(1 - cl)},
       'p_n': {str(n): {'exact': fs(n*g - (n-1)), 'float': float(n*g - (n-1))} for n in range(1, 8)},
       'p_j_potential': {str(j): fs((3 + g - j*(1-g))/2) for j in range(4)}}
T0 = {int(k): Fr(v['exact']) for k, v in ff['density_sectors_G']['0,0']['series'].items()}
n2q = sum(v*v for v in T0.values())/4       # ||.||^2_{L2(0,pi/2)} / pi
out['Theta_0'] = {'sine_coefficients_exact': {str(k): fs(v) for k, v in T0.items()}, 'norm2_L2_0_pi_over_pi_exact': fs(n2q*2), 'norm_L2_0_pi': (A(n2q*2)*arb.pi()).sqrt().str(30),
                  'norm_L2_0_pi_half': (A(n2q)*arb.pi()).sqrt().str(30), 'sup_theta_rigorous': sup_trig({('s', k): v for k, v in T0.items()}).str(15)}
ell = (1 - g)*(n2q*2)
out['ell_inf_K_bar'] = {'formula': '(1-gamma) ||Theta_0||^2_{L2(0,pi)} = (1-gamma) * pi * (exact)', 'exact_over_pi': fs(ell), 'arb': (A(ell)*arb.pi()).str(30)}
for N in (1, 2, 3):
    S = {int(k): Fr(v['exact']) for k, v in ff['residual_sectors_E']['%d,0' % N]['series'].items()}
    n2 = sum(v*v for v in S.values())/4
    out['E_%d' % N] = {'exponent_exact': ff['residual_sectors_E']['%d,0' % N]['exponent'], 'norm_L2_0_pi_half': (A(n2)*arb.pi()).sqrt().str(25), 'sup_theta_rigorous_upper': sup_trig({('s', k): v for k, v in S.items()}).str(15), 'max_harmonic': max(S)}
F = {tuple(int(v) for v in k.split(',')): Fr(s) for k, s in og['F'].items()}
out['five_Taylor_defects_exact'] = {('x^%d y^%d' % k): {'exact': fs(v), 'float': float(v)} for k, v in F.items() if sum(k) in (3, 5)}
json.dump(out, open(sys.argv[4], 'w'), indent=1)
for k in ('gamma', 'lambda_2cl_minus_1', 'a0', 'sigma_a0_over_lambda_minus_1'): print(k, out[k])
print('Theta_0 norms:', out['Theta_0']['norm_L2_0_pi'], out['Theta_0']['norm_L2_0_pi_half'], 'sup', out['Theta_0']['sup_theta_rigorous'])
print('ell_inf(K_bar) =', out['ell_inf_K_bar']['arb'])
for N in (1, 2, 3): print('E_%d:' % N, out['E_%d' % N])
