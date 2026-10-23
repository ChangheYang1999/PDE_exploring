"""Independent rational reconstruction of degree23 node equations.

Only verifier-owned exact_degree21 arithmetic is imported. Producer JSON is
compared as data and no producer computation module is executed.
"""
from collections import Counter
from exact_degree21 import *

def dp(data):
 assert isinstance(data,list)
 terms={}
 for pair in data:
  assert isinstance(pair,list) and len(pair)==2
  ex,v=pair
  assert len(ex)==3 and all(type(j)is int and j>=0 for j in ex)
  assert tuple(ex)not in terms
  terms[tuple(ex)]=int(v)
 return C.from_dict(terms)

def dq(data):
 assert len(data)==2
 return Q(dp(data[0]),dp(data[1]))

def coeffpoly(data):
 co=list(map(int,data['coefficients_low_to_high']))
 assert co and co[-1] and data['degree']==len(co)-1
 return sum((C.constant(c)*h**i for i,c in enumerate(co)),C.constant(0))

def qsubst(q,i,z):
 q=Q(q)
 def sub(p):
  out=Q(0)
  for k in range(degree(p,i),-1,-1):out=out*z+coef(p,i,k)
  return out
 return sub(q.n)/sub(q.d)

def denominator_ok(q,allowed):
 d=Q(q).d
 for a in allowed:
  a=prim(a)
  assert a and a.total_degree()>0
  while d.total_degree()>0:
   z,r=divmod(d,a)
   if r:break
   d=z
 return bool(d)and d.total_degree()==0

def fill(A,known,L,b,K,ck,name):
 assert 0<=K<=L and b>0
 co=[Q(1)];targets=[Q(L)]
 for k in range(1,K+1):
  target=-(Q(A*(h-1)**k)+sum((w*s[k]for w,s in known),Q(0)))/b
  targets.append(target)
  co.append(-(target+sum((co[j]*targets[k-j]for j in range(1,k)),Q(0)))/k)
  # Newton makes the kth power sum linear in its kth monic coefficient.
  probe=co+[Q(0)]*(L-k)
  s=ps(probe,k)[k]
  ck(name+' moment pivot '+str(k),ps(probe[:k]+[probe[k]+1]+probe[k+1:],k)[k]-s==-k)
  ck(name+' moment target '+str(k),s==target)
 return co

def moment(A,groups,singles,K,ck,name):
 arrays=[]
 for j,(w,co)in enumerate(groups):
  ck(name+' Newton coverage '+str(j),1<=len(co)-1<=8 and 0<=K<=9)
  arrays.append((w,ps(co,K)))
 return [Q(A*(h-1)**k)+sum((w*s[k]for w,s in arrays),Q(0))+sum((w*Q(z)**k for w,z in singles),Q(0))for k in range(K+1)]

def match_configuration(groups,singles,data,allowed,ck,name):
 sc=data.get('classes',[]);ss=data.get('singletons',[])
 ck(name+' number of classes',len(groups)==len(sc));ck(name+' number of singletons',len(singles)==len(ss))
 for j,((w,co),row)in enumerate(zip(groups,sc)):
  ck(name+' class weight '+str(j),w==row['weight']);ck(name+' coefficient count '+str(j),len(co)==len(row['coefficients']))
  for k,(q,s)in enumerate(zip(co,row['coefficients'])):
   ck(name+f' class{j} coefficient{k}',Q(q)==dq(s));ck(name+f' class{j} denominator{k}',denominator_ok(q,allowed))
 for j,((w,z),row)in enumerate(zip(singles,ss)):
  ck(name+' singleton weight '+str(j),w==row['weight']);ck(name+' singleton node '+str(j),Q(z)==dq(row['node']));ck(name+' singleton denominator '+str(j),denominator_ok(z,allowed))
 if 'class_polynomials'in data:
  ck(name+' duplicate class count',len(data['class_polynomials'])==len(groups))
  for j,((w,co),stored)in enumerate(zip(groups,data['class_polynomials'])):
   ck(name+' duplicate length '+str(j),len(co)==len(stored))
   for k,(q,s)in enumerate(zip(co,stored)):ck(name+f' duplicate{j} coefficient{k}',Q(q)==dq(s))

