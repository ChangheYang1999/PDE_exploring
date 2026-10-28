"""Summary table of all N12 potentials: S14 norms at sigma = 0.15 / 0.3 / 0.4 (from *_norms.json), near-field indicators, sup |F|, sector norms."""
import sys, json, math, glob, os
files = sys.argv[1:]
print('%-18s %-9s %-9s %-9s | %-9s %-9s %-9s | %-9s %-9s %-9s | %-9s %-9s %-9s | %-8s' % ('potential', 's.15 w0', 'w1', 'w2', 's.3 w0', 'w1', 'w2', 's.4 w0', 'w1', 'w2', 'sup|F|', 'F(r~1)', 'F/r^3<.1', 'E2 norm'))
for f in files:
    d = json.load(open(f)); name = os.path.basename(f).replace('_norms.json', '').replace('_exact', '').replace('state131_T1', 'checkpoint')
    row = []
    for sg in ('0.15', '0.3', '0.4'):
        row += [d[sg]['w0F']['norm'], d[sg]['w1DF']['norm'], d[sg]['w2D2F']['norm']]
    e2 = d['sectors'].get('2,0', {}).get('norm_L2_quarter', float('nan'))
    # near-field indicators were printed, not stored; recover sup
    print('%-18s %-9.4g %-9.4g %-9.4g | %-9.4g %-9.4g %-9.4g | %-9.4g %-9.4g %-9.4g | %-9.4g %-9s %-9s | %-8.4g' % (name, *row, d['sup_F'], '-', '-', e2))
