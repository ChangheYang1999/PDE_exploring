"""compare_lineages.py -- side-by-side table of lineage 1 (y0 2.87 dipole, a0 1.011258; accepted stages blam16v/24v/32v/40v) and lineage 2
(y0 2.5 dipole, a0 1.0; blamL2k24 stages) at equal lambda: beta, fit floor, a0^(1/beta) Q_R (up), Q_down, a_pl, w, S at r = 2.3e5 (from the
axis_*.json and drop_*.json diagnostics; run code/stage_diag.py on each new lineage-2 stage first). Usage: python3 code/compare_lineages.py [tag2]"""
import sys, os, glob, json, math, numpy as np
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tag2 = sys.argv[1] if len(sys.argv) > 1 else 'blamL2k24'
L1 = {0.99: 'blam16v_lambda0.99', 0.98: 'blam16v_lambda0.98', 0.97: 'blam16v_lambda0.97', 0.965: 'blam16v_lambda0.965', 0.96: 'blam24v_lambda0.96',
      0.955: 'blam24v_lambda0.955', 0.95: 'blam40v95_lambda0.95', 0.945: 'blam40v_lambda0.945', 0.94: 'blam40v_lambda0.94'}
def row(tag):
    st = f'{HERE}/runs/{tag}.npz'; aj = f'{HERE}/runs/axis_{tag}.json'; dj = f'{HERE}/runs/drop_{tag}.json'
    if not (os.path.exists(st) and os.path.exists(aj) and os.path.exists(dj)): return None
    d = np.load(st); A = json.load(open(aj)); D = json.load(open(dj))
    beta = float(d['beta']); a0 = float(d['a0']); floor = float(d['obj']); acc = int(d['continuation_accepted']) if 'continuation_accepted' in d.files else -1
    Q = A['axis']['up']['Q_closed_form_est']; Qd = A['axis']['down']['Q_closed_form_est']
    r = max(D['radii'], key=lambda k: float(k)); u = D['radii'][r]['transported']['up']
    S = math.radians(u['width_90_10_deg']) * u['a_over_angle_first_node'] / u['a_plateau'] if u['width_90_10_deg'] else float('nan')
    bulk = D['radii'][r]['a_at_delta_deg_from_upper_axis']['90'] if 'a_at_delta_deg_from_upper_axis' in D['radii'][r] else float('nan')
    return dict(beta=beta, a0=a0, floor=floor, acc=acc, Qn=a0 ** (1 / beta) * Q, Qd=Qd, apl=a0 ** (1 / beta) * u['a_plateau'], w=u['width_90_10_deg'], S=S, bulk=a0 ** (1 / beta) * bulk, K=int(d['K']))
lams2 = {}
for f in glob.glob(f'{HERE}/runs/{tag2}_lambda*.npz'):
    lams2[float(os.path.basename(f).split('lambda')[1][:-4])] = os.path.basename(f)[:-4]
print(f'lineage 1 (y0 2.87, a0 1.011258) vs lineage 2 = {tag2} (y0 2.5, a0 1.0); normalized Qn = a0^(1/beta) Q_R(up), a_pl and bulk likewise; w, S at r = 2.3e5; acc = accepted by the heuristic')
print('lambda | beta1      beta2      | floor1   floor2 (K2,acc) | Qn1     Qn2     | Qd1    Qd2   | a_pl1  a_pl2 | bulk1 bulk2 | w1     w2    | S1     S2')
for lam in sorted(set(L1) | set(lams2), reverse=True):
    r1 = row(L1[lam]) if lam in L1 else None; r2 = row(lams2[lam]) if lam in lams2 else None
    f = lambda r, k, fmt: (fmt % r[k]) if r else '-'.ljust(len(fmt % 0))
    print(f"{lam:.3f}  | {f(r1,'beta','%.6f')} {f(r2,'beta','%.6f')} | {f(r1,'floor','%8.4g')} {f(r2,'floor','%8.4g')} ({(str(r2['K'])+','+str(r2['acc'])) if r2 else '-'}) | {f(r1,'Qn','%7.2f')} {f(r2,'Qn','%7.2f')} | {f(r1,'Qd','%6.3f')} {f(r2,'Qd','%6.3f')} | {f(r1,'apl','%6.3f')} {f(r2,'apl','%6.3f')} | {f(r1,'bulk','%5.2f')} {f(r2,'bulk','%5.2f')} | {f(r1,'w','%6.2f')} {f(r2,'w','%6.2f')} | {f(r1,'S','%6.3f')} {f(r2,'S','%6.3f')}")
