# V108 (4): split of the odd delta log G of v0 = odd(rho cos th) into travel time and log|u0| at t_in -10, -12, -13.5. CPU.
"""V108 (lead team notes 10:45Z, revised V102b request (4)): the x-odd orbit-matching residual M_rho v of a perturbation v
at fixed datum, in my own code. For a state rho with velocity V[rho] (code/fwdstat.py, anchored) and node matrix DV(0) (weak
eigenvalue m1, unit eigenvector e1; DV(0) is symmetric), every exit point (r_max, phi_k), phi_k on the angle grid, is traced
BACKWARD (arclength orbits in (t, th), step hs, final step in t onto t_in) to log r = t_in, giving the backward travel time
T(phi) and the stop point X0. The weak eigenfunction Xi (V.grad Xi = m1 Xi, grad Xi(0) = e1) is Xi(exit) = e^{m1 T} X0.e1 to
leading order, and rho / |Xi|^{1/m1} is constant on orbits, so the matching function is
    log G(phi) = log A(phi) + p t_max - (1/m1) log |X0.e1| - T(phi)
(at m1 = 1/2 this is the lead's log Gt up to a constant). A profile needs G constant on the support. For x-odd v:
    M_rho v = odd part in phi of (log G[rho* + eps v] - log G[rho* - eps v]) / (2 eps)        (datum A fixed)
reported as the RMS and max over |cos phi| > 0.05 and > 0.3, for t_in = -8, -10, -12 (independence check), next to the same
for comparison vectors of equal norm (<f, g> = sum f g / r^(2p), as the Arnoldi): v0 = odd(rho* cos th) (the Arnoldi start),
odd(d_th rho*), and two random smooth x-odd vectors. Also log G of rho* itself (its spread on the support) and, per vector,
the change of b = psi_yy(0) and of e1 (deg) per eps. CPU, one thread.
Usage: python3 tests/v108d_match.py MODE.npz [er (1e-4)] [hs (0.03)]"""
import sys, math, json, time, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = 'runs/v108_mode_v74_a2-1.1_c07.npz'; er = 1e-4; hs = 0.03
md = np.load(fn, allow_pickle=True); margs = json.loads(str(md['args']))
d = np.load(margs['source'], allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p'])
par = [float(v) for v in args['par'].split(':')]
def A(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
nt = len(d['th']); t0w = time.time()
F = FwdStat(p, A, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)), q=8, nt=nt,
            dti=0.01, nstep=800, dev='cpu')
assert np.allclose(F.r.numpy(), d['r']) and np.allclose(md['r'], d['r'])
rho = torch.tensor(d['rho'], dtype=DT); Rp = F.R**p
xi = torch.tensor((nt//2 - np.arange(nt)) % nt)
odd = lambda f: 0.5*(f - f[:, xi])
nrm = lambda f: math.sqrt(float((f*f/Rp**2).sum()))
scale = float((rho/Rp).abs().max())
phi = F.th.clone(); Aphi = A(phi.numpy()); sup05 = np.abs(np.cos(phi.numpy())) > 0.05; sup3 = np.abs(np.cos(phi.numpy())) > 0.3
oddphi = lambda g: 0.5*(g - g[xi.numpy()])


def back(al, be, t_in, nmax=20000):
    au = F.Imat @ al; bu = F.Imat @ be
    t = torch.full_like(phi, F.tmax); th = phi.clone(); s = torch.zeros_like(phi); done = torch.zeros_like(phi, dtype=torch.bool)
    def f(t, th):
        a = F.interp(au, t, th); b = F.interp(bu, t, th); w = torch.sqrt(a*a + b*b)
        return -a/w, -b/w, 1.0/w
    def ft(t, th):
        a = F.interp(au, t, th); b = F.interp(bu, t, th)
        return b/a, 1.0/a
    h = hs
    for n in range(nmax):
        idx = torch.nonzero(~done).squeeze(1)
        if idx.numel() == 0:
            break
        tt, hh, ss = t[idx], th[idx], s[idx]
        k1 = f(tt, hh); k2 = f(tt + h/2*k1[0], hh + h/2*k1[1]); k3 = f(tt + h/2*k2[0], hh + h/2*k2[1]); k4 = f(tt + h*k3[0], hh + h*k3[1])
        tn = tt + h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); hn = hh + h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        sn = ss + h/6*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
        cross = tn <= t_in
        if bool(cross.any()):
            ht = t_in - tt[cross]; tc = tt[cross]; thc = hh[cross]          # ht < 0: step in t down to t_in
            q1 = ft(tc, thc); q2 = ft(tc + ht/2, thc + ht/2*q1[0]); q3 = ft(tc + ht/2, thc + ht/2*q2[0]); q4 = ft(tc + ht, thc + ht*q3[0])
            hn[cross] = thc + ht/6*(q1[0] + 2*q2[0] + 2*q3[0] + q4[0])
            sn[cross] = ss[cross] - ht/6*(q1[1] + 2*q2[1] + 2*q3[1] + q4[1])
            tn[cross] = t_in
        t[idx] = tn; th[idx] = hn; s[idx] = sn; done[idx] = cross
    return th, s, int((~done).sum())



v = odd(rho*torch.cos(F.TH)); v = v/nrm(v); eps = er*scale
res = {}
for sg in (1, -1):
    R = rho + sg*eps*v
    al, be, _, _ = F.fields(R); nd = F.node(R); e = math.radians(nd['e1_deg'])
    for tin in (-10.0, -12.0, -13.5):
        th0, T, nb = back(al, be, tin)
        u0 = math.exp(tin)*(torch.cos(th0)*math.cos(e) + torch.sin(th0)*math.sin(e))
        res[(sg, tin)] = (T.numpy(), np.log(np.abs(u0.numpy())), th0.numpy(), nd['m1'])
m1 = res[(1, -10.0)][3]
for tin in (-10.0, -12.0, -13.5):
    dT = oddphi((res[(1, tin)][0] - res[(-1, tin)][0])/(2*eps)); du = oddphi((res[(1, tin)][1] - res[(-1, tin)][1])/(2*eps))
    dth = (np.remainder(res[(1, tin)][2] - res[(-1, tin)][2] + np.pi, 2*np.pi) - np.pi)/(2*eps)
    print('tin', tin, 'rms dT %.4g' % np.sqrt(np.mean(dT[sup05]**2)), 'rms dlog|u0|/m1 %.4g' % np.sqrt(np.mean((du/m1)[sup05]**2)),
          'rms total %.4g' % np.sqrt(np.mean((-du/m1 - dT)[sup05]**2)), 'max |d th0| %.3g' % np.abs(dth[sup05]).max())
    for k in (20, 60, 100, 200):
        print('   phi %.1f dT %.4g dlogu0/m1 %.4g th0 %.4f' % (np.degrees(phi[k].item()), dT[k], du[k]/m1, res[(1, tin)][2][k] % (2*np.pi)))
