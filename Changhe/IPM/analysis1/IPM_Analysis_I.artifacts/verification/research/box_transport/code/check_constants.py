"""Exact box costs; Arb exponential versus positive Taylor series with iv rounding."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,resource,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];E=B/'research/box_transport/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ae(x):
 assert x.is_finite()
 def one(y):assert y.rad()==0;m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return one(x.lower()),one(x.upper())
def ie(x):
 out=[]
 for s,m,e,b in x._mpi_:
  assert b>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return tuple(out)
def pack(v,method):
 l,h=ae(v) if method=='arb' else ie(v);return {'lower_exact':str(l),'upper_exact':str(h),'display':str(v)}
def exponential_series(z,N=128):
 assert 0<=z<1 and N>=0
 term=F(1);total=term;ti=iv.mpf(1);si=ti
 for j in range(1,N+1):
  term*=z/j;total+=term;ti*=ii(z)/j;si+=ti
 ratio=z/(N+2);rem=term*z/(N+1)/(1-ratio)
 remi=ti*ii(z)/(N+1)/(1-ii(ratio));out=iv.mpf([si.a,(si+remi).b])
 l,h=ie(out);assert l<=total<=total+rem<=h and rem>=0
 return out,{'degree':N,'argument_exact':str(z),'sum_exact':str(total),'tail_majorant_exact':str(rem),'maximum_tail_ratio_exact':str(ratio)}
def main():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 endpoint=0
 for q in [F(0),F(1),F(-13,64),F(1,3),F(2929,13000)]:
  for pair in [ae(aa(q)),ie(ii(q))]:assert pair[0]<=q<=pair[1];endpoint+=1
 rejects=0
 for x in [iv.mpf('inf'),iv.mpf('-inf'),iv.mpf('nan')]:
  try:ie(x)
  except AssertionError:rejects+=1
  else:raise AssertionError('nonfinite accepted')
 l,u,h=F('4.80'),F('6.82'),F('2.85');speed=F(13);top=F('1.23');outside=F('-0.22');duration=(u-l)/speed;assert duration==F(101,650)
 rows=[];overlaps=0;comparisons=[]
 for kap,expected,public_low,public_high in [(F(1,5),F(1111,5000),F('6.244'),F('6.245')),(F(11,50),F(2929,13000),F('5.694'),F('5.695'))]:
  assert kap>0 and outside+kap<=0;cost=(top+kap)*duration;assert cost==expected
  A=aa(cost).exp()/aa(kap);I,series=exponential_series(cost);I/=ii(kap)
  al,ah=ae(A);il,ih=ie(I);assert max(al,il)<=min(ah,ih);overlaps+=1
  sl=F(series['sum_exact'])/kap;sh=(F(series['sum_exact'])+F(series['tail_majorant_exact']))/kap
  assert il<=sl<=sh<=ih and al<=sl<=sh<=ah
  for method,pair in [('arb',(al,ah)),('iv',(il,ih))]:
   assert public_low<pair[0]<=pair[1]<public_high
   comparisons.append({'kappa_exact':str(kap),'method':method,'strict_public_lower_exact':str(public_low),'strict_public_upper_exact':str(public_high)})
  if kap==F(1,5):assert min(al,il)>F('6.2')
  else:assert max(ah,ih)<F('5.7')
  rows.append({'kappa_exact':str(kap),'K_exact':str(cost),'C_upper_exact':str(2*cost),'arb':pack(A,'arb'),'iv':pack(I,'iv'),'series':series,'exact_series_scaled_interval':[str(sl),str(sh)],'joint_enclosure':[str(min(al,il)),str(max(ah,ih))]})
 # The exact derivative bound covers the entire allowed kappa interval.
 der_upper=duration-1/(-outside);assert der_upper<0
 # Independently rearranged semigroup margin arithmetic, including nonpositive c_l.
 count=0
 for cl in [F(-3),F(0),F(1),F(9007199254740992,1615536043799051)]:
  for kap in [F(1,5),F(11,50),F(1,3)]:
   for dt in [F(0),F(1,7),F(2),F(100)]:
    K=(top+kap)*duration;weight_change=2*(1+cl-kap)*dt+2*K;log_norm_e_t_S=weight_change/2-cl*dt-dt;assert log_norm_e_t_S==K-kap*dt;count+=1
 # Positive-part coverage and factor2 contract on exact finite histories with overlap.
 histories=0
 for off in [F(0),F(-1,10),F(-3)]:
  for s1 in [F(0),F(1,3),F(5)]:
   for s2 in [F(0),F(2,7)]:
    intervals=[(F(0),F(1),s1),(F(1,2),F(3,2),s2)];grid=[F(0),F(1,2),F(1),F(3,2),F(2)];vals=[]
    for a,b in zip(grid,grid[1:]):
     midpoint=(a+b)/2;cover=sum(s for l,r,s in intervals if l<=midpoint<=r);val=cover+off;vals.append((b-a,val,cover))
    K=s1+s2;positive=sum(dt*max(v,0) for dt,v,c in vals);assert positive<=K
    for a in range(len(vals)):
     for b in range(a,len(vals)+1):assert 2*sum(dt*v for dt,v,c in vals[a:b])<=2*K;histories+=1
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_CONDITIONAL_CONSTANTS','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/box_transport/PROOF.md'),'lead_snapshot_sha256':sha(E/'lead_global_flow_v2.md'),'runtime':{'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_decimal_digits':iv.dps},'box_exact':{'x_lower':str(l),'x_upper':str(u),'y_upper':str(h),'negative_speed':str(speed),'inside_T_upper':str(top),'outside_T_upper':str(outside),'residence_upper':str(duration)},'rows':rows,'public_comparisons':comparisons,'allowed_kappa_upper_exact':str(-outside),'log_bound_derivative_upper_exact':str(der_upper),'checks':{'endpoint_containments':endpoint,'nonfinite_rejections':rejects,'exponential_overlaps':overlaps,'public_two_sided_enclosures':len(comparisons),'semigroup_factor_identities':count,'overlapping_history_segment_inequalities':histories},'seconds':time.monotonic()-start,'scope':'Conditional box inverse expressions and exact algebra only. No actual finite-domain velocity, margin, orbit, canonical input or coupled operator evaluated.'}
 tmp=E/'checks.json.tmp';tmp.write_text(json.dumps(out,indent=2)+'\n');os.replace(tmp,E/'checks.json')
 print(json.dumps({'utc':out['utc'],'status':out['status'],'checks':out['checks'],'bounds':[{key:r[key] for key in ['kappa_exact','K_exact','arb','iv']} for r in rows],'seconds':out['seconds']}))
if __name__=='__main__':main()
