"""Propose denser exact node data by floating interpolation. Not a certificate.
The finite envelope remains Holder1 for arbitrary proposed values.
"""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
from scipy.interpolate import RegularGridInterpolator,LinearNDInterpolator
from scipy.spatial import cKDTree
import numpy as np,json,argparse,hashlib
ROOT=Path(__file__).resolve().parents[1]

def main():
 p=argparse.ArgumentParser();p.add_argument('--factor',type=int,default=2);p.add_argument('--out',required=True);args=p.parse_args();factor=args.factor
 source=ROOT/'numerics_data/lp4/D_a05_b0.json';src=json.loads(source.read_text());pts=np.array(src['nodes']);pts[:,0]-=.5
 exactpath=ROOT/'data/envelope_D_half_axis_nodes_symmetric.json';exact=json.loads(exactpath.read_text());old=np.array(exact['nodes'],float)
 _,idx=cKDTree(old[:,:2]).query(pts);values=old[idx,2];info=src['info'];nt=16;nf=48;jn=info['J'];jf=info['Jf']
 near=[]
 for start,center,pole in [(0,-.5,.5),(info['n_near0'],.5,-.5)]:
  xy=pts[start:start+jn*nt].reshape(jn,nt,2);v=values[start:start+jn*nt].reshape(jn,nt)
  rel=xy-np.array([center,0]);r=np.linalg.norm(rel,axis=2)[:,0];theta=np.mod(np.arctan2(rel[0,:,1],rel[0,:,0]),2*np.pi);order=np.argsort(theta);theta=theta[order]
  profile=((v-pole)/r[:,None]**.5)[:,order];theta=np.concatenate([theta[-1:]-2*np.pi,theta,theta[:1]+2*np.pi]);profile=np.column_stack([profile[:,-1],profile,profile[:,0]])
  interp=RegularGridInterpolator((np.log(r[::-1]),theta),profile[::-1],bounds_error=False,fill_value=None)
  near.append((center,pole,interp,float(r.min()),float(r.max())))
 start=info['n_near0']+info['n_near1'];xy=pts[start:start+jf*nf].reshape(jf,nf,2);v=values[start:start+jf*nf].reshape(jf,nf)
 r=np.linalg.norm(xy,axis=2)[:,0];theta=np.mod(np.arctan2(xy[0,:,1],xy[0,:,0]),2*np.pi);order=np.argsort(theta);theta=theta[order]
 profile=(v/r[:,None]**.5)[:,order];theta=np.concatenate([theta[-1:]-2*np.pi,theta,theta[:1]+2*np.pi]);profile=np.column_stack([profile[:,-1],profile,profile[:,0]])
 far=RegularGridInterpolator((np.log(r),theta),profile,bounds_error=False,fill_value=None)
 m=(np.linalg.norm(pts,axis=1)<2)&(np.linalg.norm(pts-[.5,0],axis=1)>.15)&(np.linalg.norm(pts+[.5,0],axis=1)>.15)
 mid=LinearNDInterpolator(pts[m],values[m])
 def propose(q):
  q=np.asarray(q);out=np.empty(len(q));remaining=np.ones(len(q),bool)
  for center,pole,interp,rmin,rmax in near:
   rel=q-[center,0];rr=np.linalg.norm(rel,axis=1);mask=(rr<.5)&remaining
   th=np.mod(np.arctan2(rel[mask,1],rel[mask,0]),2*np.pi);safe=np.maximum(rr[mask],rmin)
   out[mask]=pole+rr[mask]**.5*interp(np.column_stack([np.log(safe),th]));remaining[mask]=False
  rr=np.linalg.norm(q,axis=1);mask=(rr>=1)&remaining
  th=np.mod(np.arctan2(q[mask,1],q[mask,0]),2*np.pi)
  out[mask]=rr[mask]**.5*far(np.column_stack([np.log(rr[mask]),th]));remaining[mask]=False
  out[remaining]=mid(q[remaining]);assert np.all(np.isfinite(out))
  return out
 proposals=[old[:,:2]]
 for center,pole,interp,rmin,rmax in near:
  rr=np.geomspace(rmin,.5,jn*factor);th=np.arange(nt*factor)*2*np.pi/(nt*factor)
  proposals.append(np.column_stack([(center+rr[:,None]*np.cos(th)).ravel(),(rr[:,None]*np.sin(th)).ravel()]))
 rr=np.geomspace(1,r.max(),jf*factor);th=np.arange(nf*factor)*2*np.pi/(nf*factor)
 proposals.append(np.column_stack([(rr[:,None]*np.cos(th)).ravel(),(rr[:,None]*np.sin(th)).ravel()]))
 axis=np.arange(0,1.01,.05/factor);X,Y=np.meshgrid(axis,axis);q=np.column_stack([X.ravel(),Y.ravel()]);mask=(np.linalg.norm(q-[.5,0],axis=1)>=.49)&(np.linalg.norm(q,axis=1)<=1.01);proposals.append(q[mask])
 q=np.vstack(proposals);q=np.round(abs(q),12);q=np.unique(q,axis=0)
 vs=sum(sx*propose(q*[sx,sy]) for sx in [-1,1] for sy in [-1,1])/4
 nodes={}
 for (x,y),v in zip(q,vs):
  dx=Decimal(f'{x:.12f}');dy=Decimal(f'{y:.12f}');dv=Decimal(f'{v:.12f}')
  if dx==0:dv=Decimal(0)
  for sx in [-1,1]:
   for sy in [-1,1]:nodes[(str(dx*sx),str(dy*sy))]=str(dv*sx)
 rows=[[x,y,v] for (x,y),v in nodes.items()]
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha='1/2',nodes=rows,symmetry='central odd and even Y, exact decimal reflections',factor=factor,proposal_method='linear interpolation of local normalized radial profiles in log radius and periodic angle; planar middle interpolation; arbitrary data are allowed by envelope theorem',input_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,exactpath]})
 (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n');print('nodes',len(rows),args.out,flush=True)
if __name__=='__main__':main()
