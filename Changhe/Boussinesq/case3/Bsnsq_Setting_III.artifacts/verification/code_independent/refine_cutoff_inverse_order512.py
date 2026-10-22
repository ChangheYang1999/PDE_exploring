from pathlib import Path
import json,time
from datetime import datetime,timezone
import numpy as np
from cutoff_polynomial import CutoffPolynomial
from cartesian_inverse import CartesianInverse,InverseSettings

start=time.monotonic();rows=[]
for R in (8.,16.,32.):
    pr=CutoffPolynomial(R)
    ip=np.array([[0.,0.],[.4,-.2],[.2*R,.1*R]])
    expected=pr.velocity(ip,relative=True)
    for order in (512,):
        inv=CartesianInverse(pr.omega,InverseSettings(radius=2.25*R,core_radial_order=order,core_angular_order=2*order,exterior_radial_order=8,exterior_angular_order=8))
        v=inv.relative(ip);center=inv.square_velocity([0.,0.])
        row={'R':R,'order':order,'relative_error':float(np.max(np.abs(v-expected))),'center_error':float(np.max(np.abs(center-[0.,1.]))),'center':center.tolist(),'elapsed_seconds':time.monotonic()-start}
        rows.append(row)
        Path('verification/cutoff_inverse_order512.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','rows':rows},indent=2)+'\n')
        print(row,flush=True)
Path('verification/cutoff_inverse_order512.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPLETE','rows':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
