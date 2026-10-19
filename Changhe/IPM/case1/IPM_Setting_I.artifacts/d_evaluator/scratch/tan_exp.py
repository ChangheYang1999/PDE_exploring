"""G58: base field times exp(eps * tH), tH = log(F(tan_c6b+h) / F(tan_c6b-h)) / (2h) from my generator's fields of the
lead's tangent shapes: the exponential (trial-class) form of the field-level line of tan_on_c6c.py. Equals the lead's
coefficient-level transplant up to the change of L along the line (G58 (a)). Where rho = 0 (the axes) rho stays 0.
Usage (from code/): python3 ../scratch/tan_exp.py base.npz Fplus.npz Fminus.npz h eps out.npz"""
import sys
import numpy as np
bp, pp, mp, h, eps, outp = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
f = np.load(bp, allow_pickle=True); fp = np.load(pp, allow_pickle=True); fm = np.load(mp, allow_pickle=True)
for k in ('r', 'theta'):
    assert np.array_equal(f[k], fp[k]) and np.array_equal(f[k], fm[k]), k
ok = (fp['rho'] > 0) & (fm['rho'] > 0) & (f['rho'] > 0)
tH = np.zeros_like(f['rho'])
tH[ok] = np.log(fp['rho'][ok] / fm['rho'][ok]) / (2 * h)
rho = f['rho'] * np.exp(eps * tH)
out = {k: f[k] for k in f.files if k != 'rho'}
out.pop('c', None); out.pop('c_l', None)
np.savez(outp, rho=rho, eps=eps, **out)
print(dict(eps=eps, h=h, tHmax=float(np.abs(tH).max()), n_zero=int((~ok).sum()), rel_change=float(np.abs(np.expm1(eps * tH)).max())))
