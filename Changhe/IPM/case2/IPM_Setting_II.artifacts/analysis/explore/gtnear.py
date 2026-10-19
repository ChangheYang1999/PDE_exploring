# Lead exploration: behaviour of G, Gt and |Xi| near the strong exit angle 90 deg of a saved x-even state.
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
st = np.load(sys.argv[1]); p = float(sys.argv[2]); k = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
Af = lambda t: np.abs(np.cos(t)) ** k
nA = 4096
ng = FE.node_and_G(p, Af, st['g'], st['lr'], st['th'], nA=nA)
th = ng['thA']; m1 = ng['m1']; lAn = ng['logAn']; lXi = m1 * lAn
lA = np.log(np.maximum(ng['A'], 1e-300))
i0 = 0
for d in (0, 30, 60, 75, 80, 85, 88, 89, 89.5, 89.8, 89.9):
    i = int(round(np.radians(d) / (2 * np.pi) * nA))
    print('%6.2f  log|Xi| %9.4f  logG %9.4f  logGt %9.4f  log|90-th| %8.4f' % (np.degrees(th[i]), lXi[i] - lXi[0],
          (lA - lAn)[i] - (lA - lAn)[0], (lA - 2 * lXi)[i] - (lA - 2 * lXi)[0], np.log(abs(np.pi / 2 - th[i]) + 1e-300)))
