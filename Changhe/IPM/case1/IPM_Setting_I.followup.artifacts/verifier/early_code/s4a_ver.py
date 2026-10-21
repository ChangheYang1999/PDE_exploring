"""verifier: SPEC S4 (a) recomputed with this lane's estimator on the first-run gen4 axis traces (written for this run).
Primary estimator: trace_axis.b3_ibp_full (w-only form integrated by parts on [0, x*]; needs w'' only), on
trace_axis.TraceAxis data (one-sided fits at x*, h(P) regularization).  Validated on exact R12 data sampled on the same
grid (tests/t_trace_r12.py: floor 5e-8; 1e-9 white noise on w'' gives 1e-4).
Variants: data (fits, near-x* least squares, regularization), windows xlo in {0.17, 0.34, 0.5}, xc in {2.0, 2.6, 3.0, 3.5},
deg in {8, 12}, end pieces (frac_e, end_deg) in {(0.92, 6), (0.88, 6), (0.96, 4), (0.92, 8)}.
Usage: s4a_ver.py name1,name2,... wppkey tag"""
import sys, time, math, json
sys.path.insert(0, 'verifier/early_code')
import numpy as np
from trace_axis import TraceAxis, b3_ibp_full, b3_trace
from vaxis import B3

D = 'first-run-records/ver/runs/gen4/'
names = sys.argv[1].split(',')
wppkey = sys.argv[2] if len(sys.argv) > 2 else 'wpp_ode'
tag = sys.argv[3] if len(sys.argv) > 3 else 'run'
WINS = [(a, c, deg) for a in (0.17, 0.34, 0.5) for c in (2.0, 2.6, 3.0, 3.5) for deg in (8, 12)]
ENDS = [(0.92, 6), (0.88, 6), (0.96, 4), (0.92, 8)]
DATA = {'near3': dict(near_frac=0.03), 'near3b': dict(near_frac=0.03, near_fit=(40, 8)),
        'near6': dict(near_frac=0.06, near_fit=(40, 6)), 'ls24': dict(fit01=(24, 11), fit2=(24, 11)),
        'ls24n3': dict(fit01=(24, 11), fit2=(24, 11), near_frac=0.03), 'centred': dict(onesided=False),
        'near3Ag': dict(near_frac=0.03, reg='Ag')}
# (the one-sided 12-point interpolation extrapolated to x* is excluded: it amplifies the sample noise, h(P) - 1 = -3e-5
#  on fxn24g against +7e-7 centred and -1e-6 to -8e-6 with least squares)
out = {}
for nm in names:
    path = D + nm + '_traces.npz'
    rec = {}
    for dk, kw in DATA.items():
        t0 = time.time()
        ad = TraceAxis(path, wppkey=wppkey, **kw)
        b = B3(ad)
        v = np.array([[b3_ibp_full(b, xlo, xc, deg=deg, frac_e=fe, end_deg=ed)['Bnat'] for fe, ed in ENDS]
                      for xlo, xc, deg in WINS])                         # (24, 4)
        f2 = np.array([b3_trace(b, 'F2b', xlo, xc, deg=deg)['Bnat'] for xlo, xc, deg in WINS])
        rec[dk] = dict(c_l_file=ad.c_l_file, c_l_used=ad.c_l, xs=ad.xs, hP_file=ad.hP_file, ibp=v.tolist(), F2b=f2.tolist())
        print('%-8s %-7s %-8s c_l %.9f (used %.9f) x* %.7f h(P)-1 %+.2e | ibp med %.5f [%.5f, %.5f] by end %s | '
              'F2b(fit) med %.5f [%.5f, %.5f] (%.0f s)' % (
                  nm, wppkey, dk, ad.c_l_file, ad.c_l, ad.xs, ad.hP_file - 1, np.median(v), v.min(), v.max(),
                  '/'.join('%.5f' % np.median(v[:, k]) for k in range(len(ENDS))), np.median(f2), f2.min(), f2.max(),
                  time.time() - t0), flush=True)
    out[nm] = rec
    json.dump(out, open('verifier/early_data/s4a_ver_%s_%s.json' % (tag, wppkey), 'w'))
