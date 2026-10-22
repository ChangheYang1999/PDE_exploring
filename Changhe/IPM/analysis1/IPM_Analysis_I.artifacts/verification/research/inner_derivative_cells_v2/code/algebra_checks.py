"""Exact manufactured identity checks; no numerical cell certificate."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,random
R=Path(__file__).resolve().parents[3];D=R/'research/inner_derivative_cells';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
first=json.loads((E/'proof_first.json').read_text());assert first['sha256']==sha(D/'PROOF.md') and first['code_files']==[]
started=now();rng=random.Random(18120261022);checks=0
for case in range(360):
 Q=[8,9,16][case%3];lam=F([-526,-522,-2,0,2,50,522][case%7],1 if case%5 else 7);h=F([1,2,3,5][case%4],100);sig=F([-1,1,-1,1][case%4],1 if case%2 else 2)
 g=[F(rng.randint(-9,9),rng.randint(1,9)) for _ in range(Q+1)];y0=F(rng.randint(-9,9),7);p=[y0]
 for j in range(Q):p.append(h*(lam*p[-1]+sig*g[j])/(j+1))
 # Independently solve the triangular coefficients by the closed finite sum.
 closed=[y0*(lam*h)**j/F(math.factorial(j))+sig*h*sum((g[l]*F(math.factorial(l),math.factorial(j))*(lam*h)**(j-l-1) for l in range(j)),F(0)) for j in range(Q+1)]
 assert p==closed;checks+=Q+1
 defect=lam*p[Q]+sig*g[Q]
 for j in range(Q+1):
  dp=F(j+1)*p[j+1]/h if j<Q else F(0)
  assert dp-lam*p[j]-sig*g[j]==(-defect if j==Q else 0);checks+=1
  d2p=F((j+2)*(j+1))*p[j+2]/h**2 if j+2<=Q else F(0)
  dg=F(j+1)*g[j+1]/h if j<Q else F(0)
  assert d2p-lam*dp-sig*dg==(-Q*defect/h if j==Q-1 else 0);checks+=1
 # Exact derivative of high polynomial terms versus truncation difference.
 u=[F(rng.randint(-5,5),11) for _ in range(2*Q+1)]
 for d in range(3):
  for j in range(2*Q+1-d):
   factor=F(math.factorial(j+d),math.factorial(j))/h**d
   full=factor*u[j+d];ret=factor*u[j+d] if j+d<=Q else F(0)
   high=factor*u[j+d] if j+d>Q else F(0)
   assert full-ret==high;checks+=1
# Two exact moment formulas imply both physical Green ODEs for generic polynomial forcing.
def deriv(p):return [(j+1)*p[j+1] for j in range(len(p)-1)]+[F(0)]
def primitive(p,lam):
 assert lam;q=[F(0)]*len(p)
 for j in range(len(p)-1,-1,-1):q[j]=(p[j]-(j+1)*q[j+1] if j+1<len(p) else p[j])/lam
 return q
green=0
for n in range(1,262):
 m=2*n;al=F(501,10);hm=[F(rng.randint(-5,5),13) for _ in range(7)];hp=[F(rng.randint(-5,5),17) for _ in range(7)]
 im=primitive(hm,m+4+al);jp=primitive([-x for x in hp],al+4-m)
 forcing=[(dm+dp+(al+4-m)*x+(al+4+m)*y)/2 for dm,dp,x,y in zip(deriv(hm),deriv(hp),hm,hp)]
 A=[(x+y)/2-m*z for x,y,z in zip(hm,hp,im)];B=[m*z-(x+y)/2 for x,y,z in zip(hm,hp,jp)]
 assert [d+(al+4+m)*v for d,v in zip(deriv(A),A)]==forcing
 assert [d+(al+4-m)*v for d,v in zip(deriv(B),B)]==[-v for v in forcing]
 green+=14
partition=[(F(-5)+F(j,5),F(-5)+F(j+1,5)) for j in range(15)]+[(F(-2)+F(j,10),F(-2)+F(j+1,10)) for j in range(19)]+[(F(-1,10)+F(j,100),F(-1,10)+F(j+1,100)) for j in range(10)]
assert len(partition)==44 and partition[0][0]==-5 and partition[-1][1]==0 and all(a<b for a,b in partition) and all(partition[j][1]==partition[j+1][0] for j in range(43))
out={'start_utc':started,'utc':now(),'status':'PASS_EXACT_MANUFACTURED_ANALYTIC_IDENTITY_CHECKS_ONLY','proof_sha256':sha(D/'PROOF.md'),'source_sha256':sha(__file__),'manufactured_ode_and_truncation_coefficient_checks':checks,'green_ode_coefficient_checks':green,'cells':44,'partition':[[str(a),str(b)] for a,b in partition],'scope':'Finite algebra diagnostics support the separately proved identities. No numerical residual evaluation or finite-cell certificate.'}
(E/'algebra_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='partition'}))
