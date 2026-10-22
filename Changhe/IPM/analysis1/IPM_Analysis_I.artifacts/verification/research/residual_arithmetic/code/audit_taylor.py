"""Exact counterexamples to arithmetic and modal identities in the residual source snapshot."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/residual_arithmetic/evidence'
sys.path.insert(0,str(E))
from cert_resid import TMArr,Certifier,MR
ctx.prec=256
Q=12;h=F.from_float(.01);hpow=np.array([1.]+[float(h**i) for i in range(1,2*Q+3)])
def aa(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def cell_interval(tm,j=0):
 p=sum((aa(F.from_float(float(tm.c.m[j,i])))*aa(h)**i for i in range(Q+1)),arb(0))
 r=sum((aa(F.from_float(float(tm.c.r[j,i])))*aa(h)**i for i in range(Q+1)),aa(F.from_float(float(tm.r[j]))))
 return p+arb(0,r.upper())
# (1) Product coefficient cancellation with exact input polynomials.
a=np.array([[1e16]+[1.]*6+[-1e16]+[0.]*5]);b=np.ones((1,8))
tm=TMArr(MR.exact(a),np.zeros(1));prod=tm.mul_poly(MR.exact(b),hpow)
m,r=(F.from_float(float(v)) for v in (prod.c.m[0,7],prod.c.r[0,7]))
exact=sum((F.from_float(float(a[0,i])) for i in range(8)),F(0))
assert exact==6 and m+r<exact
cancellation={'exact_degree_7_coefficient':str(exact),'returned_midpoint':str(m),'returned_radius':float(r),'coefficient_enclosed':False}
# (2) The frozen snapshot already has the repaired B sign. Check the actual signature and corrected call.
C=Certifier.__new__(Certifier);C.Q=Q
coef=np.zeros((1,Q+1));coef[0,0]=1
g=TMArr(MR.exact(coef),np.zeros(1));gd=np.zeros((1,Q+1));gd[0,0]=1
assert 'h_up, gsign=-1.0)' in (E/'cert_resid.py').read_text()
wrong=C.ode_tm(MR.exact(np.ones(1)),g,gd,np.array([2.]),float(h),gsign=-1.0)
true=(1+(2*aa(h)).exp())/2;enclosure=cell_interval(wrong)
assert enclosure.contains(true)
wrong_b={'true_B_equation':'Bprime=2B-1, B(0)=1','true_B_at_h':true.str(40),'returned_TM_at_h':enclosure.str(40),'h_exact':str(h),'contains_true':True,'status':'REPAIRED in this snapshot; original contrary finding withdrawn','true_linear_coefficient':'1','returned_linear_coefficient':float(wrong.c.m[0,1])}
# (3) Tangential product uses the opposite difference-frequency sign from radial product.
C.M=0;C.Nf=1;C.N1=np.array([[1]]);C.N2=np.array([[0]]);C.S2=np.array([[-1.]]);C.Nmax=2
p=TMArr(MR.exact(coef),np.zeros(1))
v=C.conv_scatter(p,p,hpow,float(h));m0=F.from_float(float(v.c.m[0,0]));r0=F.from_float(float(v.c.r[0,0]))
assert m0+r0<1
angular={'identity':'2 sin(2 theta) cos(theta)=sin(3 theta)+sin(theta)','expected_sin_theta_coefficient':1,'returned_constant_coefficient':float(m0),'returned_radius':float(r0),'coefficient_enclosed':False,'scope':'cell() uses the same scatter sign for radial and tangential products; the latter must reverse S2.'}
# (4) The Bernstein transform is not an exact dyadic matrix.
from cert_resid import bernstein_matrix
br=F.from_float(float(bernstein_matrix(Q)[4,1]));assert br!=F(1,3)
bern={'entry':[4,1],'exact':'1/3','stored_dyadic':str(br),'absolute_error':str(abs(br-F(1,3))),'exported_radius_in_constructor':'0'}
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256((E/'cert_resid.py').read_bytes()).hexdigest(),'midrad_sha256':hashlib.sha256((E/'midrad.py').read_bytes()).hexdigest(),'product_cancellation':cancellation,'corrected_B_forcing':wrong_b,'wrong_tangential_scatter':angular,'Bernstein_exactness':bern,'verdict':'REFUTED for product-coefficient invariants and tangential sign; B sign repaired. No claim about reachability or size on actual profile data'}
(E/'taylor_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
