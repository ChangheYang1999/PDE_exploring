"""Manufactured Poisson and stream-gradient tests, including a control study."""
import json,argparse,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from manufactured import PolynomialRadialStream
from duffy_inverse import DuffyQuadrature,stream_duffy,velocity_duffy
from residuals import differentiate
from profile_data import CoefficientProfile


def pair(omega,points,cfg):
    psi=lambda x:stream_duffy(omega,x,cfg)
    value=psi(points)
    px=differentiate(psi,points,0);py=differentiate(psi,points,1)
    lap=differentiate(psi,points,0,derivative=2)+differentiate(psi,points,1,derivative=2)
    return value,np.column_stack([-py,px]),-lap-omega(points)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source');ap.add_argument('--tag',default='manufactured');args=ap.parse_args()
    start=time.monotonic();stamp=lambda:datetime.now(timezone.utc).isoformat()
    pts=np.array([[.2,.7],[1.3,.1],[.7,1.8]])
    rows=[]
    for alpha in [None,.25]:
        obj=PolynomialRadialStream(alpha)
        for order in [32,64,128]:
            cfg=DuffyQuadrature(order,1 if alpha is None else 2*alpha,1.)
            psi,u,E=pair(obj.omega,pts,cfg)
            row=dict(exponent=alpha,order=order,max_stream_error=float(np.max(np.abs(psi-obj.psi(pts)))),
                     max_gradient_error=float(np.max(np.abs(u-obj.velocity(pts)))),max_poisson_defect=float(np.max(np.abs(E))))
            rows.append(row);print(json.dumps(row),flush=True)
    result=dict(timestamp=stamp(),manufactured=rows)
    if args.source:
        obj=CoefficientProfile(args.source);pts=np.array([[1.,1.],[15.,.3],[21.,9.]])
        result.update(source=args.source,metadata=obj.metadata(),points=pts.tolist(),control=[])
        for order in [64,128,192]:
            cfg=DuffyQuadrature(order,obj.tail_power,obj.length)
            psi,u,E=pair(obj.omega,pts,cfg)
            direct=velocity_duffy(obj.omega,pts,cfg)
            row=dict(order=order,psi=psi.tolist(),gradient_velocity=u.tolist(),kernel_velocity=direct.tolist(),
                     poisson_defect=E.tolist(),max_gradient_disagreement=float(np.max(np.abs(u-direct))))
            result['control'].append(row);print(json.dumps(row),flush=True)
    result['elapsed_seconds']=time.monotonic()-start
    Path('runs/'+args.tag+'_stream.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
