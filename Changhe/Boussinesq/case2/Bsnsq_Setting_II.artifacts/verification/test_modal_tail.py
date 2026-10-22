import json,time
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from modal_tail import exterior
from test_modal_quad import Manufactured
from modal_quad import velocity

rows=[];start=time.monotonic()
points=np.array([[.01,.03],[1,0],[0,1],[1,1]])
for a in [None,.25,.6,1.3]:
    m=Manufactured(a)
    for R in [2,10,100]:
        data=exterior(m,R,points,.5 if a is None else 2*a,1e-11)
        h,h1,_=m.h(R*R);c=h+.5*R*R*h1
        exact=c*np.column_stack([-points[:,0],points[:,1]])
        err=float(np.max(abs(np.array(data['U'])-exact)))
        assert err<1e-10,(a,R,err)
        assert abs(c-data['strain_exterior'])<1e-10
        rows.append(dict(alpha=a,radius=R,velocity_error=err,strain_error=abs(c-data['strain_exterior']),info=data['info']))
    axes=np.array([[0,0],[0,1],[1,0],[-1,0],[0,-1]])
    u,info=velocity(m,axes,.5 if a is None else 2*a,1e-11)
    assert np.max(abs(u-m.exact(axes)))<1e-10
    assert np.all(u[axes[:,0]==0,0]==0) and np.all(u[axes[:,1]==0,1]==0)
Path('runs/adaptive_modal_tail_tests.json').write_text(json.dumps(dict(timestamp=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,rows=rows,axis_parity='exact zeros checked'),indent=2)+'\n')
print('PASS',len(rows),'exterior cases and axis parity on4 manufactured fields')
