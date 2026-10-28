"""Covering certificate for W = U - DU(0) X (components W1 = U1 - (c_l-1) x, W2 = U2 - (1-c_l) y) and for K_bar = rho[phi_K] on cells r <= Rmax:
per cell sup|W|/r_lo^3 (N4) and inf K_bar. The linear coordinate parts are subtracted at the jet level (exact), so the enclosure width is that of a
cubic-order field. Usage: cert_W.py state.json ckpt.json out.jsonl r0 Rmax ratio ntheta nproc K"""
import sys, os, json, math, time
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flint import arb, ctx
from cert_M import cell_box, flo, fhi

S = None; KORD = 8
def init(state_json, ckpt_json, K):
    global S, KORD
    from fcert import FCert
    S = FCert(state_json, ckpt_json, prec=256); KORD = K

def enclose_W(xc, yc, hx, hy, K):
    from boxenc3 import FIELDS, _arb_fr
    ctx.prec = S.prec
    xcA = _arb_fr(Fr(xc)); ycA = _arb_fr(Fr(yc)); hxA = _arb_fr(Fr(hx)); hyA = _arb_fr(Fr(hy))
    xabs = abs(xcA) + hxA; yabs = abs(ycA) + hyA
    xmin = abs(xcA) - hxA; ymin = abs(ycA) - hyA
    xmin = xmin if xmin > 0 else arb(0); ymin = ymin if ymin > 0 else arb(0)
    q_lo = xmin*xmin + ymin*ymin; q_hi = xabs*xabs + yabs*yabs
    J = S.phi_jet(xcA, ycA, 3 + K)
    crude = S.crude_phi(xabs, yabs, q_lo, q_hi, 3 + K + 1)
    dx = arb(0, float(hxA.upper())); dy = arb(0, float(hyA.upper()))
    dxp = [arb(1)]; dyp = [arb(1)]; hxp = [arb(1)]; hyp = [arb(1)]
    for i in range(K+2): dxp.append(dxp[-1]*dx); dyp.append(dyp[-1]*dy); hxp.append(hxp[-1]*hxA); hyp.append(hyp[-1]*hyA)
    out = {}
    for name, comb, lin in (('W1', FIELDS['U1'], ('x', S.cl - 1)), ('W2', FIELDS['U2'], ('y', 1 - S.cl))):
        poly = arb(0)
        for b1 in range(K+1):
            for b2 in range(K+1-b1):
                coef = sum((c*J[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
                if (b1, b2) == (0, 0): coef = coef - lin[1]*(xcA if lin[0] == 'x' else ycA)
                if (b1, b2) == ((1, 0) if lin[0] == 'x' else (0, 1)): coef = coef - lin[1]
                poly += coef*dxp[b1]*dyp[b2]/(math.factorial(b1)*math.factorial(b2))
        rem = arb(0)
        for b1 in range(K+2):
            b2 = K+1-b1
            coef = sum((abs(c)*crude[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
            rem += coef*hxp[b1]*hyp[b2]/(math.factorial(b1)*math.factorial(b2))
        out[name] = poly + arb(0, float(rem.upper())); out[name+'_rem'] = float(rem.upper())
    # K_bar = rho[phi_K]
    JK = S.jet_branches(S.branches('K'), xcA, ycA, 3 + K)
    crudeK = S.crude_branches(S.radial_specs('K'), xabs, yabs, q_lo, q_hi, 3 + K + 1)
    comb = FIELDS['rho']; poly = arb(0)
    for b1 in range(K+1):
        for b2 in range(K+1-b1):
            coef = sum((c*JK[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
            poly += coef*dxp[b1]*dyp[b2]/(math.factorial(b1)*math.factorial(b2))
    rem = arb(0)
    for b1 in range(K+2):
        b2 = K+1-b1
        coef = sum((abs(c)*crudeK[(a+b1, b+b2)] for (a, b), c in comb.items()), arb(0))
        rem += coef*hxp[b1]*hyp[b2]/(math.factorial(b1)*math.factorial(b2))
    out['K'] = poly + arb(0, float(rem.upper())); out['K_rem'] = float(rem.upper())
    return out

def work(task):
    (i, k, r_lo, r_hi, t_lo, t_hi) = task
    ctx.prec = 256
    xc, yc, hx, hy = cell_box(r_lo, r_hi, t_lo, t_hi)
    t0 = time.time()
    try:
        o = enclose_W(xc, yc, hx, hy, KORD)
        W = (abs(o['W1'])*abs(o['W1']) + abs(o['W2'])*abs(o['W2'])).sqrt()
        res = {'status': 'ok', 'W_hi': fhi(W), 'W_over_r3_hi': fhi(W)/r_lo**3, 'W1_rem': o['W1_rem'], 'W2_rem': o['W2_rem'], 'K_lo': flo(o['K']), 'K_hi': fhi(o['K']), 'K_rem': o['K_rem']}
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
    print('cells', nr*ntheta, 'todo', len(tasks), flush=True)
    t0 = time.time(); n = 0
    with Pool(nproc, initializer=init, initargs=(state_json, ckpt_json, K)) as pool, open(out_path, 'a') as f:
        for res in pool.imap_unordered(work, tasks, chunksize=4):
            f.write(json.dumps(res) + '\n'); f.flush(); n += 1
            if n % 400 == 0: print('%d/%d cells, %.0f s' % (n, len(tasks), time.time()-t0), flush=True)
    print('done', time.time()-t0, flush=True)
