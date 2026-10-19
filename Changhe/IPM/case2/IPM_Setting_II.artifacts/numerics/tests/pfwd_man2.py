"""Two-control continuation on the compatibility manifold m1 = 1/2 (lead request 2026-10-18T04:28Z item 6).
At each point of a scan in the y-even controls (a_2 = cos 2th coefficient, a_4, p), the m1 compensator amplitude c is found by a secant
so that the CORE-CORRECTED m1 = 1/p - (c_moment + core) equals 1/2 (tol).  Compensators (direction in the x-even basis
sin th, cos 2th, sin 3th, cos 4th, sin 5th, cos 6th):
   c13: sin th + sin 3th = 4 sin th cos^2 th   (endpoint preserving: F(pi/2) - F(-pi/2) unchanged)
   c51: sin 5th - sin th                        (endpoint preserving)
   a3:  sin 3th                                 (the shift-2 compensator; moves F(pi/2) - F(-pi/2) by -2 c)
Reported per point: D_ax (axis formula, specification M25(h); both the k-ODE form and the referee result 17 paired integral), the axis-law drifts, D_samp
from the tracer with a DEEP inner stop (V59), dips, bulk std, m1 with and without the core term.  States saved as npz.
Usage: python3 tests/pfwd_man2.py tag comp "a2=-0.714,-0.9,-1.1" ["p=0.4957,0.45"] [lo=-14] [Nr=721] [lr0=-13] [nsteps=900] [tol=3e-4] [c0=0]
       (if both a2 and p lists are given the scan is the product, p outer)"""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_fp import FixedPoint
from pfwd_diag import core_term, axis_D, deep_trace_stats
torch.set_default_dtype(torch.float64)

tag, comp = sys.argv[1], sys.argv[2]
opt = dict(lo=-14.0, Nr=721, lr0=-13.0, nsteps=900, tol=3e-4, c0=0.0, a4=None, ds=0.02, Nth=256)
A2 = [-0.7141]; PS = [0.4957]
for s_ in sys.argv[3:]:
    k, v = s_.split('=', 1)
    if k == 'a2': A2 = [float(u) for u in v.split(',')]
    elif k == 'p': PS = [float(u) for u in v.split(',')]
    elif k == 'a4': opt['a4'] = [float(u) for u in v.split(',')]
    elif k in ('Nr', 'nsteps', 'Nth'): opt[k] = int(v)
    elif k == 'base': opt[k] = v
    else: opt[k] = float(v)
DIRS = dict(c13=[1, 0, 1, 0, 0, 0], c51=[-1, 0, 0, 0, 1, 0], a3=[0, 0, 1, 0, 0, 0], p=[0, 0, 0, 0, 0, 0])
vdir = np.array(DIRS[comp], float)
# comp 'p': the odd part is frozen and p itself is the compensator (y-even, endpoint preserving); then c IS p.
a0 = np.array([0.2390, -0.7141, -0.2124, 0.1220, 0.1070, -0.0270])        # N = 6 fixed point, a_3 retuned (earlier base)
if 'base' in opt: a0 = np.array([float(u) for u in str(opt['base']).split(',')])
FP = FixedPoint(PS[0], 6, Nr=opt['Nr'], lo=opt['lo'], hi=10.0, ds=opt['ds'], nsteps=opt['nsteps'], nA=1440, dt=0.01, Nth=opt['Nth'])
S = FP.S
os.makedirs('runs/pfwd/man2', exist_ok=True)
log = open('runs/pfwd/man2_%s.log' % tag, 'a')
def emit(rec):
    line = json.dumps(rec); print(line, flush=True); log.write(line + '\n'); log.flush()

def ev(x, p, full=False):
    g, Wr, Wt, d, dg, ok = FP.steady(list(x), p)
    rho = S.r[:, None] ** p * g
    Wr, Wt = S.velocity(rho); d = S.diagnostics(g, Wr, Wt, krings=(20,))
    core = core_term(S, rho)
    m1_nc = 1 / p - d['c_moment']; m1 = m1_nc - core
    info = dict(m1_nocore=m1_nc, core=core, m1_ring20=d['ring20']['m1'], dgds=dg, ok=ok, gmin=d['gmin'])
    if full:
        A = FP.Afun(list(x))(S.th)
        ax = axis_D(S, g, Wr, p, m1, A=A)
        st, lg = deep_trace_stats(FP, Wr, Wt, FP.Afun(list(x))(FP.thA), m1, lr0=opt['lr0'])
        info.update(ax=ax, tr=st, g=g, lg=lg)
    return m1, info

