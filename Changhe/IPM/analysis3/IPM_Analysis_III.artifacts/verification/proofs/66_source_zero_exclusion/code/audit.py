"""Original-input and independent derivative/output audit at 640 bits."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import json,hashlib
import numpy as np
from flint import arb,arb_mat,ctx
import certify as C
ctx.prec=640;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
raw=np.load(source,allow_pickle=False);sha=hashlib.sha256(source.read_bytes()).hexdigest()
cachefile=TOP/'evidence/boundary_cache.json';cache=json.loads(cachefile.read_text());out=json.loads((TOP/'evidence/wide_result.json').read_text())
assert sha==cache['original_sha256']=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
assert out['cache_sha256']==hashlib.sha256(cachefile.read_bytes()).hexdigest()
assert out['script_sha256']==hashlib.sha256((TOP/'code/certify.py').read_bytes()).hexdigest()
assert out['proof_sha256'] in [hashlib.sha256(q.read_bytes()).hexdigest() for q in [TOP/'PROOF.md',TOP/'evidence/PROOF_during_computation.md'] if q.exists()]
knots=[F.from_float(float(x)) for x in raw['knots']]
def weights(x,i):
    values=[[F(int(j==k)) for k in range(8)] for j in range(8)]
    for rr in range(1,8):
        for j in range(7,rr-1,-1):
            index=i-7+j;alpha=(x-knots[index])/(knots[index+8-rr]-knots[index])
            values[j]=[(1-alpha)*a+alpha*b for a,b in zip(values[j-1],values[j])]
    assert sum(values[7])==1 and min(values[7])>=0
    return values[7]
# Reconstruct projected controls directly from the read-only original, not cache rows.
controls=[]
Sraw=raw['S']
for j in range(Sraw.shape[1]):
    vec=[arb(0) for n in range(262)]
    for m in range(260):
        value=C.aa(F.from_float(float(Sraw[m,j])))
        for freq in [1+2*m,1-2*m,3+2*m,3-2*m]:
            vec[(abs(freq)-1)//2]+=value*(1 if freq>0 else -1)/8
    controls.append(vec)
polynomial_checks=0;derivative_checks=0;boundary_checks=0
for key,cached in cache['spans'].items():
    i=int(key);t0,t1=map(F,cache['knots'][key]);assert [t0,t1]==knots[i:i+2]
    rows=[[arb(v) for v in row] for row in cached['rows']];IL=list(map(arb,cached['IL']));JR=list(map(arb,cached['JR']))
    for u in [F(j,7) for j in range(8)]:
        independent=(arb_mat([[C.aa(v) for v in weights(t0+(t1-t0)*u,i)]])*arb_mat(controls[i-7:i+1])).tolist()[0]
        for n in range(262):
            val=C.horner([rows[j][n] for j in range(8)],C.aa(u))
            assert val.overlaps(independent[n]) and abs(val-independent[n])<arb('1e-140')
            polynomial_checks+=1
    # Check Taylor derivatives against a fresh Green integral and differentiated ODE.
    mid=C.aa((t0+t1)/2);rad=C.aa((t1-t0)/16)
    H,Sf,rems=C.local_series(rows,IL,JR,t0,t1,mid,rad)
    for sign in [-1,1]:
        v=sign*rad;t=mid+v;ell=t-C.aa(t0);rr=C.aa(t1)-t;HH=C.M.shift_rows(rows,ell/C.aa(t1-t0),C.aa(t1-t0))
        for n in range(1,262):
            aa=2*n+4;bb=2*n-4
            pi=C.M.phi_series(-aa*ell,N=192);pj=C.M.phi_series(-bb*rr,N=192)
            iv=(-aa*ell).exp()*IL[n-1]+sum(((-1)**j*HH[j][n-1]*ell**(j+1)*pi[j] for j in range(8)),arb(0))
            jv=(-bb*rr).exp()*JR[n-1]+sum((HH[j][n]*rr**(j+1)*pj[j] for j in range(8)),arb(0))
            for j in range(4):
                di=(-aa)**j*iv+sum(((-aa)**(j-1-l)*factorial(l)*HH[l][n-1] for l in range(j)),arb(0))
                dj=bb**j*jv-sum((bb**(j-1-l)*factorial(l)*HH[l][n] for l in range(j)),arb(0))
                direct=(dj-di)/2
                pc=[Sf[n-1][l]*F(factorial(l),factorial(l-j)).numerator/F(factorial(l),factorial(l-j)).denominator for l in range(j,C.N+1)]
                tay=C.horner(pc,v)+arb(0,rems[n-1][j])
                assert tay.overlaps(direct),(i,n,j,sign,tay,direct)
                derivative_checks+=1
    # Adjacent endpoint Green values checked with independent series moments.
    nxt=cache['spans'].get(str(i+1))
    if nxt:
        h=C.aa(t1-t0);rev=(arb_mat([[(-1)**j*__import__('math').comb(l,j) if l>=j else 0 for l in range(8)] for j in range(8)])*arb_mat(rows)).tolist()
        for n in range(1,262):
            a=2*n+4;ph=C.M.phi_series(-a*h,N=192)
            value=(-a*h).exp()*IL[n-1]+h*sum((rev[j][n-1]*ph[j] for j in range(8)),arb(0))
            assert value.overlaps(arb(nxt['IL'][n-1]));boundary_checks+=1
    print(json.dumps({'span':i,'polynomial_checks':polynomial_checks,'derivative_checks':derivative_checks}),flush=True)

def pair(rec):return F(rec['lower_exact']),F(rec['upper_exact'])
def lower(rec):return pair(rec)[0]
def upper(rec):return pair(rec)[1]
lo,hi,theta=C.bounds();seen=set();maxv=F(0);maxr=F(0)
for c in out['cells']:
    i=c['span'];j=c['radial_cell'];k=c['angular_cell'];seen.add((i,j,k))
    t0,t1=map(F,cache['knots'][str(i)]);left=max(lo,C.aa(t0));right=min(hi,C.aa(t1))
    l=left+(right-left)*j/out['radial_subdivisions_per_span'];r=left+(right-left)*(j+1)/out['radial_subdivisions_per_span']
    cl,cu=pair(c['t_interval']);al,au=pair(c['theta_interval'])
    assert C.aa(cl)<=l and C.aa(cu)>=r
    assert C.aa(al)<=theta*k/out['angular_subdivisions'] and C.aa(au)>=theta*(k+1)/out['angular_subdivisions']
    sq={name:max(abs(lower(rec)),abs(upper(rec)))**2 for name,rec in c['derivatives'].items()}
    mv=upper(c['MV_upper']);mr=upper(c['Mrho_upper'])
    assert mv**2>=sq['pxxx']+3*sq['pxxy']+3*sq['pxyy']+sq['pyyy']
    assert mr**2>=sq['rxx']+2*sq['rxy']+sq['ryy']
    maxv=max(maxv,mv);maxr=max(maxr,mr)
assert seen=={(int(i),j,k) for i in cache['spans'] for j in range(out['radial_subdivisions_per_span']) for k in range(out['angular_subdivisions'])}
assert upper(out['MV_upper'])==maxv and upper(out['Mrho_upper'])==maxr
assert maxv<F(13,10)
h=F(1,2);radius=(C.aa(h+C.B-C.A)**2+C.aa(h)**2).sqrt()
mu=F(99999997745,100000000000)
loss=C.aa(maxv)*radius
assert loss<C.aa(mu)
margin=C.aa(mu)-loss
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','original_sha256':sha,
 'precision_bits':640,'polynomial_values':polynomial_checks,
 'independent_Green_derivatives':derivative_checks,'adjacent_boundary_checks':boundary_checks,
 'covered_cells':len(seen),'MV_bound_exact':str(maxv),'MV_simple_bound':'1.3',
 'box_half_width':'1/2','box_x_lower_exact':str(C.A-h),'box_x_upper_exact':str(C.B+h),
 'distance_bound':C.record(radius),'source_min_rate_lower_exact':str(mu),
 'symmetric_DV_margin':C.record(margin),
 'scope':'Unique zero in the stated source rectangle; no global zero count',
 'result_sha256':hashlib.sha256((TOP/'evidence/wide_result.json').read_bytes()).hexdigest(),
 'proof_sha256':out['proof_sha256']}
(TOP/'evidence/audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
