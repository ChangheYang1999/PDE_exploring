"""Per-node Mac/Linux rounding model for the strict-replay difference (G1 criterion 1 of the lead's 03:26Z note).

For >= 200 training-mesh nodes spread over the three blocks, near both axes and r <= 0.02, evaluate R_f with the
handoff's own 85-digit Decimal Cartesian Taylor evaluator (field_tests.independent_fields, exact binary coefficients,
analytic c0 at precision 90), and compare the saved Mac residual and the fresh Linux V3 residual in units of
eps * (|w_x f_x| + |w_y f_y| + |q f|) at the node. Read-only on the copy."""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, os, sys, time, platform
from multiprocessing import Pool
from pathlib import Path
sys.path.insert(0, ((_artifact_root + "/work") + '/tools'))
from runtime import Runtime
rt = Runtime(((_artifact_root + "/work"))); rt.install()
import numpy as np
from threadpoolctl import threadpool_limits
from absolute_common import A_REF
from absolute_fields import prepare_candidate
from field_tests import independent_fields
from stage13_integration_v3 import EpochIntegrator
from stage13_model_v3 import CachedAbsoluteProblem as V3
EPS = np.finfo(float).eps
state = rt.read(rt.research/'campaign/global181_v3/state.json'); seed = rt.read(state['parent_candidate_path'])
cand = rt.read(rt.research/'campaign/global181_v3/snapshots/accepted_00000278.json')
integ = EpochIntegrator(seed, state['epoch_path']); mesh = integ.mesh; blocks = integ.training_blocks
p, extra = np.asarray(state['p']), np.asarray(state['extra'])
with np.load(state['arrays_path'], allow_pickle=False) as a: saved = a['residual'].copy()
with threadpool_limits(limits=4, user_api='blas'):
    m = V3(seed, mesh, A_REF, workers=4, block_size=1024); fresh = m.fun(p, extra); m.clear_cache()
root = np.sqrt(2*mesh.weights/(np.pi*A_REF**2)); x, y = mesh.coordinates(); r = np.hypot(x, y)
Rf_mac = saved/root; Rf_lin = fresh/root
rng = np.random.default_rng(20261024); chosen = []
for b in (0, 1, 2):
    idx = np.flatnonzero(blocks == b)
    chosen += list(rng.choice(idx, 56, replace=False))
    th = mesh.theta[idx]; chosen += list(idx[np.argsort(th)[:4]]) + list(idx[np.argsort(th)[-4:]])   # nearest to both axes
small = np.flatnonzero(r <= .02); chosen += list(rng.choice(small, 12, replace=False))
near = np.argsort(abs(r-.02))[:8]; chosen += list(near)
chosen = sorted(set(int(i) for i in chosen))
prepared = prepare_candidate(cand, 'center_chart'); cl = float(p[0])
def one(i):
    ref = independent_fields(prepared, float(x[i]), float(y[i]), precision=85)
    wx = cl*x[i]-ref['psiy']; wy = cl*y[i]+ref['psix']
    terms = abs(wx*ref['fx'])+abs(wy*ref['fy'])+abs(ref['q']*ref['f'])
    em = Rf_mac[i]-ref['Rf']; el = Rf_lin[i]-ref['Rf']
    return {'node': i, 'block': int(blocks[i]), 'r': float(r[i]), 'theta': float(mesh.theta[i]), 'Rf_ref85': ref['Rf'], 'Rf_mac': float(Rf_mac[i]), 'Rf_linux': float(Rf_lin[i]),
            'term_sum': float(terms), 'err_mac': float(em), 'err_linux': float(el),
            'ratio_mac': float(abs(em)/(EPS*terms)) if terms else None, 'ratio_linux': float(abs(el)/(EPS*terms)) if terms else None,
            'ratio_linux_minus_mac': float(abs(Rf_lin[i]-Rf_mac[i])/(EPS*terms)) if terms else None,
            'rel_Rf_err_linux': float(abs(el)/abs(ref['Rf'])) if ref['Rf'] else None}
began = time.time()
with Pool(4) as pool: rows = pool.map(one, chosen, chunksize=4)
def summary(key):
    v = np.array([row[key] for row in rows if row[key] is not None]); return {'max': float(v.max()), 'median': float(np.median(v)), 'p95': float(np.quantile(v, .95)), 'count': int(len(v))}
out = {'host': platform.node(), 'nodes': len(rows), 'blocks_count': {str(b): sum(1 for row in rows if row['block'] == b) for b in (0, 1, 2)},
       'nodes_r_le_0p02': sum(1 for row in rows if row['r'] <= .02), 'eps': EPS, 'reference': 'field_tests.independent_fields, 85-digit Decimal point-centered Cartesian Taylor, analytic c0 precision 90',
       'ratio_mac': summary('ratio_mac'), 'ratio_linux': summary('ratio_linux'), 'ratio_linux_minus_mac': summary('ratio_linux_minus_mac'),
       'per_block': {str(b): {k: summary_k for k, summary_k in ((key, {'max': float(max(row[key] for row in rows if row['block'] == b and row[key] is not None))}) for key in ('ratio_mac', 'ratio_linux', 'ratio_linux_minus_mac'))} for b in (0, 1, 2)},
       'nodes_with_ratio_linux_above_64': [row['node'] for row in rows if row['ratio_linux'] is not None and row['ratio_linux'] > 64],
       'nodes_with_ratio_mac_above_64': [row['node'] for row in rows if row['ratio_mac'] is not None and row['ratio_mac'] > 64],
       'whole_vector': {'fresh_minus_saved_norm': float(np.linalg.norm(fresh-saved)), 'threshold_64eps': float(64*EPS*np.linalg.norm(saved))},
       'seconds': time.time()-began, 'rows': rows}
Path(sys.argv[1]).write_text(json.dumps(out, indent=1)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=1))
