"""Table of the lead's weight set (C1): ||r F||_2, ||F||_2, ||grad F||_2, ||(1+4r^2)^0.4 D^2 F||_2 with far parts, |F| and |D^2 F| at r = 1,
and the octave profile of the weighted Hessian squared norm."""
import sys, json, math, os
files = sys.argv[1:]
cols = [('||r F||_2', 'rF'), ('||F||_2', 'F'), ('||grad F||_2', 'gradF'), ('||(1+4r^2)^.4 D^2F||_2', 'wLD2F')]
print('%-14s' % 'potential' + ''.join('%27s' % c[0] for c in cols) + '%12s %12s' % ('|F|(r=1)', '|D2F|(r~1)'))
data = {}
for f in files:
    d = json.load(open(f)); data[f] = d; L = d['L']
    row = []
    for name, key in cols:
        g = math.sqrt(L[key]['inner_sq']); far = L[key]['far_sq']
        row.append('%8.4g +far %s' % (g, ('%.2e' % math.sqrt(far)) if far < 1e300 else 'inf'))
    print('%-14s' % os.path.basename(f).replace('_lead.json', '').replace('_exact', '').replace('state131_T1', 'checkpoint') + ''.join('%27s' % v for v in row) + '%12.3e %12.3e' % (d.get('F_at_r1', float('nan')), d.get('D2F_at_r1', float('nan'))))
print('\noctave profile of ||(1+4r^2)^0.4 D^2 F||^2 (grid part), j: r in [2^j, 2^(j+1)):')
hdr = '   j  ' + ''.join('%14s' % os.path.basename(f).replace('_lead.json', '').replace('_exact', '').replace('state131_T1', 'ckpt') for f in files); print(hdr)
for j in range(-10, 14):
    print('  %3d ' % j + ''.join('%14.3e' % data[f]['L']['wLD2F']['dyadic_sq'].get(str(j), 0.0) for f in files))
