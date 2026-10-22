"""Run with single-threaded CPU; save absolute errors and real timestamps."""
import json,time,platform,sys
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from cartesian_inverse import CartesianInverse,InverseSettings
from manufactured import Gaussian,SlowStream


def main():
    begin=datetime.now(timezone.utc).isoformat()
    start=time.monotonic()
    points=np.array([[0,0],[0,.4],[.3,.2],[1,-.7],[-2,1.5],[4,3]],float)
    records=[]
    for field in (Gaussian(),SlowStream()):
        for radius in (8.,16.,32.):
            for n in (12,20,32):
                settings=InverseSettings(radius=radius,core_radial_order=n,
                    core_angular_order=2*n,exterior_radial_order=2*n,
                    exterior_angular_order=2*n,decay_power=field.decay_power)
                inv=CartesianInverse(field.omega,settings)
                got=inv.relative(points)
                exact=field.relative(points)
                without=inv.relative(points,include_exterior=False)
                err=float(np.max(np.abs(got-exact)))
                rec={'field':field.name,'radius':radius,'order':n,
                     'max_absolute_error':err,
                     'truncated_max_absolute_error':float(np.max(np.abs(without-exact))),
                     'relative_velocity':got.tolist(),
                     'pointwise_absolute_errors':np.abs(got-exact).tolist()}
                records.append(rec)
                print(field.name,radius,n,'full',err,'truncated',rec['truncated_max_absolute_error'],flush=True)
    result={'started_utc':begin,'ended_utc':datetime.now(timezone.utc).isoformat(),
            'elapsed_seconds':time.monotonic()-start,'python':sys.version,
            'numpy':np.__version__,'platform':platform.platform(),
            'points':points.tolist(),'records':records}
    Path('verification/cartesian_inverse_manufactured.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ('gaussian','slow_stream'):
        final=[r for r in records if r['field']==name and r['order']==32]
        assert max(r['max_absolute_error'] for r in final)<2e-9,(name,final)

if __name__=='__main__':
    main()
