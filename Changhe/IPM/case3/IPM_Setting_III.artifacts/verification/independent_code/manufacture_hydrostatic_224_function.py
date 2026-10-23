"""Hand-computable comparison tests; no candidate and no inverse."""
from audit_hydrostatic_224_function import compare,sha,token_interval,token_agrees,CartesianQJet,ScalarMPDensity
from fractions import Fraction as F
import mpmath as mp
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json
R=Path('research/hydrostatic_224_function_difference');checks=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
a=np.array([[4.,3.,4.,0.]]);b=np.array([[2.,0.,0.,0.]]);zero=np.array([0.]);three=np.array([3.])
z=compare(a,b,(zero,zero),zero)['inner']
for key,expected in [('field',2.),('gradient',5.),('pointwise_relative',1.)]:ck('origin '+key,z[key]['value']==expected)
z=compare(a,b,(three,zero),three)['annulus'];ck('physical radius field',z['field']['value']==1.);ck('physical radius Euclidean gradient',z['gradient']['value']==10.)
z=compare(a,b,(three,zero),zero,zero)['inner'];ck('nominal weight distinction',z['field']['value']==2. and z['gradient']['value']==5.)
b[:,0]=0;z=compare(a,b,(zero,zero),zero)['inner'];ck('nonzero over zero flag',z['nonzero_over_zero']==1 and z['zero_over_zero']==0 and z['pointwise_relative']is None)
a[:,0]=0;z=compare(a,b,(zero,zero),zero)['inner'];ck('zero over zero excluded',z['nonzero_over_zero']==0 and z['zero_over_zero']==1 and z['pointwise_relative']is None)
b[:,0]=2**-44;a[:,0]=2**-43;z=compare(a,b,(zero,zero),zero)['inner'];ck('small positive retained',z['near_zero_positive_count']==1 and z['least_positive_weighted_density']==2**-44 and z['pointwise_relative']['value']==1.)
bound=np.array([1e7]);z=compare(a,b,(bound,zero),bound);ck('boundary separately counted',z['outer']['count']==0 and z['outer_boundary']['count']==1);ck('empty region has no max',z['inner']['count']==0 and z['inner']['field']is None);ck('full sample included',z['full_sample']['count']==1)
lo,hi,half=token_interval('3.12e-02');ck('exact half unit',half==F(1,20000));ck('exact token endpoints',(lo,hi)==(F(623,20000),F(625,20000)));ck('closed token endpoints',token_agrees(lo,'3.12e-02')and token_agrees(hi,'3.12e-02'));ck('outside token rejected',not token_agrees(lo-F(1,10**9),'3.12e-02')and not token_agrees(hi+F(1,10**9),'3.12e-02'))
aa=np.array([[4.,0.,0.,0.],[10.,0.,0.,0.]]);bb=np.array([[2.,0.,0.,0.],[2.,0.,0.,0.]]);x=np.array([0.,3.]);y=np.zeros(2);z=compare(aa,bb,(x,y),x)['full_sample']['field'];ck('argmax index and value',z['index']==1 and z['value']==4.);ck('argmax location and operands',(z['x'],z['y'],z['numerator'],z['denominator'])==(3.,0.,8.,2.))
class OriginOnlyQ:
 p=.5;M=0;kappa=2.;coeff=np.array([[2.]]);basis='cheb';tk=None
 def polynomial(self,k,t):return np.full_like(t,2.,dtype=float)
 def coordinates(self,r):return -np.ones_like(r),np.zeros_like(r),np.ones_like(r)
j=CartesianQJet(OriginOnlyQ());zz=j.jet(0.,0.);za=j.jet(np.array([0.]),np.array([0.]));ck('Cartesian scalar shape',zz.shape==(4,));ck('Cartesian array shape',za.shape==(1,4));ck('Cartesian ordering and scalar array equality',np.array_equal(zz,[0.,0.,2.,0.])and np.array_equal(zz,za[0]))
with mp.workdps(48):
 m=ScalarMPDensity([[2.]],1.,2.);mj=m.jet(0.,0.);ck('MP scalar flat interface',len(mj)==4 and all(isinstance(a,mp.mpf)for a in mj));ck('MP ordered origin jet',max(abs(a-b)for a,b in zip(mj,[0,0,2,0]))<mp.mpf('1e-40'))
files=[Path(__file__),Path('independent_code/audit_hydrostatic_224_function.py'),R/'MANUFACTURE_PROOF.md',R/'REVIEW_RESOLUTION_PROOF.md',R/'SECOND_REVIEW_RESOLUTION_PROOF.md',Path('independent_code/independent_hydrostatic.py'),Path('independent_code/scalar_mp_hydrostatic_density.py')]
out=dict(status='PASS',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings={str(p):sha(p)for p in files})
(R/'verification/MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks))
