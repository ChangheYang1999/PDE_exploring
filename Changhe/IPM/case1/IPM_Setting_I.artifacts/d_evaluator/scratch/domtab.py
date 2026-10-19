# Verifier scratch (shift 7): canonical-law (formula continued) domain table for the answer to astra ref7 item 7.
import json, sys, os
A = 'runs/audit/'
rows = [('dom90g', '_frm'), ('dom300g', '_frm'), ('c6g', ''), ('c6g2', ''), ('dom9000g', '_frm'), ('dom9000g', '_frm44')]
cfgs = ['N11250_q384', 'N16875_q512', 'N22500_q384']
keys = [('r<=1000,ya>=0.006', 'flux_max', 'Nf A5 r<=1000'), ('|X-P|<0.5', 'flux_max', 'Nf |X-P|<0.5'),
        ('r<=1000,ya>=0.006', 'Nv_max', 'Nv A5 r<=1000'), ('r>1000,ya>=0.006', 'Nv_max', 'Nv A5 r>1000'),
        ('1000<=r<=R', 'Nv_max', 'Nv all r>=1000')]
for t, suf in rows:
    for c in cfgs:
        f = A + '%s_%s_R7.652e6%s.json' % (t, c, suf)
        if not os.path.exists(f):
            continue
        d = json.load(open(f)); res = {e['region']: e for e in d['residual']}
        conv = {k: d[k] for k in ('k_self', 'rfit', 'Rfit', 'closure', 'convention') if k in d}
        s = '  '.join('%s %.3e' % (lab, res[reg][fld]) for reg, fld, lab in keys if reg in res)
        print('%-9s%-7s %-12s %s %s' % (t, suf, c, s, conv))
