import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import time
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms = load131()
gens = OPT.t1_generators_860(); a0, a0_exact = OPT.case4_coefficients_t1(J, c)
mesh = EV.training_mesh(dev)
t0 = time.time(); prob = OPT.Problem(gens, c, mesh, objective='Jabs', r_cut=0.02); print('problem build', time.time()-t0)
print('objective at 131 (Jabs excl r<0.02):', prob.objective_value(a0))
print('taylor values:', prob.taylor_values(a0))
# check exact terms reproduce state 131 sector E_1
tv = X.residual_sectors(c, OPT.exact_terms(prob, a0_exact), 1)[0]; gamma=1/c; lam=1-gamma
print('E_1 quarter norm via T1 gens:', X.quarter_norm(tv[gamma-lam]))
prob.add_center()
a, hist = prob.optimize(a0, steps=6, lam0=1e-4, taylor=True, log='RUN_ROOT/numerics_N1N2/numerics/optimization/logs/sanity.log')
print('final objective', prob.objective_value(a), 'taylor', prob.taylor_values(a))
