"""V60: check of specification v3.7 M25(i) addendum 04:56Z (lead): e_p of the N = 6 datum with a_2 changed is -0.130 / -0.033 / +0.064 / +0.156 at
a_2 = -0.714 / -0.9 / -1.1 / -1.3 (zero near a_2 = -0.97); with the odd part removed and a_2 = -1.1, w_e/r^p = +0.054. Uses the
spectral stream-function evaluation and the closed formula of tests/v56_ep_general.py (sign calibrated there on cos^2).
Datum A = cos^2 th exp(F), F = a1 sin th + a2 cos 2th + a3 sin 3th + a4 cos 4th + a5 sin 5th + a6 cos 6th.
Usage: python3 tests/v60_ep_a2.py"""
import sys, numpy as np
sys.argv = ['x']
import importlib.util
spec = importlib.util.spec_from_file_location('v56', 'tests/v56_ep_general.py')
src = open('tests/v56_ep_general.py').read().split("P = (0.2")[0]
ns = {}; exec(src, ns)
we_ratio, formula = ns['we_ratio'], ns['formula']
p = 0.49568
cf = -2*(p + 1)/(p*(p + 2)*(p + 4)); sg = np.sign(we_ratio(lambda t: np.cos(t)**2, p)/cf)
base = [0.239, -0.7141, -0.2097, 0.122, 0.107, -0.027]
def A(a):
    return lambda t: np.cos(t)**2*np.exp(a[0]*np.sin(t) + a[1]*np.cos(2*t) + a[2]*np.sin(3*t) + a[3]*np.cos(4*t) + a[4]*np.sin(5*t) + a[5]*np.cos(6*t))
for odd in (1, 0):
    for a2 in (-0.7141, -0.9, -0.97, -1.1, -1.3):
        a = list(base); a[1] = a2
        if not odd: a[0] = a[2] = a[4] = 0.0
        print('odd part %s  a_2 %+.4f  e_p spectral %+.5f  formula %+.5f' % ('base' if odd else 'zero', a2, sg*we_ratio(A(a), p), formula(A(a), p)))
for odd in (1, 0):
    lo, hi = -0.9, -1.1
    for _ in range(50):
        mid = 0.5*(lo + hi); a = list(base); a[1] = mid
        if not odd: a[0] = a[2] = a[4] = 0.0
        if formula(A(a), p) < 0: lo = mid
        else: hi = mid
    print('odd part %s: e_p = 0 at a_2 = %.4f' % ('base' if odd else 'zero', 0.5*(lo + hi)))
