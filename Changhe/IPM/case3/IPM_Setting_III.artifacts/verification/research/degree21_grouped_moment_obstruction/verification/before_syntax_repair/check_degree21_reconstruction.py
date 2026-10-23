"""Result285: reconstruct rational equations; independently verify inner eliminations.
Outer univariate identities are queued for our exact integer determinant gate.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,resource,traceback
from collections import Counter
from exact_degree21 import *
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';E=V/'external';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];jobs=[];details=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save(status='RUNNING'):
 out=dict(status=status,started_utc=t0,updated_utc=utc(),count=len(checks),checks=checks,jobs=jobs,cases=details,proof_sha256=sha(R/'PROOF.md'),types56_proof_sha256=sha(R/'TYPES56_PROOF.md'),driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),inputs_sha256=sha(V/'INPUTS.json'))
 (V/'RECONSTRUCTION.json').write_text(json.dumps(out,indent=2)+'\n')
def matchq(q,stored,name):ck(name,q==qdecode(stored))
def matchp(q,stored,name):ck(name,prim(q)==decode(stored))
def qsubst(q,i,z):
 def ev(p):
  out=Q(0)
  for k in range(degree(p,i),-1,-1):out=out*z+coef(p,i,k)
  return out
 return ev(q.n)/ev(q.d)
def group(co,stored,name):
 ck(name+' length',len(co)==len(stored))
 for k,(q,s)in enumerate(zip(co,stored)):matchq(Q(q),s,name+' coefficient '+str(k))
 def denfactors(q):
  d=q.d
  for f in allowed:
   while degree(d,0)>0 or degree(d,1)>0 or degree(d,2)>0:
    z,rr=divmod(d,f)
    if rr:break
    d=z
  return d.total_degree()==0
 for k,q in enumerate(co):ck(name+' admissible denominator '+str(k),denfactors(Q(q)))
def moments(groups,weights,A,K,name):
 pp=[]
 for j,co in enumerate(groups):
  a=ps(co,K);b=logps(co,K)
  for k in range(K+1):ck(name+' Newton/formal log '+str((j,k)),a[k]==b[k])
  pp.append(a)
 return [Q(A*(h-1)**k)+sum((w*a[k]for w,a in zip(weights,pp)),Q(0))for k in range(K+1)]
def fill_from_moments(A,known,L,b,K):
 co=[Q(1)];targets=[Q(L)]
 for k in range(1,K+1):
  target=-(Q(A*(h-1)**k)+sum((w*pp[k]for w,pp in known),Q(0)))/b;targets.append(target)
  co.append(-(target+sum((co[j]*targets[k-j]for j in range(1,k)),Q(0)))/k)
 return co

def remove(p,recs,admissible,name):
 for j,rec in enumerate(recs):
  f=decode(rec['polynomial']);e=rec['exponent'];ck(name+' allowed factor '+str(j),e>=0 and any(prim(f)==prim(a)for a in admissible),rec)
  p=divexact(p,f**e)
 return prim(p)
def job(f,g,stored,i,name):
 target=decode(stored);ck(name+' eliminated variable gone',degree(target,i)<=0)
 ck(name+' inputs primitive',prim(f)==f and prim(g)==g)
 ck(name+' positive generic degrees',degree(f,i)>0 and degree(g,i)>0)
 jobs.append(dict(name=name,f=encode(f),g=encode(g),resultant=stored,var=i));return target

def positivity(pol,data,name,require=True):
 # The source positivity is for the positive primitive polynomial.
 pol=prim(pol);co=univ(pol);sh=shifted(co,23)
 ck(name+' full original coefficient list',list(map(int,data['coefficients_eta_ascending']))==co)
 ck(name+' full shifted coefficient list',list(map(int,data['coefficients_shifted_ascending']))==sh)
 ck(name+' degree and shift',data['degree']==len(co)-1 and data['shift']==23)
 ck(name+' minimum',int(data['least_shifted_coefficient'])==min(sh))
 ck(name+' recorded sign flags',bool(data['all_strictly_positive'])==all(v>0 for v in sh)and bool(data['all_nonnegative_positive_constant'])==(sh[0]>0 and all(v>=0 for v in sh)))
 if require:ck(name+' every coefficient strictly positive',all(v>0 for v in sh))
 return dict(degree=len(co)-1,least=str(min(sh)),strictly_positive=all(v>0 for v in sh))

def gcd_certificate(f,g,target,name):
 aa=fmpq_poly(univ(f));bb=fmpq_poly(univ(g));d,s,t=aa.xgcd(bb)
 ck(name+' Bezout',s*aa+t*bb==d)
 target=prim(target);tt=fmpq_poly(univ(target));ck(name+' gcd up to nonzero scalar',d*tt.leading_coefficient()==tt*d.leading_coefficient())
 ck(name+' gcd divides both',not(aa%tt)and not(bb%tt))
 return dict(gcd=[str(v)for v in d],s=[str(v)for v in s],t=[str(v)for v in t])

def regular_two_logs(groups,weights,A,name):
 p,q=groups;w,b=weights;T=A*h-21
 ck(name+' first logarithmic relation',(w-b)*Q(h)*der(p,h)+Q(T)*val(p,h)==0)
 ck(name+' second logarithmic relation',(w-b)*Q(h)*der(q,h)-Q(T)*val(q,h)==0)

def regular_single_logs(p,q,L1,L2,name):
 ck(name+' pair log',der(p,h)==L1*val(p,h));ck(name+' other log',der(q,h)==L2*val(q,h))

def readregular(d,mms,baseidx,admissible,name,newtype):
 # Reconstruct M2/3/4 or M4/5/6 and polynomial pseudo-division.
 N,F1,F2=[prim(mms[k].n)for k in [baseidx,baseidx+1,baseidx+2]]
 for k,p in zip(['N0','F1','F2'],[N,F1,F2]):matchp(p,d[k],name+' '+k)
 r1,q1,k1=prem(F1,N,1);r2,q2,k2=prem(F2,N,1);r1=prim(r1);r2=prim(r2)
 ck(name+' pseudo division identities',bool(N))
 if newtype!='VI':
  matchp(r1,d['R1'],name+' R1');matchp(r2,d['R2'],name+' R2');ck(name+' linear remainders',degree(r1,1)==degree(r2,1)==1)
  U=coef(r1,1,1)*coef(r2,1,0)-coef(r1,1,0)*coef(r2,1,1);rawV=resultant(N,r1,1)
  U=remove(U,d['removed_from_U'],admissible,name+' U');vv=remove(rawV,d['removed_from_V'],admissible,name+' V');matchp(U,d['N1'],name+' N1');matchp(vv,d['N2'],name+' N2')
  H=job(U,vv,d['resultant'],0,name+' outer H');pos=positivity(H,d['positivity'],name+' H',newtype=='IV')
  if newtype=='V':
   ck(name+' leading coefficient384T2',coef(N,1,2)==384*(h-21)**2)
   ww=remove(resultant(N,r2,1),d['removed_from_W'],admissible,name+' W');other=d['other_eliminant'];matchp(U,other['N1'],name+' other N1');matchp(ww,other['N2'],name+' other N2');HH=job(U,ww,other['resultant'],0,name+' outer J');positivity(HH,other['positivity'],name+' J',False)
   target=decode(d['common_resultant']);bez=gcd_certificate(H,HH,target,name+' gcd');pos=positivity(target,d['common_positivity'],name+' gcd');return dict(positivity=pos,bezout=bez)
  return dict(positivity=pos)
 # VI: raw y resultants and independent pseudo-remainder auxiliary route.
 U=remove(resultant(N,F1,1),d['removed_from_U'],admissible,name+' U');vv=remove(resultant(N,F2,1),d['removed_from_V'],admissible,name+' V');matchp(U,d['N1'],name+' N1');matchp(vv,d['N2'],name+' N2')
 H=job(U,vv,d['resultant'],0,name+' outer H');positivity(H,d['positivity'],name+' H',False)
 q1=remove(r1,d['removed_from_Q1'],admissible,name+' Q1');q2=remove(r2,d['removed_from_Q2'],admissible,name+' Q2');matchp(q1,d['Q1'],name+' Q1');matchp(q2,d['Q2'],name+' Q2')
 rr,qq,kk=prem(N,q1,1);rr=remove(rr,d['removed_from_R'],admissible,name+' R');matchp(rr,d['R'],name+' R');ck(name+' degrees Q1Q2R',[degree(a,1)for a in [q1,q2,rr]]==[2,2,1])
 ww=remove(resultant(q2,rr,1),d['removed_from_aux_V'],admissible,name+' W');other=d['other_eliminant'];matchp(U,other['N1'],name+' other N1');matchp(ww,other['N2'],name+' other N2');J=job(U,ww,other['resultant'],0,name+' outer J');positivity(J,other['positivity'],name+' J')
 target=decode(d['common_resultant']);aa=fmpq_poly(univ(H));bb=fmpq_poly(univ(J));gg=aa.gcd(bb);mult=Q(1)
 for rec in d['removed_from_common_resultant']:
  f=decode(rec['polynomial']);ck(name+' gcd removable',prim(f)in [prim(h),prim(h-21)]);mult*=Q(f)**rec['exponent']
 bez=gcd_certificate(H,J,prim(target*mult.n),name+' full gcd');pos=positivity(target,d['common_positivity'],name+' reduced gcd');return dict(positivity=pos,bezout=bez)

t0=utc();save()
try:
 for row in json.loads((V/'INPUTS.json').read_text())['files']:ck('input '+row['frozen'],sha(row['frozen'])==row['sha256'])
 for index in range(1,30):
  print('CASE START',index,utc(),flush=True);source=json.loads((E/f'certificate_{index:02d}.json').read_text());pat=source['pattern'];d=source['certificate'];kind=pat['type'];A=pat['A0'];e=pat['e'];T=A*h-21;allowed=[h,T];name=str(index)+' '+kind;info=dict(index=index,pattern=pat)
  ck(name+' weights degree',A+2*sum(pat['mu'])==21 and e==len(pat['mu'])-1)
  if kind in ['I','III','V']:
   w,b=d['weights'];L1,L=d['class_sizes'];ck(name+' class count',Counter([w//2]*L1+[b//2]*L)==Counter(pat['mu']))
   cc=[Q(1),Q(-x)]+([Q(y)]if L1==3 else[]);pc=-val(cc+[Q(0)],h)-(w-b)*Q(h,T)*der(cc+[Q(0)],h);p=cc+[pc]
   pp=ps(p,e);q=fill_from_moments(A,[(w,pp)],L,b,L-1);q.append((w-b)*Q(h,T)*der(q+[Q(0)],h)-val(q+[Q(0)],h));group(p,d['group_polynomials'][0],name+' p');group(q,d['group_polynomials'][1],name+' q');regular_two_logs([p,q],[w,b],A,name);mm=moments([p,q],[w,b],A,e,name)
   for k in range(1,L):ck(name+' eliminated moment '+str(k),mm[k]==0)
   if kind=='I':
    f,g=prim(mm[L].n),prim(mm[L+1].n);matchp(f,d['N1'],name+' N1');matchp(g,d['N2'],name+' N2');hh=job(f,g,d['resultant'],0,name);info['positivity']=positivity(hh,d['positivity'],name)
   elif kind=='III':
    n=prim(mm[3].n);ck(name+' linear pivot',degree(n,1)==1);a=coef(n,1,1);b0=coef(n,1,0);ck(name+' C1',a==decode(d['C1']));ck(name+' C0',b0==decode(d['C0']));z=Q(-b0,a)
    f,g=[prim(qsubst(mm[k],1,z).n)for k in [4,5]];matchp(f,d['regular']['N1'],name+' generic1');matchp(g,d['regular']['N2'],name+' generic2');hh=job(f,g,d['regular']['resultant'],0,name+' generic');info['positivity']=positivity(hh,d['regular']['positivity'],name+' generic')
    zp=d['zero_pivot'];matchp(a,zp['N1'],name+' pivot1');matchp(b0,zp['N2'],name+' pivot2');hh=job(prim(a),prim(b0),zp['resultant'],0,name+' pivot');positivity(hh,zp['positivity'],name+' pivot')
   else:info.update(readregular(d['regular'],mm,4,allowed,name,'V'))
  elif kind=='II':
   aa,bb,w=d['weights'];sizes=d['class_sizes'];L=sizes[-1];ck(name+' classes',sizes[:2]==[1,1]and Counter([aa//2,bb//2]+[w//2]*L)==Counter(pat['mu']))
   S=(T+aa-w)*h-T*x;z=Q(h)+(bb-w)*Q(h*(h-x),S);allowed +=[S];matchp(S,d['S'],name+' S');matchq(z,d['second_node'],name+' secondnode');ck(name+' S zero forbidden',(aa-w)*(bb-w)!=0)
   q=fill_from_moments(A,[(aa,[Q(1)]+[Q(x)**k for k in range(1,e+1)]),(bb,[Q(1)]+[z**k for k in range(1,e+1)])],L,w,L);group(q,d['group_polynomial'],name+' repeated');mm=moments([[Q(1),Q(-x)],[Q(1),-z],q],[aa,bb,w],A,e,name)
   for k in range(1,L+1):ck(name+' eliminated M'+str(k),mm[k]==0)
   f=prim(mm[L+1].n);g=prim(((2*Q(h)-x-z)*val(q,h)+Q(h-x)*(Q(h)-z)*der(q,h)).n);matchp(f,d['N1'],name+' N1');matchp(g,d['N2'],name+' N2');hh=job(f,g,d['resultant'],0,name);info['positivity']=positivity(hh,d['positivity'],name)
  elif kind in ['IV','VI']:
   aa,w,b=d['weights'];ss=d['class_sizes'];ck(name+' classes',ss[0]==1 and ss[1]==2 and Counter([aa//2]+[w//2]*2+[b//2]*ss[2])==Counter(pat['mu']))
   L0=Q(1,h-x);L1=(-Q(T,h)-(aa-b)*L0)/(w-b);L2=-L0-L1;allowed +=[h-x,L1.n,L2.n];matchq(L1,d['L1'],name+' L1');matchq(L2,d['L2'],name+' L2');p=[Q(1),Q(-y),(2*Q(h)-y)/L1-Q(h*h-y*h)]
   if kind=='IV':
    zz=-(Q(A*(h-1)+aa*x+w*y))/b;q=[Q(1),-zz,(2*Q(h)-zz)/L2-Q(h*h)+zz*h]
   else:
    q=fill_from_moments(A,[(aa,[Q(1)]+[Q(x)**k for k in range(1,e+1)]),(w,ps(p,e))],3,b,2);q.append(der(q+[Q(0)],h)/L2-val(q+[Q(0)],h))
   group(p,d['group_polynomials'][0],name+' pair');group(q,d['group_polynomials'][1],name+' other');regular_single_logs(p,q,L1,L2,name);mm=moments([[Q(1),Q(-x)],p,q],[aa,w,b],A,e,name)
   for k in range(1,(2 if kind=='IV'else3)):ck(name+' eliminated M'+str(k),mm[k]==0)
   info.update(readregular(d['regular'],mm,2 if kind=='IV'else3,allowed,name,kind));info['zero_branches_status']='separate gate required'
  elif kind=='exception':
   aa,b=d['weights'];L=e;xx=Q(h)*(Q(1)-Q(4,T));matchq(xx,d['single_node'],name+' singleton');q=fill_from_moments(A,[(aa,[Q(1)]+[xx**k for k in range(1,e+1)])],L,b,L);deriv=val(q,h)+(Q(h)-xx)*der(q,h);matchq(deriv,d['pi_prime_eta'],name+' derivative');ck(name+' n1value',str(deriv.at([0,0,23]))==d['at_n_1']);info['positivity']=positivity(prim(deriv.n),d['positivity'],name)
  elif kind=='two_pairs':
   a,b=d['weights'];z=Q(h,h-1);tt=Q(T);K=tt**2+A*(a+b)*(1+2*z)*tt**2+2*A*(a-b)**2*z*tt+2*(a+b)**2*z*z*tt**2+4*(a-b)**2*z*z*(tt*(a+b)-a*b);matchq(K,d['K'],name+' K');ck(name+' n1value',str(K.at([0,0,23]))==d['at_n_1']);info['positivity']=positivity(prim(K.n),d['positivity'],name)
  else:raise AssertionError(kind)
  details.append(info);save();print('CASE DONE',index,'checks',len(checks),'jobs',len(jobs),utc(),flush=True)
 save('PASS');print('PASS',len(checks),'outer jobs',len(jobs),utc(),flush=True)
except Exception:
 save('FAIL');(V/'reconstruction_traceback.txt').write_text(traceback.format_exc());raise
