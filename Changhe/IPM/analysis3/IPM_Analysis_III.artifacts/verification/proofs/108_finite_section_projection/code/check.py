from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,importlib.util
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('angles',LANE/'proofs/98_exact_angular_norm/code/angular.py');A=importlib.util.module_from_spec(sp);sp.loader.exec_module(A)
ctx.prec=256;ctx.threads=1

def mat(N):
 m=[[F(0) for j in range(N-1)] for i in range(N+1)]
 for j in range(N-1):
  for delta,c in [(0,F(3,8)),(2,F(1,4)),(-2,F(1,4)),(4,F(1,16)),(-4,F(1,16))]:
   k=2*j+1+delta;sg=1 if k>0 else -1;i=(abs(k)-1)//2
   if i<=N:m[i][j]+=sg*c
 return m

def solve(m,b):
 n=len(b);m=[list(x)+[v] for x,v in zip(m,b)]
 for j in range(n):
  k=next(k for k in range(j,n) if m[k][j]);m[j],m[k]=m[k],m[j]
  piv=m[j][j];m[j]=[x/piv for x in m[j]]
  for k in range(n):
   if k!=j:
    fac=m[k][j]
    m[k]=[x-fac*y for x,y in zip(m[k],m[j])]
 return [x[-1] for x in m]

def sin_to_cos(v):return [sum(v)]+[2*sum(v[j:]) for j in range(1,len(v))]
def H(v):
 mm=A.moments(2*len(v));return sum((v[j]*v[l]*(mm[j+l]+mm[abs(j-l)])/2 for j in range(len(v)) for l in range(len(v))))
def rec(v):return {'ball':v.str(35),'lower_exact':str(v.lower().fmpq()),'upper_exact':str(v.upper().fmpq())}
out=[]
for N in [2,19]:
 full=mat(N+2);raw=[row[N-1] for row in full];g=raw[:N+1]
 gamma=-sum(((-1)**j*(2*j+1)**2*x for j,x in enumerate(g)),F(0))/2
 assert gamma==(-1)**(N+1)*F((2*N+3)**2,32)
 r=list(g);r[0]-=gamma/4;r[1]-=gamma/4;m=mat(N)
 mtm=[[sum((m[k][i]*m[k][j] for k in range(N+1)),F(0)) for j in range(N-1)] for i in range(N-1)]
 rhs=[sum((m[k][i]*r[k] for k in range(N+1)),F(0)) for i in range(N-1)]
 q=solve(mtm,rhs)
 hin=H([F(1)]+[F(2)]*(N-1));hout=H(sin_to_cos(q));mass=A.beta_mass()
 rr=A.aa(hout/hin);yr=(A.aa(gamma**2)+mass*A.aa(hout))/(mass*A.aa(hin))
 if N==2:assert q==[F(67,16)] and hin==F(69,77) and hout/hin==F(345653,17664)
 out.append({'N':N,'false_jet':str(gamma),'raw_truncated':list(map(str,g)),'quotient':list(map(str,q)),'input_H':str(hin),'output_H':str(hout),'remainder_ratio':rec(rr.sqrt()),'Y_ratio':rec(yr.sqrt())})
I0=2*(arb(1)/4).gamma()*(arb(1)/2).gamma()/(arb(3)/4).gamma();assert I0<arb('10.49')
record={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','I0':rec(I0),'cases':out,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'evidence/check.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
