"""V114 (lead team notes 11:04Z item (b)): x-odd Arnoldi restricted to SMOOTH perturbations. Same matvec J, inner product and
start vector as tests/v108_xodd_mode.py, but the Krylov space is built for S J S, with S a fixed smoothing: on f / r^p, angular
low-pass (Fourier modes |k| <= kmax) and a row-normalised Gaussian in t = log r (width wt, node spacing weights), then x-odd
projection. After m steps: the real Ritz value nearest 1 of S J S and its Ritz vector u; the true residuals |S J S u - lam u| and,
for us = S u / |S u|, |J us - lam us| (the unsmoothed derivative) at eps_rel 1e-4 and 1e-3; the top-2 / top-10 node fractions of
u (spike test), band fractions, b per eps. Usage: python3 tests/v114_smooth_arnoldi.py OWN.npz OUT.npz [m (40)] [kmax (32)] [wt (0.5)]"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn, out = sys.argv[1], sys.argv[2]; m = int(sys.argv[3]) if len(sys.argv) > 3 else 40
kmax = int(sys.argv[4]) if len(sys.argv) > 4 else 32; wt = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
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
tn = np.log(F.r.cpu().numpy()); wsp = np.gradient(tn)
Kr = wsp[None, :]*np.exp(-(tn[:, None] - tn[None, :])**2/(2*wt**2)); Kr = torch.tensor(Kr/Kr.sum(1, keepdims=True), dtype=DT, device='cuda')
kk = torch.fft.fftfreq(nt, 1.0/nt).abs().to('cuda')
def S(f):
    G = torch.fft.fft(f/Rp, dim=1); G[:, kk > kmax] = 0
    return odd((Kr @ torch.fft.ifft(G, dim=1).real)*Rp)
def J(v, er=1e-4):
    eps = er*scale
    Tv, _ = F.T(rho + eps*v)
    return odd(Tv - T0)/eps
nd0 = F.node(rho)
print(json.dumps(dict(state=fn.split('/')[-1], m=m, m1=nd0['m1'], b=nd0['b'], defect=float(((T0 - rho)/Rp).abs().max()))), flush=True)
v0 = S(odd(rho*torch.cos(F.TH))); V = [v0/nrm(v0)]; H = np.zeros((m + 1, m))
for k in range(m):
    wv = S(J(S(V[k])))
    for _ in range(2):
        for j in range(k + 1):
            h = ip(V[j], wv); H[j, k] += h; wv = wv - h*V[j]
    H[k + 1, k] = nrm(wv); V.append(wv/H[k + 1, k])
    if (k + 1) % 8 == 0:
        w = np.linalg.eigvals(H[:k + 1, :k + 1]); rr = w[np.abs(w.imag) < 1e-10].real
        cn = sorted(w, key=lambda z: abs(z - 1))[:4]; cm = sorted(w, key=lambda z: -abs(z))[:4]
        print(json.dumps(dict(k=k + 1, real_ritz_nearest_1=sorted([round(float(x), 4) for x in rr], key=lambda x: abs(x - 1))[:3],
                              ritz_nearest_1=[[round(float(z.real), 4), round(float(z.imag), 4)] for z in cn],
                              ritz_largest_mod=[[round(float(z.real), 4), round(float(z.imag), 4)] for z in cm],
                              wall=round(time.time() - t0, 1))), flush=True)
w, Y = np.linalg.eig(H[:m, :m])
real = np.where(np.abs(w.imag) < 1e-10)[0]; i = real[np.argmin(np.abs(w[real].real - 1))]
lam = float(w[i].real); y = Y[:, i]; y = (y/y[np.argmax(np.abs(y))]).real
u = sum(float(c)*V[j] for j, c in enumerate(y)); u = u/nrm(u)
rec = dict(lam=round(lam, 5), ritz_res=float('%.2g' % abs(H[m, m - 1]*Y[-1, i])))
us = S(u); us = us/nrm(us)
for er in (1e-4, 1e-3):
    Ju = J(us, er); SJSu = S(J(S(u), er))
    rec['eps%g' % er] = dict(res_SJS=float('%.3g' % nrm(SJSu - lam*u)), res_J_on_Su=float('%.3g' % nrm(Ju - lam*us)),
                             rayleigh_J_on_Su=round(ip(us, Ju), 5), cos_u_Su=round(ip(u, us)/nrm(u), 5))
    eps = er*scale; nd = F.node(rho + eps*us)
    rec['eps%g' % er]['b_per_eps'] = float('%.5g' % ((nd['b'] - nd0['b'])/eps))
Uf = np.sort((u**2/Rp**2).cpu().numpy().ravel())[::-1]; rec['top2_top10_frac'] = [round(float(Uf[:2].sum()/Uf.sum()), 4), round(float(Uf[:10].sum()/Uf.sum()), 4)]
rec['kmax'] = kmax; rec['wt'] = wt
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
print('SMODE ' + json.dumps(rec), flush=True)
np.savez(out, u=u.cpu().numpy(), lam=lam, H=H, ritz=w, r=F.r.cpu().numpy(), th=F.th.cpu().numpy(), p=p, args=json.dumps(dict(source=fn, m=m, kmax=kmax, wt=wt, smooth=1)))
