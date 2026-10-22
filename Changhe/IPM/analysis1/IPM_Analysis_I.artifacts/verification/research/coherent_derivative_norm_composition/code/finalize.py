"""Authenticate actual finite composition and a later independent adjudication."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def load(p):return json.loads(p.read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def need(v,s):
 if not v:raise ValueError(s)
post=load(D/'evidence/postreview_record.json');need(post['status']=='CONFIRMED_AFTER_COMPLETED_FOLLOWUP_REVIEW' and post['all_substantive_objections_resolved'] is True,'own decision');need(post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'own text');pins={};reviews=[]
need([x['tag'] for x in post['reviews']]==['coherent_norm_proof','coherent_norm_complete'],'complete actual chain')
for e in post['reviews']:
 tag=e['tag'];m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();request=R/(tag+'_request.txt')
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');need(m['stop_reason']==raw['stop_reason']==('max_tokens' if tag=='coherent_norm_proof' else 'end_turn'),'preserve truncated first and complete second');need(m['request_id']==e['request_id'] and sha(request)==m['input_sha256']==e['input_sha256'] and sha(R/(tag+'_response.json'))==e['response_sha256'],'review identity');need(text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n','response text');req=request.read_text();need(req.endswith('\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])),'current reviewed files')
 for restriction in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster']:need(restriction in req,'delegation restrictions')
 need(datetime.fromisoformat(m['end_utc'])<datetime.fromisoformat(post['utc']),'later own decision');reviews.append(m)
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);pins[str(p.relative_to(B))]=sha(p)
c=load(D/'evidence/check.json');a=load(D/'evidence/audit.json');need(c['status']=='PASS_COMPLETE_ROW_BINDING_AND_CONDITIONAL_CORRECTED_CEILINGS' and a['status']=='PASS_INDEPENDENT_ALL_ROWS_AND_CORRECTED_CEILINGS','both actual computations');need(c['rows']==a['rows']==19389 and c['exact_scalar_comparisons']==a['manual_ieee_scalar_comparisons']==135723,'complete counts');need(c['delta']==a['delta']=='1677/629659522901737472' and c['regions']==a['regions'],'shared geometry');need(datetime.fromisoformat(c['utc'])<datetime.fromisoformat(a['utc'])<datetime.fromisoformat(reviews[1]['start_utc']),'actual chronology')
for obj in [c,a]:
 for n,h in obj['files'].items():need(sha(B/n)==h,'actual source pin '+n);need(n not in pins or pins[n]==h,'compatible pins');pins[n]=h
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_COHERENT_ANNULUS_X_NORM_COMPOSITION','rows':19389,'exact_scalar_comparisons_per_engine':135723,'strict_conditional_norm_ceilings':['0.385656','585.874'],'alpha':'-1389482001461413/140737488355328','beta':'7074968463789829/281474976710656','delta':c['delta'],'accepted_dependencies':c['accepted_dependencies'],'actual_reviews':reviews,'postreview_record':post,'files':dict(sorted(pins.items())),'scope':'Conditional norms on the coherent annulus only. Requires the physical W bounds and specified weak regularity. Both tails, numerical scaling-vector numerator, global inverse and every decisive IPM endpoint remain OPEN.'}
with (D/'evidence/verdict.json').open('x') as f:json.dump(out,f,indent=1);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(D/'evidence/verdict.json')}))
