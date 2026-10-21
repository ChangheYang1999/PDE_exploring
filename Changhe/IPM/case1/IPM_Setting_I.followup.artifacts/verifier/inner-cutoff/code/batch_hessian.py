"""Resumable candidate rectangle Hessian enclosures; run only when a heavy slot is free."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,gc
from flint import ctx
from hessian import EnclosedDensity
ROOT=Path(__file__).resolve().parents[1];ctx.prec=192
ps=json.loads((ROOT.parent/'sampled-physical-actions/verification/points.json').read_text())['points']
ps+=json.loads((ROOT.parent/'fixed-cl-correction/verification/withheld_points.json').read_text())['points']
# Include the independently located L4 source observations.
ld=json.loads((ROOT.parent/'domain-states/verification/dnB_n96m40SL4_physical.json').read_text())
# Main finite samples are mandatory; schema-independent extraction below adds point pairs only.
def pairs(o):
 if isinstance(o,dict):
  for k,v in o.items():
   if k=='point' and isinstance(v,list) and len(v)==2 and all(isinstance(z,(int,float)) for z in v):yield v
   else:yield from pairs(v)
 elif isinstance(o,list):
  for v in o:yield from pairs(v)
ps+=list(pairs(ld));points=[]
for p in ps:
 if min(p)>1e-7 and p not in points:points.append(p)
files=['grid-states/data/dnB_n96m40S.npz','ritz-resolution/data/dnSB_n120m48.npz','domain-states/data/dnB_n96m40SL4.npz','fixed-cl-correction/data/n96m40S_radius0.05.npz','fixed-cl-correction/data/n120m48_S_radius0.05.npz']
path=ROOT/'verification/hessian_bounds.json';p_hash=hashlib.sha256(json.dumps(points).encode()).hexdigest()
if path.exists():out=json.loads(path.read_text());assert out['points_sha256']==p_hash and out['precision_bits']==ctx.prec
else:out={'start':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'points_sha256':p_hash,'points':points,'states':[],'scope':'Rigorous rectangle Hessian and missing local-PV disk bounds for exact binary ideal-node fields. Does not enclose annular inverse quadrature or full residual.'}
def save():
 t=path.with_suffix('.temporary');t.write_text(json.dumps(out,indent=2)+'\n');t.replace(path)
for rel in files:
 file=ROOT.parent/rel;md5=hashlib.md5(file.read_bytes()).hexdigest();st=next((s for s in out['states'] if s['source']==rel),None)
 if st is None:st={'source':rel,'md5':md5,'rows':[]};out['states'].append(st);save()
 assert st['md5']==md5
 if len(st['rows'])==len(points):continue
 print('BUILD',rel,datetime.now(timezone.utc).isoformat(),flush=True);t=time.monotonic();d=EnclosedDensity(file);st['exact_json']=d.input_json;st['exact_json_sha256']=d.input_json_sha256;st['source_sha256']=d.source_sha256;save();print('READY',rel,'seconds',time.monotonic()-t,flush=True)
 for i,pt in enumerate(points):
  if i<len(st['rows']):assert st['rows'][i]['point']==pt;continue
  r,_=d.hessian(pt);st['rows'].append(r);save();print(rel,i+1,'/',len(points),'Uhole',r['local_hole_U_bound_float'],'seconds',time.monotonic()-t,flush=True)
 st['end']=datetime.now(timezone.utc).isoformat();save();del d;gc.collect()
out['dependencies']=[{'file':str(p.relative_to(ROOT.parent.parent)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [Path(__file__),ROOT/'code/hessian.py',ROOT/'PROOF.md',ROOT.parent/'exact-data/code/nodal_input.py']];out['complete']=True;out['end']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',out['end'],flush=True)
