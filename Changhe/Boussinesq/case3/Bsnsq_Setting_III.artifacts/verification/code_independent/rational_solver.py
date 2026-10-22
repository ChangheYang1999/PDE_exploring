"""Independent rational-basis stationary least-squares exploration.

No GPU, no server, no fitting-lane imports. Uses analytic product-rule
matrices, affine elimination of three center constraints, and scipy TRF.
This solver's residuals are training diagnostics. Validation uses the
separate finite-difference and whole-plane Cartesian inverse programs.
"""
import argparse,json,time,os
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from rational_basis import make_terms,matrix,RationalProfile


def collocation(radius,nrad,nangle,seed=0):
    rng=np.random.default_rng(seed)
    radii=np.r_[0.,np.geomspace(.03,radius,nrad)]
    angles=np.linspace(-np.pi/2,np.pi/2,nangle+2)[1:-1]
    angles+=rng.uniform(-.15,.15,size=len(angles))*np.pi/(nangle+1)
    rr,aa=np.meshgrid(radii,angles,indexing='ij')
    pts=np.column_stack((rr.ravel()*np.cos(aa.ravel()),rr.ravel()*np.sin(aa.ravel())))
    # Exact invariant axis and both signs of y; no boundary at y=0.
    axis=np.column_stack((np.zeros(2*len(radii)),np.r_[radii,-radii]))
    return np.unique(np.vstack((pts,axis)),axis=0)


def eliminate(rows,targets,pivots):
    n=rows.shape[1]
    free=np.array([i for i in range(n) if i not in pivots])
    block=rows[:,pivots]
    offset=np.zeros(n);offset[pivots]=np.linalg.solve(block,targets)
    null=np.zeros((n,len(free)));null[free,np.arange(len(free))]=1.
    null[pivots,:]=-np.linalg.solve(block,rows[:,free])
    return offset,null


