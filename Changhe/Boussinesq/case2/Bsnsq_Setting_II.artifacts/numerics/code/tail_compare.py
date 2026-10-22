"""Compare a tail-constrained state with its unconstrained parent: misfit WITHOUT the tail rows (same Rw = 30 weighting),
max residuals, R1 (next-order far-field defect, Richardson t1 = 1e-5), x*, resonance, axis zeros."""
import sys, json, torch, numpy as np
sys.path.insert(0, 'code')
from lm_solve import *
for path in sys.argv[1:]:
    d = load_state(path)
    N, M, L = int(d['N']), int(d['M']), float(d['L']); beta = float(d['beta'])
    prob = LMProblem(N, M, L, float(d['beta_map']), float(d['sigma_a']), float(d['sigma_G']), float(d['a0_target']), 30.0, beta, ov=2.0, mapname='t', Rw=30.0, tail=1.0, t1=1e-5)
    z = prob.pack(torch.tensor(d['ca'], dtype=DT, device=dev), torch.tensor(d['cG'], dtype=DT, device=dev), beta)
    dd = prob.diagnostics(z)
    prob.tail = None; dn = prob.diagnostics(z); prob.tail = 1.0
    tl = float(d['tail']) if 'tail' in d else 0.0
    print(f"{path}: fitted with tail weight {tl}; |F| without tail rows {dn['Fnorm']:.4e} (Fmax {dn['Fmax']:.2e}), with tail rows {dd['Fnorm']:.4e}; Ra/RG max {dn['Ra_max']:.3f}/{dn['RG_max']:.3f}; R1 max (t1=1e-5): a {dd['R1a_max']:.3e} G {dd['R1G_max']:.3e}", flush=True)
