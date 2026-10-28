"""Print the Route U norm table (B2 of the lead's 03:04Z note) from n12_norms outputs run with sigmas -2,-1,0,0.3:
 ||r F||_2 = 'rwF' at sigma=-2 ; ||F||_2 = 'w0F' at sigma=-1 ; ||grad F||_2 = 'w1DF' at sigma=0 ; ||<r>^0.7 D^2 F||_2 = 'w2D2F' at sigma=0.3.
Grid part (r <= 1e4) and far part separated; 'inf' where the far integral diverges. Dyadic profiles of the squared norms per octave."""
import sys, json, math
files = sys.argv[1:]
cols = [('||r F||_2', '-2.0', 'rwF'), ('||F||_2', '-1.0', 'w0F'), ('||grad F||_2', '0.0', 'w1DF'), ('||<r>^0.7 D^2F||_2', '0.3', 'w2D2F')]
print('%-22s' % 'potential' + ''.join('%26s' % c[0] for c in cols))
data = {}
for f in files:
    d = json.load(open(f)); data[f] = d
    row = []
    for name, sg, key in cols:
        e = d[sg][key]; g = math.sqrt(e['inner_sq']); far = e['far_sq']
        row.append('%9.4g (grid) +far %s' % (g, ('%.2e' % math.sqrt(far)) if far < 1e300 else 'inf'))
    print('%-22s' % f.split('/')[-1].replace('_routeU.json', '') + ''.join('%26s' % v for v in row))
print('\ndyadic profiles of the SQUARED grid norms per octave j (r in [2^j, 2^(j+1))), columns as above:')
for f in files:
    d = data[f]; print(f.split('/')[-1].replace('_routeU.json', ''))
    for j in range(-10, 14):
        vals = [d[sg][key]['dyadic_sq'].get(str(j), 0.0) for name, sg, key in cols]
        print('   j=%3d [%8.3g,%8.3g): ' % (j, 2.0**j, 2.0**(j+1)) + ' '.join('%10.2e' % v for v in vals))
