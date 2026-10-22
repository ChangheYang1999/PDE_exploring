from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_point_jets';p=D/'evidence/output_audit.json';a=json.loads(p.read_text());assert a['status']=='PASS_COMPLETE_THIRTEEN_POINT_DERIVATIVE_OUTPUT_AUDIT'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
for n,h in a['files'].items():assert sha(B/n)==h
out={k:a[k] for k in ['utc','status','counts','runtime','seconds','scope','files']}
out['records']=[{k:r[k] for k in ['cell','t_exact','comparisons']} for r in a['records']]
out['maxima_display_only']={k:{j:v[j] for j in ['display_only','lower_cell','upper_cell']} for k,v in a['max_over_thirteen_point_Wiener_over_m'].items()}
out['exact_data_not_reproduced_here']='All exact rational intervals are retained in output_audit.json and all 26 coefficient files. This extract audits digests and selects counts and metadata; it does not regenerate point calculations.'
out['extracted_utc']=datetime.now(timezone.utc).isoformat();out['files'][str(p.relative_to(B))]=sha(p);out['files'][str(Path(__file__).relative_to(B))]=sha(Path(__file__))
with (D/'evidence/review_extract.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['extracted_utc'],len(out['files']))
