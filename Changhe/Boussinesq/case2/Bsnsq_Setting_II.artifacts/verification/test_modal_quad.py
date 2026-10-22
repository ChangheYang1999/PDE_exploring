import json,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from modal_quad import at_radius,velocity,CoefficientModes
from profile_data import CoefficientProfile

class Manufactured:
    frequencies=np.array([2])
    def __init__(self,alpha=None):self.alpha=alpha
    def h(self,q):
        if self.alpha is None:return np.exp(-q),-np.exp(-q),np.exp(-q)
        a=self.alpha
        return (1+q)**(-a),-a*(1+q)**(-a-1),a*(a+1)*(1+q)**(-a-2)
    def __call__(self,r):
        q=r*r;h,h1,h2=self.h(q)
        return np.array([-2*q*(3*h1+q*h2)])
    def exact(self,points):
        x,y=np.asarray(points).T;h,h1,_=self.h(x*x+y*y)
        return np.column_stack([-x*(h+2*y*y*h1),y*(h+2*x*x*h1)])


def main():
    begin=time.monotonic();rows=[]
    points=np.array([[.01,.02],[1,1],[17,.001],[21,9],[80,30]])
    for alpha in [None,.25,.6,1.3]:
        m=Manufactured(alpha)
        for tol in [1e-7,1e-10,1e-12]:
            u,info=velocity(m,points,.5 if alpha is None else 2*alpha,tol)
            rv=at_radius(m,3,.5 if alpha is None else 2*alpha,tol)
            h,h1,_=m.h(9)
            rows.append(dict(alpha=alpha,tolerance=tol,max_velocity_error=float(np.max(abs(u-m.exact(points)))),
                             sigma_error=rv['sigma']-3*h,slope_error=rv['sigma_prime']-(h+18*h1),info=info))
    # Check exact trigonometric mode extraction independently against Cartesian decoder.
    p=CoefficientProfile('../numerics/states/R4_fix3_N112M28.npz');m=CoefficientModes(p)
    errs=[]
    for r in [.01,1,19,100,1e6]:
        ph=np.array([.03,.31,.98,1.48]);xy=r*np.column_stack([np.cos(ph),np.sin(ph)])
        decoded=p.omega(xy);modal=np.sin(ph[:,None]*m.frequencies)@m(r)
        errs.append(dict(r=r,max_abs=float(np.max(abs(decoded-modal)))))
    record=dict(timestamp=datetime.now(timezone.utc).isoformat(),rows=rows,mode_decoder_errors=errs,
                elapsed_seconds=time.monotonic()-begin,warning='Floating point tests, not interval proof')
    Path('runs/adaptive_modal_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
if __name__=='__main__':main()
