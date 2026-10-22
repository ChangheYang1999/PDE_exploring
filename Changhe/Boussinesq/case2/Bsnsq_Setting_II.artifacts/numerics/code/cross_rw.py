"""Cross-evaluate N112 states fitted with different row-weight radii Rw under each weighting (misfit without tail rows), so that
the Rw variants of 5v(c) can be compared like for like."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state, problem_from_state
states = sys.argv[1:]
Rws = [20.0, 30.0, 45.0]
print("state (fitted Rw)            " + "".join(f"  |F| under Rw={R:g}" for R in Rws))
for p in states:
    d = load_state(p); row = []
    for R in Rws:
        dd = dict(d); dd['Rw'] = np.array(R); dd['tail'] = np.array(0.0)
        prob, z = problem_from_state(dd, fixed_beta=float(d['beta']))
        row.append(float(prob.F(z).norm()))
    print(f"{p.split('/')[-1]:28s} (Rw={float(d['Rw']):g})" + "".join(f"  {v:.4e}" for v in row), flush=True)
