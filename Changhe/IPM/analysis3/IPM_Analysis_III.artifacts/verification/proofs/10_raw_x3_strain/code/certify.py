"""Independent X3 scalar enclosure. Exact Cox polynomials and Arb tensor Gauss.
Only writes to the topic's evidence directory. No original evaluator is imported.
"""
import os
for var in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[var]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import factorial
import argparse,bisect,hashlib,json,time
import numpy as np
from flint import arb,acb,arb_mat,acb_mat,ctx
TOP=Path(__file__).resolve().parents[1]
LANE=TOP.parents[1]
SOURCE=LANE/'research_copy/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz'

def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def rat(x):return Q.from_float(float(x))
def ball(x):
    if isinstance(x,Q):return arb(x.numerator)/x.denominator
    return arb(x)
def text(x):return x.str(65)
def poly_add(a,b):
    out=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out
def poly_linear(a,c,d):
    out=[Q(0)]*(len(a)+1)
    for i,x in enumerate(a):out[i]+=x*c;out[i+1]+=x*d
    return out
def gauss_constant(n):return ball(Q(factorial(n)**4,(2*n+1)*factorial(2*n)**2))
def chebyshev(z,co):
    # Forward recurrence, independent of the original Clenshaw evaluator.
    terms=[z*0+1,z]
    for i in range(2,len(co)):terms.append(2*z*terms[-1]-terms[-2])
    return sum((c*t for c,t in zip(co,terms)),z*0)
def horner(rows,x):
    out=rows[-1]
    for row in reversed(rows[:-1]):out=out*x+row
    return out

