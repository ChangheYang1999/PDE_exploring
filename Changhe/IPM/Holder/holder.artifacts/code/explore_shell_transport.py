"""Heuristic finite-circle transport diagnostics, never a continuum certificate."""
import os
os.environ.setdefault('OMP_NUM_THREADS','2')
os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from scipy.special import beta as beta_function

ROOT=Path(__file__).resolve().parents[1]
N=240
angles=(np.arange(N)+0.5)*2*np.pi/N
xy=np.stack((np.cos(angles),np.sin(angles)),axis=1)
rows=[]
for alpha in [0.05,0.1,0.25,0.5,0.75,0.95]:
    for beta in np.linspace(0,np.pi/4,17):
        weights=np.cos(2*angles)*np.cos(angles-beta)/N
        pos=np.flatnonzero(weights>1e-14)
        neg=np.flatnonzero(weights < -1e-14)
        npos,nneg=len(pos),len(neg)
        pindex=np.repeat(np.arange(npos),nneg)
        nindex=np.tile(np.arange(nneg),npos)
        columns=np.arange(npos*nneg)
        A=coo_matrix((np.ones(2*len(columns)),
                    (np.r_[pindex,npos+nindex],np.r_[columns,columns])),
                    shape=(npos+nneg,len(columns))).tocsr()
        costs=np.linalg.norm(xy[pos,None,:]-xy[None,neg,:],axis=2)**alpha
        masses=np.r_[weights[pos],-weights[neg]]
        sol=linprog(costs.ravel(),A_eq=A,b_eq=masses,bounds=(0,None),method='highs')
        if not sol.success:
            raise RuntimeError(sol.message)
        exact_diagonal=2**alpha/np.pi*beta_function((alpha+2)/2,1.5)
        row=dict(alpha=alpha,beta=float(beta),nodes=N,transport=float(sol.fun),
                 diagonal_exact=float(exact_diagonal),
                 primal_residual=float(np.max(np.abs(A@sol.x-masses))))
        rows.append(row)
        (ROOT/'data/shell_transport_exploration.json').write_text(json.dumps({
            'updated_utc':datetime.now(timezone.utc).isoformat(),
            'status':'Heuristic discrete-circle transport only; no certified continuum upper bound.',
            'rows':rows},indent=2)+'\n')
    subset=rows[-17:]
    worst=max(subset,key=lambda row:row['transport'])
    print(alpha,worst['beta'],worst['transport'],exact_diagonal,flush=True)
