"""V33: as tests/cand_show3.py, plus the f0-free scale (cand_eval 'unforced_scale'): per band max|lam f0|/max|zeta/2| (size
of the forcing relative to the field) and max|D_mid|/max|zeta/2| (forced residual between nodes relative to the field), where
D_mid is the between-node forced residual (modes |m| <= M), band max; also rho_min and the f0-free LS lambda.
usage: python3 tests/cand_show4.py FILE.jsonl"""
import json, sys, os
rows = [json.loads(l) for l in open(sys.argv[1]) if l.startswith('{')]
bands = [(0, 1), (1, 10), (10, 100), (100, 1000), (1000, 3000.0001)]
hdr = ' '.join('%7s' % ('%g-%g' % b) for b in bands)
print('%-34s %5s %6s %9s %9s %8s %8s | mid/|lam f0|: %s | |lam f0|/|zeta/2|: %s' % ('state', 'R', 'cl', 'lam', 'lam_LS', 'compat',
      'jet-1', hdr, hdr))
for d in rows:
    if d.get('failed'):
        print(os.path.basename(d['path']), 'FAILED'); continue
    nm = os.path.basename(d['path']).replace('.pt', '')
    mb = []; fz = []
    for lo, hi in bands:
        ref = [abs(d['lam'])*e['f0'] for e in d['nodes'] if lo < e['r'] <= hi]
        b = [e['Dlo'] for e in d['mid'] if lo < e['r'] <= hi]
        mb.append(max(b)/max(ref) if b and ref else float('nan'))
        k = '%g-%g' % (lo, min(hi, d['R'])) if hi > d['R'] else '%g-%g' % (lo, hi)
        u = d.get('unforced_scale', {})
        key = [kk for kk in u if kk.split('-')[0] == '%g' % lo]
        fz.append(u[key[0]]['lamf0_over_zeta'] if key else float('nan'))
    print('%-34s %5g %6.3f %9.5f %9.5f %8.1e %8.1e | %s | %s' % (
        nm, d['R'], d['cl'], d['lam'], d['lam_ls_nodes'], d['compat'], d['jet'][1] - 1,
        ' '.join('%7.1e' % v for v in mb), ' '.join('%7.1e' % v for v in fz)))
