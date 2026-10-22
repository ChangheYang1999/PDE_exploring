"""Centered exterior-source contribution through adaptive radial Green integrals."""
import argparse,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from modal_quad import CoefficientModes,radial_integrals
from profile_data import CoefficientProfile


def exterior(modes,radius,points,tail_power,tolerance=1e-10):
    n=np.asarray(modes.frequencies)
    _,b,info=radial_integrals(modes,radius,tail_power,tolerance)
    points=np.asarray(points,float);u=np.zeros_like(points)
    for i,(x,y) in enumerate(points):
        r=np.hypot(x,y)
        if r>=radius:raise ValueError('All targets must lie inside the excluded source disk')
        if r==0:continue
        angle=np.arctan2(y,x)
        v=radius**2/(2*r)*(r/radius)**n*b
        ur=-np.sum(v*np.cos(n*angle));up=np.sum(v*np.sin(n*angle))
        u[i]=[ur*np.cos(angle)-up*np.sin(angle),ur*np.sin(angle)+up*np.cos(angle)]
        if x==0:u[i,0]=0
        if y==0:u[i,1]=0
    return dict(strain_exterior=float(b[0]/2),U=u.tolist(),info=info)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tag',default='published_gauss_N112');args=ap.parse_args()
    tag=args.tag;source=Path('data/control_snapshots/'+tag+'.npz');p=CoefficientProfile(source);m=CoefficientModes(p)
    radii=[.5,1,2,5,10,20,40,80,160,320,640,1280,1e4,1e6,1e10,1e14]
    # Common near-center targets for every radius; larger probes where admissible.
    small=[[.1,.07],[.2,0],[0,.2]];large=[[1,1],[15,.3],[21,9]]
    report=dict(timestamp_start=datetime.now(timezone.utc).isoformat(),source=str(source),
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),metadata=p.metadata(),
        warning='Centered circular source truncation; adaptive quadrature estimates are not rigorous error bounds.',rows=[])
    start=time.monotonic();dest=Path('runs/'+tag+'_modal_tail.json')
    for tol in [1e-9,1e-11]:
        for r in radii:
            pts=small+[v for v in large if np.linalg.norm(v)<r]
            row=dict(radius=r,tolerance=tol,points=pts,**exterior(m,r,pts,p.tail_power,tol))
            report['rows'].append(row)
            report['last_update']=datetime.now(timezone.utc).isoformat();report['elapsed_seconds']=time.monotonic()-start
            dest.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps({k:row[k] for k in ['radius','tolerance','strain_exterior','info']}),flush=True)
    report['timestamp_end']=datetime.now(timezone.utc).isoformat()
    dest.write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
