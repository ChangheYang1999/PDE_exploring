"""Exact all-mode vertical-axis spline jump; no floating differentiation."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import hashlib,json,sys,time
import numpy as np
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sys.path.insert(0,str(LANE/'proofs/04_modal_scalar/code'))
import recompute as R
SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic();digest=sha(SOURCE)
assert digest=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
data=np.load(SOURCE,allow_pickle=False)
assert int(data['p'])==7 and int(data['M'])==260
knots=[F(float(x)) for x in data['knots']];i=700
assert knots[i]==F(4958764014967233,2251799813685248)
assert knots[i-1]<knots[i]<knots[i+1]
co=[sum((F(float(data['S'][m,j]))*((-1)**m) for m in range(260)),F(0)) for j in range(data['S'].shape[1])]
T=knots[:];c=co[:]
for degree in range(7,0,-1):
    denominators=[T[j+degree+1]-T[j+1] for j in range(len(c)-1)]
    assert all(v>0 for v in denominators)
    c=[degree*(c[j+1]-c[j])/denominators[j] for j in range(len(c)-1)]
    T=T[1:-1]
assert T==knots[7:-7] and len(c)==len(T)-1
left,right=c[i-8],c[i-7];jump=right-left
assert jump!=0
polys=[R.deboor_poly(knots,co,7,i-1),R.deboor_poly(knots,co,7,i)]
widths=[knots[i]-knots[i-1],knots[i+1]-knots[i]]
seventh=[p[7]*factorial(7)/w**7 for p,w in zip(polys,widths)]
assert seventh==[left,right]
leftjets=R.jets(polys[0],widths[0],True);rightjets=R.jets(polys[1],widths[1],False)
assert leftjets==rightjets
out={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','source_sha256':digest,'source':str(SOURCE),
     'knot_index':i,'knot_exact':str(knots[i]),'axis_modes':260,'axis_weights':'(-1)^m',
     'axis_seventh_left_exact':str(left),'axis_seventh_right_exact':str(right),'axis_seventh_jump_exact':str(jump),
     'scaling_sixth_jump_exact':str(-jump),'nonzero_axis_jump':True,'independent_polynomial_agreement':True,
     'exact_join_orders_checked':list(range(7)),'all_arithmetic':'exact Fraction, binary64 inputs interpreted as dyadic rationals',
     'conclusion':'Every smooth annular cutoff of K equal to1 near this knot is outside H_full, already through its scalar coordinate',
     'proof_sha256':sha(TOP/'PROOF.md'),'script_sha256':sha(Path(__file__)),'polynomial_evaluator_sha256':sha(Path(R.__file__)),
     'seconds':time.monotonic()-start}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.endswith('_exact')},indent=2))
