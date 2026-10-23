"""Result267. Pure Python exact sparse polynomial and integer determinant checks.
No symbolic algebra system or producer routine is imported.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import gcd,lcm,comb
import json,hashlib
R=Path('research/degree15_grouped_moment_obstruction');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
class P:
 def __init__(self,terms=None,dim=2):
  self.d=dim;self.a={tuple(k):F(v)for k,v in (terms or {}).items()if v}
 @classmethod
 def var(cls,index,dim=2):
  k=[0]*dim;k[index]=1;return cls({tuple(k):1},dim)
 def cast(self,x):
  if isinstance(x,P):assert x.d==self.d;return x
  return P({(0,)*self.d:x},self.d)
 def __add__(self,other):
  other=self.cast(other);a=self.a.copy()
  for k,v in other.a.items():a[k]=a.get(k,F(0))+v
  return P(a,self.d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.a.items()},self.d)
 def __sub__(self,other):return self+-self.cast(other)
 def __rsub__(self,other):return self.cast(other)+-self
 def __mul__(self,other):
  other=self.cast(other);a={}
  for x,u in self.a.items():
   for y,v in other.a.items():
    k=tuple(i+j for i,j in zip(x,y));a[k]=a.get(k,F(0))+u*v
  return P(a,self.d)
 __rmul__=__mul__
 def __pow__(self,k):
  assert isinstance(k,int)and k>=0
  out=self.cast(1);b=self
  while k:
   if k%2:out=out*b
   b=b*b;k//=2
  return out
 def __eq__(self,other):return self.a==self.cast(other).a
 def degree(self,i):return max((k[i]for k in self.a),default=-1)
 def evaluate(self,values):
  out=F(0)
  for k,c in self.a.items():
   a=c
   for n,v in zip(k,values):a*=F(v)**n
   out+=a
  return out
 def primitive(self):
  den=1
  for v in self.a.values():den=lcm(den,v.denominator)
  a={k:int(v*den)for k,v in self.a.items()};content=0
  for v in a.values():content=gcd(content,v)
  sign=1 if a[max(a)]>0 else -1
  return P({k:v//content*sign for k,v in a.items()},self.d),F(content*sign,den)
 def specialize(self,value,degree):
  a=[F(0)]*(degree+1)
  for (i,j),c in self.a.items():a[degree-i]+=c*F(value)**j
  return [v.numerator if v.denominator==1 else v for v in a]
def stored(rows):return P({tuple(t['powers']):int(t['coefficient'])for t in rows})
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def peval(a,x):
 y=0
 for v in reversed(a):y=y*x+v
 return y
def sylvester(a,b):
 da,db=len(a)-1,len(b)-1;out=[]
 for i in range(db):out.append([0]*i+a+[0]*(db-1-i))
 for i in range(da):out.append([0]*i+b+[0]*(da-1-i))
 assert all(len(row)==da+db for row in out)
 return out
def bareiss(matrix):
 a=[row[:]for row in matrix];old=1;sign=1;divisions=0;swaps=0
 for k in range(len(a)-1):
  pivot=next((i for i in range(k,len(a))if a[i][k]),None)
  if pivot is None:return 0,divisions,swaps
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign;swaps+=1
  d=a[k][k]
  for i in range(k+1,len(a)):
   for j in range(k+1,len(a)):
    v,r=divmod(a[i][j]*d-a[i][k]*a[k][j],old)
    if r:raise ArithmeticError('Nonexact Bareiss division')
    a[i][j]=v;divisions+=1
   a[i][k]=0
  old=d
 return sign*a[-1][-1],divisions,swaps
def gaussian(matrix):
 a=[[F(x)for x in row]for row in matrix];det=F(1)
 for k in range(len(a)):
  row=next((i for i in range(k,len(a))if a[i][k]),None)
  if row is None:return F(0)
  if row!=k:a[row],a[k]=a[k],a[row];det=-det
  pivot=a[k][k];det*=pivot
  for j in range(k,len(a)):a[k][j]/=pivot
  for i in range(k+1,len(a)):
   c=a[i][k]
   for j in range(k,len(a)):a[i][j]-=c*a[k][j]
 return det
cert=json.loads((V/'certificate.json').read_text())
for item in json.loads((V/'DEPENDENCIES.json').read_text()):ck('frozen '+Path(item['frozen']).name,sha(item['frozen'])==item['sha256'])
for num,count in [(258,724),(261,824),(264,82)]:
 gate=json.loads((V/f'gate{num}.json').read_text());ck('gate '+str(num),gate['status']=='PASS'and gate['count']==count and all(x['passed']for x in gate['checks']))
 ck('gate proof '+str(num),gate['proof_sha256']==sha(V/f'proof{num}.md'))
# Newton sums from root expansions, independently of the grouped recurrence.
x,y,z=[P.var(i,3)for i in range(3)];h=x+y;j=x*y
for k,want in [(1,h),(2,h*h-2*j),(3,h**3-3*h*j),(4,h**4-4*h*h*j+2*j*j)]:ck('quadratic roots power'+str(k),x**k+y**k==want)
h=x+y+z;j=x*y+x*z+y*z;k=x*y*z
for ell,want in [(1,h),(2,h*h-2*j),(3,h**3-3*h*j+3*k),(4,h**4-4*h*h*j+2*j*j+4*h*k)]:ck('cubic roots power'+str(ell),x**ell+y**ell+z**ell==want)
# Case i with all rational denominators cleared explicitly.
n=P.var(0,1);l=n+7;Z=2*n+15;D=2*n*l;aa=Z*(n-2);hh=-D-2*aa;zz=Z*n
num=216*zz*zz-144*aa*zz-24*hh*zz+6*D*D+12*aa*aa+hh*hh+12*aa*hh
fc=[int(x)for x in cert['case_i_numerator_ascending']];claim=P({(i,):a for i,a in enumerate(fc)},1)
ck('casei full clearing',num==36*claim)
ck('casei all positive nonconstant coefficients',all(x>0 for x in fc[1:]));ck('casei numerator lower bound',sum(fc)==2732)
z0=F(17,16);a0=-z0;h0=-(1+2*a0)/6;j0=(1+2*a0*a0+6*h0*h0)/12
ck('casei h',h0==F(3,16));ck('casei j',j0==F(37,128));ck('casei direct derivative',3*z0*z0-2*(a0+h0)*z0+j0+a0*h0==F(683,128));ck('casei rational formula at1',F(peval(fc,1),8*8**2)==F(683,128))
# Case ii, generic symbols A,lambda,z,p with no specialization.
A,L,z,p=[P.var(i,4)for i in range(4)];H=-A-4*p;q=(L+1)*p*z-(L+2)*z*z;j=2*(2-L)*z*z+(L-1)*H*z
cleared=2*A*L+8*L*p*p-16*q+L*H*H-4*j
ac=12*L;bc=4*A*L-16*z;cc=L*(A+F(1,2)*A*A)+(12*L+8)*z*z+2*A*(L-1)*z
ck('caseii complete quadratic',cleared==2*(ac*p*p+bc*p+cc))
disc=bc*bc-4*ac*cc
expected=-8*A*A*L*L-48*A*L*L-96*A*L*L*z-32*A*L*z-576*L*L*z*z+(256-384*L)*z*z
ck('caseii discriminant exact',disc==expected);ck('caseii last coefficient negative forlambda>=1',256-384<0)
# Case iii, hand-cleared bivariate integer numerators.
t,n=P.var(0),P.var(1);l=n+7;Z=2*n+15;s=-n-2*t;D0=2*l*t*s
aa=Z*(t-1)*s;bb=Z*(s-1)*t;hh=-l*t*s-3*aa-2*bb;zz=Z*t*s;jj=D0*D0+6*aa*aa+4*bb*bb+2*hh*hh
rawA=4*zz*(2*zz-hh)+(t+s)*(4*zz*zz-4*hh*zz+jj)
rawB=4*D0**3+24*aa**3+16*bb**3+8*hh**3-6*hh*jj
calculated={'iii':(rawA,rawB)}
# Case iv, denominators n and n+7 are retained and never divided as polynomials.
p,n=P.var(0),P.var(1);l=n+7;Z=2*n+15;qq=2*l*(n+1)*p*Z-(n+2)*Z*Z;hh=-1-4*p
jj=2*n*l*l+8*n*l*l*p*p-4*qq+n*l*l*hh*hh
kk=2*n*(n-3)*Z**3+2*n*(2-n)*hh*Z*Z*l+(n-1)*jj*Z
rawA=16*n*n*l**3*(1+4*p**3)-48*n*l*p*qq+4*n*n*l**3*hh**3-6*n*l*hh*jj+6*kk
rawB=16*n*n*l**4*(1+4*p**4)-64*n*l*l*p*p*qq+8*qq*qq+2*n*n*l**4*hh**4-4*n*l*l*hh*hh*jj+jj*jj+4*l*hh*kk
calculated['iv']=(rawA,rawB)
for label,wanted in [('iii',(5,6,5,6,60,45,409600,[1,1,24],[9,12,1])),('iv',(3,4,5,6,38,38,-13107200,[1,1,20],[6,12,1]))]:
 row=cert['cases'][label];A=stored(row['A_terms']);B=stored(row['B_terms']);da,db,dna,dnb,bound,degree,constant,degs,powers=wanted
 for name,computed,target in zip(['A','B'],calculated[label],[A,B]):
  prim,content=computed.primitive();ck(label+' '+name+' direct numerator primitive',prim==target,str(content));ck(label+' '+name+' integer coefficients',all(v.denominator==1 for v in target.a.values()));ck(label+' '+name+' positive primitive convention',target.primitive()==(target,F(1)))
 ck(label+' actual degrees',(A.degree(0),B.degree(0),A.degree(1),B.degree(1))==(da,db,dna,dnb))
 ck(label+' determinant degree bound',db*dna+da*dnb==bound)
 rc=[int(x)for x in row['resultant_coefficients_ascending']];factors=row['resultant_factors'];ck(label+' factor count',len(factors)==3);ck(label+' constant',int(row['resultant_factor_constant'])==constant)
 ck(label+' factor degrees',[len(f['coefficients_ascending'])-1 for f in factors]==degs);ck(label+' factor powers',[f['power']for f in factors]==powers)
 product=[constant]
 for k,f in enumerate(factors):
  fc=[int(x)for x in f['coefficients_ascending']]
  shift=[sum(fc[i]*comb(i,j)for i in range(j,len(fc)))for j in range(len(fc))]
  ck(label+' factor shifted identity '+str(k),shift==[int(x)for x in f['shifted_coefficients_ascending']])
  if label=='iii'and k==2:ck('iii all25 F24 coefficients positive',len(fc)==25 and all(x>0 for x in fc),[str(x)for x in fc])
  if label=='iv'and k==2:
   for j,c in enumerate(shift):ck('iv positive shifted coefficient '+str(j),c>0,str(c))
  if k<2:ck(label+' positive linear factor '+str(k),len(fc)==2 and fc[0]>=0 and fc[1]>0 and shift[0]>0)
  for _ in range(f['power']):product=mul(product,fc)
 ck(label+' full factor convolution',product==rc);ck(label+' resultant degree',len(rc)-1==degree and degree<=bound and rc[-1]!=0)
 points=list(range(1,bound+2));ck(label+' exact interpolation count',len(set(points))==bound+1)
 for value in points+[bound+2]:
  matrix=sylvester(A.specialize(value,da),B.specialize(value,db));det,divisions,swaps=bareiss(matrix)
  ck(label+' integer determinant n'+str(value),det==peval(rc,value),dict(n=value,determinant=str(det),divisions=divisions,row_swaps=swaps))
 for value in [F(1),F(2),F(3,2)]:
  matrix=sylvester(A.specialize(value,da),B.specialize(value,db));det=gaussian(matrix)
  ck(label+' separate Gaussian n'+str(value),det==peval(rc,value),str(det))
# Exact complete partition enumeration, independent of all symbolic elimination.
def partitions(total,count,minimum=1):
 if count==0:
  if total==0:yield ()
  return
 for a in range(minimum,total//count+1):
  for rest in partitions(total-a,count-1,a):yield(a,)+rest
rows=[];survive=[]
for e in range(2,7):
 for A in range(1,16-2*(e+1),2):
  for mu in partitions((15-A)//2,e+1):
   reason=None
   if len(set(mu))==1:reason='equal'
   elif e==2 and len(set(mu))==3:reason='all real M2 positive'
   elif len(set(mu))==2:
    exceptional=[q for q in set(mu)if mu.count(q)==1]
    if len(exceptional)==1:
     nu=exceptional[0];common=next(q for q in mu if q!=nu)
     if nu>common:reason='unique higher'
     elif A!=1 or common-nu<=1:reason='unique lower A or gap'
   row=dict(e=e,A0=A,multiplicities=list(mu),reason=reason or 'retained');rows.append(row)
   if reason is None:survive.append((e,A,mu))
expected=[(2,1,(1,3,3)),(3,1,(1,1,2,3)),(3,3,(1,1,2,2)),(4,1,(1,1,1,2,2))]
ck('all25 multiplicity partitions',len(rows)==25,len(rows));ck('counts by e',[sum(x['e']==e for x in rows)for e in range(2,7)]==[11,7,4,2,1]);ck('exactly four survivors',survive==expected,survive)
ck('odd degree conclusion',17%2==1 and F(1)+F(17,2)==F(19,2))
(V/'PARTITIONS.json').write_text(json.dumps(rows,indent=2)+'\n')
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),certificate_sha256=sha(V/'certificate.json'),driver_sha256=sha(__file__),scope='Exact finite auxiliary polynomial obstruction m15; full-plane IPM OPEN. No symbolic resultant routine is used by this checker.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([x for x in checks if not x['passed']]);raise SystemExit(out['status']!='PASS')
