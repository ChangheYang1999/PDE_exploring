"""Test of legqs_hardy on the synthetic two-scale candidate: the per-mode ||r F_n||_2^2 must add up to rF^2 of legqs_norms (same integrals
regrouped), and H_UB <= rF. Usage: legqs_hardy_test.py <outdir>"""
from fractions import Fraction as Q
from pathlib import Path
import json, sys, tempfile
sys.set_int_max_str_digits(0); sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import arb
import legqs_e2norms as LS, legqs_norms as LN, legqs_hardy as LH
gens = [{'m': 2, 'j': 1, 'spec': ['legqs', 0, 2, 4, 25], 'coef': '3/7'}, {'m': 3, 'j': 0, 'spec': ['legqs', 0, 1, 4, 25], 'coef': '-2/5'},
        {'m': 1, 'j': 2, 'spec': ['legqs', 0, 1, 4, 25], 'coef': '5/11'}, {'m': 0, 'j': 0, 'spec': ['legqs', 1, 2, 4, 25], 'coef': '1/3'},
        {'m': 1, 'j': 3, 'spec': ['legqs', 0, 0, 4, 25], 'coef': '7/2'}, {'m': 2, 'j': 3, 'spec': ['legqs', 1, 0, 4, 10], 'coef': '-1/9'}]
d = Path(tempfile.mkdtemp()); f = d / 'g.json'; f.write_text(json.dumps({'cl': str(Q(4076476460239181, 2251799813685248)), 'generators': gens}))
c, A, A_s, sha, meta = LS.load_reference_legqs(f); delta = 1 - 1 / c
D, fields = LN.residual_t(A, A_s, c, 0, log=lambda *a: None)
LN.save_F(D[0, 0], d / 'synthetic_legqs_Fpoly.json', {'name': 'synthetic', 'source_sha256': sha, 'delta': str(delta), 'cl': str(c)})
rrF = LN.norm_t(D, 0, delta, Q(-1), 1, (), 56, 'rF')
LH.run('synthetic', d / 'synthetic_legqs_Fpoly.json', Path(sys.argv[1]))
out = json.loads((Path(sys.argv[1]) / 'synthetic_legqs_hardy.json').read_text())
print('rF from norm_t:', rrF['norm_lower_ball'][:40], ' sum of modes:', out['rF_check'][:40], ' H_UB:', out['H_upper'][:30])
