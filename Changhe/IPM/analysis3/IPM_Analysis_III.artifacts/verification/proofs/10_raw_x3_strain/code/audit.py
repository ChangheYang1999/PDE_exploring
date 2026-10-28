"""Independent input/de Boor/rounding audit for the raw X3 certificate."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,lzma,sys
import numpy as np
from flint import arb,arb_mat,ctx
import certify as first
ctx.prec=384;ctx.threads=1
root=Path(__file__).resolve().parents[1];lane=root.parents[1]
original=lane.parent/'source/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz'
raw=dict(np.load(original,allow_pickle=False)); sha=hashlib.sha256(original.read_bytes()).hexdigest()
assert sha=='d58bb8834b0a5859ef8d8bfd61091fe4cf1852114378d33afbbc5b5662bb53a2'
export=lane/'research_copy/analysis1/IPM_Analysis_I.artifacts/verification/data_exact/x3.json.xz'
e=json.loads(lzma.decompress(export.read_bytes()))
for name in ('z','spline_knots'):
    assert [float(x).hex() for x in raw[name]]==e[name+'_hex']
for name,value in e['scalars_hex'].items():assert float(raw[name]).hex()==value
for name,value in e['integers'].items():assert int(raw[name])==value
knots=[F.from_float(float(x)) for x in raw['spline_knots']]
z=[F.from_float(float(x)) for x in raw['z']]
co=[[F(0)]+z[1+375*m:1+375*(m+1)] for m in range(201)]
def aa(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def deboor_weights(q,i):
    # de Boor affine interpolation of eight unit-vector controls.
    v=[[F(int(j==k)) for k in range(8)] for j in range(8)]
    for r in range(1,8):
        for j in range(7,r-1,-1):
            index=i-7+j; alpha=(q-knots[index])/(knots[index+8-r]-knots[index])
            v[j]=[(1-alpha)*left+alpha*right for left,right in zip(v[j-1],v[j])]
    assert sum(v[7])==1 and min(v[7])>=0
    return v[7]
t=first.Trial(); count=0;maxerr=arb(0)
for a,b,i in t.spans:
    controls=arb_mat([[aa(co[m][j]) for m in range(201)] for j in range(i-7,i+1)])
    mid,half,rows,_=t.polynomial(i)
    for frac in (F(1,9),F(2,9),F(3,9),F(4,9),F(5,9),F(6,9),F(7,9),F(8,9)):
        q=a+(b-a)*frac
        independent=arb_mat([[aa(x) for x in deboor_weights(q,i)]])*controls
        computed=first.horner(rows,(aa(q)-mid)/half)
        for left,right in zip(independent.tolist()[0],computed.tolist()[0]):
            assert left.overlaps(right),(i,frac,str(left),str(right))
            assert abs(left-right)<arb('1e-100')
        count+=201
    if count%(201*8*100)==0:print('checked',count,'mode evaluations',flush=True)
# Separately reconstruct the scalar interval from the unscaled saved sum.
outputs=[]
for resultpath in sorted((root/'evidence').glob('*_result.json')):
    r=json.loads(resultpath.read_text());assert r['input_sha256']==sha
    part=json.loads(resultpath.with_name(resultpath.name.replace('_result','_partition')).read_text())
    errors=part['errors'];err=sum((arb(errors[k]) for k in ('radial','angular','q_strips','theta_strip')),arb(0))
    assert err.overlaps(arb(r['unscaled_error']))
    k=aa(z[0]);L=aa(F.from_float(float(raw['L'])))
    pref=4*L*L/(arb.pi()*(1-k))
    rebuilt=pref*(arb(r['quadrature_sum'])+arb(0,err.upper()))
    defect=3/k-1-rebuilt
    assert rebuilt.overlaps(arb(r['strain'])) and defect.overlaps(arb(r['held_normalization_defect']))
    assert defect>0
    assert rebuilt>arb('15.72608782162349') and rebuilt<arb('15.72608782162351')
    assert defect>arb('1.03011e-8') and defect<arb('1.03012e-8')
    assert (1+rebuilt)/3>2
    outputs.append({'file':resultpath.name,'strain':rebuilt.str(60),'lower':rebuilt.lower().str(70),'upper':rebuilt.upper().str(70),'defect':defect.str(60),'defect_lower':defect.lower().str(70),'defect_upper':defect.upper().str(70)})
out={'date':datetime.now(timezone.utc).isoformat(),'input_sha256':sha,'export_sha256':hashlib.sha256(export.read_bytes()).hexdigest(),'all_input_doubles_match_export':True,'independent_method':'exact rational de Boor weights at eight distinct points on every span, all 201 mode controls','mode_evaluations':count,'precision_bits':ctx.prec,'outputs':outputs,'status':'PASS','scope':'independent reconstruction/output audit; Cauchy proof and Arb library remain explicit dependencies'}
(root/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
