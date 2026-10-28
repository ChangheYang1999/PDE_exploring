"""Floating diagnostics only. A cycle permutes existing P_R targets."""
import json, math
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

def polygon(n):
    # Counterclockwise rectangle wholly inside the positive K_xx half-lobe.
    vertices = np.array([[.4,.1],[.8,.1],[.8,.2],[.4,.2]])
    return np.concatenate([vertices[k]+np.arange(n)[:,None]/n*(vertices[(k+1)%4]-vertices[k]) for k in range(4)])

def target(p):
    u,v = p[:,0],p[:,1]
    r2=u*u+v*v
    return np.column_stack([2*u*v*v/r2,2*u*u*v/r2])

rows=[]
for n in [8,32,128,512,2048]:
    p=polygon(n); a=target(p)
    old=np.linalg.norm(p-a,axis=1)
    for alpha in [.1,.3,.5,.75,.9]:
        for direction in [-1,1]:
            new=np.linalg.norm(p-np.roll(a,direction,axis=0),axis=1)
            gain=float(np.sum(old**alpha-new**alpha))
            rows.append(dict(n=n,alpha=alpha,direction=direction,gain=gain))
            if gain>0: print(n,alpha,direction,gain)
record=dict(timestamp=datetime.now(timezone.utc).isoformat(),status='FLOATING DIAGNOSTIC, NOT A CERTIFICATE',rectangle=[[.4,.1],[.8,.1],[.8,.2],[.4,.2]],rows=rows)
Path('08_improved_upper_bounds/local_projection/internal_cycle/verification/probe.json').write_text(json.dumps(record,indent=2)+'\n')
