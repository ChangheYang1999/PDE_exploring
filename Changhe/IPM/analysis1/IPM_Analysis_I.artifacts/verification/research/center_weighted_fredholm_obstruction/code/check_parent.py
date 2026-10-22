from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/center_weighted_fredholm_obstruction';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(p):return json.loads(Path(p).read_text())
P=ROOT/'research/center_weighted_quasimodes/evidence/verdict.json';v=read(P)
assert sha(P)=='86b9acba60ca130a8113cc6893f367fb6537c5b76f15e6314bcb32d98aaf37bc'
assert v['status']=='CONFIRMED_ACTUAL_CANONICAL_CENTER_WEIGHTED_QUASIMODES' and v['actual_background_application']=='CONFIRMED'
assert v['sequence']=={'smooth':True,'compact_support':True,'J_exact':'0','Sigma_exact':'0','X_norm_exact':'1','linearized_image_X_norm_limit':'0','zero_leading_far_coefficient':True}
for name,digest in v['files'].items():assert sha(ROOT/name)==digest,name
assert read(E/'proof_first.json')['proof_sha256']==sha(D/'PROOF.md')=='d0cb60d5415332dbcad1bf2fd7e367f95e45b1755bf026294cd089cc24ef2c80'
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ACCEPTED_PARENT_AND_PROOF_PINS_FUNCTIONAL_CONSEQUENCES_REQUIRE_REVIEW','source_sha256':sha(Path(__file__)),'proof_sha256':sha(D/'PROOF.md'),'parent_sha256':sha(P),'parent_status':v['status'],'parent_files':v['files'],'parent_file_count':len(v['files']),'scope':'Input/provenance check only. The added diagonal choice, weak convergence and operator consequences are proved in PROOF.md and are not tested by finite computation.'}
with (E/'parent_check.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print({k:out[k] for k in ['utc','status','parent_file_count']})
