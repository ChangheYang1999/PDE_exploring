from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
N=5
p=[(0,0),(3,4),(4,3),(-3,4),(5,12)]
r=[0,5,5,5,13]
z=[[F(0) for j in range(N)] for i in range(N)]
def plus(a,b):return [[a[i][j]+b[i][j] for j in range(N)] for i in range(N)]
def minus(a,b):return [[a[i][j]-b[i][j] for j in range(N)] for i in range(N)]
def scale(a,s):return [[s*a[i][j] for j in range(N)] for i in range(N)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def tr(a):return [[a[j][i] for j in range(N)] for i in range(N)]
def comm(a,b):return minus(mul(a,b),mul(b,a))
def diag(a):return [[a[i] if i==j else F(0) for j in range(N)] for i in range(N)]
S=[diag([F(p[i][v],r[i]) if r[i] else F(0) for i in range(N)]) for v in range(2)]
B=[[None,None],[None,None]]
for i,j,c in ((0,0,1),(0,1,2),(1,1,3)):
 B[i][j]=[[F((a+b+c)%7-3,1+a+b+c) for b in range(N)] for a in range(N)]
 B[j][i]=B[i][j]
C=z;TB=z;DB=z
for i in range(2):
 for j in range(2):
  C=plus(C,mul(B[i][j],mul(S[i],S[j])))
  TB=plus(TB,mul(S[i],mul(B[i][j],S[j])))
  DB=plus(DB,comm(S[i],comm(S[j],B[i][j])))
assert scale(plus(C,tr(C)),F(1,2))==plus(TB,scale(DB,F(1,2)))
b=[[F(1+i+j,1+i*i+j*j) for j in range(N)] for i in range(N)]
P0=diag([F(1),F(0),F(0),F(0),F(0)])
D=z;T=z
for s in S:
 D=plus(D,comm(s,comm(s,b)))
 T=plus(T,mul(s,mul(b,s)))
assert T==minus(minus(b,scale(plus(mul(P0,b),mul(b,P0)),F(1,2))),scale(D,F(1,2)))
for i in range(1,N):
 for j in range(1,N):
  d2=sum((F(p[i][v],r[i])-F(p[j][v],r[j]))**2 for v in range(2))
  q2=sum((p[i][v]-p[j][v])**2 for v in range(2))
  assert d2==F(q2-(r[i]-r[j])**2,r[i]*r[j])
  assert d2<=F(q2,25)
path=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','arithmetic':'exact Fraction rational','dimension':N,'checks':['symmetric matrix double commutator','scalar sum and zero-mode terms','high-high direction identity and bound'],'proof_sha256':hashlib.sha256((path/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(path/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(o['date'],o['status'])
