"""V47: localisation of the symbol defect. Along the base backward orbits (exit angle grid ne), with the measured perturbation
delta = (plus - minus)/2 of fwdstat states (datum log A +- h cos k th):
  a_meas = deltaV.V/|V|^2 (tangential re-timing rate), a_sym = -V_2 delta rho/|V|^2 (local stripe symbol applied to the MEASURED
  delta rho), a_pred = -rho V_2 q_pred/|V|^2 with q_pred = h cos(k th_exit) e^{-Q_X}; their integrals dT_x = -int a_x dtau;
  n_meas = normal drift rate (deltaV x V)/|V|^2; q_meas = delta rho/rho vs q_pred at a few radii, with the angular spread (deg) of the window orbits there.
Projections on cos(k th_exit) per period window (units of h). Usage: python3 tests/v47_hfloc.py BASE PLUS MINUS p k h [ne] [tstop] [nstep]"""
import sys, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fb, fpl, fmi = sys.argv[1], sys.argv[2], sys.argv[3]
p, k, h = float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
ne = int(sys.argv[7]) if len(sys.argv) > 7 else 2000
tstop = float(sys.argv[8]) if len(sys.argv) > 8 else -9.0
nstep = int(sys.argv[9]) if len(sys.argv) > 9 else 2000
db = np.load(fb, allow_pickle=True); args = json.loads(str(db['args'])); r0 = db['r']; nt = len(db['th'])
F = FwdStat(p, lambda t: np.cos(t)**2, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)),
            q=8, nt=nt, dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), r0)
def ld(fn):
    d = np.load(fn, allow_pickle=True); assert np.allclose(d['r'], r0); return torch.tensor(d['rho'], dtype=DT, device='cuda')
rB, rP, rM = ld(fb), ld(fpl), ld(fmi)
aB, bB, _, _ = F.fields(rB); aP, bP, _, _ = F.fields(rP); aM, bM, _, _ = F.fields(rM)
I = lambda X: F.Imat @ X
U = dict(a=I(aB), b=I(bB), da=I((aP - aM)/2), db=I((bP - bM)/2), rho=I(rB), drho=I((rP - rM)/2), rr=I(rB/F.R))
the = (torch.arange(ne, dtype=DT, device='cuda') + 0.5)*(2*math.pi/ne)
cosk = torch.cos(k*the)
hh = (tstop - F.tmax)/nstep
samples = [8.0, 4.0, 0.0, -2.0, -4.0, -6.0]
def rates(t, th, Qc):
    g = {key: F.interp(v, t, th) for key, v in U.items()}
    a, b = g['a'], g['b']; n2 = a*a + b*b
    v2 = a*torch.sin(th) + b*torch.cos(th)                                   # V_2/r
    dtau = -1.0/a                                                            # d tau / d t (t decreasing: positive increments)
    f = g['rr']*v2/n2                                                        # rho V_2/|V|^2
    am = (g['da']*a + g['db']*b)/n2                                          # deltaV.V/|V|^2
    asym = -g['drho']*v2/(n2*torch.exp(t))                                   # -V_2 delta rho/|V|^2 (V_2 = r v2, |V|^2 = r^2 n2)
    qpred = h*cosk*torch.exp(-Qc)
    apred = -f*qpred
    nm = (g['db']*a - g['da']*b)/n2                                          # normal drift rate
    return dict(th=b/a, Q=f*dtau, Im=-am*dtau, Is=-asym*dtau, Ip=-apred*dtau, In=nm*dtau, absf=f.abs()*dtau), g
th = the.clone(); t = torch.full_like(th, F.tmax)
acc = {key: torch.zeros_like(th) for key in ('Q', 'Im', 'Is', 'Ip', 'In', 'absf')}
qs = {}
for n in range(nstep):
    # RK2 (midpoint) is enough for the diagnostics; theta and all integrals advanced together
    r1, g1 = rates(t, th, acc['Q'])
    for s in samples:
        if abs(float(t[0]) - s) < abs(hh)/2:
            qs[s] = ((g1['drho']/g1['rho']).clone(), (h*cosk*torch.exp(-acc['Q'])).clone(), th.clone())
    thm = th + hh/2*r1['th']; Qm = acc['Q'] + hh/2*r1['Q']
    r2, _ = rates(t + hh/2, thm, Qm)
    th = th + hh*r2['th']
    for key in acc:
        acc[key] = acc[key] + hh*r2[key]
    t = t + hh
per = ne//k; A0 = torch.cos(the)**2
def pj(f, sl):
    c = cosk[sl]; return float((f[sl]*c).sum()/(h*(c*c).sum()))
rows = []
for j in range(k):
    sl = slice(j*per, (j + 1)*per)
    if float(A0[sl].min()) < 1e-2: continue
    row = dict(th=round(math.degrees(float(the[sl].mean())), 1), Q=round(float(acc['Q'][sl].mean()), 3),
               dT_pred=round(pj(acc['Ip'], sl), 4), dT_sym=round(pj(acc['Is'], sl), 4), dT_meas_tan=round(pj(acc['Im'], sl), 4),
               dth_normal=round(pj(acc['In'], sl), 4))
    for s in sorted(qs):
        qm, qp, ths = qs[s]
        sp = torch.remainder(ths[sl] - ths[sl].mean() + math.pi, 2*math.pi) - math.pi
        row['q_t%g' % s] = [round(pj(qm, sl), 4), round(pj(qp, sl), 4), round(math.degrees(float(sp.max() - sp.min())), 4)]
    rows.append(row)
print(json.dumps(dict(k=k, h=h, ne=ne, tstop=tstop, nstep=nstep)))
for r_ in rows:
    print(json.dumps(r_))
