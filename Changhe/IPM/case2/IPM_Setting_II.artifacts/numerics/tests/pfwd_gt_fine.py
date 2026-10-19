"""log Gt near the strong-axis traces (zeros of A) in 1-degree steps (lead request 01:22Z item 3). Usage: python3 tests/pfwd_gt_fine.py state.npz [nA=2880]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
fn = sys.argv[1]; nA = int(sys.argv[2].split('=')[1]) if len(sys.argv) > 2 else 2880
d = np.load(fn); g = torch.tensor(d['g'], device='cuda'); lr = d['lr']; a = json.loads(str(d['args'])); p = a['p']; par = a['par']
if isinstance(par, str): par = [float(v) for v in par.split(':')]
Nr, Nth = g.shape
FP = FixedPoint(p, len(par), Nr=Nr, Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), lr0=-9.0, nA=nA, dt=0.01)
S = FP.S; rho = S.r[:, None] ** p * g; Wr, Wt = S.velocity(rho); dg = S.diagnostics(g, Wr, Wt, krings=(20,))
m1 = 1 / p - dg['c_moment']
T, u0, w0, th0, it = FP.trace(Wr, Wt, (1.0, 0.0))
A = FP.Afun(par)(FP.thA)
logGt = (torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T).cpu().numpy()
thA = np.degrees(FP.thA.cpu().numpy()); w = np.abs(np.cos(np.radians(thA))) > 0.05
mean = logGt[w].mean(); dv = logGt - mean
print("%s: p=%.5f m1(moment)=%.5f; log Gt - mean(|cos|>0.05); nA=%d" % (fn.split('/')[-1], p, m1, nA))
def at(deg): return dv[int(round(deg / 360 * nA)) % nA]
print("bulk: " + ' '.join('%g:%.3f' % (dg_, at(dg_)) for dg_ in (0, 20, 40, 60, 70, 75, 180, 200, 220, 240, 245, 250)))
print("upper zero 80..100: " + ' '.join('%g:%.3f' % (dg_, at(dg_)) for dg_ in range(80, 101, 1)))
print("lower zero 250..290: " + ' '.join('%g:%.3f' % (dg_, at(dg_)) for dg_ in range(250, 291, 1)))
sel = w & (np.abs(np.cos(np.radians(thA))) > 0.02)
print("extremes on |cos| > 0.02: min %.3f at %.1f deg, max %.3f at %.1f deg; G(-inf)/G(0) ~ exp(%.3f), G(+inf)/G(0) ~ exp(%.3f)" % (dv[sel].min(), thA[sel][dv[sel].argmin()], dv[sel].max(), thA[sel][dv[sel].argmax()], at(271) - at(0), at(89) - at(0)))
