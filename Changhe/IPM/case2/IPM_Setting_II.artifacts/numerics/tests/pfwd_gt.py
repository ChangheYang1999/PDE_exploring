"""Lead request (notes 23:55Z item 3a): Gt variation on a saved forward state.  python3 tests/pfwd_gt.py state.npz [lr0=-9] [nA=512]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_fp import FixedPoint, basis
torch.set_default_dtype(torch.float64)
fn = sys.argv[1]; opt = dict(lr0=-9.0, nA=512)
for s_ in sys.argv[2:]:
    k, v = s_.split('='); opt[k] = int(v) if k == 'nA' else float(v)
d = np.load(fn); g = torch.tensor(d['g'], device='cuda'); lr = d['lr']; a = json.loads(str(d['args'])); p = a['p']
par = a.get('par', [0, 0, 0, 0])
if isinstance(par, str): par = [float(v) for v in par.split(':')]
if not isinstance(par, list): par = [0.0]
Nr, Nth = g.shape
FP = FixedPoint(p, len(par), Nr=Nr, Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), lr0=opt['lr0'], nA=opt['nA'])
S = FP.S; rho = S.r[:, None] ** p * g; Wr, Wt = S.velocity(rho); dg = S.diagnostics(g, Wr, Wt, krings=(20,))
m1 = 1 / p - dg['c_moment']; ang = math.radians(dg['ring20']['e1_deg']); e1 = (math.cos(ang), math.sin(ang))
T, u0, w0, th0, it = FP.trace(Wr, Wt, e1)
A = FP.Afun(par)(FP.thA) if a.get('kind') == 'expf' else torch.tensor(np.interp(FP.thA.cpu().numpy(), S.th.cpu().numpy(), g[-1].cpu().numpy(), period=2 * math.pi), device='cuda')
logGt = torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T
logG = torch.log(torch.clamp(A, min=1e-300)) - (1 / m1) * torch.log(torch.clamp(u0.abs(), min=1e-300)) - T
w = A / A.max(); mean = float((w * logGt).sum() / w.sum()); dev_ = logGt - mean
sel = w > 1e-2
print("state %s p=%g m1(moment)=%.5f e1=%.2f deg; tracer: %d steps, lr0=%g, nA=%d" % (fn, p, m1, dg['ring20']['e1_deg'], it, opt['lr0'], opt['nA']))
print("log Gt (A-weighted): std %.4f, range on A > 1%%: [%.4f, %.4f] -> Gt max/min = %.3f" % (float(torch.sqrt((w * dev_ ** 2).sum() / w.sum())), float(dev_[sel].min()), float(dev_[sel].max()), math.exp(float(dev_[sel].max() - dev_[sel].min()))))
lG = logG - float((w * logG).sum() / w.sum())
print("log G  (exponent 1/m1 = %.4f): range on A > 1%%: [%.4f, %.4f] -> G max/min = %.3f" % (1 / m1, float(lG[sel].min()), float(lG[sel].max()), math.exp(float(lG[sel].max() - lG[sel].min()))))
thA = FP.thA.cpu().numpy(); dv = dev_.cpu().numpy(); th0n = th0.cpu().numpy() % (2 * math.pi); Tn = T.cpu().numpy()
print("theta_far(deg)  log Gt - mean   arrival theta0(deg)   T")
for deg in (0, 5, 10, 20, 30, 45, 60, 75, 85, 95, 105, 120, 150, 170, 180, 200, 240, 270, 300, 340, 355):
    k = int(round(deg / 360 * opt['nA'])) % opt['nA']
    print("  %5.1f   %8.4f   %7.2f   %6.3f" % (deg, dv[k], math.degrees(th0n[k]), Tn[k]))
# projections on the x-even basis
for j in range(6):
    phi = basis(FP.thA, j)
    print("  projection on basis %d: %.5f" % (j + 1, float((w * dev_ * phi).sum() / w.sum())))
