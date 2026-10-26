"""Tests of basis860: maps, old-function identities, jets/strain vs frozen code, monomial identities (Decimal)."""
import json, math, sys, time
from decimal import Decimal, localcontext
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import basis860 as B
import numpy as np
from absolute_fields import core_matrices as old_core_matrices, center_data as old_center_data, _core_exponents
sys.path.insert(0, str(Path(__file__).resolve().parents[2]/"research"/"base"/"engine")); from taylor_jet import series as old_series
from spectral_basis import evaluate_modes
from absolute_common import read, ROOT
out = {'version': B.VERSION, 'checks': []}
def check(name, value, tol=None, **extra):
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL')
# manifest counts
check('canonical_count_860', len(B.CANONICAL) == 860); check('internal_count_860', len(B.CORE)+len(B.EXTRA) == 860)
check('canonical_unique', len(set(B.CANONICAL)) == 860)
T = B.conversion_matrix(); out['conversion_matrix_condition_float'] = float(np.linalg.cond(T)); check('conversion_matrix_block_diagonal_nonzero', all(abs(T[B.canonical_index(j,m,m+i),B.CORE_INDEX[(m,i,j)]])==1 for (m,i,j) in B.CORE) and all(T[B.canonical_index(j,m,max(5,m)+n),60+B.EXTRA_INDEX[(m,n,j)]]!=0 for (m,n,j) in B.EXTRA))
sv = np.linalg.svd(T, compute_uv=False); out['conversion_matrix_singular_values'] = {'max': float(sv[0]), 'min': float(sv[-1])}
# round trip internal -> canonical -> internal (Decimal)
rng = np.random.default_rng(7); c = rng.normal(size=60); g = rng.normal(size=800)*1e-3
a = B.internal_to_canonical_exact(c, g); c2, g2 = B.canonical_to_internal_exact(a)
check('roundtrip_core_max_abs', float(max(abs(Decimal(repr(float(v)))-w) for v, w in zip(c, c2))), 1e-40)
check('roundtrip_extra_max_abs', float(max(abs(Decimal(repr(float(v)))-w) for v, w in zip(g, g2))), 1e-40)
check('float_T_vs_exact_max_rel', float(np.max(abs(T@np.r_[c, g]-np.array([float(v) for v in a]))/np.maximum(1, abs(np.array([float(v) for v in a]))))), 1e-12)
# accepted278 embedding and its monomial coefficient sizes
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json')
from absolute_fields import prepare_candidate
prep = prepare_candidate(cand, 'center_chart')
c278, g278 = B.embed_old(prep['coefficients'], prep['extra'], prep['modes'])
a278 = B.internal_to_canonical_exact(c278, g278)
out['accepted278_monomial_max_abs'] = float(max(abs(v) for v in a278)); out['accepted278_internal_max_abs'] = float(max(np.max(abs(c278)), np.max(abs(g278))))
out['accepted278_nonzero_internal'] = int(np.count_nonzero(c278)+np.count_nonzero(g278))
# jets and strain of old core functions vs frozen taylor_jet.series / center_data at several cl
for cl in (1.8089923602744993, 1.5, 2.5, 3.7):
    old = old_series(cl); new = B.jets(cl); newd = B.jets(cl, decimal=True); oc = old_center_data(cl); nc = B.center_data(cl)
    err = 0.; errd = 0.; es = 0.
    for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
        terms = B.old_core_to_internal(m, s)
        if len(terms) > 1: continue  # (3,2) is a 3-term relation, tested through the field identity below
        jnew = terms[0][1]
        err = max(err, max(abs(float(u)-float(v)) for u, v in zip(old[jold], new[jnew])))
        errd = max(errd, max(abs(float(u)-float(v)) for u, v in zip(old[jold], newd[jnew])))
        es = max(es, abs(oc[0][jold]-nc[0][jnew]), abs(oc[1][jold]-nc[1][jnew]), abs(oc[2][jold]-nc[2][jnew]), abs(oc[3][jold]-nc[3][jnew]))
    check('old_core_jets_match_cl%.4f' % cl, err, 1e-12); check('old_core_jets_decimal_match_cl%.4f' % cl, errd, 1e-9); check('old_core_strain_f0_match_cl%.4f' % cl, es, 1e-12)
    # strain consistency: s_i == 4*h_i (jet h)
    check('strain_equals_jet_h_cl%.4f' % cl, float(max(abs(nc[0][i]-float(new[i][6])) for i in range(60))), 1e-12)
    check('f0_equals_jet_a_cl%.4f' % cl, float(max(abs(nc[2][i]-float(new[i][0])) for i in range(60))), 1e-12)
    # high-k (k>=5) generators have zero jets: all extra functions have potential degree >= 10 by construction (t^{max(5-m,0)} H_m)
