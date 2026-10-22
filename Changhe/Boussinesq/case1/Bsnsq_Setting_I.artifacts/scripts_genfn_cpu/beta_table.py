"""Table of the beta study (equal budgets from b300): last record, betacurv lines (rcond 1e-12), and the desingularized far
check (max R/N2 over S at t = 0 and t = 3e-3) for each state.  Usage: python3 beta_table.py tag1 tag2 ...  (runs/bfc_<tag>.npz/.log)"""
import sys, json, re, numpy as np
from desing import load
for tag in sys.argv[1:]:
    try:
        d = np.load('runs/bfc_%s.npz' % tag); h = json.loads(str(d['hist']))
    except Exception as e:
        print(tag, 'missing', e); continue
    r = h[-1]
    log = open('runs/bfc_%s.log' % tag).read()
    bc = re.findall(r'betacurv (start|end) rcond 1e-12: obj (\S+) \|J_b\| (\S+) \|P J_b\| (\S+) db\* (\S+) dB (\S+)', log)
    stop = 'stop' if 'no decrease' in log else ''
    print('%-9s recs %3d obj %.4e max %.3e far %.3e rms %.3e a0 %.3f beta %.6f %s' % (tag, len(h), r['obj'], r['maxres'],
          r['maxfar'] or 0, r['rms'], r['a0'], r['beta'], stop))
    for b in bc: print('          betacurv %-5s obj %s |PJb| %s db* %s dB %s' % (b[0], b[1], b[3], b[4], b[5]))
    if '--des' in sys.argv[0:] or True:
        dd, ds, core = load('runs/bfc_%s.npz' % tag)
        S = np.concatenate([[1e-8, 1e-4], 0.5 * (1 - np.cos(np.pi * (np.arange(101) + 0.5) / 101)), [1 - 1e-8]])
        out = []
        for t in ([0.0] if ds.qint else []) + [1e-4, 1e-3, 3e-3]:
            xh, eh, sg, _ = ds.points(np.full(S.shape, t if t > 0 else 0.0), S)
            ev = ds.evaluate(xh, eh, sg); out.append('t=%g %.2e' % (t, np.abs(ev['rN2'].numpy()).max()))
        print('          desing max R/N2: ' + '; '.join(out))