def retune(x, p, c):
    """secant in the compensator amplitude c for m1_core = 1/2: datum x + c vdir at p (comp a3/c13/c51), or datum x at p = c (comp 'p')."""
    if comp == 'p':
        xs = lambda c_: list(np.asarray(x)); pp = lambda c_: c_; smax, cl0 = 0.05, 0.56
    else:
        xs = lambda c_: list(np.asarray(x) + c_ * vdir); pp = lambda c_: p; smax, cl0 = 0.15, -0.9
    m1, info = ev(xs(c), pp(c)); f = m1 - 0.5; nev = 1; hist = [(c, m1)]
    if abs(f) < opt['tol']: return c, m1, nev, hist
    slope = cl0 if comp in ('a3', 'p') else None
    cb = c + (float(np.clip(-f / slope, -smax, smax)) if slope else (0.05 if f > 0 else -0.05))
    for k in range(7):
        m1b, infob = ev(xs(cb), pp(cb)); fb = m1b - 0.5; nev += 1; hist.append((cb, m1b))
        if abs(fb) < opt['tol']: return cb, m1b, nev, hist
        if abs(fb - f) > 1e-7: slope = (fb - f) / (cb - c)
        if slope is None or abs(slope) < 0.05: slope = cl0 if slope is None else math.copysign(0.05, slope)
        c, f, m1 = cb, fb, m1b
        cb = c + float(np.clip(-f / slope, -smax, smax))
    return c, m1, nev, hist

c = opt['c0']
emit(dict(tag=tag, comp=comp, vdir=vdir.tolist(), opt=opt, A2=A2, PS=PS, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
A4s = opt['a4'] if opt['a4'] is not None else [None]
for p in PS:
    for a2 in A2:
        for a4 in A4s:
            t0 = time.time()
            x = a0.copy(); x[1] = a2
            if a4 is not None: x[3] = a4
            if comp == 'p' and c == 0.0: c = p
            c, m1, nev, hist = retune(x, p, c)
            xf = list(np.asarray(x) + c * vdir)
            if comp == 'p': p = c
            m1f, info = ev(xf, p, full=True)
            ax, tr = info['ax'], info['tr']
            on = abs(m1f - 0.5) <= 2 * opt['tol']
            rec = dict(a2=a2, a4=a4, p=p, comp=comp, c=round(c, 5), x=[round(v, 5) for v in xf], m1=round(m1f, 6), m1_nocore=round(info['m1_nocore'], 6),
                       core=round(info['core'], 6), m1_ring20=info['m1_ring20'], on_manifold=on,
                       D_ax=round(ax['D_ax_k'], 4), D_ax_res17=round(ax['D_ax_res17'], 4), drift_up=round(ax['drift_up'], 4), drift_down=round(ax['drift_down'], 4),
                       Fp_minus_Fm=round(ax['Fp_minus_Fm_datum'], 4), twoL_k=round(ax['twoL_k'], 4), twoL_res17=round(ax['twoL_res17'], 4),
                       e_p=round(ax['e_p_formula'], 5), e_p_meas=round(ax['e_p_measured'], 5), we_m6=round(ax['we_over_r_m6'], 4),
                       D_samp=round(tr['D_samp'], 4), up=round(tr['up'], 4), low=round(tr['low'], 4), bulk_std=round(tr['bulk_std'], 4), range=round(tr['range_005'], 4),
                       lg88=tr['lg88'], lg268=tr['lg268'], lr0=tr['lr0'], dgds='%.1e' % info['dgds'], ok=info['ok'], gmin='%.2e' % info['gmin'],
                       nev=nev, hist=[(round(h[0], 5), round(h[1], 5)) for h in hist], wall=round(time.time() - t0, 1))
            emit(rec)
            fn = 'runs/pfwd/man2/%s_p%.4f_a2%.3f%s.npz' % (tag, p, a2, '' if a4 is None else '_a4%.3f' % a4)
            np.savez(fn, g=info['g'].cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), hist=json.dumps([rec]),
                     args=json.dumps(dict(p=p, kind='expf', par=xf, N=6, comp=comp, c=c)), logGt=info['lg'], thA=FP.thA.cpu().numpy())
emit(dict(tag=tag, done=True, end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
print("MAN2_DONE", flush=True)
