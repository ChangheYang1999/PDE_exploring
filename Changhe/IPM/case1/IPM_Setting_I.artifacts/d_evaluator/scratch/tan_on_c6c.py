"""G51: c6c segment 1 field + eps * (lead c6b soft tangent, field level), my generator only.
t = (F(tan_c6b+h) - F(tan_c6b-h)) / (2h), central difference of my generator's fields of the lead's tangent shapes.
Usage (from code/): python3 ../scratch/tan_on_c6c.py base.npz Fplus.npz Fminus.npz h eps out.npz"""
import sys
import numpy as np
bp, pp, mp, h, eps, outp = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
f = np.load(bp, allow_pickle=True); fp = np.load(pp, allow_pickle=True); fm = np.load(mp, allow_pickle=True)
for k in ('r', 'theta'):
    assert np.array_equal(f[k], fp[k]) and np.array_equal(f[k], fm[k]), k
t = (fp['rho'] - fm['rho']) / (2 * h)
rho = f['rho'] + eps * t
out = {k: f[k] for k in f.files if k != 'rho'}
out.pop('c', None); out.pop('c_l', None)
np.savez(outp, rho=rho, eps=eps, **out)
print(dict(eps=eps, h=h, tmax=float(np.abs(t).max()), rel_change=float(np.abs(eps * t).max() / np.abs(f['rho']).max())))
