"""Regression for an exact zero radius and mixed radial arrays in Q reader."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from q_checkpoint_reader import QCheckpoint
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
root=Path('evidence/q_reader_tests');root.mkdir(exist_ok=True,parents=True)
rows=[]
for kap in (1.05,1.5,3.,11.):
    path=root/'origin_manufactured.npz'
    np.savez_compressed(path,N=3,M=2,L=.7,p=kap,gamma=1-1/kap,cl=1/(1-1/kap),u=np.array([.91,.17,-.08,.03,-.12,.07,.011]))
    c=QCheckpoint(path)
    r=np.array([0.,1e-40,1e-7,.05,1.,1e30,0.]);t,s,w=c.coordinates(r)
    assert np.all(t[r==0]==-1) and np.all(s[r==0]==0) and np.all(w[r==0]==1)
    assert float(c.rho(0.,0.))==0.
    assert np.all(np.isfinite(c.rho(r/2,r/3)))
    h=c.L*2**(-kap)*1e-4
    slope=float(c.rho(0.,h)/h);exact=c.center_and_tail()['a0']
    assert abs(slope-exact)<1e-7
    rows.append({'kappa':kap,'slope':slope,'exact_slope':exact,'error':abs(slope-exact),'zero_coordinates':[float(t[0]),float(s[0]),float(w[0])]})
c=QCheckpoint('../numerics/artifacts/data/qls_cl1.5_N96_Lf0.125.pt')
length=c.L*2**(-c.kappa)
inv=DirectInverse(c.rho,Quadrature(24,128,96,2.,length,c.p,16*c.L,c.kappa))
u=inv.velocity(0.,0.);ct=c.center_and_tail()
fd=[]
for step in (.003,.0015,.00075):
    x,y=cartesian_gradient(c.rho,0.,0.,step,length)
    fd.append({'step':step,'rho_x':float(x),'rho_y':float(y),'slope_error':float(abs(y-ct['a0']))})
assert max(abs(u))<1e-12 and min(row['slope_error'] for row in fd)<1e-10
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','mixed_array_checks':rows,'published_origin_U':u.tolist(),'published_origin_gradient':fd,'scope':'Exact zero radius bypass only; mixed and positive radius reconstructions tested. Exact-axis residual ratios remain geometrically excluded, with raw values preserved.'}
(root/'origin_endpoint.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
