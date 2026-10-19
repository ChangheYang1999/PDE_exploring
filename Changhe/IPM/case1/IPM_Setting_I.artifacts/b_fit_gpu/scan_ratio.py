"""scan_ratio.py A.json B.json: quick_scan_fit band maxima of fit A, of fit B, and the ratios A / B (same grid required).
Bands: whole box, r <= 0.1, 0.1-2, 2-10 (N_f and N_v), 10-100, 100-1000, 1000-R (N_f and N_v; physical radii: 1000 = 131 L), rms whole box; h(P)-1, x*, c_l."""
import json, sys, gzip
def _load(path):  # plain or gzipped JSON (the packaged scans are *.json.gz)
    return json.load(gzip.open(path, 'rt') if path.endswith('.gz') else open(path))
A = _load(sys.argv[1]); B = _load(sys.argv[2])
assert (A['nr'], A['nt']) == (B['nr'], B['nt']), 'grids differ'
print('%s / %s at %d x %d' % (sys.argv[1].split('/')[-1], sys.argv[2].split('/')[-1], A['nr'], A['nt']))
rows = [('whole-box N_f', 'all/all', 'max'), ('whole-box N_v', 'all/all', 'N4_max'), ('r<=0.1 N_f', 'r<=0.1/all', 'max'),
        ('0.1-2 N_f', '0.1<=r<=2/all', 'max'), ('2-10 N_f', '2<=r<=10/all', 'max'), ('2-10 N_v', '2<=r<=10/all', 'N4_max'),
        ('10-100 N_f', '10<=r<=100/all', 'max'), ('10-100 N_v', '10<=r<=100/all', 'N4_max'), ('100-1000 N_f', '100<=r<=1000/all', 'max'),
        ('100-1000 N_v', '100<=r<=1000/all', 'N4_max'), ('1000-R N_f', '1000<=r<=R/all', 'max'), ('1000-R N_v', '1000<=r<=R/all', 'N4_max'),
        ('whole-box rms', 'all/all', 'rms'), ('1000-R N_v rms', '1000<=r<=R/all', 'N4_rms')]
for name, band, key in rows:
    a = A['bands'][band][key]; b = B['bands'][band][key]
    loc = ''
    if key == 'max': loc = '  at (r %.3f, th %.3f) / (r %.3f, th %.3f)' % (A['bands'][band]['r_max'], A['bands'][band]['theta_max'], B['bands'][band]['r_max'], B['bands'][band]['theta_max'])
    print('  %-16s %.4e / %.4e = %.3f%s' % (name, a, b, a / b if b else float('nan'), loc))
print('  h(P)-1 %+.2e / %+.2e; x* %.6f / %.6f (rel %+.2e); c_l %.9f / %.9f (diff %+.3e); R_inv %s / %s' % (
    A['hP'] - 1, B['hP'] - 1, A['xstar'], B['xstar'], A['xstar'] / B['xstar'] - 1, A['cl'], B['cl'], A['cl'] - B['cl'], A['R_inverse_shape_units'], B['R_inverse_shape_units']))
