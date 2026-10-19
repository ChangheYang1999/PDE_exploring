"""V43: independent node-coordinate check of a forward state (own backward-orbit tracer, own velocity code/charsolve.py via
code/fwdstat.py). referee result 13: rho = |xi|^gamma G(tau), gamma = 1/m1, tau = eta/|xi|^(m2/m1); along the orbit through the exit point
(L, theta), G = L^p A(theta)/|Xi(theta)|^gamma with Xi(theta) = far-field trace of the weak linearising coordinate:
Xi = u0 e^{m1 T}, u0 = X0.e1 at the inner stop r0 of the backward orbit (-V) from (L, theta), T = backward travel time.
Setting II needs m1 = 1/2 AND G constant (A = C |Xi|^2). Reported: log G and log Gt (exponent 2) statistics over exit angles,
for two inner stops (convergence of log|u0| + m1 T), plus a manufactured linear-flow self-test (Xi = L cos theta exactly).
Usage: python3 tests/v43_gfix.py FILE p kind par [nt] [ppu]  (kind expf: par = a1:a2:...)."""
import sys, math, json, numpy as np, torch
from scipy.interpolate import CubicSpline
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
f, p, kind = sys.argv[1], float(sys.argv[2]), sys.argv[3]
par = [float(v) for v in sys.argv[4].split(':')] if kind == 'expf' else float(sys.argv[4])
bump = None                                                # V52: zero-window bumps, read from the state's fs_run args (key bump)
cmode = 0.0                                                # V52(d): sin 3th cos^2 th compensator (fs_run key cmode)
def Afun(t):
    A0 = Afun0(t)*np.exp(cmode*np.sin(3*t)*np.cos(t)**2)
    if bump is None: return A0
    s = np.sin(t); bl, bu, w = bump
    return A0*np.exp(bl*np.exp(-(1 + s)/w) + bu*np.exp(-(1 - s)/w))
def Afun0(t):
    c, s = np.cos(t), np.sin(t)
    if kind == 'cos2': return c**2
    if kind == 'cosk': return np.abs(c)**par
    if kind == 'expsin3': return c**2*np.exp(-par*np.sin(3*t))
    if kind == 'expf':
        f = np.zeros_like(t)
        for j, aj in enumerate(par):
            n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
        return c**2*np.exp(f)
    raise ValueError(kind)
d = np.load(f, allow_pickle=True)
if 'args' in d.files and json.loads(str(d['args'])).get('bump'):
    bump = [float(v) for v in json.loads(str(d['args']))['bump'].split(':')]
if 'args' in d.files and json.loads(str(d['args'])).get('cmode'):
    cmode = float(json.loads(str(d['args']))['cmode'])
if 'g' in d.files:
    g0, lr0, th0 = d['g'], d['lr'], d['th']
else:
    p0 = float(d['p']); r0 = d['r']; th0 = d['th']; g0 = d['rho']/r0[:, None]**p0; lr0 = np.log(r0)
nt = int(sys.argv[5]) if len(sys.argv) > 5 else len(th0)
ppu = int(sys.argv[6]) if len(sys.argv) > 6 else 3
tmin, tmax = -12.0, float(lr0[-1])
F = FwdStat(p, Afun, tmin=tmin, tmax=tmax, ppu=ppu, q=8, nt=nt, dti=0.01, nstep=800)
rr = F.r.cpu().numpy(); lrr = np.log(rr); thn = F.th.cpu().numpy()
G = CubicSpline(lr0, g0, axis=0)(np.clip(lrr, lr0[0], lr0[-1]))
if len(th0) != len(thn) or not np.allclose(th0, thn):
    th_ext = np.concatenate([th0, [2*math.pi]]); G_ext = np.concatenate([G, G[:, :1]], 1)
    G = CubicSpline(th_ext, G_ext, axis=1, bc_type='periodic')(thn)
G[lrr < lr0[0]] = 0.0
rho = torch.tensor(rr[:, None]**p*G, dtype=DT, device='cuda')
nd = F.node(rho); m1, m2 = nd['m1'], nd['m2']; e1 = math.radians(nd['e1_deg'])

def back(au, bu, th_exit, tstop, nstep):
    """RK4 in t from tmax down to tstop: d th/dt = beta/alpha, dT/dt = -1/alpha (T = backward time >= 0)."""
    h = (tstop - F.tmax)/nstep
    th = th_exit.clone(); T = torch.zeros_like(th); t = torch.full_like(th, F.tmax)
    def fr(t, th):
        a = F.interp(au, t, th); b = F.interp(bu, t, th)
        return b/a, -1.0/a
    for n in range(nstep):
        k1t, k1s = fr(t, th); k2t, k2s = fr(t + h/2, th + h/2*k1t); k3t, k3s = fr(t + h/2, th + h/2*k2t); k4t, k4s = fr(t + h, th + h*k3t)
        th = th + h/6*(k1t + 2*k2t + 2*k3t + k4t); T = T + h/6*(k1s + 2*k2s + 2*k3s + k4s); t = t + h
    return th, T