# core_matrices: old 24 functions vs new at random points, several cl, with cl derivatives
x = np.r_[rng.uniform(0, 3, 40), 0., 1e-9, 2., 50., 1e4]; y = np.r_[rng.uniform(0, 3, 40), 1.3, 2e-9, 0., 1e-9, 3e3]
for cl in (1.8089923602744993, 1.3, 2.9):
    oM, odM = old_core_matrices(cl, x, y, True); nM, ndM = B.core_matrices(cl, x, y, True)
    e = 0.; ed = 0.
    V, dV = evaluate_modes(x, y, cl, [{'family': 'global', 'm': 3, 'n': 0, 'sigma': 0.0}], True)
    for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
        terms = B.old_core_to_internal(m, s)
        for key in B.KEYS:
            val = sum(f*(nM[key][:, idx] if kind == 'core' else V[key][:, 0]) for kind, idx, f in terms)
            dval = sum(f*(ndM[key][:, idx] if kind == 'core' else dV[key][:, 0]) for kind, idx, f in terms)
            # Exclude entries that vanish by symmetry (rounding residue only): require |old| above 1e-10 of the pointwise term size.
            size = sum(abs(nM[key][:, idx] if kind == 'core' else V[key][:, 0]) for kind, idx, f in terms)
            use = abs(oM[key][:, jold]) > 1e-10*size
            if np.any(use): e = max(e, float(np.max(abs(oM[key][use, jold]-val[use])/abs(oM[key][use, jold]))))
            dsize = sum(abs(ndM[key][:, idx] if kind == 'core' else dV[key][:, 0]) for kind, idx, f in terms)
            use = abs(odM[key][:, jold]) > 1e-10*dsize
            if np.any(use): ed = max(ed, float(np.max(abs(odM[key][use, jold]-dval[use])/abs(odM[key][use, jold]))))
    check("old_core_fields_rel_cl%.4f" % cl, e, 1e-8); check("old_core_cl_derivative_rel_cl%.4f" % cl, ed, 1e-8)
# extra modes: j=0 modes identical dicts to old modes
old_modes = cand['modes']; new_modes = B.extra_modes()
check('old_modes_embedded_identical_dicts', all(new_modes[B.old_mode_to_internal(md)] == md for md in old_modes))
# Monomial identities in Decimal at points: sum_k a_k chi_{mkj}(x,y) vs internal function values, several cl.
def chi_mon(m, k, j, cl, xx, yy):
    L = Decimal(cl); p = B.p_exponents(L)[0][j]; q = xx*xx+yy*yy; R = 1+q
    z = complex(float(xx), float(yy))  # H_m via Decimal binomial expansion of Re(x+iy)^{2m}
    H = sum(Decimal((-1)**l*math.comb(2*m, 2*l))*xx**(2*m-2*l)*yy**(2*l) for l in range(m+1))
    return H*q**(k-m)*(R.ln()*(p-k)).exp()
def internal_core_value(m, i, j, cl, xx, yy):
    L = Decimal(cl); p = B.p_exponents(L)[0][j]; q = xx*xx+yy*yy; R = 1+q
    H = sum(Decimal((-1)**l*math.comb(2*m, 2*l))*xx**(2*m-2*l)*yy**(2*l) for l in range(m+1))
    return H*(R.ln()*(p-m-i)).exp()
