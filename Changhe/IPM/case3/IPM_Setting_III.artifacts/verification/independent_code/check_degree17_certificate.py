"""Result275 independent exact rational polynomial and Sylvester checker.
No Sympy, no lead/numerics code. Discovery coefficients are untrusted inputs.
"""
from exact_polynomial_275 import *
import time
start=datetime.now(timezone.utc).isoformat()
def divpoly(a,b):
 """Single-divisor leading-term division; a zero remainder proves exact divisibility."""
 if not b.a:raise ZeroDivisionError
 q=P(dim=a.d);r=P(a.a,a.d);kb=max(b.a);vb=b.a[kb]
 while r.a:
  kr=max(r.a)
  if not all(i>=j for i,j in zip(kr,kb)):return q,r
  term=P({tuple(i-j for i,j in zip(kr,kb)):r.a[kr]/vb},a.d);q=q+term;r=r-term*b
 return q,r
factors=[];cancellations=[]
class Rat:
 def __init__(self,num=0,den=None):
  self.num=num if isinstance(num,P)else P({(0,0):F(num)});self.den={k:v for k,v in (den or {}).items()if v}
  for k in sorted(self.den):
   while self.den[k]>0:
    q,r=divpoly(self.num,factors[k])
    if r.a:break
    self.num=q;self.den[k]-=1;cancellations.append(k)
  self.den={k:v for k,v in self.den.items()if v}
 def cast(self,b):return b if isinstance(b,Rat)else Rat(b)
 def __add__(self,b):
  b=self.cast(b);den={k:max(self.den.get(k,0),b.den.get(k,0))for k in set(self.den)|set(b.den)};a1=self.num;b1=b.num
  for k,v in den.items():a1=a1*factors[k]**(v-self.den.get(k,0));b1=b1*factors[k]**(v-b.den.get(k,0))
  return Rat(a1+b1,den)
 __radd__=__add__
 def __neg__(self):return Rat(-self.num,self.den)
 def __sub__(self,b):return self+-self.cast(b)
 def __rsub__(self,b):return self.cast(b)+-self
 def __mul__(self,b):
  b=self.cast(b);return Rat(self.num*b.num,{k:self.den.get(k,0)+b.den.get(k,0)for k in set(self.den)|set(b.den)})
 __rmul__=__mul__
 def __pow__(self,k):
  assert isinstance(k,int)and k>=0
  return Rat(self.num**k,{j:v*k for j,v in self.den.items()})
 def denominator(self):
  d=P({(0,0):1})
  for k,v in self.den.items():d=d*factors[k]**v
  return d
 def evaluate(self,v):return self.num.evaluate(v)/self.denominator().evaluate(v)
def ps(co,K):
 L=len(co)-1;out=[L]
 for k in range(1,K+1):
  if k<=L:out.append(-sum(co[j]*out[k-j]for j in range(1,k))-k*co[k])
  else:out.append(-sum(co[j]*out[k-j]for j in range(1,L+1)))
 return out
def readp(rows):return P({tuple(t['powers']):F(t['coefficient'])for t in rows})
def uni_p(c):return P({(0,i):F(a)for i,a in enumerate(c)})
def factorcheck(label,sc):
 # Product sign is the constant sign only after every factor is proved positive.
 product=[F(sc['constant'])];sign=1 if product[0]>0 else -1
 ck(label+' nonzero constant',product[0]!=0,str(product[0]))
 for k,f in enumerate(sc['factors']):
  fc=[F(x)for x in f['coefficients_ascending']];shift=[sum(fc[i]*comb(i,j)for i in range(j,len(fc)))for j in range(len(fc))]
  ck(label+' exact shift'+str(k),shift==[F(x)for x in f['shifted_coefficients_ascending']])
  ck(label+' positive shift'+str(k),all(x>0 for x in shift),[str(x)for x in shift]);ck(label+' positive integer factor power'+str(k),isinstance(f['power'],int)and f['power']>=1)
  for _ in range(f['power']):product=mul(product,fc)
 ck(label+' factor convolution',product==[F(x)for x in sc['coefficients_ascending']]);return product,sign
cert=json.loads((V/'certificate.json').read_text())
ck('initial proof frozen',sha(R/'INITIAL_REDUCTION.md')==cert['initial_proof_sha256'])
ck('discovery driver frozen',sha('independent_code/derive_degree17_reductions.py')==cert['driver_sha256'])
for item in json.loads((V/'DEPENDENCIES.json').read_text()):ck('dependency '+Path(item['frozen']).name,sha(item['frozen'])==item['sha256'])
for num,count in [(258,724),(261,824),(267,204)]:
 g=json.loads((V/f'gate{num}.json').read_text());ck('gate'+str(num),g['status']=='PASS'and g['count']==count and all(r['passed']for r in g['checks']));ck('proof gate'+str(num),g['proof_sha256']==sha(V/f'proof{num}.md'))
