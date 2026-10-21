"""B_3 (natural units) on the stored first-run axis traces (first-run verifier gen4 traces, both w'' forms),
by the lead's b3core (32-variant medians of the original R10 form and of the ibp form, and the fixed configuration)."""
import sys, time
import numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'b3infl')); import b3core
D = os.environ.get('TRACE_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'traces')) + os.sep
names = sys.argv[1].split(',')
for nm in names:
    z = np.load(D + nm + '_traces.npz', allow_pickle=True)
    cl = float(z['c_l'])
    for form in ('wpp_ode', 'wpp_fd'):
        t0 = time.time()
        x, w, wp, wpp = z['x'], z['w'], z['wp'], z[form]
        try:
            Bo, Bi, d = b3core.b3_one(x, w, wp, wpp, cl, both=True)
            s = b3core.b3_median(x, w, wp, wpp, cl)
            gP = np.interp(d['xs'], d['x'], d['g'])
            print('%-14s %-7s c_l %.9f x* %.7f g* %.5f | one orig %.5f ibp %.5f | med orig %.5f [%.5f, %.5f] ibp %.5f '
                  '[%.5f, %.5f] (%.1f s)' % (nm, form, cl, d['xs'], gP, Bo, Bi, s['orig_median'], s['orig_min'],
                                             s['orig_max'], s['ibp_median'], s['ibp_min'], s['ibp_max'], time.time() - t0),
                  flush=True)
        except Exception as e:
            print(nm, form, 'FAILED', repr(e), flush=True)
