"""Independent reconstruction of all eight zero-logarithm branches."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,resource
from exact_degree21 import *
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';E=V/'external';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];details=[];t0=utc()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save(status):
 out=dict(status=status,started_utc=t0,updated_utc=utc(),count=len(checks),checks=checks,branches=details,proof_sha256=sha(R/'ZERO_BRANCH_PROOF.md'),driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),inputs_sha256=sha(V/'INPUTS.json'),universal_sha256=sha(V/'UNIVERSAL_NEWTON.json'))
 (V/'BRANCH_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def subst(q,z):
 def ev(p):
  o=Q(0)
  for k in range(degree(p,1),-1,-1):o=o*z+coef(p,1,k)
  return o
 return ev(q.n)/ev(q.d)
def moments(A,aa,xx,w,p,b,q,K):
 pp,qq=ps(p,K),ps(q,K)
 return [Q(A*(h-1)**k)+aa*xx**k+w*pp[k]+b*qq[k]for k in range(K+1)]
def mq(q,s,n):ck(n,q==qdecode(s))
def mp(q,s,n):ck(n,prim(q)==prim(decode(s)))
def admiss(q,T,n):
 d=q.d
 for p in [prim(h),prim(T)]:
  while d.total_degree()>0:
   s,r=divmod(d,p)
   if r:break
   d=s
 ck(n,d.total_degree()==0,str(q.d))
def bezout(f,g,stored,n):
 a,b=fmpq_poly(univ(f)),fmpq_poly(univ(g));d,s,t=a.xgcd(b);goal=fmpq_poly(univ(prim(decode(stored))))
 ck(n+' explicit identity',s*a+t*b==d);ck(n+' target',d*goal.leading_coefficient()==goal*d.leading_coefficient());ck(n+' divisibility',not(a%goal)and not(b%goal))
 return dict(d=[str(c)for c in d],s=[str(c)for c in s],t=[str(c)for c in t])
def gaussian(matrix):
 a=[list(map(fmpq,row))for row in matrix];sign=1;d=fmpq(1)
 for j in range(len(a)):
  ii=next((i for i in range(j,len(a))if a[i][j]),None)
  if ii is None:return fmpq(0)
  if ii!=j:a[ii],a[j]=a[j],a[ii];sign=-sign
  p=a[j][j];d*=p
  for i in range(j+1,len(a)):
   t=a[i][j]/p
   for k in range(j+1,len(a)):a[i][k]-=t*a[j][k]
   a[i][j]=0
 return sign*d
save('RUNNING')
try:
 u=json.loads((V/'UNIVERSAL_NEWTON.json').read_text());ck('universal320PASS',u['status']=='PASS'and u['count']==320 and all(c['passed']for c in u['checks']));ck('bound library',u['library_sha256']==sha('independent_code/exact_degree21.py'))
 for index in [5,9,20,11]:
  file=E/f'certificate_{index:02d}.json';s=json.loads(file.read_text());d=s['certificate'];A=s['pattern']['A0'];aa,w0,b0=d['weights'];T=A*h-21;kind=s['pattern']['type']
  for record in d['zero_branches']:
   zero=record['zero_weight'];name=f'{index} {kind} zero{zero}';info=dict(name=name,source_sha256=sha(file));ck(name+' singleton weight distinct',aa!=w0 and aa!=b0)
   if kind=='IV' or zero==w0:
    w=zero;b=b0 if zero==w0 else w0;xx=Q(h)*(Q(1)+Q(aa-b,T));L0=1/(Q(h)-xx);p=[Q(1),Q(-2*h),Q(y)];mq(xx,record['single_node'],name+' x');ck(name+' zero pair',der(p,h)==0)
    c1=(Q(A*(h-1))+aa*xx+2*w*h)/b
    if kind=='IV':q=[Q(1),c1,der([Q(1),c1,Q(0)],h)/(-L0)-val([Q(1),c1,Q(0)],h)]
    else:
     c2=(Q(A*(h-1)**2)+aa*xx**2+w*(4*Q(h*h)-2*y)+b*c1**2)/(2*b)
     cc=[Q(1),c1,c2,Q(0)];q=cc[:-1]+[der(cc,h)/(-L0)-val(cc,h)]
    ck(name+' nonzero other log',(aa-b)*L0==-Q(T,h));ck(name+' other log identity',der(q,h)==-L0*val(q,h))
    mm=moments(A,aa,xx,w,p,b,q,4 if kind=='IV'else 5)
    for k in range(1,2 if kind=='IV'else 3):ck(name+' eliminated M'+str(k),mm[k]==0)
    selected=[mm[k]for k in ([2,3,4]if kind=='IV'else[3,4,5])]
   else:
    ck(name+' zero triple recognized',zero==b0);w,b=w0,b0;xx=Q(h)*(Q(1)+Q(aa-w,T));L0=1/(Q(h)-xx);p=[Q(1),Q(-y),(2*Q(h)-y)/(-L0)-Q(h*h-y*h)];c1=(Q(A*(h-1))+aa*xx+w*y)/b;c2=-3*Q(h*h)-2*c1*h;q0=[Q(1),c1,c2,Q(0)];mm0=moments(A,aa,xx,w,p,b,q0,3);q=q0[:-1]+[mm0[3]/(3*b)];mm=moments(A,aa,xx,w,p,b,q,5)
    mq(xx,record['single_node'],name+' x');ck(name+' nonzero pair log',(aa-w)*L0==-Q(T,h));ck(name+' pair log identity',der(p,h)==-L0*val(p,h));ck(name+' zero triple derivative',der(q,h)==0);ck(name+' M1',mm[1]==0);ck(name+' M3',mm[3]==0);selected=[mm[k]for k in [2,4,5]]
   for j,qv in enumerate([xx]+p+q+selected):admiss(qv,T,name+' admissible denominator'+str(j))
   for j,(qv,stored)in enumerate(zip(selected,record['free_y_moments'])):mq(qv,stored,name+' free moment'+str(j))
   ck(name+' three equations',len(record['free_y_moments'])==3)
   if kind=='IV':
    qv=selected[0];ck(name+' constant M2 pivot',Q(coef(qv.n,1,1),qv.d)==-2*w);yy=Q(-coef(qv.n,1,0),coef(qv.n,1,1));mq(yy,record['determined_y'],name+' determined product');rem=[subst(a,yy)for a in selected[1:]]
    for j,qv in enumerate(rem):mq(qv,record['remaining_moments'][j],name+' remaining'+str(j));admiss(qv,T,name+' remaining denominator'+str(j))
    info['bezout']=bezout(rem[0].n,rem[1].n,record['gcd'],name);ck(name+' gcd1',prim(decode(record['gcd']))==C.constant(1))
   else:
    pol=[prim(qv.n)for qv in selected];ck(name+' degrees',[degree(pv,1)for pv in pol]==([1,2,2]if zero==4 else[2,4,5]))
    for j,pv in enumerate(pol):mp(pv,record['equations'][j],name+' equation'+str(j))
    rr=[]
    for j,item in enumerate(record['resultants']):
     inds=item['indices'];ck(name+' pair indices'+str(j),inds==[0,j+1]);matrix=sylv(pol[inds[0]],pol[inds[1]],1);det,divs,swaps=bareiss(matrix);mp(det,item['polynomial'],name+' full resultant'+str(j));rr.append(prim(det))
     for eta in [23,24,41]:ck(name+f' Gaussian{j}/{eta}',gaussian([[p(0,0,eta)for p in row]for row in matrix])==det(0,0,eta))
     info.setdefault('resultants',[]).append(dict(degree=degree(det,2),divisions=divs,swaps=swaps))
    ck(name+' resultant degrees',[degree(pv,2)for pv in rr]==([16,18]if zero==4 else[24,30]));info['bezout']=bezout(rr[0],rr[1],record['gcd'],name);ck(name+' gcd T power',prim(decode(record['gcd']))==prim(T**(4 if zero==4 else 8)))
   goal=prim(decode(record['gcd']));shift=shifted(univ(goal),23);saved=record['positivity'];ck(name+' full shifted gcd',list(map(int,saved['coefficients_shifted_ascending']))==shift);ck(name+' strictly positive',all(v>0 for v in shift));info['gcd']=encode(goal);details.append(info);save('RUNNING');print('BRANCH',name,len(checks),utc(),flush=True)
 ck('all eight branches',len(details)==8);save('PASS');print('PASS',len(checks),utc(),flush=True)
except Exception:
 save('FAIL');(V/'branches_traceback.txt').write_text(traceback.format_exc());raise
