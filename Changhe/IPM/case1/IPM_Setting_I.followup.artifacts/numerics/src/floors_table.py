"""Table of residual floors over discrete systems / grids / domains: for each state tag, |F|_2, |F|_inf, c_l, C, x* (from the
s4e json if present), h(P) - 1, identity, N, M, L, and the smallest singular values from runs/svd_<svdtag>.json (node_cl400) or the Ritz
values from runs/crossgrid_<tag>.json if given as tag:svdtag or tag:crossgrid=<tag>.
Usage: python3 src/floors_table.py state1[:svdtag1] state2[:svdtag2] ...   (state = runs/<state>.npz basename)"""
import sys, json, os, numpy as np
LANE = '.'
rows = []
for arg in sys.argv[1:]:
    st, _, sv = arg.partition(':')
    d = np.load(f'{LANE}/runs/{st}.npz', allow_pickle=True)
    r = dict(state=st, N=int(d['N']), M=int(d['M']), L=float(d['L']), c_l=float(d['c_l']), C=float(d['C']) if 'C' in d.files else float('nan'))
    for k in ('F2', 'Finf', 'hP_minus_1', 'identity', 'ident', 'xstar'):
        if k in d.files: r[k] = float(d[k])
    s4 = f'{LANE}/runs/s4e_{st}.json'
    if os.path.exists(s4):
        j = json.load(open(s4)); r.setdefault('xstar', j.get('xstar')); r['F_psi_2'] = j.get('F_psi_2'); r['hP_minus_1'] = j.get('hP_minus_1'); r['ident'] = j.get('identity_defect')
    if sv.startswith('ritz='):
        j = json.load(open(f'{LANE}/runs/ritz_{sv[5:]}.json')); r['smallest'] = j['ritz'][:6]; r['svd_kind'] = 'exact-action Ritz (unscaled)'
    elif sv.startswith('crossgrid='):
        j = json.load(open(f'{LANE}/runs/crossgrid_{sv[10:]}.json')); r['smallest'] = j['target']['ritz'][:6]; r['svd_kind'] = 'Ritz (interpolated subspace)'
    elif sv:
        j = json.load(open(f'{LANE}/runs/svd_{sv}.json')); r['smallest'] = j['svd']['node_cl400']['smallest20'][:6]; r['svd_kind'] = 'SVD node_cl400'
    rows.append(r)
hdr = '| state | (N,M) | L | |F|_2 | |F|_inf | c_l | C | x* | h(P)-1 | ident | smallest singular values (node norm) |\n|---|---|---|---|---|---|---|---|---|---|---|'
print(hdr)
for r in rows:
    f = lambda k, fmt: (fmt.format(r[k]) if r.get(k) is not None and not (isinstance(r.get(k), float) and np.isnan(r[k])) else 'n/a')
    sm = ' '.join('%.2e' % v for v in r['smallest']) + f" ({r['svd_kind']})" if 'smallest' in r else 'n/a'
    print(f"| {r['state']} | ({r['N']},{r['M']}) | {r['L']:g} | {f('F2','{:.4e}')} | {f('Finf','{:.2e}')} | {f('c_l','{:.8f}')} | {f('C','{:.6f}')} | {f('xstar','{:.6f}')} | {f('hP_minus_1','{:+.1e}')} | {f('ident','{:+.1e}')} | {sm} |")
