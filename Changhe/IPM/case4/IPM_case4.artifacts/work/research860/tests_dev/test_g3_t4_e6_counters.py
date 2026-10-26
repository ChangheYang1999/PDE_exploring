"""E6 lane fixture (lead 11:54Z item 8): the exact zero-trial counter lines of g3_t4 run on a real Model860 built over a small point set (shapes860.point_model at three
points with r > 1, so no origin series is needed): after model.fun at the seed and model.clear_cache(), a second model.fun at the same key advances fun_calls by 1 with
evaluation_cache_hits unchanged (re-evaluation); without the clear, the same call is a cache hit (hits + 1). The g3_t4 source must contain the exact lines executed here.
Runs under the guard. Records sha256 of g3_t4 and this script (E10). Usage: fixture_g3_t4_e6_counters.py <g3_t4.py> <out.json>"""
_artifact_root = str(next(p for p in __import__("pathlib").Path(__file__).resolve().parents if (p / "work" / "research860").is_dir() and (p / "outputs").is_dir()))
import json, sys, hashlib, time
from pathlib import Path
LANE = Path((_artifact_root)); sys.path.insert(0, str(LANE/'work/research860')); sys.path.insert(0, str(LANE/'work/research860/tests')); sys.path.insert(0, str(LANE/'work/tools'))
import numpy as np
import basis860 as B
from shapes860 import point_model
g3 = Path(sys.argv[1]).resolve(); src = g3.read_text(); out_json = Path(sys.argv[2]).resolve()
res = {'source': str(g3), 'source_sha256': hashlib.sha256(g3.read_bytes()).hexdigest(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:300], flush=True)
LINES = ["model.clear_cache(); hits0 = int(model.evaluation_cache_hits); calls0 = int(model.fun_calls); builds0 = int(model.cache_builds)", "rz2 = model.fun(Pz, hz); hits1 = int(model.evaluation_cache_hits); calls1 = int(model.fun_calls)", "reevaluated = bool(hits1 == hits0 and calls1 == calls0+1)"]
record('g3_t4_contains_the_exact_counter_lines', all(l in src for l in LINES) and "cache_record().get('fun_calls'" not in src)
sd = np.load(B.REPLAY_REFERENCE_FILE); P = sd['P'].copy(); high = sd['high'].copy()
t0 = time.time(); model, root = point_model([1.5, 2.5, 40.], [0.7, 1.1, 30.], workers=1); r0 = model.fun(P, high); t_build = time.time()-t0
Pz, hz = P.copy(), high.copy()                       # the zero trial reproduces the seed key bitwise (as feasible_trial(0) does in T4)
hitsA = int(model.evaluation_cache_hits); callsA = int(model.fun_calls); rA = model.fun(Pz, hz); hitsB = int(model.evaluation_cache_hits); callsB = int(model.fun_calls)
record('without_clear_same_key_is_a_cache_hit', hitsB == hitsA+1 and callsB == callsA+1 and rA.tobytes() == r0.tobytes(), hits=[hitsA, hitsB], calls=[callsA, callsB])
model.clear_cache(); hits0 = int(model.evaluation_cache_hits); calls0 = int(model.fun_calls); builds0 = int(model.cache_builds)
rz2 = model.fun(Pz, hz); hits1 = int(model.evaluation_cache_hits); calls1 = int(model.fun_calls)
reevaluated = bool(hits1 == hits0 and calls1 == calls0+1)
record('after_clear_the_exact_lines_show_reevaluation', reevaluated and rz2.tobytes() == r0.tobytes() and int(model.cache_builds) >= builds0, hits=[hits0, hits1], calls=[calls0, calls1], cache_builds_delta=int(model.cache_builds)-builds0, bitwise_equal_to_first_evaluation=rz2.tobytes() == r0.tobytes(), build_seconds=round(t_build, 2))
record('counter_fields_are_integers', all(type(v) is int for v in (hits0, hits1, calls0, calls1)))
model.clear_cache()
res['passed'] = all(c['passed'] for c in res['cases'].values()); out_json.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