# Algebraic manufacture: elementary symmetric coefficients from formal roots,
# then Newton recurrence vs separately summed powers, through degree L+2.
for L in range(1,5):
 roots=[P.var(i,L)for i in range(L)];co=[P({(0,)*L:1},L)]
 for v in roots:
  new=[P(dim=L)for _ in range(len(co)+1)]
  for j,c in enumerate(co):new[j]=new[j]+c;new[j+1]=new[j+1]-v*c
  co=new
 power=ps(co,L+2)
 for k in range(1,L+3):ck('Newton roots L'+str(L)+' k'+str(k),power[k]==sum(v**k for v in roots))
expected=[('q22a','two',(5,4,2,2)),('q22b','two',(1,6,2,2)),('q23a','two',(1,2,4,3)),('q23b','two',(3,4,2,3)),('q24','two',(1,4,2,4)),('s112a','three',(1,8,4,2,2)),('s112b','three',(1,6,2,4,2)),('s112c','three',(3,6,4,2,2)),('s113','three',(1,6,4,2,3))]
ck('exact case names',list(cert['cases'])==[r[0]for r in expected]);case_info={}
ck('active exact library frozen',sha('independent_code/exact_polynomial_275.py')==sha(V/'exact_polynomial_275_frozen.py'))
for name,kind,par in expected:
 print('START',name,datetime.now(timezone.utc).isoformat(),flush=True);t0=time.monotonic();r=cert['cases'][name];ck(name+' parameters',r['kind']==kind and r['parameters']==list(par));x0,n0=P.var(0),P.var(1);D=17+2*n0;T=par[0]*D-17; x=Rat(x0);cancellations=[]
 if kind=='two':
  A,a,b,L=par;factors=[D,T*F(1,a-b)];lam=Rat(factors[1]);li=Rat(1,{1:1});tau=Rat(D-1,{0:1});c=((lam+1)*x-(lam+2))*li;u=ps([Rat(1),-x,c],L+1);co=[Rat(1)];ss=[L]
  for k in range(1,L):
   ss.append(-(A*tau**k+a*u[k])*F(1,b));co.append(-(ss[k]+sum(co[j]*ss[k-j]for j in range(1,k)))*F(1,k))
  co.append(sum((L-j)*co[j]for j in range(L))*li-sum(co));w=ps(co,L+1);eq=[A*tau**k+a*u[k]+b*w[k]for k in [L,L+1]]
 else:
  A,a,b,w,L=par;s0=(-T-(a-w)*x0)*F(1,b-w);factors=[D,x0,s0];tau=Rat(D-1,{0:1});s=Rat(s0);alpha=1-Rat(1,{1:1});beta=1-Rat(1,{2:1});co=[Rat(1)];ss=[L]
  for k in range(1,L+1):
   ss.append(-(A*tau**k+a*alpha**k+b*beta**k)*F(1,w));co.append(-(ss[k]+sum(co[j]*ss[k-j]for j in range(1,k)))*F(1,k))
  power=ps(co,L+1);eq=[A*tau**(L+1)+a*alpha**(L+1)+b*beta**(L+1)+w*power[L+1],sum((L-j)*co[j]for j in range(L))+(x+s)*sum(co)]
 pp=[];den_stats=[]
 for j,(equation,data)in enumerate(zip(eq,r['equations'])):
  num=readp(data['numerator_terms']);den=readp(data['denominator_terms']);prim=readp(data['primitive_terms']);content=F(data['primitive_content']);own_den=equation.denominator();quot,rem=divpoly(own_den,den)
  ck(name+' rational equation identity'+str(j),equation.num*den==num*own_den)
  ck(name+' cancelled denominator divides allowed product'+str(j),not rem.a and bool(quot.a))
  ck(name+' primitive numerator'+str(j),num==content*prim and prim.primitive()==(prim,F(1)) and content!=0)
  ck(name+' saved degrees'+str(j),[prim.degree(0),prim.degree(1)]==r['degrees'][j]);pp.append(prim);den_stats.append(dict(allowed_factor_powers=equation.den,denominator_degree=[own_den.degree(0),own_den.degree(1)]))
 if name.startswith('q22'):
  A=pp[0];aa=P({(0,j):v for(i,j),v in A.a.items()if i==2});bb=P({(0,j):v for(i,j),v in A.a.items()if i==1});cc=P({(0,j):v for(i,j),v in A.a.items()if i==0});disc=bb*bb-4*aa*cc;rc,sign=factorcheck(name+' disc',r['discriminant']);ck(name+' exact discriminant',disc==uni_p(rc));ck(name+' negative discriminant',sign==-1);ck(name+' quadratic degree',A.degree(0)==2)
 else:
  A,B=pp;da,db=A.degree(0),B.degree(0);bound=db*A.degree(1)+da*B.degree(1);ck(name+' exact degree bound',bound==r['degree_bound']);rc,sign=factorcheck(name+' resultant',r['resultant']);ck(name+' integer coefficients',all(c.denominator==1 for c in rc));ck(name+' determinant degree within bound',len(rc)-1<=bound and rc[-1]!=0)
  for value in range(1,bound+3):
   mat=sylvester(A.specialize(value,da),B.specialize(value,db));det,nd,ns=bareiss(mat);ck(name+' Bareiss n'+str(value),det==peval(rc,value),dict(divisions=nd,swaps=ns,determinant=str(det)))
  for value in [F(1),F(2),F(3,2)]:ck(name+' independent Gaussian n'+str(value),gaussian(sylvester(A.specialize(value,da),B.specialize(value,db)))==peval(rc,value))
 case_info[name]=dict(denominators=den_stats,exact_factor_cancellations={str(k):cancellations.count(k)for k in set(cancellations)},wall_seconds=time.monotonic()-t0)
 (V/'CHECKS_partial.json').write_text(json.dumps(dict(checks=checks,case_info=case_info),indent=2)+'\n');print('DONE',name,'checks',len(checks),'fail',sum(not c['passed']for c in checks),flush=True)
