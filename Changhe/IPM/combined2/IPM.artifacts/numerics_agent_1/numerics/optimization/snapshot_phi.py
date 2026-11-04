"""snapshot_phi.py (lane numerics_agent_1): immutable snapshot of an exact odd-potential correction candidate (AT-119 class) in exchange/candidate_snapshots/<ID>/.
argv: ID phi_exact_json eval_json summary_json "description" "notes" [extra files...]
The candidate is the composite correction h_* = (rho_base - rho_007) + h_phi of the exact base candidate named in the phi JSON (center block); the manifest
records both parents (C2-REF-007 and the base snapshot), the exact identities (A, B, A + 3B = 0, a_*), the FLOAT evaluation and the code hashes."""
import sys, os, json, hashlib, shutil, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
ID, phij, evj, sumj, descr, notes = sys.argv[1:7]; extra = sys.argv[7:]
ROOT = os.path.dirname(LANE); SH = os.path.join(ROOT, 'exchange', 'candidate_snapshots'); dest = os.path.join(SH, ID)
assert not os.path.exists(dest), 'snapshot exists: '+ID
os.makedirs(dest)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
J = json.load(open(phij)); ev = json.load(open(evj)); sm = json.load(open(sumj))
assert J['c_exact'] == '4076476460239181/2251799813685248' and J['reference_sha256'] == REF007_SHA
files = {}
for src in [phij, evj, sumj]+extra:
    name = os.path.basename(src); shutil.copy(src, os.path.join(dest, name)); files[name] = sha(os.path.join(dest, name))
code = []
for rel in ('numerics/optimization/phi_fit.py', 'numerics/optimization/phi_atoms.py', 'numerics/optimization/ipm_optn1.py', 'numerics/optimization/n1_setup.py', 'numerics/optimization/exact_origin.py',
            'numerics/lib/ipm_polar.py', 'numerics/lib/ipm_eval.py', 'numerics/lib/ipm_opt2.py', 'numerics/lib/ipm_opt.py', 'numerics/lib/ipm_exact.py'):
    p = os.path.join(LANE, rel)
    if os.path.exists(p): code.append({'path': 'numerics_agent_1/'+rel, 'sha256': sha(p)})
rp = ev['report_FLOAT']
man = {'id': ID, 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'created_by_lane': 'numerics_agent_1', 'kind': 'odd-potential correction (numerical_audit AT-119 class) of an exact campaign-basis center; composite correction of Candidate 007',
       'parents': [{'id': 'C2-REF-007', 'sha256': REF007_SHA, 'role': 'reference background rho_bar (unchanged)'}, {'id': J['center']['base_candidate_id'], 'sha256': J['center']['base_exact_sha256'], 'role': 'exact base center C; h_* = (rho_C - rho_007) + h_phi'}],
       'c_l_exact': J['c_exact'], 'correction_file': {'name': os.path.basename(phij), 'sha256': files[os.path.basename(phij)], 'schema': J['schema_version'], 'n_atoms': J['n_atoms_nonzero'], 'definition': J['definition'], 'conversion_policy': J['conversion_policy']},
       'exact_identities': J['exact_identities'], 'center': J['center'],
       'evaluation_FLOAT': {'file': os.path.basename(evj), 'sha256': files[os.path.basename(evj)], 'mesh': ev['mesh'], 'background_mesh_meta': ev['background'],
                            'Fstar_L2': rp['G0'], 'sup_Fstar': rp['supF'], 'N2_P-S1': rp['N2_P-S1'], 'N2_P-S2': rp['N2_P-S2'], 'E012_P-S1': rp['E012_P-S1'], 'E012_P-S2': rp['E012_P-S2'],
                            'h_phi_L2': rp['h_L2'], 'grad_h_phi_inf': rp['grad_h_inf'], 'DU_h_phi_frobenius_inf': rp['DU_frob_inf'], 'a_star_float': rp['a_star'], 'label': 'FLOAT (binary64 quadrature on the stated product mesh, 0.02 <= r <= 1e4; not bounds; the far part r > 1e4 is omitted)'},
       'fit_summary': {'file': os.path.basename(sumj), 'sha256': files[os.path.basename(sumj)], 'final_objective': sm['meta']['final_objective'], 'steps_accepted': sm['meta']['steps_accepted'], 'config': sm['meta']['config']},
       'far_field_note': 'every atom has tau <= mu = 4/c - 3 exactly, so h_phi, U[h_phi] and all terms of L h_phi + U[h_phi].grad h_phi carry only exponents <= e = 4/c - 5 (the first surviving sector (3,1) of the base) or lower; the eleven EXACT-ZERO sectors of the base are untouched (exponent bookkeeping of PROOF.md; the exact sector table of F_* is not recomputed here)',
       'evaluator_code': code, 'audit': 'PENDING-AN', 'notes': notes}
json.dump(man, open(os.path.join(dest, 'MANIFEST.json'), 'w'), indent=1)
msha = sha(os.path.join(dest, 'MANIFEST.json'))
with open(os.path.join(dest, 'SHA256SUMS'), 'w') as f:
    f.write(f'{msha}  MANIFEST.json\n')
    for name, h in files.items(): f.write(f'{h}  {name}\n')
for name in os.listdir(dest): os.chmod(os.path.join(dest, name), 0o444)
open(os.path.join(SH, 'INDEX.md'), 'a').write(f"| {ID} | {man['created_utc']} | numerics_agent_1 | {J['center']['base_candidate_id']} (+ C2-REF-007) | {descr} | {msha} |\n")
os.chmod(dest, 0o555)
print('snapshot', ID, 'MANIFEST sha256', msha)
