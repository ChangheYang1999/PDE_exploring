"""Rigorous full-plane X3 strain via exact inputs, Arb Gaussian nodes and Cauchy errors.

See ../PROOF.md. CPU: one thread, no network, no server. Every file output is
inside the lane. This certifies a scalar integral, not a PDE solution.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import argparse, bisect, hashlib, json, math, resource, time
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
from flint import arb, acb, arb_mat, acb_mat, arb_series, ctx

BASE=Path(__file__).resolve().parents[3]

def utc():return datetime.now(timezone.utc).isoformat()
def aa(x):
    if isinstance(x,F):return arb(x.numerator)/x.denominator
    return arb(x)
def jsball(x):return {'ball':x.str(35),'lower':x.lower().str(40),'upper':x.upper().str(40)}
def emit(**d):print(json.dumps({'utc':utc(),**d}),flush=True)
def cn(n):return arb(math.factorial(n))**4/((2*n+1)*arb(math.factorial(2*n))**2)
def horner(rows,z):
    out=rows[-1]
    for row in rows[-2::-1]:out=out*z+row
    return out

def cheb(z,co):
    if len(co)==1:return co[0]+z*0
    b1=z*0;b2=z*0
    for c in co[:0:-1]:b0=c+2*z*b1-b2;b2,b1=b1,b0
    return co[0]+z*b1-b2

class Data:
    def __init__(self):
        p=BASE/'data_exact/x3.json';self.sha=hashlib.sha256(p.read_bytes()).hexdigest()
        d=json.loads(p.read_text());self.raw=d
        vals={k:aa(F.from_float(float.fromhex(v))) for k,v in d['scalars_hex'].items()}
        self.L,self.k,self.r0=vals['L'],vals['k'],vals['origin_radius']
        self.cl_stored=vals['c_l']
        self.b=2/(1-self.k);self.p=6+2*self.k/(2-self.k)
        self.pref=4*self.L**2/(arb.pi()*(1-self.k))
        self.bp=((self.p-2)/self.p)**((self.p-2)/2)*2/self.p
        self.t=[F.from_float(float.fromhex(v)) for v in d['spline_knots_hex']]
        self.ta=[aa(v) for v in self.t]
        z=[aa(F.from_float(float.fromhex(v))) for v in d['z_hex']]
        self.nm=d['integers']['angular']+1;self.deg=d['integers']['spline_order'];nr=d['integers']['degree']
        self.co=[[arb(0) for _ in range(self.nm)]]+[[z[1+m*nr+i] for m in range(self.nm)] for i in range(nr)]
        self.tc=z[-d['integers']['singular']:]
        self.cm=[max((abs(row[m]) for row in self.co),key=lambda a:float(a)) for m in range(self.nm)]
        self.csum=sum(self.cm,arb(0));self.ct=sum(map(abs,self.tc),arb(0))
        self.global_M=(self.csum+self.ct*self.bp).exp()

    def poly(self,left,right):
        mid=(left+right)/2
        span=bisect.bisect_right(self.t,mid)-1
        assert self.deg<=span<len(self.co)
        assert left>=self.t[span] and right<=self.t[span+1]
        q=arb_series([aa(mid),arb(1)],prec=self.deg+1)
        w=[]
        for basis in range(self.deg+1):
            vals=[arb_series([arb(int(j==basis))],prec=self.deg+1) for j in range(self.deg+1)]
            for lev in range(1,self.deg+1):
                for j in range(self.deg,lev-1,-1):
                    idx=span-self.deg+j
                    alpha=(q-self.ta[idx])/(self.ta[idx+self.deg-lev+1]-self.ta[idx])
                    vals[j]=(1-alpha)*vals[j-1]+alpha*vals[j]
            w.append([vals[-1][power] for power in range(self.deg+1)])
        weights=arb_mat([[w[b][power] for b in range(self.deg+1)] for power in range(self.deg+1)])
        pol=weights*arb_mat(self.co[span-self.deg:span+1])
        rows=[arb_mat([row]) for row in pol.tolist()]
        return aa(mid),rows

    def radial(self,q,mid,rows,complex_arg=False):
        if complex_arg:
            zero=acb(0);one=acb(1)
            s=one-(one-q).pow(acb(self.b),analytic=True)
            chi=s/(s+self.r0**2*(one-s))
            sg=s.pow(acb(self.p/2),analytic=True)*cheb(2*q-one,[acb(v) for v in self.tc])
        else:
            zero=arb(0);one=arb(1)
            s=one-(one-q)**self.b
            chi=s/(s+self.r0**2*(one-s))
            sg=s**(self.p/2)*cheb(2*q-one,self.tc)
        bs=horner(rows,q-mid).tolist()[0]
        out=[];mul=one
        for m,bv in enumerate(bs):
            if m>1:mul=mul*chi
            out.append(bv*mul)
        out.append(sg)
        return out

    def radial_bound(self,left,right,rows_mid):
        mid,rows=rows_mid;h=aa((right-left)/2)
        # R=2h; rectangle covers all radius-R disks centered in [left,right].
        q=acb(arb(mid,(3*h).upper()),arb(0,(2*h).upper()))
        cr=[acb_mat(row) for row in rows]
        vals=self.radial(q,mid,cr,True)
        if not all(v.is_finite() for v in vals):return None
        logM=sum((v.abs_upper() for v in vals[:-1]),arb(0))+self.bp*vals[-1].abs_upper()
        if not logM.is_finite():return None
        return logM

    def angle_bound(self,left,right):
        # Coordinates are theta/(pi/2); R=h in physical angular units.
        mid=aa((left+right)/2)*arb.pi()/2;h=aa((right-left)/2)*arb.pi()/2
        z=acb(arb(mid,(2*h).upper()),arb(0,h.upper()))
        co,si=z.cos(),z.sin()
        sg=co.pow(acb(self.p-2),analytic=True)*si**2
        if not sg.is_finite():return None
        logM=sum((self.cm[m]*(2*m*z).cos().abs_upper() for m in range(self.nm)),arb(0))+self.ct*sg.abs_upper()
        kernel=(co**2*si*(3*z).sin()).abs_upper()
        if not logM.is_finite() or not kernel.is_finite():return None
        return logM,kernel

def prepare(data,maxlog):
    cap=F(1,2**60);tcap=F(1,2**20)
    knots=sorted(set(data.t));rad=[]
    stack=[(max(a,cap),min(b,1-cap),0) for a,b in zip(knots[:-1],knots[1:]) if max(a,cap)<min(b,1-cap)]
    stack.reverse()
    while stack:
        a,b,depth=stack.pop();pol=data.poly(a,b);bound=data.radial_bound(a,b,pol)
        if bound is None or not bound<maxlog:
            assert depth<90,('radial depth',str(a),str(b),str(bound))
            mid=(a+b)/2;stack.extend([(mid,b,depth+1),(a,mid,depth+1)])
        else:rad.append((a,b,pol,bound))
        if len(rad)%100==0 and rad:emit(stage='radial_partition',accepted=len(rad),pending=len(stack))
    angular=[];stack=[(F(i,16),min(F(i+1,16),1-tcap),0) for i in range(16)];stack.reverse()
    while stack:
        a,b,depth=stack.pop();bound=data.angle_bound(a,b)
        if bound is None or not bound[0]<maxlog:
            assert depth<60,('angular depth',str(a),str(b),str(bound))
            mid=(a+b)/2;stack.extend([(mid,b,depth+1),(a,mid,depth+1)])
        else:angular.append((a,b,*bound))
    return rad,angular,cap,tcap

def main(args):
    ctx.prec=args.bits;ctx.threads=1;ctx.cap=8
    resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
    started=time.monotonic();d=Data()
    emit(stage='start',bits=args.bits,nq=args.nq,nt=args.nt,input_sha256=d.sha,global_M=jsball(d.global_M),Cq=jsball(cn(args.nq)),Ctheta=jsball(cn(args.nt)*arb(2)**(2*args.nt)))
    rad,ang,cap,tcap=prepare(d,args.maxlog)
    Er=sum((aa(b-a)*lm.exp()*cn(args.nq) for a,b,_,lm in rad),arb(0))*arb.pi()/2
    Et=sum((aa(b-a)*arb.pi()/2*ker*lm.exp()*cn(args.nt)*arb(2)**(2*args.nt) for a,b,lm,ker in ang),arb(0))
    Eqcap=2*aa(cap)*arb.pi()/2*d.global_M
    delta=aa(tcap)*arb.pi()/2
    Etcap=delta**3/3*(d.csum+d.ct*delta**(d.p-2)).exp()
    error=Er+Et+Eqcap+Etcap
    prep=dict(stage='prepared',radial_cells=len(rad),angular_cells=len(ang),radial_error=jsball(Er),angular_error=jsball(Et),radial_caps=jsball(Eqcap),angular_cap=jsball(Etcap),strain_error=jsball(d.pref*error),seconds=time.monotonic()-started)
    emit(**prep)
    tag=args.tag
    evidence=BASE/'research/canonical_inverse/evidence'
    partition={'q':[[str(a),str(b)] for a,b,_,_ in rad],'theta_over_pi_half':[[str(a),str(b)] for a,b,_,_ in ang],'cap_q':str(cap),'cap_theta_normalized':str(tcap),'utc':utc(),'input_sha256':d.sha,'settings':vars(args),'bounds':prep}
    (evidence/(tag+'_partition.json')).write_text(json.dumps(partition,indent=2)+'\n')
    if args.prepare_only:return
    qnw=[arb.legendre_p_root(args.nq,k,weight=True) for k in range(args.nq)]
    tnw=[arb.legendre_p_root(args.nt,k,weight=True) for k in range(args.nt)]
    assert all(w>0 for _,w in qnw+tnw)
    assert sum((w for _,w in qnw),arb(0)).contains(2)
    assert sum((w for _,w in tnw),arb(0)).contains(2)
    thetas=[];kernels=[]
    for a,b,_,_ in ang:
        mid=aa((a+b)/2)*arb.pi()/2;half=aa((b-a)/2)*arb.pi()/2
        for node,weight in tnw:
            th=mid+half*node;thetas.append(th)
            kernels.append(half*weight*th.cos()**2*th.sin()*(3*th).sin())
    angles=arb_mat([[(2*m*th).cos() for th in thetas] for m in range(d.nm)]+[[th.cos()**(d.p-2)*th.sin()**2 for th in thetas]])
    total=arb(0)
    for i,(a,b,(mid,rows),_) in enumerate(rad):
        half=aa((b-a)/2)
        nodes=[mid+half*node for node,_ in qnw]
        values=arb_mat([d.radial(q,mid,rows) for q in nodes])
        exponents=values*angles
        for j,(_,weight) in enumerate(qnw):
            acc=sum((exponents[j,k].exp()*kernels[k] for k in range(len(thetas))),arb(0))
            total+=half*weight*acc
        if (i+1)%10==0 or i+1==len(rad):emit(stage='quadrature',done=i+1,total_cells=len(rad),sum=jsball(total),seconds=time.monotonic()-started)
    assert total.is_finite() and error.is_finite()
    enlarged=total+arb(0,error.upper())
    strain=d.pref*enlarged
    defect=3/d.k-1-strain
    result={'utc':utc(),'status':'SCALAR_ENCLOSURE_COMPUTED_REQUIRES_CODE_AUDIT','input_sha256':d.sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'settings':vars(args),'method':'Arb exact dyadic inputs; Gaussian nodes and weights; polynomial spline extension; Cauchy derivative bounds and explicit endpoint caps','quadrature_sum':jsball(total),'unscaled_error':jsball(error),'strain':jsball(strain),'canonical_cl':jsball((1+strain)/3),'held_normalization_defect':jsball(defect),'excludes_zero_normalization_defect':not defect.contains(0),'seconds':time.monotonic()-started,'endpoint_warning':'This scalar result does not prove profile existence, exclusion, a residual norm or linear invertibility.'}
    (evidence/(tag+'_result.json')).write_text(json.dumps(result,indent=2)+'\n')
    emit(stage='result',**result)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--nq',type=int,default=20);ap.add_argument('--nt',type=int,default=32);ap.add_argument('--bits',type=int,default=160);ap.add_argument('--maxlog',type=int,default=12);ap.add_argument('--tag',default='strain_arb');ap.add_argument('--prepare-only',action='store_true');main(ap.parse_args())
