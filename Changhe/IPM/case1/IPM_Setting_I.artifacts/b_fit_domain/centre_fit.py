"""Centre-weighted continuation; no additional axis-equation rows."""
import json
import time
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from scipy.sparse.linalg import LinearOperator
from stationary import Shape, krylov_solve
from linearized import StationaryDerivative


def default_knots(degree, order):
    return np.r_[np.zeros(order+1),
                 np.linspace(0,1,degree-order+2)[1:-1]**1.3,
                 np.ones(order+1)]


class CentreShape(Shape):
    def configure(self, saved, angular=None, insert=()):
        self.radial_basis = "spline"
        self.spline_order = int(saved["spline_order"])
        self.origin_radius = float(saved["origin_radius"])
        self.spline_knots = np.array(saved["spline_knots"] if "spline_knots" in saved
                                   else default_knots(int(saved["degree"]), self.spline_order))
        old_degree, old_angular = int(saved["degree"]), int(saved["angular"])
        co = saved["z"][1:1+(old_angular+1)*old_degree].reshape(old_angular+1,old_degree)
        spl = BSpline(self.spline_knots,np.vstack([np.zeros(old_angular+1),co.T]),
                      self.spline_order)
        for q in insert:
            spl = spl.insert_knot(float(q))
        self.spline_knots = spl.t
        self.degree = spl.c.shape[0]-1
        self.angular = old_angular if angular is None else angular
        co = np.zeros((self.angular+1,self.degree))
        co[:old_angular+1] = spl.c[1:].T
        z = np.r_[saved["z"][0],co.ravel(),saved["z"][-self.singular:]]
        self.p.tail_terms = 2
        self.build_basis(z[0])
        self.source_weight = 20.
        self.objective = "log"
        self.fit_radius = getattr(self, "fit_radius", .9*self.p.R)
        self.rows = (self.p.r>=1e-4*(1-1e-12)) & (self.p.r<self.fit_radius)
        self.cols = np.arange(0,self.p.nt+1,2)
        if self.cols[-1] != self.p.nt:
            self.cols=np.r_[self.cols,self.p.nt]
        self.weight = np.ones((np.sum(self.rows),len(self.cols)))
        self.weight *= np.sqrt(14000/self.weight.size)
        self.weight *= np.maximum(1.,(.04/self.p.r[self.rows])**2)[:,None]
        self.d14_weight = 1.
        self.recycle_step=np.zeros_like(z)
        if not len(insert) and angular is None and "recycle_step" in saved:
            if saved["recycle_step"].shape==z.shape:
                self.recycle_step=saved["recycle_step"].copy()
        return z

    def centre(self,z,f=None,L2=None):
        if f is None:
            _,f,L2,_,_=self.evaluate(z)
        k=z[0];cl=1/k;A=2*cl-1
        deriv=BSpline(self.spline_knots,np.eye(self.degree+1),self.spline_order)(0.,nu=1)[1:]
        co=z[1:1+(self.angular+1)*self.degree].reshape(self.angular+1,self.degree)
        ds=(k-3)/2+(1-k)/2*np.dot(deriv,co[0]+co[1])
        gs=(k-3)/2+(1-k)/2*np.dot(deriv,co[0]-co[1])
        # B4=4*q4+v4; its value/rmin² is the exterior integral.
        r0=self.p.r[0]
        moment=(4*f["q"][0,1]+f["v"][0,1])/r0**2+(ds/4-gs/8)*r0**2
        alpha=(-1/3-moment)/2;beta=(-1/3+moment)/2
        delta=ds/L2;gamma=gs/L2
        E=beta-2*A*delta;D2=(4*A+2)*gamma-5*alpha
        return dict(alpha=alpha,beta=beta,delta=delta,gamma=gamma,E=E,D2=D2,
                    E_relative=E/(abs(beta)+2*A*abs(delta)),
                    D2_relative=D2/((4*A+2)*abs(gamma)+5*abs(alpha)),
                    moment=moment,delta_shape=ds,gamma_shape=gs,L2=L2,
                    c_l=cl,A=A)

    def raw_fun(self,z):
        _,f,L2,res,den=self.evaluate(z)
        den=self.objective_den(f,den)
        values=(res[self.rows][:,self.cols]/den[self.rows][:,self.cols])*self.weight
        source=self.source(f,L2,1/z[0])
        cen=self.centre(z,f,L2)
        result=np.r_[values.ravel(),self.source_weight*(source[1]-1),
                     self.d14_weight*np.array([cen["E"],cen["D2"]])]
        return result,cen,source

    def fun(self,z):
        if time.monotonic()-self.start>self.seconds:
            raise TimeoutError("centre chunk time budget reached")
        result,cen,source=self.raw_fun(z)
        self.calls+=1
        norm=float(np.linalg.norm(result))
        if norm<self.best*(1-1e-7):
            if self.best_z is not None:
                self.recycle_step=z-self.best_z
            self.best=norm;self.best_z=z.copy()
            info=dict(call=self.calls,seconds=time.monotonic()-self.start,
                      norm=norm,cl=1/z[0],L=float(np.sqrt(cen["L2"])),
                      E=float(cen["E"]),D2=float(cen["D2"]),hP=source[1],
                      xstar=float(np.sqrt(cen["L2"])*np.exp(source[0])))
            self.history.append(info)
            if getattr(self,"output",None):self.save(self.output,z)
            print(json.dumps(info),flush=True)
        return result

    def save(self,path,z):
        _,f,L2,_,_=self.evaluate(z)
        tmp=str(path)+".partial.npz"
        np.savez_compressed(tmp,z=z,names=np.array(self.names),degree=self.degree,
                            angular=self.angular,singular=self.singular,
                            angular_cap=0,radial_basis="spline",spline_order=self.spline_order,
                            spline_knots=self.spline_knots,origin_radius=self.origin_radius,
                            compact="matched",tail_terms=2,k=z[0],L=np.sqrt(L2),
                            c_l=1/z[0],c=3/z[0]-1,R_shape=self.p.R,
                            history=np.array([json.dumps(v) for v in self.history]),
                            recycle_step=self.recycle_step,
                            run_configuration=json.dumps(getattr(self,"run_configuration",{})))
        Path(tmp).replace(path)


