"""Exact artifact linkage and fresh scalar plus polynomial audits for topic95."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,math,importlib.util
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_explicit_inverse';E=D/'evidence';ctx.prec=1536;iv.dps=250

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fa(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def fi(t):s,m,e,_=t;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def upper(x):return fa(x.upper()) if isinstance(x,arb) else fi(x._mpi_[1])
def qa(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def qi(v):v=F(v);return iv.mpf(v.numerator)/v.denominator

def cmul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def cadd(z,w):return z[0]+w[0],z[1]+w[1]
def cscale(z,a):return z[0]*a,z[1]*a
def cpow(z,k):
 if k<0:return cpow((z[0],-z[1]),-k) # unit circle only
 out=(F(1),F(0))
 for _ in range(k):out=cmul(out,z)
 return out

def exact_polynomial_tests():
 sp=importlib.util.spec_from_file_location('explicit_inverse_producer',D/'code/check_bounds.py');mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
 # Producer sets precisions at import; restore independently selected precisions.
 ctx.prec=1536;iv.dps=250
 n=0;x,y=F(3,5),F(4,5);unit=(x,y);ii=(F(0),F(1))
 for beta in (3,4):
  for m in range(8):
   for ell in range(4):
    nu=m+2*ell-beta;poly={}
    for a in range(m+1):
     for b in range(ell+1):
      key=m-a+2*(ell-b),a+2*b;z=cscale(cpow(ii,a),F(math.comb(m,a)*math.comb(ell,b)))
      poly[key]=cadd(poly.get(key,(F(0),F(0))),z)
    for k in range(6):
     for xc in range(k+1):
      yc=k-xc;direct=(F(0),F(0))
      for (ix,iy),z in poly.items():
       if ix>=xc and iy>=yc:
        fac=F(math.factorial(ix)//math.factorial(ix-xc))*F(math.factorial(iy)//math.factorial(iy-yc))*x**(ix-xc)*y**(iy-yc)
        direct=cadd(direct,cscale(z,fac))
      got=(F(0),F(0));rows=mod.cartesian(beta,m,k,xc);assert len(rows)==k+1
      for j,row in enumerate(rows):
       q=sum((v*nu**l for l,v in enumerate(row)),F());got=cadd(got,cscale(cpow(unit,m-k+2*j),q))
      got=cmul(got,cpow(ii,-yc));assert direct==got,(beta,m,ell,k,xc,direct,got);n+=1
 return n

def main():
 d=json.loads((E/'checks.json').read_text());counts=Counter();files={}
 assert d['status']=='PASS_EXPLICIT_AUXILIARY_INVERSE_BOUND'
 for name,h in d['files'].items():assert sha(B/name)==h,name;counts['producing_output_pins']+=1;files[name]=h
 for eng in ('arb','iv'):
  rows=[r for r in d['span_rows'] if r['engine']==eng];assert [r['span'] for r in rows]==list(range(663,670))
  assert len(d['span_rows'])==14
  for key,top in d['high_derivative_maxima_exact'][eng].items():
   vals=[F(r['bounds_exact'][key]) for r in rows];assert min(vals)>=0 and max(vals)==F(top);counts['whole_span_maximum_checks']+=1
   ceil=d['high_derivative_ceilings'][key];assert type(ceil)==int and F(top)<ceil;counts['strict_outward_integer_ceilings']+=1
  assert d['counts'][eng+'_polynomial_derivative_envelopes']==7*262*6 and d['counts'][eng+'_moment_whole_span_envelopes']==7*261*2
 assert d['counts']['whole_disc_radial_coverage']==2 and d['counts']['ladder_cartesian_weight_identities']==60
 counts['manufactured_mixed_cartesian_identities']=exact_polynomial_tests()
 # Independently count all singleton/pair partitions via their scalar recurrence.
 L=list(map(F,d['cutoff_L_exact']));C=[F(1)];a=F(273,64);nu=F(23,4)/a;vv=3/a
 for j in range(1,5):
  # B_{n,k} for f' = nu, f'' = vv; partial Bell recurrence.
  Bell={(0,0):F(1)}
  for n in range(1,j+1):
   for k in range(1,n+1):Bell[n,k]=sum((math.comb(n-1,r-1)*(nu if r==1 else vv)*Bell.get((n-r,k-1),F(0)) for r in (1,2) if r<=n-k+1),F())
  C.append(sum((L[k]*Bell[j,k] for k in range(1,j+1)),F()))
 assert C==list(map(F,d['cutoff_C_exact'])) and C[1]<2;counts['Bell_partition_checks']=4
 delta=F(33,2000);r0=3*delta;MV=F(743,2500);MR=F(5059,10000);ceil=d['high_derivative_ceilings']
 v=[MV*r0*r0/2,MV*r0,MV,F(ceil['U3']),F(ceil['U4'])];q=[MR*r0,MR,F(ceil['rho3']),F(ceil['rho4']),F(ceil['rho5'])]
 products=[]
 for name,bv in [('cutoff_product_Bw_exact',v),('cutoff_product_Bq_exact',q)]:
  result=[sum((F(math.comb(j,k))*C[k]/delta**k*bv[j-k] for k in range(j+1)),F()) for j in range(5)]
  assert result==list(map(F,d[name]));counts['exact_product_checks']+=5;products.append(result)
 scalar={};published={'61/20':F('2.672e34'),'153/50':F('3.518e34'),'31/10':F('1.068e35')}
 for eng,Q,pi in [('arb',qa,arb.pi()),('iv',qi,iv.pi)]:
  sqrt=lambda x:x.sqrt() if eng=='arb' else iv.sqrt(x)
  alpha=lambda t:1/(2*sqrt(pi*Q(F(t)-1)));beta=lambda t:1/(2*sqrt(pi*Q((F(t)-1)*(F(t)-2))))
  Hw,Hq=[sqrt(pi*Q(r0*r0*sum((math.comb(4,j)*b*b for j,b in enumerate(vv)),F()))) for vv in products]
  for key,val in [('H_w_upper',Hw),('H_q_upper',Hq)]:assert upper(val)<=F(d['scalar_results'][eng][key]);counts['fresh_scalar_containments']+=1
  def margins(s):return F(1301,200)-F(101,100)*s-delta*((12*s+F(9,2))*MV+3*MR),(101*s-1)/100
  sr={}
  for s in map(F,('61/20','153/50','31/10')):
   aa,dd=margins(s);R=sqrt(Q(2))*Q(s*(s-1))*Q(2)**Q(s-4)*(alpha(2)+beta(s-1))*Hw+sqrt(Q(2))*Q(s)*Q(2)**Q(s-2)*(alpha(3)+alpha(s-1))*Hq
   norm=(1+R/Q(dd))**Q(s)/Q(aa);old=d['scalar_results'][eng]['rows'][str(s)]
   assert aa==F(old['a_lower_exact']) and dd==F(old['d_lower_exact']);assert upper(R)<=F(old['R_upper']) and upper(norm)<=F(old['inverse_upper']);counts['fresh_scalar_containments']+=2
   assert upper(norm)<published[str(s)];counts['published_inverse_ceilings']+=1
   sr[str(s)]={'R_upper_exact':str(upper(R)),'inverse_upper_exact':str(upper(norm)),'published_inverse_ceiling_exact':str(published[str(s)])}
  sm,sp=F(61,20),F(31,10);amin=margins(sp)[0];dmin=margins(sm)[1]
  Rbar=sqrt(Q(2))*Q(sp*(sp-1))*Q(2)**Q(sp-4)*(alpha(2)+beta(sm-1))*Hw+sqrt(Q(2))*Q(sp)*Q(2)**Q(sp-2)*(alpha(3)+alpha(sm-1))*Hq
  unif=(1+Rbar/Q(dmin))**Q(sp)/Q(amin);assert upper(unif)<F('1.2e35');counts['uniform_interval_ceiling_checks']+=1
  scalar[eng]={'rows':sr,'uniform_R_upper_exact':str(upper(Rbar)),'uniform_inverse_upper_exact':str(upper(unif)),'uniform_inverse_display':float(upper(unif)),'uniform_R_display':float(upper(Rbar)),'uniform_ceiling_exact':str(F('1.2e35'))}
 for p in [E/'checks.json',E/'review_summary.json',D/'AUDIT_METHOD.md',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARTIFACT_AND_FRESH_SCALAR_AUDIT','counts':dict(counts),'scalar_results':scalar,'files':files,'scope':'Fresh output and mixed Cartesian identities; two existing whole-span enclosures; imported canonical archive; uniform auxiliary bound, not full IPM inverse.'}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'counts':dict(counts),'uniform_displays':{e:r['uniform_inverse_display'] for e,r in scalar.items()}},indent=2))
if __name__=='__main__':main()
