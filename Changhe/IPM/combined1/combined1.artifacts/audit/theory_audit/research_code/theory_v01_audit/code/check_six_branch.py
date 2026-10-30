from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,time,hashlib,sys
sys.set_int_max_str_digits(0);ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
def A(q):
 q=Q(q);return arb(q.numerator)/q.denominator
start=time.monotonic();p=ROOT/'source/stationary_principal.json';data=json.loads(p.read_text());delta=1-1/Q(data['cl']);N,D=delta.numerator,delta.denominator
assert D>12
coef={int(m):Q(v) for m,v in data['branches'][5]['forcing_sin'].items()}
def req(eta,s):return A(eta)/((1-34*A(s))*512*(A(Q(20,21))).sqrt())
requirements={'baseline':(3675,req(Q(1,1572864),Q(1,2**18))),'rebalanced':(1315,req(Q(3,327680),Q(1,2**16))),'graded_T1':(1021,A('0.0000000353781')),'graded_T4':(1063,A(Q(205,6442450944))),'sharp':(511,req(Q(5289,50000000),Q(1,2**13)))}
selected={75}|{k+d for k,v in requirements.values() for d in [0,1]};maximum=max(selected);distance=(arb(D)/(7*N-3*D)).sqrt();count=0;removed=0;values={};rows=[]
def add(k):
 global distance,count,removed
 for ell in range(1,13):
  num=(ell-7)*N+2*D*k
  if num<0:continue
  count+=1
  if not num:removed+=1;continue
  den=(ell+7)*N+2*D*(k-3);assert 0<num<den
  distance*=arb(num)/den
for k in range(5):add(k)
for K in range(maximum+1):
 if K:add(2*K+3);add(2*K+4)
 if K not in selected:continue
 assert removed==1 and count==12*(2*K+5)-8
 cn=arb(count)-A(Q(1,2))+arb(2*count-1).log()/8;Qn=4*cn*cn+A(Q(4,3))
 h=distance*(arb.pi()/2*sum((A(v*v)/(m*m+Qn) for m,v in coef.items()),arb(0))).sqrt();values[K]=h
 rows.append({'K':K,'power_count':count,'distance':distance.str(90),'Qn':Qn.str(90),'H_lower':h.str(90)})
checks=[]
for name,(k,tol) in requirements.items():
 assert values[k]>tol and values[k+1]<tol
 checks.append({'framework':name,'last_excluded_K':k,'first_inconclusive_K':k+1,'H_requirement':tol.str(90),'last_ratio':(values[k]/tol).str(90),'next_ratio':(values[k+1]/tol).str(90)})
 print(name,k,'last ratio',(values[k]/tol).str(20),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'theory_target_sha256':hashlib.sha256((ROOT/'source/theory_v01.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'cutoffs':checks,'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/six_branch.json').write_text(json.dumps(out,indent=2)+'\n');print('elapsed',out['elapsed_seconds'])
