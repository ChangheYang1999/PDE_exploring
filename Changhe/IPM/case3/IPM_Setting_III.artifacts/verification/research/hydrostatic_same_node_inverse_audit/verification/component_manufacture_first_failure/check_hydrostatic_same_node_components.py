"""Result304 supplemental tail-order experiment and corrected manufacture."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,ast
import numpy as np
import mpmath as mp
import sympy as sp
import torch
from scipy.special import roots_legendre
import check_hydrostatic_same_node as base
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_power_tail import PowerVerticalInverse
R=Path('research/hydrostatic_same_node_inverse_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
def comps(jet,x,y,npan,nt):
 nodes,weights=roots_legendre(24);u=min(y,1.);ts=list(u*(nodes+1)/2);ww=list(u*weights/2)
 if y>1:
  nodes,weights=roots_legendre(8)
  for l,h in zip(np.linspace(0,np.log(y),npan+1)[:-1],np.linspace(0,np.log(y),npan+1)[1:]):
   tt=np.exp((l+h)/2+(h-l)*nodes/2);ts.extend(tt);ww.extend((h-l)*weights*tt/2)
 ts=np.asarray(ts);ww=np.asarray(ww);J=float(np.dot(ww*ts,jet(x,ts)[...,3]));z,w=roots_legendre(nt);u=(z+1)/2;t=y+(1+y)*(u/(1-u))**3;wt=w/2*3*(1+y)*u*u/(1-u)**4;j=jet(x,t);I=float(np.dot(wt,j[...,3]));Ix=float(np.dot(wt,j[...,1]));return dict(J=J,I=I,Ix=Ix,V=[-Ix,J+y*I])
def main():
 checks=[];out=dict(status='RUNNING',started_utc=utc(),checks=checks,driver_sha256=sha(__file__),proof_sha256=sha(R/'TAIL_COMPONENT_PROOF.md'),base_sha256=sha(V/'CHECKS.json'),base_driver_sha256=sha('independent_code/check_hydrostatic_same_node.py'),manufactures=[],rows=[])
 def save():out['updated_utc']=utc();base.dump(V/'COMPONENTS.json',out)
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e));save()
  if not b:raise AssertionError((n,e))
 save()
 try:
  d=json.loads((V/'CHECKS.json').read_text());ck('base complete',d['status']=='PASS_FINITE_PROBES'and all(t['passed']for t in d['checks']));ck('base driver unchanged',d['driver_sha256']==out['base_driver_sha256']);ck('base sources unchanged',d['input_sha256']==sha(V/'INPUTS.json')and d['proof_sha256']==sha(R/'PROOF.md')and d['review_resolution_sha256']==sha(R/'DESIGN_REVIEW_RESOLUTION.md'))
  for f,h in d['modules'].items():ck('base module unchanged '+f,sha(Path('independent_code')/f)==h)
  X,Y=sp.symbols('X Y',real=True);a=1+X**2+Y**2;ck('exact manufactured antiderivative',sp.simplify(sp.diff(X*a**(-sp.Rational(1,4)),Y)+X*Y*a**(-sp.Rational(5,4))/2)==0)
  inp=json.loads((V/'INPUTS.json').read_text());ck('frozen state',sha(inp['state']['path'])==inp['state']['sha256']);npan=d['node_recipe']['npan']
  for m in d['manufactures'][::2]:
   for nt in [80,640]:
    got=base.diagnostic_rule(base.mj,m['x'],m['y'],npan,False,ntail=nt);c=comps(base.mj,m['x'],m['y'],npan,nt);err=max(abs(a-b)/(1+abs(b))for a,b in zip(got,m['expected']));ck('manufacture component identity '+str((m['x'],m['y'],nt)),max(abs(a-b)for a,b in zip(got,c['V']))<1e-12);out['manufactures'].append(dict(x=m['x'],y=m['y'],ntail=nt,expected=m['expected'],computed=got,scaled_error=err));
    if nt==640:ck('refined diagnostic manufacture '+str((m['x'],m['y'])),err<1e-9,err)
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(inp['state']['path'])
  jet=CartesianQJet(q)
  for b in d['rows']:
   x,y=b['x'],b['y'];p=PowerVerticalInverse(jet.jet,q.p,88,256,512.,.125).at(x,y);I=p['dV2_dy'];J=p['V'][1]-y*I;row=dict(label=b['label'],x=x,y=y,principal=dict(V=p['V'],I=I,J=J),tail_orders=[],mp=[]);out['rows'].append(row);ck(b['label']+' principal reproducibility',p['V']==b['physical'][-1]['V'])
   for nt in [80,160,320,640]:
    c=comps(jet.jet,x,y,npan,nt);v=base.diagnostic_rule(jet.jet,x,y,npan,False,ntail=nt);ck(b['label']+' component identity '+str(nt),max(abs(a-z)for a,z in zip(c['V'],v))<1e-12);c.update(ntail=nt,delta_J=c['J']-J,delta_yI=y*(c['I']-I),delta_V=[a-z for a,z in zip(c['V'],p['V'])],residual=base.record(jet.jet,c['V'],q.cl,x,y));row['tail_orders'].append(c)
    if nt==80:ck(b['label']+' baseline reproduction',max(abs(a-z)for a,z in zip(c['V'],b['diagnostic_rule']['analytic']['V']))<1e-12)
   with mp.workdps(108):
    g,gx,gy,_=map(mp.mpf,b['mp'][-1]['J']);xx,yy,c=map(mp.mpf,[x,y,q.cl]);
    for name,rec in [('physical',b['physical'][-1]),('diagnostic_analytic',b['diagnostic_rule']['analytic']),('diagnostic_fd',b['diagnostic_rule']['fd'])]:
     u,v=map(mp.mpf,rec['V']);rh=(c*xx+u)*gx+(c*yy+v)*gy-g;nf=abs((c*xx+u)*gx)+abs((c*yy+v)*gy)+abs(g);nv=abs(g)+abs(xx*gx+yy*gy)+abs(u*gx+v*gy);row['mp'].append(dict(name=name,R=mp.nstr(rh,90),Nf=mp.nstr(nf,90),Nv=mp.nstr(nv,90),Rf=mp.nstr(abs(rh)/nf,90),Rv=mp.nstr(abs(rh)/nv,90),Rf_change=float(abs(rh)/nf-mp.mpf(rec['Rf'])),Rv_change=float(abs(rh)/nv-mp.mpf(rec['Rv']))));ck(b['label']+' positive MP denominators '+name,nf>0 and nv>0)
   save();print(b['label'],[(z['ntail'],z['delta_V'],z['delta_J'],z['delta_yI'])for z in row['tail_orders']],flush=True)
  out.update(status='PASS_FINITE_COMPONENT_SENSITIVITY',finished_utc=utc(),count=len(checks));save();print('PASS',len(checks),utc(),flush=True)
 except Exception:out.update(status='FAIL',finished_utc=utc(),traceback=traceback.format_exc());save();raise
if __name__=='__main__':main()
