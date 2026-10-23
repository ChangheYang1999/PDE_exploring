"""Selected rounded-coordinate MP operands for result333; no integral enclosure."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import sys,json,hashlib,math,resource,traceback,time
import numpy as np
import mpmath as mp
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
sys.path.insert(0,str(ROOT/'independent_code'))
from angular_evaluator_sensitivity import point
from node_export_inverse_stage import quadrature_parts,RULES
from independent_hydrostatic import CartesianQJet
from q_local_checkpoint import QLocalCheckpoint
from scalar_mp_hydrostatic_density import ScalarMPDensity
from node_export_mp_chunks import MPChunkStore,decimal_value,encode_values
R=ROOT/'research/angular_integrand_precision';V=R/'verification';V.mkdir(exist_ok=True)
OLD=ROOT/'research/angular_evaluator_sensitivity/verification';EPS=np.array([0.,1e-5,1e-6]);NAMES=['angular_evaluator_sensitivity','node_export_inverse_stage','independent_hydrostatic','q_local_checkpoint','q_checkpoint_reader','scalar_mp_hydrostatic_density','node_export_mp_chunks']
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 t=Path(p).with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
def load(p):
 with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
def origins():
 out={n:str(Path(sys.modules[n].__file__).resolve())for n in NAMES}
 if any(p!=str(ROOT/'independent_code'/(n+'.py'))for n,p in out.items()):raise RuntimeError('module origin mismatch')
 return out
def source_bindings():return {str(Path(p).resolve()):sha(p)for p in [__file__,R/'PROOF.md',*[ROOT/'independent_code'/(n+'.py')for n in NAMES]]}
def geometry(jet,x,y,p):
 xx,yy,(an,aw),(bn,bw),(tn,tw),meta=quadrature_parts(x,y,p,RULES['B'])
 if not(x>0 and y>0 and xx==x and yy==y):raise ValueError('positive targets required')
 node=np.concatenate([an,bn,tn]);w2=np.concatenate([aw*an,yy*bw,yy*tw]);wt=np.concatenate([np.zeros_like(an),bw,tw]);local=jet(xx,node)
 h=np.stack([e*(1+np.hypot(xx,node))for e in EPS[1:]],axis=1);xp=xx+h;xm=xx-h
 deriv=np.column_stack([local[:,1],local[:,3],*[(jet(xp[:,k],node)[:,1]-jet(xm[:,k],node)[:,1])/(2*h[:,k])for k in range(2)]])
 fsum=lambda a:math.fsum(float(t)for t in a)
 v1=-fsum(wt*deriv[:,0]);vel=np.array([[v1,fsum(w2*deriv[:,k])]for k in [1,2,3]]);tails=np.array([fsum(wt*deriv[:,k])for k in [1,2,3]])
 return dict(x=np.array(xx),y=np.array(yy),eps=EPS,node=node,w2=w2,wt=wt,h=h,xplus=xp,xminus=xm,double_integrands=deriv,reference_velocity=vel,reference_tail=tails,metadata=meta,local_jet=np.asarray(jet(xx,yy)))
def mp_row(density,x,s,xp,xm,h):
 xx,ss=mp.mpf(float(x)),mp.mpf(float(s))
 f=lambda a:mp.diff(lambda z:density(z,ss),a,addprec=40)
 return [f(xx),mp.diff(lambda z:density(z,ss),xx,2,addprec=40),*[(f(mp.mpf(float(xp[k])))-f(mp.mpf(float(xm[k]))))/(2*mp.mpf(float(h[k])))for k in range(2)]]
def manufacture():
 checks=[];t0=now();paths=origins()
 def ck(n,b):
  checks.append(dict(name=n,passed=bool(b)))
  if not b:raise AssertionError(n)
 # Independent exact algebra for finite inverse and local/inverse decomposition.
 for g,gx,gy,x,y,v1,v2,dg,dx,dy,dv1,dv2 in [(1,2,3,4,5,6,7,8,9,10,11,12),(0,0,0,1,-1,2,3,4,0,-2,0,5),(3,-2,0,0,1,-4,0,1,4,5,-3,2)]:
  a=list(map(Q,[g,gx,gy]));b=[a[0]+dg,a[1]+dx,a[2]+dy];u=list(map(Q,[v1,v2]));v=[u[0]+dv1,u[1]+dv2]
  f=lambda j,w:(2*x+w[0])*j[1]+(2*y+w[1])*j[2]-j[0]
  ck('exact cross decomposition '+str((g,gx,gy)),f(b,v)-f(a,u)==f(b,u)-f(a,u)+f(a,v)-f(a,u)+dv1*dx+dv2*dy)
 for weights,double,high,stored in [([Q(1,3),Q(2,5)],[Q(-2),Q(7)],[Q(1,7),Q(-8,3)],Q(1,9)),([Q(0),Q(1)],[Q(1),Q(-1)],[Q(9),Q(2)],Q(-1))]:
  D=sum(w*a for w,a in zip(weights,double));M=sum(w*a for w,a in zip(weights,high));ck('exact component decomposition '+str(weights),M-stored==M-D+D-stored)
 with mp.workdps(72):
  for x,s in [(.7,.3),(.0184,2.99994),(0.,.7),(5.,9.)]:
   h=np.array([e*(1+np.hypot(x,s))for e in EPS[1:]]);xp=x+h;xm=x-h
   f=lambda a,b:b*mp.exp(-a*a-b*b)
   got=mp_row(f,x,s,xp,xm,h);xx,ss=mp.mpf(x),mp.mpf(s)
   gf=lambda a:-2*a*ss*mp.exp(-a*a-ss*ss)
   want=[gf(xx),(4*xx*xx-2)*ss*mp.exp(-xx*xx-ss*ss),*[(gf(mp.mpf(float(xp[k])))-gf(mp.mpf(float(xm[k]))))/(2*mp.mpf(float(h[k])))for k in range(2)]]
   for k,(a,b)in enumerate(zip(got,want)):ck('Gaussian rounded samples '+str((x,s,k)),abs(a-b)<mp.mpf('1e-60')*max(1,abs(b)))
  for degree in [2,4,7]:
   x,s=.7,.3;h=np.array([e*(1+np.hypot(x,s))for e in EPS[1:]]);xp=x+h;xm=x-h
   got=mp_row(lambda a,b:b*a**degree,x,s,xp,xm,h);xx,ss=Q(x),Q(s)
   exact=[degree*ss*xx**(degree-1),degree*(degree-1)*ss*xx**(degree-2),*[(degree*ss*(Q(float(xp[k]))**(degree-1)-Q(float(xm[k]))**(degree-1)))/(2*Q(float(h[k])))for k in range(2)]]
   for k,(a,b)in enumerate(zip(got,exact)):ck('polynomial exact frozen samples '+str((degree,k)),abs(a-mp.mpf(b.numerator)/b.denominator)<mp.mpf('1e-60')*max(1,abs(a)))
  d=V/'manufactured_chunks';d.mkdir(exist_ok=False);store=MPChunkStore(d,5,72,2,{'synthetic':'333'},chunk_size=2)
  compute=lambda i:[mp.mpf(i)/7,mp.mpf(i)**2/3]
  rows=store.run(compute);ck('chunk complete recovery',store.run(compute)==rows);ck('decimal validation',all(len(r)==2 and all(decimal_value(s).denominator>0 for s in r)for r in rows))
  bad=d/'chunk_0000000.json.gz';old=bad.read_bytes();bad.write_bytes(b'corrupt');rejected=False
  try:store.run(compute)
  except Exception:rejected=True
  bad.write_bytes(old);ck('corrupt chunk refused',rejected);ck('recovered restored chunk',store.run(compute)==rows)
 for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:ck('one thread '+name,os.environ[name]=='1')
 out=dict(status='PASS_SELECTED_ANGULAR_MP_MANUFACTURES',started_utc=t0,finished_utc=now(),count=len(checks),checks=checks,module_paths=paths,bindings=source_bindings());save(V/'MANUFACTURES.json',out);print(json.dumps({k:out[k]for k in ['status','started_utc','finished_utc','count']}),flush=True)
def candidate():
 t0=now();checks=[];bindings={};paths=origins();O=V/'candidate';O.mkdir(exist_ok=False)
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:raise AssertionError(n)
 def bind(p,h=None):
  p=Path(p).resolve();a=sha(p);ck('binding '+str(p),h is None or a==h);bindings[str(p)]=a;return p
 try:
  ck('nice19',os.getpriority(os.PRIO_PROCESS,0)==19);ck('memory14GiB',resource.getrlimit(resource.RLIMIT_AS)==(14*1024**3,14*1024**3))
  for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:ck('one thread '+n,os.environ[n]=='1')
  m=json.loads(bind(V/'MANUFACTURES.json').read_text());ck('manufactures completed',m['status']=='PASS_SELECTED_ANGULAR_MP_MANUFACTURES'and m['count']==len(m['checks'])and all(c['passed']for c in m['checks'])and m['module_paths']==paths)
  for p,h in m['bindings'].items():bind(p,h)
  c=json.loads(bind(OLD/'candidate/COMPLETE.json').read_text());ck('327 raw complete',c['status']=='COMPLETE_FINITE_CANDIDATE_DIAGNOSTIC_REQUIRES_CHECK')
  for p,h in {**c['bindings'],**c['outputs']}.items():bind(p,h)
  old=json.loads(bind(OLD/'CHECKS.json').read_text());ck('327 exact audit passed',old['count']==191 and all(a['passed']for a in old['checks']))
  for p,h in old['bindings'].items():bind(p,h)
  import torch
  torch.set_num_threads(1)
  sp=bind(ROOT/'research/accurate_map_final_audit/verification/hsQ_c2.0_N128_acc.pt','f8b2b6ef3d926e6af94b4a36e6d62102cdb85a4501284a5b6c2a43ce001fdc37')
  with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(sp)
  ck('exact state',q.N==128 and q.M==32 and q.cl==2 and q.p==.5 and q.L==1 and q.kappa==2 and q.basis=='local')
  jet=CartesianQJet(q).jet;records=[];base=dict(bindings)
  for radius in [3,30]:
   b=load(OLD/'candidate'/('R'+str(radius)+'_B.npz'));i=254;x,y=map(float,[b['x'][i],b['y'][i]]);geom=geometry(jet,x,y,q.p);sel=[0,2,3]
   ck('complete stored point replay '+str(radius),np.array_equal(geom['reference_velocity'],b['velocity'][i,sel])and np.array_equal(geom['reference_tail'],b['tail'][i,sel])and np.array_equal(geom['metadata'],b['meta'][i])and np.array_equal(geom['local_jet'],b['jet'][i])and np.array_equal(geom['eps'],b['eps'][sel]))
   ck('finite geometry '+str(radius),all(np.isfinite(a).all()for a in geom.values())and np.all(geom['node']>0)and np.all(geom['w2']>0)and np.all(geom['wt']>=0)and np.all(geom['h']>0))
   gp=O/('R'+str(radius)+'_geometry.npz');tmp=gp.with_suffix('.tmp.npz');np.savez_compressed(tmp,**geom);tmp.replace(gp);gb=dict(base);gb[str(gp.resolve())]=sha(gp)
   prec=[]
   for digits in [72,108]:
    with mp.workdps(digits):model=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk)
    local=MPChunkStore(O/('R'+str(radius)+'_local_'+str(digits)),1,digits,4,gb).run(lambda _:model.jet(x,y))
    def compute(k):return mp_row(model.density,x,float(geom['node'][k]),geom['xplus'][k],geom['xminus'][k],geom['h'][k])
    directory=O/('R'+str(radius)+'_integrands_'+str(digits));rows=MPChunkStore(directory,len(geom['node']),digits,4,gb).run(compute,lambda n:print(json.dumps(dict(utc=now(),radius=radius,digits=digits,completed=n,total=len(geom['node']))),flush=True))
    prec.append(dict(digits=digits,local_rows=local,integrand_directory=str(directory.resolve()),row_count=len(rows),chunk_bindings=gb))
   records.append(dict(radius=radius,index=i,x=x,y=y,geometry=str(gp.resolve()),nodes=len(geom['node']),precisions=prec))
  for p,h in bindings.items():ck('final stable '+p,sha(p)==h)
  artifacts={str(p.resolve()):sha(p)for p in O.rglob('*')if p.is_file()and not p.name.endswith('.tmp')}
  out=dict(status='COMPLETE_SELECTED_ANGULAR_MP_REQUIRES_EXACT_CHECK_AND_REVIEW',started_utc=t0,finished_utc=now(),count=len(checks),checks=checks,bindings=bindings,artifacts=artifacts,module_paths=paths,versions=dict(python=sys.version,numpy=np.__version__,mpmath=mp.__version__,torch=torch.__version__),argv=sys.argv,records=records,scope='Selected frozen B-rule nodes and rounded FD coordinates, finite MP observations, no enclosure or primary endpoint.')
  save(O/'COMPLETE.json',out);print(json.dumps({k:out[k]for k in ['status','started_utc','finished_utc','count']}),flush=True)
 except Exception:
  save(O/'FAILURE.json',dict(utc=now(),started_utc=t0,checks=checks,bindings=bindings,traceback=traceback.format_exc()));raise
if __name__=='__main__':
 if len(sys.argv)!=2 or sys.argv[1]not in ['manufacture','candidate']:raise ValueError('mode')
 (manufacture if sys.argv[1]=='manufacture'else candidate)()
