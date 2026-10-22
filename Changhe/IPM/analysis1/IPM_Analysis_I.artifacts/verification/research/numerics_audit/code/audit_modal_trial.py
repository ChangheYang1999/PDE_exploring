"""Read-only audit of new modal-trial normalization, joins and primitive cancellation."""
import os,sys
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
sys.dont_write_bytecode=True
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];NUM=Path('numerics');sys.path.insert(0,str(NUM/'src'))
from expoly import integral_exp_poly
from trial_green import integ_vec
ctx.prec=160;ctx.threads=1
def aa(x):
 if isinstance(x,F):return arb(x.numerator)/x.denominator
 return arb(x)
def exactfloat(x):return F.from_float(float(x))
rows=[]
for hv in (0.008,0.004,0.001):
 for degree in (3,7):
  cv=hv**(-degree);co=[0.0]*degree+[cv]
  h=aa(exactfloat(hv));c=aa(exactfloat(cv));z=2*h;term=arb(1);series=arb(0)
  for j in range(40):
   series+=term/(degree+j+1);term*=z/(j+1)
  tail=abs(term)/(degree+41)/(1-z/41)
  truth=c*h**(degree+1)*(series+arb(0,tail.upper()))
  val=float(integral_exp_poly(2.0,co,0,hv));vec=float(integ_vec(np.array([2.0]),co,0,hv)[0])
  rows.append({'h':hv,'degree':degree,'coefficient_binary64_exact':str(exactfloat(cv)),'independent_positive_series_interval':truth.str(40),'num_scalar_primitive_difference':val,'num_vector_primitive_difference':vec,'scalar_error':(aa(exactfloat(val))-truth).str(35),'vector_error':(aa(exactfloat(vec))-truth).str(35)})
trial=NUM/'data/trial_h0.008.npz';joins=[];constant=None
if trial.exists():
 with np.load(trial,allow_pickle=False) as d:
  constant=exactfloat(d['rmin'])**2/8
  missing=sorted(set(('D','Ei','S','Aout','Eo','bi','bo','p'))-set(d.files))
  trial_info={'source_sha256':hashlib.sha256(trial.read_bytes()).hexdigest(),'current_Trial_class_missing_keys':missing,'missing_inner_constant_strain_if_rmin_is_exact_dyadic':str(constant),'missing_constant_float':float(constant)}
  if not missing:
   D,Ei,S,A,Eo=d['D'],d['Ei'],d['S'],d['Aout'],d['Eo']
   for m in range(S.shape[0]):
    left=F(int(m==0))+sum(map(exactfloat,D[m]),F(0))+exactfloat(Ei[m,0])-exactfloat(S[m,0])
    right=sum(map(exactfloat,A[m]),F(0))+exactfloat(Eo[m,0])-exactfloat(S[m,-1])
    if left or right:joins.append({'mode':m,'inner_jump_exact_rational':str(left),'inner_jump_float':float(left),'outer_jump_exact_rational':str(right),'outer_jump_float':float(right)})
   trial_info.update(modes=S.shape[0],modes_with_exact_value_join_defect=len(joins),first_join_defects=joins[:8])
else:trial_info={'status':'source trial missing'}
out={'utc':datetime.now(timezone.utc).isoformat(),'source_hashes':{f:hashlib.sha256((NUM/'src'/f).read_bytes()).hexdigest() for f in ['modal_fit.py','trial_green.py','expoly.py']},'primitive_checks':rows,'trial':trial_info,'scope':'Floating primitive evaluation is inaccurate in small cells; the affine normalization omits a fixed contribution, and the current stored artifact is incompatible with the updated class. Exact joins remain open. This is an implementation audit, not an exclusion of corrected trials or exact PDE solutions.'}
(BASE/'research/numerics_audit/evidence/modal_trial_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
