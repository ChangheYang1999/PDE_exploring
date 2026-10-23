# compare the full Lambda coefficient lists of the external recomputation with the main-analysis gen19.py (lead)
import json, sys
src = open('../../d81/gen19.py').read().split("CASES = {15:")[0]
sys.argv = ['x']; exec(src)
r = json.load(open('resultants.json'))
MAP = {'(1; 3, 2, 1, 1)': ('three', (15, 1, 6, 4, 2)), '(1; 2, 2, 1, 1, 1)': ('two', (15, 1, 4, 2, 3)),
       '(1; 4, 2, 1, 1)': ('three', (17, 1, 8, 4, 2)), '(1; 3, 2, 2, 1)': ('three', (17, 1, 6, 2, 4)),
       '(3; 3, 2, 1, 1)': ('three', (17, 3, 6, 4, 2)), '(1; 2, 2, 2, 1, 1)': ('two', (17, 1, 2, 4, 3)),
       '(3; 2, 2, 1, 1, 1)': ('two', (17, 3, 4, 2, 3)), '(1; 2, 2, 1, 1, 1, 1)': ('two', (17, 1, 4, 2, 4))}
for rec in r:
    kind, args = MAP[rec['pattern']]
    F, G = (three if kind == 'three' else two)(*args)
    R = s.Poly(s.resultant(F.as_expr(), G.as_expr(), p), x).primitive()[1]
    if R.LC() < 0: R = -R
    mine = [int(c) for c in R.all_coeffs()]
    theirs = [int(c) for c in rec['coefficients_descending']]
    print(rec['pattern'], len(mine), mine == theirs, flush=True)
