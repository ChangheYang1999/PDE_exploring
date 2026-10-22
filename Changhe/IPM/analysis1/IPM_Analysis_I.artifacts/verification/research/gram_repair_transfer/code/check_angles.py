from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import factorial
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_repair_transfer';R=B/'research/gram_conforming_repair'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
v=read(R/'evidence/verdict.json');proof=R/'PROOF.md';check(v['files'][str(proof.relative_to(B))]==sha(proof),'132 proof membership')
text=proof.read_text();check('uniformly for every single angular mode m' in text and '[(A0+A1)B^2+A0(3B+B\')^2]' in text and 'A0<=A0+A1' in text,'explicit132angularscope')
# Engine1: signed sine frequencies.
one=[]
for m in range(24):
 c={}
 for n in [1+2*m,1-2*m,3+2*m,3-2*m]:
  if n:c[abs(n)]=c.get(abs(n),F(0))+F(1 if n>0 else -1,8)
 a0=sum((q*q for q in c.values()),F(0));a1=sum((n*n*q*q for n,q in c.items()),F(0));one.append((a0,a1))
# Engine2: polynomial recurrence and beta moments; does not read sine output.
def add(a,b):return [ (a[j] if j<len(a) else F(0))+(b[j] if j<len(b) else F(0)) for j in range(max(len(a),len(b)))]
def mul(a,b):return [sum((a[j]*b[k-j] for j in range(len(a)) if 0<=k-j<len(b)),F(0)) for k in range(len(a)+len(b)-1)]
def deriv(a):return [F(j)*a[j] for j in range(1,len(a))]
def moment(p,q):return F(2*factorial(2*p)*factorial(2*q),4**(p+q)*factorial(p)*factorial(q)*factorial(p+q))
polys=[[F(1)],[F(0),F(1)]]
for j in range(2,47):polys.append(add([F(0)]+[2*q for q in polys[-1]],[-q for q in polys[-2]]))
two=[]
for m in range(24):
 p=[F(0),F(0)]+polys[2*m];a=mul(p,p);dp=deriv(p);c=add([F(0)]+p,[-q for q in dp]);c=add(c,[F(0),F(0)]+dp);cc=mul(c,c)
 check(all(q==0 for j,q in enumerate(a) if j%2) and all(q==0 for j,q in enumerate(cc) if j%2),'even squares')
 two.append((sum((q*moment(j//2,1) for j,q in enumerate(a) if j%2==0),F(0)),sum((q*moment(j//2,0) for j,q in enumerate(cc) if j%2==0),F(0))))
check(one==two,'independent angular integrals');rows=[]
for m,(a0,a1) in enumerate(one):
 check(a0>0 and a1>0 and a0<=a0+a1,'positivity');rows.append({'m':m,'A0_over_pi_exact':str(a0),'A1_over_pi_exact':str(a1),'A0_fraction_of_sum_exact':str(a0/(a0+a1))})
files={str(p.relative_to(B)):sha(p) for p in [proof,R/'evidence/verdict.json',D/'ANGLE_SCOPE.md',Path(__file__)]}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL24_ANGULAR_ENERGIES_BY_SINE_AND_CHEBYSHEV_BETA_METHODS','rows':rows,'files':files,'scope':'Full angular derivative included and uniform cancellation valid; no actual Gram or gamma claim.'}
p=D/'evidence/angles.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'mode_count':len(rows),'sample_rows':[rows[j] for j in [0,1,2,23]]}))
