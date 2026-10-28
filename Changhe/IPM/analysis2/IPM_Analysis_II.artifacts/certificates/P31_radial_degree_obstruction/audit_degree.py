"""Independent gamma-product evaluation and exact compression matrix checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
H=Path(__file__).resolve().parent;B=H.parents[1];start=time.monotonic()
p=H/'degree_bound.json';first=json.loads(p.read_text())
assert first['code_sha256']==sha256((H/'degree_bound.py').read_bytes()).hexdigest()
for rel,v in first['dependencies'].items():assert sha256((B/rel).read_bytes()).hexdigest()==v,rel
# Exact Gram-Schmidt in a basis normalized to have endpoint one.
def dot(v,w,exps):return sum((a*b/(exps[i]+exps[j]+1) for i,a in v.items() for j,b in w.items()),Q(0))
def clean(v):return {i:a for i,a in v.items() if a}
tests=[]
for vals in [['-49/100','-2/5','-1/7','1/3','9/5','11'],['0','1/2','1','5/2','7'],['-1/3','1/9','4/3','14/9']]:
 exps=list(map(Q,vals));qs=[]
 for j in range(len(exps)):
  v={j:Q(1)}
  for q in qs:
   z=dot(v,q,exps)/dot(q,q,exps)
   v=clean({i:v.get(i,Q(0))-z*q.get(i,Q(0)) for i in v.keys()|q.keys()})
  endpoint=sum(v.values(),Q(0));assert endpoint!=0
  v={i:x/endpoint for i,x in v.items()}
  assert dot(v,v,exps)==1/(2*exps[j]+1)
  qs.append(v)
 matrix=[]
 for i,qi in enumerate(qs):
  row=[]
  for j,qj in enumerate(qs):
   Bq={k:x*exps[k] for k,x in qj.items()}
   value=dot(Bq,qi,exps)/dot(qi,qi,exps)
   expected=exps[j] if i==j else (2*exps[i]+1 if i<j else Q(0))
   assert value==expected;row.append(str(value))
  matrix.append(row)
 tests.append({'exponents':vals,'endpoint_norms_verified':True,'dilation_matrix_equals_compressed_T_minus_half':True,'rational_matrix':matrix})
c=Q(4076476460239181,2251799813685248);delta=1-1/c;astar=7*delta/2-2
annp=B/'23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json'
es={int(m):Q(v) for m,v in json.loads(annp.read_text())['leading_sine_coefficients'].items()}
rows=[]
for row in first['all_rows']:
 K=row['K'];M=2*K+4;S=Q(0);sum_a2=Q(0);sum_l2=Q(0);count=0
 logD=-arb(2*astar+1).log()/2
 for ell in range(1,13):
  lo=max(0,int(((7-ell)*delta/2).ceil()));n=M-lo+1;a=ell*delta/2-2
  sum_k=Q(n*(lo+M),2)
  sum_k2=Q(M*(M+1)*(2*M+1)-(lo-1)*lo*(2*lo-1),6)
  S+=n*(2*a+1)+2*sum_k
  sum_a2+=n*a*a+2*a*sum_k+sum_k2
  sum_l2+=n*(2*a+1)**2+4*(2*a+1)*sum_k+4*sum_k2
  count+=n
  firstk=lo+int(ell==7)
  b=(ell-7)*delta/2;d=(ell+7)*delta/2-3
  assert firstk+b>0 and firstk+d>0
  logD+=arb(M+1+b).lgamma()-arb(firstk+b).lgamma()+arb(firstk+d).lgamma()-arb(M+1+d).lgamma()
 assert str(S)==row['S_exact'] and count==row['exponent_count']
 D=logD.exp();C=(4*arb(S)**2/arb.pi()**2+arb(1)/4).sqrt()
 Cf=arb(sum_a2+(S*S-sum_l2)/2).sqrt()
 low=D*(arb.pi()/2*sum((arb(em)**2/(m*m+(1+2*C)**2) for m,em in es.items()),arb(0))).sqrt()
 N=512*(arb(20)/21).sqrt()*(1-arb(34)/2**18)*low;ratio=1572864*N
 comparisons={'D':D,'C_Volterra':C,'C_Frobenius':Cf,'Hminus_lower':low,'Route_U_N_lower':N,'ratio_to_eta':ratio}
 assert all(v.overlaps(arb(row[k])) for k,v in comparisons.items())
 assert C<Cf
 if K<=349:assert ratio>1
 if K>=350:assert ratio<1
 if K==75:assert ratio>233
 if K==349:assert ratio>arb('1.0019782')
 if K==350:assert ratio<arb('0.9917770')
 rows.append({'K':K,'all_constants_overlap':True,'ratio':ratio.str(75)})
assert first['last_K_excluded_by_bound']==349 and first['next_K_not_decided_by_bound']==350
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED independent constants and exact compressed-operator algebra; lead analytical review CORRECT at 2026-10-28T08:17Z','precision_bits':ctx.prec,'exact_compression_tests':tests,'independent_gamma_product_rows':len(rows),'last_excluded_K':349,'first_K_not_decided_by_formula':350,'K75_ratio_strict_lower':233,'K349_ratio_strict_lower':'1.0019782','K350_ratio_strict_upper':'0.9917770','rows':rows,'dependencies':{str(q.relative_to(B)):sha256(q.read_bytes()).hexdigest() for q in [p,H/'degree_bound.py',H.parent/'PROOF.md',annp,B/'26_uniform_family_gap/verification/audit_algebra.json']},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
H.joinpath('audit_degree.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['rows','exact_compression_tests']},indent=2))
