"""Post-process rounding_model.json with the lead's predeclared envelope (NOTES 03:41Z):
S_i = sqrt(2 w_i/(pi a_ref^2)) * [ (c_l|x| + sum_g|c_g psi_y,g|) sum_g|c_g f_x,g| + (c_l|y| + sum_g|c_g psi_x,g|) sum_g|c_g f_y,g|
      + (|c_l-1| + sum_g|c_g (ratio_g - strain_g)|) sum_g|c_g f_g| ],  generators g = 24 core (analytic c0) + 162 Global.
Criterion: |r_Mac - r_ref| <= 64 eps S_i and |r_Linux - r_ref| <= 64 eps S_i at every node. Read-only on the copy."""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, platform
sys.path.insert(0, ((_artifact_root + "/work") + '/tools'))
from runtime import Runtime
rt = Runtime(((_artifact_root + "/work"))); rt.install()
import numpy as np
from absolute_common import A_REF
from absolute_fields import prepare_candidate, core_matrices, center_data
from spectral_basis import evaluate_modes
from absolute_model import FrozenLogMesh
EPS = np.finfo(float).eps
d = json.load(open(sys.argv[1])); rows = d['rows']
state = rt.read(rt.research/'campaign/global181_v3/state.json'); epoch = rt.read(state['epoch_path'])
mesh = FrozenLogMesh.load(epoch['meshes']['training']['path']); root = np.sqrt(2*mesh.weights/(np.pi*A_REF**2)); X, Y = mesh.coordinates()
cand = rt.read(rt.research/'campaign/global181_v3/snapshots/accepted_00000278.json'); prep = prepare_candidate(cand, 'center_chart')
cl = float(prep['p'][0]); c = prep['c' 'oefficients'] if False else prep['coefficients']; extra = prep['extra']; modes = prep['modes']
strain = center_data(cl)[0]
idx = np.array([r['node'] for r in rows]); x = X[idx]; y = Y[idx]
M = core_matrices(cl, x, y); V = evaluate_modes(x, y, cl, modes)
def abs_sum(key, center_safe=False):
    core = M[key]-strain[None, :] if center_safe else M[key]
    return abs(core)@abs(c)+abs(V[key])@abs(extra)
Sfx = abs_sum('fx'); Sfy = abs_sum('fy'); Sf = abs_sum('f'); Spsx = abs_sum('psix'); Spsy = abs_sum('psiy'); Sq_center = abs_sum("ratio", True); Sq = abs_sum("ratio")
S_Rf_center = (cl*abs(x)+Spsy)*Sfx+(cl*abs(y)+Spsx)*Sfy+(abs(cl-1)+Sq_center)*Sf; S_Rf = (cl*abs(x)+Spsy)*Sfx+(cl*abs(y)+Spsx)*Sfy+(abs(cl-1)+Sq)*Sf
S = root[idx]*S_Rf
out_rows = []
for k, r in enumerate(rows):
    rm = root[idx[k]]*r['Rf_mac']; rl = root[idx[k]]*r['Rf_linux']; rref = root[idx[k]]*r['Rf_ref85']
    Sc = root[idx[k]]*S_Rf_center[k]
    out_rows.append({**r, 'S_Rf_envelope': float(S_Rf[k]), 'S_i': float(S[k]), 'S_Rf_center_subtracted': float(S_Rf_center[k]), 'ratio_mac_S_center': float(abs(rm-rref)/(EPS*Sc)), 'ratio_linux_S_center': float(abs(rl-rref)/(EPS*Sc)), 'r_ref': rref, 'r_mac': rm, 'r_linux': rl,
                     'ratio_mac_S': float(abs(rm-rref)/(EPS*S[k])), 'ratio_linux_S': float(abs(rl-rref)/(EPS*S[k])),
                     'ratio_linux_minus_mac_S': float(abs(rl-rm)/(EPS*S[k])), 'envelope_over_term_sum': float(S_Rf[k]/r['term_sum'])})
def summ(key):
    v = np.array([r[key] for r in out_rows]); return {'max': float(v.max()), 'p95': float(np.quantile(v, .95)), 'median': float(np.median(v)), 'min': float(v.min())}
worst_l = max(out_rows, key=lambda r: r['ratio_linux_S']); worst_m = max(out_rows, key=lambda r: r['ratio_mac_S'])
res = {'host': platform.node(), 'criterion': 'both |r_Mac - r_ref| and |r_Linux - r_ref| <= 64 eps S_i (lead NOTES 03:41Z); S uses the raw ratio field |c_l-1| + sum|c ratio_g|; the center-subtracted variant is a labeled separate diagnostic', 'nodes': len(out_rows), 'ratio_mac_S_center_subtracted_diagnostic': summ('ratio_mac_S_center'), 'ratio_linux_S_center_subtracted_diagnostic': summ('ratio_linux_S_center'),
       'ratio_mac_S': summ('ratio_mac_S'), 'ratio_linux_S': summ('ratio_linux_S'), 'ratio_linux_minus_mac_S': summ('ratio_linux_minus_mac_S'),
       'envelope_over_term_sum': summ('envelope_over_term_sum'),
       'nodes_failing_mac': [r['node'] for r in out_rows if r['ratio_mac_S'] > 64], 'nodes_failing_linux': [r['node'] for r in out_rows if r['ratio_linux_S'] > 64],
       'per_block_max': {str(b): {'ratio_mac_S': max(r['ratio_mac_S'] for r in out_rows if r['block'] == b), 'ratio_linux_S': max(r['ratio_linux_S'] for r in out_rows if r['block'] == b)} for b in (0, 1, 2)},
       'worst_linux_node': {k: worst_l[k] for k in ('node', 'block', 'r', 'theta', 'Rf_ref85', 'Rf_mac', 'Rf_linux', 'S_Rf_envelope', 'ratio_mac_S', 'ratio_linux_S')},
       'worst_mac_node': {k: worst_m[k] for k in ('node', 'block', 'r', 'theta', 'Rf_ref85', 'Rf_mac', 'Rf_linux', 'S_Rf_envelope', 'ratio_mac_S', 'ratio_linux_S')},
       'passed': all(r['ratio_mac_S'] <= 64 and r['ratio_linux_S'] <= 64 for r in out_rows), 'rows': out_rows}
open(sys.argv[2], 'w').write(json.dumps(res, indent=1)+'\n'); print(json.dumps({k: v for k, v in res.items() if k != 'rows'}, indent=1))
