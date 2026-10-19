"""Compare my evaluator's signed R/N_v (runs/farP json, c_l = 1/k and identity c_l) with my own series (code/far2_ver.py)
at the evaluator's exact columns. Usage: python3 scratch/farS.py farP.json shape.npz out.json"""
import sys, json
import numpy as np
sys.path.insert(0, 'code')
from far2_ver import main as far2
P = json.load(open(sys.argv[1]))
Nt = P['Nt']; k = P['k']
out, prof = far2(sys.argv[2], Nt * 16, ())
cols = sorted(set(x['j'] for x in P['rows']))
res = []
for x in P['rows']:
    j = x['j']; r = x['r']; d = r ** (k - 1)
    i = j * 16
    terms = [prof['q1'][i] * d, prof['q2'][i] * d ** 2, prof['qh'][i] * r ** -2, prof['q3'][i] * d ** 3]
    S = sum(terms)
    lead = terms[0]
    sc = S / lead
    rw = [w / sc for w in x['ratio_win']]       # window of measured / series (series/leading taken at the centre node)
    res.append(dict(r_L=x['r_L'], theta=x['theta'], cl=x['cl'], meas=x['R_over_Nv'], series=S, terms=terms,
                    ratio=x['R_over_Nv'] / S, win=rw, series_over_leading=sc))
json.dump(res, open(sys.argv[3], 'w'), indent=1)
for y in res:
    if y['theta'] > 1.56 or abs(y['theta'] - 0.8173) < 1e-3:
        print('%4s r %9.4g L th %.5f meas %+.5e series %+.5e  meas/series %.5f [%.4f %.4f]  series/lead %.4f' % (
            y['cl'], y['r_L'], y['theta'], y['meas'], y['series'], y['ratio'], *y['win'], y['series_over_leading']))
