"""Exact polynomial/log integral and independent interval divergence bounds."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx,fmpq_poly
from mpmath import iv
BASE=Path(__file__).resolve().parents[3];ctx.prec=160;ctx.threads=1;iv.dps=60
p=256*fmpq_poly([-1,1])**4*fmpq_poly([2,-1])**4
rational=F(0);logco=F(0)
for j in range(p.degree()+1):
 c=F(int(p[j].numerator),int(p[j].denominator))
 if j==1:logco=c
 else:rational+=c*(F(2)**(j-1)-1)/(j-1)
def ar(f):return arb(f.numerator)/f.denominator
def vi(f):return iv.mpf(f.numerator)/f.denominator
constant=ar(rational)+ar(logco)*arb(2).log();independent=vi(rational)+vi(logco)*iv.ln(2)
assert constant>0 and independent>0
rows=[]
for n in (4,8,12,16,20):
 delta=F(1,2**(2*n));eps=F(1,2**n)
 lower=-constant*ar(eps/delta);upper=-constant*ar(eps/(delta*(1+eps)))
 rows.append({'n':n,'delta':str(delta),'factor_norm_epsilon':str(eps),'D_difference_lower_bound':lower.lower().str(30),'D_difference_upper_bound':upper.upper().str(30)})
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cutoff_coefficients_ascending':list(map(str,p.coeffs())),'constant_rational':str(rational),'constant_log2_coefficient':str(logco),'C_chi_Arb':constant.str(40),'C_chi_mpmath_iv':str(independent),'divergence_bounds':rows,'verdict':'CONFIRMED explicit illustration. General X3 asymptotic proved in PROOF.md.'}
(BASE/'research/axis_finite_part/evidence/cutoff_bounds.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
