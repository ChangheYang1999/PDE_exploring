"""Evaluate all background fields of a state on a polar grid with the arb evaluator (ball arithmetic), in parallel.
Saves midpoints and radii of the balls. Usage: grid_eval.py state_exact.json out.npz smin smax ds ntheta nproc [prec] [order]
Grid: r = exp(s), s in [smin, smax] step ds; theta in [0, pi/2] with ntheta points (Chebyshev-like interior: theta_i = (i+0.5)/ntheta * pi/2, plus the two axes).
"""
import sys, os, time, math, json
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ipm_arb import State
from flint import arb, ctx

STATE = None
PREC = 192
ORDER = 5
def init(path, prec, order):
    global STATE, PREC, ORDER
    STATE = State(path, prec=prec); PREC = prec; ORDER = order

KEYS = ['rho', 'rho_x', 'rho_y', 'U1', 'U2', 'psi', 'F', 'DU11', 'DU12', 'DU21', 'DU22', 'K', 'rho_xx', 'rho_xy', 'rho_yy']

def work(args):
    s, th = args
    ctx.prec = PREC
    r = arb(s).exp(); x = r*arb(th).cos(); y = r*arb(th).sin()
    if th == 0: y = arb(0)
    if abs(th - math.pi/2) < 1e-15: x = arb(0)
    f = STATE.fields(x, y, order=ORDER)
    vals = {k: f[k] for k in ['rho', 'rho_x', 'rho_y', 'U1', 'U2', 'psi', 'F']}
    vals['DU11'], vals['DU12'] = f['DU'][0]; vals['DU21'], vals['DU22'] = f['DU'][1]
    vals['K'] = f['rho'] - x*f['rho_x'] - y*f['rho_y']
    if ORDER >= 5:
        vals['rho_xx'], vals['rho_xy'], vals['rho_yy'] = f['rho_xx'], f['rho_xy'], f['rho_yy']
    else:
        vals['rho_xx'] = vals['rho_xy'] = vals['rho_yy'] = arb(0)
    mid = [float(vals[k].mid()) for k in KEYS]
    # outward-rounded radius: ball radius plus the binary64 rounding error of the midpoint (V016 of the verifier)
    rad = [math.nextafter(float(abs(vals[k] - arb(float(vals[k].mid()))).upper()), math.inf) for k in KEYS]
    return float(x.mid()), float(y.mid()), mid, rad

if __name__ == '__main__':
    path, out, smin, smax, ds, ntheta, nproc = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
    prec = int(sys.argv[8]) if len(sys.argv) > 8 else 192; order = int(sys.argv[9]) if len(sys.argv) > 9 else 5
    svals = np.arange(smin, smax + ds/2, ds)
    thetas = [0.0] + [((i + 0.5)/ntheta)*math.pi/2 for i in range(ntheta)] + [math.pi/2]
    tasks = [(float(s), float(th)) for s in svals for th in thetas]
    print('tasks', len(tasks), flush=True)
    t0 = time.time()
    with Pool(nproc, initializer=init, initargs=(path, prec, order)) as pool:
        res = []
        for i, r in enumerate(pool.imap(work, tasks, chunksize=8)):
            res.append(r)
            if i % 2000 == 0: print(i, time.time() - t0, flush=True)
    X = np.array([r[0] for r in res]); Y = np.array([r[1] for r in res])
    MID = np.array([r[2] for r in res]); RAD = np.array([r[3] for r in res])
    np.savez(out, x=X, y=Y, s=np.repeat(svals, len(thetas)), theta=np.tile(thetas, len(svals)), mid=MID, rad=RAD, keys=np.array(KEYS), prec=prec, order=order, state=path)
    print('done', time.time() - t0, flush=True)
