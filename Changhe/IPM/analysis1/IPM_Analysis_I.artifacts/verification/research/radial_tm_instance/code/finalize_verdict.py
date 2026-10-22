"""Freeze finite local ODE checks and their exact same-runtime linkage."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/radial_tm_instance';E=D/'evidence';R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def resolve(p):return Path(p) if Path(p).is_absolute() else B/p
c=json.loads((E/'selected_v3_checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());l=json.loads((E/'linkage_checks.json').read_text());pf=json.loads((E/'proof_first.json').read_text())
assert sha(D/'PROOF.md')==pf['proof_sha256']
assert c['status']=='PASS_LOCAL_RADIAL_ODE_BOXES' and c['cells']==[0,4102,7808] and c['modes']==list(range(1,262)) and not c['failures']
assert a['status']=='PASS_FULL_OUTPUT_AND_FRESH_PARTICULAR_AUDIT' and l['status']=='PASS_EXACT_SAVED_T_TO_F_IMAGES' and l['checks']==6264
files={};dep_pins=0
for v in [c,a,l]:
 for rel,h in v['files'].items():
  p=resolve(rel);assert sha(p)==h,rel
  files[str(p) if not p.is_relative_to(B) else str(p.relative_to(B))]=h;dep_pins+=1
book=0
for ci in c['cells']:
 p=E/('selected_v3_cell_%04d.npz'%ci);assert c['files'][str(p)]==l['files'][str(p.relative_to(B))]==sha(p);book+=1
 with np.load(p) as z:
  for k in ('T_mid','T_rad','F_mid','F_rad'):assert z[k].dtype==np.dtype('float64');book+=1
# Inherited finite scalar/algebra verdicts: verify every pinned dependency.
for rel in ('research/flow_certificate/evidence/modal_verdict.json','research/flow_scalars/evidence/verdict.json'):
 p=B/rel;v=json.loads(p.read_text());files[rel]=sha(p)
 for f,h in v['files'].items():assert sha(resolve(f))==h,f;dep_pins+=1
reviews={}
for kind in ['proof','closure','linkage']:
 tag='radial_tm_instance_'+kind;m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(z['text'] for z in raw['content'] if z['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if kind in ('closure','linkage'):assert '**ACCEPT, narrowly.**' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for ext in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+ext);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SELECTED_FINITE_INPUT_ODE_ENCLOSURES','cells':c['cells'],'modes':261,'counts':c['counts']|a['counts']|{'exact_T_to_F_comparisons':l['checks'],'dtype_and_same_runtime_checks':book,'dependency_pins_checked':dep_pins},'reviews':reviews,'scope':'Mandatory proof/addenda/linkage/closure notes. Local ODE enclosures for3cells all261 modes; exact saved T-box image in saved F box. Current-runtime reconstruction only, same unchanged candidate radii.','open':['Canonical T and A/B membership beyond separately audited selected entries','The other7806 cells','All angular, range, classification and full-field inequalities','Global IPM inverse and every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'pins':len(files),'sha256':sha(E/'verdict.json'),'counts':v['counts']}))
