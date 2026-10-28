"""Exact exponential basis, trace and cylinder identities; independent direct products."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
from itertools import combinations
import json,time,sys
from flint import arb,fmpq,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
H=Path(__file__).resolve().parent;B=H.parents[1];start=time.monotonic()
A=lambda q:arb(fmpq(str(q)))
def scalar(v,w,bs):return sum((a*b/(bs[i]+bs[j]) for i,a in v.items() for j,b in w.items()),Q(0))
def exact_norm(exp):return sum((v*w/(a+b) for a,v in exp.items() for b,w in exp.items()),Q(0))
def addterm(d,b,v):d[b]=d.get(b,Q(0))+v
cases=[]
for vals in [['1/100','1/3','2','5'],['1','2','3'],['1','101/100','51/50','103/100'],['1/1000','10','1000']]:
 bs=list(map(Q,vals));basis=[];trace=Q(0);n=len(bs)
 for j in range(n):
  rr={}
  for i in range(j+1):
   num=Q(1);den=Q(1)
   for h in range(j):num*=-bs[i]-bs[h]
   for h in range(j+1):
    if h!=i:den*=bs[h]-bs[i]
   rr[i]=num/den
  assert scalar(rr,rr,bs)==1/(2*bs[j])
  assert all(scalar(rr,prior,bs)==0 for prior in basis)
  normA=2*bs[j]*sum((2*bs[i]*bs[k]*v*w/(bs[i]+bs[k])**3 for i,v in rr.items() for k,w in rr.items()),Q(0))
  assert normA<=Q(j*j+j+1,2)
  trace+=normA;basis.append(rr)
  # Check the complete cylinder square and its integration-by-parts identity.
  cyl={};weighted={}
  for i,v in rr.items():
   addterm(cyl,bs[i],-2*bs[i]*v);addterm(cyl,bs[i]+1,(1+2*bs[i])*v)
   addterm(weighted,bs[i],-bs[i]*v);addterm(weighted,bs[i]+1,bs[i]*v)
  extra=sum((v*w*(Q(2)/(bs[i]+bs[k]+1)-Q(3)/(bs[i]+bs[k]+2)) for i,v in rr.items() for k,w in rr.items()),Q(0))
  assert exact_norm(cyl)==4*exact_norm(weighted)+extra
 trace2=Q(n,2)
 for x,y in combinations(bs,2):trace2+=4*x*y/(x+y)**2
 for x,y,z in combinations(bs,3):trace2+=8*x*y*z/((x+y)*(x+z)*(y+z))
 assert trace==trace2<=Q(n*(n*n+2),6)
 cases.append({'b':vals,'all_orthonormal_basis_checks':True,'all_cylinder_identities':True,'exact_trace':str(trace),'exact_bound':str(Q(n*(n*n+2),6))})
p=H/'constant_bound.json';first=json.loads(p.read_text())
for rel,h in first['dependencies'].items():assert sha256((B/rel).read_bytes()).hexdigest()==h,rel
assert first['code_sha256']==sha256((H/'constant_bound.py').read_bytes()).hexdigest()
annp=B/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json';es={int(m):Q(v) for m,v in json.loads(annp.read_text())['leading_sine_coefficients'].items()}
c=Q(4076476460239181,2251799813685248);delta=1-1/c;astar=7*delta/2-2;rows=[]
for row in first['rows']:
 K=row['K'];M=2*K+4;D=1/A(2*astar+1).sqrt();n=0
 for ell in range(1,13):
  for k in range(M+1):
   a=ell*delta/2+k-2
   if a<astar:continue
   n+=1
   if a!=astar:D*=A(a-astar)/A(a+astar+1)
 assert n==row['n']==12*(2*K+5)-8
 Qn=Q(2*n*(n*n+2)+1,3);assert str(Qn)==row['cylinder_derivative_squared_exact']
 assert str(Q(n*(n*n+2),6))==row['exponential_HS_squared_exact']
 HM=D*(arb.pi()/2*sum((A(e)**2/(m*m+A(Qn)) for m,e in es.items()),arb(0))).sqrt()
 NU=(1-arb(34)/2**18)*512*(arb(20)/21).sqrt()*HM;ratio=1572864*NU
 for key,v in {'D':D,'Hminus_lower':HM,'Route_U_N_lower':NU,'ratio_to_eta':ratio}.items():assert v.overlaps(arb(row[key])),(K,key)
 if K<=779:assert ratio>1
 if K>=780:assert ratio<1
 if K==75:assert ratio>1308
 if K==779:assert ratio>arb('1.0035179')
 if K==780:assert ratio<arb('0.9995471')
 rows.append({'K':K,'all_direct_product_constants_overlap':True,'ratio':ratio.str(70)})
 assert row['coefficient_slots']==6*(60*(K+1)-1770)
assert first['last_K_excluded_by_bound']==779 and first['first_K_not_decided_by_bound']==780
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED exact basis/trace/cylinder identities and independent constants; lead analytical review CORRECT at 2026-10-28T08:17Z','precision_bits':ctx.prec,'small_exact_cases':cases,'independent_rows':len(rows),'last_excluded_K':779,'first_K_not_decided_by_formula':780,'K75_ratio_strict_lower':1308,'K779_ratio_strict_lower':'1.0035179','K780_ratio_strict_upper':'0.9995471','rows':rows,'dependencies':{str(q.relative_to(B)):sha256(q.read_bytes()).hexdigest() for q in [p,H/'constant_bound.py',H.parent/'PROOF.md',annp,B/'26_uniform_family_gap/verification/audit_algebra.json']},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
H.joinpath('audit_derivative.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['rows','small_exact_cases']},indent=2))
