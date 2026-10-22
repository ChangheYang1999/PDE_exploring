"""Independent P308 exact rational triangular recurrence. No teammate imports."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
N=44

def p(d=None):
 d=d or {};return [F(d.get(i,0)) for i in range(N+1)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sc(a,k):return [k*x for x in a]
def mul(a,b):
 out=p()
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N+1-i]):
    if y:out[i+j]+=x*y
 return out
def der(a):return [(i+1)*a[i+1]if i<N else F(0)for i in range(N+1)]
def shift(a,k):return p({i+k:x for i,x in enumerate(a)if 0<=i+k<=N})
def inv(a):
 out=p({0:1/a[0]})
 for i in range(1,N+1):out[i]=-sum((a[j]*out[i-j]for j in range(1,i+1)),F(0))/a[0]
 return out
def integ(a):return [F(0)]+[a[i-1]/i for i in range(1,N+1)]
def exp(a):
 assert a[0]==0;out=p({0:1})
 for i in range(1,N+1):out[i]=sum((j*a[j]*out[i-j]for j in range(1,i+1)),F(0))/i
 return out
def power(a,n):
 out=p({0:1})
 for _ in range(n):out=mul(out,a)
 return out

def evaluate(C,k,E,Fhom,checks=None):
 """E is free coefficient of theta2/Ztheta2; Fhom of omega1/Zomega1."""
 H=-k**7/231;alpha=-C*k/260
 B=p({1:1,2:k,13:alpha});P=shift(B,-1);Bd=der(B);Pi=inv(P)
 tq=mul(add(p({0:8}),sc(Bd,2)),Pi);yq=mul(add(p({0:5}),Bd),Pi)
 tau=exp(integ(shift(tq,-1)));rho=exp(integ(shift(yq,-1)))
 v=[B];theta=[p(),shift(sc(tau,C/2),10)];omega=[]
 T=sc(theta[1],2)
 eta=mul(shift(rho,6),add(p({0:H}),sc(integ(shift(mul(mul(tau,Pi),inv(rho)),3)),-C)))
 omega.append(eta);v.append(sc(add(eta,der(der(B))),F(-1,2)))
 results={}
 def solve(rhs,zeta,m,h,name,a):
  Q=mul(rhs,inv(mul(P,zeta)));residue=Q[m]
  primitive=p({i:c/F(i-m)for i,c in enumerate(Q)if i!=m});primitive[m]=h
  out=mul(zeta,primitive)
  if checks is not None:
   lhs=add(mul(B,der(out)),sc(mul(a,out),-1));defect=add(lhs,sc(rhs,-1));predicted=sc(shift(mul(P,zeta),m),-residue)
   checks.append(dict(name=name+'_ode_defect',passed=defect[:35]==predicted[:35]))
  results[name]=residue
  return out
 for l in [2,3]:
  rhs=p()
  for a in range(1,l):rhs=add(rhs,add(sc(mul(der(v[a]),theta[l-a]),F(2*(l-a),2*a+1)),sc(mul(v[a],der(theta[l-a])),-1)))
  theta.append(solve(rhs,power(tau,l),10*l,E if l==2 else F(0),'theta'+str(l),add(p({0:(4*l-1)*2+2}),sc(Bd,2*l))))
  j=l-1;rhs=sc(theta[j+1],-2*j-2)
  for a in range(1,j+1):rhs=add(rhs,add(sc(mul(der(v[a]),omega[j-a]),F(2*(j-a)+1,2*a+1)),sc(mul(v[a],der(omega[j-a])),-1)))
  omega.append(solve(rhs,mul(power(tau,j),rho),10*j+6,Fhom if j==1 else F(0),'omega'+str(j),add(p({0:(2*j+1)*4+1}),sc(Bd,2*j+1))))
  v.append(sc(add(omega[j],sc(der(der(v[j])),F(1,2*j+1))),F(-1,2*j+2)))
 if checks is not None:
  checks.append(dict(name='theta1_equation',passed=add(mul(B,der(T)),sc(mul(add(p({0:8}),sc(Bd,2)),T),-1))[:35]==p()[:35]))
  checks.append(dict(name='omega0_equation',passed=add(add(mul(B,der(eta)),sc(mul(add(p({0:5}),Bd),eta),-1)),T)[:35]==p()[:35]))
  checks.append(dict(name='prior_two_residues_zero',passed=results['theta2']==results['omega1']==0))
 return results

if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[];records=[]
 for C,k in [(F(1),F(-1)),(F(1),F(1)),(F(2),F(-1)),(F(1),F(-2)),(F(3),F(-1,2)),(F(-2),F(3,2))]:
  basis=[]
  for E,G in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(2),F(-3))]:
   ch=[];r=evaluate(C,k,E,G,ch)
   for c in ch:c['name']=f'C{C}_k{k}_E{E}_F{G}_'+c['name']
   checks.extend(ch);basis.append([r['theta3'],r['omega2']])
  r0,rE,rF,test=basis;a=[rE[i]-r0[i]for i in range(2)];b=[rF[i]-r0[i]for i in range(2)]
  checks.append(dict(name=f'C{C}_k{k}_affine_check',passed=test==[r0[i]+2*a[i]-3*b[i]for i in range(2)]))
  det=a[0]*b[1]-a[1]*b[0]
  expected_a=[12*C*k/25,-9*k**8/1925];expected_b=[F(0),-9*C*k/20]
  for i in range(2):
   checks.append(dict(name=f'C{C}_k{k}_proved_E_entry{i}',passed=a[i]==expected_a[i]))
   checks.append(dict(name=f'C{C}_k{k}_proved_F_entry{i}',passed=b[i]==expected_b[i]))
  checks.append(dict(name=f'C{C}_k{k}_proved_determinant',passed=det==-27*C**2*k**2/125))
  solution=None
  if det:
   E=(-r0[0]*b[1]+r0[1]*b[0])/det;G=(-a[0]*r0[1]+a[1]*r0[0])/det
   ch=[];testsol=evaluate(C,k,E,G,ch);checks.extend(dict(name=f'C{C}_k{k}_tuned_'+x['name'],passed=x['passed']) for x in ch);checks.append(dict(name=f'C{C}_k{k}_solved_both',passed=testsol['theta3']==testsol['omega2']==0));solution=dict(E=str(E),F=str(G))
  records.append(dict(C=str(C),k=str(k),constant=list(map(str,r0)),E_coeff=list(map(str,a)),F_coeff=list(map(str,b)),determinant=str(det),solution=solution))
  print(json.dumps(records[-1]),flush=True)
 V=Path('research/308_next_two_curved_resonances/verification');fr=json.loads((V/'freeze.json').read_text());checks.append(dict(name='proof_precedes_calculation',passed=fr['utc']<start));checks.append(dict(name='preparation_proof_hash',passed=hashlib.sha256((V/'PROOF_preparation.md').read_bytes()).hexdigest()==fr['proof_sha256']))
 ext=json.loads((V/'general_matrix_extension_preregister.json').read_text());checks.append(dict(name='general_matrix_proof_precedes_extension',passed=ext['utc']<start));checks.append(dict(name='complete_general_matrix_proof_hash',passed=hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==ext['proof_sha256']))
 out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,N=N,passed=sum(c['passed']for c in checks),total=len(checks),checks=checks,records=records,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact rational checks of six C,k samples against the arbitrary-parameter matrix proved in PROOF.md; samples are checks, not a proof of the general theorem.')
 (V/'fraction_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['checks','records']},indent=2));print('FAILED',[c for c in checks if not c['passed']])
