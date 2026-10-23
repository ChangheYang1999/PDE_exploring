from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,sys,json,hashlib,resource
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import mpmath as mp
import numpy as np
from direct_primary_quadrature import DirectField,number
ROOT=Path('verification');R=ROOT/'research/primary_direct_quadrature_spotcheck';V=R/'verification'
assert not sys.flags.optimize and Path.cwd().resolve()==ROOT
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def enc(v):v=F(v);return dict(numerator=str(v.numerator),denominator=str(v.denominator))
def data(co):return dict(alpha=enc(F(3,10)),length=enc(F(5,4)),cl=enc(F(5,2)),chebyshev_coefficients=[[enc(v)for v in row]for row in co])
def manufacture():
 checks=[]
 def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
 with mp.workdps(75):
  for co in [[[F(7,3)]],[[F((-1)**(k+j)*(k+j+1),k+2*j+3)for j in range(4)]for k in range(4)]]:
   m=DirectField(data(co))
   for xs,ys in [('.43','.79'),('1.3','.05'),('.013','2.8')]:
    x,y=mp.mpf(xs),mp.mpf(ys);g,gx,gy=m.local(x,y)
    for key,a,b in [('rho',g,m.direct_density(x,y)),('gx',gx,mp.diff(lambda t:m.direct_density(t,y),x)),('gy',gy,mp.diff(lambda t:m.direct_density(x,t),y))]:ck(key+str((len(co),xs,ys)),abs(a-b)<mp.mpf('1e-65'))
    r=mp.hypot(x,y);th=mp.atan2(y,x);f=mp.fsum(v*mp.sin(2*j*th)for j,v in enumerate(m.source(r),1));ck('source'+str((len(co),xs,ys)),abs(f-gx)<mp.mpf('1e-65'))
  m=DirectField(data([[F(7,3)]]));x,y=mp.mpf('.43'),mp.mpf('.79');nodes,weights=np.polynomial.legendre.leggauss(96);got=m.inverse(x,y,nodes,weights)
  def psi(s,t):return -number(F(7,3))*s*t*mp.hyp2f1(number(F(3,10)),2,3,-(s*s+t*t)/number(F(5,4))**2)/4
  ex=[psi(x,y),-mp.diff(lambda t:psi(x,t),y),mp.diff(lambda s:psi(s,y),x)]
  for k,a,b in zip(['psi','U1','U2'],got,ex):ck('quadrature '+k,abs(a-b)<mp.mpf('1e-11'))
 out=dict(status='PASS_DIRECT_PRIMARY_MANUFACTURES',utc=now(),checks=checks,count=len(checks),bindings={str(p.resolve()):sha(p)for p in [Path(__file__),ROOT/'independent_code/direct_primary_quadrature.py',R/'PROOF.md']});(V/'MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}),flush=True)
if sys.argv[1:]==['--manufacture']:manufacture();raise SystemExit
if sys.argv[1:]!=['--candidate']:raise SystemExit('expected --manufacture or --candidate')
assert not(V/'RESULTS.json').exists();start=now();accept=json.loads((V/'DESIGN_ACCEPTANCE.json').read_text());assert accept['status']=='ACCEPTED_DIRECT_PRIMARY_DESIGN'
for p,h in accept['bindings'].items():assert sha(p)==h,p
assert os.getpriority(os.PRIO_PROCESS,0)==19 and all(0<x<=14*1024**3 for x in resource.getrlimit(resource.RLIMIT_AS))
I=json.loads((ROOT/'research/primary_fresh_sample/verification/INPUTS.json').read_text());ref=next(s for s in I['states']if s['N']==44);assert sha(ref['exact_input'])==ref['exact_input_sha256'];d=json.loads(Path(ref['exact_input']).read_text());pt=I['points'][20]
rows=[]
with mp.workdps(75):
 m=DirectField(d);assert m.ell==mp.mpf('2.5');x,y=[number(float.fromhex(z))for z in pt['hex']];g,gx,gy=m.local(x,y)
 direct_source=[]
 for rs,ts in [('.1','.2'),('.5829415347136074','.51'),('3','1.1'),('100','.31')]:
  r,th=mp.mpf(rs),mp.mpf(ts);sx,sy=r*mp.cos(th),r*mp.sin(th);ad=mp.diff(lambda u:m.direct_density(u,sy),sx);modal=mp.fsum(v*mp.sin(2*j*th)for j,v in enumerate(m.source(r),1));direct_source.append(dict(radius=rs,theta=ts,cartesian_derivative=mp.nstr(ad,72),mode_sum=mp.nstr(modal,72),scaled_difference=mp.nstr(abs(ad-modal)/max(1,abs(ad)),72)))
 for order in [96,192,384]:
  nodes,weights=np.polynomial.legendre.leggauss(order);ps,u,v=m.inverse(x,y,nodes,weights);Rr=(m.ell*x+u)*gx+(m.ell*y+v)*gy-g;nf=abs((m.ell*x+u)*gx)+abs((m.ell*y+v)*gy)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(u*gx+v*gy)
  raw=dict(x=x,y=y,rho=g,rho_x=gx,rho_y=gy,psi=ps,U1=u,U2=v,R=Rr,Nf=nf,Nv=nv,R_Nf=abs(Rr)/nf,R_Nv=abs(Rr)/nv)
  rows.append(dict(order=order,utc=now(),nodes_sha256=hashlib.sha256(nodes.tobytes()).hexdigest(),weights_sha256=hashlib.sha256(weights.tobytes()).hexdigest(),values={k:mp.nstr(v,72)for k,v in raw.items()}));(V/'PROGRESS.json').write_text(json.dumps(dict(started_utc=start,rows=rows),indent=2)+'\n');print(json.dumps(dict(order=order,utc=rows[-1]['utc'],R=rows[-1]['values']['R'])),flush=True)
for p,h in accept['bindings'].items():assert sha(p)==h,p
out=dict(status='COMPLETE_DIRECT_PRIMARY_QUADRATURE',started_utc=start,finished_utc=now(),pid=os.getpid(),nice=os.getpriority(os.PRIO_PROCESS,0),memory_limits=resource.getrlimit(resource.RLIMIT_AS),environment={k:os.environ[k]for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},bindings=accept['bindings'],source_sha256=ref['source_sha256'],exact_input_sha256=ref['exact_input_sha256'],point=pt,working_digits=75,numpy_version=np.__version__,mpmath_version=mp.__version__,source_checks=direct_source,rows=rows,scope='Finite candidate spotcheck of independent full-plane quadrature, no error enclosure or continuum residual bound');(V/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(status=out['status'],finished_utc=out['finished_utc'])),flush=True)
