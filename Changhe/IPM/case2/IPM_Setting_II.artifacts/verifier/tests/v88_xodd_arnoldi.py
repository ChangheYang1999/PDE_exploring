"""V88: x-odd spectrum of DT, the derivative of my exit map (code/fwdstat.py, arclength orbits, NO x-even projection), at an
x-even fixed point rho* (own format), by Arnoldi instead of the power iteration of tests/v82_xodd.py (which did not converge at
a_2 -1.2: ratios 0.98-2.6, Rayleigh quotients of both signs). For odd d, odd(T(rho* + eps d)) = (T(rho* + eps d) - T(rho* - eps d)) / 2
because T commutes with th -> pi - th on x-even data, so the matvec J d = odd(T(rho* + eps d) - T(rho*)) / eps is a central
difference. Inner product <f, g> = sum f g / r^(2p) on my grid (as v82). Start vector odd(rho* cos th).
Printed after each step k >= 4: the 6 Ritz values of largest modulus with residual estimates |h_{k+1,k} y_k|, the harmonic Ritz
values nearest 1 (eigenvalues of J near 1 = symmetry-breaking bifurcation of the fixed point), and sigma_min of Hbar - I (an upper
bound for sigma_min(J - I) on the odd subspace). At the end, the x-odd moment b per unit eps of the leading Ritz vectors.
Usage: python3 tests/v88_xodd_arnoldi.py OWN.npz [m (16)] [eps_rel (1e-4)]"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64
fn = sys.argv[1]; m = int(sys.argv[2]) if len(sys.argv) > 2 else 16; er = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-4
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
print(json.dumps(dict(state=fn.split('/')[-1], p=p, nt=nt, m=m, m1=F.node(rho)['m1'], defect=float(((T0 - rho)/Rp).abs().max()),
                      odd_T0=nrm(odd(T0))/nrm(rho), wall=round(time.time() - t0, 1))), flush=True)
eps = er*float((rho/Rp).abs().max())
def J(v):
    Tv, _ = F.T(rho + eps*v)
    return odd(Tv - T0)/eps
v0 = odd(rho*torch.cos(F.TH)); V = [v0/nrm(v0)]; H = np.zeros((m + 1, m))
def report(k, final=False):
    Hk = H[:k, :k]; hk = H[k, k - 1]
    w, Y = np.linalg.eig(Hk)
    res = np.abs(hk*Y[-1, :])
    o = np.argsort(-np.abs(w))[:6]
    B = Hk - np.eye(k)
    try:
        ek = np.zeros(k); ek[-1] = 1.0
        Hh = B + hk**2*np.outer(np.linalg.solve(B.T, ek), ek)
        wh = np.linalg.eigvals(Hh) + 1.0
        oh = np.argsort(np.abs(wh - 1.0))[:4]
        harm = [[round(float(wh[i].real), 4), round(float(wh[i].imag), 4)] for i in oh]
    except np.linalg.LinAlgError:
        harm = None
    Hb = H[:k + 1, :k] - np.vstack([np.eye(k), np.zeros((1, k))])
    smin = float(np.linalg.svd(Hb, compute_uv=False)[-1])
    rec = dict(k=k, ritz=[[round(float(w[i].real), 4), round(float(w[i].imag), 4), float('%.2g' % res[i])] for i in o],
               harmonic_near_1=harm, sigma_min_Hbar_minus_I=round(smin, 4), wall=round(time.time() - t0, 1))
    print(json.dumps(rec), flush=True)
    return w, Y, o
for k in range(m):
    wv = J(V[k])
    for _ in range(2):                         # modified Gram-Schmidt, twice
        for j in range(k + 1):
            h = ip(V[j], wv); H[j, k] += h; wv = wv - h*V[j]
    H[k + 1, k] = nrm(wv)
    if H[k + 1, k] < 1e-12:
        print(json.dumps(dict(k=k + 1, msg='invariant subspace')), flush=True); report(k + 1); break
    V.append(wv/H[k + 1, k])
    if k + 1 >= 4: w, Y, o = report(k + 1)
kk = len(V) - 1
w, Y = np.linalg.eig(H[:kk, :kk]); o = np.argsort(-np.abs(w))[:3]
for i in o:
    y = Y[:, i]
    for part, yy in (('re', y.real), ('im', y.imag)):
        if np.abs(yy).max() < 1e-12: continue
        u = sum(float(c)*V[j] for j, c in enumerate(yy)); u = u/nrm(u)
        print(json.dumps(dict(ritz=[round(float(w[i].real), 4), round(float(w[i].imag), 4)], part=part,
                              b_per_eps=round(F.node(rho + eps*u)['b']/eps, 5))), flush=True)
