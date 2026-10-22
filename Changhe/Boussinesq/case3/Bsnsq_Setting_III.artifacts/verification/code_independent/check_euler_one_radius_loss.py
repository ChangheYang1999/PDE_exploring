"""Exact scalar controls for P361; independent sparse monomial arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
R=Path('research/361_euler_one_radius_loss');V=R/'verification';start=datetime.now(timezone.utc);tick=time.monotonic();C=[]
def ck(n,b):C.append(dict(name=n,passed=bool(b)))
def norm(f,r):return sum((abs(c)*r**j for j,c in f.items()),Q(0))
def op(f,m):return {j-2:Q(j*(j-1),j-m-2)*c for j,c in f.items()if j>=2 and j!=m+2 and c}
p=json.loads((V/'preparation.json').read_text());ck('proof_prepared',p['prepared_utc']<start.isoformat());ck('proof_hash',p['proof_sha256']==hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest())
for m in [0,1,2,6,10,26,100]:
 for rho in [Q(1,2),Q(1),Q(2)]:
  for q in [Q(1,10),Q(1,2),Q(9,10),Q(99,100)]:
   r=rho*q;bound=1/(rho*(rho-r))+Q((m+2)**2)/rho**2
   for j in sorted(set([0,1,2,m+1,m+2,m+3,m+100,m+1000])):
    f={j:rho**(-j)};ck(f'm{m}_rho{rho}_q{q}_j{j}',norm(op(f,m),r)<=bound*norm(f,rho))
   f={j:Q((-1)**j*(j+1),j+2)*rho**(-j)for j in range(m+15)}
   ck(f'm{m}_rho{rho}_q{q}_dense',norm(op(f,m),r)<=bound*norm(f,rho))
  ck(f'm{m}_rho{rho}_resonance_removed',op({m+2:Q(1)},m)=={})
  for j in [m+3,m+10,m+100,m+1000]:
   q=Q(j-1,j);f={j:rho**(-j)};v=norm(op(f,m),rho*q)
   ck(f'm{m}_rho{rho}_lower{j}',norm(f,rho)==1 and j-2!=m and v>=Q(j-1,3)/rho**2)
   ck(f'm{m}_rho{rho}_geometric{j}',q**(j-2)>Q(1,3))
# Exact algebraic identity for the upper-branch rational multiplier.
for m in range(16):
 for d in [1,2,3,10,100]:
  j=m+2+d;ck(f'division_m{m}_d{d}',Q(j*(j-1),d)==j+m+1+Q((m+1)*(m+2),d))
out=dict(started_utc=start.isoformat(),ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed']for c in C),total=len(C),proof_sha256=p['proof_sha256'],code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=C,scope='Finite scalar rational controls; infinite-index result is proved in PROOF.md. No B2 convergence.')
(V/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='checks'},indent=2));print('failed',[c for c in C if not c['passed']])
