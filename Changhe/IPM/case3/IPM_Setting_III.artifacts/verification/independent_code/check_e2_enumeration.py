from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import isqrt,gcd
from collections import Counter
import json,hashlib
R=Path('research/e2_integer_divisor_audit');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,b,e=None):checks.append(dict(name=name,passed=bool(b),evidence=e))
main=json.loads((V/'full1000.result.json').read_text());meta=json.loads((V/'RUN.json').read_text());algebra=json.loads((V/'ALGEBRA_CHECKS.json').read_text())
ck('exact algebra gate',algebra['status']=='PASS'and all(x['passed']for x in algebra['checks']))
ck('completed enumerator',main['status']=='DONE'and main['nmax']==1000)
ck('run input hashes',all(sha(p)==h for p,h in meta['hashes'].items()))
rows=[json.loads(x)for x in(V/'full1000.candidates.jsonl').read_text().splitlines()];counts=[json.loads(x)for x in(V/'full1000.counts.jsonl').read_text().splitlines()]
ck('all candidate records',len(rows)==main['candidates']==main['dual_equation_checks']);ck('unique triples',len({tuple(x[:3])for x in rows})==len(rows))
ck('every n complete',[x['n']for x in counts]==list(range(1,1001))and all(x['status']=='PER_N_DONE'and x['nmax']==1000 for x in counts))
seen=Counter();passing=0;zero_count=0;maxbits=0;positive_c2=True;moments=True;congruences=True;minabs=None
for ii,(n,v,mu,g,h,d)in enumerate(rows):
 seen[n]+=1;k=mu-v-n;D=1+2*v+4*mu+2*n;N=n*n//g;K=n*(25*n-12)+2*N*h
 congruences &= (n>=1 and n<=1000 and v>4*n and k>0 and D==g*d and g==gcd(D,n*n)and 4*h<g and k+1==h*d and K%d==0 and(K//d-12*n*h*h*d-24*n*h*(n-1))%g==0)
 r=F(D,D-1);a=r*(1-F(mu-v,n));S=-(1+2*v*a)/(2*mu);J=(1+2*v*a*a+2*mu*S*S)/(4*mu)
 E=3*r*r-2*(S+a)*r+J+a*S
 positive_c2 &= J-S*S/4>0
 moments &= 1+2*v*a+2*mu*S==0 and 1+2*v*a*a+2*mu*(S*S-2*J)==0
 A=n*n*(2*v+2*n+2*k+1);B=4*n*(k*k+3*n*k+2*n*(n+v));C=4*(4*n-v)*k**3+4*n*(14*n+3*v)*k*k+64*n*n*(n+v)*k+24*n*n*(n+v)**2
 FF=D*D*C+D*(D-1)*B+(D-1)**2*A
 exact=F(FF,32*mu*mu*n*n*(2*mu+n+v)**2)
 if E!=exact:raise AssertionError(('node equation mismatch',ii,n,v,mu))
 passing+=1;zero_count+=int(E==0);maxbits=max(maxbits,abs(FF).bit_length())
 if minabs is None or abs(E)<minabs[0]:minabs=(abs(E),[n,v,mu])
 if ii and ii%25000==0:print(datetime.now(timezone.utc).isoformat(),'rational node checks',ii,flush=True)
ck('every rational node equation reconstructed',passing==len(rows),passing);ck('every M1 M2 exact',moments);ck('every pair nonreal',positive_c2);ck('every arithmetic construction',congruences);ck('no exact E zeros',zero_count==0==main['zeros'])
ck('zeros file empty',(V/'full1000.zeros.jsonl').read_text()=='')
expected=json.loads((V/'EXPECTED_LOOPS.json').read_text());ck('gh total',sum(x['gh']for x in counts)==main['gh']==expected['gh'])
for i,x in enumerate(counts):ck('per-n '+str(x['n']),x['candidates']==seen[x['n']]and x['gh']==expected['per_n'][i]['gh']and x['zeros']==0)
# Separate small-domain implementation: trial divisibility through square roots,
# no sieve and no prime-factor divisor expansion from the C++ program.
def odd_divisors_sqrt(x):
 return sorted({d for a in range(1,isqrt(x)+1)if x%a==0 for d in(a,x//a)if d%2})
small=[];smallgh=0
for n in range(1,61):
 for g in odd_divisors_sqrt(n*n):
  if g<=4:continue
  for h in range(1,(g-1)//4+1):
   smallgh+=1;N=n*n//g;K=n*(25*n-12)+2*N*h
   for d in odd_divisors_sqrt(K):
    if gcd(d,N)!=1:continue
    k=h*d-1;v_num=g*d-6*n-4*k-1
    if k<=0 or v_num%6 or v_num<=24*n:continue
    v=v_num//6
    if (K//d-12*n*h*h*d-24*n*h*(n-1))%g:continue
    small.append([n,v,v+n+k,g,h,d])
ck('small direct square-root enumeration exact',sorted(small)==sorted(x for x in rows if x[0]<=60),dict(gh=smallgh,candidates=len(small)))
pilot=[json.loads(x)for x in(V/'pilot60.candidates.jsonl').read_text().splitlines()];ck('pilot agrees exactly',sorted(pilot)==sorted(small))
# Source counts are an external comparison, not an exhaustiveness premise.
source=[]
for lo,hi,gh,c in [(1,60,13037,232),(61,500,7602175,30077),(501,800,23543001,55309),(801,1000,29725175,54137)]:
 chosen=[x for x in counts if lo<=x['n']<=hi];actual=dict(lo=lo,hi=hi,gh=sum(x['gh']for x in chosen),candidates=sum(x['candidates']for x in chosen));source.append(actual);ck('source comparison '+str(lo),actual['gh']==gh and actual['candidates']==c,actual)
result=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,exact_rational_node_evaluations=passing,maximum_F_integer_bitlength=maxbits,smallest_absolute_E=dict(nu_mu=minabs[1],value=str(minabs[0])),source_comparison=source,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),enumeration_sha256=sha(V/'full1000.result.json'),candidate_sha256=sha(V/'full1000.candidates.jsonl'),scope='No integer zero for1<=n<=1000 with unrestricted nu,mu in this e2 necessary residue problem; n>1000 and full-plane IPM remain OPEN')
(V/'ENUMERATION_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count'],'rational node checks',passing,'Fbits',maxbits,flush=True);print([x for x in checks if not x['passed']]);raise SystemExit(result['status']!='PASS')
