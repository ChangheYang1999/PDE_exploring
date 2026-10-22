"""Build a start state for the forward solver: the LM state's fields for r <= Rc, continued for r > Rc by the pure
far-field law (l=0 prefactor) matched at Rc, so that the velocity has no spurious far-field stagnation points."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state, problem_from_state, fit_fields, save_state, model_prefactors, rad_of_r, dev, DT
src, Rc, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
d = load_state(src); prob, z = problem_from_state(d)
ca, cG, beta = prob.unpack(z); beta = float(beta)
m = prob.model; f = m.fields(ca, cG, beta)
a = f['a'].cpu().numpy().copy(); G = f['G'].cpu().numpy().copy()
r = m.r; rad = rad_of_r(m, prob.mapname, r)
Pa = model_prefactors(m, prob.mapname, rad, 'a')[0]; PG = model_prefactors(m, prob.mapname, rad, 'G')[0]
ic = np.argmin(np.abs(r - Rc)); Rc = r[ic]
far = r > Rc
a[far] = a[ic][None, :] * (Pa[far] / Pa[ic])[:, None]
G[far] = G[ic][None, :] * (PG[far] / PG[ic])[:, None]
print(f"matching radius {Rc:.3f}; a(Rc,th) min/max {a[ic].min():.3e}/{a[ic].max():.3e}; G(Rc,th) min/max {G[ic].min():.3e}/{G[ic].max():.3e}")
z2 = fit_fields(prob, a, G, r, m.th, beta)
d2 = prob.diagnostics(z2)
print({k: round(v, 5) for k, v in d2.items() if k in ('c', 'a0', 'G0', 'Fnorm', 'Ra_max', 'RG_max')})
save_state(out, prob, z2, [d2])