def ledger(mm,solved,remaining,data,allowed,ck,name):
 ck(name+' solved moment indices',data['solved_moments']==solved)
 ck(name+' residual moment indices',data['residual_moments']==remaining)
 for k in solved:ck(name+' solved moment '+str(k),mm[k]==0)
 for k in remaining:ck(name+' residual denominator '+str(k),denominator_ok(mm[k],allowed))

def match_equations(equations,stored,ck,name):
 ck(name+' residual count',len(equations)==len(stored))
 for i,(p,q)in enumerate(zip(equations,stored)):
  ck(name+' nonzero residual '+str(i),bool(p));ck(name+' residual polynomial '+str(i),prim(p)==prim(dp(q)))

def regular(d,ck,name):
 pat=d['pattern'];A=pat['A0'];e=pat['e'];kind=d['type'];T=A*h-23;ex=d['extra'];m=ex['m'];allowed=[h,T]
 ck(name+' variables',d['variables']==['x','y','eta'])
 ck(name+' admissible discrete data',A>0 and A%2==1 and A+2*sum(pat['mu'])==23 and e==len(pat['mu'])-1)
 ck(name+' residual order coverage',2<=e<=8 and 2<=m<=7)
 singles=[];pivot=None
 if kind in ['I','III','V','V5']:
  w,b=ex['theta1'],ex['theta2'];r=2 if kind=='I'else 3
  ck(name+' classes distinct',w>0 and b>0 and w!=b)
  ck(name+' class multiplicities',Counter([w//2]*r+[b//2]*m)==Counter(pat['mu'])and w%2==b%2==0)
  ck(name+' unknown and moment counts',e==r+m-1 and((kind=='I'and r==2)or(r==3)))
  pre=[Q(1),Q(-x)]+([Q(y)]if r==3 else[])
  p=pre+[-val(pre+[Q(0)],h)-(w-b)*Q(h,T)*der(pre+[Q(0)],h)]
  q=fill(A,[(w,ps(p,e))],m,b,m-1,ck,name+' q')
  q.append((w-b)*Q(h,T)*der(q+[Q(0)],h)-val(q+[Q(0)],h))
  ck(name+' first log',(w-b)*Q(h)*der(p,h)+Q(T)*val(p,h)==0)
  ck(name+' second log',(w-b)*Q(h)*der(q,h)-Q(T)*val(q,h)==0)
  groups=[(w,p),(b,q)];mm=moment(A,groups,[],e,ck,name)
  ledger(mm,list(range(1,m)),list(range(m,e+1)),ex,allowed,ck,name)
  eq=[prim(mm[k].n)for k in range(m,e+1)]
  if kind=='III':
   match_equations(eq,ex['original_equations'],ck,name+' original')
   ck(name+' first residual linear y',degree(eq[0],1)==1)
   c1=coef(eq[0],1,1);c0=coef(eq[0],1,0)
   # A common constant normalization must be used for both pivot coefficients.
   q1=Q(c1,dp(ex['C1']));q0=Q(c0,dp(ex['C0']))
   ck(name+' common pivot content',q1==q0 and q1.n.total_degree()==q1.d.total_degree()==0)
   z=Q(-c0,c1);allowed +=[c1]
   sub=[qsubst(mm[k],1,z)for k in [4,5]]
   for j,u in enumerate(sub):ck(name+' substituted denominator '+str(j),denominator_ok(u,allowed))
   eq=[prim(u.n)for u in sub];pivot=(prim(c1),prim(c0),coeffpoly(ex['branch']))
  inner=1;outer=0
 elif kind=='II':
  a1,a2,b=ex['A1'],ex['A2'],ex['b'];ck(name+' three distinct weights',len({a1,a2,b})==3 and min(a1,a2,b)>0)
  ck(name+' class multiplicities',Counter([a1//2,a2//2]+[b//2]*m)==Counter(pat['mu'])and a1%2==a2%2==b%2==0)
  ck(name+' unknown and moment counts',e==m+1)
  S=(T+a1-b)*h-T*x;allowed +=[S];ck(name+' S',S==dp(ex['S']))
  z=Q(h)+(a2-b)*Q(h*(h-x),S)
  r=Q(h-x);s=Q(h)-z
  ck(name+' eliminated log identity',Q(S)*s+(a2-b)*Q(h)*r==0)
  ck(name+' S zero branch nonzero',(a1-b)*(a2-b)!=0)
  ck(name+' S zero remaining term',qsubst((a2-b)*Q(h)*r,0,Q(h)+(a1-b)*Q(h,T))==-(a1-b)*(a2-b)*Q(h*h,T))
  known=[(a1,[Q(1)]+[Q(x)**k for k in range(1,e+1)]),(a2,[Q(1)]+[z**k for k in range(1,e+1)])]
  q=fill(A,known,m,b,m,ck,name+' q');groups=[(b,q)];singles=[(a1,Q(x)),(a2,z)];mm=moment(A,groups,singles,e,ck,name)
  ledger(mm,list(range(1,m+1)),[m+1],ex,allowed,ck,name)
  log=(2*Q(h)-x-z)*val(q,h)+Q(h-x)*(Q(h)-z)*der(q,h)
  ck(name+' logarithmic denominator',denominator_ok(log,allowed));eq=[prim(mm[m+1].n),prim(log.n)];inner=0;outer=0
 elif kind in ['IV','VI','VI4']:
  a,w,b=ex['A1'],ex['theta1'],ex['theta2'];ck(name+' three distinct weights',len({a,w,b})==3 and min(a,w,b)>0)
  ck(name+' class multiplicities',Counter([a//2]+[w//2]*2+[b//2]*m)==Counter(pat['mu'])and a%2==w%2==b%2==0)
  ck(name+' unknown and moment counts',e==m+2)
  L0=Q(1,h-y);L1=(-Q(T,h)-(a-b)*L0)/(w-b);L2=-L0-L1;allowed +=[h-y,L1.n,L2.n]
  ck(name+' L1',L1==dq(ex['L1']));ck(name+' L2',L2==dq(ex['L2']))
  ck(name+' unweighted log sum',L0+L1+L2==0);ck(name+' weighted log sum',a*L0+w*L1+b*L2==-Q(T,h))
  p=[Q(1),Q(-x),(2*Q(h)-x)/L1-Q(h*h-x*h)]
  known=[(a,[Q(1)]+[Q(y)**k for k in range(1,e+1)]),(w,ps(p,e))]
  q=fill(A,known,m,b,m-1,ck,name+' q');q.append(der(q+[Q(0)],h)/L2-val(q+[Q(0)],h))
  ck(name+' pair log',der(p,h)==L1*val(p,h));ck(name+' other log',der(q,h)==L2*val(q,h))
  groups=[(w,p),(b,q)];singles=[(a,Q(y))];mm=moment(A,groups,singles,e,ck,name)
  ledger(mm,list(range(1,m)),[m,m+1,m+2],ex,allowed,ck,name);eq=[prim(mm[k].n)for k in [m,m+1,m+2]];inner=0;outer=1
 else:raise AssertionError(kind)
 match_configuration(groups,singles,ex,allowed,ck,name)
 match_equations(eq,d['equations'],ck,name)
 ck(name+' remaining unknowns',all(degree(q,1)<=0 for q in eq)if len(eq)==2 else all(q.total_degree()>0 for q in eq))
 if len(eq)==3:ck(name+' inner and outer variables',d['inner_variable']==inner and d['outer_variable']==outer)
 return dict(equations=eq,allowed=allowed,pivot=pivot,inner=inner,outer=outer,groups=groups,singletons=singles,moments=mm)

def singular(d,data,ck,name):
 pat=d['pattern'];ex=d['extra'];A=pat['A0'];e=pat['e'];T=A*h-23;a,w,b=ex['A1'],ex['theta1'],ex['theta2'];m=ex['m'];zero=data['zero'];allowed=[h,T]
 ck(name+' singular branch index',zero in [1,2])
 if zero==1:
  yy=Q(h)+(a-b)*Q(h,T);LL=Q(T,(a-b)*h);p=[Q(1),-2*Q(h),Q(x)]
  ck(name+' pair derivative zero',der(p,h)==0)
  known=[(a,[Q(1)]+[yy**k for k in range(1,e+1)]),(w,ps(p,e))]
  q=fill(A,known,m,b,m-1,ck,name+' q');q.append(der(q+[Q(0)],h)/LL-val(q+[Q(0)],h))
  ck(name+' remaining log',der(q,h)==LL*val(q,h));solved=list(range(1,m));rem=[m,m+1,m+2]
 else:
  yy=Q(h)+(a-w)*Q(h,T);LL=Q(T,(a-w)*h);p=[Q(1),Q(-x),(2*Q(h)-x)/LL-Q(h*h-x*h)]
  ck(name+' remaining log',der(p,h)==LL*val(p,h))
  known=[(a,[Q(1)]+[yy**k for k in range(1,e+1)]),(w,ps(p,e))]
  q=fill(A,known,m,b,m-2,ck,name+' q');q.append(-der(q+[Q(0),Q(0)],h));q.append(Q(0))
  pre=moment(A,[(w,p),(b,q)],[(a,yy)],e,ck,name+' before constant')
  shiftedq=q[:-1]+[Q(1)]
  ck(name+' moment m constant pivot',moment(A,[(w,p),(b,shiftedq)],[(a,yy)],m,ck,name+' constant pivot')[m]-pre[m]==-m*b)
  q[-1]=pre[m]/(m*b);ck(name+' other derivative zero',der(q,h)==0)
  solved=list(range(1,m-1))+[m];rem=[m-1,m+1,m+2]
 L0=Q(1)/(Q(h)-yy);ck(name+' surviving unweighted log',L0+LL==0)
 ck(name+' surviving weighted log',a*L0+(b if zero==1 else w)*LL==-Q(T,h))
 groups=[(w,p),(b,q)];singles=[(a,yy)];mm=moment(A,groups,singles,e,ck,name)
 ledger(mm,solved,rem,data['construction'],allowed,ck,name)
 match_configuration(groups,singles,data['construction'],allowed,ck,name)
 eq=[prim(mm[k].n)for k in rem];match_equations(eq,data['equations'],ck,name)
 value=None;residuals=None
 if m==2:
  ck(name+' first equation linear x',degree(eq[0],0)==1)
  a1=coef(eq[0],0,1);a0=coef(eq[0],0,0);value=Q(-a0,a1)
  ck(name+' solved variable',value==dq(data['solved_variable']));ck(name+' solved variable denominator',denominator_ok(value,allowed))
  slope=qsubst(mm[rem[0]],0,Q(x)+1)-mm[rem[0]]
  ck(name+' exact residual pivot',slope==(-2*w if zero==1 else w))
  residualq=[qsubst(mm[k],0,value)for k in rem[1:]]
  for i,u in enumerate(residualq):ck(name+' remaining denominator '+str(i),denominator_ok(u,allowed))
  residuals=[prim(u.n)for u in residualq];match_equations(residuals,data['residuals'],ck,name+' substituted')
  ck(name+' no remaining node variable',all(degree(p,0)<=0 and degree(p,1)<=0 for p in residuals))
 return dict(equations=eq,allowed=allowed,substituted=residuals,value=value)