class Trial:
    def __init__(self):
        self.sha=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        self.md5=hashlib.md5(SOURCE.read_bytes()).hexdigest()
        assert self.md5=='15f8095f7e79dbfa0c50d75e5fe8997a'
        with np.load(SOURCE,allow_pickle=False) as f:
            self.raw={key:f[key].copy() for key in f.files}
        f=self.raw
        self.knots=[rat(x) for x in f['spline_knots']]
        self.d=int(f['spline_order']);self.nr=int(f['degree']);self.nm=int(f['angular'])+1
        assert (self.d,self.nr,self.nm,int(f['singular']))==(7,375,201,6)
        z=[rat(x) for x in f['z']];self.z=z
        assert len(z)==1+self.nr*self.nm+6
        assert z[0]==rat(f['k'])
        self.k=ball(z[0]);self.L=ball(rat(f['L']));self.r0=ball(rat(f['origin_radius']))
        assert 0<self.k<1 and self.L>0 and self.r0>0
        self.p=6+2*self.k/(2-self.k);self.b=2/(1-self.k)
        assert 6<self.p<7
        self.pref=4*self.L**2/(arb.pi()*(1-self.k))
        self.coeff=[[Q(0)]+z[1+m*self.nr:1+(m+1)*self.nr] for m in range(self.nm)]
        self.tc=[ball(x) for x in z[-6:]]
        self.cm=[ball(max(map(abs,row))) for row in self.coeff]
        self.csum=sum(self.cm,arb(0));self.ct=sum(map(abs,self.tc),arb(0))
        self.bp=((self.p-2)/self.p)**((self.p-2)/2)*2/self.p
        self.m0=(self.csum+self.ct*self.bp).exp()
        assert self.knots[:8]==[Q(0)]*8 and self.knots[-8:]==[Q(1)]*8
        assert all(self.knots[i]<self.knots[i+1] for i in range(7,len(self.knots)-8))
        self.spans=[]
        for index in range(self.d,len(self.coeff[0])):
            a,b=self.knots[index:index+2]
            if a<b:self.spans.append((a,b,index))
        self.cache={}
    def polynomial(self,index):
        if index in self.cache:return self.cache[index]
        t=self.knots;a,b=t[index:index+2];mid=(a+b)/2;half=(b-a)/2
        basis={index:[Q(1)]}
        for degree in range(1,self.d+1):
            nxt={}
            for j in range(index-degree,index+1):
                u=[Q(0)];v=[Q(0)]
                if j in basis and t[j+degree]!=t[j]:
                    den=t[j+degree]-t[j]
                    u=poly_linear(basis[j],(mid-t[j])/den,half/den)
                if j+1 in basis and t[j+degree+1]!=t[j+1]:
                    den=t[j+degree+1]-t[j+1]
                    v=poly_linear(basis[j+1],(t[j+degree+1]-mid)/den,-half/den)
                nxt[j]=poly_add(u,v)
            basis=nxt
        total=[sum((v[j] for v in basis.values()),Q(0)) for j in range(8)]
        assert total==[Q(1)]+[Q(0)]*7
        weights=arb_mat([[ball(basis[i][j]) for i in range(index-7,index+1)] for j in range(8)])
        coeff=arb_mat([[ball(self.coeff[m][i]) for m in range(self.nm)] for i in range(index-7,index+1)])
        mat=weights*coeff
        rows=[arb_mat([row]) for row in mat.tolist()]
        crows=[acb_mat(row) for row in rows]
        value=(ball(mid),ball(half),rows,crows)
        self.cache[index]=value
        return value
    def radial(self,q,index,complex_domain=False):
        mid,half,rows,crows=self.polynomial(index)
        if complex_domain:
            ss=1-(1-q).pow(acb(self.b),analytic=True)
            sg=ss.pow(acb(self.p/2),analytic=True)*chebyshev(2*q-1,[acb(c) for c in self.tc])
            vals=horner(crows,(q-mid)/half).tolist()[0]
        else:
            ss=1-(1-q)**self.b
            sg=ss**(self.p/2)*chebyshev(2*q-1,self.tc)
            vals=horner(rows,(q-mid)/half).tolist()[0]
        chi=ss/(ss+self.r0**2*(1-ss))
        power=q*0+1
        for m in range(self.nm):
            if m>=2:power*=chi
            vals[m]*=power
        return vals+[sg]
    def radial_bound(self,a,b,index):
        mid=ball((a+b)/2);h=ball((b-a)/2)
        q=acb(arb(mid,(3*h).upper()),arb(0,(2*h).upper()))
        if not (1-q).real>0:return None
        ss=1-(1-q).pow(acb(self.b),analytic=True)
        if not ss.is_finite() or not ss.real>0:return None
        den=ss+self.r0**2*(1-ss)
        if not den.abs_lower()>0:return None
        vals=self.radial(q,index,True)
        if not all(v.is_finite() for v in vals):return None
        logm=sum((v.abs_upper() for v in vals[:-1]),arb(0))+self.bp*vals[-1].abs_upper()
        if not logm.is_finite():return None
        return logm,[(1-q).real.lower(),ss.real.lower(),den.abs_lower()]
    def angle_bound(self,a,b):
        mid=ball((a+b)/2)*arb.pi()/2;h=ball((b-a)/2)*arb.pi()/2
        z=acb(arb(mid,(2*h).upper()),arb(0,h.upper()))
        co=z.cos();si=z.sin()
        if not co.real>0:return None
        singular=co.pow(acb(self.p-2),analytic=True)*si**2
        if not singular.is_finite():return None
        logm=sum((c*(2*m*z).cos().abs_upper() for m,c in enumerate(self.cm)),arb(0))+self.ct*singular.abs_upper()
        kernel=(co**2*si*(3*z).sin()).abs_upper()
        if not logm.is_finite() or not kernel.is_finite():return None
        return logm,kernel,co.real.lower()

def prepare(t,args):
    epsq=Q(1,2**args.qcap);epst=Q(1,2**args.tcap)
    rad=[];ang=[]
    todo=[(max(a,epsq),min(b,1-epsq),index,0) for a,b,index in t.spans if max(a,epsq)<min(b,1-epsq)]
    todo.reverse()
    while todo:
        a,b,index,depth=todo.pop();got=t.radial_bound(a,b,index)
        if got is None or not got[0]<args.maxlog:
            assert depth<100,(a,b,index,depth,str(got))
            mid=(a+b)/2;todo.extend([(mid,b,index,depth+1),(a,mid,index,depth+1)])
        else:
            rad.append((a,b,index,*got))
            if len(rad)%100==0:emit(stage='radial_partition',accepted=len(rad),pending=len(todo))
    todo=[(Q(i,32),min(Q(i+1,32),1-epst),0) for i in reversed(range(32))]
    while todo:
        a,b,depth=todo.pop();got=t.angle_bound(a,b)
        if got is None or not got[0]<args.maxlog:
            assert depth<100,(a,b,depth,str(got))
            mid=(a+b)/2;todo.extend([(mid,b,depth+1),(a,mid,depth+1)])
        else:ang.append((a,b,*got))
    er=arb.pi()/2*gauss_constant(args.nq)*sum((ball(b-a)*lm.exp() for a,b,_,lm,_ in rad),arb(0))
    et=gauss_constant(args.nt)*arb(2)**(2*args.nt)*sum((ball(b-a)*arb.pi()/2*lm.exp()*ker for a,b,lm,ker,_ in ang),arb(0))
    ecq=ball(epsq)*arb.pi()*t.m0
    d=ball(epst)*arb.pi()/2;ect=d**3/3*(t.csum+t.ct*d**(t.p-2)).exp()
    errors=dict(radial=text(er),angular=text(et),q_strips=text(ecq),theta_strip=text(ect),strain_error=text(t.pref*(er+et+ecq+ect)))
    part={'date':now(),'input_sha256':t.sha,'settings':vars(args),'q':[[str(a),str(b),index,text(lm),list(map(text,margins))] for a,b,index,lm,margins in rad],'theta_over_pi_half':[[str(a),str(b),text(lm),text(ker),text(margin)] for a,b,lm,ker,margin in ang],'errors':errors}
    (TOP/'evidence'/f'{args.tag}_partition.json').write_text(json.dumps(part,indent=2)+'\n')
    emit(stage='prepared',radial_cells=len(rad),angular_cells=len(ang),errors=errors)
    return rad,ang,er+et+ecq+ect

