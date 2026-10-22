"""Independent Cartesian rational-basis profile search, not an existence proof.

D=1+x^2+y^2, q_s=x^2/D, q_t=y^2/D.
H=D^(-1/(2 beta))*sum h_ij q_s^i q_t^j, Psi=xy H.
F=D^(-1/beta)*sum f_ij q_s^i q_t^j, Theta=y F.
Omega=-Delta Psi, with analytic basis differentiation only in this fitting code.
All fields are smooth on the actual plane, and U=o(r) for every finite beta>0.
The canonical inverse equals this U by sublinear uniqueness, to be independently
checked numerically with plane_quadrature and independent_residuals.

Only spatial scale is fixed: F_s(0)=b1, b1=+1 or -1. H(0)=-2 is the required
physical center relation. a0=F(0) and beta remain unknown (unless beta is fixed).
The rational family restricts far-field corrections; failed fits prove no exclusion.
"""
import argparse,datetime,json,math,time,os
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

DERIVS=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def indices(n):return [(i,k-i) for k in range(n+1) for i in range(k,-1,-1)]
def falling(n,k):return math.prod(range(n-k+1,n+1)) if k else 1

def basis(s,t,p,ij,orders=DERIVS,family="monomial",degree=None):
    s=np.asarray(s);t=np.asarray(t);D=1+s+t;qs=s/D;qt=t/D
    out={}
    if degree is None:degree=max(i+j for i,j in ij)
    for a,b in orders:
        arr=np.zeros((len(s),len(ij)))
        for k,(i,j) in enumerate(ij):
            extra=degree-i-j if family=="bernstein" else 0
            m=p+i+j+extra
            factor=math.factorial(degree)/(math.factorial(i)*math.factorial(j)*math.factorial(extra)) if family=="bernstein" else 1
            val=np.zeros(len(s))
            for u in range(min(a,i)+1):
                for v in range(min(b,j)+1):
                    ell=a+b-u-v
                    coeff=math.comb(a,u)*math.comb(b,v)*falling(i,u)*falling(j,v)
                    coeff*=(-1)**ell*math.prod(m+z for z in range(ell))
                    val+=coeff*qs**(i-u)*qt**(j-v)
            arr[:,k]=factor*D**(-p-extra-a-b)*val
        out[a,b]=arr
    return out


def elevate_bernstein(coefficients, old_degree, new_degree):
    """Exact polynomial degree elevation on q_s+q_t+q_0=1."""
    if new_degree < old_degree: raise ValueError('degree reduction is not exact')
    old=indices(old_degree); new=indices(new_degree)
    denominator=math.comb(new_degree,old_degree)
    answer=[]
    for i,j in new:
        k=new_degree-i-j; value=0.
        for coefficient,(a,b) in zip(coefficients,old):
            c=old_degree-a-b
            if a<=i and b<=j and c<=k:
                value+=coefficient*math.comb(i,a)*math.comb(j,b)*math.comb(k,c)/denominator
        answer.append(value)
    return np.array(answer)


def cartesian_grid(n,R):
    axis=np.r_[0.,np.geomspace(.015,R,n-1)]
    x,y=np.meshgrid(axis,axis,indexing='ij')
    return np.stack([x.ravel(),y.ravel()],axis=1)


