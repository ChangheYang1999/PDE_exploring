"""Certified covering for the residual F = (c_l X + U).grad rho - rho over 0.005 <= r <= R_max (quadrant; F is even in x and odd in y, so |F| has quadrant symmetry).
Regime A (r_hi <= r_split): boxenc3.enclose_F (exact center jet of F to degree K, crude remainder; valid where remainders are small, r <= 0.3).
Regime B (r_lo >= r_split): fcert.FCert.enclose_F (F = rho[phi_L] + U.grad rho with tight field enclosures).
Per cell: F_hi = sup |F| bound, Fw_hi = sup |F| / r_lo^p2, F7_hi = sup |F - F_3 - F_5| / r_lo^7 (regime A only; F_3, F_5 exact jets).
Adaptive split while Fw_hi > target and depth < 4. Output JSON lines (resumable). Usage: cert_F.py state.json ckpt.json out.jsonl r0 Rmax ratio ntheta nproc target K r_split
"""
import sys, os, json, math, time
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, ctx
from cert_M import cell_box, flo, fhi

S = None; P2 = None; TARGET = None; KORD = 8; RSPLIT = 0.3; F3 = None; F5 = None
def init(state_json, ckpt_json, target, K, rsplit, taylor_json):
    global S, P2, TARGET, KORD, RSPLIT, F3, F5
    from fcert import FCert
    S = FCert(state_json, ckpt_json, prec=256); P2 = 2/S.cl - 1; TARGET = target; KORD = K; RSPLIT = rsplit
    T = json.load(open(taylor_json))
    F3 = {tuple(int(v) for v in k.split(',')): Fr(s) for k, s in T['F'].items() if sum(int(v) for v in k.split(',')) == 3}
    F5 = {tuple(int(v) for v in k.split(',')): Fr(s) for k, s in T['F'].items() if sum(int(v) for v in k.split(',')) == 5}

def jets_sup(r_hi):
    """sup over |X| <= r_hi of |F_3 + F_5| <= sum |coef| r^deg (tiny)."""
    s = sum(abs(float(v)) for v in F3.values())*r_hi**3 + sum(abs(float(v)) for v in F5.values())*r_hi**5
    return s

def work(task):
    (i, k, r_lo, r_hi, t_lo, t_hi, depth) = task
    ctx.prec = 256
    out = []; stack = [(r_lo, r_hi, t_lo, t_hi, depth)]
    while stack:
        a, b, c, d, dep = stack.pop()
        xc, yc, hx, hy = cell_box(a, b, c, d)
        t0 = time.time()
        try:
            if b <= RSPLIT:
                o = S.__class__.__mro__[1].enclose_F(S, xc, yc, hx, hy, K=KORD)      # boxenc3 version (exact jet of F)
                regime = 'A'
            else:
                o = S.enclose_F(xc, yc, hx, hy, K=KORD); regime = 'B'
            Fh = fhi(abs(o['F']))
            res = {'status': 'ok', 'regime': regime, 'F_hi': Fh, 'Fw_hi': Fh/a**float(P2), 'rem': o.get('F_rem', o.get('rhoL_rem', None))}
            if regime == 'A': res['F7_hi'] = (Fh + jets_sup(b))/a**7
            res['F_center'] = float(o['F_center'].mid()) if 'F_center' in o else None
        except Exception as e:
            res = {'status': 'error', 'error': str(e), 'Fw_hi': 1e9}
        res.update({'i': i, 'k': k, 'r_lo': a, 'r_hi': b, 't_lo': c, 't_hi': d, 'depth': dep, 'seconds': time.time()-t0})
        if res['Fw_hi'] > TARGET and dep < 4:
            rm = math.sqrt(a*b); tm = (c+d)/2
            stack += [(a, rm, c, tm, dep+1), (rm, b, c, tm, dep+1), (a, rm, tm, d, dep+1), (rm, b, tm, d, dep+1)]
            res['split'] = True
        out.append(res)
    return out

if __name__ == '__main__':
    state_json, ckpt_json, out_path = sys.argv[1:4]
    r0, Rmax, ratio = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
    ntheta, nproc, target, K, rsplit = int(sys.argv[7]), int(sys.argv[8]), float(sys.argv[9]), int(sys.argv[10]), float(sys.argv[11])
    taylor_json = sys.argv[12]
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
    print('cells', nr*ntheta, 'todo', len(tasks), 'K', K, 'target', target, 'r_split', rsplit, flush=True)
    t0 = time.time(); n = 0; worst = 0.0
    with Pool(nproc, initializer=init, initargs=(state_json, ckpt_json, target, K, rsplit, taylor_json)) as pool, open(out_path, 'a') as f:
        for out in pool.imap_unordered(work, tasks, chunksize=4):
            for res in out:
                f.write(json.dumps(res) + '\n')
                if res['status'] == 'ok' and not res.get('split'): worst = max(worst, res['Fw_hi'])
            f.flush(); n += 1
            if n % 200 == 0: print('%d/%d cells, %.0f s, worst accepted Fw_hi so far %.5f' % (n, len(tasks), time.time()-t0, worst), flush=True)
    print('done', time.time()-t0, 'worst', worst, flush=True)
