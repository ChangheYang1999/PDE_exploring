"""Result327 independent controlled derivative-integrand experiment.
Own Cartesian jets and physical quadrature only. See standalone PROOF.md.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
 os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sys,json,hashlib,math,argparse
import numpy as np
from independent_hydrostatic import CartesianQJet
from node_export_inverse_stage import quadrature_parts,RULES
from q_local_checkpoint import QLocalCheckpoint
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_evaluator_sensitivity';V=R/'verification';EPS=np.array([0.,1e-4,1e-5,1e-6])
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,d):Path(p).write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def fsum(v):return math.fsum(float(x)for x in np.asarray(v).ravel())
def fd(jet,x,s,eps):
 if not math.isfinite(eps)or eps<0:raise ValueError('eps must be nonnegative finite')
 s=np.asarray(s,float)
 if eps==0:return jet(x,s)[...,3]
 h=eps*(1+np.hypot(x,s))
 if not np.all(h>0):raise ArithmeticError('zero FD step')
 return (jet(x+h,s)[...,1]-jet(x-h,s)[...,1])/(2*h)
def point(jet,x,y,p,rule,epses=EPS):
 xx,yy,(an,aw),(bn,bw),(tn,tw),meta=quadrature_parts(x,y,p,rule)
 nodes=np.concatenate([an,bn,tn]);local=jet(xx,nodes);ia=len(an);ib=ia+len(bn)
 sx=-1 if x<0 else 1;sy=-1 if y<0 else 1
 w2=np.concatenate([aw*an,yy*bw,yy*tw]);wt=np.concatenate([np.zeros_like(an),bw,tw])
 I1=fsum(wt*local[:,1]);v1=-sx*I1 if x else 0.
 velocity=[];tails=[]
 for eps in epses:
  d=local[:,3]if eps==0 else fd(jet,xx,nodes,float(eps))
  tails.append(fsum(wt*d));velocity.append([v1,sy*fsum(w2*d)if y else 0.])
 return np.asarray(velocity),np.asarray(tails),meta

def gaussian(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));e=np.exp(-x*x-y*y)
 return np.stack([y*e,-2*x*y*e,(1-2*y*y)*e,(4*x*x-2)*y*e],axis=-1)
def float_residual(j,v,x,y):
 gx,gy=j[1],j[2];a=(2*x+v[0])*gx;b=(2*y+v[1])*gy
 rr=fsum([a,b,-j[0]]);nf=fsum([abs(a),abs(b),abs(j[0])]);nv=fsum([abs(j[0]),abs(x*gx+y*gy),abs(v[0]*gx+v[1]*gy)])
 return rr,nf,nv,abs(rr)/nf if nf else np.nan,abs(rr)/nv if nv else np.nan

def manufacture():
 import mpmath as mp
 mp.mp.dps=80;checks=[];records=[];started=utc()
 def check(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
 def Q(z):return Fraction(float(z))
 for x,s in [(0.,0.),(0.,.7),(.7,.3),(-.7,.3),(.7,-.3),(5.,9.)]:
  for eps in [1e-4,1e-5,1e-6,.1,.3]:
   h=float(eps*(1+np.hypot(x,s)));xx,ss,hh=map(Q,[x,s,h])
   for degree in [2,4]:
    numerator=degree*((xx+hh)**(degree-1)-(xx-hh)**(degree-1))*ss
    expected=2*ss if degree==2 else 12*xx*xx*ss+4*hh*hh*ss
    check('exact polynomial '+str((x,s,eps,degree)),numerator/(2*hh)==expected)
    def jet(a,b):
     a,b=np.broadcast_arrays(np.asarray(a,float),np.asarray(b,float));z=np.zeros_like(a)
     return np.stack([b*a**degree,degree*b*a**(degree-1),a**degree,degree*(degree-1)*b*a**(degree-2)],axis=-1)
    value=float(fd(jet,x,np.array(s),eps));want=float(expected)
    scale=(abs(float(jet(x+h,s)[1]))+abs(float(jet(x-h,s)[1])))/(2*h)
    tol=128*np.finfo(float).eps*(1+abs(want)+scale)
    check('float polynomial '+str((x,s,eps,degree)),abs(value-want)<=tol,dict(value=value,expected=want,tolerance=tol))
 for label,rule in RULES.items():
  for eps in [0.,.1,.3]:
   vel,tails,_=point(gaussian,0.,0.,.5,rule,[eps]);ee=mp.mpf(float(eps));a=1+ee**2;b=2*ee**2
   J=mp.sqrt(mp.pi)/(2*mp.sqrt(a))*mp.exp(b*b/(4*a))*mp.erfc(b/(2*mp.sqrt(a)))
   exact=-mp.exp(-ee**2)/a+b/a*mp.exp(-ee**2)*J
   value=float(tails[0]);error=abs(value-float(exact));check('Gaussian center '+str((label,eps)),error<=5e-13,dict(value=value,exact=str(exact),error=error))
   records.append(dict(kind='Gaussian center',rule=label,eps=eps,value=value,reference=str(exact)))
 # Off-axis high-precision integral uses tanh-sinh and analytic first derivatives.
 for x,y in [(.7,.3),(1.3,.9)]:
  for eps in [0.,.1,.3]:
   xx,yy,ee=map(mp.mpf,[x,y,eps])
   def d(s):
    if not ee:return (4*xx*xx-2)*s*mp.exp(-xx*xx-s*s)
    hh=ee*(1+mp.sqrt(xx*xx+s*s))
    gx=lambda z:-2*z*s*mp.exp(-z*z-s*s)
    return (gx(xx+hh)-gx(xx-hh))/(2*hh)
   inner=mp.quad(lambda s:s*d(s),[0,yy]);tail=mp.quad(d,[yy,1,4,mp.inf]);reference=inner+yy*tail;reference1=xx*mp.exp(-xx*xx-yy*yy)
   for label,rule in RULES.items():
    vv,tt,_=point(gaussian,x,y,.5,rule,[eps]);err=max(abs(vv[0,0]-float(reference1)),abs(vv[0,1]-float(reference)),abs(tt[0]-float(tail)))
    check('Gaussian off-axis '+str((x,y,eps,label)),err<=8e-13,dict(error=err,V=vv[0].tolist(),reference=[str(reference1),str(reference)],tail=float(tt[0]),tail_reference=str(tail)))
    records.append(dict(kind='Gaussian off-axis',rule=label,eps=eps,xy=[x,y],max_error=err))
 for sx,sy in [(-1,1),(1,-1),(-1,-1)]:
  a,t,_=point(gaussian,.7,.3,.5,RULES['B']);b,u,_=point(gaussian,sx*.7,sy*.3,.5,RULES['B'])
  check('Gaussian parity '+str((sx,sy)),np.array_equal(b,a*np.array([sx,sy]))and np.array_equal(t,u))
 check('strict products do not skip zero',sum(a*b<0 for a,b in zip([1,0,-1,1],[0,-1,1,0]))==1)
 check('Rv can attain2',Fraction(2,1)/Fraction(1,1)==2)
 check('both-zero Nf undefined',float_residual([0,0,0,0],[0,0],0,0)[1]==0)
 for eps in [-1.,float('nan'),float('inf')]:
  try:fd(gaussian,1.,np.array([.3]),eps);bad=True
  except ValueError:bad=False
  check('invalid eps rejected '+str(eps),not bad)
 for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:check('single thread '+key,os.environ[key]=='1')
 out=dict(status='PASS_MANUFACTURES'if all(c['passed']for c in checks)else'FAIL_MANUFACTURES',started_utc=started,finished_utc=utc(),source_sha256=sha(__file__),proof_sha256=sha(R/'PROOF.md'),count=len(checks),checks=checks,records=records)
 path=V/('MANUFACTURES_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'.json');dump(path,out);dump(V/'MANUFACTURES_LATEST.json',dict(path=str(path),sha256=sha(path),status=out['status']))
 print(json.dumps({k:out[k]for k in ['status','started_utc','finished_utc','count']},indent=2),flush=True)
 if out['status']!='PASS_MANUFACTURES':raise RuntimeError('manufacture failure')


def candidate():
 started=utc();latest=json.loads((V/'MANUFACTURES_LATEST.json').read_text());m=json.loads(Path(latest['path']).read_text())
 if latest['sha256']!=sha(latest['path'])or m['status']!='PASS_MANUFACTURES'or m['source_sha256']!=sha(__file__)or m['proof_sha256']!=sha(R/'PROOF.md'):raise RuntimeError('manufacture/source gate')
 outdir=V/'candidate';outdir.mkdir(exist_ok=False)
 inputs=json.loads((V/'INPUTS.json').read_text());bindings={}
 for row in inputs['files']:
  p=row.get('snapshot',row.get('reused_path'))
  if sha(p)!=row['sha256']:raise RuntimeError('input changed '+p)
  bindings[p]=row['sha256']
 for p in [Path(__file__),R/'PROOF.md',ROOT/'independent_code/node_export_inverse_stage.py',ROOT/'independent_code/independent_hydrostatic.py',ROOT/'independent_code/q_local_checkpoint.py',ROOT/'independent_code/q_checkpoint_reader.py',V/'INPUTS.json',Path(latest['path'])]:bindings[str(p.resolve())]=sha(p)
 prior=ROOT/'research/accurate_map_final_audit/verification';
 import torch
 torch.set_num_threads(1)
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
  q=QLocalCheckpoint(prior/'hsQ_c2.0_N128_acc.pt')
 jet=CartesianQJet(q).jet
 if not(q.N==128 and q.M==32 and q.cl==2 and q.p==.5):raise RuntimeError('unexpected state')
 theta=np.linspace(0,np.pi/2,8*q.M+1)[1:-1];np.savez_compressed(outdir/'GRID.npz',theta=theta,eps=EPS)
 allrecords=[]
 for radius in [3.,30.]:
  x=radius*np.cos(theta);y=radius*np.sin(theta);prodpath=V/('hsQ_c2.0_N128_acc_scan_r'+str(int(radius))+'.npz')
  with np.load(prodpath,allow_pickle=False)as prod:
   if not(np.array_equal(theta,prod['theta'])and np.array_equal(x,prod['x'])and np.array_equal(y,prod['y'])):raise RuntimeError('coordinates differ')
  j=jet(x,y);vs=[];ts=[];metas=[];rs=[]
  for i,(xx,yy)in enumerate(zip(x,y)):
   velocity,tails,meta=point(jet,xx,yy,q.p,RULES['B']);vs.append(velocity);ts.append(tails);metas.append(meta);rs.append([float_residual(j[i],vv,xx,yy)for vv in velocity])
   if (i+1)%16==0 or i+1==len(x):
    print(json.dumps(dict(utc=utc(),stage='B',radius=radius,completed=i+1,total=len(x))),flush=True)
  vs=np.asarray(vs);ts=np.asarray(ts);rs=np.asarray(rs)
  np.savez_compressed(outdir/('R'+str(int(radius))+'_B.npz'),x=x,y=y,theta=theta,eps=EPS,jet=j,velocity=vs,tail=ts,meta=np.asarray(metas),residual=rs)
  reasons={}
  def add(i,why):reasons.setdefault(int(i),[]).append(why)
  for i in [0,len(x)//2,len(x)-1]:add(i,'predeclared endpoint/midpoint')
  for k,e in enumerate(EPS):
   add(np.nanargmax(rs[:,k,3]),'max Rf eps='+str(e))
   if k:
    z=(vs[:,k,1]-vs[:,0,1])*j[:,2]/rs[:,0,1];add(np.argmax(abs(z)),'max fixed-denominator velocity change eps='+str(e))
    d=ts[:,k]-ts[:,0];add(np.argmax(abs(d)),'max finite divergence proxy eps='+str(e))
    flips=np.flatnonzero(rs[:,k,0]*rs[:,0,0]<0)
    for i in flips[:3]:add(i,'first pointwise opposite residual sign eps='+str(e))
  ids=np.array(sorted(reasons));dump(outdir/('R'+str(int(radius))+'_SELECTION.json'),dict(indices=ids.tolist(),reasons={str(i):reasons[i]for i in ids}))
  for label in ['A','C']:
   vv=[];tt=[];mm=[];rr=[]
   for i in ids:
    value,tail,meta=point(jet,x[i],y[i],q.p,RULES[label]);vv.append(value);tt.append(tail);mm.append(meta);rr.append([float_residual(j[i],z,x[i],y[i])for z in value])
   np.savez_compressed(outdir/('R'+str(int(radius))+'_'+label+'.npz'),indices=ids,velocity=vv,tail=tt,meta=mm,residual=rr)
   print(json.dumps(dict(utc=utc(),stage=label,radius=radius,selected=len(ids))),flush=True)
  allrecords.append(dict(radius=radius,points=len(x),selected=len(ids)))
 for p,h in bindings.items():
  if sha(p)!=h:raise RuntimeError('source changed during run '+p)
 outputs={str(p.resolve()):sha(p)for p in sorted(outdir.iterdir())if p.is_file()}
 complete=dict(status='COMPLETE_FINITE_CANDIDATE_DIAGNOSTIC_REQUIRES_CHECK',started_utc=started,finished_utc=utc(),bindings=bindings,outputs=outputs,records=allrecords,eps=EPS.tolist(),scope='Auxiliary finite perturbed evaluator; eps>0 is generally not divergence free; no error bound or causal authentication.')
 dump(outdir/'COMPLETE.json',complete);print(json.dumps({k:complete[k]for k in ['status','started_utc','finished_utc','records']},indent=2),flush=True)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['manufacture','candidate']);args=parser.parse_args()
 (manufacture if args.mode=='manufacture'else candidate)()
