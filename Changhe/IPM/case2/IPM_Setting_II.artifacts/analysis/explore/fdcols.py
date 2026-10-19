# Lead: one-sided finite-difference columns of the lead-code residual (leadres.py) at a lead state, for a list of
# unknowns (mode index j = 1..K, or 0 for p), to compare with the numerics' Jacobian (their J file, optional).
# Usage: python3 withpf2.py fdcols.py state.npz outprefix "0,1,2,3" [h=0.01 hp=0.004 Jnum=path]
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import leadres as LR

st = np.load(sys.argv[1]); pre = sys.argv[2]; cols = [int(v) for v in sys.argv[3].split(',')]
o = dict(h=0.01, hp=0.004, Jnum='')
for s in sys.argv[4:]:
    k, v = s.split('='); o[k] = v if k == 'Jnum' else float(v)
K = len(st['x']); LR.setup(K, st['lr'], st['th'], pre)
x0 = np.concatenate([st['x'], [float(st['p'])]]); g0 = st['g']
Jn = np.load(o['Jnum'])['J'] if o['Jnum'] else None
log = open(pre + '.log', 'a')
def emit(d):
    s = json.dumps(d); print(s, flush=True); log.write(s + '\n'); log.flush()
F0, g, d0 = LR.evaluate(x0, g0, x0, 'base'); emit(dict(base=d0))
for c in cols:
    idx = n_idx = (len(x0) - 1) if c == 0 else c - 1
    h = o['hp'] if c == 0 else o['h']
    x = x0.copy(); x[idx] += h
    F, _, d = LR.evaluate(x, g, x0, 'col%d' % c)
    col = (F - F0) / h
    rec = dict(col=c, h=h, dm1=round(float(col[0] / LR.opt['wm']), 4), colnorm=float(np.linalg.norm(col)), lead=[round(float(v), 4) for v in col[:12]], m1=d['m1'], steps=d['steps'])
    if Jn is not None:
        jc = Jn[:, idx]
        rec.update(num_dm1=round(float(jc[0] / LR.opt['wm']), 4), num=[round(float(v), 4) for v in jc[:12]],
                   rel_diff=float(np.linalg.norm(col - jc) / max(np.linalg.norm(jc), 1e-12)))
    emit(rec)
