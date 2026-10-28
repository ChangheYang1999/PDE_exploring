"""Exact original-data seventh derivative jumps of two spline modes."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
import numpy as np
TOP=Path(__file__).resolve().parents[1]; LANE=TOP.parents[1]
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
r=np.load(source,allow_pickle=False)
assert int(r['p'])==7 and int(r['M'])==260
knots=[Q(float(x)) for x in r['knots']]
# Select an ordinary interior knot; the proof is local at this exact circle.
i=700
assert knots[i-1]<knots[i]<knots[i+1]
results={}
for mode in (0,1):
    T=knots[:];c=[Q(float(x)) for x in r['S'][mode]]
    for p in range(7,0,-1):
        den=[T[j+p+1]-T[j+1] for j in range(len(c)-1)]
        assert min(den)>0
        c=[p*(c[j+1]-c[j])/den[j] for j in range(len(c)-1)]
        T=T[1:-1]
    assert len(c)==len(T)-1 and T==knots[7:-7]
    # Degree zero coefficient k is on [T[k],T[k+1]).
    left=c[i-8]; right=c[i-7];jump=right-left
    assert jump!=0
    results[str(mode)]={'left_exact':str(left),'right_exact':str(right),'jump_exact':str(jump),'jump_decimal_diagnostic':float(jump)}
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','input':str(source),'input_sha256':sha,
     'method':'Seven exact derivative-coefficient recurrences; subtract adjacent degree-zero coefficients',
     'original_knot_index':i,'knot_exact':str(knots[i]),'knot_decimal_diagnostic':float(knots[i]),
     'modes_checked':results,'nonconstant_angular_jump':True,
     'residual_local_sobolev_threshold':'13/2 (membership fails at the endpoint)',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest()}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
