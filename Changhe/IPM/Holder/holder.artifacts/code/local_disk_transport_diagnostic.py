"""Floating diagnostic for transport across local disks, with full identity atoms.

No output is a rigorous upper bound. The sparse LP only selects candidate
couplings; continuum masses and support radii require a separate certificate.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time,math
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.optimize import linprog
ROOT=Path(__file__).resolve().parents[1]

def trial(alpha,phase,nr,nt,delta,neighbors):
    logedges=np.linspace(math.log(delta),math.log(.5),nr+1)
    radii=np.exp((logedges[:-1]+logedges[1:])/2)
    theta=(np.arange(nt)+.5)*2*np.pi/nt+phase/2+np.pi/4
    u=np.exp(1j*theta)
    r=radii[:,None]
    w=(np.cos(2*theta-phase)-r*r*np.real(np.exp(1j*phase)/(1+r*u)**2))/(2*np.pi)
    density=(w*(2*np.pi/nt)*np.diff(logedges)[:,None]).ravel()
    right=(.5+r*u).ravel()
    points=np.concatenate([right,-right,[.5,-.5]])
    masses=np.concatenate([density,-density,[-.5,.5]])
    pos=np.flatnonzero(masses>0);neg=np.flatnonzero(masses<0)
    pp=points[pos];nn=points[neg]
    tree=cKDTree(np.c_[nn.real,nn.imag]);k=min(neighbors,len(neg))
    _,ix=tree.query(np.c_[pp.real,pp.imag],k=k,workers=1)
    if k==1:ix=ix[:,None]
    edges={(i,int(j)) for i,row in enumerate(ix) for j in row}
    # Every signed node has its exact opposite-mass reflected counterpart.
    inverse={int(j):k for k,j in enumerate(neg)}
    half=nr*nt
    for i,index in enumerate(pos):
        reflected=index+half if index<half else index-half if index<2*half else (4*half+1-index)
        edges.add((i,inverse[int(reflected)]))
    # Keep every same-radius/adjacent-radius angular coupling available.
    # Geometric nearest neighbors alone omit the circle transport when the
    # log mesh contains many tiny radii. Give each identity atom all edges.
    neg_rows={row:[] for row in range(nr)}
    atom_neg=[]
    for j,index in enumerate(neg):
        if index>=2*half:atom_neg.append(j)
        else:neg_rows[(int(index)%half)//nt].append(j)
    for i,index in enumerate(pos):
        if index>=2*half:
            edges.update((i,j) for j in range(len(neg)))
        else:
            row=(int(index)%half)//nt
            for rr in range(max(0,row-1),min(nr,row+2)):
                edges.update((i,j) for j in neg_rows[rr])
            edges.update((i,j) for j in atom_neg)
    edges=sorted(edges);ii=np.array([i for i,j in edges]);jj=np.array([j for i,j in edges]);N=len(edges)
    costs=abs(pp[ii]-nn[jj])**alpha
    A=coo_matrix((np.ones(2*N),(np.r_[ii,len(pos)+jj],np.r_[np.arange(N),np.arange(N)])),shape=(len(pos)+len(neg),N)).tocsr()
    rhs=np.r_[masses[pos],-masses[neg]]
    t=time.monotonic()
    res=linprog(costs,A_eq=A,b_eq=rhs,bounds=(0,None),method='highs-ds',options={'time_limit':100,'threads':1})
    out=dict(alpha=alpha,phase_over_pi=phase/np.pi,radial=nr,angles=nt,delta=delta,neighbors=k,nodes=len(points),edges=N,status=res.message,success=bool(res.success),seconds=time.monotonic()-t)
    if res.success:
        residual=float(np.max(abs(A@res.x-rhs)))
        a2=2**(1+alpha/2)/(np.pi*(alpha+2))
        small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
        out.update(local_lp_cost=float(res.fun),small_disk=small,local_plus_small=float(res.fun+small),max_constraint_residual=residual,nonzero_edges=int(np.sum(res.x>1e-12)))
    return out

def main():
    p=argparse.ArgumentParser();p.add_argument('--alpha',type=float,default=.5);p.add_argument('--nr',type=int,default=40);p.add_argument('--nt',type=int,default=48);p.add_argument('--delta',type=float,default=1e-5);p.add_argument('--neighbors',type=int,default=48);p.add_argument('--indices',type=int,nargs='+',default=[0,8,12,16,24,32]);p.add_argument('--out',required=True);a=p.parse_args()
    dest=ROOT/a.out;dest.parent.mkdir(parents=True,exist_ok=True);rows=[]
    for j in a.indices:
        row=trial(a.alpha,np.pi*j/32,a.nr,a.nt,a.delta,a.neighbors);rows.append(row);print(json.dumps(row),flush=True)
        dest.write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),status='FLOATING DIAGNOSTIC ONLY; not a continuum bound',rows=rows),indent=2)+'\n')
if __name__=='__main__':main()
