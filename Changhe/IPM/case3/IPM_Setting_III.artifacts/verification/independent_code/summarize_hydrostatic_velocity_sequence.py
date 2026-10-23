"""Result277: compare independent225point inverses with frozen tables."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
import numpy as np
R=Path('research/hydrostatic_velocity_sequence_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[]
def ck(n,v,e=None):checks.append(dict(name=n,passed=bool(v),evidence=e))
g=json.loads((V/'RUN.json').read_text());assert g['status']=='PASS','Wait for complete raw277';ck('rawPASS',all(c['passed']for c in g['checks']));ck('proofhash',g['proof_sha256']==sha(R/'PROOF.md'));ck('driverhash',g['driver_sha256']==sha('independent_code/audit_hydrostatic_velocity_sequence.py'));ck('inputhash',g['input_sha256']==sha(V/'INPUTS.json'))
for f,h in g['code_sha256'].items():ck('module '+f,sha(Path('independent_code')/f)==h)
inp=json.loads((V/'INPUTS.json').read_text())
for f in inp['files']:ck('frozen '+f['path'],sha(f['path'])==f['sha256'])
for item in inp['states']:ck('coefficient '+item['tag'],sha(item['state']['path'])==item['state']['sha256'])
items={s['tag']:s for s in g['states']};arrays={};rules={};rd=None;points=None;quadrature=[]
for tag,s in items.items():
 ck(tag+' DONE',s['status']=='DONE'and len(s['levels'])==3)
 for lev in s['levels']:ck(tag+' count'+str(lev['order']),len(lev['points'])==225)
 ar=[np.array([q['V']for q in lev['points']])for lev in s['levels']];pt=np.array([[q['x'],q['y'],q['r']]for q in s['levels'][-1]['points']]);
 if points is None:points=pt;rd=pt[:,2]
 ck(tag+' commoncoords',np.array_equal(points,pt));arrays[tag]=ar[-1];rules[tag]=ar
 quadrature.append(dict(tag=tag,weighted_max_32_48=float(np.max(abs(ar[0]-ar[1])/(1+rd[:,None])**s['p'])),weighted_max_48_64=float(np.max(abs(ar[1]-ar[2])/(1+rd[:,None])**s['p']))))
def rounding(value,tok):
 m,e=tok.lower().split('e');return abs(value-float(tok))<=.5*10**(int(e)-len(m.split('.')[1]))
summary=[]
for c,suffix in [(2,'c2'),(3,'c3_hsG')]:
 text=(V/f'producer_hs_vel_cauchy_{suffix}.txt').read_text();tags=sorted([t for t,s in items.items()if s['c']==c],key=lambda t:int(re.search(r'_N(\d+)',t)[1]));printed=[]
 for line in text.split('scale of',1)[0].splitlines():
  m=re.match(r'^\d+x\d+\s*->\s*\d+x\d+\s+(.*)$',line)
  if m:printed.append(re.findall(r'[+-]?\d+\.\d+e[+-]\d+',m[1]))
 ck('paircount'+str(c),len(printed)==len(tags)-1)
 for old,new,tokens in zip(tags,tags[1:],printed):
  A,B=arrays[old],arrays[new];D=A-B;normd=np.linalg.norm(D,axis=1);normb=np.linalg.norm(B,axis=1);regions={};ck(old+new+' tokens',len(tokens)==12)
  for k,(reg,lo,hi)in enumerate([('inner',0,.1),('subunit',.1,1),('annulus',1,100),('far',100,10001)]):
   ii=np.flatnonzero((rd>=lo)&(rd<hi));wf=(1+rd)**(1/c);rec=dict(count=len(ii),components=[])
   for j in [0,1]:
    ix=int(ii[np.argmax(abs(D[ii,j])/wf[ii])]);val=float(abs(D[ix,j])/wf[ix]);rec['components'].append(dict(value=val,index=ix,x=float(points[ix,0]),y=float(points[ix,1]),numerator=float(abs(D[ix,j])),denominator=float(wf[ix])));ck(old+new+reg+' component'+str(j),rounding(val,tokens[3*k+j]),dict(own=val,printed=tokens[3*k+j]))
   di=int(ii[np.argmax(normd[ii])]);bi=int(ii[np.argmax(normb[ii])]);ratio=float(normd[di]/normb[bi]);rec['euclidean_regional_ratio']=dict(value=ratio,numerator=float(normd[di]),denominator=float(normb[bi]),difference_index=di,scale_index=bi);rec['component_regional_ratio']=float(np.max(abs(D[ii]))/np.max(abs(B[ii])));rec['weighted_component_scale']=[float(np.max(abs(B[ii,j])/wf[ii]))for j in [0,1]];ck(old+new+reg+' Euclideanratio',rounding(ratio,tokens[3*k+2]),dict(own=ratio,printed=tokens[3*k+2]));regions[reg]=rec
  summary.append(dict(c=c,old=old,new=new,regions=regions))
out=dict(status='PASS'if all(q['passed']for q in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,summary=summary,quadrature=quadrature,proof_sha256=sha(R/'SUMMARY_PROOF.md'),raw_sha256=sha(V/'RUN.json'),driver_sha256=sha(__file__),scope='Finite sampled auxiliaryvelocities;axisrowsneedseparatecheck;no fullplaneendpoint')
(V/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
