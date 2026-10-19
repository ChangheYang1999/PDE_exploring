# V108 (4): alpha, beta of the -1.1 state on the axes and their odd derivative along v0, by log r (linear node regime check). CPU.
import sys, math, json, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
d = np.load('runs/v74_a2-1.1_c07.npz', allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=0.01, nstep=800, dev='cpu')
rho = torch.tensor(d['rho'], dtype=DT); Rp = F.R**p
xi = torch.tensor((nt//2 - np.arange(nt)) % nt); odd = lambda f: 0.5*(f - f[:, xi]); nrm = lambda f: math.sqrt(float((f*f/Rp**2).sum()))
v = odd(rho*torch.cos(F.TH)); v = v/nrm(v); eps = 1e-4*float((rho/Rp).abs().max())
out = {}
for sgn in (1, -1):
    al, be, W1, W2 = F.fields(rho + sgn*eps*v); out[sgn] = (al.numpy(), be.numpy(), F.node(rho + sgn*eps*v))
t = np.log(F.r.numpy()); deg = np.degrees(F.th.numpy())
print('m1', out[1][2]['m1'], out[-1][2]['m1'], 'b', out[1][2]['b'], out[-1][2]['b'], 'e1', out[1][2]['e1_deg'], out[-1][2]['e1_deg'])
for tt in (-13.5, -12, -10, -8, -6):
    i = int(np.argmin(np.abs(t - tt)))
    for j in (0, nt//2, nt//4):
        da = (out[1][0][i, j] - out[-1][0][i, j])/(2*eps); db = (out[1][1][i, j] - out[-1][1][i, j])/(2*eps)
        print('t %.2f deg %.1f alpha %.6f dalpha/eps %.4g dbeta/eps %.4g' % (t[i], deg[j], out[1][0][i, j], da, db))
