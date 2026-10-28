"""Original-data global nonzero cover with an exact source rectangle."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,hashlib,time,gzip
from flint import arb,arb_mat,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/68_independent_global_coefficients/code'))
import global_check as G
ctx.prec=512;ctx.threads=1
QL=F(4559930541822721,562949953421312);QR=F(5122880495244367,562949953421312)
aa=G.aa;rec=G.rec
start=time.monotonic();d=G.M.Data();cache=G.load_cache(d);ell=1/aa(d.k)
# 128 initial angular cells and two radial cells per original span.
ang=G.Angular(128);records=[];exceptional=[];inside_count=0;positive_count=0;unresolved=[]
minimum=arb.pos_inf();range_cache={}
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def inside(l,r,a,b):
 return bool(aa(l).exp()*(arb.pi()*aa(b)).cos()>=aa(QL)
       and aa(r).exp()*(arb.pi()*aa(a)).cos()<=aa(QR)
       and aa(r).exp()*(arb.pi()*aa(b)).sin()<=arb(1)/2)
def vlo(q,u):
 def alo(v):return arb(0) if v.contains(0) else min(abs(v.lower()),abs(v.upper()))
 x,y=alo(q),alo(u)
 return (arb(x)**2+arb(y)**2).sqrt().lower()
def ranges(i,l,r,rows,IL,JR):
 key=(i,l,r)
 if key in range_cache:return range_cache[key]
 t0,t1=d.knots[i:i+2];mid=aa((l+r)/2);rad=aa((r-l)/2)
 H,S,rem=G.C.local_series(rows,IL,JR,t0,t1,mid,rad)
 vv=arb(0,rad.upper());r2=(2*aa(l)).union(2*aa(r)).exp();P=[];Q=[]
 for n in range(1,262):
  ss=G.C.horner(S[n-1],vv)+arb(0,rem[n-1][0])
  sp=G.C.horner([(j+1)*S[n-1][j+1] for j in range(G.C.N)],vv)+arb(0,rem[n-1][1])
  P.append(2*n*r2*ss);Q.append(r2*(4*ss+sp))
 range_cache[key]=(P,Q)
 return P,Q
def refine(i,l,r,a,b,rows,IL,JR,depth,parent):
 global minimum,inside_count,positive_count
 item={'parent':parent,'span':i,'t0':str(l),'t1':str(r),'a0':str(a),'a1':str(b),'depth':depth}
 if inside(l,r,a,b):
  item['verdict']='INSIDE_EXACT_Q';inside_count+=1;exceptional.append(item);return
 P,Q=ranges(i,l,r,rows,IL,JR)
 t=(arb.pi()*aa(a)).union(arb.pi()*aa(b))
 q=ell-sum((p*(2*n*t).cos() for n,p in enumerate(P,1)),arb(0))
 u=sum((v*(2*n*t).sin() for n,v in enumerate(Q,1)),arb(0));v=vlo(q,u)
 assert q.is_finite() and u.is_finite() and arb(v).is_finite()
 if v>0:
  item.update(verdict='POSITIVE',q=rec(q),u=rec(u),lower=rec(v))
  positive_count+=1;minimum=min(minimum,v);exceptional.append(item);return
 if depth>=12:
  item.update(verdict='UNRESOLVED',q=rec(q),u=rec(u));unresolved.append(item);exceptional.append(item);return
 if aa(b-a)*arb.pi()>=aa(r-l):
  m=(a+b)/2;refine(i,l,r,a,m,rows,IL,JR,depth+1,parent);refine(i,l,r,m,b,rows,IL,JR,depth+1,parent)
 else:
  m=(l+r)/2;refine(i,l,m,a,b,rows,IL,JR,depth+1,parent);refine(i,m,r,a,b,rows,IL,JR,depth+1,parent)

def add_batch(label,l,r,P,Q,context=None):
 global minimum,positive_count
 qs=[ell-z for z in ang.dot(P,ang.c2)];us=ang.dot(Q,ang.s2);vals=[];failed=[]
 for j,(q,u) in enumerate(zip(qs,us)):
  assert q.is_finite() and u.is_finite();v=vlo(q,u)
  if v>0:vals.append(v);minimum=min(minimum,v);positive_count+=1
  else:failed.append(j)
 record={'label':label,'t0':str(l),'t1':str(r),'positive_initial_angles':128-len(failed),'failed_initial_angles':failed,
         'minimum_positive_initial':rec(min(vals)) if vals else None}
 records.append(record)
 for j in failed:
  assert context is not None,'Unexpected unresolved outer box'
  i,rows,IL,JR=context;refine(i,l,r,F(j,256),F(j+1,256),rows,IL,JR,0,[label,j])
 if len(records)%80==0:emit(stage='cover',radial_cells=len(records),minimum=arb(minimum).str(16),inside=inside_count,unresolved=len(unresolved),seconds=time.monotonic()-start)

for idx,i in enumerate(d.spans):
 rows=d.poly(i).tolist();IL=list(map(arb,cache['I_left'][idx]));JR=list(map(arb,cache['J_right'][idx]));a,b=d.knots[i:i+2]
 range_cache.clear()
 for sub in range(2):
  l=a+(b-a)*sub/2;r=a+(b-a)*(sub+1)/2;P,Q=ranges(i,l,r,rows,IL,JR)
  add_batch(['spline',i,sub],l,r,P,Q,(i,rows,IL,JR))
pe,qe,_,_=G.outer_eps(d,cache)
for i in range(160):
 l=F(i,20);r=F(i+1,20);mid=(l+r)/2;rad=(r-l)/2
 P=[p.range(mid,rad) for p in pe];Q=[p.range(mid,rad) for p in qe]
 add_batch(['outer',i],d.tp+l,d.tp+r,P,Q)
# End error bounds of topic68 control both velocity components.
ends=json.loads((LANE/'proofs/68_independent_global_coefficients/evidence/ends.json').read_text())
def upper(x):return aa(F(x['upper_exact']))
inn=ends['inner'];out=ends['outer'];A=2*ell-1
inner_lower=A-upper(inn['P_error_upper'])-upper(inn['T_error_upper'])/2
outer_lower=ell-upper(out['P_error_upper'])-upper(out['T_error_upper'])/2
assert inner_lower>0 and outer_lower>0
minimum=min(minimum,inner_lower.lower(),outer_lower.lower())
result={'date':now(),'status':'COMPUTED_PENDING_AUDIT' if not unresolved else 'UNRESOLVED','input_sha256':d.sha,
 'cache_sha256':hashlib.sha256(G.CACHE.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),'bits':512,'initial_angular_cells':128,
 'initial_radial_cells':len(records),'positive_terminal_boxes':positive_count,'inside_terminal_boxes':inside_count,
 'unresolved':unresolved,'minimum_positive_outside_Q':rec(minimum),'inner_through':str(d.tm),'outer_from':str(d.tp+8),
 'inner_lower':rec(inner_lower),'outer_lower':rec(outer_lower),'records':records,'exceptional_terminal_boxes':exceptional,
 'seconds':time.monotonic()-start}
with gzip.open(TOP/'evidence/independent_cover.json.gz','wt') as f:json.dump(result,f)
emit(stage='finished',minimum=arb(minimum).str(30),unresolved=len(unresolved),seconds=result['seconds'])