def audit_nodes(n):
    pairs=[arb.legendre_p_root(n,j,weight=True) for j in range(n)]
    assert all(-1<x<1 and w>0 for x,w in pairs)
    assert all(pairs[i][0]>pairs[i+1][0] for i in range(n-1))
    for k in range(2*n):
        target=arb(0) if k%2 else arb(2)/(k+1)
        assert sum((w*x**k for x,w in pairs),arb(0)).overlaps(target)
    return pairs

def main(args):
    ctx.prec=args.bits;ctx.threads=1
    started=time.monotonic();t=Trial()
    emit(stage='start',input_sha256=t.sha,global_M=text(t.m0),settings=vars(args))
    rad,ang,error=prepare(t,args)
    if args.prepare_only:return
    nq=audit_nodes(args.nq);nt=audit_nodes(args.nt)
    points=[];kernels=[]
    for a,b,*rest in ang:
        mid=ball((a+b)/2)*arb.pi()/2;half=ball((b-a)/2)*arb.pi()/2
        for x,w in nt:
            theta=mid+half*x;points.append(theta)
            kernels.append(half*w*theta.cos()**2*theta.sin()*(3*theta).sin())
    angular=arb_mat([[(2*m*x).cos() for x in points] for m in range(t.nm)]+[[x.cos()**(t.p-2)*x.sin()**2 for x in points]])
    total=arb(0)
    for i,(a,b,index,*rest) in enumerate(rad):
        mid=ball((a+b)/2);half=ball((b-a)/2)
        vals=arb_mat([t.radial(mid+half*x,index) for x,w in nq])
        exponent=vals*angular
        for j,(x,w) in enumerate(nq):
            row=sum((exponent[j,k].exp()*kw for k,kw in enumerate(kernels)),arb(0))
            total+=half*w*row
        if (i+1)%20==0 or i+1==len(rad):
            checkpoint={'date':now(),'completed_cells':i+1,'total_cells':len(rad),'quadrature_sum':text(total),'elapsed_seconds':time.monotonic()-started}
            (TOP/'evidence'/f'{args.tag}_progress.json').write_text(json.dumps(checkpoint,indent=2)+'\n')
            emit(stage='quadrature',**{k:v for k,v in checkpoint.items() if k!='date'})
    strain=t.pref*(total+arb(0,error.upper()));defect=3/t.k-1-strain
    result={'date':now(),'status':'COMPUTED_PENDING_INDEPENDENT_AUDIT','input_sha256':t.sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),'settings':vars(args),'quadrature_sum':text(total),'unscaled_error':text(error),'strain':text(strain),'canonical_ell':text((1+strain)/3),'held_normalization_defect':text(defect),'normalization_defect_excludes_zero':not defect.contains(0),'seconds':time.monotonic()-started,'scope':'exact raw X3 scalar integral, not a stationary solution or inverse'}
    (TOP/'evidence'/f'{args.tag}_result.json').write_text(json.dumps(result,indent=2)+'\n')
    emit(stage='result',result=result)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=192);ap.add_argument('--nq',type=int,default=24);ap.add_argument('--nt',type=int,default=40);ap.add_argument('--maxlog',type=int,default=12);ap.add_argument('--qcap',type=int,default=68);ap.add_argument('--tcap',type=int,default=22);ap.add_argument('--tag',default='raw_x3_24_40');ap.add_argument('--prepare-only',action='store_true')
    main(ap.parse_args())
