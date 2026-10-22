"""Independent exact-Cox and interval-series checks of actual trial spline moments."""
import os,sys
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
sys.dont_write_bytecode=True
import io,json,hashlib,math
from types import SimpleNamespace
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.interpolate import PPoly
from flint import arb,ctx
from moments import integral,aa
BASE=Path(__file__).resolve().parents[3];NUM=Path('numerics');sys.path.insert(0,str(NUM/'src'))
from expoly import integral_exp_poly
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import exact_poly
ctx.prec=200;ctx.cap=8;ctx.threads=1
path=NUM/'data/trial_h0.008.npz';raw=path.read_bytes()
with np.load(io.BytesIO(raw),allow_pickle=False) as data:knots=np.array(data['knots'])
tt=[F.from_float(float(v)) for v in knots];n=len(tt)-8;dummy=SimpleNamespace(t=tt,deg=7);rows=[]
for bi in [0,1,7,50,500,1000,n-8,n-1]:
 co=np.zeros(n);co[bi]=1;pp=PPoly.from_spline((knots,co,7));exacttotal=arb(0);pptotal=arb(0);numtotal=0.0
 for span in range(max(7,bi),min(bi+7,n-1)+1):
  a,b=tt[span],tt[span+1]
  if a==b:continue
  sp,basis=exact_poly(dummy,a,b);assert sp==span;col=bi-(span-7)
  midco=[F(str(basis[j,col])) for j in range(8)];h=b-a
  local=[sum((math.comb(l,j)*midco[l]*(-h/2)**(l-j) for l in range(j,8)),F(0)) for j in range(8)]
  exacttotal+=(2*aa(a)).exp()*integral(2,local,F(0),h)
  pc=pp.c[::-1,span]
  pptotal+=(2*aa(a)).exp()*integral(2,[F.from_float(float(v)) for v in pc],F(0),h)
  numtotal+=np.exp(2*float(a))*float(integral_exp_poly(2,pc,0,float(h)))
 assert exacttotal>0
 rows.append({'basis':bi,'exact_Cox_interval_integral':exacttotal.str(40),'same_float_PPoly_coefficients_interval_integral':pptotal.str(40),'num_primitive_result':numtotal,'num_minus_true':(aa(F.from_float(numtotal))-exacttotal).str(35),'PPoly_rounding_minus_true':(pptotal-exacttotal).str(35)})
# Formula check at lambda=0, including interval partition and signed coefficients.
cs=[F(2,3),F(-5,7),F(11,13)];a=F(-3,2);b=F(7,4)
zero=integral(0,cs,a,b);truth=sum((c*(b**(j+1)-a**(j+1))/(j+1) for j,c in enumerate(cs)),F(0));assert zero.contains(aa(truth))
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'moment_library_sha256':hashlib.sha256((Path(__file__).parent/'moments.py').read_bytes()).hexdigest(),'trial_source_sha256':hashlib.sha256(raw).hexdigest(),'num_expoly_sha256':hashlib.sha256((NUM/'src/expoly.py').read_bytes()).hexdigest(),'bits':200,'lambda_zero_exact_polynomial_check':True,'basis_moments':rows,'verdict':'Actual positive spline moments independently enclosed; compare primitive subtraction failures in rows.'}
(BASE/'research/exponential_moments/evidence/actual_spline_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
