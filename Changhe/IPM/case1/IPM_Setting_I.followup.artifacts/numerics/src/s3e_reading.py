"""SPEC S3 (e) reading from svd_<tag>.json files (coarse, middle, fine) in a chosen norm, plus overlaps from compare_*.json if given.
Usage: python3 src/s3e_reading.py norm tagA tagB tagC [compare_AB.json compare_BC.json]   (norm: node_cl400 or S3norm)"""
import sys, json, numpy as np
LANE = '.'
norm = sys.argv[1]; tags = sys.argv[2:5]; comps = sys.argv[5:7]
S = [json.load(open(f'{LANE}/runs/svd_{t}.json')) for t in tags]
out = []
for t, s in zip(tags, S):
    r = s['svd'][norm]; out.append(f"{t}: n {s['n']} |F| {s['F2']:.2e} stationarity {s['stationarity_JtF']:.1e} smax {r['smax']:.3e} smallest {' '.join('%.3e' % x for x in r['smallest20'][:6])} counts {r['counts']} rel {r['counts_rel']}")
print('\n'.join(out))
sm = [S[i]['svd'][norm]['smallest20'] for i in range(3)]
s1 = [x[0] for x in sm]; s2 = [x[1] for x in sm]
ch1 = abs(s1[2] - s1[1]) / s1[1]; ch2 = abs(s2[2] - s2[1]) / s2[1]
fall = [s1[i] / s1[i + 1] for i in range(2)]
cnt = [S[i]['svd'][norm]['counts_rel'] for i in range(3)]
grow10 = cnt[0]['<1e-10*smax'] <= cnt[1]['<1e-10*smax'] <= cnt[2]['<1e-10*smax'] and cnt[2]['<1e-10*smax'] > cnt[0]['<1e-10*smax']
ov = None
if len(comps) == 2:
    C = [json.load(open(c)) for c in comps]; ov = [C[i]['result']['r<200']['overlaps'][0] for i in range(2)]
print(f'\nsigma_1 by grid: {s1}; sigma_2: {s2}; sigma_1 change between the two finest: {ch1:.2f}; sigma_2 change: {ch2:.2f}; sigma_1 fall factors: {fall}')
print(f'counts below 1e-10 smax: {[c["<1e-10*smax"] for c in cnt]}, below 1e-11 smax: {[c["<1e-11*smax"] for c in cnt]}; v_1 overlaps (coarse-mid, mid-fine): {ov}')
fam = (fall[1] >= 1.5 and ch2 < 0.3 and (ov is None or ov[1] >= 0.9))
iso = (ch1 < 0.3 and (ov is None or ov[1] >= 0.9))
nonf = (grow10 and all(f >= 1.5 for f in fall) and (ov is None or ov[1] < 0.5))
reading = 'family' if fam else 'isolated (Fredholm-like)' if iso else 'non-Fredholm / pseudo-mode softness' if nonf else 'undecided'
print(f'criteria: family {fam}, isolated {iso}, non-Fredholm {nonf} -> reading: {reading} (overlaps {"not available: provisional" if ov is None else "used"})')
