from fractions import Fraction as F
from math import comb
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def mult(v,k):
 out=[F(0)]*(len(v)+k)
 for j,c in enumerate(v):
  for s in [-1,1]:
   f=2*j+1+s*2*k;sg=1 if f>0 else -1;out[(abs(f)-1)//2]+=sg*c/2
 return out
def m4(v):
 out=[F(0)]*(len(v)+2)
 for j,x in enumerate(v):out[j]+=3*x/8
 for j,x in enumerate(mult(v,1)):out[j]+=x/2
 for j,x in enumerate(mult(v,2)):out[j]+=x/8
 return out
def exact_input(m):
 p=[F(1,4),F(1,4)];g=mult(p,m)
 for j,c in enumerate(p):g[j]-=(-1)**m*c
 return g
def inverse(g):
 n=len(g)
 return [16*sum(((-1)**k*comb(k+3,3)*g[j+2+k] for k in range(n-2-j)),F(0)) for j in range(n-2)]
for m in range(1,65):
 q=[F(2*(-1)**(m-1-j)*(2*m-2*j-1)) for j in range(m)]
 g=exact_input(m);assert m4(q)==g;assert inverse(g)==q
 assert sum(abs(x) for x in q)==2*m*m
 assert sum(x*x for x in q)==F(4*m*(4*m*m-1),3)
for n in [3,4,5,10,31,64]:
 q=[F((-1)**j*(j*j+1),j+1) for j in range(n-2)];assert inverse(m4(q))==q
# Q_m = sum_p poly[m][p] sin(theta)^(2p+1).
poly=[[2], [0,-8], [2,-16,32]]
I=[F(1)]
for p in range(6):I.append(I[-1]*F(4*p+2,4*p+3))
Gram=[[sum((F(a*b)*I[i+j+1] for i,a in enumerate(x) for j,b in enumerate(y)),F(0)) for y in poly] for x in poly]
assert Gram[0][1]/Gram[0][0]==F(-24,7)
assert Gram[1][1]/Gram[0][0]==F(960,77)
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','input_modes_checked':list(range(1,65)),'generic_inverse_lengths':[3,4,5,10,31,64],'first_three_gram_over_I0':[[str(v) for v in row] for row in Gram],'error_constants':{str(n):{'infinity':16*comb(n+1,4),'l1':16*comb(n+2,5)} for n in [531,533,535]},'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'evidence/check.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
