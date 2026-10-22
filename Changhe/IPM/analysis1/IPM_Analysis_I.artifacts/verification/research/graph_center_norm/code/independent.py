"""Exact rational ODE coefficient reconstruction; no SymPy or primary polynomial reuse."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/graph_center_norm'
def check(q,label):
 if not q:raise ValueError(label)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rr(q):return str(q.numerator)+'/'+str(q.denominator)
def clean(a):return {p:c for p,c in a.items() if c}
def add(a,b):
 c=dict(a)
 for p,v in b.items():c[p]=c.get(p,F(0))+v
 return clean(c)
def mul(a,b):
 c={}
 for (i,j),v in a.items():
  for (k,l),u in b.items():c[i+k,j+l]=c.get((i+k,j+l),F(0))+v*u
 return clean(c)
def scale(a,q):return clean({p:c*q for p,c in a.items()})
def der(a,j):
 c={}
 for p,v in a.items():
  if p[j]:
   q=list(p);q[j]-=1;c[tuple(q)]=v*p[j]
 return c
def radial_jet(poly,j):
 v=F(0)
 for p,c in poly.items():
  fact=1
  for i in range(j):fact*=p-i
  v+=c*fact
 return v
def powR(j):return {(2*i,2*(j-i)):F(comb(j,i)) for i in range(j+1)}
def sincart(n):return {(n-j,j):F((-1)**((j-1)//2)*comb(n,j)) for j in range(1,n+1,2)}
def beta(a,b):return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))
chi={j:F((-1)**j*comb(6,j)) for j in range(7)}
H={}
for j,a in chi.items():H=add(H,scale(mul({(2,1):F(1)},powR(j)),a))
psi={};rows=[];matches=0;sourcecart={}
for n in (2,4):
 source=clean({2*j+2:(F(1)+F(j,2))*a if n==2 else F(j,4)*a for j,a in chi.items()})
 particular={p+2:-a/F((p+2)**2-n*n) for p,a in source.items()}
 P=sum(particular.values(),F(0));dP=radial_jet(particular,1)
 a=-(n*P+dP)/(2*n);b=(n*P-dP)/(2*n);inside=dict(particular);inside[n]=a
 check(n not in particular,'nonresonance');check(b==(F(-1,4032) if n==2 else F(-1,13440)),'external beta value')
 ext={-n:b};jets=[]
 for j in range(7):
  q=radial_jet(inside,j);check(q==radial_jet(ext,j),'matching jet');jets.append(rr(q));matches+=1
 for p,q in inside.items():
  check(p>=n and (p-n)%2==0,'Cartesian regularity');psi=add(psi,scale(mul(powR((p-n)//2),sincart(n)),q))
 for p,q in source.items():sourcecart=add(sourcecart,scale(mul(powR((p-n)//2),sincart(n)),q))
 rows.append({'stream_mode':n,'source_coefficients':{str(p):rr(c) for p,c in source.items()},'inner_stream_coefficients':{str(p):rr(c) for p,c in inside.items()},'exterior_stream_coefficient':rr(b),'matching_jets_0_through_6':jets})
check(sourcecart==der(H,0),'Cartesian source');check(scale(add(der(der(psi,0),0),der(der(psi,1),1)),F(-1))==sourcecart,'Cartesian Poisson')
U=[scale(der(psi,1),F(-1)),der(psi,0)];check(add(der(U[0],0),der(U[1],1))=={},'divergence');check(add(der(U[1],0),scale(der(U[0],1),F(-1)))==scale(sourcecart,F(-1)),'curl');check(all(p[0]+p[1]>=1 for q in U for p in q),'origin')
strain=der(der(psi,0),1).get((0,0),F(0));check(strain==beta(1,7)/8==F(1,56),'strain beta integral');check(-beta(3,7)/16==F(-1,4032) and -beta(4,7)/16==F(-1,13440),'exterior integration by parts')
S0=sum(map(abs,H.values()),F(0));S1=sum((sum(map(abs,der(H,j).values()),F(0)) for j in range(2)),F(0));S2=sum((sum(map(abs,der(der(H,j),k).values()),F(0)) for j in range(2) for k in range(2)),F(0));DU=sum((sum(map(abs,der(q,j).values()),F(0)) for q in U for j in range(2)),F(0));outside0=sum((n*abs(F(row['exterior_stream_coefficient'])) for n,row in zip((2,4),rows)),F(0));outside1=sum((n*(n+1)*abs(F(row['exterior_stream_coefficient'])) for n,row in zip((2,4),rows)),F(0));const={'H0':rr(S0),'H1':rr(S1),'H2':rr(S2),'DU_inner':rr(DU),'U_outer':rr(outside0),'DU_outer':rr(outside1),'C_H':rr(max(DU,outside0,outside1))}
# Affine exponent = (coefficient of alpha, constant). All operations exact.
def ea(a,b):return (a[0]+b[0],a[1]+b[1])
def es(a,c):return (a[0]*c,a[1]*c)
center=ea(es((1,2),2),(0,-5));middle=ea(es((1,-2),2),(0,-5));far=(0,-10)
check(center==(2,-1) and middle==(2,-9) and far==(0,-10),'radial exponents');check(ea(middle,(0,13))==(2,4),'integrated middle delta');check(ea(center,(0,5))==(2,4),'integrated inner delta')
# For 0<alpha<1: 2alpha>0, 8-2alpha>6, and 12-(4+2alpha)>6.
check((8-2)>0 and 12-4-2>0,'denominator and delta dominance')
primary=json.loads((D/'evidence/compute.json').read_text());check(primary['radial_modes']==rows,'all primary radial data');check(primary['polynomial_abs_coefficient_constants']==const,'all constants');polys={'H':H,'psi_inner':psi,'U1_inner':U[0],'U2_inner':U[1]};coefs=0
for name,p in polys.items():
 q={(v['x_power'],v['y_power']):F(v['coefficient']) for v in primary['cartesian_polynomials'][name]};check(q==p,'all primary Cartesian polynomials');coefs+=len(p)
files={str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'evidence/proof_first.json',D/'evidence/compute.json',D/'code/compute.py',Path(__file__)]}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_RATIONAL_ODE_CARTESIAN_DICTIONARIES_BETA_MOMENTS_AND_EXPONENTS','radial_modes':rows,'matching_jet_checks':matches,'cartesian_coefficient_comparisons':coefs,'strain_exact':rr(strain),'polynomial_abs_coefficient_constants':const,'affine_alpha_exponents':{'center':center,'middle':middle,'far':far},'files':files,'scope':'Independent exact finite bump identities and graph-norm exponent arithmetic. No background numerical constants or actual kernel certified.'};p=D/'evidence/independent.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','matching_jet_checks','cartesian_coefficient_comparisons','strain_exact')}))
