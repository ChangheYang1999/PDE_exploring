"""Self-convergence of GreenAxis jets (hmax, qf, Nth) on X3 at x in [3e-3, 8.5]."""
import sys, math, time
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from vgen import Trial
from vgaxis import GreenAxis
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
xx = np.concatenate([np.geomspace(3e-3, 0.3, 5), np.geomspace(0.5, 8.5, 6)])
res = {}
for lab, kw in [('ref h.05 q14 N2048', dict(hmax=0.05, qf=14, Nth=2048)), ('h.025 q14 N2048', dict(hmax=0.025, qf=14, Nth=2048)),
                ('h.05 q20 N2048', dict(hmax=0.05, qf=20, Nth=2048)), ('h.05 q14 N4096', dict(hmax=0.05, qf=14, Nth=4096)),
                ('h.05 q14 N2048 tlo1e-10 thi1e14', dict(hmax=0.05, qf=14, Nth=2048, t_lo=math.log(1e-10), t_hi=math.log(1e14)))]:
    t0 = time.time()
    ga = GreenAxis.__new__(GreenAxis)
    GreenAxis.__init__(ga, tr, K=6, xstar=8.6000638, **kw) if False else None
    # build only what jets_at needs (no axis panels)
    ga = GreenAxis(tr, K=6, xstar=8.6000638, xmin=1.0, q=4, **kw)
    W = ga.jets_at(xx)['w']
    res[lab] = (W, ga.info['M_n'][0])
    print('%s: %.1fs M_1/2 %.15f' % (lab, time.time() - t0, ga.info['M_n'][0] / 2), flush=True)
W0 = res['ref h.05 q14 N2048'][0]
for lab, (W, M) in res.items():
    if lab.startswith('ref'):
        continue
    print(lab)
    for i, x in enumerate(xx):
        print('  x %.4f rel diff jets 0..6: ' % x + ' '.join('%.1e' % (abs(W[k, i] - W0[k, i]) / (abs(W0[k, i]) + 1e-300)) for k in range(7)))
