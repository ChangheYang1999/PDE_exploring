"""Read-only executable check of the modal strain's fixed affine contribution."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,ast,json,hashlib
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
import sympy as sp
BASE=Path(__file__).resolve().parents[3];NUM=BASE.parent/'ipmA-num'
sys.path.insert(0,str(NUM/'src'))
from modal_fit import Trial
source=NUM/'src/modal_fit.py';text=source.read_text();tree=ast.parse(text)
exprs={}
for node in ast.walk(tree):
 if isinstance(node,ast.Assign):
  for target in node.targets:
   if isinstance(target,ast.Name) and target.id in ('c_now','c_after'):
    exprs[target.id]=node.value
assert set(exprs)=={'c_now','c_after'}
# Execute the actual source expression with zero variable coefficients.
# This isolates the functional's affine offset; it does not pretend zero data obey joins.
env={'np':np,'sum':sum,'range':range,'weights_m':np.array([.25,.125,-.125,-.125]),'kap':np.array([1.,2.]),'Z':np.eye(2),'y':np.zeros((2,4)),'cp0':np.zeros(2),'coef':np.zeros((2,4))}
actual={name:float(eval(compile(ast.Expression(value),str(source),'eval'),env)) for name,value in exprs.items()}
assert all(v==0 for v in actual.values())
# The actual Trial adds one in a_0 even with all variable coefficients zero.
d={'k':.2,'L':1.,'rmin':.5,'R0':2.,'knots':np.r_[np.full(8,np.log(.5)),np.full(8,np.log(2.))],'p':7,'D':np.zeros((4,7)),'Ei':np.zeros((4,7)),'S':np.zeros((4,8)),'Aout':np.zeros((4,10)),'Eo':np.zeros((4,7)),'bi':1.,'bo':1.}
t=Trial(d);inner=t.eval(np.array([np.log(.25)]))[0]
assert np.array_equal(inner,np.array([1.,0.,0.,0.]))
# Full-circle Fourier coefficient: (1/pi) integral = twice its constant Laurent coefficient.
z=sp.symbols('z');co=(z+1/z)/2;si=(z-1/z)/(2*sp.I);si3=(z**3-z**-3)/(2*sp.I)
weights=[]
for m in range(9):
 mode=(z**(2*m)+z**(-2*m))/2
 weights.append(sp.expand(2*co**2*si*si3*mode).coeff(z,0))
assert weights==[sp.Rational(1,4),sp.Rational(1,8),-sp.Rational(1,8),-sp.Rational(1,8),0,0,0,0,0]
trial=NUM/'data/trial_h0.008.npz'
with np.load(trial,allow_pickle=False) as a:rmin=F.from_float(float(a['rmin']))
missing=rmin*rmin/8
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'actual_source_expressions':{name:ast.get_source_segment(text,value) for name,value in exprs.items()},'source_expressions_at_zero_variable_coefficients':actual,'actual_Trial_inner_at_zero_variable_coefficients':inner.tolist(),'exact_angular_weights_m_0_through_8':list(map(str,weights)),'all_higher_weights_zero_reason':'The kernel factor is a trigonometric polynomial of maximal cosine mode 6, so orthogonality kills m>=4.','stored_binary64_rmin_exact':str(rmin),'missing_fixed_strain_exact':str(missing),'missing_fixed_strain_decimal':float(missing),'verdict':'REFUTED affine strain functional in the hashed source. Zero variable coefficients are used to isolate the offset, not as an admissible joined trial.'}
(BASE/'research/numerics_audit/evidence/affine_strain_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
