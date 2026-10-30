"""Tables for numerics_v06: extended weak distances (weaktests2 + highk + bridge JSONs), far_weak table, pairing-run summary.  Prints markdown blocks separated by blank lines."""
import json, os, glob, math
tags = {'C1-N1-007-d2w-j7-e2bal': 'd2w_j7_n4_E2bal_mid180', 'C1-N1-008-d2w-j7-x3bal': 'd2w_j7_n4_X3bal_mid180', 'C1-N1-009-d2w-j7-x3balk': 'd2w_j7_n4_X3balK_mid180',
        'C1-N1-010-d2w-j7-x3bal-legqs': 'd2w_j7_n4_X3bal_legqs_mid180', 'C1-N1-011-e2bal-legqs-from007': 'd2w_j7_n4_E2bal_legqs_cpu_m8', 'C1-N1-012-e2balk1e7-from009': 'd2w_j7_n4_E2balK_cpu_m8',
        'C1-N1-013-pairU-from007': 'd2w_j7_n4_E2bal_pairU_cpu_m16', 'C1-N1-014-desc3-from007': 'd2w_j7_n4_E2bal_desc3_cpu_m16'}
def load(tag, suffix):
    p = f'candD2/{tag}_{suffix}.json'
    return json.load(open(p)) if os.path.exists(p) else None
out = []
# extended weak table: per candidate, m_k at selected k and the max
cols = [0, 8, 64, 128, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
out.append('| candidate | ' + ' | '.join(f'm_k k={k}' for k in cols) + ' | max over all computed k (at k) | pairing k=0 |')
out.append('|---|' + '---|'*len(cols) + '---|---|')
for cid, tag in tags.items():
    W = {}
    for suf in ('weaktests2', 'weaktests2_highk', 'weaktests2_bridge'):
        d = load(tag, suf)
        if d: W.update({int(k): v for k, v in d['NORM-T-WEAK-v1_a0'].items()})
    if not W: continue
    kmax = max(W, key=lambda k: W[k]['m_lower_bound'])
    cells = [f"{W[k]['m_lower_bound']:.2e}" if k in W else '-' for k in cols]
    out.append(f"| {cid} | " + ' | '.join(cells) + f" | {W[kmax]['m_lower_bound']:.3e} (k = {kmax}; k range to {max(W)}) | {W[0]['I_k_signed_mesh']+W[0]['I_k_far']:+.3e} |")
out.append('')
# full k profile for 007
W = {}
for suf in ('weaktests2', 'weaktests2_highk', 'weaktests2_bridge'):
    d = load(tags['C1-N1-007-d2w-j7-e2bal'], suf)
    if d: W.update({int(k): v for k, v in d['NORM-T-WEAK-v1_a0'].items()})
out.append('Full k profile of C1-N1-007 (FLOAT; I_k signed mesh value plus far correction, D_k, m_k):')
out.append('| k | r_peak (dr density, e = -2.79) | I_k | D_k | m_k |'); out.append('|---|---|---|---|---|')
for k in sorted(W):
    v = W[k]; rp = math.sqrt((2*k-2.7904+2)/(2+2.7904)) if 2*k-0.79 > 0 else 0
    out.append(f"| {k} | {rp:.1f} | {v['I_k_signed_mesh']+v['I_k_far']:+.3e} | {v['D_k']:.3e} | {v['m_lower_bound']:.3e} |")
out.append('')
# far_weak table
fw = json.load(open('candD2/007_far_weak.json')) if os.path.exists('candD2/007_far_weak.json') else None
if fw:
    out.append('Far-field weak probe of 007 from the exact sector table (31 sectors with a sin theta component, exponents -2.79 to -6.82; I_far = |sum_e pi s_1(e) T_e(k)| exact-formula; A_k exact; B_k, C_k scaled estimates; near-field bound G0 t_R^k sqrt(pi/12)):')
    out.append('| k | r_peak | I_far | leading-sector term | A_k | m_far (estimate) | near-field bound R=100 / 300 / 1000 |'); out.append('|---|---|---|---|---|---|---|')
    for r in fw['rows']:
        nb = r['near_field_bound_by_R']
        out.append(f"| {r['k']} | {r['r_peak_dr']:.0f} | {r['I_far']:.3e} | {r['leading_term']:+.3e} | {r['A_k']:.3e} | {r['m_far_est']:.3e} | {nb['100']:.1e} / {nb['300']:.1e} / {nb['1000']:.1e} |")
    out.append('')
print('\n'.join(out))
