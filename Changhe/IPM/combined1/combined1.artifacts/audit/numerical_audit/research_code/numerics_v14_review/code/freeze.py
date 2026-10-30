from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
R=Path.cwd();B=R/'research/numerics_v14_review';files={}
def bind(name,p):
 p=Path(p);b=p.read_bytes();files[name]={'path':str(p.relative_to(R)),'sha256':sha256(b).hexdigest(),'bytes':len(b)}
def copy(name,p):
 b=Path(p).read_bytes();out=B/'source'/name
 with out.open('xb') as f:f.write(b)
 bind(name,out);files[name]['original']=str(p)
bind('publication',B/'source/numerics_v14.md')
for n in ['016','022','023','024','025','026']:bind(n,R/f'research/numerics_v13_audit/source/N1_{n}_weaktests3.json')
bind('027',R/'research/continuation027_float_audit/source/027_weaktests3.json')
copy('028',R.parent/'c1-n1/numerics/optimization/candD2/legqs25_nin24_m9to15_gpu_m16_weaktests3.json')
for n in ['N1_weak_tests3.py','N1_ipm_opt3.py','N1_run_quot.py','N4_024_holdout.json','N4_025_holdout.json','N4_025_shape_peer.json','N4_025_weak.json','N4_026_holdout.json','N4_016_cells.json']:bind(n,R/'research/numerics_v13_audit/source'/n)
for name,p in [('audit372','research/numerics_v13_audit/verification/result.json'),('proof372','research/numerics_v13_audit/PROOF.md'),('015_cells','research/candidate015_dyadic_peer/verification/result_v02.json'),('accepted_distances','research/final_table_trace/source/distance_contract_v01.json'),('accepted_distances_check','research/final_table_trace/verification/distance_v02.json')]:bind(name,R/p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha256((B/'PROOF.md').read_bytes()).hexdigest(),'checker_exists':(B/'code/check.py').exists(),'files':files}
assert not obj['checker_exists']
with (B/'source/MANIFEST.json').open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
print(obj['utc'],len(files),sha256((B/'source/MANIFEST.json').read_bytes()).hexdigest())
