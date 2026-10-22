"""Fresh Arb1536 complex powers; same FLINT library, distinct evaluation."""
from flint import arb,acb,ctx
N=261

def check(node,m,r,g):
 ctx.prec=1536;lo,hi,_=node;pi=arb.pi();theta=pi*(lo+hi)/102400
 root=acb(0,theta*2).exp();power=acb(1);prefix=[arb(0),arb(0),arb(0)];alternating=[arb(0),arb(0),arb(0)];count=0
 for n in range(1,N+1):
  power*=root;v=(power.real,-2*n*power.imag,-2*n*n*power.real);sg=(-1)**n
  for k in range(3):
   vals=(v[k],int(k==0)+v[k]+2*prefix[k],(-1)**(n-1)*(int(k==0)+sg*v[k]+2*alternating[k]))
   for fam,ref in enumerate(vals):
    assert ref.is_finite() and bool(abs(ref-arb(float(m[fam,k,n-1]))).upper()<=arb(float(r[fam,k,n-1]))),(node,n,fam,k)
    count+=1
   prefix[k]+=v[k];alternating[k]+=sg*v[k]
 a=pi*lo/51200;b=pi*hi/51200
 for j,value in enumerate((a.cos(),b.cos(),a.sin(),b.sin())):
  assert bool(arb(float(g[2*j]))<=value.lower()) and bool(value.upper()<=arb(float(g[2*j+1])))
 assert bool(arb(float(g[8]))<=a.lower()) and bool(b.upper()<=arb(float(g[9])))
 assert bool(arb(float(g[10]))>(pi*(hi-lo)/102400).upper())
 assert count==9*N
 return count,7