def functional_gradient(s,z,f,dfbar,boundarybar):
    """Transpose forcing samples and the two-term tail into H coefficients."""
    p=s.p;k=z[0]
    fxbar=(2/p.nt)*p.sine_series(dfbar)
    rtbar=fxbar*p.ct/p.rr
    rabar=-fxbar*p.st/p.rr
    rhobar=np.zeros_like(f["rho"])
    partbars=[]
    for exponent in (k,2*k-1):
        bar=np.zeros(p.nt)
        valuebar=boundarybar/(2*p.R*(p.m-1-exponent))
        bar[:-1]+=(exponent-p.m+1)*valuebar
        bar[1:]+=(exponent+p.m+1)*valuebar
        partbars.append(bar)
    secondbar=partbars[1]-partbars[0]
    modesbar=partbars[0]-k*secondbar/(k-1)
    modestbar=secondbar/(k-1)
    proj=p.weights[:,None]*p.sodd.T
    rhobar[-1]+=modesbar@proj.T
    rtbar[-1]+=modestbar@proj.T
    return s.transpose_basis(f["rho"]*rhobar+f["rt"]*rtbar+f["ra"]*rabar,
                             f["rho"]*rtbar,f["rho"]*rabar)


class CentreDerivative(LinearOperator):
    def __init__(self,s,z):
        self.base=StationaryDerivative(s,z)
        self.s=s
        f=self.base.f;L2=self.base.L2
        p=s.p;cen=s.centre(z,f,L2);A=cen["A"];k=z[0]
        zero=np.zeros_like(f["q"])
        bb=np.zeros_like(zero);bb[0,0]=.5
        dfbar,tailbar=p.modal_integrals_transpose(zero,bb)
        dfbar[0,0]+=.25
        gc=functional_gradient(s,z,f,dfbar,tailbar)
        bb[:]=0.;bb[0,1]=1/p.r[0]**2
        dfbar,tailbar=p.modal_integrals_transpose(zero,bb)
        gm=functional_gradient(s,z,f,dfbar,tailbar)
        deriv=BSpline(s.spline_knots,np.eye(s.degree+1),s.spline_order)(0.,nu=1)[1:]
        gd=np.zeros(len(z)-1);gg=np.zeros_like(gd)
        gd[:s.degree]=(1-k)/2*deriv;gd[s.degree:2*s.degree]=(1-k)/2*deriv
        gg[:s.degree]=(1-k)/2*deriv;gg[s.degree:2*s.degree]=-(1-k)/2*deriv
        gm+=(gd/4-gg/8)*p.r[0]**2
        gd=gd/L2+cen["delta"]*gc/f["c"]
        gg=gg/L2+cen["gamma"]*gc/f["c"]
        J=np.empty((2,len(z)))
        J[0,1:]=gm/2-2*A*gd
        J[1,1:]=(4*A+2)*gg+2.5*gm
        eps=2e-6
        zp=z.copy();zm=z.copy();zp[0]+=eps;zm[0]-=eps
        cp=s.centre(zp);cm=s.centre(zm)
        J[:,0]=[(cp[name]-cm[name])/(2*eps) for name in ("E","D2")]
        s.build_basis(k)
        self.J=s.d14_weight*J
        super().__init__(dtype=np.dtype(float),shape=(self.base.shape[0]+2,len(z)))

    def _matvec(self,v):
        return np.r_[self.base@v,self.J@v]

    def _rmatvec(self,v):
        return self.base.rmatvec(v[:-2])+self.J.T@v[-2:]


