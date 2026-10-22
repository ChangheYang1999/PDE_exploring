"""Authenticate the restricted exterior threshold and its completed reviews."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
sys.set_int_max_str_digits(200000)
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/exterior_conic_threshold';R=B/'notes/reviews'
def sha(p):
 with Path(p).open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def require(x,s):
 if not x:raise ValueError(s)
a=load(D/'evidence/scalars.json');c=load(D/'evidence/audit.json');ex=load(D/'evidence/review_extract.json')
require(a['status']=='PASS_TWO_METHOD_EXTERIOR_CONIC_SCALARS_REQUIRES_REVIEW' and c['status']=='PASS_EXACT_SAVED_NUMBER_AND_DEPENDENCY_AUDIT','complete result')
require(c['scalar_sha256']==sha(D/'evidence/scalars.json') and c['producer_sha256']==sha(D/'code/compute.py') and c['audit_sha256']==sha(D/'code/audit.py'),'audit binding')
require(c['counts']['strict_public_comparison']==18 and c['counts']['input_hash']==51,'comparison counts')
pins=dict(a['files'])
for name,h in pins.items():require(sha(B/name)==h,'input '+name)
for q in ex['entries']:
 require(sha(B/q['file'])==q['sha256'],'extract input');pins[q['file']]=q['sha256']
for method,rows in ex['outward_40decimal_rational_scalar_intervals'].items():
 for key,pair in rows.items():
  l,u=map(F,pair);rl,ru=map(F,a['methods'][method][key]);require(l<=rl<=ru<=u,'outward extract')
for method,rows in ex['positive_40decimal_rational_lower_margins'].items():
 for key,value in rows.items():require(0<F(value)<=F(c['strict_margins_exact'][method][key]),'strict margin extract')
reviews={}
for tag,expected in [('exterior_conic_proof','718d8c3a098eb72c42d9d06d2c1151f62daf0aa3ce580bbd7dd5ef6d37ed6ed2'),('exterior_conic_complete','4d3f046fcd90c77ec4b179e756e3d2b79f84b2daa012c3974b4cda5eb5dbe5e1')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 require(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual model')
 require(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']==expected,'request digest')
 require(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';require(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag.endswith('complete'):require('CONFIRMED_ANALYTIC_EXTERIOR_CONIC_THRESHOLD_TAU5 is justified' in text and 'OPEN' in text,'accepted scope')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for root in [D,D/'code',D/'evidence']:
 for p in root.iterdir():
  if not p.is_file() or p.is_symlink() or p.name=='verdict.json':continue
  name=str(p.relative_to(B));h=sha(p);require(name not in pins or pins[name]==h,'final collision');pins[name]=h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ANALYTIC_EXTERIOR_CONIC_THRESHOLD_TAU5','t_b_exact':a['parameters_exact']['t_b'],'tau_start_exact':'5','public_radius_strict_upper':'510000','T_strict_upper':'-11/50','s_strict_lower':'557/100','v1_v2_strict_lower':'557/100','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory FINAL_ADJUDICATION. Inherited accepted canonical exterior theorem53. Complete tau>=5 only; finite middle/exterior/global flow/inverse/nonlinear/neighborhood/PDE endpoints OPEN.'}
p=D/'evidence/verdict.json';require(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
