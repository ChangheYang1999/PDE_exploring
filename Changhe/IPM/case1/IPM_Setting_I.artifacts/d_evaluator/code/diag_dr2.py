"""Run the DR (vdr) and save full snapshots at chosen times, for inspection of the onset of grid-scale structure."""
import sys, json, time
import numpy as np
from vdr import DR

cfg = json.loads(sys.argv[1])
dr = DR(N=cfg['N'], M=cfg['M'], r0=cfg.get('r0', 1e-5), R=cfg.get('R', 1e12), filt=cfg.get('filt'))
dr.ghost_follow_k = True
dr.inner_outflow_free = bool(cfg.get('iof', 1))
dr.hv = cfg.get('hv')
F = dr.init_field(cfg.get('L2', 4.67), cfg.get('k0', 0.67))
# closure exponent (velocity tail beyond R and outer ghosts); defaults to the initial far-field exponent k0
k = cfg.get('kcl', cfg.get('k0', 0.67))
tsave = list(cfg['tsave'])
tau, n = 0.0, 0
snaps, taus, cls = [], [], []
t0 = time.time()
while tsave:
    if n % 20 == 0:
        dt, cl = dr.dt_cfl(F, cfg.get('cfl', 0.5), k)
    F, cl = dr.step(F, dt, k)
    tau += dt
    n += 1
    if n % cfg.get('every', 500) == 0:
        print(json.dumps(dict(step=n, tau=tau, dt=dt, cl=cl, wall=time.time() - t0, maxF=float(np.abs(F).max()))), flush=True)
    if tau >= tsave[0]:
        snaps.append(F.copy()); taus.append(tau); cls.append(cl)
        print(json.dumps(dict(snap=1, tau=tau, cl=cl, wall=time.time() - t0)), flush=True)
        tsave.pop(0)
        np.savez(cfg['out'], F=np.array(snaps), tau=np.array(taus), cl=np.array(cls), r=dr.r, ms=dr.ms, cfg=json.dumps(cfg))
    if not np.isfinite(F).all():
        break
