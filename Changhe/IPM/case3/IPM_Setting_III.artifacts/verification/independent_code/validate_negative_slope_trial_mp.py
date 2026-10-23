import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,math,time
import numpy as np
import mpmath as mp
R=Path('research/negative_slope_independent_trials');D=R/'verification/trials/cl2_M4_J4_L3_a0m4';V=D/'mp_validation';V.mkdir(exist_ok=True);mp.mp.dps=60
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();d=json.loads((D/'RESULT.json').read_text());data=np.load(D/'VALIDATION.npz');rows=d['dictionary'];co=[mp.mpf(float.fromhex(z))for z in d['coefficients_hex']];beta=[mp.mpf(Fraction(row['beta']).numerator)/Fraction(row['beta']).denominator for row in rows];cl=mp.mpf(Fraction(d['c_l']).numerator)/Fraction(d['c_l']).denominator
started=datetime.now(timezone.utc).isoformat();clock0=time.monotonic();checks=[];results=[]
def ck(name,got,want,tol=1e-6):
 err=abs(got-want)/(1+abs(want));checks.append(dict(name=name,passed=bool(err<tol),relative_error=str(err),tolerance=tol))
def rho(x,y):
 return mp.fsum(a*mp.im((x+1j*y)**row['n'])*(1+x*x+y*y)**(-bb) for a,row,bb in zip(co,rows,beta))
streams=sorted({row['n']+1 for row in rows}|{row['n']-1 for row in rows if row['n']>=3})
source_terms={k:[]for k in streams}
for a,row,bb in zip(co,rows,beta):
 n=row['n'];source_terms[n+1].append((a,n,bb,True))
 if n>=3:source_terms[n-1].append((a,n,bb,False))
def source(k,r):
 if r==0:return mp.mpf(0)
 one=1+r*r
 return mp.fsum(a*((-bb*r**(n+1)*one**(-bb-1))if upper else(n*r**(n-1)*one**(-bb)-bb*r**(n+1)*one**(-bb-1)))for a,n,bb,upper in source_terms[k])
def green(r):
 values=[]
 for k in streams:
  innercuts=[mp.mpf(0)]+[mp.mpf(10)**j for j in range(-3,9)if mp.mpf(10)**j<r]+[r]
  outercuts=[r]+([mp.mpf(1),mp.mpf(10)]if r<1 else[10*r])+[mp.inf]
  I=mp.quad(lambda s:s**(k+1)*source(k,s),innercuts)
  J=mp.quad(lambda s:s**(1-k)*source(k,s),outercuts)
  values.append((k,(r**(-k)*I+r**k*J)/(2*k),(-r**(-k-1)*I+r**(k-1)*J)/2))
 return values
indices=sorted({d['regions'][name]['maxima'][key]['point_index']for name,key in [('all','absolute'),('all','Rf'),('all','Rv'),('tiny','Rf'),('inner','absolute'),('core','absolute')]})
ax=np.flatnonzero(np.isclose(data['theta'],np.pi/2,rtol=0,atol=1e-15)&(data['rho']>0))
if len(ax):indices=sorted(set(indices+[int(ax[0]),int(ax[-1])]))
for index in indices+[-1]:
 x=mp.mpf(float(data['x'][index]))if index>=0 else mp.mpf('1e-9');y=mp.mpf(float(data['y'][index]))if index>=0 else mp.mpf('1e-9');r=mp.sqrt(x*x+y*y);theta=mp.atan2(y,x)
 value=rho(x,y);dx=mp.diff(lambda xx:rho(xx,y),x);dy=mp.diff(lambda yy:rho(x,yy),y);g=green(r)
 ur=mp.fsum(-k*gg*mp.cos(k*theta)/r for k,gg,gp in g);ut=mp.fsum(gp*mp.sin(k*theta)for k,gg,gp in g);ux=ur*x/r-ut*y/r;uy=ur*y/r+ut*x/r
 psi=mp.fsum(gg*mp.sin(k*theta)for k,gg,gp in g);res=(cl*x+ux)*dx+(cl*y+uy)*dy-value;nf=abs((cl*x+ux)*dx)+abs((cl*y+uy)*dy)+abs(value);nv=abs(value)+abs(x*dx+y*dy)+abs(ux*dx+uy*dy)
 qsum=mp.fsum(source(k,r)*mp.sin(k*theta)for k in streams);ck(f'point{index} Cartesian source',qsum,dx,1e-35)
 got=dict(rho=value,dx=dx,dy=dy,ux=ux,uy=uy,R=res,Nf=nf,Nv=nv)
 if index>=0:
  for key,v in got.items():ck(f'point{index} {key}',v,mp.mpf(float(data[key][index])))
  ck(f'point{index} Rf',abs(res)/nf,mp.mpf(float(abs(data['R'][index])/data['Nf'][index])))
  ck(f'point{index} Rv',abs(res)/nv,mp.mpf(float(abs(data['R'][index])/data['Nv'][index])))
 else:ck('direct stream center strain',psi/(x*y),mp.mpf(d['strain']),1e-8)
 out=dict(index=index,x=str(x),y=str(y),values={k:str(v)for k,v in got.items()},Rf=str(abs(res)/nf),Rv=str(abs(res)/nv),center_ratio=str(psi/(x*y))if index<0 else None,elapsed_seconds=time.monotonic()-clock0)
 results.append(out);(V/'PROGRESS.json').write_text(json.dumps(dict(started_utc=started,last=out,points_done=len(results)),indent=2)+'\n');print(json.dumps(dict(index=index,Rf=out['Rf'],Rv=out['Rv'],elapsed=out['elapsed_seconds'])),flush=True)
slope=mp.fsum(a for a,row in zip(co,rows)if row['n']==1);p=Fraction(d['p']);K=mp.fsum(a*(-1)**((row['n']-1)//2)for a,row in zip(co,rows)if Fraction(row['beta'])==(row['n']-p)/2)
ck('exact coefficient slope',slope,mp.mpf(d['a0']));ck('exact coefficient K',K,mp.mpf(-1),1e-8)
out=dict(status='PASS'if all(z['passed']for z in checks)else'FAIL',started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-clock0,count=len(checks),checks=checks,points=results,exact_slope=str(slope),exact_K=str(K),trial_sha256=sha(D/'RESULT.json'),validation_data_sha256=sha(D/'VALIDATION.npz'),proof_sha256=sha(R/'VALIDATION_PROOF.md'),driver_sha256=sha(Path(__file__)),interpretation='Method agreement check on a failed finite trial, not low PDE residual.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],flush=True)
if out['status']!='PASS':raise SystemExit(1)
