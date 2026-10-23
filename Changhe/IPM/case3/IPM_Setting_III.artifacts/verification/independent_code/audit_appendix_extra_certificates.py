"""Rational arithmetic audit of printed A3.44 and A3.46 certificates."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
inp=Path('evidence/lead_merge_audit/AUD26_extra_inputs.json');d=json.loads(inp.read_text())
assert hashlib.sha256(Path(d['source_report']).read_bytes()).hexdigest()==d['source_sha256']
def b(j):return F(9+4*j*j,4*abs(4*j*j-9))
def dg(j,sgn):return F(sgn,4 if j==1 else 2)
rows=[]
for v in d['weight3']:
 a=list(map(F,v['vector']));sgn=v['sign'];u=F(v['upper']);l=F(v['lower']);rat=F(v['tail_ratio']);tau=F(v['tau'])
 rs=[]
 for j in range(1,len(a)+1):
  rs.append(dg(j,sgn)+b(j)*(a[j] if j<len(a) else a[-1]*rat)/a[j-1]+(b(j-1)*a[j-2]/a[j-1] if j>1 else 0))
 tail=F(sgn,2)+b(len(a))/rat+b(len(a)+1)*rat
 assert max(rs+[tail])<u
 ray=(sum(dg(j,sgn)*a[j-1]**2 for j in range(1,len(a)+1))+sum(2*b(j)*a[j-1]*a[j] for j in range(1,len(a))))/sum(x*x for x in a)
 assert ray>l
 assert tau==F(sgn,2)+2*b(9)
 piv=[]
 for j in range(1,9):
  p=u-dg(j,sgn)-(b(j-1)**2/piv[-1] if j>1 else 0)-(b(8)**2/(u-tau) if j==8 else 0)
  assert p>0;piv.append(p)
 low=[]
 for j in range(1,v['lower_negative_pivot']+1):
  p=l-dg(j,sgn)-(b(j-1)**2/low[-1] if j>1 else 0)
  assert p<0 if j==v['lower_negative_pivot'] else p>0
  low.append(p)
 jmin=min(range(len(rs)),key=lambda j:u-rs[j]);rows.append(dict(name='m3',sign=sgn,closest_row=jmin+1,closest_margin=str(u-rs[jmin]),first_tail=str(tail),rayleigh=str(ray),upper_pivots=[str(z) for z in piv],lower_pivots=[str(z) for z in low]))
v=d['lambda'];a=list(map(F,v['vector']));rat=F(v['tail_ratio']);up=F(v['upper_A']);lo=F(v['lower_A'])
def alpha(r):return F(1,4*(2*r+1))
rs=[2*alpha(0)*a[1]/a[0]]
for r in range(1,len(a)):
 rs.append((alpha(r-1)*a[r-1]+alpha(r)*(a[r+1] if r+1<len(a) else a[-1]*rat))/a[r])
tail=alpha(len(a)-1)/rat+alpha(len(a))*rat
assert max(rs+[tail])<up
ray=4*sum(alpha(r)*a[r]*a[r+1] for r in range(len(a)-1))/(a[0]**2+2*sum(x*x for x in a[1:]));assert ray>lo
assert ray==F(67289333,185151890)
N=v['last_arm_vertex'];tau=F(v['tau']);assert tau==2*alpha(N+1)
up=F(v['upper_B']);lo=F(v['lower_B']);pa={N:up-alpha(N)**2/(up-tau)};qa={N:lo}
for r in range(N-1,0,-1):
 pa[r]=up-alpha(r)**2/pa[r+1];qa[r]=lo-alpha(r)**2/qa[r+1]
pa[0]=up-2*alpha(0)**2/pa[1];qa[0]=lo-2*alpha(0)**2/qa[1]
assert all(x>0 for x in pa.values());assert all(qa[r]>0 for r in range(1,N+1)) and qa[0]<0
rows.append(dict(name='lambda',A_ratios=[str(z) for z in rs],A_tail=str(tail),A_rayleigh=str(ray),B_upper_pivots={str(k):str(z) for k,z in pa.items()},B_lower_pivots={str(k):str(z) for k,z in qa.items()}))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),rows=rows)
Path('evidence/lead_merge_audit/AUD26_extra_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(utc=out['utc'],status='PASS',cases=len(rows),lambda_upper_central_pivot=float(pa[0]),lambda_lower_central_pivot=float(qa[0])),indent=2))
