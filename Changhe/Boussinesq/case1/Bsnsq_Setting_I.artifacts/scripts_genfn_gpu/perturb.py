"""Perturbation control for the history branches (3.28): copies of a state with Gaussian noise added to the outer (c) and core (cc) coefficients,
delta = sigma * rms(block) * N(0, 1), fixed seed; hist reset. Usage: perturb.py STATE OUTPREFIX sigma1,sigma2,... [--seed s]"""
import sys, numpy as np, json
f, pre = sys.argv[1], sys.argv[2]; sigmas = [float(a) for a in sys.argv[3].split(',')]
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 7
d = np.load(f, allow_pickle=True); base = {k: d[k] for k in d.files}
for sg in sigmas:
    rng = np.random.default_rng(seed); out = dict(base)
    for k in ('c', 'cc'):
        if k in out:
            v = np.array(out[k], dtype=float); out[k] = v + sg * np.sqrt(np.mean(v ** 2)) * rng.standard_normal(v.shape)
    out['hist'] = json.dumps([]); out['init'] = '%s perturbed sigma %g seed %d' % (f, sg, seed)
    name = '%s_s%s.npz' % (pre, ('%.0e' % sg).replace('e-0', 'e-').replace('+', ''))
    np.savez(name, **out); print(name, 'sigma', sg, '|dc|/|c| %.3e' % (np.linalg.norm(out['c'] - base['c']) / np.linalg.norm(base['c'])))
