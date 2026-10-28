"""Independent exact-rational output and de Boor audit of the modal source."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import hashlib,json
import numpy as np
import sympy as sy
from flint import arb,arb_mat,ctx
import certify as main
ctx.prec=640;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
raw=np.load(source,allow_pickle=False)
assert hashlib.sha256(source.read_bytes()).hexdigest()=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
rat=lambda x:F.from_float(float(x))
aa=main.aa
knots=[rat(x) for x in raw['knots']]
def interval(rec):
    a,b=F(rec['lower_exact']),F(rec['upper_exact']);assert a<=b
    return a,b
outputs=[]
for path in sorted((TOP/'evidence').glob('source_*_result.json')):
    r=json.loads(path.read_text());assert r['input_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
    assert r['script_sha256']==hashlib.sha256((TOP/'code/certify.py').read_bytes()).hexdigest()
    assert r['scalar_input_sha256']==hashlib.sha256(main.SCALAR.read_bytes()).hexdigest()
    assert r['all_radial_spans']==1558 and r['stream_modes']==261
    a,b=map(F,r['source_bracket']);assert a<b and a>4
    assert [a,b]==[F(4841405518533377,562949953421312),F(4841405518533711,562949953421312)]
    tl,tr=map(F,r['source_span']);assert aa(tl)<aa(a).log()<aa(b).log()<aa(tr)
    assert interval(r['results']['a']['w'])[1]<0<interval(r['results']['b']['w'])[0]
    for name,low,high in [('wprime',F(10),F(51,5)),('mu',F(99999997745,10**11),F(99999997750,10**11)),('g',F(29749,1000),F(119,4))]:
        lo,hi=interval(r['results']['whole'][name]);assert low<lo<=hi<high,(name,lo,hi)
    lo,hi=interval(r['results']['whole']['mu']);gl,gu=interval(r['results']['whole']['g'])
    residual_bounds=[(lo-1)*gu,(hi-1)*gl]
    assert F(-68,10**8)<residual_bounds[0]<residual_bounds[1]<F(-66,10**8)
    outputs.append({'file':path.name,'source_bracket':[str(a),str(b)],'mu_strictly_below_one':True,'epsilon_y_at_exact_source_enclosure':[str(F(-68,10**8)),str(F(-66,10**8))]})
assert outputs
# Differential identity checked without any radial integrator.
t=sy.symbols('t',real=True);m=sy.symbols('m',integer=True,positive=True)
I,J,H,K=[sy.Function(x)(t) for x in ['I','J','H','K']]
expr=-sy.diff(J-I,t,2)-8*sy.diff(J-I,t)+(m*m-16)*(J-I)
subs={sy.diff(I,t,2):-(m+4)*(-(m+4)*I+H)+sy.diff(H,t),sy.diff(J,t,2):(m-4)*((m-4)*J-K)-sy.diff(K,t),sy.diff(I,t):-(m+4)*I+H,sy.diff(J,t):(m-4)*J-K}
assert sy.simplify(expr.xreplace(subs)-(sy.diff(H,t)+(4-m)*H+sy.diff(K,t)+(m+4)*K))==0
# Exact de Boor recurrence is independent of the Cox polynomial reconstruction.
def weights(x,i):
    values=[[F(int(j==k)) for k in range(8)] for j in range(8)]
    for r in range(1,8):
        for j in range(7,r-1,-1):
            index=i-7+j;alpha=(x-knots[index])/(knots[index+8-r]-knots[index])
            values[j]=[(1-alpha)*a+alpha*b for a,b in zip(values[j-1],values[j])]
    assert sum(values[7])==1 and min(values[7])>=0
    return values[7]
d=main.Data();count=0;moment_count=0
for ordinal,span in enumerate(d.spans):
    left,right=knots[span:span+2];rows=d.poly(span).tolist()
    controls=arb_mat(d.control[span-7:span+1])
    for u in [F(2,7),F(5,7)]:
        independent=(arb_mat([[aa(v) for v in weights(left+(right-left)*u,span)]])*controls).tolist()[0]
        polynomial=[sum((rows[j][n]*aa(u)**j for j in range(8)),arb(0)) for n in range(262)]
        for a,b in zip(independent,polynomial):assert a.overlaps(b) and abs(a-b)<arb('1e-150')
        count+=262
    if ordinal%250==0:print('de Boor spans',ordinal+1,flush=True)
# Distinct widths, extremal frequencies, zero and positive exponent.
for width in sorted(set(knots[i+1]-knots[i] for i in d.spans)):
    for lam in [-526,-6,-2,0,2]:
        z=aa(width*lam);a=main.phi_direct(z);b=main.phi_series(z,N=192)
        for x,y in zip(a,b):assert x.overlaps(y)
        moment_count+=8
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'outputs':outputs,'mode_evaluations':count,'primitive_series_comparisons':moment_count,'precision_bits':ctx.prec,'symbolic_stream_identity':True,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'exact modal source and coefficient box; no raw X3 source or stationarity'}
(TOP/'evidence/audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