class Problem:
    def __init__(self,degree,n,R,beta,b1,a0,free_beta,seed=0,family="monomial"):
        self.ij=indices(degree);self.K=len(self.ij);self.degree=degree;self.family=family
        self.points=cartesian_grid(n,R);self.s=self.points[:,0]**2;self.t=self.points[:,1]**2
        self.D=1+self.s+self.t;self.n=n;self.R=R;self.beta=beta;self.b1=b1
        self.a0_initial=a0;self.free_beta=free_beta;self.seed=seed
        self.hmask=np.arange(1,self.K);self.f10=self.ij.index((1,0));self.fmask=np.array([k for k in range(self.K) if k!=self.f10])
        self.npar=2*(self.K-1)+int(free_beta);self.calls=0;self.jcalls=0;self.best=float('inf');self.history=[]
        self.t0=time.monotonic();self.directory=None;self.cached=None

    def transforms(self,b):
        K=self.K;p=1/(2*b);q=1/b
        hc=np.zeros(K);hc[0]=-2;HT=np.eye(K)[:,self.hmask]
        fc=np.zeros(K);FT=np.eye(K)[:,self.fmask]
        if self.family=="bernstein":
            fc[self.f10]=self.b1/self.degree
            FT[self.f10,np.where(self.fmask==0)[0][0]]=(q+self.degree)/self.degree
        else:
            fc[self.f10]=self.b1
            FT[self.f10,np.where(self.fmask==0)[0][0]]=q
        return hc,HT,fc,FT

    def initial(self):
        b=self.beta;p=1/(2*b);q=1/b;a0=self.a0_initial
        hc,HT,fc,FT=self.transforms(b)
        h=hc.copy();f=fc.copy();f[0]=a0
        d1=-(2*b+4)*self.b1/(3*a0)
        d2=-self.b1/(3*(2*b+1))-d1
        b2=-a0*d2/(2*(b-2)) if abs(b-2)>1e-6 else 0.
        h[self.ij.index((1,0))]=d1-2*p
        h[self.ij.index((0,1))]=d2-2*p
        f[self.f10]=self.b1+q*a0
        f[self.ij.index((0,1))]=b2+q*a0
        if self.family=="bernstein":
            h0,hx,hy=h[0],h[self.ij.index((1,0))],h[self.ij.index((0,1))]
            f0,fx,fy=f[0],f[self.ij.index((1,0))],f[self.ij.index((0,1))]
            h=np.array([h0+hx*i/self.degree+hy*j/self.degree for i,j in self.ij])
            f=np.array([f0+fx*i/self.degree+fy*j/self.degree for i,j in self.ij])
        rng=np.random.default_rng(self.seed)
        if self.seed:
            for k,(i,j) in enumerate(self.ij):
                if i+j>=2:
                    h[k]+=rng.normal(0,.05);f[k]+=rng.normal(0,.05*max(1,abs(a0)))
        z=np.r_[h[self.hmask],f[self.fmask]]
        if self.free_beta:z=np.r_[z,b]
        return z

    def coefficients(self,z):
        b=float(z[-1]) if self.free_beta else self.beta
        hc,HT,fc,FT=self.transforms(b);kh=self.K-1
        h=hc+HT@z[:kh];f=fc+FT@z[kh:2*kh]
        return b,h,f,HT,FT

    def prepare(self,b):
        if self.cached is not None and self.cached[0]==b:return self.cached[1:]
        s=self.s;t=self.t
        h=basis(s,t,1/(2*b),self.ij,family=self.family,degree=self.degree)
        f=basis(s,t,1/b,self.ij,orders=[(0,0),(1,0),(0,1)],family=self.family,degree=self.degree)
        g=-(4*s[:,None]*h[2,0]+6*h[1,0]+4*t[:,None]*h[0,2]+6*h[0,1])
        gs=-(4*s[:,None]*h[3,0]+10*h[2,0]+4*t[:,None]*h[1,2]+6*h[1,1])
        gt=-(4*s[:,None]*h[2,1]+6*h[1,1]+4*t[:,None]*h[0,3]+10*h[0,2])
        self.cached=(b,h,f,g,gs,gt)
        return self.cached[1:]

    def compute(self,z,jac=False):
        b,hcoef,fcoef,HT,FT=self.coefficients(z)
        hb,fb,gb,gsb,gtb=self.prepare(b);s=self.s;t=self.t
        H=hb[0,0]@hcoef;Hs=hb[1,0]@hcoef;Ht=hb[0,1]@hcoef
        F=fb[0,0]@fcoef;Fs=fb[1,0]@fcoef;Ft=fb[0,1]@fcoef
        G=gb@hcoef;Gs=gsb@hcoef;Gt=gtb@hcoef
        A=b-H-2*t*Ht;B=b+H+2*s*Hs
        dt=2*s*A*Fs+2*t*B*Ft+(B-b+2)*F
        do=2*s*A*Gs+2*t*B*Gt+(A+B+1)*G-2*Fs
        wt=self.D**(1/b)/(max(1,abs(self.a0_initial))*(b+2))
        wo=self.D**(1+1/(2*b))/(2*b+1)
        # Center is the first Cartesian point; these are independent necessary jets.
        a0=F[0];d1=Hs[0];d2=Ht[0];b2=Ft[0]
        jets=np.array([(2*b+4)*self.b1+3*a0*d1,2*(b-2)*b2+a0*d2,(2*b+1)*G[0]-2*self.b1])
        jw=np.array([1/(b+2),1/(b+2),1/(2*b+1)])
        res=np.r_[wt*dt,wo*do,jw*jets]
        if not jac:return res
        dH=hb[0,0]@HT;dHs=hb[1,0]@HT;dHt=hb[0,1]@HT
        dA=-dH-2*t[:,None]*dHt;dB=dH+2*s[:,None]*dHs
        dF=fb[0,0]@FT;dFs=fb[1,0]@FT;dFt=fb[0,1]@FT
        dG=gb@HT;dGs=gsb@HT;dGt=gtb@HT
        dtH=2*(s*Fs)[:,None]*dA+(2*t*Ft+F)[:,None]*dB
        dtF=2*(s*A)[:,None]*dFs+2*(t*B)[:,None]*dFt+(B-b+2)[:,None]*dF
        doH=2*s[:,None]*(dA*Gs[:,None]+A[:,None]*dGs)+2*t[:,None]*(dB*Gt[:,None]+B[:,None]*dGt)+(dA+dB)*G[:,None]+(A+B+1)[:,None]*dG
        doF=-2*dFs
        jetH=np.stack([3*a0*dHs[0],a0*dHt[0],(2*b+1)*dG[0]])
        jetF=np.stack([3*d1*dF[0],2*(b-2)*dFt[0]+d2*dF[0],np.zeros(self.K-1)])
        mat=np.vstack([wt[:,None]*np.hstack([dtH,dtF]),wo[:,None]*np.hstack([doH,doF]),jw[:,None]*np.hstack([jetH,jetF])])
        if self.free_beta:
            eps=1e-5*max(1,b);zp=z.copy();zm=z.copy();zp[-1]+=eps;zm[-1]-=eps
            db=(self.compute(zp)-self.compute(zm))/(2*eps)
            mat=np.column_stack([mat,db])
        return res,mat

    def objective(self,z):
        self.calls+=1;r=self.compute(z);cost=float(r@r/2)
        if cost<self.best:
            self.best=cost
            if self.directory is not None and (self.calls<=3 or self.calls%10==0):self.save_candidate(z,'best_candidate.json',cost)
        if self.calls<=3 or self.calls%20==0:
            b,h,f,*_=self.coefficients(z)
            row={'utc':utc(),'call':self.calls,'elapsed_s':time.monotonic()-self.t0,'cost':cost,'max_abs_weighted_residual':float(np.max(np.abs(r))),'beta':b,'a0':float(self.prepare(b)[1][0,0][0]@f),'coefficient_norm':float(np.linalg.norm(z))}
            self.history.append(row);print(json.dumps(row),flush=True)
            if self.directory is not None:
                with (self.directory/'history.jsonl').open('a') as out:out.write(json.dumps(row)+'\n')
        return r

    def jacobian(self,z):self.jcalls+=1;return self.compute(z,jac=True)[1]

    def save_candidate(self,z,name,cost=None):
        b,h,f,*_=self.coefficients(z)
        data={'schema':'rational-A1-v1','basis_family':self.family,'degree':self.degree,'created_utc':utc(),'status':'unverified approximate state; not a numerical YES','beta':b,
              'indices':[list(k) for k in self.ij],'H_coefficients':h.tolist(),'F_coefficients':f.tolist(),
              'formula':{'D':'1+x^2+y^2','q_s':'x^2/D','q_t':'y^2/D','H':'D^(-1/(2*beta))*sum h_ij*q_s^i*q_t^j','F':'D^(-1/beta)*sum f_ij*q_s^i*q_t^j','Psi':'x*y*H','Theta':'y*F','Omega':'-Delta Psi'},
              'normalization':{'H00':-2.,'F_s00':self.b1,'a0_free':True,'beta_free':self.free_beta},
              'search':{'degree':self.degree,'grid_n':self.n,'R':self.R,'initial_beta':self.beta,'initial_a0':self.a0_initial,'seed':self.seed,'weighted_cost':cost},
              'basis_definition':'For monomial, B_ij=q_s^i*q_t^j. For bernstein, B_ij=degree!/(i!*j!*(degree-i-j)!)*q_s^i*q_t^j*D^(-(degree-i-j)); replace each q_s^i*q_t^j in the field formulas by B_ij.',
              'scope':'Smooth whole-plane rational ansatz with beta-dependent leading tails. Higher fractional far-field corrections are not a complete free expansion. Failure of this family excludes no full profile class.'}
        (self.directory/name).write_text(json.dumps(data,indent=2)+'\n')


