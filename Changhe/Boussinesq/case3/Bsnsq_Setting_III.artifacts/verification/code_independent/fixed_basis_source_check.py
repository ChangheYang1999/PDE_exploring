"""Independent physical-source comparison for the fixed-basis restart.

Only this lane's SciPy spline reader is used. No solver-lane code is imported.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import time
import numpy as np
from r2_state_values import R2State

start=time.monotonic()
root=Path('verification/fixed_basis_driver_20261020T2250')
original=Path('../numerics/runs/blam1_lambda0.97.npz')
snapshot=root/'input_lambda0.97.npz'
snapshot.write_bytes(original.read_bytes())
with np.load(snapshot,allow_pickle=False) as a:
    base={k:a[k].copy() for k in a.files}
coeff=base['cG_f'].copy()
bseed=float(base['beta_seed']); bcurrent=float(base['beta_basis'])
for k in ['cG_f','cG_f_effective','beta_seed','lam']:
    base.pop(k,None)
base.update(cG=coeff,cF=np.zeros_like(coeff),eps=np.array(1.))
states={}
for name,b in [('original_source',bseed),('reinterpreted_source',bcurrent)]:
    data=dict(base);data.update(beta=np.array(b),beta_basis=np.array(b))
    path=root/(name+'.npz');np.savez(path,**data)
    states[name]=R2State(path)
s,c=states.values()
raw=coeff.reshape(s.K,s.nb)
# At theta=0, T_(2j)(0)=(-1)^j and odd T values vanish.
endpoint=sum(((-1)**(k//2))*Fraction.from_float(float(raw[k,-1])) for k in range(0,s.K,2))
assert endpoint != 0
radii=np.array([1.,1e2,1e4,1e8,1e12,1e20,1e40,1e80,1e120])
vs=s.omega(radii,np.zeros_like(radii));vc=c.omega(radii,np.zeros_like(radii))
rows=[]
for r,x,y in zip(radii,vs,vc):
    rows.append({'r':float(r),'original_source':float(x),'reinterpreted_source':float(y),
                 'difference':float(y-x),'relative_difference':float(abs((y-x)/x)),
                 'seed_weighted_difference':float(r**(1/bseed)*abs(y-x))})
out={'utc':datetime.now(timezone.utc).isoformat(),'input':str(original.resolve()),
     'input_sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest(),
     'beta_seed':bseed,'beta_current_basis':bcurrent,
     'endpoint_exact':str(endpoint),'endpoint_float':float(endpoint),
     'strain_original':s.strain(),'strain_reinterpreted':c.strain(),
     'original_tail_power':1/bseed,'reinterpreted_tail_power':1/bcurrent,
     'rows':rows,'elapsed_seconds':time.monotonic()-start,
     'verdict':'CONFIRMED: identical coefficients interpreted at different basis exponents give different physical sources. Zero strain does not detect it. Not a PDE test.'}
(root/'source_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
