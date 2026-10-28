"""Single-thread original-data certificate for a simple vertical turning height."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,hashlib,time,bisect
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
s=importlib.util.spec_from_file_location('turn_integrate',LANE/'proofs/134_residual_green_taylor/code/integrate.py');I=importlib.util.module_from_spec(s);s.loader.exec_module(I)
P,G,M,aa=I.P,I.G,I.M,I.aa
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def emit(**kw): print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),**kw}),flush=True)
def point(d,cache,t):
 rh,drh,pp,qq,ppt=P.point(d,cache,t);fac=(2*aa(t)).exp();r0=[fac*v for v in rh];r1=[fac*(2*v+dv) for v,dv in zip(rh,drh)];p2=[]
 for n in range(1,262):
  base=qq[n-1]+(r0[n-1]+r0[n])/2;ii=(base-pp[n-1])/(2*n);jj=(base+pp[n-1])/(2*n)
  ii=-(2*n+2)*ii+r0[n-1];jj=(2*n-2)*jj-r0[n]
  ii=-(2*n+2)*ii+r1[n-1];jj=(2*n-2)*jj-r1[n]
  p2.append(n*(jj-ii))
 dj=[-sum(((-1)**n*v for n,v in enumerate(row,1)),arb(0)) for row in [pp,ppt,p2]];dj[0]+=1/aa(d.k)
 return 2/aa(d.k)-dj[0]-dj[1],-dj[1]-dj[2],dj

def encl(ep,half):
 co,err=I.series(ep,F(0),half,16);radius=sum((arb(v.abs_upper()) for v in co[1:]),arb(0))+err
 return co[0]+arb(0,radius.upper()),G.rec(err)

def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1
 M.SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz';d=M.Data();cache=G.load_cache(d)
 assert d.sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 assert H(G.CACHE)=='817da858bacb71182584aef99311572a8212e4525105de775dedb8bb513c5da2'
 lo,hi=F(2),F(3);al=point(d,cache,lo)[0];ah=point(d,cache,hi)[0];assert al<0 and ah>0;steps=[]
 for j in range(18):
  mid=(lo+hi)/2;a,at,dj=point(d,cache,mid);steps.append({'t':str(mid),'a':G.rec(a),'at':G.rec(at)})
  if a<0:lo=mid
  elif a>0:hi=mid
  else:raise ValueError('Indeterminate bisection sign')
  emit(step=j,lo=str(lo),hi=str(hi),a=a.str(12),seconds=time.monotonic()-start)
  if hi-lo<=F(1,65536) and bisect.bisect_right(d.knots,lo)==bisect.bisect_left(d.knots,hi):break
 center=(lo+hi)/2;half=(hi-lo)/2;span=bisect.bisect_right(d.knots,center)-1
 assert d.knots[span]<lo<hi<d.knots[span+1]
 results=[]
 for bits in (512,640):
  ctx.prec=bits
  hs,pe,qe=I.spline_eps(d,cache,span,center);axis=G.EP({F(0):[1/aa(d.k)]})
  for n,ep in enumerate(pe,1):axis=axis+(ep+ep.deriv()).scale((-1)**n)
  ar,er=encl(axis,half);atr,etr=encl(axis.deriv(),half)
  left=P.evaluate(axis,aa(lo-center));right=P.evaluate(axis,aa(hi-center));ac=P.evaluate(axis,arb(0));atc=P.evaluate(axis.deriv(),arb(0))
  checka,checkat,dj=point(d,cache,center)
  assert ac.overlaps(checka) and atc.overlaps(checkat)
  assert left<0 and right>0 and atr>0
  dr=aa(center).exp()+arb(0,((aa(center).exp())*((aa(half).exp())-1)).upper())
  ay=atr/dr
  results.append({'bits':bits,'left_a':G.rec(left),'right_a':G.rec(right),'a_interval':G.rec(ar),'a_t_interval':G.rec(atr),'a_y_interval':G.rec(ay),'y_interval':G.rec(dr),'taylor_remainder_a':er,'taylor_remainder_at':etr,'independent_center_ODE_check':'PASS','center_d_jets':[G.rec(x) for x in dj]})
  emit(stage='certified',bits=bits,lo=str(lo),hi=str(hi),at=atr.str(20),ay=ay.str(20),seconds=time.monotonic()-start)
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_PENDING_PROOF_AUDIT','source_sha256':d.sha,'cache_sha256':H(G.CACHE),'scalar_sha256':H(M.SCALAR),'t_interval_exact':[str(lo),str(hi)],'spline_span':span,'knots_exact':[str(d.knots[span]),str(d.knots[span+1])],'results':results,'bisection':steps,'code_sha256':H(__file__),'dependencies':{str(Path(z.__file__).relative_to(LANE)):H(z.__file__) for z in [I,P,G,M]},'elapsed_seconds':time.monotonic()-start}
 (TOP/'evidence/turn_certificate.json').write_text(json.dumps(out,indent=2)+'\n');emit(stage='DONE',seconds=out['elapsed_seconds'])
if __name__=='__main__':main()