def solve(args):
    p=Problem(args.degree,args.grid,args.radius,args.beta,args.b1,args.a0,args.free_beta,args.seed,args.basis)
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True);p.directory=out
    z=p.initial()
    if args.resume:
        old=json.loads(Path(args.resume).read_text());
        if old.get('basis_family','monomial')!=p.family:raise ValueError('resuming across basis families requires explicit conversion')
        if abs(old['beta']-p.beta)>1e-12 and not p.free_beta:
            raise ValueError('fixed-beta continuation must preserve beta')
        if p.family=='bernstein':
            hh=elevate_bernstein(old['H_coefficients'],old['degree'],p.degree)
            ff=elevate_bernstein(old['F_coefficients'],old['degree'],p.degree)
        else:
            mapping={tuple(k):i for i,k in enumerate(old['indices'])}
            hh=np.array([old['H_coefficients'][mapping[k]] if k in mapping else 0. for k in p.ij])
            ff=np.array([old['F_coefficients'][mapping[k]] if k in mapping else 0. for k in p.ij])
        z=np.r_[hh[p.hmask],ff[p.fmask]]
        if p.free_beta:z=np.r_[z,old['beta']]
    p.save_candidate(z,'initial_candidate.json')
    low=np.full(p.npar,-np.inf);high=np.full(p.npar,np.inf)
    if p.free_beta:low[-1]=args.beta_min;high[-1]=args.beta_max
    start=utc()
    result=least_squares(p.objective,z,jac=p.jacobian,bounds=(low,high),max_nfev=args.max_nfev,gtol=1e-9,ftol=1e-11,xtol=1e-11,x_scale='jac')
    p.save_candidate(result.x,'candidate.json',float(result.cost))
    sv=np.linalg.svd(result.jac,compute_uv=False)
    summary={'start_utc':start,'end_utc':utc(),'elapsed_s':time.monotonic()-p.t0,'success':bool(result.success),'message':result.message,
             'nfev':result.nfev,'njev':result.njev,'cost':float(result.cost),'optimality':float(result.optimality),'max_abs_weighted_residual':float(np.max(np.abs(result.fun))),
             'jacobian_singular_values':sv.tolist(),'jacobian_shape':list(result.jac.shape),'beta':p.coefficients(result.x)[0],'a0':float(p.coefficients(result.x)[2][0]),
             'state':'not independently verified; no existence inference'}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=4);ap.add_argument('--grid',type=int,default=18);ap.add_argument('--radius',type=float,default=32);ap.add_argument('--beta',type=float,default=3);ap.add_argument('--a0',type=float,default=40);ap.add_argument('--b1',type=float,default=-1);ap.add_argument('--free-beta',action='store_true');ap.add_argument('--beta-min',type=float,default=2.001);ap.add_argument('--beta-max',type=float,default=12);ap.add_argument('--seed',type=int,default=0);ap.add_argument('--max-nfev',type=int,default=600);ap.add_argument('--output',required=True);ap.add_argument('--resume');ap.add_argument('--basis',choices=['monomial','bernstein'],default='bernstein');solve(ap.parse_args())
