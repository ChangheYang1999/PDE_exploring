"""Exact all-mode endpoint checks from the read-only original NPZ."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import factorial,comb
import hashlib,json,time
import numpy as np
P=Path(__file__).resolve().parents[1]
LANE=P.parents[1]
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
started=time.monotonic()
f=np.load(source,allow_pickle=False)
for name in f.files:
    assert np.issubdtype(f[name].dtype,np.number) and np.all(np.isfinite(f[name])),name
assert int(f['p'])==7 and int(f['M'])==260
knots=[Q(float(v)) for v in f['knots']]
nb=len(knots)-8
assert nb==1565 and f['S'].shape==(260,nb) and f['D'].shape==(260,7)
assert f['Aout'].shape==(260,10)
assert knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8
assert all(knots[j]<knots[j+1] for j in range(7,len(knots)-8))
k,bi,bo=(Q(float(f[name])) for name in ('k','bi','bo'))
assert 0<k<1 and bi>50 and bo>125 and 3-bo<k
pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
alpha=[k-3-j*(1-k)-2*l for j,l in pairs]
assert all(a<=k-3 for a in alpha)

def endpoint(row,side):
    offset=0 if side=='left' else nb-7
    co=[Q(float(v)) for v in row[offset:offset+7]]
    jet=[]
    for n in range(7):
        jet.append(co[0] if side=='left' else co[-1])
        if n<6:
            den=[knots[offset+i+8]-knots[offset+i+n+1] for i in range(len(co)-1)]
            assert all(d>0 for d in den)
            co=[(7-n)*(co[i+1]-co[i])/den[i] for i in range(len(co)-1)]
    return jet

def matched(jet,base,b):
    diff=[x-y for x,y in zip(jet,base)]
    out=[sum(((-b)**(i-j)*diff[j]/(factorial(i-j)*factorial(j)) for j in range(i+1)),Q(0)) for i in range(7)]
    for n in range(7):
        recovered=sum((Q(comb(n,i))*b**(n-i)*factorial(i)*out[i] for i in range(n+1)),Q(0))
        assert recovered==diff[n]
    return out

h=hashlib.sha256()
max_bits=0
for mode in range(260):
    di=[Q(float(v)) for v in f['D'][mode]]
    ao=[Q(float(v)) for v in f['Aout'][mode]]
    im=[Q(mode==0 and n==0)+sum((di[j]*(2*j+2)**n for j in range(7)),Q(0)) for n in range(7)]
    om=[sum((ao[j]*alpha[j]**n for j in range(10)),Q(0)) for n in range(7)]
    ei=matched(endpoint(f['S'][mode],'left'),im,bi)
    eo=matched(endpoint(f['S'][mode],'right'),om,-bo)
    for x in ei+eo:
        h.update((str(x)+'\n').encode())
        max_bits=max(max_bits,x.numerator.bit_length(),x.denominator.bit_length())
# A unit change of A_00 gives this linear correction to the matching polynomial.
repair=matched([Q(0)]*7,[alpha[0]**n for n in range(7)],-bo)
assert any(repair)
out={
 'date_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'input':str(source),'input_sha256':sha,'method':'Exact rational local derivative-coefficient recurrence and exponential-polynomial matching, every mode and both endpoints',
 'modes':260,'spline_degree':7,'spline_functions':nb,'simple_interior_knots':len(knots)-16,
 'all_mode_endpoint_equalities':260*2*7,'repair_parameter_equalities':7,
 'stored_matching_arrays_used_as_defining_coefficients':False,
 'matching_coefficient_serialization_sha256':h.hexdigest(),'largest_rational_bits':max_bits,
 'k_exact':str(k),'bi_exact':str(bi),'bo_exact':str(bo),'outer_exponents_exact':[str(a) for a in alpha],
 'strict_exponent_checks':{'0<k<1':True,'bi>50':True,'bo>125':True,'3-bo<k':True,'all_alpha<=k-3':True},
 'elapsed_seconds':time.monotonic()-started,
 'scope':'Qualitative finiteness of the density coefficient bounds in B1/B2. No transport margin, norm bound or inverse.',
 'proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
