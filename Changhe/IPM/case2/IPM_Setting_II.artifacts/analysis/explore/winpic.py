# Lead (2026-10-18): window-only Picard for the forward problem (x-even class).
# At fixed velocity, G(th_in) is proportional to A(th_in) along each orbit, so A <- A G_bulk / G is exact at fixed velocity.
# Here the correction is applied only in windows |cos th| < sin(w2) around the zeros +-pi/2 (smooth taper from w1 to w2 degrees),
# where A ~ cos^2 carries little mass; the bulk datum (6 x-even modes x, p) is frozen. Each iteration: relax (evolve) from the previous
# state, deep backward tracer (lr0), log Gt - bulk, update the window factor c(th), axis value D_ax (a_dir, k = 1 at r_min).
# Usage: python3 withpf2.py winpic.py state.npz K out_prefix [its=6 w1=6 w2=12 beta=1 lr0=-11.5 nA=4096 nmax=1500 tol=1e-7 nmin=200]
import sys, json, time, numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
st = np.load(sys.argv[1]); K = int(sys.argv[2]); pre = sys.argv[3]
opt = dict(its=6, w1=6.0, w2=12.0, beta=1.0, lr0=-11.5, nA=4096, nmax=1500, tol=1e-7, nmin=200)
for s in sys.argv[4:]:
    k, v = s.split('='); opt[k] = int(v) if k in ('its', 'nA', 'nmax', 'nmin') else float(v)
g, lr, th, x, p = st['g'], st['lr'], st['th'], st['x'][:K], float(st['p']); l = 1 / p; r = np.exp(lr); N = len(th)
nA = opt['nA']; thf = 2 * np.pi * np.arange(nA) / nA; cf = np.zeros(nA)
if 'cwin' in st and len(st['cwin']) == nA: cf = st['cwin'].copy()
F0 = lambda t: x @ FE.basis(np.atleast_1d(t).ravel(), K)
def Af(t):
    t = np.atleast_1d(t); tt = np.mod(t.ravel(), 2 * np.pi)
    c = np.interp(tt, np.concatenate([thf, [2 * np.pi]]), np.concatenate([cf, [cf[0]]]))
    return (np.cos(tt) ** 2 * np.exp(F0(tt) + c)).reshape(t.shape)
dz = np.abs(np.cos(thf)); s1, s2 = np.sin(np.radians(opt['w1'])), np.sin(np.radians(opt['w2']))
chi = np.clip((s2 - dz) / (s2 - s1), 0, 1); chi = chi * chi * (3 - 2 * chi)
kk = np.fft.rfftfreq(N, 1.0 / N)
def dax(g, m1):
    rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
    dwt = np.fft.irfft(1j * kk * np.fft.rfft(wt, axis=1), N, axis=1); gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(g, axis=1), N, axis=1)
    q = {}
    for name, j in (('up', N // 4), ('down', 3 * N // 4)):
        Vr = l * r + wr[:, j]; adir = (Vr + dwt[:, j]) / r; h = r ** (p - 2) * gtt[:, j]
        law = np.concatenate([[0], np.cumsum(0.5 * ((1 - 2 * m1) / Vr[1:] + (1 - 2 * m1) / Vr[:-1]) * np.diff(r))])
        f = -(adir - m1) / Vr; logk = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))])
        q[name] = np.log(np.abs(h)) - 2 * logk - law
    wq = lr >= -8
    return float(q['down'][-1] - q['up'][-1]), float(np.ptp(q['up'][wq])), float(np.ptp(q['down'][wq])), float(wr[:, :].min() / 1.0)
for it in range(opt['its'] + 1):
    t0 = time.time(); steps = 0
    if it > 0 or 'relaxed' not in opt:
        while True:
            g, info = FE.evolve(p, Af, g, lr, th, 100); steps += 100
            if (steps >= opt['nmin'] and info['dgds'] < opt['tol']) or steps >= opt['nmax']: break
    ng = FE.node_and_G(p, Af, g, lr, th, nA=nA, lr0=opt['lr0'])
    lgt = np.log(np.maximum(ng['A'], 1e-300)) - 2 * ng['m1'] * ng['logAn']
    deg = np.degrees(ng['thA']); bulk = float(np.mean(lgt[dz > 0.3])); dev = lgt - bulk
    near = dz < np.sin(np.radians(0.3)); dev_s = dev.copy()
    for c0 in (90.0, 270.0):
        side = np.abs(deg - c0) < 0.3; ref = np.abs(np.abs(deg - c0) - 0.35) < 0.05
        dev_s[side] = np.mean(dev[ref])
    D, spu, spd, _ = dax(g, ng['m1'])
    ok = dz > 0.02
    prof = {str(a): round(float(dev[np.argmin(np.abs(deg - a))]), 4) for a in (60, 75, 80, 85, 88, 89, 89.5, 270.5, 271, 272, 275, 280, 285, 300)}
    rec = dict(it=it, m1=round(ng['m1'], 5), steps=steps, dgds=float('%.2g' % info['dgds']) if steps else None, D_ax=round(D, 4),
               spread_up=round(spu, 4), spread_down=round(spd, 4), D_samp=round(float(dev[np.argmin(np.abs(deg - 269))] - dev[np.argmin(np.abs(deg - 89))]), 4),
               bulk_std=round(float(dev[ok].std()), 4), range=round(float(np.ptp(dev[ok])), 4), maxdev_win=round(float(np.max(np.abs(dev_s * chi))), 4),
               cmax=round(float(np.max(np.abs(cf))), 4), prof=prof, wall=round(time.time() - t0))
    print(json.dumps(rec), flush=True)
    np.savez('%s_it%d.npz' % (pre, it), g=g, lr=lr, th=th, x=st['x'], p=p, m1=ng['m1'], thA=ng['thA'], logGt=lgt, cwin=cf.copy())
    if it < opt['its']:
        cf = cf - opt['beta'] * chi * dev_s
