# Random-pair test of [f]_a <= 1 for the gated two-point test function (sanity check only).
import numpy as np
from explore_lower import f, u
rng = np.random.default_rng(1)
for a in [0.05, 0.25, 0.5, 0.9]:
    best = 0; bu = 0
    for it in range(40):
        p = rng.normal(size=(200000, 2))*rng.choice([0.05, 0.3, 1, 3], size=(200000,1))
        d = rng.normal(size=(200000, 2))*np.exp(rng.uniform(-8, 2, size=(200000,1)))
        q = p + d
        fp = f(p[:,0], p[:,1], a); fq = f(q[:,0], q[:,1], a)
        ratio = np.abs(fp-fq)/np.linalg.norm(d, axis=1)**a
        best = max(best, ratio.max())
        up = u(p[:,0], p[:,1], a); uq = u(q[:,0], q[:,1], a)
        bu = max(bu, (np.abs(up-uq)/np.linalg.norm(d, axis=1)**a).max())
    print(a, "max ratio f:", best, " u:", bu)
