"""V47: test of the lead's high-frequency symbol of the Gt residual (team notes 00:39Z item 2, explore/hfsym.py not used).
Own derivation: for delta log A = h cos(k theta) at r = L the leading-order response is a stripe pattern along the orbits,
delta rho = rho q, whose velocity is delta W = alpha V with alpha = -rho V_2 q/|V|^2 (tangent to the orbits; order 0 in k),
so V.grad q = (rho V_2/|V|^2) q, q = h cos(k theta_exit) e^{-Q_X}, Q_X = int_X^exit rho V_2/|V|^2 dtau, and the orbits are
only re-timed: delta T = h cos(k theta)(1 - e^{-Q}), Q = Q at the node. Hence
    delta log Gt = s(theta) delta log A,  s = 1 - 2 m1 (1 - e^{-Q});   delta log G = e^{-Q} delta log A   (delta m1 neglected).
This script: base state and the two perturbed states (datum A e^{+-h cos k th}, solved independently with tests/fs_run.py),
own backward-orbit tracer (as tests/v43_gfix.py) with Q accumulated along the base orbits, central difference of log Gt and log G
over +-h, compared with s h cos(k th) and e^{-Q} h cos(k th).
Usage: python3 tests/v47_hfsym.py BASE PLUS MINUS p k h [ne] [tstop] [nstep]."""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fb, fpl, fmi = sys.argv[1], sys.argv[2], sys.argv[3]
p, k, h = float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
ne = int(sys.argv[7]) if len(sys.argv) > 7 else 2000             # divisible by k for the window fits
tstop = float(sys.argv[8]) if len(sys.argv) > 8 else -9.0
nstep = int(sys.argv[9]) if len(sys.argv) > 9 else 2000
db = np.load(fb, allow_pickle=True)
args = json.loads(str(db['args']))
r0 = db['r']; nt = len(db['th'])
tmin, tmax = float(args.get('tmin', -12)), float(args.get('tmax', 10))
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), r0), 'grid mismatch'
the = (torch.arange(ne, dtype=DT, device='cuda') + 0.5)*(2*math.pi/ne)
A0 = torch.cos(the)**2

def back(au, bu, qu, th_exit):
    """RK4 in t from tmax to tstop: d th/dt = beta/alpha, dT/dt = -1/alpha, dQ/dt = -(rho/r)(alpha sin + beta cos)/((alpha^2 + beta^2) alpha)."""
    hh = (tstop - F.tmax)/nstep
    th = th_exit.clone(); T = torch.zeros_like(th); Q = torch.zeros_like(th); t = torch.full_like(th, F.tmax)
    def fr(t, th):
        a = F.interp(au, t, th); b = F.interp(bu, t, th); q = F.interp(qu, t, th)                       # rho/r
        return b/a, -1.0/a, -q*(a*torch.sin(th) + b*torch.cos(th))/((a*a + b*b)*a)
    for n in range(nstep):
        k1 = fr(t, th); k2 = fr(t + hh/2, th + hh/2*k1[0]); k3 = fr(t + hh/2, th + hh/2*k2[0]); k4 = fr(t + hh, th + hh*k3[0])
        th = th + hh/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        T = T + hh/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        Q = Q + hh/6*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
        t = t + hh
    return th, T, Q

def state(fn, sgn):
    d = np.load(fn, allow_pickle=True)
    assert np.allclose(d['r'], r0) and abs(float(d['p']) - p) < 1e-12
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
    nd = F.node(rho); m1 = nd['m1']; e1 = math.radians(nd['e1_deg'])
    alpha, beta, _, _ = F.fields(rho)
    au = F.Imat @ alpha; bu = F.Imat @ beta; qu = F.Imat @ (rho/F.R)
    th0, T, Q = back(au, bu, qu, the)
    u0 = math.exp(tstop)*torch.cos(th0 - e1)
    logXi = torch.log(torch.abs(u0)) + m1*T
    logA = torch.log(A0) + sgn*h*torch.cos(k*the)
    return dict(m1=m1, e1=nd['e1_deg'], logXi=logXi, T=T, Q=Q, th0=th0, logGt=logA - 2*logXi, logG=logA - logXi/m1)

B = state(fb, 0.0); P = state(fpl, 1.0); M = state(fmi, -1.0)
m1 = B['m1']; Q = B['Q']; eQ = torch.exp(-Q)
s = 1 - 2*m1*(1 - eQ)
pert = h*torch.cos(k*the)
dGt = (P['logGt'] - M['logGt'])/2; dG = (P['logG'] - M['logG'])/2; dXi = (P['logXi'] - M['logXi'])/2
dm1 = (P['m1'] - M['m1'])/2
predGt = s*pert; predG = eQ*pert; predXi = m1*(1 - eQ)*pert
msk = A0 > 1e-2
def rel(x, y):
    return float(torch.sqrt(((x - y)[msk]**2).sum()/(y[msk]**2).sum()))
out = dict(base=fb.split('/')[-1], k=k, h=h, ne=ne, tstop=tstop, nstep=nstep, m1_base=round(m1, 6), m1_plus=round(P['m1'], 6),
           m1_minus=round(M['m1'], 6), dm1_over_h=round(dm1/h, 5),
           Q_range=[round(float(Q[msk].min()), 4), round(float(Q[msk].max()), 4)], s_range=[round(float(s[msk].min()), 4), round(float(s[msk].max()), 4)],
           relerr_logGt=round(rel(dGt, predGt), 4), relerr_logG=round(rel(dG, predG), 4), relerr_logXi=round(rel(dXi, predXi), 4),
           relerr_logGt_with_dm1T=round(rel(dGt, predGt - 2*dm1*B['T']), 4),
           size_dGt_over_pert=round(float(torch.sqrt((dGt[msk]**2).sum()/(pert[msk]**2).sum())), 4))
print(json.dumps(out), flush=True)
# windowed symbol estimate: <dGt cos(k th)>/<h cos^2(k th)> over one period, vs <s> on the window
per = ne//k
rows = []
for j in range(k):
    sl = slice(j*per, (j + 1)*per)
    c = torch.cos(k*the[sl])
    if float(A0[sl].min()) < 1e-2:
        continue
    meas = float((dGt[sl]*c).sum()/(h*(c*c).sum())); measG = float((dG[sl]*c).sum()/(h*(c*c).sum()))
    rows.append((round(math.degrees(float(the[sl].mean())), 1), round(float(Q[sl].mean()), 4), round(float(s[sl].mean()), 4), round(meas, 4),
                 round(float(eQ[sl].mean()), 4), round(measG, 4)))
print('windows (theta_deg, Q, s_pred, s_meas_Gt, eQ_pred, eQ_meas_G):', json.dumps(rows), flush=True)
tn = lambda x: x.cpu().numpy()
np.savez('runs/v47_hfsym_k%d.npz' % k, the=tn(the), dGt=tn(dGt), dG=tn(dG), dXi=tn(dXi), dm1=dm1, m1=m1, Q=tn(Q), T=tn(B['T']),
         Tp=tn(P['T']), Tm=tn(M['T']), th0=tn(B['th0']), th0p=tn(P['th0']), th0m=tn(M['th0']), logXi=tn(B['logXi']), A0=tn(A0), h=h, k=k)
