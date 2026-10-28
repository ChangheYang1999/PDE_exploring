"""Covering certificate for the Hessian of rho_bar: per cell sup of r |D^2 rho|_F (and |D^2 rho|_F), from boxenc3.enclose with the Hessian fields.
Usage: cert_H.py state.json ckpt.json out.jsonl r0 Rmax ratio ntheta nproc K"""
import sys, os, json, math, time
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, ctx
from cert_M import cell_box, fhi
S = None; KORD = 6
def init(state_json, ckpt_json, K):
    global S, KORD
    from boxenc3 import BoxEnclosure3, HESS
    S = BoxEnclosure3(state_json, ckpt_json, prec=256); KORD = K
def work(task):
    from boxenc3 import HESS
    (i, k, r_lo, r_hi, t_lo, t_hi) = task
    ctx.prec = 256
    xc, yc, hx, hy = cell_box(r_lo, r_hi, t_lo, t_hi); t0 = time.time()
    try:
        o = S.enclose(xc, yc, hx, hy, K=KORD, fields=dict(HESS))
        H2 = o['rho_xx']*o['rho_xx'] + 2*o['rho_xy']*o['rho_xy'] + o['rho_yy']*o['rho_yy']
        res = {'status': 'ok', 'H_hi': fhi(H2.sqrt()), 'rH_hi': fhi(H2.sqrt())*r_hi, 'rem': max(o['rho_xx_rem'], o['rho_xy_rem'], o['rho_yy_rem'])}
    except Exception as e:
        res = {'status': 'error', 'error': str(e)}
    res.update({'i': i, 'k': k, 'r_lo': r_lo, 'r_hi': r_hi, 't_lo': t_lo, 't_hi': t_hi, 'seconds': time.time()-t0})
    return res
if __name__ == '__main__':
    state_json, ckpt_json, out_path = sys.argv[1:4]
    r0, Rmax, ratio, ntheta, nproc, K = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])
    nr = int(math.ceil(math.log(Rmax/r0)/math.log(ratio))); radii = [r0*ratio**i for i in range(nr+1)]
    thetas = [k*math.pi/2/ntheta for k in range(ntheta+1)]
    done = set()
    if os.path.exists(out_path):
        for line in open(out_path):
            try: d = json.loads(line); done.add((d['i'], d['k']))
            except Exception: pass
    tasks = [(i, k, radii[i], radii[i+1], thetas[k], thetas[k+1]) for i in range(nr) for k in range(ntheta) if (i, k) not in done]
    print('cells', nr*ntheta, 'todo', len(tasks), flush=True); t0 = time.time(); n = 0; worst = 0
    with Pool(nproc, initializer=init, initargs=(state_json, ckpt_json, K)) as pool, open(out_path, 'a') as f:
        for res in pool.imap_unordered(work, tasks, chunksize=4):
            f.write(json.dumps(res) + '\n'); f.flush(); n += 1
            if res['status'] == 'ok': worst = max(worst, res['rH_hi'])
            if n % 400 == 0: print('%d/%d cells, %.0f s, max r|D2rho| so far %.4f' % (n, len(tasks), time.time()-t0, worst), flush=True)
    print('done', time.time()-t0, 'max rH', worst, flush=True)
