"""Fresh source certificate: signed exponential series and exact primitives."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import json,hashlib,sys,time,math
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/source_instance';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def qa(q):
 q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):
 q=F(q);return iv.mpf(q.numerator)/q.denominator
def ends(x):
 if isinstance(x,arb):
  assert x.is_finite()
  def cv(v):
   m,e=v.man_exp();return F(int(m))*F(2)**int(e)
  a,b=cv(x.lower()),cv(x.upper())
 else:
  def cv(v):
   s,m,e,bc=v;assert bc>=0;return F((-1 if s else 1)*int(m))*F(2)**int(e)
  a,b=map(cv,x._mpi_)
 assert a<=b;return a,b
def hull(a,b,q):
 assert a<=b
 return qa(a).union(qa(b)) if q==qa else iv.mpf([qi(a).a,qi(b).b])
def mag(x):a,b=ends(x);return max(abs(a),abs(b))
def dec(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1'
 m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return m-r,m+r
def horner(p,x,q):
 ans=q(0)
 for c in reversed(p):ans=ans*x+c
 return ans
def shift(p,d,q):
 return [sum((p[j]*math.comb(j,l)*d**(j-l) for j in range(l,len(p))),q(0)) for l in range(len(p))]
def moments(L,lam,N=80):
 lo,hi=ends(L);assert lo>=0
 z=L*lam;zmax=mag(z);assert zmax<N+2
 power=arb(1);out=[arb(0) for j in range(8)]
 for k in range(N+1):
  for j in range(8):out[j]+=power/(j+k+1)
  power*=z/(k+1)
 tailbase=zmax**(N+1)/F(math.factorial(N+1))/(1-zmax/F(N+2))
 for j in range(8):
  tail=hi**(j+1)*tailbase/F(j+N+2)
  out[j]=L**(j+1)*out[j]+hull(-tail,tail,qa)
 return out

def primitive(p,L,lam):
 assert ends(L)[0]>=0
 if lam==0:return sum((c*L**(j+1)/(j+1) for j,c in enumerate(p)),qi(0))
 aa=[sum((p[j]*qi(F((-1)**(j-l)*math.factorial(j),math.factorial(l))/F(lam)**(j-l+1)) for j in range(l,len(p))),qi(0)) for l in range(len(p))]
 return iv.exp(L*lam)*horner(aa,L,qi)-aa[0]

def enclosure(x):
 a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
start=time.monotonic();files={};pin_count=0
for name,digest in [('n8_density_hessian','c590ba0d354b26595bd1131f68ca87bbc9875c9d248b4cf5fdf71344ef6e01ca'),('n8_velocity_hessian','8a35f9cb43b241bd7a880b03aa8fcfdc01806a2517f50dbea99530e03a2455d5'),('n8_coefficient_closure','2db983975d979bd3cd553b5dbe98454fcba0053580900e708fff5b6400029447'),('source_local_estimate','81801cde767bf540ecc7dfc31ea89eeb1c641b0d0be1a93217468f7015be0cf7'),('source_semigroup','a57aa031447ac2c44d360d2bae0e288923c2ae0e29f4ac0580c0b9e81d0024a1'),('canonical_strain_sign','ca191db6d3e5902c5bed0e0fbb62e400d78740013762a7218d8c98636f180ae8')]:
 p=B/'research'/name/'evidence/verdict.json'
 assert sha(p)==digest,name
 v=json.loads(p.read_text());files[str(p.relative_to(B))]=digest
 for f,h in v['files'].items():assert sha(B/f)==h,f;pin_count+=1
ip=B/'research/n8_velocity_hessian/evidence/moment_inputs.json';assert sha(ip)=='6f7d3dcf4f1f09256970c0796dc461bc3262cc109051305aa40e9da76a7aa61c'
data=json.loads(ip.read_text());files[str(ip.relative_to(B))]=sha(ip)
for f,h in data['files'].items():assert sha(B/f)==h;pin_count+=1
exactp=B/'data_exact/modal_v2.json';exact=json.loads(exactp.read_text());assert sha(exactp)==data['source_header']['hashes']['input'];files[str(exactp.relative_to(B))]=sha(exactp)
a,b=map(F,data['source_center_bracket_exact']);delta=F(data['delta_exact']);assert delta==F(33,2000)
assert a==F(4841405518533377,562949953421312) and b==F(4841405518533711,562949953421312)
assert 0<delta<=1 and 3*delta<a/2
k=F(data['source_header']['scalars_exact']['k']);assert k==F(float.fromhex(exact['scalars_hex']['k']));cl=1/k
knots=[F(float.fromhex(v)) for v in exact['arrays']['knots']['hex']];assert len(knots)==exact['arrays']['knots']['shape'][0] and exact['degree']==7
assert knots==sorted(knots);km=Counter(knots);uk=sorted(km);assert km[uk[0]]==km[uk[-1]]==8
assert all(km[t]==1 for t in uk[1:-1])
# Both engines establish the whole containing radial annulus is interior.
for q,log in [(qa,lambda x:x.log()),(qi,iv.ln)]:
 assert ends(log(q(a-3*delta)))[0]>uk[0] and ends(log(q(b+3*delta)))[1]<uk[-1]
selected=[]
for sp in data['spans']:
 ta,tb=F(sp['a_exact']),F(sp['b_exact'])
 if all(ta<ends(log(q(a)))[0] and ends(log(q(b)))[1]<tb for q,log in [(qa,lambda x:x.log()),(qi,iv.ln)]):selected.append(sp)
assert len(selected)==1;sp=selected[0];ta,tb,tm=map(F,[sp['a_exact'],sp['b_exact'],sp['polynomial_mid_exact']]);assert tm==(ta+tb)/2
assert ta in km and tb in km and uk[uk.index(ta)+1]==tb
assert len(sp['density_polynomials'])==262 and len(sp['i_left'])==len(sp['j_right'])==261
assert all(len(p)==8 for p in sp['density_polynomials']);assert all(dec(v)==(F(),F()) for v in sp['density_polynomials'][-1])
counts={'frozen_dependency_pins':pin_count,'exact_simple_interior_knots':len(uk)-2,'axis_mode_divergence_identities':0,'primitive_coefficient_identities':0,'arb_monomial_tails':0,'iv_complete_primitives':0,'source_evaluations':0,'engine_endpoint_signs':0,'engine_whole_interval_bounds':0,'moment_overlap_diagnostics':0}
for n in range(1,262):
 m=2*n
 # Coefficients of d_x V1 and d_y V2 in the variables I,J,Hlo,Hhi.
 I=(F(1),F(0),F(0),F(0));J=(F(0),F(1),F(0),F(0));Hlo=(F(0),F(0),F(1),F(0));Hhi=(F(0),F(0),F(0),F(1))
 def addv(v,w):return tuple(x+y for x,y in zip(v,w))
 def scalev(c,v):return tuple(c*x for x in v)
 def subv(v,w):return addv(v,scalev(-1,w))
 Ip=addv(scalev(-m-4,I),Hlo);Jp=subv(scalev(m-4,J),Hhi)
 Y=subv(J,I);Yp=subv(Jp,Ip)
 radial=scalev(-m,addv(scalev(3,Y),Yp))
 angular=subv(scalev(m,addv(scalev(4,Y),Yp)),scalev(m,Y))
 cc=tuple(map(F,[-m*(m+1),-m*(m-1),m,m]));dd=tuple(map(F,[m*(m+1),m*(m-1),-m,-m]))
 assert radial==cc and angular==dd and all(x+y==0 for x,y in zip(radial,angular));counts['axis_mode_divergence_identities']+=1
 for lam in [-m-4,-m+4]:
  if lam==0:continue
  for j in range(8):
   v=[F((-1)**(j-l)*math.factorial(j),math.factorial(l))/F(lam)**(j-l+1) for l in range(j+1)]
   assert all(lam*v[l]+((l+1)*v[l+1] if l<j else 0)==(1 if l==j else 0) for l in range(j+1));counts['primitive_coefficient_identities']+=1
outputs={};moment_intervals={};variation_count=0
for engine,q,log,exp in [('arb',qa,lambda x:x.log(),lambda x:x.exp()),('iv',qi,iv.ln,iv.exp)]:
 polys=[[hull(*dec(v),q) for v in p] for p in sp['density_polynomials']]
 left=[hull(*dec(v),q) for v in sp['i_left']];right=[hull(*dec(v),q) for v in sp['j_right']]
 outputs[engine]={};moment_intervals[engine]={};endpoint_moments=[]
 for label,xx in [('a',q(a)),('b',q(b)),('whole',hull(a,b,q))]:
  t=log(xx);assert ta<ends(t)[0]<=ends(t)[1]<tb
  L=t-q(ta);R=q(tb)-t;H=[shift(p,t-q(tm),q) for p in polys]
  ws=q(0);ds=q(0);mom=[]
  for n in range(1,262):
   m=2*n;li=-m-4;lj=-m+4
   if engine=='arb':
    ml=moments(L,li);mr=moments(R,lj)
    I=exp(li*L)*left[n-1]+sum((v*z*((-1)**j) for j,(v,z) in enumerate(zip(H[n-1],ml))),q(0))
    J=exp(lj*R)*right[n-1]+sum((v*z for v,z in zip(H[n],mr)),q(0));counts['arb_monomial_tails']+=16
    ds+=m*((m+1)*I+(m-1)*J-H[n-1][0]-H[n][0])
   else:
    if label!='whole':
     I=exp(li*L)*left[n-1]+primitive([v*((-1)**j) for j,v in enumerate(H[n-1])],L,li)
     J=exp(lj*R)*right[n-1]+primitive(H[n],R,lj);counts['iv_complete_primitives']+=2
     if label=='a':endpoint_moments.append((I,J))
    else:
     dt=ends(log(q(b))-log(q(a)))[1];assert dt>0
     Ia,Ja=endpoint_moments[n-1]
     # Forcing H evaluated over the complete t interval, not at its midpoint.
     fi=mag(H[n-1][0]);fj=mag(H[n][0])
     eri=ends(q(dt)*exp(q(abs(li)*dt))*q(abs(li)*mag(Ia)+fi))[1]
     erj=ends(q(dt)*exp(q(abs(m-4)*dt))*q(abs(m-4)*mag(Ja)+fj))[1]
     I=Ia+hull(-eri,eri,q);J=Ja+hull(-erj,erj,q);variation_count+=2
    ds+=m*(-(m+1)*I-(m-1)*J+H[n-1][0]+H[n][0])
   ws+=m*(I-J);mom.extend([ends(I),ends(J)])
  w=q(cl)*xx+xx**3*ws/2;g=xx**2*sum(((2*j+1)*p[0] for j,p in enumerate(H)),q(0))
  direct=q(cl)+xx**2*ds/2
  mu=direct if engine=='arb' else q(2*cl)-direct
  wp=q(2*cl)-direct if engine=='arb' else direct
  for val in [w,g,mu,wp]:ends(val)
  outputs[engine][label]={name:enclosure(val) for name,val in [('w',w),('g',g),('mu',mu),('wprime',wp)]};moment_intervals[engine][label]=mom;counts['source_evaluations']+=1
  if label=='a':assert ends(w)[1]<0;counts['engine_endpoint_signs']+=1
  if label=='b':assert ends(w)[0]>0;counts['engine_endpoint_signs']+=1
  if label=='whole':
   for val,lo,hi in [(wp,F(10),F(51,5)),(mu,F(99,100),F(101,100)),(g,F(29),F(30))]:
    vl,vu=ends(val);assert lo<=vl<=vu<=hi;counts['engine_whole_interval_bounds']+=1
  print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'engine':engine,'label':label,'seconds':time.monotonic()-start,'w_display':str(w)}),flush=True)
for label in ['a','b','whole']:
 for (a1,b1),(a2,b2) in zip(moment_intervals['arb'][label],moment_intervals['iv'][label]):assert max(a1,a2)<=min(b1,b2);counts['moment_overlap_diagnostics']+=1
assert variation_count==522
assert F(1)+(F(10)+F(99,100))/2-F(1687,500)==F(3121,1000)
counts['whole_bracket_ode_variation_bounds']=variation_count
for p in [Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json',B/'research/modal_repair/PROOF.md',B/'research/modal_repair/evidence/audit_verdict.json']:files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_SOURCE_AND_LOCAL_INSTANCE','auxiliary_d_lower_exact':'3121/1000','source_bracket_exact':data['source_center_bracket_exact'],'delta_exact':str(delta),'cl_exact':str(cl),'source_span':sp['span'],'outputs':outputs,'counts':counts,'seconds':time.monotonic()-start,'scope':'Each interval engine independently verifies every endpoint sign and whole-source-bracket inequality. Shared canonical anchors and polynomials are accepted dependencies; overlap is diagnostic only. Actual normalized modal_v2 trial local instance, not an exact stationary solution or global inverse.','files':files}
(E/'checks_v2.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:obj[k] for k in ['utc','status','counts','seconds']}),flush=True)
