# (o6): B on the lead's references ref_c6g_K<K>.json with the own evaluator bnat.py; w0 < 0 on (0, 1); inf of
# om = -w0/(u(1 - u)); fit errors against the stored c6g trace (ipm1-ver/runs/gen4/c6g_traces.npz).
import sys, time, json
sys.path.insert(0, '.')
import mpmath as mp, sympy as sp, numpy as np
from bnat import Ref, B_value
Ks = [int(k) for k in sys.argv[1].split(',')]
mode = sys.argv[2] if len(sys.argv) > 2 else 'all'
z = np.load('lead/exclusion_certificates/reference_fit/data/c6g_traces.npz')
out = {}
for K in Ks:
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
    mp.mp.dps = 40
    A = repr(d['A']); xs = mp.mpf(repr(d['x_star'])); e = 1/xs**2
    t0 = time.time()
    R = Ref(A, e, d['q_monomial'], dps=40)
    u = R.sym['u']
    res = dict(K=K, lead_B=d['B'], lead_mu0=d['mu0'])
    # w0 < 0 on (0, 1) iff om > 0 there: exact Sturm count of the roots of the numerator of om in [0, 1]
    num = sp.Poly(sp.expand(sp.cancel(R.sym['om']*(1 + u**2))), u)
    nroots = num.count_roots(0, 1)
    gv = [mp.mpf(k)/4000 for k in range(1, 4000)]
    omv = [R.om(x) for x in gv]
    kmin = min(range(len(gv)), key=lambda k: omv[k])
    um = mp.findroot(R.om1, gv[kmin]) if 0 < kmin < len(gv) - 1 else gv[kmin]
    crit = [mp.findroot(R.om1, gv[k]) for k in range(1, len(gv) - 1) if (omv[k] - omv[k-1])*(omv[k+1] - omv[k]) < 0]
    crit_vals = [(mp.nstr(c, 8), mp.nstr(R.om(c), 15)) for c in crit]
    res.update(roots_om_numerator_in_01=nroots, om_min_grid=mp.nstr(omv[kmin], 15), u_min_grid=mp.nstr(gv[kmin], 6),
               om_at_0=mp.nstr(R.om(0), 15), om_at_1=mp.nstr(R.om(1), 15), om_critical_points=crit_vals)
    print('K=%d: roots of num(om) in [0,1]: %d; om(0) = %s, om(1) = %s; grid min %s at u = %s; critical points (u, om): %s'
          % (K, nroots, res['om_at_0'], res['om_at_1'], res['om_min_grid'], res['u_min_grid'], crit_vals), flush=True)
    # fit errors against the stored trace
    x = z['x']; sel = x <= float(xs)*(1 + 1e-12)
    uu = x[sel]/float(xs)
    W = np.array([float(R.w0(mp.mpf(v))) for v in uu])
    W1f = sp.lambdify(u, sp.diff(R.sym['w0'], u), 'mpmath')
    W1 = np.array([float(W1f(mp.mpf(v))) for v in uu])
    W2 = np.array([float(R.w02(mp.mpf(v))) for v in uu])
    bands = [(0, 0.01), (0.01, 0.1), (0.1, 0.5), (0.5, 0.9), (0.9, 1.0 + 1e-12)]
    ferr = {}
    for (lo, hi) in bands:
        mk = (uu >= lo) & (uu < hi)
        e1 = np.max(np.abs(W[mk]/uu[mk] - z['w'][sel][mk]/float(xs)/uu[mk]))
        e2 = np.max(np.abs(W1[mk] - z['wp'][sel][mk]))
        e3f = np.max(np.abs(W2[mk] - float(xs)*z['wpp_fd'][sel][mk]))
        e3o = np.max(np.abs(W2[mk] - float(xs)*z['wpp_ode'][sel][mk]))
        ferr['%g-%g' % (lo, min(hi, 1))] = [e1, e2, e3f, e3o, int(mk.sum())]
    res['fit_err'] = ferr
    print('   fit errors by band [w/u, wp, x* wpp (fd), x* wpp (ode), n]:', {k: ['%.3e' % v for v in vv[:4]] + [vv[4]] for k, vv in ferr.items()}, flush=True)
    print('   lead bands:', {k: ['%.3e' % v for v in vv] for k, vv in d['max_err_w_over_u_wp_wpp_by_band'].items()}, flush=True)
    if mode != 'fit':
        R.series0(80)
        vals = {}
        fine = dict(nmid=40, wmid=mp.mpf(1)/40, ns=40, levels=14)
        runs = [('II', '0.15', {}), ('II', '0.25', {}), ('I', '0.2', {})] if mode != 'fine' else \
               [('II', '0.25', {}), ('II', '0.25', fine), ('II', '0.15', fine)]
        for which, delta, kw in runs:
            t1 = time.time()
            v, parts = B_value(R, which, mp.mpf(delta), **kw)
            tag = '%s_%s%s' % (which, delta, '_fine' if kw else '')
            vals[tag] = mp.nstr(v, 25)
            print('   B (%s) = %s   minus lead %s  (%.0fs)' % (tag, mp.nstr(v, 22), mp.nstr(v - mp.mpf(d['B']), 3), time.time() - t1), flush=True)
        res['B'] = vals
    out[K] = res
    json.dump(out, open('../../runs/o6_%s_%s.json' % (sys.argv[1].replace(',', '_'), mode), 'w'), indent=1, default=str)
