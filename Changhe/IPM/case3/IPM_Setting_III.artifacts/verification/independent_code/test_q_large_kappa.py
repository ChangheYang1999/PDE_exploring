"""Regression of safeguarded radial inversion at large compactification exponents."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json
import numpy as np
from q_checkpoint_reader import QCheckpoint
rows=[]
for kap in [1.05,1.5,3.,11.,17.,21.,51.,101.]:
    c=object.__new__(QCheckpoint);c.kappa=kap;c.L=1.;c.M=2;c.coeff=[np.array([1.]),np.array([.13])]
    radii=np.concatenate(([0.],np.geomspace(1e-100,1e140,1001),np.linspace(.6,.9,701)))
    t,sg,w=c.coordinates(radii);mask=radii>0
    assert np.all(np.isfinite(t)) and np.all(np.isfinite(sg)) and np.all(np.isfinite(w))
    assert (t[0],sg[0],w[0])==(-1.,0.,1.)
    log_forward=.5*np.log(sg[mask])-kap*np.log(2*w[mask])
    err=np.max(abs(log_forward-np.log(radii[mask]))/(1+abs(np.log(radii[mask]))))
    assert err<3e-13,(kap,err)
    # Density retains parity even where the endpoint coordinate rounds to +-1.
    x=radii[1:]*.6;y=radii[1:]*.8
    v=c.rho(x,y)
    assert np.array_equal(v,c.rho(-x,y))
    assert np.array_equal(v,-c.rho(x,-y))
    rows.append({'kappa':kap,'count':len(radii),'max_relative_log_map_error':float(err)})
if len(sys.argv)>1:
    c=QCheckpoint(sys.argv[1])
    for lo,hi in [(1e-7,1e-3),(1e-3,1.),(1.,1e2),(1e2,1e80)]:
        rr=np.geomspace(lo,hi,501);t,sg,w=c.coordinates(rr)
        forward=.5*np.log(sg)-c.kappa*np.log(2*w)+np.log(c.L)
        err=np.max(abs(forward-np.log(rr))/(1+abs(np.log(rr))))
        assert err<3e-13
        rows.append({'snapshot':str(sys.argv[1]),'kappa':c.kappa,'interval':[lo,hi],'max_relative_log_map_error':float(err)})
root=Path('evidence/q_reader_tests');root.mkdir(exist_ok=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','rows':rows,'scope':'Forward logarithmic map equation and exact density parity. Does not test a PDE or verify any candidate.'}
(root/'large_kappa.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
