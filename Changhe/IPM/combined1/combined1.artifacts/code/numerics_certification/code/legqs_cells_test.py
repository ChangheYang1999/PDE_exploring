"""Validation of the legqs Laplacian path on a CONFIRMED value: N_a(d2) (all modes) from the e2norms-format d2 F record through
legqs_norms.diff_t twice and normsq_t with a_shift = a - 2 must reproduce the wlap_norms values 1161.65961265051 (a = 0) and
22.6836992643494 (a = 1), T4-107 / N4-099 (CONFIRMED). Usage: legqs_cells_test.py <d2 F record> <outdir>"""
from pathlib import Path
from fractions import Fraction as Q
import json, sys, time
sys.set_int_max_str_digits(0); sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import arb, ctx
import legqs_norms as LN
ctx.prec = 1024; t0 = time.time()
F, raw = LN.load_F(sys.argv[1]); delta = Q(raw['delta'])
D1y = LN.canon_t(LN.diff_t(F, 0, 'y', delta)); D1x = LN.canon_t(LN.diff_t(F, 0, 'x', delta))
Lap = LN.canon_t(LN.plus_t((1, LN.diff_t(D1x, 1, 'x', delta)), (1, LN.diff_t(D1y, 1, 'y', delta))))
print(f'd2 Laplacian: {len(Lap)} components ({time.time()-t0:.0f}s)', flush=True)
out = {}
for a, ref in ((Q(1), '22.6836992643494'), (Q(0), '1161.65961265051')):
    r = LN.normsq_t([(1, Lap)], 2, delta, a_shift=a - 2); N = r['hi'].sqrt()
    out[str(a)] = {'N_a': N.str(30), 'ref_T4_107': ref, 'agree': abs(N - arb(ref)) < 1e-12}
    print(f'a = {a}: N_a(d2) = {N.str(20)}  (T4-107 / N4-099: {ref})  agree to 1e-12: {out[str(a)]["agree"]}  ({time.time()-t0:.0f}s)', flush=True)
Path(sys.argv[2], 'legqs_cells_test_d2.json').write_text(json.dumps(out, indent=1) + '\n')
