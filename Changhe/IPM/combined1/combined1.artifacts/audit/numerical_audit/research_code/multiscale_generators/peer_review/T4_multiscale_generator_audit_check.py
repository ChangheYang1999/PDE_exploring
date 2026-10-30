"""Independent exact rational coefficients and one-power Cartesian jets."""
from pathlib import Path
from datetime import datetime,timezone
from math import factorial,comb
import importlib.util,hashlib,json,sys,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
ROOT=Path(__file__).resolve().parents[1];X=P([0,1]);ZERO=P([])
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def choose(a,k):
 v=Q(1)
 for i in range(k):v*= (a-i)/(i+1)
 return v
def leg(n):
 p=ZERO
 for k in range(n//2+1):p+=Q((-1)**k*factorial(2*n-2*k),2**n*factorial(k)*factorial(n-k)*factorial(n-2*k))*X**(n-2*k)
 return p
def conv(a,b,d):return [sum((a[j]*b[i-j] for j in range(max(0,i-len(b)+1),min(i+1,len(a)))),Q(0)) for i in range(d+1)]
def moments(p,m,w,n,q,R,d):
 ans=[Q(0)]*(d+1)
 if q>d:return ans
 cc=leg(n)
 for k,c in enumerate(cc):
  if not c:continue
  a=list((1-R*R*X)**k)
  b=[choose(Q(-w-q-k),i)*R**(2*i) for i in range(d-q+1)]
  ab=conv(a,b,d-q)
  row=conv(ab,[choose(p-m,i) for i in range(d-q+1)],d-q)
  for i,v in enumerate(row):ans[i+q]+=R**(2*q)*c*v
 return ans
def mul(A,B,d):
 out={}
 for (i,j),a in A.items():
  for (k,l),b in B.items():
   if i+j+k+l<=d:out[i+k,j+l]=out.get((i+k,j+l),Q(0))+a*b
 return {k:v for k,v in out.items() if v}
def ar(q):return arb(q.numerator)/q.denominator
def exact_jet(p,m,w,n,q,R,x,y,d):
 s=x*x+y*y;aa=1+s;bb=R*R+s
 N=ZERO
 for k,c in enumerate(leg(n)):N+=c*(X-R*R)**k*(X+R*R)**(n-k)
 N*=X**w;shift=N(X+s);B=w+q+n
 coeff=conv(list(shift),[choose(Q(-B),j)/bb**j for j in range(d+1)],d)
 coeff=conv(coeff,[choose(p-m,j)/aa**j for j in range(d+1)],d)
 D={(1,0):2*x,(0,1):2*y,(2,0):Q(1),(0,2):Q(1)};power={(0,0):Q(1)};rad={}
 for c in coeff:
  for idx,v in power.items():rad[idx]=rad.get(idx,Q(0))+c*v
  power=mul(power,D,d)
 H={}
 for k in range(0,2*m+1,2):
  fac=Q((-1)**(k//2)*comb(2*m,k))
  for i in range(min(d,2*m-k)+1):
   for j in range(min(d-i,k)+1):
    H[i,j]=H.get((i,j),Q(0))+fac*comb(2*m-k,i)*comb(k,j)*x**(2*m-k-i)*y**(k-j)
 result=mul(rad,H,d);factor=ar(R**(2*q)/bb**B)*ar(aa)**ar(p-m)
 return {(i,j):factor*ar(result.get((i,j),Q(0))*factorial(i)*factorial(j)) for i in range(d+1) for j in range(d+1-i)},result
start=time.monotonic();ctx.prec=768
peer_m=load('peer_m',ROOT/'source/N4_moments.py');peer_j=load('peer_j',ROOT/'source/N4_cartesian.py')
c=Q(4076476460239181,2251799813685248);delta=1-1/c;rows=[]
for j in [0,3,7]:
 p=(3+1/c-j*delta)/2
 for m in [0,2,9]:
  w=max(5-m,0)
  for n in [0,1,5,11]:
   for q in [0,4]:
    for R in [Q(1,2),Q(1),Q(3,2),Q(10),Q(100)]:
     got=moments(p,m,w,n,q,R,14);expected=peer_m.coefficients(p,m,w,n,q,R,14)
     assert got==expected
     assert got[q]==R**(2*q) and got[q+1]==R**(2*q)*(p-m-R*R*(w+q+n*(n+1))) and all(v==0 for v in got[:q])
     rows.append({'j':j,'m':m,'w':w,'n':n,'Q':q,'R':str(R),'all_15_equal':True,'coefficients_sha256':hashlib.sha256(('\n'.join(map(str,got))+'\n').encode()).hexdigest()})
print('moments',len(rows),'seconds',time.monotonic()-start,flush=True)
jets=[]
for m,w,n,q,R,x,y,d in [(0,5,0,0,Q(10),Q(1,3),Q(2,5),6),(1,4,1,4,Q(100),Q(50),Q(100,3),6),(2,3,3,4,Q(10),Q(1),Q(2),6),(2,3,2,0,Q(1,2),Q(0),Q(1),6),(0,0,3,4,Q(100),Q(0),Q(0),6),(2,0,1,0,Q(10),Q(0),Q(0),6),(0,5,0,0,Q(10),Q(0),Q(0),9),(1,4,11,4,Q(100),Q(0),Q(0),9),(2,3,3,4,Q(10),Q(0),Q(0),9),(9,0,11,0,Q(100),Q(0),Q(0),9)]:
 data={'cl':'5/2','generators':[{'j':1,'m':m,'spec':['legqs',w,n,q,str(R)],'coef':'1'}]}
 got,rationals=exact_jet(Q(7,5),m,w,n,q,R,x,y,d);expected=peer_j.GeneratorJet(data,str(x),str(y),order=d)
 assert all(v.overlaps(expected.chi(*idx)) for idx,v in got.items())
 vanishes=x==0 and y==0 and m+w>=5
 if vanishes:assert not rationals and all(v.is_zero() for v in got.values())
 jets.append({'m':m,'w':w,'n':n,'Q':q,'R':str(R),'point':[str(x),str(y)],'order':d,'comparisons':len(got),'all_overlap':True,'exact_vanishing':vanishes})
 print('jet',len(jets),'seconds',time.monotonic()-start,flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':digest(ROOT/'PROOF.md'),'code_sha256':digest(Path(__file__)),'N4_proof_sha256':digest(ROOT/'source/N4_PROOF.md'),'N4_moments_sha256':digest(ROOT/'source/N4_moments.py'),'N4_cartesian_sha256':digest(ROOT/'source/N4_cartesian.py'),'moment_rows':rows,'jet_rows':jets,'exact_coefficient_comparisons':len(rows)*15,'interval_jet_comparisons':sum(v['comparisons'] for v in jets),'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print('complete',out['elapsed_seconds'],flush=True)
