# Sampled fit errors of the referee's fitted reference (fred23/01 fitted_reference.json) against the stored c6g trace,
# in the normalization of run_o6.py (u = x/L0, w~ = w/L0), by band; also the sup of |w~ error| on 0.02 <= u <= 0.985.
import json
import numpy as np, mpmath as mp
mp.mp.dps = 30
d = json.load(open('fred23/01-obstruction/data/fitted_reference.json'))
A0 = mp.mpf(d['A0_exact']); L0 = mp.mpf(d['L0_exact']); q = [mp.mpf(s) for s in d['q_power_coefficients_exact_decimal']]
def w0(u):
    t = u*u
    return -A0*u*(1 - t)/(1 + t) + u**3*(1 - t)**2*mp.polyval(q[::-1], t)
def w1(u): return mp.diff(w0, u)
z = np.load('lead/exclusion_certificates/reference_fit/data/c6g_traces.npz')
x = z['x']; sel = x <= float(L0)*(1 + 1e-12)
uu = x[sel]/float(L0); wt = z['w'][sel]/float(L0); wp = z['wp'][sel]
W = np.array([float(w0(mp.mpf(v))) for v in uu]); W1 = np.array([float(w1(mp.mpf(v))) for v in uu])
for lo, hi in [(0, 0.01), (0.01, 0.1), (0.1, 0.5), (0.5, 0.9), (0.9, 1 + 1e-12)]:
    mk = (uu >= lo) & (uu < hi)
    print('band %g-%g: n %d, max|w/u err| %.3e, max|w err| %.3e, max|w\' err| %.3e' % (lo, min(hi, 1), mk.sum(),
          np.max(np.abs((W - wt)[mk]/uu[mk])), np.max(np.abs((W - wt)[mk])), np.max(np.abs((W1 - wp)[mk]))))
mk = (uu >= 0.02) & (uu <= 0.985)
print('0.02 <= u <= 0.985: n %d, max|w err| %.4e, max|w/u err| %.4e' % (mk.sum(), np.max(np.abs((W - wt)[mk])), np.max(np.abs((W - wt)[mk]/uu[mk]))))
