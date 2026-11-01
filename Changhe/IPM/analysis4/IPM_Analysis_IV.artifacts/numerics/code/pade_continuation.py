"""Analytic continuation test along the positive z axis. Scalar functionals of the series: s_n = <f_n, w> for test
vectors w (a single Fourier mode, or f_1 itself). The scalar series S(z) = sum_n s_n z^{n-1} has the singularities of
the vector series (generically). We (i) locate the poles of Pade approximants [m/m] (mpmath, 60 digits) and compare
their moduli with 1/L and their arguments with the correlation estimate; (ii) evaluate the Pade approximants at real
z beyond 1/L to test analytic continuation on the positive axis (agreement of successive approximants).
usage: pade_continuation.py CKPT [L]"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
import mpmath as mp
mp.mp.dps = 60
ff = FarField.load(sys.argv[1]); R = ff.R; N = max(ff.f); Lfit = float(sys.argv[2]) if len(sys.argv) > 2 else None
def coeff_series(k):   # a_{n,k}
    return [mp.mpf(R.to_str(ff.f[n][k]).split(' ')[0].strip('[')) if (k < len(ff.f[n])) else mp.mpf(0) for n in range(1, N + 1)]
def to_mpf(x):
    if R.name == 'arb':
        m, e = x.mid().man_exp(); return mp.mpf(int(m)) * mp.power(2, int(e))
    return mp.mpf(str(x))
series = {'a_n0 (sin theta mode)': [to_mpf(ff.f[n][0]) for n in range(1, N + 1)],
          'a_n1 (sin 3theta mode)': [to_mpf(ff.f[n][1]) if len(ff.f[n]) > 1 else mp.mpf(0) for n in range(1, N + 1)]}
for name, s in series.items():
    print(f'== functional {name}: N={N}')
    for m in (20, 30, 40, 50):
        if 2 * m + 1 > N: continue
        try:
            p, q = mp.pade(s[:2 * m + 1], m, m)
        except Exception as e:
            print('  pade failed', m, e); continue
        roots = mp.polyroots(list(reversed(q)), maxsteps=200, extraprec=200) if len(q) > 1 else []
        roots = sorted(roots, key=lambda r: abs(r))[:6]
        print(f'  [{m}/{m}] nearest poles (|z|, arg deg): ' + ', '.join(f'({float(abs(r)):.4f}, {float(mp.arg(r))*180/math.pi:+.1f})' for r in roots))
        # values on the positive axis
        zs = [0.5 / Lfit, 1.0 / Lfit, 1.5 / Lfit, 2.0 / Lfit, 3.0 / Lfit] if Lfit else [1, 2, 3]
        vals = [mp.polyval(list(reversed(p)), z) / mp.polyval(list(reversed(q)), z) for z in zs]
        print('    Pade values at z/z0 = 0.5,1,1.5,2,3: ' + ', '.join(f'{float(v):+.6e}' for v in vals))
