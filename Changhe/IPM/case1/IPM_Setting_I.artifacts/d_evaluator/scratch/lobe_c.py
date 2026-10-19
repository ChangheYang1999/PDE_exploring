# Lead analysis 13.15 (c) check (G65): largest near-axis lobe of the signed R/N_f at r 8.40 / 8.47 / 8.52, theta < 0.08,
# from my resmap files (own evaluator; between-node grid of vresmap.py). Prints max |R/N_f|, its theta and sign, and the mean
# zero spacing in theta < 0.08.
import sys, numpy as np
for t in sys.argv[1:]:
    d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf = d['r'], d['th'], d['R'], d['Nf']
    with np.errstate(all='ignore'): X = np.where(Nf > 0, R / Nf, 0.0)
    out = []
    for r0 in (8.40, 8.47, 8.52):
        i = int(np.argmin(np.abs(r - r0))); j = (th > 1e-6) & (th < 0.08)
        a = X[i, j]; tj = th[j]; k = int(np.argmax(np.abs(a)))
        z = tj[:-1][a[:-1] * a[1:] < 0]
        sp = float(np.mean(np.diff(z))) if len(z) > 1 else float('nan')
        out.append('r %.3f max %+.2e at th %.4f, %d zeros, spacing %.4f' % (r[i], a[k], tj[k], len(z), sp))
    print(t, 'dr %.4f dth %.5f |' % (np.median(np.diff(r)), np.median(np.diff(th))), ' | '.join(out))
