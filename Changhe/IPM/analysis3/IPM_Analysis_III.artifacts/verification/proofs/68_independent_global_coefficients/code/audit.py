"""Independent coverage, endpoint, exact aggregation and cached-source audit."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb
import json,gzip,hashlib
import numpy as np
from flint import arb,arb_mat,ctx
import global_check as G
ctx.prec=640;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lo(r):return F(r['lower_exact'])
def hi(r):return F(r['upper_exact'])
def exact_record(r):
 a,b=lo(r),hi(r);assert a<=b
 return G.aa(a).union(G.aa(b))
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
raw=np.load(source,allow_pickle=False);knots=[F.from_float(float(v)) for v in raw['knots']]
spans=[i for i in range(len(knots)-1) if knots[i]<knots[i+1]]
full=json.loads((TOP/'evidence/full.json').read_text());ends=json.loads((TOP/'evidence/ends.json').read_text())
assert full['input_sha256']==ends['input_sha256']==sha(source)
for data in (full,ends):
 assert data['cache_sha256']==sha(G.CACHE)
 assert data['script_sha256']==sha(TOP/'code/global_check.py')
 assert data['proof_sha256']==sha(TOP/'PROOF.md')
assert full['part']=='all' and full['start']==0 and full['stop']==1558
assert full['precision_bits']==512 and full['angular_cells']==128
assert full['radial_subdivisions']==2 and full['outer_cells']==160
expected=[]
for i in spans:
 a,b=knots[i:i+2]
 for j in range(2):expected.append((['spline',i,j],a+(b-a)*j/2,a+(b-a)*(j+1)/2))
for i in range(160):expected.append((['outer',i],knots[-1]+F(i,20),knots[-1]+F(i+1,20)))
assert len(expected)==full['cell_count']==len(full['records'])==3276
for (label,a,b),r in zip(expected,full['records']):
 assert r['label']==label and F(r['left_exact'])==a and F(r['right_exact'])==b
 assert 0<=r['ma_argmin']<128
 for key in ('d','ma_lower','mr_lower','kappa_lower','gradient_upper'):exact_record(r[key])
assert all(expected[j][2]==expected[j+1][1] for j in range(len(expected)-1))
assert F(ends['inner_through_exact'])==expected[0][1]
assert F(ends['outer_from_exact'])==expected[-1][2]
for key,ckey in [('ma_lower','ma_lower'),('mr_lower','mr_lower'),('d_lower','d'),('kappa_lower','kappa_lower')]:
 assert lo(full[key])==min(lo(r[ckey]) for r in full['records'])
assert hi(full['gradient_upper'])==max(hi(r['gradient_upper']) for r in full['records'])
# Half-line inequalities are checked with exact rational endpoints and exact ell.
k=F.from_float(float(raw['k']));ell=1/k;A=2*ell-1;D=4*ell-1;a=F(17,4)
for side in ('inner','outer'):
 r=ends[side];ep=hi(r['P_error_upper']);et=hi(r['T_error_upper']);gr=hi(r['gradient_upper'])
 # Lower records were rounded as balls; the lower endpoint must be no larger
 # than the formula using the outward error endpoints.
 bounds=({'d_lower':D-ep,'ma_lower':1+ell+a*A-a*(ep+et)-gr,'mr_lower':1+ell-A/8-ep/8-gr}
  if side=='inner' else {'d_lower':ell-ep,'ma_lower':1+ell-5*ell/8-5*ep/8-a*et-gr,'mr_lower':1+ell-5*ell/8-5*ep/8-gr})
 for key,val in bounds.items():assert lo(r[key])<=val,(side,key)
 assert lo(r['d_lower'])>0 and lo(r['ma_lower'])>0 and lo(r['mr_lower'])>0
assert lo(ends['inner']['central_check'])<=3*ell-1<=hi(ends['inner']['central_check'])
# Compare all overlapping source-boundary entries against the independently
# prepared and audited 190-digit source cache. No numerics-lane code is used.
with gzip.open(G.CACHE,'rt') as f:cache=json.load(f)
assert cache['spans']==spans and cache['knots']==list(map(str,knots))
local=json.loads((LANE/'proofs/66_source_zero_exclusion/evidence/boundary_cache.json').read_text())
assert local['original_sha256']==cache['input_sha256']
assert local['scalar_sha256']==cache['scalar_sha256']
checks=0
for key,value in local['spans'].items():
 i=spans.index(int(key))
 for glob,loc in [('I_left','IL'),('J_right','JR')]:
  for x,y in zip(cache[glob][i],value[loc]):
   xx,yy=arb(x),arb(y);assert xx.is_finite() and yy.is_finite() and xx.overlaps(yy)
   checks+=1
# Original-data endpoint equations and independent phi-series consistency.
d=G.M.Data();G.check_hash(d)
for x,y in zip(cache['I_left'][0],d.initial('I')):assert arb(x).overlaps(y)
for x,y in zip(cache['J_right'][-1],d.initial('J')):assert arb(x).overlaps(y)
moment_checks=0
for i in sorted(set([0,1,400,641,661,700,1000,1400,1557])):
 span=spans[i];width=knots[span+1]-knots[span]
 for lam in (-526,-122,-58,-6,0,2):
  z=G.aa(width*lam)
  direct=G.M.phi_direct(z);series=G.slow_phi(z,N=256)
  for x,y in zip(direct,series):assert x.overlaps(y);moment_checks+=1
# The independent source audit has already checked the exact spline
# reconstruction by de Boor values, all local Taylor derivatives and the
# Cartesian formulas. This compares every shared boundary, not just a sample.
limits={key:min(lo(full[key]),lo(ends['inner'][key]),lo(ends['outer'][key])) for key in ('ma_lower','mr_lower','d_lower')}
positive=all(v>0 for v in limits.values())
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS' if positive else 'NEGATIVE_GLOBAL_LOWER_BOUND',
 'input_sha256':sha(source),'finite_cells':3276,'angular_cells':128,'full_real_radial_cover':True,
 'source_boundary_overlap_checks':checks,'independent_moment_checks':moment_checks,
 'global_lowers_exact':{k:str(v) for k,v in limits.items()},'global_lowers_diagnostic':{k:float(v) for k,v in limits.items()},
 'full_result_sha256':sha(TOP/'evidence/full.json'),'ends_sha256':sha(TOP/'evidence/ends.json'),
 'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(Path(__file__))}
(TOP/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
