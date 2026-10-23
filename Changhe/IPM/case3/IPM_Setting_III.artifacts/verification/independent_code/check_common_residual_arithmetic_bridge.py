"""Supplement to287: exact raw/controlled arithmetic and exceptional MP probe."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,traceback
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from scalar_mp_hydrostatic_density import ScalarMPDensity
torch.set_num_threads(1)
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';utc=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings={};rows=[];probes=[];ratios=[];start=utc()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 v=sha(p)
 if h:ck('hash '+str(p),v==h)
 bindings[str(p)]=v
 return Path(p)
def frac(x):return F.from_float(float(x))
def residual(j,v,x,y,c):return(c*x+v[0])*j[1]+(c*y+v[1])*j[2]-j[0]
def metrics(j,v,x,y,c):
 g,gx,gy=j[:3];a=(c*x+v[0])*gx;b=(c*y+v[1])*gy;z=dict(Rh=a+b-g,Nf=abs(a)+abs(b)+abs(g),Nv=abs(g)+abs(x*gx+y*gy)+abs(v[0]*gx+v[1]*gy),Nbound=mp.sqrt((c*x+v[0])**2+(c*y+v[1])**2)*mp.sqrt(gx*gx+gy*gy)+abs(g))
 for key,den in [('Rf','Nf'),('Rv','Nv'),('Rbound','Nbound')]:z[key]=abs(z['Rh'])/z[den]if z[den]else None
 return z
def save(status,error=None):
 out=dict(status=status,started_utc=start,finished_utc=utc(),count=len(checks),checks=checks,bindings=bindings,exact_bridges=rows,controlled_jet_bridges=ratios,exceptional_probe=probes,traceback=error,scope='Exact identities on represented numbers and empirical MP consistency; no error enclosure or full-plane endpoint.')
 tmp=V/'ARITHMETIC_BRIDGE.json.tmp';tmp.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');tmp.replace(V/'ARITHMETIC_BRIDGE.json')
try:
 for p in [__file__,R/'CONTROLLED_ARITHMETIC_BRIDGE_PROOF.md',R/'SCALAR_ARRAY_JET_CORRECTION_PROOF.md',V/'INPUTS.json',V/'POINTS.npz','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/scalar_mp_hydrostatic_density.py']:bind(p)
 j=[F(5,16),F(1,4),F(5,4),F(1,2)];v=[F(1,8),-F(1,2)];x,y,c=F(1,2),F(1,4),F(2);ck('hand residual',residual(j,v,x,y,c)==-F(1,32));ja=[j[0]+F(1,16),j[1],j[2]+F(1,8),j[3]];va=[v[0]+F(1,4),v[1]-F(1,8)];ck('hand inverse bracket',residual(j,va,x,y,c)-residual(j,v,x,y,c)==-F(3,32));ck('hand jet bracket',residual(ja,va,x,y,c)-residual(j,va,x,y,c)==-F(5,64))
 data={}
 for name in ['RUN','ADAPTIVE','ADAPTIVE_SUMMARY','MP_JETS','MP_SENSITIVITY','FRACTION_ADAPTIVE']:
  p=V/(name+'.json');bind(p);d=json.loads(p.read_text());ck(name+' PASS',d['status']=='PASS'and all(q['passed']for q in d['checks']));data[name]=d
 for name in ['MP_SENSITIVITY','ADAPTIVE_SUMMARY']:
  for p,h in data[name]['source_sha256'].items():bind(p,h)
 points=np.load(V/'POINTS.npz')['points'];fixed={};adaptive={};params={}
 for s in data['RUN']['states']:
  p=s['levels'][-1];bind(p['path'],p['sha256']);fixed[s['tag']]=dict(np.load(p['path']))
 for s in data['ADAPTIVE']['states']:
  tag=s['tag'];params[tag]=s['c'];adaptive[tag]={a['index']:a for a in s['points']};ff=fixed[tag]
  for a in s['points']:
   i=a['index'];jf=list(map(frac,ff['jets'][i]));ja=list(map(frac,a['jet']));vf=list(map(frac,ff['velocity'][i]));va=list(map(frac,a['V']));x,y=map(frac,points[i,:2]);c=frac(s['c']);rf,ra=frac(ff['Rh'][i]),frac(a['Rh']);dd=residual(jf,vf,x,y,c);da=residual(jf,va,x,y,c);aa=residual(ja,va,x,y,c);z=dict(inverse_only=da-dd,local_jet=aa-da,adaptive_saved_arithmetic=ra-aa,fixed_saved_arithmetic=rf-dd,raw_difference=ra-rf);ck(tag+' exact telescoping '+str(i),z['raw_difference']==z['inverse_only']+z['local_jet']+z['adaptive_saved_arithmetic']-z['fixed_saved_arithmetic']);rows.append(dict(tag=tag,index=i,exact={k:str(v)for k,v in z.items()},approximate={k:float(v)for k,v in z.items()}))
 ck('exact295coverage',len(rows)==295)
 with mp.workdps(108):
  for z in data['MP_SENSITIVITY']['rows']:
   tag=z['tag'];i=z['index'];a=adaptive[tag][i];ff=fixed[tag];x,y=map(lambda t:mp.mpf(float(t)),points[i,:2]);c=mp.mpf(float(params[tag]));v=list(map(lambda t:mp.mpf(float(t)),a['V']));jf=list(map(lambda t:mp.mpf(float(t)),ff['jets'][i]));ja=list(map(lambda t:mp.mpf(float(t)),a['jet']));mf=metrics(jf,v,x,y,c);ma=metrics(ja,v,x,y,c);e={};scale=max(mp.mpf('1e-300'),ma['Nf'],mf['Nf'])
   for key in ['Rh','Nf','Nv','Nbound','Rf','Rv','Rbound']:
    old=z['four_records']['doublejet_adaptiveV'][key];ck(tag+' controlled value '+str(i)+key,(old is None and mf[key]is None)or(old is not None and mf[key]is not None and abs(mp.mpf(old)-mf[key])<=mp.mpf('1e-95')*max(scale,abs(mf[key]))))
    if ma[key]is None:ck(tag+' undefined '+str(i)+key,a[key]is None);e[key]=None;continue
    local=ma[key]-mf[key];arithmetic=mp.mpf(float(a[key]))-ma[key];total=mp.mpf(float(a[key]))-mf[key];ck(tag+' MP bridge '+str(i)+key,abs(total-local-arithmetic)<=mp.mpf('1e-95')*max(scale,abs(total)));e[key]={k:mp.nstr(v,100)for k,v in dict(local_jet_change=local,saved_arithmetic_change=arithmetic,saved_minus_controlled=total).items()}
   ratios.append(dict(tag=tag,index=i,metrics=e))
 ck('controlled18coverage',len(ratios)==18)
 tag='hsG_c3.0_N64_log';i=214;item=next(t for t in json.loads((V/'INPUTS.json').read_text())['states']if t['tag']==tag);bind(item['state']['path'],item['state']['sha256']);a=adaptive[tag][i];ck('exceptional coordinate',a['x']==points[i,0]and a['y']==points[i,1]);
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['state']['path'])
 values=[]
 for digits in [72,108]:
  with mp.workdps(digits):
   m=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);jj=m.jet(float(points[i,0]),float(points[i,1]));values.append([mp.nstr(v,digits)for v in jj])
 with mp.workdps(108):
  lo,hi=[list(map(mp.mpf,z))for z in values];relative=[abs(x-y)/(abs(x)+abs(y))if x or y else mp.mpf(0)for x,y in zip(lo,hi)];ck('exceptional MP precision',max(relative)<mp.mpf('1e-55'));r=mp.sqrt(mp.mpf(float(points[i,0]))**2+mp.mpf(float(points[i,1]))**2);p=mp.mpf(1)/3;weights=[(1+r)**p,(1+r)**(p-1),(1+r)**(p-1),(1+r)**(p-2)];differences={}
  for label,jj in [('fixed',fixed[tag]['jets'][i]),('adaptive',a['jet'])]:
   errors=[abs(mp.mpf(float(x))-y)/w for x,y,w in zip(jj,hi,weights)];ck('exceptional weighted '+label,max(errors)<mp.mpf('2e-9'));differences[label]=[mp.nstr(e,35)for e in errors]
  probes.append(dict(tag=tag,index=i,x=a['x'],y=a['y'],precisions=[72,108],jets=values,relative_precision=[mp.nstr(e,35)for e in relative],weighted_differences=differences))
 save('PASS');print('PASS',len(checks),'295 exact bridges,18 controlled bridges,1 exceptional MP probe',utc())
except Exception:
 save('FAIL',traceback.format_exc());raise