# manufactured self-test: linear flow V = diag(a, b) X, Xi = L cos(theta) exactly
a_, b_ = 0.5, 3.5
TH = F.TH; au_t = (a_*torch.cos(F.TH)**2 + b_*torch.sin(F.TH)**2)[:1].expand(F.Nu, -1).contiguous()
bu_t = ((b_ - a_)*torch.sin(F.TH)*torch.cos(F.TH))[:1].expand(F.Nu, -1).contiguous()
the = torch.linspace(0.05, math.pi/2 - 0.3, 50, dtype=DT, device='cuda')
th0_, T_ = back(au_t, bu_t, the, -6.0, 1600)
logXi = math.log(math.exp(-6.0)) + torch.log(torch.abs(torch.cos(th0_))) + a_*T_
selftest = float((logXi - (F.tmax + torch.log(torch.cos(the)))).abs().max())

alpha, beta, _, _ = F.fields(rho)
au = F.Imat @ alpha; bu = F.Imat @ beta
ne = 2048
the = (torch.arange(ne, dtype=DT, device='cuda') + 0.5)*(2*math.pi/ne)
A = torch.tensor(Afun(the.cpu().numpy()), dtype=DT, device='cuda')
res = {}
for tstop, nstep in ((-6.0, 1600), (-9.0, 2000), (-9.0, 4000)):
    th0_, T_ = back(au, bu, the, tstop, nstep)
    u0 = math.exp(tstop)*torch.cos(th0_ - e1)
    logXi = torch.log(torch.abs(u0)) + m1*T_
    logG = p*F.tmax + torch.log(A) - logXi/m1
    logGt = p*F.tmax + torch.log(A) - 2*logXi
    w = A**2; w = w/w.sum()                                  # weight away from the zeros of A
    m = A > 1e-3*A.max()
    def st(x):
        mu = float((w*x).sum()); sd = float(torch.sqrt((w*(x - mu)**2).sum()))
        return dict(wmean=round(mu, 5), wstd=round(sd, 5), max_minus_min=round(float(x[m].max() - x[m].min()), 5))
    res['tstop%g_n%d' % (tstop, nstep)] = dict(logG=st(logG), logGt=st(logGt), max_angle_off_axis_deg=round(math.degrees(float(
        torch.abs(torch.sin(th0_ - e1)).max())), 4))
    if nstep == 2000:
        prof = [(round(math.degrees(float(the[k])), 2), round(float(A[k]), 5), round(float(logGt[k]), 5)) for k in range(0, ne, 64)]
        tn = lambda x: x.cpu().numpy()
        np.savez(f.replace('.npz', '_gfixprof.npz'), the=tn(the), A=tn(A), logGt=tn(logGt), logG=tn(logG), T=tn(T_), th0=tn(th0_),
                 m1=m1, m2=m2, p=p)
        # near the zeros of A (strong-axis traces), 1 deg spacing: log Gt minus its unweighted mean on |cos| > 0.05
        # (the lead's normalisation, notes 01:16Z/01:22Z); also the weak-axis exit value on the same scale
        mb = torch.abs(torch.cos(the)) > 0.05
        g0 = float(logGt[mb].mean())
        near = {'mean_cos>0.05': round(g0, 5)}
        for c0 in (0.0, 30.0, 60.0, 120.0, 180.0, 240.0, 300.0):
            k = int(round(math.radians(c0)/(2*math.pi/ne) - 0.5)) % ne
            near['%g' % c0] = round(float(logGt[k]) - g0, 4)
        for c0 in (90.0, 270.0):
            for dd in range(-20, 21):
                k = int(round(math.radians(c0 + dd)/(2*math.pi/ne) - 0.5)) % ne
                near['%g' % (c0 + dd)] = round(float(logGt[k]) - g0, 4)
        near['range_cos>0.05'] = round(float(logGt[mb].max() - logGt[mb].min()), 4)
print(json.dumps(dict(file=f.split('/')[-1], p=p, kind=kind, par=par, bump=bump, cmode=cmode, nt=nt, ppu=ppu, m1=round(m1, 6), m2=round(m2, 6),
                      e1_deg=round(nd['e1_deg'], 4), selftest_logXi_err=selftest, res=res)), flush=True)
print('profile (exit angle deg, A, log Gt):', json.dumps(prof))
print('near zeros (exit angle deg: log Gt - mean over |cos| > 0.05, tstop -9 n 2000):', json.dumps(near))
