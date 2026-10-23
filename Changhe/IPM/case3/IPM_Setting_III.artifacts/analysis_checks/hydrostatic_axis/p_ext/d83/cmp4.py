# type (IV), d = 23: does the external pairwise Lambda (degree 72) divide my Lambda (report construction, degree 234)?
import json, pickle, glob, os
from flint import fmpz_poly
exec(open('cmpx3q.py').read().split('pairs=')[0])
ext4 = [os.path.basename(f)[:-5] for f in glob.glob(C + '*.json') if not f.endswith(('_stage.json', '_real.json'))]
ext4 = [p for p in ext4 if json.load(open(C + p + '.json')).get('pattern', {}).get('type') == 'IV']
print('external type IV:', ext4)
for f in sorted(glob.glob('sp2b_23_*.pkl')):
    import sympy as s; L = pickle.load(open(f, 'rb'))['Lambda']; M = fmpz_poly([int(t) for t in s.Poly(L, s.Symbol('x')).all_coeffs()[::-1]])
    for pid in ext4:
        E, var, sh, pos = ext(pid); E = prim(E)
        q, r = divmod(M, E)
        if r == 0:
            q2, r2 = divmod(q, E)
            print(f, M.degree(), '<-', pid, E.degree(), 'divides:', True, 'square divides:', r2 == 0, 'ext shift', sh, pos)