# Independent positive partitions, explicit necessary exclusions.
def part(total,count,minimum=1):
 if count==0:
  if total==0:yield ()
  return
 for q in range(minimum,total//count+1):
  for v in part(total-q,count-1,q):yield(q,)+v
rows=[];surv=[]
for e in range(2,8):
 for A in range(1,18-2*(e+1),2):
  for mu in part((17-A)//2,e+1):
   reason=None;unique=set(mu)
   if len(unique)==1:reason='equal'
   elif len(unique)==len(mu):reason='all real M2 positive'
   elif len(unique)==2:
    singles=[q for q in unique if mu.count(q)==1]
    if len(singles)==1:
     q=singles[0];common=next(v for v in mu if v!=q)
     if q>common:reason='unique higher'
     elif A!=1 or common-q<=1:reason='unique lower A or gap'
   rows.append(dict(e=e,A0=A,multiplicities=mu,reason=reason or 'retained'))
   if reason is None:surv.append((A,mu))
want=[(5,(1,1,2,2)),(1,(1,1,3,3)),(1,(1,1,2,2,2)),(3,(1,1,1,2,2)),(1,(1,1,1,1,2,2)),(1,(1,1,2,4)),(1,(1,2,2,3)),(3,(1,1,2,3)),(1,(1,1,1,2,3))]
ck('exact nine surviving partitions',sorted(surv)==sorted(want),surv);ck('total degree accounting',all(A+2*sum(mu)==17 for A,mu in want));
# Derive multiplicity multisets from every grouped structural tuple and match
# the independently enumerated survivors, not just another hard-coded list.
mapped=[]
for name,kind,par in expected:
 if kind=='two':
  A,a,b,L=par;weights=[a]*2+[b]*L
 else:
  A,a,b,w,L=par;weights=[a,b]+[w]*L
 ck(name+' case maps to survivor',all(v>0 and v%2==0 for v in weights)and (A,tuple(sorted(v//2 for v in weights)))in surv)
 mapped.append((A,tuple(sorted(v//2 for v in weights))))
ck('case mapping is bijective',len(mapped)==len(set(mapped)) and sorted(mapped)==sorted(surv))
ck('degree lower bound scope',F(1)+F(19,2)==F(21,2))
(V/'PARTITIONS.json').write_text(json.dumps(rows,indent=2)+'\n')
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,case_info=case_info,partition_count=len(rows),proof_sha256=sha(R/'PROOF.md'),certificate_sha256=sha(V/'certificate.json'),driver_sha256=sha(__file__),polynomial_library_sha256=sha('independent_code/exact_polynomial_275.py'),scope='Finite auxiliary polynomial degree17 obstruction only; full-plane IPM OPEN.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
