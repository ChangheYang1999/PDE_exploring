"""Separate closure after actual reviews and independently written adjudication."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def need(v,s):
 if not v:raise ValueError(s)
expected=[('radial_first_failure_actual', 'efbb5ec6-5984-400a-a2e5-60747efa4dae'), ('radial_first_failure_followup', '3ff30d55-2f8f-45d3-b075-b282d67ab59a')]
# Request IDs, digest and response hashes are separately fixed by the adjudication record.
post=load(D/'evidence/postreview_record.json');need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING','own decision');need(post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'written decision binding');reviews=[];pins={}
for tag,expected_id in expected:
 r=B/'notes/reviews';m=load(r/(tag+'_metadata.json'));raw=load(r/(tag+'_response.json'));text=(r/(tag+'_response.md')).read_text();request=r/(tag+'_request.txt')
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');need(m['stop_reason']==raw['stop_reason']=='end_turn','completed response');need(sha(request)==m['input_sha256'],'request hash');need(request.read_text().endswith('\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])),'current reviewed bundle');need(text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n','actual extracted text')
 need(m['request_id']==expected_id,'fixed actual request ID')
 entry={'tag':tag,'request_id':m['request_id'],'input_sha256':m['input_sha256'],'response_sha256':sha(r/(tag+'_response.json'))};need(entry in post['reviews'],'own response binding');need(datetime.fromisoformat(m['end_utc'])<datetime.fromisoformat(post['utc']),'own later decision');reviews.append(m)
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=r/(tag+'_'+suffix);pins[str(p.relative_to(B))]=sha(p)
need(len(post['reviews'])==2,'two full responses')
c=load(D/'evidence/check.json');a=load(D/'evidence/audit.json');need(c['exact_range_contained'] is True and c['arb_range_contained'] is False and c['iv_range_contained'] is True,'actual diagnosis');need(a['status']=='PASS_ORIGINAL_INPUTS_AND_EXACT_MARGINS' and a['strict_exact_containment'] is True and len(a['original_input_elements'])==6,'independent exact audit');need(datetime.fromisoformat(a['utc'])<datetime.fromisoformat(reviews[-1]['start_utc']),'actual audit before followup')
for name,v in c['pins'].items():
 p=Path(v['path']);need(sha(p)==v['sha256'],'source '+name);pins[str(p.relative_to(B)) if p.is_relative_to(B) else str(p)]=v['sha256']
for name,h in a['pins'].items():need(sha(B/name)==h,'audit pin '+name);pins[name]=h
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ISOLATED_EXACT_COEFFICIENT_CONTAINMENT_AND_SUFFICIENT_TEST_FAILURE','cell':2955,'mode':135,'family':'R','coefficient':0,'exact_range_contained':True,'arb_sufficient_bound_failed':True,'iv_sufficient_bound_passed':True,'exact_margin_over_candidate_radius_lower_bound':'1/100000','actual_reviews':reviews,'postreview_record':post,'files':dict(sorted(pins.items())),'scope':'One unchanged regenerated coefficient box and six independently decoded original inputs. Exact whole-input-box membership for R0 only. Full radial/canonical membership, other coefficients and remainders, physical derivatives, inverse, tails and every IPM endpoint remain OPEN.'}
with (D/'evidence/verdict.json').open('x') as f:json.dump(out,f,indent=1);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(D/'evidence/verdict.json')}))
