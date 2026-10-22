"""Authenticate actual review bundles and immutable composition artifacts."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_source_composition';E=D/'evidence';R=B/'notes/reviews'
def now():return datetime.now(timezone.utc).isoformat()
def when(s):return datetime.fromisoformat(s)
def need(x,s):
 if not x:raise ValueError(s)
def unique(items):
 out={}
 for k,v in items:need(k not in out,'duplicate JSON key');out[k]=v
 return out
def load(p):return json.loads(Path(p).read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,v):
 with Path(p).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def pin(pins,n,h=None):
 p=Path(n);p=p if p.is_absolute() else B/p;p=p.resolve()
 if p.is_relative_to(B):n=str(p.relative_to(B))
 else:need(str(p)=='numerics/data/cert_green.npz' and h=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1','fixed read-only external pin');n=str(p)
 actual=sha(p);need(h is None or h==actual,'immutable pin '+n);need(n not in pins or pins[n]==actual,'consistent duplicate pin');pins[n]=actual;return actual
def merge(pins,v):
 for n,h in v['files'].items():pin(pins,n,h)
def auth(pins,tag,verdict,required):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();req=(R/(tag+'_request.txt')).read_text()
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and 'availability_error' not in m,'actual completed Opus5.5')
 need(len(m['files'])==len(set(m['files'])) and set(required)<=set(m['files']),'mandatory complete review bundle')
 pre=req.split('\n\nFILE ',1)[0];need(all(v in pre for v in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds','no outside writes','no people contact']),'all delegated restrictions')
 need(req==pre+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']) and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'unchanged actual full request')
 need(text=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n','actual full response bytes')
 need(re.findall(r'(?m)^VERDICT:\s*(\w+)\s*$',text)==[verdict] and text.rstrip().splitlines()[-1]=='VERDICT: '+verdict,'unique exact scoped final verdict')
 need(when(m['start_utc'])<=when(m['end_utc'])<=datetime.now(timezone.utc),'actual review chronology')
 for n in m['files']:pin(pins,n)
 for suf in ['metadata.json','request.txt','response.json','response.md']:pin(pins,R/(tag+'_'+suf))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
def post(pins,tag,review,record,assessment):
 v=load(record);rh=sha(R/(tag+'_response.json'));need(v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==review['request_id'] and v['input_sha256']==review['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(assessment) and v['all_substantive_objections_resolved'] is True,'independent postreview record')
 need(review['request_id'] in assessment.read_text() and rh in assessment.read_text(),'written actual review binding');need(when(review['end_utc'])<when(v['utc'])<=datetime.now(timezone.utc),'actual later adjudication')
 m=load(R/(tag+'_metadata.json'));need(str(assessment.relative_to(B)) not in m['files'] and str(record.relative_to(B)) not in m['files'],'separately later post outside bundle');pin(pins,record);pin(pins,assessment);return v
def preparation():
 v=load(E/'preparation_acceptance.json');need(v['status']=='ACCEPTED_CANONICAL_SOURCE_COMPOSITION_PREPARATION_ONLY','accepted preparation');pins={};merge(pins,v);pin(pins,E/'preparation_acceptance.json');return pins,v
def full():
 pins,p=preparation();v=load(E/'checks.json');need(v['status']=='PASS_COMPLETE_CANONICAL_SOURCE_PREMISE_COMPOSITION_REQUIRES_ACTUAL_REVIEW' and v['complete_application'] is True,'actual complete new composition')
 need(v['counts']=={'archive_spans':1558,'archive_H_shapes':3265568,'archive_moment_shapes':813276,'selected_records':7,'selected_H_balls':14672,'selected_moment_two_method_boxes':3654} and v['selected_spans']==list(range(663,670)),'complete exact source counts')
 merge(pins,v);pin(pins,E/'checks.json');n='research/canonical_archive_second/evidence/verdict.json';d=load(B/n);need(v['accepted_dependencies']['156']=={'sha256':sha(B/n),'utc':d['utc']} and d['status']=='CONFIRMED_COMPLETE_CANONICAL_MOMENT_ARCHIVE','actual same accepted156')
 need(when(p['utc'])<when(v['start_utc']) and when(d['utc'])<when(v['start_utc'])<when(v['utc']),'actual application after both accepted prerequisites');return pins,p,v
