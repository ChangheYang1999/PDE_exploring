"""Independent quadrature of the finite-envelope R_1^2 witness. Not certified."""
from pathlib import Path
from datetime import datetime,timezone
from numpy.polynomial.legendre import leggauss
from envelope_witness import Envelope
import numpy as np,json,argparse,time

def quadrature(env,n,delta=1e-6,R=1e6):
    gx,gw=leggauss(n);total=0.;fp=float(env.evaluate([[.5,0]])[0][0]);parts=[]
    for left,right in [(delta,.5),(.5,2.),(2.,R)]:
        ul,ur=np.log(left),np.log(right)
        r=np.exp((ul+ur)/2+(ur-ul)/2*gx)[:,None]
        angle=np.where(r<=.5,np.pi,np.arccos(np.clip(-.5/r,-1,1)))
        theta=angle*(gx+1)[None,:]/2
        X=.5+r*np.cos(theta);Y=r*np.sin(theta)
        fv,_=env.evaluate(np.column_stack([X.ravel(),Y.ravel()]));fv=fv.reshape(X.shape)
        own=((X-.5)**2-Y*Y)/(2*np.pi*r**4)
        other=((X+.5)**2-Y*Y)/(2*np.pi*((X+.5)**2+Y*Y)**2)
        integrand=own*(fv-fp)-other*fv if right<=.5 else (own-other)*fv
        val=np.sum(integrand*r*r*angle*gw[:,None]*gw[None,:])*(ur-ul)
        parts.append(float(val));total+=val
    return dict(order=n,pole_value=fp,parts=parts,compact_functional=float(total-fp),delta=delta,R=R)

def main():
    p=argparse.ArgumentParser();p.add_argument('--orders',default='64,128');p.add_argument('--out',default='data/envelope_D_half_float.json');args=p.parse_args()
    env=Envelope();start=time.monotonic();rows=[]
    for n in map(int,args.orders.split(',')):
        row=quadrature(env,n);rows.append(row);print(row,'seconds',time.monotonic()-start,flush=True)
    Path(args.out).write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Floating diagnostic, no quadrature error certificate',rows=rows,elapsed_seconds=time.monotonic()-start),indent=2)+'\n')
if __name__=='__main__':main()
