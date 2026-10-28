"""Floating evaluation of the exact finite-envelope witness, diagnostic only."""
from pathlib import Path
import json
import numpy as np
from scipy.spatial.distance import cdist

class Envelope:
    def __init__(self,path='data/envelope_D_half_axis_nodes_symmetric.json'):
        data=json.loads(Path(path).read_text())
        assert data['alpha']=='1/2'
        nodes=np.array(data['nodes'],dtype=float)
        self.p=nodes[:,:2];self.v=nodes[:,2]
    def evaluate(self,q,batch=1024):
        q=np.asarray(q,dtype=float).reshape(-1,2)
        out=np.empty(len(q));nearest=np.empty(len(q))
        for s in range(0,len(q),batch):
            e=min(len(q),s+batch)
            d=cdist(q[s:e],self.p,metric='sqeuclidean')
            np.sqrt(d,out=d)
            nearest[s:e]=np.min(d,axis=1)
            np.sqrt(d,out=d)
            low=np.max(self.v[None,:]-d,axis=1)
            high=np.min(self.v[None,:]+d,axis=1)
            out[s:e]=(low+high)/2
        return out,nearest