def load_shape(path,nr=2048,nt=480,R=1000.,angular=None,insert=(),fit_radius=None):
    # fit_radius (shape units, as in astra construct5): fit rows r < fit_radius and inverse domain R = fit_radius/0.9
    old=np.load(path)
    if fit_radius is not None:
        R=fit_radius/.9
    s=CentreShape(nr,nt,R,int(old["degree"]),int(old["angular"]),
                  "matched",int(old["singular"]),rmin=1e-4)
    if fit_radius is not None:
        s.fit_radius=fit_radius
    z=s.configure(old,angular,insert)
    return s,z


def main():
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("input");ap.add_argument("output")
    ap.add_argument("--nr",type=int,default=2048);ap.add_argument("--nt",type=int,default=480)
    ap.add_argument("--angular",type=int);ap.add_argument("--insert",default="")
    ap.add_argument("--seconds",type=float,default=480)
    ap.add_argument("--iterations",type=int,default=250)
    ap.add_argument("--nfev",type=int,default=2)
    ap.add_argument("--prepare",action="store_true")
    ap.add_argument("--recycle",action="store_true",
                    help="Use the previous accepted coefficient step as the LSMR initial guess.")
    ap.add_argument("--pweight",type=float,default=1.,
                    help="Lead addition: extra weight 1+(pweight-1)exp(-(d/pwidth)^2), d = physical distance to P.")
    ap.add_argument("--pwidth",type=float,default=3.)
    ap.add_argument("--pcentre",type=float,default=8.60088)
    args=ap.parse_args()
    insert=list(map(float,args.insert.split(","))) if args.insert else []
    s,z=load_shape(args.input,args.nr,args.nt,angular=args.angular,insert=insert)
    if args.pweight!=1.:
        Ls=float(np.load(args.input)["L"])
        rr=s.p.r[s.rows][:,None];tt=s.p.theta[s.cols][None,:]
        dist=np.hypot(rr*np.cos(tt)-args.pcentre/Ls,rr*np.sin(tt))*Ls
        s.weight=s.weight*(1+(args.pweight-1)*np.exp(-(dist/args.pwidth)**2))
    s.output=args.output;s.run_configuration=vars(args);s.seconds=args.seconds
    s.start=time.monotonic()
    if args.prepare:
        s.save(args.output,z);return
    initial=s.fun(z)
    result=None
    try:
        result=krylov_solve(s.fun,lambda zz:CentreDerivative(s,zz),z,
                            (np.r_[.05,np.full(len(z)-1,-30.)],
                             np.r_[.98,np.full(len(z)-1,30.)]),
                            max_nfev=args.nfev,damping=1e-8,maxiter=args.iterations,
                            initial_step=s.recycle_step.copy() if args.recycle else None,
                            deadline=s.start+args.seconds)
        s.save(args.output,result.x)
        message=str(result.message)
    except TimeoutError as e:
        if s.best_z is not None:s.save(args.output,s.best_z)
        message=str(e)
    info=dict(input=args.input,output=args.output,configuration=vars(args),
              history=s.history,message=message,
              initial_norm=float(np.linalg.norm(initial)),final_norm=float(s.best),
              change=float(1-s.best/np.linalg.norm(initial)),
              nfev=s.calls,elapsed=time.monotonic()-s.start,
              optimality=float(result.optimality) if result is not None else None)
    Path(args.output+".run.json").write_text(json.dumps(info,indent=2))
    print(json.dumps(info),flush=True)


if __name__=="__main__":
    main()
