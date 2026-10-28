"""Certified covering of the quadrant r <= R_max by boxes (boxenc3) : per box, rigorous lower bound of lambda_min(M), of M22-(c_l+2),
of rho_y, of K_bar (theta > 0), and upper bound of |F| <r>^{-p_2} and of |F|/r^7 (r <= 0.1). Adaptive splitting when lambda_min bound < target.
Resumable: results appended as JSON lines; cells already present are skipped.
Usage: cert_M.py state_exact.json checkpoint.json out.jsonl r0 Rmax ratio ntheta nproc target K
"""
import sys, os, json, math, time
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, ctx


def flo(b):
    """binary64 lower bound of an arb ball (outward rounded by one ulp)."""
    v = float(b.lower()); return math.nextafter(v, -math.inf)
def fhi(b):
    v = float(b.upper()); return math.nextafter(v, math.inf)

S = None; CL = None; P2 = None; TARGET = None; KORD = 8
def init(state_json, ckpt_json, target, K):
    global S, CL, P2, TARGET, KORD
    from boxenc3 import BoxEnclosure3
    S = BoxEnclosure3(state_json, ckpt_json, prec=256); CL = S.cl; P2 = 2/S.cl - 1; TARGET = target; KORD = K

def cell_box(r_lo, r_hi, t_lo, t_hi):
    """Enclosing box of the polar cell (first quadrant) with certified endpoints: cos/sin evaluated in arb on the exact (rational) angles,
    outward-rounded to rationals; a cell touching the float pi/2 endpoint gets x_lo = 0, which covers the sliver up to the exact axis."""
    from flint import arb as _arb, ctx as _ctx
    _ctx.prec = 128
    tl = _arb(Fr(t_lo).numerator)/Fr(t_lo).denominator; th = _arb(Fr(t_hi).numerator)/Fr(t_hi).denominator
    def lo(v): return Fr(float(v.lower()))*(1 - Fr(1, 2**40)) if float(v.lower()) > 0 else Fr(0)
    def hi(v): return Fr(float(v.upper()))*(1 + Fr(1, 2**40))
    x_lo = Fr(r_lo)*lo(th.cos()) if t_hi < math.pi/2 else Fr(0)
    x_hi = Fr(r_hi)*hi(tl.cos())
    y_lo = Fr(r_lo)*lo(tl.sin()) if t_lo > 0 else Fr(0)
    y_hi = Fr(r_hi)*hi(th.sin())
    return (x_lo+x_hi)/2, (y_lo+y_hi)/2, (x_hi-x_lo)/2, (y_hi-y_lo)/2

def analyze(o):
    from boxenc3 import Mmin
    lm, (M11, M22, M12) = Mmin(o, CL)
    r2 = o['x']*o['x'] + o['y']*o['y']
    Fw = abs(o['F'])/(1 + r2)**(P2/2)
    res = {'lam_min_lo': flo(lm), 'lam_min_hi': fhi(lm), 'M22_minus_cl2_lo': flo(M22 - CL - 2), 'M11_lo': flo(M11), 'absM12_hi': fhi(abs(M12)),
           'rho_y_lo': flo(o['rho_y']), 'Fw_hi': fhi(Fw), 'F_hi': fhi(abs(o['F'])), 'K_lo': flo(o['K']),
           'rem_max': max(o[k] for k in o if k.endswith('_rem') and k not in ('phi_rem', 'psi_rem'))}
    for k in ['rho', 'rho_x', 'rho_y', 'U1', 'U2', 'DU11', 'DU12', 'DU21', 'DU22', 'F', 'K']:
        res[k+'_lo'] = flo(o[k]); res[k+'_hi'] = fhi(o[k])
    return res

def work(task):
    (i, k, r_lo, r_hi, t_lo, t_hi, depth) = task
    ctx.prec = 256
    out = []
    stack = [(r_lo, r_hi, t_lo, t_hi, depth)]
    while stack:
        a, b, c, d, dep = stack.pop()
        xc, yc, hx, hy = cell_box(a, b, c, d)
        t0 = time.time()
        try:
            o = S.enclose(xc, yc, hx, hy, K=KORD)
            res = analyze(o); res['status'] = 'ok'
        except Exception as e:
            res = {'status': 'error', 'error': str(e), 'lam_min_lo': -1e9}
        res.update({'i': i, 'k': k, 'r_lo': a, 'r_hi': b, 't_lo': c, 't_hi': d, 'depth': dep, 'seconds': time.time()-t0})
        if res['lam_min_lo'] < TARGET and dep < 4:
            rm = math.sqrt(a*b); tm = (c+d)/2
            stack += [(a, rm, c, tm, dep+1), (rm, b, c, tm, dep+1), (a, rm, tm, d, dep+1), (rm, b, tm, d, dep+1)]
            res['split'] = True
        out.append(res)
    return out

def origin_work(h, K):
    ctx.prec = 256
    o = S.enclose(0, 0, Fr(h), Fr(h), K=K)
    res = analyze(o); res.update({'origin_box_h': h, 'status': 'ok'})
    return res

if __name__ == '__main__':
    state_json, ckpt_json, out_path = sys.argv[1:4]
    r0, Rmax, ratio = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
    ntheta, nproc, target, K = int(sys.argv[7]), int(sys.argv[8]), float(sys.argv[9]), int(sys.argv[10])
    done = set()
    if os.path.exists(out_path):
        for line in open(out_path):
            try:
                d = json.loads(line)
                if d.get('depth') == 0: done.add((d['i'], d['k']))
            except Exception: pass
    nr = int(math.ceil(math.log(Rmax/r0)/math.log(ratio)))
    radii = [r0*ratio**i for i in range(nr+1)]
    thetas = [k*math.pi/2/ntheta for k in range(ntheta+1)]
    tasks = [(i, k, radii[i], radii[i+1], thetas[k], thetas[k+1], 0) for i in range(nr) for k in range(ntheta) if (i, k) not in done]
    print('cells', nr*ntheta, 'todo', len(tasks), 'K', K, 'target', target, flush=True)
    t0 = time.time(); n = 0
    with Pool(nproc, initializer=init, initargs=(state_json, ckpt_json, target, K)) as pool, open(out_path, 'a') as f:
        if not done:
            for h in (0.005, 0.01, 0.02):
                res = pool.apply(origin_work, (h, K)); res['i'] = -1; res['k'] = -1; res['depth'] = 0
                f.write(json.dumps(res) + '\n'); f.flush()
                print('origin box h=%g: lam_min >= %.6f, M22-(cl+2) >= %.3e, rem %.1e' % (h, res['lam_min_lo'], res['M22_minus_cl2_lo'], res['rem_max']), flush=True)
        worst = 1e9
        for out in pool.imap_unordered(work, tasks, chunksize=4):
            for res in out:
                f.write(json.dumps(res) + '\n')
                if res['status'] == 'ok' and not res.get('split'): worst = min(worst, res['lam_min_lo'])
            f.flush(); n += 1
            if n % 200 == 0: print('%d/%d cells, %.0f s, worst accepted lam_min_lo so far %.5f' % (n, len(tasks), time.time()-t0, worst), flush=True)
    print('done', time.time()-t0, 'worst', worst, flush=True)
