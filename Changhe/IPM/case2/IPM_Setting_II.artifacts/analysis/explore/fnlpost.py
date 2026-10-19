# Lead (2026-10-18): post-processing of an fpnloc iterate (datum A = cos^2 exp(Fourier K + zero-window bumps ws)).
# mode 'same': re-relax at the stored grid; 'ang': 2x angles (FFT interpolation); 'dom=L': extend to r_max = e^L (same
# radial spacing, new outer cells g = A). Then relax to dg/ds < 1e-8 and report m1 (ring), m1 from the forward moment
# identity, the full log Gt profile (uniform mean on |cos| > cut removed) with picks, and save the state.
# Usage: python3 fnlpost.py iter.npz mode out.npz [nA=2048 cut=0.02 nmax=6000 ds=0.02]
import sys, json, time
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
d = np.load(sys.argv[1]); mode = sys.argv[2]; outf = sys.argv[3]
opt = dict(nA=2048, cut=0.02, nmax=6000, ds=0.02)
for s in sys.argv[4:]:
    k, v = s.split('='); opt[k] = int(v) if k in ('nA', 'nmax') else float(v)
args = json.loads(str(d['args']))
p = float(d['p']); x = np.asarray(d['x'], float); K = int(args['K']); ws = list(args['ws'])


def basis(t):
    out = [FE.basis(t, K)] if K > 0 else []
    s = np.sin(t)
    for w in ws: out.append(np.exp(-(1 - s) / w)[None, :])
    for w in ws: out.append(np.exp(-(1 + s) / w)[None, :])
    return np.vstack(out)


Af = lambda t: np.cos(t) ** 2 * np.exp(x @ basis(np.atleast_1d(t).ravel())).reshape(np.shape(t))
g, lr, th = d['g'], d['lr'], d['th']
if mode == 'ang':
    Nth = g.shape[1]
    G = np.fft.rfft(g, axis=1); G2 = np.zeros((g.shape[0], Nth + 1), complex); G2[:, :G.shape[1]] = G * 2
    G2[:, Nth // 2] *= 0.5
    g = np.fft.irfft(G2, 2 * Nth, axis=1); th = 2 * np.pi * np.arange(2 * Nth) / (2 * Nth)
elif mode.startswith('dom='):
    L = float(mode[4:]); drho = lr[1] - lr[0]; nadd = int(round((L - lr[-1]) / drho))
    lr = np.concatenate([lr, lr[-1] + drho * np.arange(1, nadd + 1)])
    g = np.vstack([g, np.repeat(Af(th)[None, :], nadd, axis=0)])
t0 = time.time()
g, info = FE.evolve(p, Af, g, lr, th, 400, ds=opt['ds']); steps = info['steps']
while info['dgds'] > 1e-8 and steps < opt['nmax']:
    g, info = FE.evolve(p, Af, g, lr, th, 100, ds=opt['ds'], tol=1e-8); steps += info['steps']
ng = FE.node_and_G(p, Af, g, lr, th, nA=opt['nA'])
thA = ng['thA']; lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
w = (np.abs(np.cos(thA)) > opt['cut']) & np.isfinite(lgt)
lgt = lgt - lgt[w].mean(); deg = np.degrees(thA)
pick = {str(d0): round(float(lgt[int(np.argmin(np.abs(deg - d0)))]), 4)
        for d0 in (0, 30, 60, 80, 85, 88, 89, 91, 120, 150, 180, 210, 240, 260, 265, 268, 269, 271, 275, 280, 300, 330)}
l = 1.0 / p; r = np.exp(lr); rho = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rho, lr, th, p)
itg = 3 * rho * r[:, None] ** -2 * (wt * np.cos(3 * th)[None, :] - wr * np.sin(3 * th)[None, :])
Q = np.trapz(itg.sum(1) * (2 * np.pi / len(th)), dx=lr[1] - lr[0])
print(json.dumps(dict(src=sys.argv[1], mode=mode, Nr=len(lr), Nth=len(th), lrmax=float(lr[-1]), p=p, steps=steps,
                      dgds=info['dgds'], m1=ng['m1'], m2=ng['m2'], m1_Q=float(l - Q / (np.pi * (l - 1))),
                      range=float(lgt[w].max() - lgt[w].min()), std=float(lgt[w].std()), logGt=pick,
                      wall=round(time.time() - t0))), flush=True)
np.savez(outf, g=g, lr=lr, th=th, x=x, p=p, thA=thA, logGt=lgt, m1=ng['m1'],
         args=json.dumps(dict(p=p, K=K, ws=ws, x=x.tolist(), kind='fnlpost', mode=mode, src=sys.argv[1])))
