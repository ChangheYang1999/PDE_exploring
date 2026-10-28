"""Evaluate rho~, grad rho~, U, V of the exact-join modal trial on a polar grid (float64, NUMERICAL only).
Writes field.npz with arrays on (t, theta), theta in [0, pi/2]."""
import sys, os, time
# Set ANALYSIS1_SRC to the numerics/src directory of a copy of the Analysis I artifacts.
SRC = os.environ.get('ANALYSIS1_SRC', 'IPM_Analysis_I.artifacts/numerics/src')
sys.path.insert(0, SRC)
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen
T = Trial(np.load(SRC + '/../data/trial_v2_h0.008.npz'))
G = TrialGreen(T); t0 = time.time(); G.build(); print('build %.1fs c=%.15f 3/k-1=%.15f' % (time.time()-t0, G.c, 3/G.k-1), flush=True)
cl = G.c_l
Nt = int(sys.argv[1]) if len(sys.argv) > 1 else 400
Nth = int(sys.argv[2]) if len(sys.argv) > 2 else 181
t = np.linspace(np.log(1e-3), np.log(1e5), Nt)
th = np.linspace(0, np.pi/2, Nth)
R, Rt = G.rho_modes(t)                       # (Nt, M+1), coefficient of sin((2j+1) th); Rt = r dR/dr
psi, dpsi = G.psi_at(t)                      # coefficient of sin(2n th), n = 1..Nf ; dpsi = d psi_n/dr
j = np.arange(R.shape[1]); n = G.n
S1 = np.sin((2*j[:, None]+1)*th[None, :]); C1 = np.cos((2*j[:, None]+1)*th[None, :])
S2 = np.sin(2*n[:, None]*th[None, :]); C2 = np.cos(2*n[:, None]*th[None, :])
r = np.exp(t)[:, None]
rho = R @ S1; rho_r = (Rt @ S1)/r; rho_th = (R*(2*j+1)) @ C1
ps = psi @ S2; ps_r = dpsi @ S2; ps_th = (psi*2*n) @ C2
c, s = np.cos(th)[None, :], np.sin(th)[None, :]
rho_x = c*rho_r - s*rho_th/r; rho_y = s*rho_r + c*rho_th/r
ps_x = c*ps_r - s*ps_th/r; ps_y = s*ps_r + c*ps_th/r
U1, U2 = -ps_y, ps_x
x, y = r*c, r*s
V1, V2 = cl*x + U1, cl*y + U2
np.savez('field.npz', t=t, th=th, rho=rho, rho_x=rho_x, rho_y=rho_y, U1=U1, U2=U2, V1=V1, V2=V2, cl=cl, c=G.c)
print('done %.1fs' % (time.time()-t0))
