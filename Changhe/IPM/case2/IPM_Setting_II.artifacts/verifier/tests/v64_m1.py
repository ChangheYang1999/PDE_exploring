"""V64b: node strain m1 of an imported state: (i) own moment formula (code/charsolve.moments) split by t band (how much of
c = psi_xy(0) comes from each band, and the band integrand at the inner end); (ii) ring fits of the own velocity
V = M X on rings r = e^t (least squares of alpha = e_r.M e_r, beta = e_th.M e_r over the angles), eigenvalues of the
symmetric part, as the lead's pforward.node_matrix does at ring 8 (t = -11.73).  Usage: python3 tests/v64_m1.py OWN.npz"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
d = np.load(sys.argv[1], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt,
            dti=0.01, nstep=800)
rho = torch.tensor(d['rho'], dtype=DT, device='cuda'); S = F.S
nd = F.node(rho)
rm3 = S.rho_modes(rho)[:, 3]
w = S.w; r = S.r
contrib = (-2*(w*rm3/r**2).imag).cpu().numpy()       # contributions to c by node
t = np.log(r.cpu().numpy())
tail = float(-2*(torch.dot(S.ext_last.to(torch.complex128), rm3[-F.q:])/(S.L*(1 - p))).imag)
out = dict(state=sys.argv[1].split('/')[-1], m1_moment=round(nd['m1'], 5), m2_moment=round(nd['m2'], 5), c=round(nd['c'], 5),
           b=round(nd['b'], 6), c_tail_beyond_L=round(tail, 5))
bands = {}
for a_, b_ in ((-12, -11), (-11, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10)):
    m = (t >= a_) & (t < b_); bands['%g..%g' % (a_, b_)] = round(float(contrib[m].sum()), 5)
out['c_by_band'] = bands
dcdt = contrib/(w.cpu().numpy()/r.cpu().numpy())     # dc/dt at each node
i0 = np.argmin(np.abs(t - (-11.9))); out['dc_dt_at_t-11.9'] = round(float(dcdt[i0]), 5)
al, be, _, _ = F.fields(rho); al = al.cpu().numpy(); be = be.cpu().numpy(); th = F.th.cpu().numpy()
c2, s2 = np.cos(2*th), np.sin(2*th)
# alpha = (M11+M22)/2 + (M11-M22)/2 cos2 + (M12+M21)/2 sin2 ; beta = (M21-M12)/2 - (M11-M22)/2 sin2 + (M12+M21)/2 cos2
A = np.zeros((2*nt, 4)); A[:nt] = np.stack([0.5 + 0.5*c2, 0.5*s2, 0.5*s2, 0.5 - 0.5*c2], 1)
A[nt:] = np.stack([-0.5*s2, -0.5 + 0.5*c2, 0.5 + 0.5*c2, 0.5*s2], 1)
rings = []
for tv in (-11.73, -11, -10, -9, -8, -7, -6):
    i = int(np.argmin(np.abs(t - tv)))
    M = np.linalg.lstsq(A, np.concatenate([al[i], be[i]]), rcond=None)[0].reshape(2, 2)
    ev = np.linalg.eigvalsh(0.5*(M + M.T))
    resid = np.linalg.norm(A @ M.ravel() - np.concatenate([al[i], be[i]]))/math.sqrt(2*nt)
    rings.append(dict(t=round(float(t[i]), 2), m1=round(float(ev[0]), 4), m2=round(float(ev[1]), 4), fit_rms=round(float(resid), 3)))
out['ring_fits'] = rings
print(json.dumps(out, indent=1), flush=True)
