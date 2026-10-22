"""mpmath.iv180 recurrence, no Arb arithmetic on the reference path."""
from mpmath import iv
N=261

def check(node,m,r,g):
 iv.dps=180;left,right,_=node;pi=iv.pi;t=pi*(left+right)/102400
 co=iv.cos(2*t);si=iv.sin(2*t);c=iv.mpf(1);s=iv.mpf(0)
 cum=[iv.mpf(0) for _ in range(3)];alt=[iv.mpf(0) for _ in range(3)];count=0
 for j in range(1,N+1):
  c,s=c*co-s*si,s*co+c*si;v=(c,-2*j*s,-2*j*j*c);sg=1 if j%2==0 else -1
  for derivative in range(3):
   unit=1 if derivative==0 else 0
   refs=(v[derivative],unit+v[derivative]+2*cum[derivative],(-sg)*(unit+sg*v[derivative]+2*alt[derivative]))
   for fam,value in enumerate(refs):
    delta=abs(value-iv.mpf(float(m[fam,derivative,j-1])))
    assert (delta.b<=iv.mpf(float(r[fam,derivative,j-1]))) is True,(node,j,fam,derivative)
    count+=1
   cum[derivative]+=v[derivative];alt[derivative]+=sg*v[derivative]
 a=pi*left/51200;b=pi*right/51200
 for j,value in enumerate((iv.cos(a),iv.cos(b),iv.sin(a),iv.sin(b))):
  assert (iv.mpf(float(g[2*j]))<=value.a) is True and (value.b<=iv.mpf(float(g[2*j+1]))) is True,(node,'trig',j)
 assert (iv.mpf(float(g[8]))<=a.a) is True and (b.b<=iv.mpf(float(g[9]))) is True
 assert (iv.mpf(float(g[10]))>(pi*(right-left)/102400).b) is True
 assert count==9*N
 return count,7
