from pathlib import Path
from fractions import Fraction as F
from math import isqrt,comb
from hashlib import sha256
from datetime import datetime,timezone
import json,os,time,sys
sys.set_int_max_str_digits(0)
B=Path('research/source013_moment_refinement');V=B/'verification';A=Path('research/source013_norms_actual_audit/verification');start=datetime.now(timezone.utc).isoformat();tic=time.monotonic();checks=0
assert os.sched_getaffinity(0)=={40}and os.getpriority(os.PRIO_PROCESS,0)>=19

def ck(b):
 global checks
 checks+=1;assert b
def h(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def put(p,d):
 with p.open('x')as f:json.dump(d,f,indent=2);f.write('\n')
def floorroot(a,k):
 lo=0;hi=1<<((a.bit_length()+k-1)//k)
 while lo+1<hi:
  m=(lo+hi)//2
  if m**k<=a:lo=m
  else:hi=m
 return hi if hi**k<=a else lo
def roots(p,k,digits=28):
 ck(p>=0);S=10**digits;n=floorroot((p.numerator*S**k)//p.denominator,k);lo=F(n,S);hi=lo if lo**k==p else F(n+1,S);ck(lo**k<=p<=hi**k);return lo,hi
files={}
for name in ['norms_v01.json','check_v01.json','weighted_actual_review_v02.json','unweighted_actual_review_v02.json']:
 src=A/name;dst=B/'source'/name;os.link(src,dst);files[str(dst)]=h(src);ck(h(dst)==files[str(dst)])
c=read(A/'check_v01.json');ck(c['status']=='PASS');d=read(A/'norms_v01.json');review=read(A/'weighted_actual_review_v02.json');ck(review['status']=='BOUND'and review['result_sha256']==c['weighted_result_sha256']);ck(review['bindings'][str(A/'norms_v01.json')]==h(A/'norms_v01.json'));ck(review['bindings'][str(A/'check_v01.json')]==h(A/'check_v01.json'))
T=d['weighted']['tensor_energies'];L=[F(x['lower_exact'])for x in T];U=[F(x['upper_exact'])for x in T];old=list(U);U[1]=min(U[1],roots(U[0]*U[2],2)[1]);ck(U[1]**2>=U[0]*U[2]or U[1]==old[1]);ck(L[1]<=U[1]<old[1]);EmL=[sum(comb(m,j)*L[j]for j in range(m+1))for m in range(4)];EmU=[sum(comb(m,j)*U[j]for j in range(m+1))for m in range(4)];integers=[]
for j in range(4):
 lo=roots(EmL[j],2)[0];hi=roots(EmU[j],2)[1];ck(lo*lo<=EmL[j]<=EmU[j]<=hi*hi);integers.append({'order':j,'energy_lower_exact':str(EmL[j]),'energy_upper_exact':str(EmU[j]),'norm_interval_exact':[str(lo),str(hi)]})
ck(EmU[1]>0);p=EmL[2]**11/EmU[1];ql=roots(p,20)[0];lower=max(F(integers[2]['norm_interval_exact'][0]),ql);upper=roots(EmU[2]**9*EmU[3],20)[1];ck(upper**20>=EmU[2]**9*EmU[3]);ck(lower**2<=EmL[2]or lower**20<=p);prior=list(map(F,d['weighted']['fractional_norm_interval_exact']));ck(prior[0]<=lower<=upper<prior[1]);ck(upper<F('0.0072'))
result={'source':d['source'],'tensor_energies':[{'order':j,'lower_exact':str(L[j]),'upper_exact':str(U[j])}for j in range(4)],'old_T1_upper_exact':str(old[1]),'integer_norms':integers,'fractional_order_exact':'21/10','fractional_norm_interval_exact':[str(lower),str(upper)]};put(V/'result_v01.json',result)
def display(x,n=22):
 a,b=map(F,x);S=10**n;l=a.numerator*S//a.denominator;u=-((-b.numerator*S)//b.denominator)
 def text(k):return str(k//S)+'.'+str(k%S).zfill(n)
 out=[text(l),text(u)];ck(F(out[0])<=a<=b<=F(out[1]));return out
out={'T1_upper':str(U[1]),'integer_norms':[{'order':r['order'],'interval':display(r['norm_interval_exact'])}for r in integers],'fractional_interval':display(result['fractional_norm_interval_exact'])};put(V/'display_v01.json',out)
for n,z in files.items():ck(h(Path(n))==z)
put(V/'bindings_v01.json',{'created_utc':start,'files':files});put(V/'check_v01.json',{'status':'PASS','started_utc':start,'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tic,'checks':checks,'input_result_sha256':h(A/'norms_v01.json'),'output_sha256':h(V/'result_v01.json'),'scope':'Whole-plane moment inequality refinement of the same certified P-S1 residual. No closure or existence.'});print(json.dumps(out,indent=2))
