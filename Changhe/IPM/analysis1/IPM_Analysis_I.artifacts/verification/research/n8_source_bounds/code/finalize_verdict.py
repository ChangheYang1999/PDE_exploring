"""Freeze the limited N8 metadata audit, with current two-round model review."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_source_bounds';E=D/'evidence';R=B/'notes/reviews'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_METADATA_OBSTRUCTION_AND_CONDITIONAL_ARITHMETIC'
assert c['counts']=={'missing_disc_witnesses':3,'reported_scalar_upper_comparisons':2,'conditional_exact_identities_and_inequalities':6}
for rel,h in c['files'].items():assert sha(B/rel)==h,rel
for row in c['missing_disc_coverage']:
 assert F(row['missing_point_radius_lower'])-F(row['radial_cover_upper'])==F(row['positive_gap'])>0
assert F(33,2000)*F('13.34')==F(22011,100000)
assert F('3.374')-F(22011,100000)==F(315389,100000)>F(500,159)
assert F(1,20)*F('18.634')==F(9317,10000)
assert F('3.374')-F(9317,10000)==F(24423,10000)>F(100,41)
reviews={};files={}
for tag in ['n8_metadata','n8_metadata_followup']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());req=(R/(tag+'_request.txt')).read_text();raw=json.loads((R/(tag+'_response.json')).read_text());ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag.endswith('followup'):assert 'ACCEPT_N8_METADATA_SCOPE' in ans[:200] and 'retract' in ans and 'withdraw' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_METADATA_OBSTRUCTION_AND_CONDITIONAL_ARITHMETIC','confirmed':['Fine rows delta=.05,.1,.2 lack complete-disc coverage relative to the reported radial endpoint. This does not prove the derivative bounds false.','If full-disc C_V<13.34 at delta=.0165 then E<.22011 and K1<.318.','If full-disc C_V<18.634 at delta=.05 then E<.9317 and K1<.41.'],'counts':c['counts'],'reviews':reviews,'scope':'Reported metadata and conditional exact algebra only. The ADDENDUM limits all claims; no actual coefficient supremum accepted.','open':['Directed exact runtime radial coverage','Paired Bernstein/coordinate subinterval containment','Floating geometric exclusion filter','Green anchors, Taylor remainders, Cartesian derivatives, all Frobenius sums','Actual derivative suprema and local coefficient hypothesis','Global inverse and decisive endpoints'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
