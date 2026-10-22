from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
from flint import fmpq
from mpmath import iv
iv.dps=220
R=Path(__file__).resolve().parents[3];P=R/'research/variable_transport_graph_obstruction';E=P/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();primary=p.load(E/'check.json');p.rehash(primary['parent_files']);assert primary['proof_sha256']==p.sha(P/'PROOF.md')=='5f6216563558ba2bbf28709c1a24bb2772b792d19f9fa75ee87eb033763202a4'
raw=p.load(R/'data_exact/modal_v2.json')
def hx(text):
 sign=-1 if text.startswith('-') else 1;text=text.lstrip('+-');mant,pow2=text.split('p');whole,frac=mant[2:].split('.');return fmpq(sign*int(whole+frac,16))*fmpq(2)**(int(pow2)-4*len(frac))
k=hx(raw['scalars_hex']['k']);A=(2-k)/k;D=(4-k)/k;eps=fmpq(1,10000);low=fmpq(1,2000);high=fmpq(3,2000);M=fmpq(743,2500);radius=fmpq(99,2000)
# Combine the entire two-component Taylor cost before subtracting from A mu.
err=M*(eps*eps+high*high)/2;xlo=fmpq(43,5)-eps;cost=(D*low*(fmpq(51,5)*eps+err)+A*xlo*err)/(xlo*low);bound=A*fmpq(99,100)-cost
assert bound>10 and eps*eps+high*high<radius*radius
actual={n:str(v) for n,v in {'k':k,'A':A,'D':D,'e':eps,'y_min':low,'y_max':high,'Taylor_remainder':err,'b_lower':bound}.items()};assert actual==primary['actual']
# Independently read the canonical source interval and coarse positive source box.
src=p.load(R/'research/modal_source/evidence/source_result.json');root=[fmpq(q) for q in src['final_root_endpoints_exact']];mul=1+fmpq(src['final_values']['mu_minus_1']['lower_exact']);a0up=fmpq(src['final_values']['A_trial']['upper_exact']);assert root[0]>fmpq(43,5) and mul>fmpq(99,100) and a0up<fmpq(51,5)
# Polynomial dictionaries in (A,D,a,t), where t=i*n. Euler derivative jets
# are built first; then the differential operator coefficients are combined.
Z=(0,0,0,0)
def const(v):v=F(v);return {Z:v} if v else {}
def var(i):z=[0]*4;z[i]=1;return {tuple(z):F(1)}
def add(*polys):
 out={}
 for q in polys:
  for t,c in q.items():out[t]=out.get(t,F())+c
 return {t:c for t,c in out.items() if c}
def mul(q,r):
 out={}
 for t,c in q.items():
  for u,d in r.items():v=tuple(i+j for i,j in zip(t,u));out[v]=out.get(v,F())+c*d
 return {t:c for t,c in out.items() if c}
def scale(q,v):return mul(q,const(v))
Av,Dv,av,t=map(var,range(4));xjet=add(av,const(F(-1,2)),mul(t,Dv));yjet=mul(t,Av)
frozen=add(scale(mul(Av,xjet),-1),mul(Dv,yjet),const(-1));wanted=add(scale(mul(Av,av),-1),scale(Av,F(1,2)),const(-1));assert frozen==wanted
phase=add(scale(mul(Av,mul(t,Dv)),-1),mul(Dv,mul(t,Av)));assert not phase
# On the variable field q1=V1/x and q2=V2/y, the coefficient of i*n is
# D*q1+A*q2. Independent primitive Euler jets xjet,yjet have these two
# coefficients; remove them and inspect the actual zero-order remainder.
restx=add(xjet,scale(mul(t,Dv),-1));resty=add(yjet,scale(mul(t,Av),-1));assert restx==add(av,const(F(-1,2))) and resty=={}
# Direct rational-kernel differentiation in a separate two-variable ring.
def p2mon(i,j,v=1):return {(i,j):F(v)}
def p2add(*qs):
 out={}
 for q in qs:
  for t,c in q.items():out[t]=out.get(t,F())+c
 return {t:c for t,c in out.items() if c}
def p2mul(q,r):
 out={}
 for (i,j),c in q.items():
  for (l,m),d in r.items():out[(i+l,j+m)]=out.get((i+l,j+m),F())+c*d
 return {t:c for t,c in out.items() if c}
def dy(q):return {(i,j-1):j*c for (i,j),c in q.items() if j}
def sc(q,v):return {t:F(v)*c for t,c in q.items() if v*c}
N=p2add(p2mon(2,0),p2mon(0,2,-1));RR=p2add(p2mon(2,0),p2mon(0,2));num=p2add(sc(p2mul(dy(N),RR),-1),sc(p2mul(N,dy(RR)),2));assert sc(num,F(1,2))==p2add(p2mon(2,1,3),p2mon(0,3,-1))
# Exact symbol numerator bound: x^2*y^2+x^4 = x^2*(x^2+y^2).
assert p2add(p2mon(2,2),p2mon(4,0))==p2mul(p2mon(2,0),RR)
identities=['Euler_jet_frozen_conjugation','Euler_jet_phase_cancellation','Euler_jet_variable_zero_order_remainder','direct_strain_kernel_rational_derivative','vector_symbol_numerator_identity']
def Q(v):v=fmpq(v);return iv.mpf(int(v.p))/int(v.q)
vk=Q(k);aa=(2-vk)/vk;dd=(4-vk)/vk;xx=Q(fmpq(43,5))-Q(eps);er=Q(M)*(Q(eps)**2+Q(high)**2)/2;cc=(dd*Q(low)*(Q(fmpq(51,5))*Q(eps)+er)+aa*xx*er)/(xx*Q(low));bb=aa*Q(fmpq(99,100))-cc

def ep(v):sign,man,exp,bc=v;return F((-1 if sign else 1)*man)*F(2)**exp
il,iu=map(ep,bb._mpi_);lo,hi=map(F,primary['strict_window']);assert lo<il<=F(str(bound))<=iu<hi
al,au=F(primary['arb512']['lower_exact']),F(primary['arb512']['upper_exact']);assert max(il,al)<=min(iu,au)
out={'start_utc':start,'utc':p.now(),'status':'PASS_SEPARATE_HEX_FMPQ_IV_AND_EULER_JET_CHECKS','proof_sha256':p.sha(P/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(primary['parent_files']),'exact_values_compared':len(actual),'exact_algebra_checks':identities,'iv220':{'lower_exact':str(il),'upper_exact':str(iu)},'strict_window':primary['strict_window'],'scope':'Independent arithmetic libraries and algebra construction; analytic Sobolev/sequence proof is not replaced by these finite checks.'};p.write(E/'independent.json',out);print(json.dumps(out))
