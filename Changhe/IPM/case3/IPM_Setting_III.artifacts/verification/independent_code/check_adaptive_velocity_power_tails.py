"""Slow algebraic-tail manufacture with independent high precision closed form."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']: os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import math,json,hashlib
import numpy as np
import mpmath as mp
from adaptive_hydrostatic_velocity import AdaptiveVerticalVelocity
R=Path('research/hydrostatic_velocity_sequence_audit');V=R/'verification'
assert V.resolve().is_relative_to(Path('verification'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];rows=[]
def ck(name,b,e=None): checks.append(dict(name=name,passed=bool(b),evidence=e))
def jet_for(p):
    b=(p-1)/2
    def jet(x,y):
        x,y=np.broadcast_arrays(x,y);S=1+x*x+y*y
        g=y*S**b
        gx=2*b*x*y*S**(b-1)
        gy=S**b+2*b*y*y*S**(b-1)
        gxx=2*b*y*S**(b-1)+4*b*(b-1)*x*x*y*S**(b-2)
        return np.stack([g,gx,gy,gxx],axis=-1)
    return jet

def exact_float(value):
    a,b=float(value).as_integer_ratio()
    return mp.mpf(a)/b

def reference(p,x,y,dps):
    with mp.workdps(dps):
        xx=exact_float(x);yy=exact_float(y);b=exact_float((p-1)/2);B=1+xx*xx
        def primitive(beta):
            return yy*B**beta*mp.hyp2f1(mp.mpf(1)/2,-beta,mp.mpf(3)/2,-yy*yy/B)
        values=[xx*(B+yy*yy)**b,-primitive(b)-2*b*xx*xx*primitive(b-1)]
        return [mp.nstr(value,dps-5) for value in values]
points=[(0,0),(.03,0),(0,.03),(.137,.219),(.5,.5),(3,4),(.01,10000),(10000,0),(1000,1000),(-.137,.219),(.137,-.219),(-.137,-.219)]
for p in [.5,1/3]:
    jet=jet_for(p)
    for x,y in points:
        r=math.hypot(x,y);ref70=reference(p,x,y,70);ref110=reference(p,x,y,110)
        with mp.workdps(110):
            difference=max(abs(mp.mpf(a)-mp.mpf(b)) for a,b in zip(ref70,ref110))
            scale=max(mp.mpf(1),*(abs(mp.mpf(a)) for a in ref110))
            ck(f'high precision {p,x,y}',difference/scale<mp.mpf('1e-60'),mp.nstr(difference/scale,20))
        exact=list(map(float,ref110))
        for split in [37,512,1024]:
            result=AdaptiveVerticalVelocity(jet,p,split=split).at(x,y)
            weighted=max(abs(a-b) for a,b in zip(result['V'],exact))/(1+r)**p
            name=str((p,x,y,split))
            ck('power inverse '+name,weighted<2e-10,weighted)
            ck('no adaptive warning '+name,not result['messages'],result['messages'])
            ck('finite estimates '+name,np.isfinite(result['estimated_error']).all())
            rows.append(dict(p=p,x=x,y=y,r=r,split=split,reference70=ref70,reference110=ref110,weighted_error=weighted,result=result))
# Deliberate invalid input must fail instead of silently clipping.
inv=AdaptiveVerticalVelocity(jet_for(.5),.5)
for point in [(float('inf'),0),(0,float('nan'))]:
    try:
        inv.at(*point);raised=False
    except ValueError:
        raised=True
    ck('guard coordinate '+str(point),raised)
def invalid_jet(x,y):
    return np.full((np.asarray(y).size,4),float('nan'))
try:
    AdaptiveVerticalVelocity(invalid_jet,.5).at(1,1);raised=False
except FloatingPointError:
    raised=True
ck('nonfinite sample rejected',raised)
out=dict(status='PASS' if all(q['passed'] for q in checks) else 'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,proof_sha256=sha(R/'ADAPTIVE_REVIEW_PROOF.md'),module_sha256=sha('independent_code/adaptive_hydrostatic_velocity.py'),driver_sha256=sha(__file__),scope='Empirical complete adaptive inverse tests; high precision references are not interval certificates')
(V/'ADAPTIVE_POWER_MANUFACTURE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(checks));print([q for q in checks if not q['passed']]);print('max weighted error',max(q['weighted_error'] for q in rows))
raise SystemExit(out['status']!='PASS')
