"""Exploration of the balanced projection witness. No numerical certification."""
from pathlib import Path
from datetime import datetime,timezone
from numpy.polynomial.legendre import leggauss
from scipy.optimize import differential_evolution
from scipy.special import gamma
import numpy as np,json,argparse

def psi(points,alpha,a):
    X=np.abs(points[...,0]);Y=points[...,1];dy=np.abs(Y)-a;dx=X-.5
    seg=np.hypot(dx,np.maximum(dy,0));projection=dx/2+np.sqrt(3)*dy/2
    ray=np.where(projection>0,abs(np.sqrt(3)*dx/2-dy/2),np.hypot(dx,dy))
    dist=np.minimum(seg,ray);sgn=np.sign(dx-np.maximum(dy,0)/np.sqrt(3))
    v=np.hypot(dist,Y);P=np.divide(2*dist*abs(Y),v,out=np.zeros_like(v),where=v>0)
    return .5*np.sign(sgn*Y)*P**alpha

def values(points,alpha,a):
    x=np.array([.5,0.]);y=-x
    return psi(points,alpha,a)+.5*(np.linalg.norm(points-x,axis=-1)**alpha-np.linalg.norm(points-y,axis=-1)**alpha)

def integral(alpha,a,nr=256,nt=320):
    delta=min(.001,a/20);R=1e5;g,w=leggauss(nr);t,v=leggauss(nt);total=0.
    for left,right in [(delta,.5),(.5,2.),(2.,R)]:
        ul,ur=np.log(left),np.log(right);r=np.exp((ul+ur)/2+(ur-ul)/2*g)[:,None]
        lim=np.where(r<=.5,np.pi,np.arccos(np.clip(-.5/r,-1,1)))
        theta=lim*(t+1)[None,:]/2;X=.5+r*np.cos(theta);Y=r*np.sin(theta)
        z=X+1j*Y;nu=-(z/(np.pi*(z*z-.25)**2)).imag
        p=psi(np.stack([X,Y],axis=-1),alpha,a)
        total+=np.sum(4*nu*p*r*r*lim*w[:,None]*v[None,:])*(ur-ul)/4
    A=gamma((alpha+2)/2)/(2*np.sqrt(np.pi)*gamma((alpha+3)/2))
    # Own-pole omitted disks have leading contribution 2 A delta^alpha/alpha.
    # Cross terms and the omitted exterior are not certified here.
    return float(total+2*A*delta**alpha/alpha)

def sup_search(alpha,a):
    def objective(v):
        p=np.array(v[:2]);q=np.array(v[2:]);d=np.linalg.norm(p-q)
        if d<1e-12:return 0.
        return -abs(values(p,alpha,a)-values(q,alpha,a))/d**alpha
    results=[]
    for seed in [29,51]:
        out=differential_evolution(objective,[(-3,3)]*4,seed=seed,popsize=15,maxiter=300,tol=1e-8,polish=True)
        results.append(dict(ratio=-float(out.fun),points=out.x.tolist()))
    for pole in [[.5,0],[-.5,0]]:
        def obj(q):return objective([*pole,*q])
        out=differential_evolution(obj,[(-3,3)]*2,seed=32,popsize=15,maxiter=200,tol=1e-9,polish=True)
        results.append(dict(ratio=-float(out.fun),points=[*pole,*out.x]))
    return max(results,key=lambda x:x['ratio'])
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--alpha',type=float,default=.5);p.add_argument('--shapes',type=float,nargs='+',default=[.5,1.,1.5]);p.add_argument('--out',default='data/balanced_projection_diagnostic.json');args=p.parse_args();rows=[]
    for a in args.shapes:
        J=integral(args.alpha,a);sup=sup_search(args.alpha,a);numerator=np.hypot(J,args.alpha/(2*(args.alpha+2)))+.5
        row=dict(alpha=args.alpha,a=a,J=J,numerator=float(numerator),sup_search=sup,diagnostic_ratio=float(numerator/sup['ratio']));rows.append(row);print(row,flush=True)
    Path(args.out).write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,status='Floating diagnostics only. Computed supremum is only a lower bound on the seminorm. No operator lower bound follows from the ratios.'),indent=2)+'\n')
