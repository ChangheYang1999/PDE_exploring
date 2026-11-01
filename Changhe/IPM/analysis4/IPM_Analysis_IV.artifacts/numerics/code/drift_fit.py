"""Drift fits of the period-3 multiplier of the canonical 2/3 log series (section 5.11b (b5)). Reads the cycle_diag.py outputs given on the
command line (later files win for duplicated orders), takes the resonance-shifted density multiplier a_n ('a_n shift', which = F) at the
class-0 orders, prints the per-period increments of log10 |a_n|, and fits three models on each window [w0, n_max]:
  power:  log10 |a_n| = c + beta log10 n          (multiplier growing like n^beta; Gevrey-type)
  1/n:    log10 |a_n| = log10 a_inf + c1 / n       (approach to a finite limit multiplier a_inf; the form of V529)
  linear: log10 |a_n| = c + s n                    (multiplier growing exponentially in n)
The multipliers are the four-significant-digit values printed by cycle_diag.py (V534); the verifier holds full-precision values (V529).
usage: drift_fit.py w0[,w0b,...] cycle_diag_file [more files...]"""
import sys, math
import numpy as np
w0s = [int(x) for x in sys.argv[1].split(',')]
mult = {}
for path in sys.argv[2:]:
    for line in open(path):
        p = line.split()
        if len(p) < 8 or not p[0].isdigit(): continue
        n, cls, which = int(p[0]), int(p[1]), p[2]
        if cls == 0 and which == 'F': mult[n] = float(p[6])
ns = sorted(mult)
print('orders covered:', ns[0], '..', ns[-1], '(rms values are in log10 |a_n| units)')
print('class-0 multipliers:', ' '.join(f"{n}:{mult[n]:.5f}" for n in ns[-7:]))
inc = [(ns[i], math.log10(abs(mult[ns[i]])) - math.log10(abs(mult[ns[i-1]]))) for i in range(1, len(ns)) if ns[i] - ns[i-1] == 3]
print('per-period increments of log10|a| (class-0 orders ' + str(inc[0][0] - 3) + '..):', ' '.join(f"{v:+.5f}" for _, v in inc))
for w0 in w0s:
    sel = [n for n in ns if n >= w0]; x = np.array(sel, float); a = np.array([abs(mult[n]) for n in sel]); la = np.log10(a)
    cb = np.polyfit(np.log10(x), la, 1); r1 = la - np.polyval(cb, np.log10(x))
    c2 = np.polyfit(1.0 / x, la, 1); r2 = la - np.polyval(c2, 1.0 / x); ainf = 10.0 ** c2[1]
    c3 = np.polyfit(x, la, 1); r3 = la - np.polyval(c3, x)
    rms = lambda r: math.sqrt(float(np.mean(r * r)))
    print(f"window {w0}..{sel[-1]}: power beta = {cb[0]:.3f} (rms {rms(r1):.1e}); 1/n: |a_inf| = {ainf:.5f}, c1 = {c2[0]:.1f} (rms {rms(r2):.1e}); linear in n: slope {c3[0]:.6f}/order (rms {rms(r3):.1e})")
