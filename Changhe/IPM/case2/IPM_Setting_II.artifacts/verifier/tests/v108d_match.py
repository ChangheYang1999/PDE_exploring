"""V108 (lead team notes 10:45Z, revised V102b request (4)): the x-odd orbit-matching residual M_rho v of a perturbation v
at fixed datum, in my own code. For a state rho with velocity V[rho] (code/fwdstat.py, anchored) and node matrix DV(0) (weak
eigenvalue m1, unit eigenvector e1; DV(0) is symmetric), every exit point (r_max, phi_k), phi_k on the angle grid, is traced
BACKWARD (arclength orbits in (t, th), step hs, final step in t onto t_in) to log r = t_in, giving the backward travel time
T(phi) and the stop point X0. The weak eigenfunction Xi (V.grad Xi = m1 Xi, grad Xi(0) = e1) is Xi(exit) = e^{m1 T} X0.e1 to
leading order, and rho / |Xi|^{1/m1} is constant on orbits, so the matching function is
    log G(phi) = log A(phi) + p t_max - (1/m1) log |X0.e1| - T(phi)
(at m1 = 1/2 this is the lead's log Gt up to a constant). A profile needs G constant on the support. For x-odd v:
    M_rho v = odd part in phi of (log G[rho* + eps v] - log G[rho* - eps v]) / (2 eps)        (datum A fixed)
reported as the RMS and max over |cos phi| > 0.05 and > 0.3, for t_in = -12, -13, -13.5 (independence check; at -10 the
backward orbits are not yet aligned with e1: stop angle 20 deg), next to the same
for comparison vectors of equal norm (<f, g> = sum f g / r^(2p), as the Arnoldi): v0 = odd(rho* cos th) (the Arnoldi start),
odd(d_th rho*), and two random smooth x-odd vectors. Also log G of rho* itself (its spread on the support) and, per vector,
the change of b = psi_yy(0) and of e1 (deg) per eps. CPU, one thread.
Usage: python3 tests/v108d_match.py MODE.npz [er (1e-4)] [hs (0.03)]"""
import sys, math, json, time, numpy as np, torch
torch.set_num_threads(1)
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; er = float(sys.argv[2]) if len(sys.argv) > 2 else 1e-4; hs = float(sys.argv[3]) if len(sys.argv) > 3 else 0.03
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


TINS = (-12.0, -13.0, -13.5)       # the linear node regime starts below log r about -12 at the p 0.35 states (V108)
def logG(R):
    al, be, _, _ = F.fields(R); nd = F.node(R); e = math.radians(nd['e1_deg']); m1 = nd['m1']
    out = {}
    for tin in TINS:
        th0, T, nbad = back(al, be, tin)
        u0 = math.exp(tin)*(torch.cos(th0)*math.cos(e) + torch.sin(th0)*math.sin(e))
        with np.errstate(divide='ignore', invalid='ignore'):
            out[tin] = (np.log(Aphi) + p*F.tmax - np.log(np.abs(u0.numpy()))/m1 - T.numpy(), nbad)
    return out, nd
G0, nd0 = logG(rho)
rec = dict(mode=fn.split('/')[-1], state=margs['source'].split('/')[-1], lam=float(md['lam']), nt=nt, er=er, hs=hs,
           m1=round(nd0['m1'], 6), e1_deg=round(nd0['e1_deg'], 4), b=float('%.3g' % nd0['b']))
rec['logG_rho*'] = {('%g' % k): dict(not_reached=v[1], spread05=round(float(np.ptp(v[0][sup05])), 4),
                                    std05=round(float(np.std(v[0][sup05])), 4), odd_max05=float('%.3g' % np.abs(oddphi(v[0])[sup05]).max()))
                    for k, v in G0.items()}
rec['logG_rho*_tin_diff05'] = float('%.3g' % np.abs((G0[-13.5][0] - G0[-12.0][0])[sup05]).max())
gen = torch.Generator().manual_seed(7)
def smooth_rand():
    c = torch.randn(6, 6, generator=gen, dtype=DT); tt = (F.t_nodes - F.tmin)/(F.tmax - F.tmin)
    f = sum(c[i, j]*torch.cos(i*math.pi*tt)[:, None]*torch.cos((j + 1)*F.TH) for i in range(6) for j in range(6))
    return odd(rho*f)
vecs = dict(mode=torch.tensor(md['u'], dtype=DT), v0=odd(rho*torch.cos(F.TH)),
            dth=odd(torch.real(torch.fft.ifft(1j*torch.fft.fftfreq(nt, 1.0/nt, dtype=DT)*torch.fft.fft(rho, dim=1), dim=1))),
            rand1=smooth_rand(), rand2=smooth_rand())
eps = er*scale
for nm, v in vecs.items():
    v = odd(v); v = v/nrm(v)
    Gp, ndp = logG(rho + eps*v); Gm, ndm = logG(rho - eps*v)
    r2 = dict(b_per_eps=float('%.5g' % ((ndp['b'] - ndm['b'])/(2*eps))), e1deg_per_eps=float('%.5g' % (((ndp['e1_deg'] - ndm['e1_deg'] + 90) % 180 - 90)/(2*eps))),
              dm1_per_eps=float('%.3g' % ((ndp['m1'] - ndm['m1'])/(2*eps))))
    for tin in TINS:
        M = oddphi((Gp[tin][0] - Gm[tin][0])/(2*eps))
        r2['tin%g' % tin] = dict(rms05=float('%.4g' % math.sqrt(np.mean(M[sup05]**2))), max05=float('%.4g' % np.abs(M[sup05]).max()),
                                 rms3=float('%.4g' % math.sqrt(np.mean(M[sup3]**2))), nbad=Gp[tin][1] + Gm[tin][1])
    rec[nm] = r2
    print(json.dumps({nm: r2}), flush=True)
rec['wall'] = round(time.time() - t0w, 1)
print('MATCH ' + json.dumps(rec), flush=True)
