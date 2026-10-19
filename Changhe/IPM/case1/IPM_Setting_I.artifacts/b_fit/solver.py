"""Positive log-amplitude dynamic rescaling for the specified canonical IPM law.

Only numpy/scipy, CPU, single thread. No servers, subprocesses or GPU.
Run with timeout 540 and a memory limit; all outputs are relative to cwd.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"
import argparse
import json
import time
from pathlib import Path
import numpy as np
from scipy.signal import lfilter
from scipy.fft import dst,dct
from scipy.integrate import simpson
from scipy.interpolate import RectBivariateSpline, CubicSpline
from scipy.optimize import brentq


def derivative(a, h, axis):
    """Fourth order centered in the interior, second order at the two ends."""
    z = np.moveaxis(a, axis, 0)
    d = np.gradient(z, h, axis=0, edge_order=2)
    d[2:-2] = (z[:-4] - 8*z[1:-3] + 8*z[3:-1] - z[4:])/(12*h)
    return np.moveaxis(d, 0, axis)


def upwind(a, speed, h, axis, angular=False):
    z = np.moveaxis(a, axis, 0)
    if angular:
        e = np.concatenate((z[2:0:-1], z, z[-2:-4:-1]), axis=0)
    else:
        # At the origin log a = O(r²); at outer outflow extrapolate.
        e = np.concatenate((z[:1]*np.exp(-4*h), z[:1]*np.exp(-2*h),
                            z, 2*z[-1:]-z[-2:-1], 3*z[-1:]-2*z[-2:-1]), axis=0)
    plus = (e[:-4]-6*e[1:-3]+3*e[2:-2]+2*e[3:-1])/(6*h)
    minus = (-2*e[1:-3]-3*e[2:-2]+6*e[3:-1]-e[4:])/(6*h)
    plus, minus = np.moveaxis(plus, 0, axis), np.moveaxis(minus, 0, axis)
    return np.where(speed >= 0, plus, minus)


class Problem:
    def __init__(self, nr=192, nt=48, R=1000., rmin=1e-4, d=1.5, tailk=.5,
                 quadrature_order=2):
        self.nr, self.nt, self.R, self.rmin, self.d = nr, nt, R, rmin, d
        self.tailk = tailk
        self.quadrature_order=quadrature_order
        self.tail_terms=1
        self.t = np.linspace(np.log(rmin), np.log(R), nr)
        self.r = np.exp(self.t)
        self.theta = np.linspace(0, np.pi/2, nt+1)
        self.dt, self.dtheta = self.t[1]-self.t[0], self.theta[1]
        self.rr = self.r[:, None]
        self.ct, self.st = np.cos(self.theta), np.sin(self.theta)
        self.ct[-1] = 0
        self.st[0] = 0
        self.factor = self.rr**3 * (self.ct**2*self.st)
        self.m = 2*np.arange(1, nt)
        self.sin = np.sin(self.m[:, None]*self.theta)
        self.cos = np.cos(self.m[:, None]*self.theta)
        self.sin[:, [0, -1]] = 0
        self.project = self.sin.T * (2/nt)
        self.sodd = np.sin(np.arange(1, 2*nt, 2)[:, None]*self.theta)
        self.weights = np.ones(nt+1)*(2/nt)
        self.weights[[0,-1]] *= .5
        self.tan_sin = self.sin.copy()
        self.cot_sin = self.sin.copy()
        self.tan_sin[:, :-1] *= (self.st[:-1]/self.ct[:-1])
        self.tan_sin[:, -1] = -self.m*self.cos[:, -1]
        self.cot_sin[:, 1:] *= (self.ct[1:]/self.st[1:])
        self.cot_sin[:, 0] = self.m
        self.quad = []
        self.quad4=[]
        for rate in (self.m+2, self.m-2):
            e = np.exp(-rate*self.dt)
            w0 = np.empty(len(rate), float)
            w1 = np.empty(len(rate), float)
            nz = rate != 0
            w0[nz] = 1/rate[nz] - (1-e[nz])/(rate[nz]**2*self.dt)
            w1[nz] = (1-e[nz])/rate[nz]-w0[nz]
            w0[~nz] = w1[~nz] = self.dt/2
            self.quad.append((e,w0,w1))
            nodes,weights=np.polynomial.legendre.leggauss(12)
            nodes=(nodes+1)/2;weights=weights/2
            lagrange=[]
            for a in (-1,0,1,2):
                poly=np.ones_like(nodes)
                for b in (-1,0,1,2):
                    if a!=b:poly*=((nodes-b)/(a-b))
                lagrange.append(poly)
            w=(self.dt*np.exp(-rate[:,None]*self.dt*(1-nodes))*
               weights)@np.array(lagrange).T
            self.quad4.append((e,w))

    def modal_integrals(self,f,ftail,k,tail_B=None):
        """f has radial first, modes last, with optional batch dimensions."""
        # Each recurrence traverses radius for one mode. Keeping modes last
        # during that traversal gives a large cache stride for batched
        # Jacobians; move them to separate contiguous slabs.
        fm=np.ascontiguousarray(np.moveaxis(f,-1,0))
        A=np.empty_like(fm);B=np.empty_like(fm)
        for j,m in enumerate(self.m):
            for side,out in enumerate((A,B)):
                vals=fm[j] if side==0 else fm[j,::-1]
                initial=(fm[j,0]/(m+4) if side==0 else
                         (ftail[...,j]/(m-1-k) if tail_B is None else tail_B[...,j]))
                if self.quadrature_order==2:
                    e,w0,w1=(v[j] for v in self.quad[side])
                    zi=np.expand_dims(initial-w0*vals[0],axis=0)
                    ans=lfilter([w0,w1],[1,-e],vals,axis=0,zi=zi)[0]
                else:
                    e,weights=self.quad4[side];e=e[j];w=weights[j]
                    # Cubic extrapolation is only used for quadrature stencils
                    # inside the disk; the exterior integral stays analytic.
                    low=4*vals[:1]-6*vals[1:2]+4*vals[2:3]-vals[3:4]
                    high=4*vals[-1:]-6*vals[-2:-1]+4*vals[-3:-2]-vals[-4:-3]
                    ext=np.concatenate((low,vals,high),axis=0)
                    drive=np.empty_like(vals)
                    drive[0]=initial
                    drive[1:]=(w[0]*ext[:-3]+w[1]*ext[1:-2]+
                               w[2]*ext[2:-1]+w[3]*ext[3:])
                    ans=lfilter([1],[1,-e],drive,axis=0)
                out[j]=ans if side==0 else ans[::-1]
        return (np.ascontiguousarray(np.moveaxis(A,0,-1)),
                np.ascontiguousarray(np.moveaxis(B,0,-1)))

    def project_sine(self,values):
        return dst(values[...,1:-1],type=1,axis=-1)/self.nt

    def sine_series(self,coefficients):
        out=np.zeros((*coefficients.shape[:-1],self.nt+1))
        out[...,1:-1]=dst(coefficients,type=1,axis=-1)/2
        return out

    def cosine_series(self,coefficients):
        padded=np.zeros((*coefficients.shape[:-1],self.nt+1))
        padded[...,1:-1]=coefficients/2
        return dct(padded,type=1,axis=-1)

    def cosine_series_transpose(self,values):
        padded=values.copy()
        padded[...,1:-1]*=.5
        return dct(padded,type=1,axis=-1)[...,1:-1]

    def modal_integrals_transpose(self,Abar,Bbar):
        """Adjoint with respect to sampled f and explicit outer B values."""
        fbar=np.zeros_like(Abar)
        boundarybar=np.zeros(Abar.shape[-1])
        for j,m in enumerate(self.m):
            for side,gradient in enumerate((Abar[:,j],Bbar[::-1,j])):
                if self.quadrature_order==4:
                    e,weights=self.quad4[side];e=e[j];w=weights[j]
                else:
                    e,w0,w1=(v[j] for v in self.quad[side])
                drivebar=lfilter([1],[1,-e],gradient[::-1])[::-1]
                if self.quadrature_order==4:
                    extbar=np.zeros(self.nr+2)
                    for offset in range(4):
                        extbar[offset:offset+self.nr-1]+=w[offset]*drivebar[1:]
                    valsbar=extbar[1:-1].copy()
                    valsbar[:4]+=extbar[0]*np.array([4.,-6.,4.,-1.])
                    valsbar[-4:]+=extbar[-1]*np.array([-1.,4.,-6.,4.])
                else:
                    valsbar=np.zeros(self.nr)
                    valsbar[1:]+=w0*drivebar[1:]
                    valsbar[:-1]+=w1*drivebar[1:]
                if side==0:
                    valsbar[0]+=drivebar[0]/(m+4)
                    fbar[:,j]+=valsbar
                else:
                    boundarybar[j]+=drivebar[0]
                    fbar[:,j]+=valsbar[::-1]
        return fbar,boundarybar

    def initial(self, k=.5, L=None):
        if L is None:
            L = np.sqrt(4*(2.5*self.d)*(1-k))
        return np.broadcast_to((k-3)/2*np.log1p(self.rr**2/L**2),
                               (self.nr,self.nt+1)).copy()

    def fields(self, H, tailk=None, ht=None, ha=None):
        if tailk is None:
            tailk = self.tailk
        rho = self.factor*np.exp(H)
        ht = derivative(H,self.dt,0) if ht is None else ht
        ha = derivative(H,self.dtheta,1) if ha is None else ha
        ha[:,[0,-1]] = 0
        # Differentiate the factor analytically, avoiding division on axes.
        angular = self.ct**2*self.st
        angularprime = self.ct**3-2*self.ct*self.st**2
        rt = (3+ht)*rho
        ra = self.rr**3*np.exp(H)*(angularprime+angular*ha)
        fx = (rt*self.ct-ra*self.st)/self.rr
        f = fx @ self.project
        ftail = (((tailk*rho[-1])*self.ct-ra[-1]*self.st)/self.R) @ self.project
        tail_B=None
        rho_modes=rho[-1]@(self.weights[:,None]*self.sodd.T)
        tail_powers=np.array([tailk])
        tail_modes=rho_modes[None,:]
        if self.tail_terms==2:
            rho_modes_t=rt[-1]@(self.weights[:,None]*self.sodd.T)
            second=(rho_modes_t-tailk*rho_modes)/(tailk-1)
            tail_powers=np.array([tailk,2*tailk-1])
            tail_modes=np.array([rho_modes-second,second])
            tail_B=np.zeros_like(ftail)
            for exponent,modes in zip(tail_powers,tail_modes):
                ft=((exponent-self.m+1)*modes[:-1]+
                    (exponent+self.m+1)*modes[1:])/(2*self.R)
                tail_B+=ft/(self.m-1-exponent)
        A,B=self.modal_integrals(f,ftail,tailk,tail_B)
        q = (A+B)/(2*self.m)
        v = (B-A)/2
        ur = -(q*self.m) @ self.cos
        ua = v @ self.sin
        ux = ur-v @ self.tan_sin
        uy = ur+v @ self.cot_sin
        c = (B[0,0]+f[0,0]/2)/2
        rho3 = rho @ (self.weights*np.sin(3*self.theta))
        c2 = simpson(rho3/self.r,x=self.t)+rho3[0]/(2*self.r[0])
        c2 += sum(modes[1]/(self.R*(1-exponent))
                  for exponent,modes in zip(tail_powers,tail_modes))
        return dict(rho=rho,ht=ht,ha=ha,rt=rt,ra=ra,fx=fx,f=f,
                    q=q,v=v,ur=ur,ua=ua,ux=ux,uy=uy,c=float(c),c2=float(c2),
                    tailk=tailk,tail_powers=tail_powers,tail_modes=tail_modes)

    def rhs(self,H,fields=False):
        f = self.fields(H)
        vr, va = self.d+f["ur"], f["ua"]
        source = -f["c"]-2*f["ux"]-f["uy"]
        rhs = source-vr*upwind(H,vr,self.dt,0)-va*upwind(H,va,self.dtheta,1,True)
        # Leading cubic normalization: analytic limiting evolution is zero.
        # The first grid ring is a small-radius approximation, not a forced
        # zero-density state.
        rhs[0] = 0
        cfl = .35/np.max(np.abs(vr)/self.dt+np.abs(va)/self.dtheta)
        return (rhs,f,cfl) if fields else rhs

    def basic(self,H,tau=0):
        f=self.fields(H)
        c=f["c"]; a=3*self.d-c
        R=(self.d+f["ur"])*f["rt"]+f["ua"]*f["ra"]-a*f["rho"]
        den=np.abs(a*f["rho"])+np.abs(self.d*f["rt"])+np.abs(f["ur"]*f["rt"]+f["ua"]*f["ra"])
        out=dict(tau=float(tau),c=c,crho=a,cl=self.d/a if a !=0 else None,
                 c2=f["c2"],rhomax=float(np.max(f["rho"])),
                 Hmin=float(H.min()),Hmax=float(H.max()),
                 residual=float(np.max(np.abs(R))/max(np.max(den),1e-300)),
                 rhsmax=float(np.max(np.abs(self.rhs(H)))))
        return out

    def save(self,path,H,tau,history):
        f=self.fields(H); a=3*self.d-f["c"]
        data=dict(H=H,r=self.r,theta=self.theta,rho=f["rho"],d=self.d,
                  c_dynamic=f["c"],crho=a,c_l=self.d/a,
                  tau=tau,R=self.R,rmin=self.rmin,tailk=self.tailk,
                  history=np.array([json.dumps(h) for h in history]))
        if a>0:
            L=a**-.5
            data.update(r_physical=L*self.r,rho_physical=L/a*f["rho"],
                        c_physical=f["c"]/a)
        np.savez_compressed(path,**data)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nr",type=int,default=192)
    ap.add_argument("--nt",type=int,default=32)
    ap.add_argument("--R",type=float,default=1000)
    ap.add_argument("--rmin",type=float,default=1e-4)
    ap.add_argument("--d",type=float,default=1.5)
    ap.add_argument("--tailk",type=float,default=.5)
    ap.add_argument("--until",type=float,default=10)
    ap.add_argument("--seconds",type=float,default=460)
    ap.add_argument("--load")
    ap.add_argument("--output",default="candidate.npz")
    ap.add_argument("--initial-L",type=float)
    args=ap.parse_args()
    p=Problem(args.nr,args.nt,args.R,args.rmin,args.d,args.tailk)
    tau=0.;history=[]
    if args.load:
        z=np.load(args.load)
        H=RectBivariateSpline(np.log(z["r"]),z["theta"],z["H"])(p.t,p.theta)
        # If the new grid extends outward, linearly continue log a.
        outside=p.r>z["r"][-1]
        if outside.any():
            H[outside]=H[~outside][-1]+(p.t[outside,None]-p.t[~outside][-1])*(p.tailk-3)
        tau=float(z["tau"])
        history=[json.loads(s) for s in z["history"]]
    else:
        H=p.initial(args.tailk,args.initial_L)
    start=time.monotonic();n=0;nextreport=tau
    while tau<args.until and time.monotonic()-start<args.seconds:
        rhs,f,dt=p.rhs(H,True)
        if tau>=nextreport:
            info=p.basic(H,tau);history.append(info)
            print(json.dumps(info),flush=True)
            p.save(args.output,H,tau,history)
            nextreport=tau+.25
        if not np.all(np.isfinite(rhs)) or np.max(np.abs(H))>300 or abs(f["c"])>100:
            print("STOP: divergence guard",flush=True);break
        dt=min(dt,args.until-tau,.02)
        H1=H+dt*rhs
        H2=.75*H+.25*(H1+dt*p.rhs(H1))
        Hnew=H/3+2/3*(H2+dt*p.rhs(H2))
        if not np.all(np.isfinite(Hnew)):
            print("STOP: nonfinite RK stage; retaining preceding checkpoint",flush=True);break
        H=Hnew;tau+=dt;n+=1
    info=p.basic(H,tau);history.append(info);p.save(args.output,H,tau,history)
    print(json.dumps(info),flush=True)
    print("steps",n,"wall_seconds",time.monotonic()-start,flush=True)

if __name__=="__main__":
    main()
