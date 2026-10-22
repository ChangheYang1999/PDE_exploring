"""Authenticate complete checks, actual reviews and a separately later adjudication."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def need(v,s):
 if not v:raise ValueError(s)
post=load(D/'evidence/postreview_record.json');need(post['status']=='CONFIRMED_AFTER_READING_ALL_ACTUAL_REVIEWS','own decision');need(post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'own text');need(post['all_substantive_objections_resolved'] is True,'scope adjudicated');reviews=[];pins={}
for e in post['reviews']:
 tag=e['tag'];r=B/'notes/reviews';m=load(r/(tag+'_metadata.json'));raw=load(r/(tag+'_response.json'));text=(r/(tag+'_response.md')).read_text();request=r/(tag+'_request.txt')
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');need(m['stop_reason']==raw['stop_reason']=='end_turn','complete response');need(m['request_id']==e['request_id'] and sha(request)==m['input_sha256']==e['input_sha256'] and sha(r/(tag+'_response.json'))==e['response_sha256'],'actual identity');need(text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n','actual text');need(request.read_text().endswith('\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])),'current reviewed files');need(datetime.fromisoformat(m['end_utc'])<datetime.fromisoformat(post['utc']),'later own decision');reviews.append(m)
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=r/(tag+'_'+suffix);pins[str(p.relative_to(B))]=sha(p)
need([e['tag'] for e in post['reviews']]==['derivative_intended_partition_proof','derivative_intended_partition_actual','derivative_intended_partition_followup','derivative_intended_partition_primitives'],'complete collaboration chain')
c=load(D/'evidence/check.json');a=load(D/'evidence/audit.json');s=load(D/'evidence/source_binding.json');need(c['status']=='PASS_COHERENT_PARTITION_SOURCE_ROUNDING_AND_WIDTHS' and a['status']=='PASS_INDEPENDENT_ALL_ROWS_AND_PARAMETER_COVERAGE','actual checks');need(c['rows']==a['rows']==19389 and c['node_inclusions']==a['node_inclusions']==19392 and a['bernstein_shift_boxes']==77556,'exhaustive counts');need(c['delta']==a['delta']=='1677/629659522901737472' and c['regions']==a['regions'],'exact shared result');need(datetime.fromisoformat(c['utc'])<datetime.fromisoformat(a['utc'])<datetime.fromisoformat(reviews[1]['start_utc']),'actual output chronology')
for obj,key in [(c,'files'),(a,'pins'),(s,'pins')]:
 for name,h in obj[key].items():need(sha(B/name)==h,'source pin '+name);pins[name]=h
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_COHERENT_DERIVATIVE_PARTITION_AND_CONDITIONAL_WEIGHT_THEOREM','rows':19389,'node_inclusions':19392,'bernstein_shift_boxes':77556,'regions':c['regions'],'max_exact_start_displacement':c['delta'],'coordinate_weight_loss_strict_upper':'1.00000000000004','independent_rational_loss_upper':a['independent_rational_exp_upper'],'actual_reviews':reviews,'postreview_record':post,'files':dict(sorted(pins.items())),'scope':'Finite coherent geometry, source rounding/parameter binding and a conditional exact weight/norm theorem only. Physical W majorants, density/Green input linkage, derivative and Bernstein arithmetic, all omitted tails, historical execution, numerical full-norm sums, inverse/lower-bound claims and every IPM endpoint remain OPEN. Topic153 literal rounded union is unchanged.'}
with (D/'evidence/verdict.json').open('x') as f:json.dump(out,f,indent=1);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(D/'evidence/verdict.json')}))
