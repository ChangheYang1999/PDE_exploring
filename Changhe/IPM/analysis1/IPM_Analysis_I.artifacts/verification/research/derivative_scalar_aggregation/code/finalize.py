from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_scalar_aggregation';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={}
for name,status in [('compute.json','PASS_EXACT_SAVED_SCALAR_AGGREGATION_PHYSICAL_OPEN'),('independent.json','PASS_BIT_DECIMAL_AND_TWO_INTERVAL_SCALAR_RECONSTRUCTION_PHYSICAL_OPEN'),('coverage.json','PASS_EXACT_SOURCE_ROW_COVERAGE_AND_REPORT_BINDING'),('derivative_order.json','PASS_ORDER_LABELS_AND_ALL_SAVED_DERIVATIVE_FIELDS_PHYSICAL_OPEN')]:
 a=load(D/'evidence'/name);check(a['status']==status,'calculation status')
 for n,h in a['files'].items():check(sha(B/n)==h,'calculation pin');check(n not in pins or pins[n]==h,'conflict');pins[n]=h
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
first=load(D/'evidence/compute.json');second=load(D/'evidence/independent.json');coverage=load(D/'evidence/coverage.json');order=load(D/'evidence/derivative_order.json')
check(first['maxima']==second['maxima'],'all exact maxima')
check(second['rows']==19389 and second['decoded_binary64_fields']==213279 and second['exact_scalar_comparisons']==232668 and second['interval_enclosures']==465336,'finite comparison counts')
check(coverage['ordered_source_rows']==19389 and coverage['footer_read'] is True and order['all_order_indexed_fields']==121989,'coverage')
from fractions import Fraction as F
check(F(first['maxima']['gradient']['upper_exact'])==F(27937224698257691,66597438051412104)<F(839,2000),'gradient ceiling')
check(F(first['maxima']['second_partial']['upper_exact'])==F(47432765931014321977,66508632013116448)<F(3566,5),'second partial ceiling')
check(F(427,1000)<F(second['saved_R5_middle_maximum_exact'])==F(7116661148760413,16649359512853026)<F(106861,250000),'R5 direction')
check(F(first['maxima']['K']['upper_exact'])<F(2254,5) and F(first['maxima']['EK']['upper_exact'])<2119,'additional ceilings')
check(datetime.fromisoformat(load(D/'evidence/proof_first.json')['utc'])<datetime.fromisoformat(first['utc']),'proof chronological check')
reviews={}
for tag,stop in [('derivative_scalar_aggregation_complete','end_turn'),('derivative_scalar_aggregation_resolved','end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']==stop,'stop');check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'request digest')
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 check('VERDICT: CONFIRM_SAVED_DERIVATIVE_SCALARS_PHYSICAL_OPEN' in text.splitlines(),'accepted restricted scalar audit')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for n in ['PROOF.md','ADDENDUM.md','SOURCE_CLAIMS.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md']:check((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SAVED_DERIVATIVE_SCALARS_PHYSICAL_OPEN','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF,ADDENDUM,SOURCE_CLAIMS,REVIEW_RESOLUTIONS,FINAL_ADJUDICATION. Complete saved scalar audit only. Printed R5 0.427 is not an outward ceiling of its saved majorants. Physical derivatives, execution provenance, canonical inputs, weights, geometric coverage, tails, inverse and IPM endpoints remain OPEN.'}
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
