#!/usr/bin/env python3
"""Compare linear-response columns of the parity-free Jacobian across settings (eps_rel, filter, mask).
usage: python3 tests/pfwd_par_colcmp.py runs/pfwd/par/A_J.npz runs/pfwd/par/B_J.npz [...]  (first file = reference)
Prints per common column: the record residuals (Hessenberg, TSVD, true, full, core), the x-odd row values (b-LSQ rows, M_up, M_dn, psi_yy0 [, G_up, G_dn]) and the
relative difference of the x-odd part of the column to the reference, |c - c_ref| / |c_ref| (x-odd rows only), plus the x-even leak |c_even| / |c_odd|."""
import sys, json, numpy as np
files = sys.argv[1:]
data = []
for fn in files:
    d = np.load(fn, allow_pickle=True); J = d['J']; cols = [str(c) for c in d['cols']]; rows = [str(r) for r in d['row_names']]; recs = json.loads(str(d['recs']))
    data.append((fn, J, cols, rows, recs))
fn0, J0, cols0, rows0, recs0 = data[0]
odd_rows = np.array([r.startswith('b') or r in ('M_up', 'M_dn', 'psi_yy0', 'G_up', 'G_dn') for r in rows0])
print('rows:', rows0); print('odd rows:', [r for r, o in zip(rows0, odd_rows) if o])
def recof(recs, cols, cname):
    for r in recs:
        if cols and 'col' in r and r['col'] < len(rows0) + 100:
            pass
    for r in recs:
        if r.get('col') is not None and r.get('name', None) == cname: return r
    # lincol records carry the column index j; map through the column names of the full unknown list a1..aK, b1..bKo, [t1, t2], p
    return None
for fn, J, cols, rows, recs in data:
    print('\n==', fn)
    for rec in recs:
        j = rec['col']; print('  col j=%d  eps_rel %g smooth %s kang %s sig_lr %s tsvd %s lrcut %s | resid: hess %.3g tsvd %.3g true %.3g full %s core %s | |v| %.3g |y_full| %.3g | H_sv min %.3g max %.3g | dF_odd %.3g dF_even %.3g' % (
            j, rec['eps_rel'], rec.get('smooth'), rec.get('kang'), rec.get('sig_lr'), rec.get('tsvd'), rec.get('lrcut'), rec['gmres_resid'][-1], rec.get('resid_tsvd', float('nan')), rec['resid_true'],
            ('%.3g' % rec['resid_full']) if rec.get('resid_full') is not None else '-', ('%.3g' % rec['resid_core']) if rec.get('resid_core') is not None else '-',
            rec['v_norm'], rec.get('v_norm_full', float('nan')), min(rec['H_sv']), max(rec['H_sv']), rec['dF_odd'], rec['dF_even']))
        c = J[:, j]
        if np.all(np.isfinite(c)):
            print('     odd rows:', ' '.join('%s=%.4f' % (r, v) for r, v in zip(np.array(rows)[odd_rows], c[odd_rows])))
            print('     even leak |c_even|/|c_odd| = %.3g' % (np.linalg.norm(c[~odd_rows]) / max(np.linalg.norm(c[odd_rows]), 1e-300)))
            if fn != fn0 and np.all(np.isfinite(J0[:, j])):
                c0 = J0[:, j]; rel = np.linalg.norm((c - c0)[odd_rows]) / max(np.linalg.norm(c0[odd_rows]), 1e-300)
                print('     REL DIFF of x-odd part to reference: %.3g   (per row: %s)' % (rel, ' '.join('%.3f' % v for v in (c - c0)[odd_rows])))
