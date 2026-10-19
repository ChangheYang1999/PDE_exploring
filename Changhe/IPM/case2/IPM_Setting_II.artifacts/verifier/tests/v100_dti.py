"""V100 (follows V89: on my a_2 -1.2 fixed point, dm1 = m1(T rho) - m1(rho) is -2.8e-6 under hs 0.03 -> 0.015 but -1.7e-3 under
the transfer grid dti 0.01 -> 0.005). dti is the spacing of the uniform t grid on which alpha, beta are sampled (panel Lagrange
from the Gauss nodes) and then interpolated by 4-point Lagrange cubics in t and th along the orbits. Here: dm1 for
dti = 0.01, 0.005, 0.0025, 0.00125 at hs 0.03 (nmax 8000, x-even projection as in the state's args), the band split of dm1 (T rho on one
t band only), and the angular split of dm1 on t < -10 into the weak-axis sectors |sin th| < sin 6 deg, the slow window 80-100 /
260-280 deg and the rest; plus the max jump of the panel-Lagrange interpolants of alpha, beta across panel edges (relative to max
|alpha|), which would make the dti error first order.
Usage: python3 tests/v100_dti.py OWN.npz [dti list, comma separated]"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
from charsolve import lagrange_eval
DT = torch.float64
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p'])
dtis = [float(v) for v in sys.argv[2].split(',')] if len(sys.argv) > 2 else [0.01, 0.005, 0.0025, 0.00125]
par = [float(v) for v in args['par'].split(':')]
def A(t):
    f = np.zeros_like(t)
    for j, aj in enumerate(par):
        n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
    return np.cos(t)**2*np.exp(f)
nt = len(d['th']); t0 = time.time()
bands = ((-20, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, 10))
for k, dti in enumerate(dtis):
    F = FwdStat(p, A, tmin=float(args['tmin']), tmax=float(args['tmax']), ppu=int(args['ppu']), q=8, nt=nt, dti=dti, nstep=800)
    assert np.allclose(F.r.cpu().numpy(), d['r'])
    F.smode = True; F.hs = 0.03; F.nmax = 8000; F.xsym = bool(int(args.get('xsym', 0)))
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda'); Rp = F.R**p
    m1s = F.node(rho)['m1']
    if k == 0:
        al, be, _, _ = F.fields(rho); S = F.S; q = S.q
        edges = np.concatenate([[0.0], np.exp(np.linspace(F.tmin, F.tmax, int(round((F.tmax - F.tmin)*int(args['ppu']))) + 1))])
        xg = np.polynomial.legendre.leggauss(q)[0]
        Lm, Lp = torch.tensor(lagrange_eval(xg, 1.0), dtype=DT, device='cuda'), torch.tensor(lagrange_eval(xg, -1.0), dtype=DT, device='cuda')
        am = float(al.abs().max()); jmp = {}
        for nm, f in (('alpha', al), ('beta', be)):
            js = []
            for e in range(2, len(edges) - 1):        # interior edges between panels e-1 and e (panel 0 = core)
                left = Lm @ f[(e - 1)*q:e*q]; right = Lp @ f[e*q:(e + 1)*q]
                js.append(float((left - right).abs().max()))
            js = np.array(js); i = int(np.argmax(js))
            jmp[nm] = [float('%.3g' % (js.max()/am)), round(float(math.log(edges[2 + i])), 3), float('%.3g' % np.median(js/am))]
        print(json.dumps(dict(state=fn.split('/')[-1], m1=m1s, panel_edge_jump_rel_max_t_median=jmp)), flush=True)
    Tr, _ = F.T(rho)
    t = F.t_nodes[:, None].expand_as(F.R); deg = torch.rad2deg(F.TH)
    rec = dict(dti=dti, dm1=float('%.4g' % (F.node(Tr)['m1'] - m1s)), defect=float('%.3g' % float(((Tr - rho)/Rp).abs().max())))
    sp = {}
    for lo, hi in bands:
        msk = (t >= lo) & (t < hi)
        sp['%g..%g' % (lo, hi)] = float('%.3g' % (F.node(torch.where(msk, Tr, rho))['m1'] - m1s))
    weak = torch.abs(torch.sin(F.TH)) < math.sin(math.radians(6))
    win = ((deg >= 80) & (deg <= 100)) | ((deg >= 260) & (deg <= 280))
    core = t < -10
    for nm, sec in (('weak', weak), ('window', win), ('rest', ~weak & ~win)):
        sp['t<-10 ' + nm] = float('%.3g' % (F.node(torch.where(core & sec, Tr, rho))['m1'] - m1s))
    rec['dm1_split'] = sp; rec['wall'] = round(time.time() - t0, 1)
    print(json.dumps(rec), flush=True)
    del F, Tr; torch.cuda.empty_cache()
