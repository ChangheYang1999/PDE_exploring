"""Validate code/pfwd_diag.py on the saved N = 6 state against the lead's dsum.py numbers on the same npz
(lead 04:5xZ: Fp_minus_Fm 1.1115, twoL 0.4239, D_ax -0.6876, twoL_res17 0.4243, we_over_r_m6 0.2957, we_far_over_rp -0.1294)."""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd, datum
from pfwd_diag import core_term, axis_D, deep_trace_stats
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
fn = sys.argv[1] if len(sys.argv) > 1 else 'runs/pfwd/fp_p014N6_state.npz'
d = np.load(fn); a = json.loads(str(d['args'])); p = a['p']; par = a['par']
g = torch.tensor(d['g'], device='cuda'); lr = d['lr']; Nr, Nth = g.shape
FP = FixedPoint(p, len(par), Nr=Nr, Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), nA=1440, dt=0.01)
S = FP.S
rho = S.r[:, None] ** p * g
Wr, Wt = S.velocity(rho)
dg = S.diagnostics(g, Wr, Wt, krings=(20,))
core = core_term(S, rho)
m1_nc = 1 / p - dg['c_moment']; m1_c = 1 / p - dg['c_moment'] - core
print(json.dumps(dict(p=p, m1_nocore=round(m1_nc, 6), core=round(core, 6), m1_core=round(m1_c, 6), m1_ring20=dg['ring20']['m1'])))
A = FP.Afun(par)(S.th)
for m1 in (m1_nc, m1_c):
    ax = axis_D(S, g, Wr, p, m1, A=A)
    print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in ax.items() if k not in ('q_up', 'q_down')}))
    print('  q_up  ', ax['q_up']); print('  q_down', ax['q_down'])
Af = FP.Afun(par)(FP.thA)
for lr0 in (-9.0, -11.5, -11.9):
    st, lg = deep_trace_stats(FP, Wr, Wt, Af, m1_c, lr0=lr0)
    print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in st.items()}))
