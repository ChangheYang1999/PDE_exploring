import json, sys
tags = {'C1-N1-007-d2w-j7-e2bal':'d2w_j7_n4_E2bal_mid180','C1-N1-008-d2w-j7-x3bal':'d2w_j7_n4_X3bal_mid180',
        'C1-N1-009-d2w-j7-x3balk':'d2w_j7_n4_X3balK_mid180','C1-N1-010-d2w-j7-x3bal-legqs':'d2w_j7_n4_X3bal_legqs_mid180'}
out=[]
# point tests
out.append('| candidate | R_nec(2^-18) | at (r, theta) | R_nec(2^-17) | R_nec(2^-16) | R_nec(5 2^-18) | R_sym axis (2^-18) |')
out.append('|---|---|---|---|---|---|---|')
for cid,tag in tags.items():
    d=json.load(open(f'candD2/{tag}_diag2.json'))
    pt=d['point_tests']; a=pt['2^-18']
    out.append(f"| {cid} | {a['R_nec']:.3g} | ({a['at']['r']:.3g}, {a['at']['theta']:.3g}) | {pt['2^-17']['R_nec']:.3g} | {pt['2^-16']['R_nec']:.3g} | {pt['5*2^-18']['R_nec']:.3g} | {a['R_sym_axis']:.3g} |")
out.append('')
# dyadic profiles for 009, 010 (008 skipped: comparison candidate)
for cid in ['C1-N1-009-d2w-j7-x3balk','C1-N1-010-d2w-j7-x3bal-legqs']:
    tag=tags[cid]; d=json.load(open(f'candD2/{tag}_diag2.json'))
    out.append(f"NORM-T-DYADIC-v1 profile of {cid} (FLOAT; exterior beyond r = 8356.47 from the exact sectors: ||F|| {d['F2_far']**0.5:.3g}, ||rF|| {d['rF2_far']**0.5:.3g}):")
    out.append('| annulus | ||F||_L2 | ||rF||_L2 | ||grad F||_L2 | ||omega D^2 F||_L2 | sup|F| |')
    out.append('|---|---|---|---|---|---|')
    tot=sum(x['L2']**2 for x in d['dyadic']); best=max(d['dyadic'],key=lambda x:x['L2'])
    for x in d['dyadic']:
        out.append(f"| [{x['range'][0]:.4g}, {x['range'][1]:.4g}) | {x['L2']:.3g} | {x['rF']:.3g} | {x['gradF']:.3g} | {x['omD2F']:.3g} | {x['supF']:.3g} |")
    out.append(f"Reading for {cid}: largest L^2 annulus [{best['range'][0]:.4g}, {best['range'][1]:.4g}) with {100*best['L2']**2/tot:.0f} percent of the mesh ||F||_2^2; sup|F| {d['supF']:.3g}.")
    out.append('')
# weak tests
for cid,tag in tags.items():
    try: w=json.load(open(f'candD2/{tag}_weaktests.json'))
    except FileNotFoundError: out.append(f'{cid}: weak tests not yet available'); continue
    W=w['NORM-T-WEAK-v1_a0']
    ks=sorted(W,key=int)
    mk=max(W[k]['m_lower_bound'] for k in ks); kbest=max(ks,key=lambda k:W[k]['m_lower_bound'])
    wl=w['NORM-T-WL2-v1']
    pa='; '.join(f"[{x['range'][0]:.4g},{x['range'][1]:.4g}): {x['pairing_k0']:+.3g}" for x in w['pairing_k0_per_annulus'] if abs(x['pairing_k0'])>1e-6)
    lap=w['NORM-T-WLAP-v1']
    passes=[a for a,v in lap.items() if v.get('passes')]
    out.append(f"{cid}: weak-distance lower bound (NORM-T-WEAK-v1, a = 0, max over k = 0..8) {mk:.4e} (at k = {kbest}; k = 0: {W['0']['m_lower_bound']:.3e}; I_0 = {W['0']['I_k']:+.4e}); NORM-T-WL2-v1 at a = 1/2, 3/4, 1, 6/5: {wl['0.5']:.4f}, {wl['0.75']:.4f}, {wl['1.0']:.4f}, {wl['1.2']:.4f}; N_a FLOAT at a = 0, 1/2, 1: {lap['0.000000']['N_a']:.2f}, {lap['0.500000']['N_a']:.2f}, {lap['1.000000']['N_a']:.2f} (NC-T-DYADIC-LAP cell test passes at: {passes if passes else 'no a'}); per-annulus k = 0 pairing (|.| > 1e-6): {pa}.")
print('\n'.join(out))