class Matrices:
    def __init__(self,beta,psi_terms,theta_terms,points):
        self.beta=beta
        self.x=points[:,0]
        self.y=points[:,1]
        self.points=points
        self.psi_terms=psi_terms;self.theta_terms=theta_terms
        self.A=-matrix(psi_terms,beta,'psi',points,dy=1,divide_x=1)
        self.B=matrix(psi_terms,beta,'psi',points,dx=1)-matrix(psi_terms,beta,'psi',[[0,0]],dx=1)
        self.G=matrix(psi_terms,beta,'omega',points,divide_x=1)
        # Differentiate Omega/x as a polynomial-power expansion explicitly.
        from rational_basis import omega_expansion,differentiate,evaluate_terms
        for axis,label in ((0,'Gx'),(1,'Gy')):
            cols=[]
            for term in psi_terms:
                e=omega_expansion(term,beta)
                e={(i-1,j,q):c for (i,j,q),c in e.items()}
                e=differentiate(e,axis,term.scale)
                cols.append(evaluate_terms(e,self.x,self.y,term.scale))
            setattr(self,label,np.column_stack(cols))
        self.F=matrix(theta_terms,beta,'theta',points,divide_x=2)
        from rational_basis import expansion
        for axis,label in ((0,'Fx'),(1,'Fy')):
            cols=[]
            for term in theta_terms:
                e=expansion(term,beta,'theta')
                e={(i-2,j,q):c for (i,j,q),c in e.items()}
                e=differentiate(e,axis,term.scale)
                cols.append(evaluate_terms(e,self.x,self.y,term.scale))
            setattr(self,label,np.column_stack(cols))
        c=matrix(psi_terms,beta,'psi',[[0,0]],dx=1,dy=1)[0]
        b=matrix(psi_terms,beta,'omega',[[0,0]],dx=1)[0]
        a=matrix(theta_terms,beta,'theta',[[0,0]],dx=2)[0]/2
        pivot_c=next(i for i,t in enumerate(psi_terms) if t.i==1 and t.j==1 and t.scale==1 and t.tail_order==1)
        pivot_b=next(i for i,t in enumerate(psi_terms) if t.i==1 and t.j==0 and t.scale==1 and t.tail_order==1)
        pivot_a=next(i for i,t in enumerate(theta_terms) if t.i==2 and t.j==0 and t.scale==1 and t.tail_order==1)
        self.p0,self.pn=eliminate(np.vstack((c,b)),np.array([1+beta/2,4/beta]),[pivot_c,pivot_b])
        self.t0,self.tn=eliminate(a[None,:],np.array([1.]),[pivot_a])
        self.np=self.pn.shape[1];self.nt=self.tn.shape[1]
        self.freep=[i for i in range(len(psi_terms)) if i not in (pivot_c,pivot_b)]
        self.freet=[i for i in range(len(theta_terms)) if i!=pivot_a]
        r=np.linalg.norm(points,axis=1)
        self.wf=(1+r)**(1+2/beta)
        self.wg=(1+r)**(1+1/beta)
        self.center_rows=(a,c,b)

    def unpack(self,z):
        return self.p0+self.pn@z[:self.np],self.t0+self.tn@z[self.np:]

    def evaluate(self,z,jac=False):
        p,t=self.unpack(z)
        A=self.beta+self.A@p;B=self.beta*self.y+self.B@p
        F=self.F@t;Fx=self.Fx@t;Fy=self.Fy@t
        G=self.G@p;Gx=self.Gx@p;Gy=self.Gy@p
        rf=(2*A-self.beta+2)*F+self.x*A*Fx+B*Fy
        rg=(A+1)*G+self.x*A*Gx+B*Gy-2*F-self.x*Fx
        if not jac:return np.r_[self.wf*rf,self.wg*rg]
        jf_p=(2*F+self.x*Fx)[:,None]*self.A+Fy[:,None]*self.B
        jf_t=(2*A-self.beta+2)[:,None]*self.F+(self.x*A)[:,None]*self.Fx+B[:,None]*self.Fy
        jg_p=(G+self.x*Gx)[:,None]*self.A+Gy[:,None]*self.B+(A+1)[:,None]*self.G+(self.x*A)[:,None]*self.Gx+B[:,None]*self.Gy
        jg_t=-2*self.F-self.x[:,None]*self.Fx
        top=np.column_stack((jf_p@self.pn,jf_t@self.tn))*self.wf[:,None]
        bot=np.column_stack((jg_p@self.pn,jg_t@self.tn))*self.wg[:,None]
        return np.vstack((top,bot))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--beta',type=float,default=3.)
    parser.add_argument('--degree',type=int,default=4)
    parser.add_argument('--radius',type=float,default=12.)
    parser.add_argument('--nrad',type=int,default=12)
    parser.add_argument('--nangle',type=int,default=9)
    parser.add_argument('--seed',type=int,default=0)
    parser.add_argument('--max-nfev',type=int,default=600)
    parser.add_argument('--scales',default='1,4')
    parser.add_argument('--tails',default='1,2')
    parser.add_argument('--out',required=True)
    parser.add_argument('--free-beta',action='store_true')
    parser.add_argument('--beta-max',type=float,default=8.)
    parser.add_argument('--restart')
    args=parser.parse_args()
    start=time.monotonic();began=datetime.now(timezone.utc).isoformat()
    scales=tuple(float(s) for s in args.scales.split(','));tails=tuple(int(s) for s in args.tails.split(','))
    if 1. not in scales:raise ValueError('scale 1 required for pivot normalization')
    ps=make_terms(args.degree,scales,tails,'psi');ts=make_terms(args.degree,scales,tails,'theta')
    # Remove exact uniform-velocity columns on the fixed beta=2 branch.
    # For free beta the search is beta>2, with beta=2 studied separately.
    if not args.free_beta:
        ps=[t for t in ps if not (t.i==1 and t.j==0 and abs(2-t.tail_order/args.beta-1)<1e-14)]
    pts=collocation(args.radius,args.nrad,args.nangle,args.seed)
    m=Matrices(args.beta,ps,ts,pts)
    rng=np.random.default_rng(args.seed)
    z0=np.zeros(m.np+m.nt) if args.seed==0 else rng.normal(0,.03,m.np+m.nt)
    if args.restart:
        previous=RationalProfile.from_dict(json.loads(Path(args.restart).read_text()))
        pc=dict(zip(previous.psi_terms,previous.psi_coeff));tc=dict(zip(previous.theta_terms,previous.theta_coeff))
        z0=np.r_[[pc.get(ps[i],0.) for i in m.freep],[tc.get(ts[i],0.) for i in m.freet]]
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    history=[]
    cache={'beta':args.beta,'matrices':m}
    def at_beta(beta):
        if beta!=cache['beta']:
            cache['beta']=beta;cache['matrices']=Matrices(beta,ps,ts,pts)
        return cache['matrices']
    def fun(z):
        beta=z[-1] if args.free_beta else args.beta
        mm=at_beta(beta)
        values=mm.evaluate(z[:-1] if args.free_beta else z)
        history.append({'evaluation':len(history),'elapsed_seconds':time.monotonic()-start,
                        'beta':float(beta),'cost':float(np.dot(values,values)/2),
                        'max_weighted':float(np.max(np.abs(values))),'parameter_norm':float(np.linalg.norm(z))})
        if len(history)%40==1:
            partial={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'parameters':z.tolist(),'latest':history[-1],'status':'RUNNING'}
            temporary=out/'progress.tmp'
            temporary.write_text(json.dumps(partial,indent=2)+'\n')
            temporary.replace(out/'progress.json')
        return values
    def jac(z):
        if not args.free_beta:return at_beta(args.beta).evaluate(z,True)
        beta=z[-1];zz=z[:-1]
        main=at_beta(beta).evaluate(zz,True)
        h=2e-5*max(1.,abs(beta))
        plus=Matrices(beta+h,ps,ts,pts).evaluate(zz)
        minus=Matrices(beta-h,ps,ts,pts).evaluate(zz)
        return np.column_stack((main,(plus-minus)/(2*h)))
    if args.free_beta:
        z0=np.r_[z0,args.beta]
        lower=np.r_[np.full(len(z0)-1,-np.inf),2+1e-6]
        upper=np.r_[np.full(len(z0)-1,np.inf),args.beta_max]
    else:
        lower,upper=-np.inf,np.inf
    result=least_squares(fun,z0,jac=jac,max_nfev=args.max_nfev,bounds=(lower,upper),
                         ftol=2e-11,xtol=2e-11,gtol=2e-11,x_scale='jac',verbose=1)
    beta=float(result.x[-1]) if args.free_beta else args.beta
    z=result.x[:-1] if args.free_beta else result.x
    m=at_beta(beta)
    p,t=m.unpack(z)
    profile=RationalProfile(beta,ps,ts,p,t)
    a,c,b=m.center_rows
    testpoints=collocation(args.radius*1.2,args.nrad+3,args.nangle+2,args.seed+987)
    vm=Matrices(beta,ps,ts,testpoints)
    vr=vm.evaluate(z)
    sv=np.linalg.svd(result.jac,compute_uv=False)
    summary={'started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds':time.monotonic()-start,'pid':os.getpid(),'arguments':vars(args),'beta':beta,
        'parameters':len(result.x),'fit_points':len(pts),'nfev':result.nfev,'njev':result.njev,
        'cost':float(result.cost),'optimality':float(result.optimality),'status':int(result.status),
        'message':result.message,'fit_max_weighted':float(np.max(np.abs(result.fun))),
        'between_points_max_weighted':float(np.max(np.abs(vr))),
        'center':{'a0':float(a@t),'c':float(c@p),'b0':float(b@p),'stream_v0':profile.v0},
        'jacobian_singular_values':sv.tolist(),'coefficient_norm':float(np.linalg.norm(np.r_[p,t])),
        'verdict':'OPEN; exploratory fit only; no independent validation yet'}
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    (out/'candidate.json').write_text(json.dumps(profile.to_dict(),indent=2)+'\n')
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    np.savez_compressed(out/'restart.npz',parameters=result.x,points=pts)
    (out/'history.json').write_text(json.dumps(history,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='jacobian_singular_values'},indent=2),flush=True)

if __name__=='__main__':main()
