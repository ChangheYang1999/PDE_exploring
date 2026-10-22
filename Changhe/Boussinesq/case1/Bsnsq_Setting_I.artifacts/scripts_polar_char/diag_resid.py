"""Where is the residual largest? Print the top normalized-residual locations and the y-axis ODE profile."""
import sys, math, torch, numpy as np
sys.path.insert(0, '.')
from polarlib import *; from evalfields import *
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); beta = P.beta; device = dev()
qmax = P.q_of_u(torch.tensor(1e6, dtype=DT)).item()
q = (torch.arange(600, dtype=DT, device=device) + 0.5) / 600 * qmax
r = P.u_of_q(q) * P.L
th = (torch.arange(90, dtype=DT, device=device) + 0.5) / 90 * (math.pi / 2)
prof = radial_profiles(P, cT, cO, r, NT, NO, K)
F = fields_at(prof, r, th, beta, NT, NO)
ratT = (F['RT'].abs() / F['NT']); ratO = (F['RO'].abs() / F['NO'])
R = r[:, None].expand_as(ratT); TH = th[None, :].expand_as(ratT)
for name, rat in (('Theta', ratT), ('Omega', ratO)):
    v, idx = torch.topk(rat.reshape(-1), 12)
    print(name, 'top normalized residuals:')
    for vi, ii in zip(v.tolist(), idx.tolist()):
        print('   ratio=%.3e at r=%.4g theta=%.3f (deg %.1f)' % (vi, R.reshape(-1)[ii], TH.reshape(-1)[ii], TH.reshape(-1)[ii] * 180 / math.pi))
    # angular distribution of the max over r<10
    m = (R < 10)
    print('   max over r<10 per angle decile:', [float(rat[(R < 10) & (TH >= a) & (TH < a + math.pi / 20)].max()) for a in np.arange(0, math.pi / 2, math.pi / 20)])
    print('   max per radial decade:', [(lo, float(rat[(R >= lo) & (R < lo * 10)].max())) for lo in (1e-3, 1e-2, 1e-1, 1, 10, 100, 1e3, 1e4, 1e5) if ((R >= lo) & (R < lo * 10)).any()])
# y-axis ODE: V Theta0' - (beta-2) Theta0 with Theta0 = sum (-1)^n f_n, V = W2(0,y)
f = prof['f']; df = prof['df']; sgn = torch.tensor([(-1.0) ** n for n in range(NT)], dtype=DT, device=device)
Th0 = (sgn[:, None] * f).sum(0); dTh0 = (sgn[:, None] * df).sum(0)
psi = prof['psi']; dpsi = prof['dpsi']
# U2(0,y) = Psi_x at theta=pi/2: Psi_x = cos Psir - sin Psith/r -> -(1/r) sum 2n psi_n cos(n pi) = -sum 2n (-1)^n psi_n / r
U20 = -sum(2 * n * ((-1) ** n) * psi[n - 1] for n in range(1, NO + 1)) / r
V = beta * r + U20
res = V * dTh0 - (beta - 2) * Th0; nrm = (V * dTh0).abs() + (beta - 2) * Th0.abs()
rr = r.cpu().numpy()
print('y-axis: r, V/y, Theta0/y, |res|/norm')
for i in range(0, len(rr), 25):
    print('   %.4g  %.5f  %.5f  %.3e' % (rr[i], V[i] / r[i], Th0[i] / r[i], res[i].abs() / nrm[i]))
