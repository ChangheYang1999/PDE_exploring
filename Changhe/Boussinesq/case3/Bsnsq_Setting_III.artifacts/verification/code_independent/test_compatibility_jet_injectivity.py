"""Independent Cartesian rational check of packet138. No NUM/fitting imports."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys,time,hashlib
from exact_bivariate import add,scale,mul,diff,lap,dot_grad,trunc,homogeneous,serialize
from constrained_primitive_certificate import jet_from_state

root=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
tic=time.perf_counter();controls=[];rows=[]
def residual_operator_M(W,t,beta,D):
    J=diff(W[1],0);Jy=diff(J,1);Wy=diff(W[1],1);k=Q(beta)-2
    return add(mul(mul(J,J,D),diff(t,1),D),
        scale(mul(mul(J,W[1],D),diff(diff(t,0),1),D),-1),
        mul(add(mul(W[1],Jy,D),mul(J,add({(0,0):k},scale(Wy,-1)),D)),diff(t,0),D))
def from_stream(psi,beta,D):
    psi=dict(psi);psi.pop((1,0),None);omega=scale(lap(psi),-1)
    W=(add({(1,0):beta},scale(diff(psi,1),-1)),add({(0,1):beta},diff(psi,0)))
    F=add(dot_grad(W,omega,D),omega)
    theta={(i+1,j):a/Q(i+1)for(i,j),a in F.items()}
    t=add(dot_grad(W,theta,D),scale(theta,-(beta-2)))
    J=diff(W[1],0);D0=add(mul(add({(0,0):beta-2},scale(diff(W[0],0),-1)),F,D),scale(dot_grad(W,F,D),-1))
    Z=add(mul(mul(W[0],J,D),F,D),mul(W[1],D0,D))
    E=add(mul(J,diff(Z,1),D),scale(mul(Z,diff(J,1),D),-1),scale(mul(J,D0,D),-(beta-2)))
    return W,t,E

# Differentiate generic higher jets with exact rational coefficients, independently
# of the numerical source construction. Include beta2 and both signs of j1.
for beta in [Q(1),Q(2),Q(9,4),Q(7,2)]:
 for p in [Q(2,7),Q(-3,11)]:
  c=1+beta/2;j1=6*p;lam2=1+3*beta/2;k=beta-2
  psi={(1,1):c,(3,0):p,(1,2):Q(4,9),(3,1):Q(2,5),(1,3):Q(-7,4),(1,4):Q(1,3)}
  W=(add({(1,0):beta},scale(diff(psi,1),-1)),add({(0,1):beta},diff(psi,0)))
  for N in range(2,8):
   t={(a,N-a):Q(a+N,3*a+1)for a in range(2,N+1,2)}
   t[(2,N)]=Q(13,17)  # arbitrary later term cannot change degree N
   result=trunc(residual_operator_M(W,t,beta,N+2),N)
   expected={(a,b):-j1*a*(lam2*(b+1)-k)*v for(a,b),v in t.items()if a+b==N}
   assert result==expected and result
   controls.append({'beta':str(beta),'j1':str(j1),'degree':N,'passed':True})

for path in sorted(root.glob('fixed*_n6_J6_state.json')):
 state=json.loads(path.read_text());beta=Q(state['beta']);psi=jet_from_state(state,11)
 j1=6*psi.get((3,0),Q(0));assert j1
 W,t,E=from_stream(psi,beta,11);t=trunc(t,6);E=trunc(E,6)
 assert t and not trunc(t,4)
 assert all(a>=2 and a%2==0 for a,b in t)
 N=min(a+b for a,b in t);tn=homogeneous(t,N);en=homogeneous(E,N)
 assert not trunc(E,N-1)
 predicted={(a,b):-j1*a*((1+3*beta/2)*(b+1)-(beta-2))*v for(a,b),v in tn.items()}
 assert en==predicted and en
 # Evaluate E from its defining polynomial and M from the separate residual route.
 M=trunc(residual_operator_M(W,t,beta,8),N)
 assert M==en
 row={'state':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'beta':str(beta),'j1':str(j1),
      'first_nonzero_thermal_degree':N,'first_nonzero_compatibility_degree':N,
      'thermal_leading_coefficients':serialize(tn),'compatibility_leading_coefficients':serialize(en),
      'direct_E_equals_predicted':True,'verdict':'REFUTED_ANY_LOCAL_TEMPERATURE_FOR_THIS_ANALYTIC_STREAM',
      'scope':'The specified analytic W/Omega cannot solve both transport equations on any nonempty open set. No exclusion of a nearby stream or the broad class.'}
 (out/(path.stem+'_compatibility.json')).write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'ALL_EXACT_CONTROLS_PASSED','elapsed_seconds':time.perf_counter()-tic,'manufactured_control_count':len(controls),'controls':controls,'states':rows}
(out/'tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'],result['elapsed_seconds'],'controls',len(controls),'states',len(rows),flush=True)
for row in rows:print(row['state'],'j1',float(Q(row['j1'])),'first_degree',row['first_nonzero_thermal_degree'],flush=True)
