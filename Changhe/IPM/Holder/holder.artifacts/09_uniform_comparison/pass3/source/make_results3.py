# Writes RESULTS3.md: per upper segment the smaller of the Theorem 3.5 and Theorem 3.7 segment bounds (PROOF3.md, "Minimum"),
# from uniform_result_thm35_pass3.json and uniform_result_thm37_pass3.json (both produced by combine3.py with the same nodes).
import json, hashlib, math, glob
from flint import arb, ctx
ctx.prec = 200
def up10(x):
    # exp of an upper endpoint, rounded up at 10 decimals
    y = arb(x).upper().exp()
    return math.ceil(float((y * 10**10).upper())) / 10**10
def sha(f): return hashlib.sha256(open(f, 'rb').read()).hexdigest()
R = {m: json.load(open(f'uniform_result_{m}_pass3.json')) for m in ('thm35', 'thm37')}
seg = {}
for m, d in R.items():
    for r in d['rows']:
        k = (r['group'], r['kind'], tuple(r['upper_segment']))
        seg.setdefault(k, {})[m] = (arb(arb(r['log_ratio_upper']).upper()), r['worst_point'])
assert all(set(v) == {'thm35', 'thm37'} for v in seg.values())
best = {}
for k, v in seg.items():
    m = 'thm35' if not (v['thm37'][0] < v['thm35'][0]) else 'thm37'
    best[k] = (v[m][0], m, v[m][1])
out = []; P = lambda s='': out.append(s)
P('# Results of the uniform comparison (third pass)')
P()
P('Produced by `combine3.py` (modes `thm35` and `thm37`, same nodes and lower certificates) and this script. On each upper')
P('segment the smaller of the two segment bounds is used (`PROOF3.md`, "Minimum"). Every number is the exponential of the')
P('upper endpoint of an Arb ball (200 bits), rounded up in the last place shown.')
P()
for m in ('thm35', 'thm37'):
    u = R[m]['uniform']
    P(f"- `{m}` alone: C log ratio $\\le$ `{u['C']['log_ratio_upper']}` (ratio $\\le$ {up10(u['C']['log_ratio_upper']):.10f}, near {u['C']['at']:.5f}, group {u['C']['group']}); "
      f"D log ratio $\\le$ `{u['D']['log_ratio_upper']}` (ratio $\\le$ {up10(u['D']['log_ratio_upper']):.10f}, near {u['D']['at']:.5f}, group {u['D']['group']}).")
P()
P('| group | worst C ratio (min of both) | segment | from | worst D ratio | segment |')
P('|---|---|---|---|---|---|')
overall = {}
for g in range(8):
    row = []
    for kind in 'CD':
        ks = [k for k in best if k[0] == g and k[1] == kind]
        k = max(ks, key=lambda k: float(best[k][0].mid()))
        assert all(not (best[j][0] > best[k][0]) for j in ks)
        row.append((k, best[k]))
        if kind not in overall or best[k][0] > overall[kind][1][0]: overall[kind] = (k, best[k])
    (kc, bc), (kd, bd) = row
    P(f'| {g} | {up10(bc[0]):.10f} | [{kc[2][0]}, {kc[2][1]}] | {bc[1]} | {up10(bd[0]):.10f} | [{kd[2][0]}, {kd[2][1]}] |')
P()
(kc, bc), (kd, bd) = overall['C'], overall['D']
P(f'Uniform on $[1/200, 199/200]$: $\\log\\rho_C\\le$ `{bc[0].str(20, more=True)}`, $\\rho_C\\le{up10(bc[0]):.10f}$ (segment [{kc[2][0]}, {kc[2][1]}], group {kc[0]}, {bc[1]});')
P(f'$\\log\\rho_D\\le$ `{bd[0].str(20, more=True)}`, $\\rho_D\\le{up10(bd[0]):.10f}$ (segment [{kd[2][0]}, {kd[2][1]}], group {kd[0]}).')
P()
nod = R['thm37']['nodal_upper']
P('Nodal cross-check. The `thm37` upper values for $C_\\alpha$ at the nodes $\\frac12$ (groups 2 and 3), $\\frac34$ (group 5) and $\\frac9{10}$ (group 6) are')
P(f"`{nod['2']['C']['1/2']}`, `{nod['3']['C']['1/2']}`, `{nod['5']['C']['3/4']}` and `{nod['6']['C']['9/10']}`. They agree with the single-exponent")
P('Theorem 3.7 certificates $C_{1/2}\\le2.1970179509$, $C_{3/4}\\le2.6442935978$, $C_{9/10}\\le5.0137426873$ of the report (Table 1).')
P()
P('The end intervals are unchanged (`../uniform/PROOF.md`, section 5: $C$ ratio at most $1.0263$, $D$ ratio at most $1.0324$ there).')
P()
P('## Reproduction')
P()
P('```')
P('bash run3.sh            # local and middle node chunks (local/, mid/)')
P('python3 combine3.py thm37 --nodes ../uniform/nodes2.json --upper ../uniform/upper_n384.json,../uniform/upper_n384_b.json --lower ../uniform/lower2_g --far ../uniform/far2_g --tag _pass3')
P('python3 combine3.py thm35 --nodes ../uniform/nodes2.json --upper ../uniform/upper_n384.json,../uniform/upper_n384_b.json --lower ../uniform/lower2_g --far ../uniform/far2_g --tag _pass3')
P('python3 make_results3.py')
P('```')
P()
P('## SHA-256')
P()
P('| file | sha256 |')
P('|---|---|')
fs = ['PROOF3.md', 'combine3.py', 'make_results3.py', 'local_nodes.py', 'mid_nodes.py', 'run3.sh', 'certify_local_circles_greedy.py',
      'local_circle_greedy.py', 'middle_circle_plan.py', 'circle_transport_plan.py', 'uniform_result_thm35_pass3.json', 'uniform_result_thm37_pass3.json']
fs += sorted(glob.glob('local/r*.json')) + sorted(glob.glob('mid/n512_*.json'))
for f in fs: P(f'| `{f}` | `{sha(f)}` |')
open('RESULTS3.md', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out[:30]))
