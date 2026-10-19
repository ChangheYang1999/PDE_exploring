"""V108: the real x-odd eigenvalue of DT near 1 found by the 48-step Arnoldi of V102b (a_2 -1.1: 0.9694, residual 3e-5 at k 32).
Same matvec, inner product and start vector as tests/v88_xodd_arnoldi.py (J d = odd(T(rho* + eps d) - T(rho*)) / eps, arclength
orbits, no projection, <f, g> = sum f g / r^(2p), v0 = odd(rho* cos th)). After m steps: the real Ritz value nearest 1 and its
Ritz vector u (normalised, saved to OUT.npz), then
  - the true residual |J u - lambda u| / |u| at eps_rel 1e-4 (the Arnoldi eps), 1e-5 and 1e-3, and <u, J u> at each;
  - where u lives: fractions of |u|^2 by t band and by sector (windows 80-100 / 260-280 deg, weak axes |sin th| < sin 10 deg, rest),
    and the (t, deg) of max |u| / r^p;
  - the jet it moves: for rho* + eps u, the off-diagonal moment b, and the angle of the weak eigenvector of DV(0) (e1_deg), per eps.
Usage: python3 tests/v108_xodd_mode.py OWN.npz OUT.npz [m (40)]"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn, out = sys.argv[1], sys.argv[2]; m = int(sys.argv[3]) if len(sys.argv) > 3 else 40
d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p'])
par = [float(v) for v in args['par'].split(':')]
def A(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
nt = len(d['th'])
F = FwdStat(p, A, tmin=float(args.get('tmin', -12)), tmax=float(args.get('tmax', 10)), ppu=int(args.get('ppu', 3)), q=8, nt=nt,
            dti=0.01, nstep=800)
assert np.allclose(F.r.cpu().numpy(), d['r'])
F.smode = True; F.hs = 0.03; F.nmax = 8000; F.xsym = False
rho = torch.tensor(d['rho'], dtype=DT, device='cuda'); Rp = F.R**p
xi = torch.tensor((nt//2 - np.arange(nt)) % nt, device='cuda')
odd = lambda f: 0.5*(f - f[:, xi])
ip = lambda f, g: float((f*g/Rp**2).sum())
nrm = lambda f: math.sqrt(ip(f, f))
t0 = time.time()
T0, _ = F.T(rho)
scale = float((rho/Rp).abs().max())
def J(v, er=1e-4):
    eps = er*scale
    Tv, _ = F.T(rho + eps*v)
    return odd(Tv - T0)/eps
nd0 = F.node(rho)
print(json.dumps(dict(state=fn.split('/')[-1], m=m, m1=nd0['m1'], b=nd0['b'], defect=float(((T0 - rho)/Rp).abs().max()))), flush=True)
v0 = odd(rho*torch.cos(F.TH)); V = [v0/nrm(v0)]; H = np.zeros((m + 1, m))
for k in range(m):
    wv = J(V[k])
    for _ in range(2):
        for j in range(k + 1):
            h = ip(V[j], wv); H[j, k] += h; wv = wv - h*V[j]
    H[k + 1, k] = nrm(wv); V.append(wv/H[k + 1, k])
    if (k + 1) % 8 == 0:
        w = np.linalg.eigvals(H[:k + 1, :k + 1]); rr = w[np.abs(w.imag) < 1e-10].real
        print(json.dumps(dict(k=k + 1, real_ritz_nearest_1=sorted([round(float(x), 4) for x in rr], key=lambda x: abs(x - 1))[:3],
                              wall=round(time.time() - t0, 1))), flush=True)
w, Y = np.linalg.eig(H[:m, :m])
real = np.where(np.abs(w.imag) < 1e-10)[0]; i = real[np.argmin(np.abs(w[real].real - 1))]
lam = float(w[i].real); y = Y[:, i]; y = (y/y[np.argmax(np.abs(y))]).real
u = sum(float(c)*V[j] for j, c in enumerate(y)); u = u/nrm(u)
rec = dict(lam=round(lam, 5), ritz_res=float('%.2g' % abs(H[m, m - 1]*Y[-1, i])))
for er in (1e-4, 1e-5, 1e-3):
    Ju = J(u, er)
    rec['eps%g' % er] = dict(res=float('%.3g' % (nrm(Ju - lam*u))), rayleigh=round(ip(u, Ju), 5))
    eps = er*scale; nd = F.node(rho + eps*u)
    rec['eps%g' % er]['b_per_eps'] = float('%.5g' % ((nd['b'] - nd0['b'])/eps))
    rec['eps%g' % er]['e1_deg'] = float('%.4g' % nd.get('e1_deg', float('nan')))
U = (u**2/Rp**2).cpu().numpy(); tot = U.sum()
t = np.log(F.r.cpu().numpy()); deg = np.degrees(F.th.cpu().numpy())
bands = [(-30, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 11)]
rec['band_frac'] = {'%g..%g' % (a, b): round(float(U[(t >= a) & (t < b)].sum()/tot), 4) for a, b in bands}
win = ((deg >= 80) & (deg <= 100)) | ((deg >= 260) & (deg <= 280))
weak = np.abs(np.sin(np.radians(deg))) < math.sin(math.radians(10))
rec['sector_frac'] = dict(windows=round(float(U[:, win].sum()/tot), 4), weak_axes=round(float(U[:, weak].sum()/tot), 4),
                          rest=round(float(U[:, ~win & ~weak].sum()/tot), 4))
a = (u.abs()/Rp).cpu().numpy(); ii, jj = np.unravel_index(np.argmax(a), a.shape)
rec['argmax_u_over_rp'] = [round(float(t[ii]), 2), round(float(deg[jj]), 2)]
rec['wall'] = round(time.time() - t0, 1)
print('MODE ' + json.dumps(rec), flush=True)
np.savez(out, u=u.cpu().numpy(), lam=lam, r=F.r.cpu().numpy(), th=F.th.cpu().numpy(), p=p, args=json.dumps(dict(source=fn, m=m)))
