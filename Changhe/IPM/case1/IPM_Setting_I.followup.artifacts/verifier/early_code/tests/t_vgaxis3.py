"""GreenAxis jets: absolute values and absolute differences under (qf, Nth, NG) at fixed hmax; X3."""
import sys, math, time
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from vgen import Trial
from vgaxis import GreenAxis
tr = Trial('../IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz', 'cuda')
xx = np.array([0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 8.0])
cfg = [('q14 N2048', dict(qf=14, Nth=2048)), ('q18 N2048', dict(qf=18, Nth=2048)), ('q24 N2048', dict(qf=24, Nth=2048)),
       ('q14 N4096', dict(qf=14, Nth=4096)), ('q14 N2048 NG192', dict(qf=14, Nth=2048, NG=192))]
res = {}
for lab, kw in cfg:
    t0 = time.time()
    ga = GreenAxis(tr, K=6, xstar=8.6000638, xmin=1.0, q=4, hmax=0.05, **kw)
    res[lab] = ga.jets_at(xx)['w']
    print('%s %.1fs' % (lab, time.time() - t0), flush=True)
W0 = res['q14 N2048']
print('reference |W_k| (Taylor coefficients):')
for i, x in enumerate(xx):
    print('  x %.3f ' % x + ' '.join('%.3e' % W0[k, i] for k in range(7)))
for lab, W in res.items():
    if lab == 'q14 N2048':
        continue
    print(lab, 'abs diff of Taylor coefficients k = 0..6')
    for i, x in enumerate(xx):
        print('  x %.3f ' % x + ' '.join('%.1e' % abs(W[k, i] - W0[k, i]) for k in range(7)))
np.savez('verifier/early_data/t_vgaxis3.npz', xx=xx, **{k.replace(' ', '_'): v for k, v in res.items()})
