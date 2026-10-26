"""Diagnose the Linux strict-replay difference: libm exp vs BLAS threads vs provider. Read-only on the copy."""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, math, os, sys, time, platform
from pathlib import Path
sys.path.insert(0, ((_artifact_root + "/work") + '/tools'))
from runtime import Runtime
rt = Runtime(((_artifact_root + "/work"))); rt.install()
import numpy as np
from threadpoolctl import threadpool_limits, threadpool_info
from absolute_common import A_REF
from stage13_integration_v3 import EpochIntegrator
from stage13_model_v3 import CachedAbsoluteProblem as V3
from stage13_model_v2 import CachedAbsoluteProblem as V2cached
from absolute_model_v2 import AbsoluteLossProblem as V2stateless
state = rt.read(rt.research/'campaign/global181_v3/state.json')
seed = rt.read(state['parent_candidate_path'])
integ = EpochIntegrator(seed, state['epoch_path'])
p, extra = np.asarray(state['p']), np.asarray(state['extra'])
with np.load(state['arrays_path'], allow_pickle=False) as a: saved = a['residual'].copy()
out = {'host': platform.node(), 'saved_norm': float(np.linalg.norm(saved)), 'threshold_64eps': float(64*np.finfo(float).eps*np.linalg.norm(saved))}
def cmp(name, r):
    d = r-saved
    out[name] = {'diff_norm': float(np.linalg.norm(d)), 'max_abs': float(np.max(abs(d))), 'n_differ': int(np.count_nonzero(d)),
                 'rel_norm': float(np.linalg.norm(d)/np.linalg.norm(saved)), 'J': float(r@r/2)}
    return r
res = {}
for workers in (1, 4):
    with threadpool_limits(limits=workers, user_api='blas'):
        m = V3(seed, integ.mesh, A_REF, workers=workers, block_size=1024); res[('v3', workers)] = cmp('v3_private_scalar_exp_workers%d' % workers, m.fun(p, extra)); m.clear_cache()
        m = V2cached(seed, integ.mesh, A_REF, workers=workers, block_size=1024); res[('v2c', workers)] = cmp('v2_cached_numpy_exp_workers%d' % workers, m.fun(p, extra)); m.clear_cache()
    with threadpool_limits(limits=workers, user_api='blas'):
        m = V2stateless(seed, integ.mesh, A_REF, block_size=1024); res[('v2s', workers)] = cmp('v2_stateless_workers%d' % workers, m.fun(p, extra))
out['v3_w1_vs_w4_bitwise'] = bool(np.array_equal(res[('v3',1)], res[('v3',4)]))
out['v2c_w1_vs_w4_bitwise'] = bool(np.array_equal(res[('v2c',1)], res[('v2c',4)]))
out['v3_vs_v2cached_w4_diff_norm'] = float(np.linalg.norm(res[('v3',4)]-res[('v2c',4)]))
out['v3_vs_v2stateless_w4_diff_norm'] = float(np.linalg.norm(res[('v3',4)]-res[('v2s',4)]))
# repeat v3 run twice for determinism on this host
with threadpool_limits(limits=4, user_api='blas'):
    m = V3(seed, integ.mesh, A_REF, workers=4, block_size=1024); r1 = m.fun(p, extra); m.clear_cache()
    m = V3(seed, integ.mesh, A_REF, workers=4, block_size=1024); r2 = m.fun(p, extra); m.clear_cache()
out['v3_w4_repeat_bitwise'] = bool(np.array_equal(r1, r2))
# numpy exp vs scalar libm exp on representative exponent arrays
rng = np.random.default_rng(1); z = rng.uniform(-40, 40, 200000)
ne = np.exp(z); se = np.fromiter((math.exp(float(v)) for v in z), dtype=float, count=len(z))
out['numpy_exp_vs_math_exp_differing_fraction'] = float(np.mean(ne != se))
out['numpy_exp_vs_math_exp_max_ulp'] = float(np.max(abs(ne-se)/np.spacing(np.abs(se))))
out['threadpools'] = threadpool_info()
out['relocation'] = rt.record()
Path(sys.argv[1]).write_text(json.dumps(out, indent=1)+'\n')
print(json.dumps({k: v for k, v in out.items() if k not in ('threadpools', 'relocation')}, indent=1))
