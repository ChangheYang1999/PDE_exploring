"""Independent Cartesian finite audit of a completed tuned c=3 prefix."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from functools import lru_cache
import argparse,gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,acb,arb_poly,acb_poly,fmpq,ctx
from stream_precision_audit import unpack

ap=argparse.ArgumentParser();ap.add_argument('--max-order',type=int,default=150);ap.add_argument('--grid-steps',type=int,default=2048);a=ap.parse_args()
start=time.monotonic();ctx.prec=1536;zero=arb(0)
root=Path('research/128_tuned_finite_audit');stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');out=root/'verification'/stamp;out.mkdir()
text=lambda x:x.str(40,radius=True)
@lru_cache(None)
def rb(q):return arb(fmpq(str(q)))
class L:
 def __init__(self,lo=0,coeff=None):self.lo=lo;self.p=arb_poly([] if coeff is None else coeff)
 def coeff(self,m):return self.p[m-self.lo] if m>=self.lo else zero
 def scale(self,c):return L(self.lo,self.p*c)
 def __add__(self,o):
  lo=min(self.lo,o.lo)
  return L(lo,arb_poly([zero]*(self.lo-lo)+self.p.coeffs())+arb_poly([zero]*(o.lo-lo)+o.p.coeffs()))
 def __sub__(self,o):return self+o.scale(-1)
 def __mul__(self,o):return L(self.lo+o.lo,self.p*o.p)
 def diff(self,q,Y=False):
  c=self.p.coeffs();r=[zero]*(len(c)+2)
  for j,v in enumerate(c):
   m=self.lo+j;r[j]+=v*rb((q+m)/2);r[j+2]+=v*rb((q-m)/2)*(-1 if Y else 1)
  return L(self.lo-1,r)
 def sine_coeffs(self):
  hi=self.lo+len(self.p)-1;r=[zero]*(max(0,hi)+1)
  for m in range(1,hi+1):
   v=self.coeff(m);assert (v+self.coeff(-m)).contains(0)
   if m%2==0:assert v.contains(0)
   else:r[m]=2*v
  assert self.coeff(0).contains(0)
  return r

def p(n):return Q(1)-Q(2*n,3)
def field(coeff,odd):
 degree=(2*(len(coeff)-1)+1) if odd else 2*(len(coeff)-1);v=[zero]*(2*degree+1)
 for j,x in enumerate(coeff):
  m=2*j+(1 if odd else 0)
  if not m:assert x.is_zero();continue
  v[degree+m]=x/2;v[degree-m]=-x/2
 return L(-degree,v)
def certified_sup(coeff,k,steps):
 cc=[v*(m**k) for m,v in enumerate(coeff)]
 pp=acb_poly([acb(v) for v in cc]);lower=zero;upper=zero
 for j in range(steps+1):
  th=arb.pi()*j/steps;value=pp(acb(th.cos(),th.sin()));value=value.imag if k%2==0 else value.real
  lower=lower.max(value.abs_lower());upper=upper.max(value.abs_upper())
 M2=sum((abs(v)*m*m for m,v in enumerate(cc)),zero);error=(arb.pi()/steps)**2*M2/8
 return dict(lower=text(lower),upper=text(upper+error),grid_upper=text(upper),interpolation_error=text(error),steps=steps)
def evaluate(coeff,theta):
 pp=acb_poly([acb(v) for v in coeff]);th=rb(theta);return pp(acb(th.cos(),th.sin())).imag

try:
 src=Path('../a4-num/ckpt/tuned_b1_p1024.pkl');raw=src.read_bytes();srcsha=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
 Nsrc=max(state['f']);assert state['ring']=='arb' and state['prec']==1024
 # A source checkpoint ends on an open resonance; require three following orders
 # before retaining a free stream coefficient. This conservative cut is uniform.
 N=min(a.max_order,Nsrc-3);assert N>=81
 for k in ['f','g','stats']:state[k]={n:v for n,v in state[k].items() if n<=N}
 state['N']=N
 packed=pickle.dumps(state,protocol=4);(out/'selected_checkpoint.pkl.gz').write_bytes(gzip.compress(packed,compresslevel=1,mtime=0))
 selection=dict(source_path=str(src),source_sha256=srcsha,source_maximum_order=Nsrc,selected_maximum_order=N,selection_rule='orders at most min(requested, source maximum minus3)',selected_uncompressed_sha256=sha256(packed).hexdigest(),selected_uncompressed_bytes=len(packed));del packed
 for name in ['tuned_c3.py','ffcore.py','evaluate_series.py']:(out/(name+'.source.txt')).write_bytes(Path('../a4-num/code',name).read_bytes())
 evalsrc=Path('../a4-num/notes/eval_tuned_b1_p1024.json');evaldata=json.loads(evalsrc.read_text());(out/'source_evaluation.json').write_bytes(evalsrc.read_bytes())
 f={n:[arb(*unpack(v)) for v in state['f'][n]] for n in range(1,N+1)};g={n:[arb(*unpack(v)) for v in state['g'][n]] for n in range(1,N+1)}
 assert f[1][0]==1;b=f[1][1]
 exactroot=json.loads(Path('research/119_tuned_rational_series/verification/algebraic_numeric_values.json').read_text())['rows'][0]['root_interval'];lo,hi=map(Q,exactroot)
 P=[10532171936,-243275209320,2783057141280,-20675598499400,96180432855375,-222533688701250,176703765525000]
 def peval(x):
  v=Q(0)
  for c in reversed(P):v=v*x+c
  return v
 fl=peval(lo)
 for _ in range(1600):
  mid=(lo+hi)/2;fm=peval(mid)
  if fl*fm<0:hi=mid
  else:lo=mid;fl=fm
 exactball=rb(lo).union(rb(hi));assert b.contains(exactball)
 counts=dict(root_containment=1,old_cartesian_overlap=0,poisson_coefficients=0,nonlinear_coefficients=0,ordered_pairs=0,compatibility_projections=0)
 old=json.loads(Path('research/119_tuned_rational_series/verification/arb_N30_20261031T094659Z/coefficients.json').read_text())[0]
 for key,series,odd in [('density',f,True),('stream',g,False)]:
  for ns,values in old[key].items():
   n=int(ns)
   for ms,oldv in values.items():
    m=int(ms);j=(m-1)//2 if odd else m//2
    assert series[n][j].overlaps(arb(oldv)),(key,n,m);counts['old_cartesian_overlap']+=1
 F={n:field(f[n],True) for n in f};G={n:field(g[n],False) for n in g}
 FX={n:F[n].diff(p(n)) for n in F};FY={n:F[n].diff(p(n),True) for n in F}
 GX={n:G[n].diff(p(n)+1) for n in G};GY={n:G[n].diff(p(n)+1,True) for n in G}
 maxrel=zero;normrows=[]
 for n in range(1,N+1):
  rr=GX[n].diff(p(n)).scale(-1)+GY[n].diff(p(n),True)-FX[n]
  for v in rr.p.coeffs():assert v.contains(0),('poisson',n,text(v));counts['poisson_coefficients']+=1
  M=sum(map(abs,f[n]),zero);S=sum(map(abs,g[n]),zero)
  normrows.append(dict(n=n,density_norm=text(M),stream_norm=text(S),density_root=text((M.log()/n).exp()),stream_root=text((S.log()/n).exp()),density_norm_relative_radius=text(M.rad()/abs(M.mid())),stream_norm_relative_radius=text(S.rad()/abs(S.mid()))))
  if n==1:continue
  acc=L()
  for i in range(1,n):
   j=n-i;acc=acc+GX[i]*FY[j]-GY[i]*FX[j];counts['ordered_pairs']+=1
  rr=acc-F[n].scale(2*(n-1))
  for v in rr.p.coeffs():assert v.contains(0),('nonlinear',n,text(v));counts['nonlinear_coefficients']+=1
  rel=sum((abs(v) for v in rr.p.coeffs()),zero)/(2*(n-1)*M);maxrel=maxrel.max(rel)
  if n%3==0 and n>=6:
   obstruction=f[n][n//3-2];assert obstruction.contains(0);counts['compatibility_projections']+=1
  if n%10==0:print(json.dumps(dict(stage='coefficient_audit',n=n,elapsed_s=time.monotonic()-start)),flush=True)
 (out/'coefficient_checks.json').write_text(json.dumps(dict(selection=selection,counts=counts,norm_rows=normrows,maximum_relative_nonlinear_residual=text(maxrel),root_source_ball=text(b),all_checks_pass=True),indent=2)+'\n')
 rows=[]
 for Nt in [10,20,40,80]:
  for radius in [Q(1,4),Q(1,2),Q(1),Q(2),Q(4)]:
   z=(-rb(Q(2,3))*rb(radius).log()).exp();A=L();B=L();C=L();D=L();lin=L();partial=L();power=arb(1)
   for n in range(1,Nt+1):
    A=A+GX[n].scale(power);B=B+GY[n].scale(power);C=C+FX[n].scale(power);D=D+FY[n].scale(power);lin=lin+F[n].scale(-2*(n-1)*power);partial=partial+F[n].scale(power);power*=z
   residual=((A*D-B*C).scale(z)+lin).sine_coeffs();fc=F[Nt+1].scale(z**Nt).sine_coeffs();sc=partial.sine_coeffs()
   bounds={str(k):certified_sup(residual,k,a.grid_steps) for k in range(3)}
   nextbounds={str(k):certified_sup(fc,k,a.grid_steps) for k in range(2)}
   partials=[evaluate(sc,th) for th in [Q(3,10),Q(9,10),Q(13,10)]]
   reported=next(r for r in evaldata['rows'] if r['N']==Nt and Q(str(r['R']))==radius)
   row=dict(N=Nt,R=str(radius),residual_bounds=bounds,next_increment_bounds=nextbounds,partial_sums=list(map(text,partials)),reported=reported)
   rows.append(row)
   (out/'residual_checks.partial.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n')
   print(json.dumps(dict(stage='residual',N=Nt,R=str(radius),bound=bounds['0'],elapsed_s=time.monotonic()-start)),flush=True)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,selection=selection,counts=counts,rows=rows,arithmetic_bits=ctx.prec,actual_elapsed_s=time.monotonic()-start,scope='Finite interval consistency and continuum residual bounds; no improved infinite convergence radius is inferred.')
 (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
 for name in ['tuned_checkpoint_audit.py','stream_precision_audit.py']:(out/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
 files={p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()};(out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(dict(all_checks_pass=True,output=str(out),actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as e:
 import traceback
 failure=dict(error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)],actual_elapsed_s=time.monotonic()-start)
 (out/'FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
