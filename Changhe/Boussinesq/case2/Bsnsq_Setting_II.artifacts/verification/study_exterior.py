"""Manufactured exterior check and far-tail omissions for immutable controls."""
import json,time,argparse
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from profile_data import CoefficientProfile
from exterior_inverse import exterior_velocity_and_strain
from manufactured import PolynomialRadialStream


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source');ap.add_argument('--tag',default='exterior');args=ap.parse_args()
    start=time.monotonic();rows=[]
    pts=np.array([[0,0],[.2,.7],[-.3,.5],[1.,.1]])
    for alpha in [.25,.75,1.25]:
        obj=PolynomialRadialStream(alpha)
        for R in [2.,10.,50.]:
            q=R*R
            exact=(1+q)**(-alpha)*(1-alpha*q/(2*(1+q)))
            exact_u=exact*pts*np.array([-1,1])
            for order in [24,48,96]:
                U,c=exterior_velocity_and_strain(obj.omega,pts,R,2*alpha,order)
                rows.append(dict(alpha=alpha,R=R,order=order,strain=c,exact_strain=exact,
                                 velocity_error=float(np.max(np.abs(U-exact_u))),strain_error=abs(c-exact)))
    out=dict(timestamp=datetime.now(timezone.utc).isoformat(),manufactured=rows)
    assert max(r['velocity_error'] for r in rows if r['order']==96)<1e-8
    if args.source:
        p=CoefficientProfile(args.source)
        points=np.array([[0,0],[.5,.5],[2.,1.],[10.,.3]])
        base=max(2*p.length,2*np.max(np.linalg.norm(points,axis=1)))
        out.update(source=args.source,metadata=p.metadata(),points=points.tolist(),control=[])
        for R in base*np.array([1.,2.,5.,20.,80.,320.]):
            for order in [48,96,192]:
                U,c=exterior_velocity_and_strain(p.omega,points,float(R),p.tail_power,order)
                row=dict(radius=float(R),order=order,U=U.tolist(),strain=c,
                         strain_normalized=c/(2*p.beta+2),max_abs_velocity=float(np.max(np.abs(U))))
                out['control'].append(row)
                print(json.dumps(row),flush=True)
    out['elapsed_seconds']=time.monotonic()-start
    Path('runs/'+args.tag+'_exterior.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