def legendre(n, z):
    p0, p1 = Decimal(1), z
    if n == 0: return p0
    for k in range(1, n): p0, p1 = p1, ((2*k+1)*z*p1-k*p0)/(k+1)
    return p1
def internal_extra_value(m, n, j, cl, xx, yy):
    L = Decimal(cl); p = B.p_exponents(L)[0][j]; q = xx*xx+yy*yy; R = 1+q; t = q/R
    H = sum(Decimal((-1)**l*math.comb(2*m, 2*l))*xx**(2*m-2*l)*yy**(2*l) for l in range(m+1))
    return H*(R.ln()*(p-m)).exp()*t**max(5-m, 0)*Decimal(2*n+1).sqrt()*legendre(n, 2*t-1)
worst = 0.; rows = []
with localcontext() as ctx:
    ctx.prec = 60
    pts = [(Decimal('0.3'), Decimal('0.7')), (Decimal('2.5'), Decimal('0.1')), (Decimal('0.01'), Decimal('0.02')), (Decimal('40'), Decimal('17'))]
    for cl in ('1.8089923602744993', '1.3', '4.1'):
        for (m, i, j) in [(0, 0, 0), (0, 4, 0), (2, 1, 1), (3, 1, 3), (4, 0, 2), (1, 3, 0)]:
            col = np.zeros(60); col[B.CORE_INDEX[(m, i, j)]] = 1.; a = B.internal_to_canonical_exact(col, np.zeros(800))
            for xx, yy in pts:
                lhs = sum(a[B.canonical_index(j, m, k)]*chi_mon(m, k, j, cl, xx, yy) for k in range(m, 26) if a[B.canonical_index(j, m, k)])
                rhs = internal_core_value(m, i, j, cl, xx, yy); rel = abs(lhs-rhs)/max(abs(rhs), Decimal('1e-300')); worst = max(worst, float(rel))
        for (m, n, j) in [(0, 0, 0), (0, 20, 0), (3, 0, 0), (5, 17, 2), (9, 16, 3), (7, 5, 1), (2, 13, 0)]:
            col = np.zeros(800); col[B.EXTRA_INDEX[(m, n, j)]] = 1.; a = B.internal_to_canonical_exact(np.zeros(60), col)
            for xx, yy in pts:
                lhs = sum(a[B.canonical_index(j, m, k)]*chi_mon(m, k, j, cl, xx, yy) for k in range(m, 26) if a[B.canonical_index(j, m, k)])
                rhs = internal_extra_value(m, n, j, cl, xx, yy); rel = abs(lhs-rhs)/max(abs(rhs), Decimal('1e-300')); worst = max(worst, float(rel))
                rows.append({'cl': cl, 'mnj': [m, n, j], 'x': str(xx), 'y': str(yy), 'rel': float(rel)})
check('monomial_identities_decimal60_worst_rel', worst, 1e-40)
# old core offsets identity (spec rule 1 and 2) directly: H_m R^{A-m-s} vs sum (-1)^h C(s,h) chi_{m,m+h,0} already covered by core identity; check offsets mapping values
for cl in (1.8089923602744993, 2.2):
    oe = _core_exponents(cl); ne = B.core_exponents(cl)
    single = [(jo, B.old_core_to_internal(*B.OLD_CORE_ORDER[jo])) for jo in range(24)]
    single = [(jo, t_[0][1]) for jo, t_ in single if len(t_) == 1]
    check('old_core_exponent_b_match_cl%.3f' % cl, float(max(abs(oe[jo][1]-ne[jn][1]) for jo, jn in single)), 1e-15)
    check('old_core_exponent_db_match_cl%.3f' % cl, float(max(abs(oe[jo][2]-ne[jn][2]) for jo, jn in single)), 1e-15)
out['passed'] = all(r['passed'] for r in out['checks'])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED')
