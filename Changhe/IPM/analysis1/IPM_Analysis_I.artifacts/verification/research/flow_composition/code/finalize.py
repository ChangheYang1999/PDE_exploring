"""Authenticate finite composition outputs and all three actual model reviews."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_composition';R=B/'notes/reviews'
def sha(p):
 with Path(p).open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def require(x,s):
 if not x:raise ValueError(s)
a=load(D/'evidence/audit_outputs.json');p=load(D/'evidence/preparation.json');f=load(D/'evidence/final_checks.json')
require(a['status']=='PASS_FINITE_COMPOSITION_RECORD_AUDIT' and a['rectangles']==9 and a['reference_range_checks']==72 and a['modal_products_per_engine']==274833,'audit status/counts')
require(a['code_sha256']==sha(D/'code/audit_outputs.py') and p['code_sha256']==sha(D/'code/prepare.py'),'core code')
require(f['status']=='PASS_SUPPLEMENTAL_EXACT_WIDTH_LABEL_AND_MARGIN_CHECKS' and len(f['width_checks'])==9 and len(f['source_semantic_statements'])==14,'supplement')
require(F(a['smallest_exact_inclusion_margin'])==F(f['minimum_margin_location']['margin_exact'])>0,'minimum exact')
pins=dict(p['dependency_pins']);require(len(pins)==189,'dependency count')
for name,h in f['files'].items():
 require(name not in pins or pins[name]==h,'collision');pins[name]=h
for q in a['records']:pins[q['file']]=q['sha256']
for q in p['packets']:
 for n,h in [(q['file'],q['sha256']),(q['radial_input_file'],q['radial_input_sha256'])]:
  require(n not in pins or pins[n]==h,'packet collision');pins[n]=h
for n,h in pins.items():require(sha(B/n)==h,'data hash '+n)
reviews={}
for tag,expected in [('flow_composition_proof','4fd6497cd013d23054b0a7b139e4c75fa78978d6b24954f953fcdd5b1f113f41'),('flow_composition_complete','37ceefa950e69ec1d7d4d89546517632e9e7cb4068d6c92b762ce430aa1daccc'),('flow_composition_final_details','cad3799a88d8782e3fc12d9510cfa2c331d38e3bc69c2890486fba7133328e3d')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 require(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual model/stop')
 require(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']==expected,'request digest')
 require(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+s+'\n'+(B/s).read_text() for s in m['files']),'current review bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';require(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='flow_composition_final_details':require('archival' in text and 'justified' in text and 'CONFIRMED_FINITE_SELECTED_FLOW_COMPOSITION' in text and 'remain OPEN' in text,'accepted scope')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  q=R/(tag+suffix);pins[str(q.relative_to(B))]=sha(q)
for root in [D,D/'code',D/'evidence']:
 for q in root.iterdir():
  if not q.is_file() or q.is_symlink() or q.name=='verdict.json':continue
  n=str(q.relative_to(B));h=sha(q);require(n not in pins or pins[n]==h,'final collision');pins[n]=h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_SELECTED_FLOW_COMPOSITION','radial_cells':p['radial_cells'],'angular_nodes':p['nodes'],'rectangles':9,'source_ranges':36,'reference_range_checks':72,'modal_products_per_engine':274833,'minimum_margin_location':f['minimum_margin_location'],'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory FINAL_ADJUDICATION. Finite contemporary output composition conditional on73/93/75. Canonical physical radial membership/full coverage/global flow/inverse/nonlinear/neighborhood/endpoints remain OPEN.'}
p=D/'evidence/verdict.json';require(not p.exists(),'no overwrite');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
