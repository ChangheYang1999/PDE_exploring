"""Where is the residual? Per-radius max over angle of weighted and unweighted desingularized residuals."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state, problem_from_state, dev, DT
d = load_state(sys.argv[1]); prob, z = problem_from_state(d)
ca, cG, beta = prob.unpack(z); f = prob.model.fields(ca, cG, beta)
m = prob.model
Ra = f['Ra'].cpu().numpy(); RG = f['RG'].cpu().numpy()
Pa0 = 1.0 / prob.wa_r.cpu().numpy(); PG0 = 1.0 / prob.wG_r.cpu().numpy()
r = m.r
print(f"beta={float(beta):.6f} c={float(f['c']):.6f} a0={float(f['a0']):.6f} G0={float(f['G0']):.6f}")
print("     r        max|Ra|     max|Ra|/Pa0   max|RG|     max|RG|/PG0   a(r,th0)   G(r,th0)   w1(th0)   w2(th1)")
idx = np.unique(np.linspace(0, len(r) - 1, 28).astype(int))
for i in idx:
    print(f"{r[i]:10.3e}  {np.abs(Ra[i]).max():.2e}   {np.abs(Ra[i]).max()/Pa0[i]:.2e}     {np.abs(RG[i]).max():.2e}   {np.abs(RG[i]).max()/PG0[i]:.2e}    "
          f"{f['a'][i,0].item():+.3e} {f['G'][i,0].item():+.3e} {f['w1'][i,0].item():+.3e} {f['w2'][i,-1].item():+.3e}")
# angular profile of the weighted residual at the worst radius
i = int(np.argmax(np.abs(Ra).max(1) / Pa0)); print("worst Ra/Pa0 at r=%.3e, angular profile:" % r[i], np.array2string(Ra[i] / Pa0[i], precision=2))
i = int(np.argmax(np.abs(RG).max(1) / PG0)); print("worst RG/PG0 at r=%.3e, angular profile:" % r[i], np.array2string(RG[i] / PG0[i], precision=2))
