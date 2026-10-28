"""Exact coverage and independent higher-precision exceptional-box replay."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,gzip,hashlib,sys
import numpy as np
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/68_independent_global_coefficients/code'))
import global_check as G
ctx.prec=640;ctx.threads=1
aa=G.aa
QL=F(4559930541822721,562949953421312);QR=F(5122880495244367,562949953421312)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lo(r):return F(r['lower_exact'])
def hi(r):return F(r['upper_exact'])
def ball(r):
 assert lo(r)<=hi(r)
 return aa(lo(r)).union(aa(hi(r)))
path=TOP/'evidence/independent_cover.json.gz'
with gzip.open(path,'rt') as f:out=json.load(f)
assert out['status']=='COMPUTED_PENDING_AUDIT' and out['unresolved']==[]
assert out['script_sha256']==sha(TOP/'code/independent_cover.py')
assert out['proof_sha256']==sha(TOP/'PROOF.md')
assert out['cache_sha256']==sha(G.CACHE)
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert out['input_sha256']==sha(source)
raw=np.load(source,allow_pickle=False);knots=[F.from_float(float(v)) for v in raw['knots']]
spans=[i for i in range(len(knots)-1) if knots[i]<knots[i+1]]
expected=[]
for i in spans:
 l,r=knots[i:i+2]
 for j in range(2):expected.append((['spline',i,j],l+(r-l)*j/2,l+(r-l)*(j+1)/2))
for i in range(160):expected.append((['outer',i],knots[-1]+F(i,20),knots[-1]+F(i+1,20)))
assert len(expected)==3276==out['initial_radial_cells']==len(out['records'])
assert out['initial_angular_cells']==128 and out['bits']==512
assert F(out['inner_through'])==expected[0][1]
assert F(out['outer_from'])==expected[-1][2]
assert all(expected[j][2]==expected[j+1][1] for j in range(len(expected)-1))
roots={};initial_count=0;minima=[]
for r,(label,l,u) in zip(out['records'],expected):
 assert r['label']==label and F(r['t0'])==l and F(r['t1'])==u
 failed=r['failed_initial_angles'];assert failed==sorted(set(failed)) and all(0<=j<128 for j in failed)
 assert r['positive_initial_angles']==128-len(failed)
 initial_count+=r['positive_initial_angles']
 if r['positive_initial_angles']:
  assert lo(r['minimum_positive_initial'])>0;minima.append(lo(r['minimum_positive_initial']))
 for j in failed:roots[(tuple(label),j)]=(l,u,F(j,256),F(j+1,256))
children={key:[] for key in roots};positive=[];inside=[]
for r in out['exceptional_terminal_boxes']:
 key=(tuple(r['parent'][0]),r['parent'][1]);assert key in roots
 box=tuple(F(r[k]) for k in ('t0','t1','a0','a1'));l,u,a,b=box
 L,U,A,B=roots[key]
 assert L<=l<u<=U and A<=a<b<=B and 0<=r['depth']<=12
 assert r['span']==key[0][1]
 children[key].append(box)
 if r['verdict']=='POSITIVE':
  q=ball(r['q']);v=ball(r['u']);low=lo(r['lower']);assert low>0
  # Check the saved distance to the interval rectangle in exact arithmetic.
  def dist(z):return max(F(0),lo(z),-hi(z))
  assert low**2<=dist(r['q'])**2+dist(r['u'])**2
  minima.append(low);positive.append(r)
 elif r['verdict']=='INSIDE_EXACT_Q':
  assert aa(l).exp()*(arb.pi()*aa(b)).cos()>=aa(QL)
  assert aa(u).exp()*(arb.pi()*aa(a)).cos()<=aa(QR)
  assert aa(u).exp()*(arb.pi()*aa(b)).sin()<=arb(1)/2
  inside.append(r)
 else:raise AssertionError(r['verdict'])
for key,boxes in children.items():
 l,u,a,b=roots[key]
 assert boxes and sum(((z[1]-z[0])*(z[3]-z[2]) for z in boxes),F(0))==(u-l)*(b-a)
 for i,x in enumerate(boxes):
  for y in boxes[i+1:]:
   assert not(max(x[0],y[0])<min(x[1],y[1]) and max(x[2],y[2])<min(x[3],y[3]))
assert initial_count+len(positive)==out['positive_terminal_boxes']
assert len(inside)==out['inside_terminal_boxes']
# Recompute all exceptional positive boxes from original polynomials and the
# independently certified Green cache. These are not imported numerics cells.
d=G.M.Data();cache=G.load_cache(d);ell=1/aa(d.k);memo={};recomputed=[]
for r in positive:
 i=r['span'];l,u,a,b=[F(r[k]) for k in ('t0','t1','a0','a1')];key=(i,l,u)
 if key not in memo:
  idx=spans.index(i);rows=d.poly(i).tolist();IL=list(map(arb,cache['I_left'][idx]));JR=list(map(arb,cache['J_right'][idx]))
  mid=aa((l+u)/2);rad=aa((u-l)/2);H,S,rem=G.C.local_series(rows,IL,JR,knots[i],knots[i+1],mid,rad)
  v=arb(0,rad.upper());r2=(2*aa(l)).union(2*aa(u)).exp();P=[];Q=[]
  for n in range(1,262):
   sn=G.C.horner(S[n-1],v)+arb(0,rem[n-1][0])
   sp=G.C.horner([(j+1)*S[n-1][j+1] for j in range(G.C.N)],v)+arb(0,rem[n-1][1])
   P.append(2*n*r2*sn);Q.append(r2*(4*sn+sp))
  memo[key]=(P,Q)
 P,Q=memo[key];th=(arb.pi()*aa(a)).union(arb.pi()*aa(b))
 q=ell-sum((p*(2*n*th).cos() for n,p in enumerate(P,1)),arb(0))
 v=sum((p*(2*n*th).sin() for n,p in enumerate(Q,1)),arb(0))
 assert q.is_finite() and v.is_finite() and q.overlaps(ball(r['q'])) and v.overlaps(ball(r['u']))
 def alo(z):return arb(0) if z.contains(0) else min(abs(z.lower()),abs(z.upper()))
 lower=(arb(alo(q))**2+arb(alo(v))**2).sqrt().lower()
 assert lower>0
 recomputed.append(G.rec(lower))
# Exact independent end formulas from the accepted original-data certificate.
ends=json.loads((LANE/'proofs/68_independent_global_coefficients/evidence/ends.json').read_text())
k=F.from_float(float(raw['k']));ee=1/k
il=2*ee-1-hi(ends['inner']['P_error_upper'])-hi(ends['inner']['T_error_upper'])/2
ol=ee-hi(ends['outer']['P_error_upper'])-hi(ends['outer']['T_error_upper'])/2
assert lo(out['inner_lower'])<=il and lo(out['outer_lower'])<=ol
minima.extend([lo(out['inner_lower']),lo(out['outer_lower'])])
assert lo(out['minimum_positive_outside_Q'])==min(minima)
safe=F(24,100000)
assert min(minima)>=safe and all(lo(z)>=safe for z in recomputed)
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(source),
 'radial_cells':len(expected),'angular_cells':128,'failed_initial_roots':len(roots),
 'positive_initial_boxes':initial_count,'positive_refined_terminal_boxes':len(positive),
 'inside_terminal_boxes':len(inside),'exact_terminal_partitions_checked':len(children),
 'exceptional_boxes_recomputed_at_640_bits':len(recomputed),'distinct_radial_replays':len(memo),
 'safe_global_lower_outside_Q':str(safe),'exact_saved_global_lower':str(min(minima)),
 'full_cover_sha256':sha(path),'proof_sha256':sha(TOP/'PROOF.md'),
 'script_sha256':sha(Path(__file__)),
 'scope':'Outside the exact source rectangle and the origin, |V(X)|/|X|>=0.00024. Inside Q, V070 supplies the unique source.'}
(TOP/'evidence/independent_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
