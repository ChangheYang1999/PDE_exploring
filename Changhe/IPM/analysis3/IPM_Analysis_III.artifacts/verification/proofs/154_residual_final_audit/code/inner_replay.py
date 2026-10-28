"""Replay an upper tail bound: compare inequalities, not equality of bounds."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import importlib.util,json,hashlib
from flint import ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('inner_replay_I',LANE/'proofs/134_residual_green_taylor/code/integrate.py')
I=importlib.util.module_from_spec(sp);sp.loader.exec_module(I)
ctx.prec=640;ctx.threads=1
I.M.SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
d=I.M.Data();cache=I.G.load_cache(d)
meta=json.loads((LANE/'proofs/134_residual_green_taylor/evidence/production_28/metadata.json').read_text())
assert d.sha==meta['source_sha256']
ends={'inner':I.inner_eps(d,cache)}
fresh=I.inner_tail(d,ends,Q(-40),I.ANG.beta_mass())
saved=meta['inner_tail']
fresh_upper=Q(fresh['energy_upper']['upper_exact']);saved_upper=Q(saved['energy_upper']['upper_exact'])
out={'date':datetime.now(timezone.utc).isoformat(),'bits':640,'source_sha256':d.sha,'checker_sha256':sha(Path(__file__)),'fresh':fresh,'saved':saved,'fresh_upper_le_saved_upper':fresh_upper<=saved_upper,'difference_exact':str(saved_upper-fresh_upper)}
(TOP/'evidence/inner_replay.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('fresh','saved')},indent=2),flush=True)
assert fresh_upper<=saved_upper,'The independently recomputed upper bound must fit within the certified stored upper bound.'
p=TOP/'evidence/replay.json';oldsha=sha(p);record=json.loads(p.read_text())
assert record['bits']==640 and record['degree']==36 and len(record['rows'])==13
assert len({r['leaf_id'] for r in record['rows']})==13
assert all(r['overlap']=='PASS' for r in record['rows'])
record.update({'date':out['date'],'status':'REPLAY_PASS','inner_tail':fresh,'inner_check':'fresh upper <= stored upper','previous_partial_replay_sha256':oldsha,'inner_checker_sha256':out['checker_sha256'],'source_sha256':d.sha})
p.write_text(json.dumps(record,indent=2)+'\n')
