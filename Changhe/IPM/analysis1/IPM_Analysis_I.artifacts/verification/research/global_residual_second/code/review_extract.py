"""Compact completed scalar evidence with every source pin retained."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/global_residual_second'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
m=load(D/'data_exact/manifest.json');a=load(D/'evidence/arb_assembly.json');q=load(D/'evidence/output_audit.json');assert q['status']=='PASS_GLOBAL_SECOND_SCALAR_ASSEMBLY_IV220_AND_EXACT_INTEGER_CHECK';pins=dict(q['files'])
for n,h in pins.items():assert sha(B/n)==h
for p in [D/'evidence/output_audit.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETED_GLOBAL_SECOND_REVIEW_EXTRACT','preparation_utc':m['utc'],'arb_utc':a['utc'],'independent_check_utc':q['utc'],'cells':m['cells'],'old_global_verdict_sha256':m['old_global_verdict_sha256'],'actual_full_middle_verdict_sha256':m['actual_full_middle_verdict_sha256'],'squared_norm_exact':a['squared_norm_exact'],'root_arb512_exact':a['root_arb512_exact'],'root_iv220_exact':q['root_iv220_exact'],'integer_lower_exact':q['integer_lower_exact'],'strict_root_ceiling_exact':q['strict_root_ceiling_exact'],'strict_root_ceiling_decimal':q['strict_root_ceiling_decimal'],'suprema':a['suprema'],'files':dict(sorted(pins.items())),'scope':q['scope']+' Text reviewer sees this exact scalar extract and the algorithms, not every inherited regional coefficient file.'}
with (D/'evidence/review_extract.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'norm_ceiling':q['strict_root_ceiling_decimal'],'pins':len(pins)}))
