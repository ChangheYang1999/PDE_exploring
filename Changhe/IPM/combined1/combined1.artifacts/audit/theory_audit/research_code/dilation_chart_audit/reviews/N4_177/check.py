"""Independent all-branch raw endpoints and full Fourier density derivatives."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from itertools import permutations
import json, sys, time
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]; BASE=ROOT/'research/branch_tail_audit'
def H(p):return sha256(Path(p).read_bytes()).hexdigest()
def density(amplitudes,d):
    f={}
    for m,v in amplitudes.items():
        if m==0:f[0]=v
        else:f[2*m]=f[-2*m]=v/2
    imag=defaultdict(Q)
    for n,v in f.items():
        lap=(d*d-n*n)*v
        imag[n+1]+=lap*(d-2-n)/2
        imag[n-1]-=lap*(d-2+n)/2
    assert all(v==-imag[-n] for n,v in list(imag.items()))
    return {n:-2*v for n,v in sorted(imag.items()) if n>0 and v}
def main():
    start=time.monotonic(); src=BASE/'source'
    manifest=json.loads((src/'MANIFEST.json').read_text())
    for name,row in manifest['files'].items():assert H(src/name)==row['sha256']
    peer=json.loads((src/'T4_result.json').read_text())
    assert peer['proof_sha256']==H(src/'T4_PROOF.md') and peer['code_sha256']==H(src/'T4_check.py')
    rawpath=ROOT/'research/basis_redundancy/source/candidate007.json'
    canpath=ROOT/'research/basis_redundancy/source/canonical007.json'
    assert H(rawpath)=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
    assert H(canpath)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
    raw=json.loads(rawpath.read_text());can=json.loads(canpath.read_text())
    c=Q(raw['cl_exact']);assert c==Q(can['cl'])==Q(4076476460239181,2251799813685248)
    gamma=1/c;delta=1-gamma;amps=defaultdict(Q);count=0
    for g in raw['generators']:
        spec=g['spec'];assert spec[0] in ('mono','leg')
        n=0 if spec[0]=='mono' else int(spec[2]);a=b=Q(1)
        for k in range(1,n):a,b=b,((2*k+1)*b-k*a)/(k+1)
        assert b==1;count+=1;amps[g['j'],g['m']]+=Q(g['coef'])*b
    amps2=defaultdict(Q)
    for (j,m,k),v in zip(can['order'],can['coefficients'],strict=True):amps2[j,m]+=Q(v)
    assert dict(amps)==dict(amps2) and count==2982 and len(amps)==360
    rows=[]
    for j in range(8):
        e=1-(j+1)*delta;d=3+e
        A={m:v for (jj,m),v in amps.items() if jj==j}
        sine=density(A,d);v=sine[1]
        formula=-A[0]*d*d*(d-2)+A[1]*(d*d-4)*d/2
        assert v==formula==Q(peer['branches'][j]['first_sine_exact']) and v
        assert e==Q(peer['branches'][j]['exponent'])
        floor=(v.numerator*10**12)//v.denominator
        lo=Q(floor-1,10**12);hi=Q(floor+2,10**12)
        assert lo<v<hi and lo*hi>0
        rows.append({'j':j,'exponent':str(e),'first_sine_exact':str(v),
                     'first_sine_lower':str(lo),'first_sine_upper':str(hi),
                     'first_sine_float_diagnostic':float(v),'nonzero':True,
                     'full_leading_sine_map':{str(n):str(z) for n,z in sine.items()}})
    cuts=[4*gamma-2,3*gamma-1,2*gamma,1+gamma]
    assert 0<cuts[0]<cuts[1]<cuts[2]<cuts[3]
    assert all(v==Q(w) for v,w in zip(cuts,peer['dimension_thresholds']))
    assert Q(rows[3]['exponent'])>-1>Q(rows[4]['exponent'])
    matrix=[[z**k-1 for k in range(1,5)] for z in (2,3,4,5)]
    det=0
    for perm in permutations(range(4)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term=sign
        for i in range(4):term*=matrix[i][perm[i]]
        det+=term
    assert det==Q(peer['vandermonde_determinant'])!=0
    paths=[rawpath,canpath,src/'MANIFEST.json',src/'T4_result.json',src/'T4_PROOF.md',src/'T4_check.py',BASE/'PROOF.md',Path(__file__)]
    out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):H(p) for p in paths},
         'raw_endpoint_count':count,'matching_amplitude_blocks':len(amps),'c_exact':str(c),
         'branches':rows,'weighted_dimension_thresholds':list(map(str,cuts)),
         'determinant':str(det),'all_eight_peer_first_harmonics_equal':True,
         'elapsed_seconds':time.monotonic()-start,
         'verdict':'CONFIRMED all eight nonzero branch coefficients and exact chart arithmetic; Opus theorem review separate'}
    with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(out['utc'],out['verdict'],out['elapsed_seconds'],flush=True)
    print([(z['j'],z['first_sine_float_diagnostic']) for z in rows],flush=True)
if __name__=='__main__':main()
