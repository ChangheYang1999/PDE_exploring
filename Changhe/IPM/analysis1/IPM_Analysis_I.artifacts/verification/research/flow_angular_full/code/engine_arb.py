"""Arb512 direct even trigonometric sums, independent of source odd products."""
from common import arb,ctx,N

def check(node,m,r,g):
 ctx.prec=512;pi=arb.pi();l,h,_=node;theta=pi*(l+h)/102400
 sums=[arb(0) for _ in range(3)];alts=[arb(0) for _ in range(3)];count=0
 for n in range(1,N+1):
  x=2*n*theta;v=[x.cos(),-2*n*x.sin(),-2*n*n*x.cos()];sign=(-1)**n
  values=[v,[arb(k==0)+v[k]+2*sums[k] for k in range(3)],[-sign*(arb(k==0)+sign*v[k]+2*alts[k]) for k in range(3)]]
  for f in range(3):
   for k in range(3):
    ref=values[f][k];assert ref.is_finite() and bool(abs(ref-arb(float(m[f,k,n-1]))).upper()<=arb(float(r[f,k,n-1]))),(node,n,f,k)
    count+=1
  for k in range(3):sums[k]+=v[k];alts[k]+=sign*v[k]
 a=pi*l/51200;b=pi*h/51200;refs=[a.cos(),b.cos(),a.sin(),b.sin()]
 for j,ref in enumerate(refs):assert bool(arb(float(g[2*j]))<=ref.lower()) and bool(ref.upper()<=arb(float(g[2*j+1]))),(node,'trig',j)
 assert bool(arb(float(g[8]))<=a.lower()) and bool(b.upper()<=arb(float(g[9])))
 assert bool(arb(float(g[10]))>(pi*(h-l)/102400).upper())
 assert count==9*N
 return count,7
