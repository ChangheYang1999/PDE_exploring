"""tabulate runs/cand_batch1.jsonl (output of tests/cand_eval.py): per state the collocation checks at the numerics nodes and
the residual between nodes, by radius band.  usage: python3 tests/cand_show.py FILE.jsonl"""
import json, sys, os
import numpy as np
rows = [json.loads(l) for l in open(sys.argv[1]) if l.startswith('{')]
bands = [(0, 10), (10, 50), (50, 100), (100, 1e9)]
print('%-34s %4s %5s %5s %6s %10s %10s %9s %8s %8s | node Dlo by band | mid Dlo by band | |lam f0| max' %
      ('state', 'Nr', 'R', 'nt', 'cl', 'lam', 'lam_nodes', 'compat', 'jet_x-1', 'fit'))
for d in rows:
    nm = os.path.basename(d['path']).replace('.pt', '')
    nb = []; mb = []
    for lo, hi in bands:
        a = [e['Dlo'] for e in d['nodes'] if lo < e['r'] <= hi]
        b = [e['Dlo'] for e in d['mid'] if lo < e['r'] <= hi]
        nb.append(max(a) if a else float('nan')); mb.append(max(b) if b else float('nan'))
    lf = max(abs(d['lam'])*e['f0'] for e in d['nodes'])
    print('%-34s %4d %5g %5d %6.3f %10.6f %10.6f %9.1e %8.1e %8.1e | %s | %s | %.3f' % (
        nm, d['Nr'], d['R'], d['nt'], d['cl'], d['lam'], d['lam_ls_nodes'], d['compat'], d['jet'][1] - 1, d['fit_err'],
        ' '.join('%7.1e' % v for v in nb), ' '.join('%7.1e' % v for v in mb), lf))
print()
print('Chebyshev tail (max_m |b_m,k|/max|b|, last 5 k) and dense-grid rel residual by decade (tailfit f0)')
for d in rows:
    nm = os.path.basename(d['path']).replace('.pt', '')
    bd = d['f0_tailfit']['by_decade']
    print('%-34s %s | %s | c=%.7f seed c_tail=%.7f exact=%.7f minVr/r=%.3f rho_min=%.1e' % (
        nm, ' '.join('%7.1e' % v for v in d['cheb_tail_rel']), ' '.join('%s:%.1e' % (k, v['rel']) for k, v in bd.items()),
        d['c'], d['seed']['c_tail'], d['seed']['c_exact'], d['minVr_r_inside'], d['rho_min_inside']))
