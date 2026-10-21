# fred23 03 aligned obstruction values: B(A_0, e_0, (A_0/A_i) w_i) for the lead's K = 12 and K = 18 references,
# A_0 = 10.150725, e_0 = 1/8.6000638^2, with the own evaluator bnat.py (form (II), default and refined panels).
import sys, time, json
sys.path.insert(0, '.')
from fractions import Fraction as Fr
import mpmath as mp
from bnat import Ref, B_value
ref = {12: '0.2674821674646158', 18: '0.2996502481374085'}
out = {}
for K in (12, 18):
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
    ratio = Fr('10.150725')/Fr(repr(d['A']))
    qa = ['%d/%d' % ((Fr(s)*ratio).numerator, (Fr(s)*ratio).denominator) for s in d['q_monomial']]
    mp.mp.dps = 40
    e0 = 1/mp.mpf('8.6000638')**2
    R = Ref('10.150725', e0, qa, dps=40)
    R.series0(80)
    res = {}
    for tag, kw in [('II_0.25', {}), ('II_0.25_fine', dict(nmid=40, wmid=mp.mpf(1)/40, ns=40, levels=14))]:
        t1 = time.time()
        v, parts = B_value(R, 'II', mp.mpf('0.25'), **kw)
        res[tag] = mp.nstr(v, 22)
        print('K=%d aligned B (%s) = %s  minus fred23 %s  (%.0fs)' % (K, tag, mp.nstr(v, 20), mp.nstr(v - mp.mpf(ref[K]), 3),
              time.time() - t1), flush=True)
    out[K] = res
json.dump(out, open('../../runs/aligned_B.json', 'w'), indent=1)
