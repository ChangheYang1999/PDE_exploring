"""V97 (lead team notes 09:35Z item 1(f)): frozen-velocity split of c = psi_xy(0) by exit angle, in my own code.
For an own-format state (rho on my panel grid), V is computed from rho (code/fwdstat.py), and every node's forward orbit is traced
to r_max with the arclength tracer (hs 0.03, nmax 8000, as in the solver), giving the exit angle phi. With my moment quadrature
the cell contribution to c is dc_ij = (2/nt) (w_i / r_i^2) rho_ij sin 3th_j; the sum over cells plus the closed-form tail is c.
On orbits rho = e^{-T} r_max^p A(phi), so the sum over the cells whose exit angle lies in a set E is the frozen-velocity derivative
dc / d log A over E. Windows (as the lead's explore/ckernel.py): upper 80-100 deg, lower 260-280 deg, bulk = the rest; also the
narrow windows 85-95 / 265-275. t bands: core panel (t < t_min), [t_min, -10), [-10, -6), [-6, -4), [-4, -2), [-2, t_max], plus
the tail. Check: the same split of the image T[rho] (frozen V, datum A) next to the split of rho.
Usage: python3 tests/v97_ckernel.py OWN.npz [OWN2.npz ...]   (the datum is args.par, or args.par of args.source for imports)"""
import sys, math, json, time, numpy as np, torch
sys.path.insert(0, 'code')
from fwdstat import FwdStat
DT = torch.float64


def datum(args):
    par = args.get('par')
    if par is None and 'source' in args:
        src = np.load(args['source'].replace('../numerics', '../numerics'), allow_pickle=True)
        par = json.loads(str(src['args']))['par']
    if isinstance(par, str):
        par = [float(v) for v in par.split(':')]
    par = [float(v) for v in par]

    def A(t):
        f = np.zeros_like(t)
        for j, aj in enumerate(par):
            n = j + 1; f = f + aj*(np.sin(n*t) if n % 2 == 1 else np.cos(n*t))
        return np.cos(t)**2*np.exp(f)
    return A, len(par)


for fn in sys.argv[1:]:
    t0 = time.time()
    d = np.load(fn, allow_pickle=True); args = json.loads(str(d['args'])); p = float(d['p']); nt = len(d['th'])
    A, K = datum(args)
    tmin = float(args.get('tmin', -14)); tmax = float(args.get('tmax', 10))
    F = FwdStat(p, A, tmin=tmin, tmax=tmax, ppu=int(args.get('ppu', 3)), q=8, nt=nt, dti=0.01, nstep=800)
    assert np.allclose(F.r.cpu().numpy(), d['r'])
    S = F.S
    rho = torch.tensor(d['rho'], dtype=DT, device='cuda')
    al, be, _, _ = F.fields(rho)
    t0n = F.t_nodes[:, None].expand_as(F.R).reshape(-1); th0 = F.TH.reshape(-1)
    the, s, nbad = F.trace_s(al, be, t0n, th0, 0.03, 8000)
    phi = torch.rad2deg(torch.remainder(the, 2*math.pi)).reshape(F.R.shape).cpu().numpy()
    Tr = (torch.exp(-s)*F.L**p*torch.tensor(A(the.cpu().numpy()), dtype=DT, device='cuda')).reshape(F.R.shape)
    r = S.r.cpu().numpy(); w = S.w.cpu().numpy(); th = S.th.cpu().numpy(); t = np.log(r)
    sin3 = np.sin(3*th)
    nd = F.node(rho)

    def split(R):
        R = R.cpu().numpy()
        dc = (2.0/nt)*(w/r**2)[:, None]*R*sin3[None, :]
        rm3 = S.rho_modes(torch.tensor(R, device='cuda'))[:, 3]
        tail = float(-2*(torch.dot(S.ext_last.to(torch.complex128), rm3[-S.q:])/(S.L*(1 - p))).imag)
        return dc, tail
    sets = dict(up80_100=(phi >= 80) & (phi < 100), lo260_280=(phi >= 260) & (phi < 280),
                up85_95=(phi >= 85) & (phi < 95), lo265_275=(phi >= 265) & (phi < 275))
    sets['bulk'] = ~(sets['up80_100'] | sets['lo260_280'])
    bl = [tmin, -10, -6, -4, -2, tmax]
    bands = [('core t<tmin', t < tmin - 1e-12)] + [('%g..%g' % (a, b), (t >= a - 1e-12) & (t < b - 1e-12) if b < tmax else (t >= a - 1e-12))
                                                 for a, b in zip(bl[:-1], bl[1:])]
    bands.append(('t<-10 (core + tmin..-10)', t < -10 - 1e-12))
    out = dict(state=fn.split('/')[-1], p=p, nt=nt, K=K, m1=round(nd['m1'], 6), c=round(nd['c'], 5), not_exited=nbad,
               defect_T=float('%.3g' % float(((Tr - rho)/F.R**p).abs().max())))
    for lab, R in (('rho', rho), ('Trho', Tr)):
        dc, tail = split(R)
        rows = {}
        for nm, m in bands:
            rec = dict(total=round(float(dc[m].sum()), 4))
            for k, E in sets.items():
                rec[k] = round(float(dc[m[:, None] & E].sum()), 4)
            rows[nm] = rec
        rows['tail'] = round(tail, 4)
        rows['sum'] = round(float(dc.sum()) + tail, 5)
        out[lab] = rows
    out['wall'] = round(time.time() - t0, 1)
    print('CKERNEL ' + json.dumps(out), flush=True)
