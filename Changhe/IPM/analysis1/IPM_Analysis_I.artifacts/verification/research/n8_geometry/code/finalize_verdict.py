"""Freeze exact exported-mask geometry, retaining historical provenance limits."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_geometry';E=D/'evidence';R=B/'notes/reviews'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text())
assert c['status']=='PASS_ALL_N8_COORDINATE_GEOMETRY_ONLY' and a['status']=='PASS_EXACT_GEOMETRY_OUTPUT_AUDIT'
assert a['counts']=={'omitted_pairs_recounted':584546,'unique_boxes_recounted':203682,'subnode_endpoint_checks':2556,'strict_saved_inequalities':25}
for doc in [c,a]:
 for p,h in doc['files'].items():assert sha(B/p)==h,p
reviews={};files={}
for tag in ['n8_geometry_proof','n8_geometry_closure','n8_geometry_scope']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='n8_geometry_scope':assert 'ACCEPT, limited to coordinate-coverage geometry for the newly exported masks' in ans and 'Historical mask identity is **OPEN**' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXPORTED_MASK_COORDINATE_GEOMETRY_ONLY','confirmed':['Exported coordinate hulls cover theta>=0 half-discs, all four full-run deltas, fine delta=.0165.','All omitted exported boxes are strictly disjoint for all centers in the imported bracket.','Fine larger-delta rows have proved missing-point witnesses and are incomplete whole-disc coverage certificates.'],'counts':a['counts'],'reviews':reviews,'scope':'PUBLICATION.md gives the completed result and incorporates all final reviewer wording corrections. Historical proof-first and review files are preserved unchanged.','dependencies':['Exact radial partition tied to trial by topics31/69','Center lies in imported exact bracket','Reflection extension is a separate source and stream parity premise'],'open':['Historical mask elementwise identity','MR.from_arb outwardness for coefficient and coordinate factors','Bernstein/coordinate domain pairing','Green anchors and all Taylor remainders','All actual derivative and Frobenius bounds, C_V','Global inverse and decisive endpoints'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
