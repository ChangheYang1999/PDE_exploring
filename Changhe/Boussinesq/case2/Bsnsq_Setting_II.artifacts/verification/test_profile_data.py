"""Independent analytic tests of both documented radial coefficient maps."""
import json,tempfile
from pathlib import Path
import numpy as np
from profile_data import CoefficientProfile

points=np.array([[0,0],[.2,.7],[-.2,.7],[.2,-.7],[2.,3.],[1e6,3e5]])
rows=[]
for mapname in ['xi','t']:
    c=np.array([[1.,.2,-.1],[.3,.05,0.]])
    with tempfile.TemporaryDirectory(dir='runs') as tmp:
        p=Path(tmp)/'data.npz'
        np.savez(p,ca=c,cG=2*c,beta=3.,L=2.,sigma_a=4/3,sigma_G=7/6,
                 mapname=mapname,beta_map=2.5)
        obj=CoefficientProfile(p)
        x,y=points.T;q=x*x+y*y
        ratio=4/(4+q)
        arg=1-2*ratio if mapname=='xi' else 2*ratio**.2-1
        weight=(2*ratio if mapname=='xi' else ratio)**(4/3)
        exact=weight*(1+.2*arg-.1*(2*arg*arg-1)+(x*x-y*y)/(q+4)*(.3+.05*arg))
        err=float(np.max(np.abs(obj.a(points)-exact)))
        assert err<2e-14,err
        phi=np.array([.23,.7,1.2]);r=1e40
        targets=r*np.column_stack([np.cos(phi),np.sin(phi)])
        normalized=obj.a(targets)*r**(8/3)
        asym=obj.leading_amplitude(c,4/3,phi)
        farerr=float(np.max(np.abs(normalized-asym)))
        assert farerr<2e-12,farerr
        assert obj.a([[.2,.7]])==obj.a([[-.2,.7]])
        rows.append(dict(map=mapname,absolute_error=err,leading_amplitude_error=farerr,metadata=obj.metadata()))
Path('runs/profile_data_tests.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
