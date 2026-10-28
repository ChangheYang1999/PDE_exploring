"""Independent exact reconstruction of the exported excluded polar boxes."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1];NUM=LANE.parent/'s2-num/work'
def aa(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def sh(b):return hashlib.sha256(b).hexdigest()
def snap(path,name):
 b=path.read_bytes();(TOP/'inputs'/name).write_bytes(b);return b
out=json.loads(snap(NUM/'runs/ZREF/zrefine.json','zrefine.json'))
code=snap(NUM/'zrefine.py','zrefine.py')
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
raw=np.load(source,allow_pickle=False);knots=[F.from_float(float(v)) for v in raw['knots']]
spans=[(a,b) for a,b in zip(knots,knots[1:]) if a<b]
Qlo=F(4559930541822721,562949953421312);Qhi=F(5122880495244367,562949953421312)
checks=[]
for ci,tl,tr,al,ar in out['inside_BP']:
 a,b=spans[ci-5];width=b-a
 # Recover the exact dyadic child positions. The exported values are rounded
 # diagnostics only. Uniqueness follows from the separation of this grid.
 coeff=[]
 for v in (tl,tr):
  q=F((v-float(a))/float(width)).limit_denominator(512)
  assert q.denominator&(q.denominator-1)==0 and 0<=q<=1
  exact=a+q*width;assert abs(float(exact)-v)<1e-12
  coeff.append(exact)
 theta=[]
 for v in (al,ar):
  q=F(v/math.pi).limit_denominator(128*512)
  assert (q*128).denominator&(q*128).denominator-1==0
  assert 0<=q<=F(1,2) and abs(float(aa(q)*arb.pi())-v)<1e-14
  theta.append(q)
 l,r=coeff;v,w=theta
 xmin=aa(l).exp()*(aa(w)*arb.pi()).cos();xmax=aa(r).exp()*(aa(v)*arb.pi()).cos();ymax=aa(r).exp()*(aa(w)*arb.pi()).sin()
 inside=bool(xmin>=aa(Qlo) and xmax<=aa(Qhi) and ymax<=aa(F(1,2)))
 checks.append({'cell':ci,'t0_exact':str(l),'t1_exact':str(r),'theta0_over_pi_exact':str(v),'theta1_over_pi_exact':str(w),'inside_exact_Q':inside,
                'lower_x_margin':str(xmin-aa(Qlo)),'upper_x_margin':str(aa(Qhi)-xmax),'upper_y_margin':str(aa(F(1,2))-ymax)})
assert all(c['inside_exact_Q'] for c in checks)
# Code increments the counter before recursing. Therefore the exported
# count is tree nodes, not terminal leaves. A finite full binary forest
# with T roots and N nodes has (N+T)/2 leaves.
N=out['leaves'];T=out['boxes_refined'];assert (N+T)%2==0
terminal=(N+T)//2;positive=terminal-len(checks)-out['unresolved_count']
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXCLUDED_BOXES_ONLY','archived_summary_sha256':sh((TOP/'inputs/zrefine.json').read_bytes()),
 'exact_Q_containment_checks':checks,'reported_count_is_nodes':N,'root_boxes':T,'terminal_leaves_from_tree_identity':terminal,
 'inside_leaves':len(checks),'positive_leaves_from_tree_identity':positive,'unresolved':out['unresolved_count'],
 'scope':'All excluded boxes lie in the exact certified Q; positive terminal intervals and exact coverage require replay or independent reconstruction.',
 'script_sha256':sh(Path(__file__).read_bytes()),'proof_sha256':sh((TOP/'PROOF.md').read_bytes())}
(TOP/'evidence/summary_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='exact_Q_containment_checks'},indent=2))
