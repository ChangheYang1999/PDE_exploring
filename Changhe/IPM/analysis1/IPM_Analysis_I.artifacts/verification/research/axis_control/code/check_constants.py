"""Independent Arb and mpmath.iv bounds, plus symbolic axis-kernel algebra."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
import sympy as sp
BASE=Path(__file__).resolve().parents[3];sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from strain_arb import Data,jsball
ctx.prec=160;ctx.threads=1;d=Data();iv.dps=60
B=3*d.L*d.L/(4*(1-d.k));K=d.L*d.L/(1-d.k)*(arb(1)/36+arb(3).sqrt()/(8*arb.pi()));positive=(-d.csum).exp()
assert positive>arb(135)/10000 and K<7
raw=d.raw;zz=[F.from_float(float.fromhex(v)) for v in raw['z_hex']];nr=raw['integers']['degree'];nm=raw['integers']['angular']+1
cs=sum((max(abs(v) for v in zz[1+m*nr:1+(m+1)*nr]) for m in range(nm)),F(0))
def vv(q):return iv.mpf(q.numerator)/q.denominator
kk=F.from_float(float.fromhex(raw['scalars_hex']['k']));ll=F.from_float(float.fromhex(raw['scalars_hex']['L']));ki=vv(ll)**2/(1-vv(kk))*(iv.mpf(1)/36+iv.sqrt(3)/(8*iv.pi));bi=3*vv(ll)**2/(4*(1-vv(kk)));pi=iv.exp(-vv(cs))
assert pi>iv.mpf(135)/10000 and ki<7
x,r,c=sp.symbols('x r c',positive=True);beta=r*r/(r*r+x*x)
pair=(x-r*c)/(x*x+r*r-2*x*r*c)**2+(x+r*c)/(x*x+r*r+2*x*r*c)**2
closed=2*x*beta**2*(1-4*beta**2*c*c)/(1-4*beta*(1-beta)*c*c)**2
assert sp.factor(r**4*pair-closed)==0
# Differentiating the elementary rational integral gives both claimed J formulas.
a,b=sp.symbols('a b',positive=True);basic=sp.pi/(2*(a+b))
j0=-sp.diff(basic,a)/(2*a);j1=-sp.diff(j0,b)/(2*b)
assert sp.simplify(j0.subs(a,1)-sp.pi/(4*(1+b)**2))==0
assert sp.simplify(j1.subs(a,1)-sp.pi/(4*b*(1+b)**3))==0
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':d.sha,'Csum':jsball(d.csum),'exp_minus_Csum':jsball(positive),'axis_velocity_constant_B':jsball(B),'scaling_constant_K':jsball(K),'axis_drift_constant_B_plus_K':jsball(B+K),'independent_iv':{'exp_minus_Csum':str(pi),'B':str(bi),'K':str(ki)},'symbolic_axis_kernel_identity':True,'rational_integral_derivative_identities':True,'verdict':'CONFIRMED constants and symbolic identities; full analytic argument in PROOF.md.'}
(BASE/'research/axis_control/evidence/constants.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
