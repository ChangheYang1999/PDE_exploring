"""FLOAT normalization check of the exact Fourier HS kernel representation.

For fixed differencek, integrate G(eta+k,eta)^2 overeta and compare to the
known analytic HS constants. This is independent numerical validation only;
quadrature and far tails are not used as a mathematical certificate.
"""
import argparse,json,math
from pathlib import Path
import numpy as np


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    xx,ww=np.polynomial.legendre.leggauss(96)
    edges=[0,.25,.49,.5,.51,1,4,16,64,256,1024,4096]
    r=np.concatenate([(a+b)/2+(b-a)*xx/2 for a,b in zip(edges,edges[1:])])
    weights=np.concatenate([ww*(b-a)/2 for a,b in zip(edges,edges[1:])])
    theta=2*np.pi*(np.arange(2048)+.5)/2048
    X=r[:,None]*np.cos(theta);Y=r[:,None]*np.sin(theta);results=[]
    for kx,ky,expected in [(1,0,np.pi*(np.log(2)-.5)),(0,1,np.pi*(3*np.log(2)-2))]:
        ex=X-kx/2;ey=Y-ky/2;fx=X+kx/2;fy=Y+ky/2
        a=np.hypot(fx,fy);b=np.hypot(ex,ey);wx=fx/a;wy=fy/a;vx=ex/b;vy=ey/b
        direct=(wx-vx)*((wx-vx)*ky-(wy-vy)*kx)
        geometric=(wx-vx)*(a-b)*(wx*vy-wy*vx)
        integral=np.dot(weights*r,np.mean(geometric*geometric,axis=1)*2*np.pi)
        results.append({'k':[kx,ky],'integral_float':float(integral),'analytic_expected':float(expected),
            'absolute_difference':float(abs(integral-expected)),
            'max_direct_vs_geometric_difference':float(np.max(np.abs(direct-geometric)))})
    out={'status':'FLOAT_NORMALIZATION_CHECK_ONLY','rows':results,
        'open_errors':['radial and angular quadrature','omitted eta tail beyond4096']}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
