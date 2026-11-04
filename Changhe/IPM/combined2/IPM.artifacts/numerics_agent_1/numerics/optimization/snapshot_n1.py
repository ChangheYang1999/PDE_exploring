"""snapshot_n1.py (lane numerics_agent_1): immutable candidate snapshot in exchange/candidate_snapshots/<ID>/ (CONTRACTS section 6).
argv: ID parent_id parent_sha256 exact_json sectors_json eval_json loss_value "loss definition" "description" "notes" [sf_json|none]
Writes MANIFEST.json, copies of the exact coefficient file, the sector table and the FLOAT evaluation, SHA256SUMS; appends INDEX.md; chmod read-only."""
import sys, os, json, hashlib, shutil, time, stat
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
from exact_origin import exact_origin
ID, parent_id, parent_sha, exact_json, sectors_json, eval_json, loss_value, loss_def, descr, notes = sys.argv[1:11]
sf_json = sys.argv[11] if len(sys.argv) > 11 and sys.argv[11] != 'none' else None
ROOT = os.path.dirname(LANE); SH = os.path.join(ROOT, 'exchange', 'candidate_snapshots'); dest = os.path.join(SH, ID)
assert not os.path.exists(dest), 'snapshot exists: '+ID
os.makedirs(dest)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
c, gens, coefs_q, J = OPT.load_candidate_json(exact_json)
sec = json.load(open(sectors_json)); ev = json.load(open(eval_json)); org = exact_origin(exact_json)
assert org['cl_exact'] == '4076476460239181/2251799813685248', 'c_l out of scope'
files = {}
for src in (exact_json, sectors_json, eval_json) + ((sf_json,) if sf_json else ()):
    name = os.path.basename(src); shutil.copy(src, os.path.join(dest, name)); files[name] = sha(os.path.join(dest, name))
branches = sorted({int(g['j']) for g in gens if 'j' in g}); mmax = max(int(g['m']) for g in gens)
kmax = max(t['k'] for t in X.generators_to_terms(c, [dict(g, coef=1) for g in gens]) if t.get('kind') != 'series')
first = sec.get('first_nonzero')
code = []
for rel in ('numerics/lib/ipm_exact.py', 'numerics/lib/ipm_eval.py', 'numerics/lib/ipm_polar.py', 'numerics/lib/ipm_origin.py', 'numerics/lib/ipm_opt.py', 'numerics/lib/ipm_opt2.py',
            'numerics/optimization/ipm_optn1.py', 'numerics/optimization/run_n1.py', 'numerics/optimization/eval_candidate.py', 'numerics/optimization/n1_setup.py', 'numerics/optimization/exact_origin.py', 'numerics/cert/e2norms.py', 'numerics/cert/exact_g0.py'):
    p = os.path.join(LANE, rel)
    if os.path.exists(p): code.append({'path': 'numerics_agent_1/'+rel, 'sha256': sha(p)})
man = {'id': ID, 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'created_by_lane': os.environ.get('SNAP_LANE', 'numerics_agent_1'), 'parent': {'id': parent_id, 'sha256': parent_sha},
       'c_l_exact': org['cl_exact'],
       'basis': {'description': descr, 'generator_count': len(gens), 'branches': branches, 'angular_max_m': mmax, 'angular_max_harmonic_2m': 2*mmax, 'radial_max_k_canonical': kmax,
                 'generator_specs': sorted({g['spec'][0] for g in gens})},
       'constraints': {'exact_linear_rows': J.get('meta', {}).get('n_linear_rows', int(os.environ.get('SNAP_ROWS', '421'))), 'description': 'center relation (B0n, F_y(0) = 0); Theta_0 of state 131 for every m present; zero q = 1 descendants of branches ' + str(J.get('meta', {}).get('desc_zero', [0, 1, 2])) + '; exact leading moments of branches 1..JMAX from the stationary recursion; five quadratic origin Taylor rows imposed numerically (SQP projection)', 'taylor_rows_numerical': J.get('meta', {}).get('taylor_rows', True)},
       'coefficient_files': [{'name': os.path.basename(exact_json), 'sha256': files[os.path.basename(exact_json)], 'format': J.get('format'), 'exactness': 'all coefficients exact rationals; pivot coefficients solved exactly (flint fmpq_mat) so that every linear row holds exactly; the other coefficients are binary64 values'}],
       'evaluator_code': code,
       'B0n_status': 'EXACT' if org['B0n_exact'] else 'INCONCLUSIVE', 'a0': {'exact': org['a0_exact'], 'float': org['a0_float'], 'label': 'EXACT (rational from the exact origin jet)'},
       'origin_Rf_taylor': {'keys': org['taylor_keys'], 'float': org['Rf_taylor_float'], 'note': 'exact rationals of the saved coefficients; the five quadratic rows hold only to binary64 projection accuracy'},
       'sector_table': {'name': os.path.basename(sectors_json), 'sha256': files[os.path.basename(sectors_json)], 'first_surviving_exponent_exact': first['exponent_exact'] if first else None, 'first_surviving_exponent': first['exponent'] if first else None, 'first_surviving_full_circle_L2': first['full_circle_L2'] if first else None, 'exact_zero_sectors_above': [r['exponent_exact'] for r in sec['rows'] if r['status'] == 'EXACT-ZERO' and (first is None or r['exponent'] > first['exponent'])]},
       'loss': {'value': float(loss_value), 'definition': loss_def, 'label': 'LOSS'},
       'G0': {'value': ev['G0'], 'label': 'FLOAT', 'rule': ev['rule'], 'audit': 'PENDING-AN', 'G0_inner': ev['G0_inner'], 'F2_far': ev['F2_far']},
       'float_norms': {'rF': ev['rF'], 'G1': ev['G1'], 'P2': ev['P2'], 'supF_mesh': ev['supF'], 'label': 'FLOAT', 'file': os.path.basename(eval_json)},
       'background_screen': {'theta_inner_sup': ev['BL2']['theta_inner_sup']['value'], 'kappa_inner': ev['BL2']['kappa_inner'], 'beta0_float': ev['BL2']['beta0_float'], 'nu_flow_min': ev['flow']['nu_min'], 'label': 'FLOAT (mesh), not bounds'},
       'S_F': ({'file': os.path.basename(sf_json), 'sha256': files[os.path.basename(sf_json)]} if sf_json else {'status': 'not computed in this snapshot', 'grid_proxy_sigma_1.75': ev.get('strong_proxy')}),
       'notes': notes}
json.dump(man, open(os.path.join(dest, 'MANIFEST.json'), 'w'), indent=1)
msha = sha(os.path.join(dest, 'MANIFEST.json'))
with open(os.path.join(dest, 'SHA256SUMS'), 'w') as f:
    f.write(f'{msha}  MANIFEST.json\n')
    for name, h in files.items(): f.write(f'{h}  {name}\n')
for name in os.listdir(dest): os.chmod(os.path.join(dest, name), 0o444)
idx = os.path.join(SH, 'INDEX.md')
if not os.path.exists(idx): open(idx, 'w').write('# candidate_snapshots INDEX (append-only; written by numerics_agent_1)\n| ID | created_utc | lane | parent | description | MANIFEST sha256 |\n|---|---|---|---|---|---|\n')
open(idx, 'a').write(f"| {ID} | {man['created_utc']} | numerics_agent_1 | {parent_id} | {descr} | {msha} |\n")
os.chmod(dest, 0o555)
print('snapshot', ID, 'MANIFEST sha256', msha); print(json.dumps({k: man[k] for k in ('a0', 'B0n_status', 'G0', 'sector_table')}, indent=1))
