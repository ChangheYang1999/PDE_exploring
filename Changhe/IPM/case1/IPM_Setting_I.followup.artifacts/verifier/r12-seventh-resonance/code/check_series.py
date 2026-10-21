"""Independent Fraction power-series hierarchy and degree-bound reconstruction."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json,math,time
start=time.time();N=42
Z=lambda:[Q(0)]*(N+1)
def add(*aa):return [sum(a[i] for a in aa) for i in range(N+1)]
def scale(a,c):return [Q(c)*t for t in a]
def mul(a,b):
 c=Z()
 for i,ai in enumerate(a):
  if ai:
   for j,bj in enumerate(b[:N+1-i]):
    if bj:c[i+j]+=ai*bj
 return c
def der(a):return [(i+1)*a[i+1] for i in range(N)]+[Q(0)]
def poly(d):
 a=Z()
 for j,c in d.items():a[j]=Q(c)
 return a
def power(a,n):
 b=poly({0:1})
 for _ in range(n):b=mul(a,b)
 return b
def invD(k):return poly({2*j:Q((-1)**j*math.comb(k+j-1,j),4**(k+j)) for j in range(N//2+1)})
D=poly({0:4,2:1});w=mul(poly({1:-8,3:2}),invD(1));g=mul(poly({2:4}),invD(1));h=add(poly({0:3}),scale(der(w),-1))
G={1:g,3:scale(mul(poly({2:1}),invD(3)),Q(64,3)),5:scale(mul(poly({2:9984,4:-1872,6:88,8:11}),invD(5)),Q(1,90))}
a={0:w};b={1:h};F={};checks={}
# Derivatives reduce available order. All compared orders below24 are unaffected by N=42 truncation.
for j in [3,5,7]:
 a[j-1]=scale(add(der(b[j-2]),der(G[j-2])),Q(1,j-1));b[j]=scale(der(a[j-1]),Q(-1,j))
 F[j]=scale(add(*[add(mul(a[k],der(G[j-k])),scale(mul(b[k+1],G[j-k]),j-k)) for k in range(2,j,2)]),-1)
 if j in G:
  res=add(mul(w,der(G[j])),mul(add(scale(h,j),poly({0:-1})),G[j]),scale(F[j],-1))
  checks['transport_'+str(j)]=all(t==0 for t in res[:25]);assert checks['transport_'+str(j)]
# Common-denominator degree <=14 follows directly from differentiation and multiplication.
num9=mul(F[7],power(D,9));assert all(t==0 for t in num9[15:25])
num8=mul(F[7],power(D,8));assert all(t==0 for t in num8[13:25])
# Multiplying the reconstructed degree12 numerator by D recovers all degree<=14 terms exactly.
reconstructed=mul(poly({i:c for i,c in enumerate(num8[:13]) if c}),D)
assert reconstructed[:25]==num9[:25]
K=scale(mul(poly({i:c for i,c in enumerate(num8[:13]) if c}),power(poly({0:4,2:-1}),2)),Q(1,2*4**10))
terms={i-18:c for i,c in enumerate(K) if c};assert -1 not in terms
B=sum(c*Q(2)**(e+1)/Q(e+1) for e,c in terms.items())
assert B==Q(-23,29059430400)
# The zero-center-homogeneous particular solution is even: -H7 times the odd Laurent primitive.
# Hence its odd degree17 coefficient vanishes; the selected homogeneous contribution is exactly B.
checks['F7_common_denominator_degree_bound']=True;checks['F7_denominator_cancellation']=True;checks['finitepart']=True
out={'date':datetime.now(timezone.utc).isoformat(),'method':'Fraction-only center power series, independent hierarchy, rational degree-bound reconstruction; no sympy or first check data imported','checks':checks,'F7_times_D8':{str(i):str(c) for i,c in enumerate(num8[:13]) if c},'Laurent_coefficients':{str(e):str(c) for e,c in sorted(terms.items())},'B7':str(B),'seconds':time.time()-start}
p=Path(__file__).resolve().parents[1]/'verification'/'series.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
