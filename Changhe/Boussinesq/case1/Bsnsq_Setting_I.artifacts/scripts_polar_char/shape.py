"""Shape measures of an Omega-basis state (solve_gn npz), authors' 18:55Z item 3: a0; x half-width x* of Theta_y(x,0); y at which
W2(0,y)/y reaches 2; core radius below which |W - DW(0) X| < 1e-2 |X| (sampled on 45 deg and both axes); radius of max |Omega|
(polar max over angles of max_phi |Omega(r, phi)|); plus objective/residual data from the run history."""
import sys, json, math, torch, numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs, radial_profiles, fields_at
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); device = dev(); beta = P.beta
r = torch.logspace(-3, 6, 9001, dtype=DT, device=device) * P.L
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
th = torch.tensor([0.0, math.pi / 4, math.pi / 2], dtype=DT, device=device)
F = fields_at(prof, r, th, beta, NT, NO)
a0 = float(F['Th_y'][0, 0]) if False else None
m = torch.tensor([2 * n + 1 for n in range(NT)], dtype=DT, device=device); tau = (m[:, None] * prof['f']).sum(0) / r   # Theta_y(x,0)
a0 = float(tau[0]); idx = torch.nonzero(tau < a0 / 2); xstar = float(r[int(idx[0])]) if idx.numel() else float('nan')
w2y = F['W2_y'][:, 2]   # W2/y on the y-axis
idx2 = torch.nonzero(w2y >= 2.0); y2 = float(r[int(idx2[0])]) if idx2.numel() else float('nan')
# core: |W - DW(0) X| / |X| with DW(0) = diag(beta+2, beta-2)
dev_core = []
for j, thj in enumerate(th):
    X, Y = F['X'][:, j], F['Y'][:, j]
    d = torch.sqrt((F['W1'][:, j] - (beta + 2) * X) ** 2 + (F['W2'][:, j] - (beta - 2) * Y) ** 2) / r
    dev_core.append(d)
dev_core = torch.stack(dev_core).max(0).values
idx3 = torch.nonzero(dev_core > 1e-2); rcore = float(r[int(idx3[0])]) if idx3.numel() else float('inf')
# radius of max |Omega| over a fine angular grid
thf = torch.linspace(0, math.pi / 2, 181, dtype=DT, device=device)
prof_f = {k: (v[:, ::10] if torch.is_tensor(v) else v) for k, v in prof.items()}
Ff = fields_at(prof_f, r[::10], thf, beta, NT, NO)
om = Ff['Om'].abs().max(1).values; rmax_om = float(r[::10][int(om.argmax())]); ommax = float(om.max())
d = np.load(sys.argv[1], allow_pickle=True); h = json.loads(str(d['hist']))[-1]
out = dict(file=sys.argv[1], beta=beta, a0=a0, xstar=xstar, y_W2y_eq_2=y2, r_core_1em2=rcore, r_maxOmega=rmax_om, maxOmega=ommax, b1=h.get('b1'), obj=h.get('obj'), maxnormT=h.get('maxnormT'), maxnormO=h.get('maxnormO'), it=h.get('it'))
print(json.dumps(out))
