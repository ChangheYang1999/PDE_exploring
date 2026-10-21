# R12 against the low-degree approximants K = 4, 6, 8 (same evaluator as ndist_ver.py, both conventions).
import json
src = open('ndist_ver.py').read().split('\npairs = ')[0]
exec(src)
for K in (4, 6, 8):
    d = json.load(open(L + '/src/xref/ref_c6g_K%d.json' % K))
    refs['K%d' % K] = (mp.mpf(repr(d['A'])), [mp.mpf(s) for s in d['q_monomial']])
out = {}
for b in ('K4', 'K6', 'K8'):
    Aa, qa = refs['R12']; Ab, qb = refs[b]
    s = Aa / Ab
    p = [-s * x for x in qb]
    c = v_coeffs(p)
    for var in ('mono', 'phi'):
        tot, parts = ndist(c, var)
        out['R12-%s-%s' % (b, var)] = dict(total=mp.nstr(tot, 6), **parts)
        print('R12 - %-3s (%s): N = %s  %s' % (b, var, mp.nstr(tot, 6), parts), flush=True)
json.dump(out, open('verifier/early_runs/ndist_low.json', 'w'), indent=1)
