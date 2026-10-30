from pathlib import Path
from collections import defaultdict
from datetime import datetime,timezone
import json,hashlib,time,sys
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
sys.set_int_max_str_digits(0)
ctx.prec=512
name=sys.argv[1]
assert name == "C1-N1-005-d2w-j7-x3"
root=Path(__file__).resolve().parents[1]
T=Poly([0,1]);U=Poly([1,-1]);Z=Poly([])
def put(A,key,P):
 j,n=key
 if n==0:return
 if n<0:n,P=-n,-P
 A[j,n]=A.get((j,n),Z)+P
 if not A[j,n]:del A[j,n]
def divide_t(P,k):
 assert all(P[i]==0 for i in range(k))
 return Poly(list(P)[k:])
def radial(P,p,d):return (2*p*T-d)*P+2*T*U*P.derivative()
def td(P,a):return (1-2*a*T)*P+2*T*U*P.derivative()
def beta(m,v):
 assert m>=1 and v>0
 z=1/v
 for k in range(1,m):z*=Q(k)/(k+v)
 return z
def integrate(P,start,v):return sum((a*beta(k+start,v) for k,a in enumerate(P)),Q(0))
def inner(A,B,exps,grad=False):
 ans=Q(0)
 for (j,n),P in A.items():
  for (k,m),S in B.items():
   if n!=m:continue
   b,c=exps[j],exps[k]
   if grad:ans+=integrate(td(P,b)*td(S,c)+n*n*P*S,1,b+c-1)
   else:ans+=integrate(P*S,2,b+c-2)
 return ans
def ar(q):return arb(q.numerator)/arb(q.denominator)
start=time.monotonic();p=root/'data'/f'{name}_canonical.json';a=json.loads(p.read_text());c=Q(a['cl']);gamma=1/c;delta=1-gamma
pot={}
for (j,m,k),v in zip(a['order'],a['coefficients']):
 key=j,2*m
 pot.setdefault(key,[]);pot[key]+=[Q(0)]*max(0,k+1-len(pot[key]));pot[key][k]+=Q(v)
rho={}
for (j,n),coeffs in pot.items():
 P=Poly(coeffs);power=(3+gamma-j*delta)/2
 B=radial(radial(P,power,0),power,0)-n*n*P
 E=radial(B,power,2)
 put(rho,(j,n-1),(E+n*B)/2);put(rho,(j,n+1),-(E-n*B)/2)
rho={k:divide_t(P,2) for k,P in rho.items()}
exps={j:(j+1)*delta/2+1 for j,n in rho};lap={};difference={}
for (j,n),P in rho.items():
 a=exps[j]-1
 put(lap,(j,n),divide_t(td(td(P,a),a)-n*n*P,1))
 lower=td(P,a)+n*P;lower=td(lower,a)+(n-2)*lower
 upper=td(P,a)-n*P;upper=td(upper,a)-(n+2)*upper
 put(difference,(j,n-2),divide_t(lower,1)/2);put(difference,(j,n+2),divide_t(upper,1)/2)
xx={k:(lap.get(k,Z)+difference.get(k,Z))/2 for k in set(lap)|set(difference)}
yy={k:(lap.get(k,Z)-difference.get(k,Z))/2 for k in set(lap)|set(difference)}
assert all(xx[k]+yy[k]==lap.get(k,Z) for k in xx)
values={'D2rho':inner(lap,lap,exps),'D3rho':inner(lap,lap,exps,True),
        'D_rho_x':inner(xx,lap,exps),'D_rho_y':inner(yy,lap,exps)}
reference=root/'source'/f'N4_{name}.json';old=json.loads(reference.read_text());out={}
for norm_name,v in values.items():
 assert v>0
 assert v==Q(old['norms'][norm_name]['unweighted_rational_sum']),norm_name
 norm=(arb.pi()/2*ar(v)).sqrt()
 out[norm_name]={'rational_energy_over_pi_half':str(v),'norm':norm.str(65),'exact_N4_rational_agreement':True}
 assert norm.overlaps(arb(old['norms'][norm_name]['norm_upper_ball']))
 print(norm_name,norm.str(40),flush=True)
assert values['D_rho_x']+values['D_rho_y']==values['D2rho']
hs=((arb(2).log()-arb(1)/2)*ar(values['D_rho_x'])+(3*arb(2).log()-2)*ar(values['D_rho_y']))/32
hs=hs.sqrt();assert hs.overlaps(arb(old['gradient_identity_conditional_HS_upper']))
result={'candidate':name,'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'N4_target_sha256':hashlib.sha256(reference.read_bytes()).hexdigest(),'precision_bits':ctx.prec,
 'method':'Direct radial Laplacian of the canonical potential; Hessian integration-by-parts identities; rational beta recurrence',
 'norms':out,'gradient_HS_norm':hs.str(65),'elapsed_seconds':time.monotonic()-start}
(root/'verification'/f'{name}_reproduction.json').write_text(json.dumps(result,indent=2)+'\n')
print('HS',hs.str(45),'elapsed',result['elapsed_seconds'])
