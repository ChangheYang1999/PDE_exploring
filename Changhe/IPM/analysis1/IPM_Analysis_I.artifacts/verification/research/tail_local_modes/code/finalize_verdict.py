"""Freeze audited topic114. No JS, servers, RLScience, outside writes."""
import json,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_modes';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 a=read(E/'audit.json');assert a['status']=='PASS_COMPLETE_FINITE_AUDIT_REQUIRES_COLLABORATIVE_CLOSURE';pins=dict(a['files'])
 for rel,h in pins.items():assert sha(B/rel)==h,rel
 assert a['counts']['all_finite_derivative_weights']==6240 and a['counts']['prior_frozen_pins']==249 and a['counts']['complete_engine_reruns']==2
 assert F(a['source_margin_exact'])>F('6.6989e-7')
 reviews={}
 for tag in ('tail_local_modes_proof','tail_local_modes_closure'):
  R=B/'notes/reviews';m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
  assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
  assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
  supplied=req[req.index('\n\nFILE ')+2:];current='\n\n'.join('FILE '+p+'\n'+(B/p).read_text() for p in m['files']);assert supplied==current,tag
  text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert text==(R/(tag+'_response.md')).read_text()
  if tag.endswith('closure'):assert 'ACCEPT' in text and 'None that block this scope' in text
  else:assert 'sound as written' in text
  for suf in ('_metadata.json','_request.txt','_response.json','_response.md'):p=R/(tag+suf);pins[str(p.relative_to(B))]=sha(p)
  reviews[tag]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
 for p in (E/'audit.json',E/'audit.log',E/'arb.log',E/'iv.log',E/'proof_review.log',E/'closure_review.log',E/'review_summary.json',D/'CLOSURE_NOTES.md',D/'PUBLICATION.md',D/'FINAL_ADJUDICATION.md',Path(__file__)):pins[str(p.relative_to(B))]=sha(p)
 for rel,h in pins.items():assert sha(B/rel)==h,rel
 v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_MODE_LOCAL_VELOCITY_AND_ALL_ADMISSIBLE_T_HIGHER_TAIL_SOURCE_DEFECT','scope':'PROOF with ADDENDUM, CLOSURE_NOTES and FINAL_ADJUDICATION. Every admissible106 family cutoff T>=Rb: strict component C3 velocity bounds on disk9 and source derivative defect>6.6989e-7. Prior two certified H2 arrays reused explicitly. No surrounding exclusion, small global forcing, inverse, stationary solution or endpoint.','strict_public_ceilings':a['strict_public_ceilings'],'strict_source_derivative_lower':a['strict_source_defect_lower'],'counts':a['counts'],'reviews':reviews,'source_archive':a['source_archive'],'open':['Global residual norm ceilings and physical inverse','Nonlinear closure and meaningful uncertainty neighborhood of X3','Every decisive endpoint'],'files':dict(sorted(pins.items()))}
 (E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'pins':len(pins),'verdict_sha256':sha(E/'verdict.json')}))
if __name__=='__main__':main()
