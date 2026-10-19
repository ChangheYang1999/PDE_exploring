"""Diagnose the onset of the DR instability: track c_l, high angular mode content and radial grid-scale content."""
import sys, json, time
import numpy as np
from vdr import DR

cfg = json.loads(sys.argv[1])
dr = DR(N=cfg['N'], M=cfg['M'], r0=cfg.get('r0', 1e-5), R=cfg.get('R', 1e3), filt=cfg.get('filt'))
dr.ghost_follow_k = bool(cfg.get('fixk'))
dr.inner_outflow_free = bool(cfg.get('iof'))
dr.hv = cfg.get('hv')
F = dr.init_field(cfg.get('L2', 4.67), cfg.get('k0', 0.67))
k = cfg.get('k0', 0.67)
tau, n = 0.0, 0
r = dr.r
hi = dr.ms > dr.M // 2
snaps = []
t0 = time.time()
while tau < cfg['tmax']:
    if n % 20 == 0:
        dt, cl = dr.dt_cfl(F, cfg.get('cfl', 0.5), k)
        if cfg.get('fixk') is None and cl > 1:
            k = 1 / cl
    F, cl = dr.step(F, dt, k)
    tau += dt
    n += 1
    if n % cfg.get('every', 50) == 0:
        amp = np.abs(F).max(1)
        d2 = np.abs(np.diff(F, 2, axis=1)).max(0) / (np.abs(F).max(0)[1:-1] + 1e-300)
        j = int(np.argmax(d2))
        rec = dict(tau=tau, wall=time.time() - t0, cl=cl, dt=dt, k=k, hi=float(amp[hi].max() / amp.max()), d2=float(d2.max()), r_d2=float(r[j + 1]),
                   f1R=float(F[0, -1]), f3R=float(F[1, -1]))
        print(json.dumps(rec), flush=True)
        snaps.append(F.copy())
        if not np.isfinite(F).all() or dt < 1e-5:
            break
np.savez(cfg['out'], F=np.array(snaps[-40:]), r=r, ms=dr.ms)
