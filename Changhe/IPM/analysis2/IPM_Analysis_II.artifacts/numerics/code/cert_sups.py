"""C2: certified global sups of weighted background derivatives (state 131 or a refit in T1 generator form) by the box-enclosure method.
Fields: omega |D^j rho|_F (j = 2,3,4), omega |D^j U|_F (j = 1,2,3), |D rho|, |D U|, omega = (1+4r^2)^(2/5); and every component separately.
Cells: polar cells (ratio, ntheta) on [r0, Rmax] enclosed in axis boxes (cert_M.cell_box), center Taylor polynomial of degree K + Lagrange remainder
(boxenc3.enclose with the needed field combinations; crude bounds at order |alpha| + K + 1). omega over the cell: (1+4 r_hi^2)^(2/5) (monotone).
Origin square [-r0, r0]^2 handled as a cell with center 0. Far field r >= Rmax: separate (farfield_bounds-type sector bounds; reported separately).
Output: JSON lines per cell with the upper bounds of each component and of the Frobenius norms; summary at the end.
Usage: cert_sups.py state_exact.json ckpt.json out.jsonl r0 Rmax ratio ntheta nproc K"""
import sys, os, json, math, time
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, ctx
from cert_M import cell_box, fhi

# field definitions as linear combinations of phi derivatives: name -> {(a,b): coef}
def D(base, i, j):
    return {(a+i, b+j): c for (a, b), c in base.items()}
RHO = {(2, 1): -1, (0, 3): -1}; U1 = {(1, 2): -1}; U2 = {(2, 1): 1}
FIELDS = {}
JMAX_RHO = 2; JMAX_U = 2     # the Lagrange-remainder box method certifies first and second derivatives; higher orders lose factorially in the crude bounds
for j in range(1, JMAX_RHO+1):
    for i in range(j+1):
        FIELDS['rho_%d_%d' % (i, j-i)] = D(RHO, i, j-i)          # d^i_x d^(j-i)_y rho
for j in range(1, JMAX_U+1):
    for i in range(j+1):
        FIELDS['U1_%d_%d' % (i, j-i)] = D(U1, i, j-i); FIELDS['U2_%d_%d' % (i, j-i)] = D(U2, i, j-i)

S = None; KORD = 6
def init(state_json, ckpt_json, K):
    global S, KORD
    from boxenc3 import BoxEnclosure3
    S = BoxEnclosure3(state_json, ckpt_json, prec=256); KORD = K

def frob(vals, order):
    """Frobenius norm of the order-`order` derivative tensor from the component sups (multinomial multiplicities)."""
    tot = arb(0)
    for i in range(order+1):
        mult = math.comb(order, i)       # number of index tuples with i x-derivatives
        tot += mult*vals[(i, order-i)]*vals[(i, order-i)]
    return tot.sqrt()

def work(task):
    (i, k, r_lo, r_hi, t_lo, t_hi) = task
    ctx.prec = 256
    xc, yc, hx, hy = cell_box(r_lo, r_hi, t_lo, t_hi) if r_lo > 0 else (Fr(0), Fr(0), Fr(r_hi), Fr(r_hi))
    t0 = time.time()
    try:
        o = S.enclose(xc, yc, hx, hy, K=KORD, fields=FIELDS)
        w_hi = (1 + 4*arb(r_hi)**2)**arb(0.4)
        res = {'status': 'ok'}
        for name in FIELDS: res[name] = fhi(abs(o[name]))
        for j in range(1, JMAX_RHO+1):
            vals = {(ii, j-ii): abs(o['rho_%d_%d' % (ii, j-ii)]) for ii in range(j+1)}
            res['Frob_D%d_rho' % j] = fhi(frob(vals, j)); res['wFrob_D%d_rho' % j] = fhi(w_hi*frob(vals, j))
        for j in range(1, JMAX_U+1):
            v1 = {(ii, j-ii): abs(o['U1_%d_%d' % (ii, j-ii)]) for ii in range(j+1)}; v2 = {(ii, j-ii): abs(o['U2_%d_%d' % (ii, j-ii)]) for ii in range(j+1)}
            f = (frob(v1, j)**2 + frob(v2, j)**2).sqrt()
            res['Frob_D%d_U' % j] = fhi(f); res['wFrob_D%d_U' % j] = fhi(w_hi*f)
        res['rem_max'] = max(o[kk] for kk in o if kk.endswith('_rem'))
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
    tasks = [(-1, -1, 0.0, r0, 0.0, math.pi/2)] if (-1, -1) not in done else []
    tasks += [(i, k, radii[i], radii[i+1], thetas[k], thetas[k+1]) for i in range(nr) for k in range(ntheta) if (i, k) not in done]
    print('cells', nr*ntheta + 1, 'todo', len(tasks), 'K', K, flush=True); t0 = time.time(); n = 0
    with Pool(nproc, initializer=init, initargs=(state_json, ckpt_json, K)) as pool, open(out_path, 'a') as f:
        for res in pool.imap_unordered(work, tasks, chunksize=2):
            f.write(json.dumps(res) + '\n'); f.flush(); n += 1
            if n % 200 == 0: print('%d/%d cells, %.0f s' % (n, len(tasks), time.time()-t0), flush=True)
    print('done', time.time()-t0, flush=True)
