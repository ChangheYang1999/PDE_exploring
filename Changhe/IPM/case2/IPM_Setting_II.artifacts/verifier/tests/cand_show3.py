"""V29: tabulate runs/cand_batch3*.jsonl (tests/cand_eval.py output).  Per state: lambda (stored) vs least-squares lambda
at the numerics nodes (my evaluator), compatibility c_l - 1/2 - c, jet, then the forced residual D = R[zeta] - lambda f0
(modes |m| <= M) at the numerics nodes and at the radial midpoints between nodes, max over angle and band, relative to the
band max of |lambda f0|.  usage: python3 tests/cand_show3.py FILE.jsonl [abs]"""
import json, sys, os
rows = [json.loads(l) for l in open(sys.argv[1]) if l.startswith('{')]
ab = len(sys.argv) > 2
bands = [(0, 1), (1, 10), (10, 50), (50, 100), (100, 300), (300, 1000), (1000, 3000.0001)]
hdr = ' '.join('%7s' % ('%g-%g' % b) for b in bands)
print('%-30s %5s %6s %9s %9s %8s %8s %6s | node: %s | mid: %s' % ('state', 'R', 'cl', 'lam', 'lam_LS', 'compat', 'jet-1',
      'mVr/r', hdr, hdr))
for d in rows:
    if d.get('failed'):
        print(os.path.basename(d['path']), 'FAILED'); continue
    nm = os.path.basename(d['path']).replace('.pt', '')
    nb = []; mb = []
    for lo, hi in bands:
        ref = [abs(d['lam'])*e['f0'] for e in d['nodes'] if lo < e['r'] <= hi]
        rf = max(ref) if ref and not ab else 1.0
        a = [e['Dlo'] for e in d['nodes'] if lo < e['r'] <= hi]
        b = [e['Dlo'] for e in d['mid'] if lo < e['r'] <= hi]
        nb.append(max(a)/rf if a else float('nan')); mb.append(max(b)/rf if b else float('nan'))
    print('%-30s %5g %6.3f %9.5f %9.5f %8.1e %8.1e %6.3f | node: %s | mid: %s' % (
        nm, d['R'], d['cl'], d['lam'], d['lam_ls_nodes'], d['compat'], d['jet'][1] - 1, d['minVr_r_inside'],
        ' '.join('%7.1e' % v for v in nb), ' '.join('%7.1e' % v for v in mb)))
