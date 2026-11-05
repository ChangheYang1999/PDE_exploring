"""Source-bound finite-radius residual Taylor series and Cauchy enclosure."""
import sys,time,math,json
from pathlib import Path
from collections import defaultdict
from repository_paths import add_source_modules
add_source_modules()
from fields013 import Evaluator,C,rational_arb,SOURCE_HASHES
from flint import arb,arb_series,arb_poly,ctx

def encode(modes,K,shift,stride,scale):
    out=[arb(0)]*((2*shift)*stride+K+1)
    powers=[scale**k for k in range(K+1)]
    for (kind,n),p in modes.items():
        assert n<=shift
        for k in range(K+1):
            a=p[k]*powers[k]/2
            out[(shift+n)*stride+k]+=a
            out[(shift-n)*stride+k]+=a if kind=='c' else -a
    return arb_poly(out)

def residual_taylor(e,r,K,scale=None):
    r=arb(r);scale=r/32 if scale is None else arb(scale);fields=e.modes_taylor(r,K)
    shift=max(n for mm in fields.values()for kind,n in mm)
    stride=2*K+1
    v1=dict(fields['u1',0,0]);v2=dict(fields['u2',0,0]);rr=arb_series([r,1],prec=K+1)
    v1['c',1]=v1.get(('c',1),arb_series([],prec=K+1))+arb(C)*rr
    v2['s',1]=v2.get(('s',1),arb_series([],prec=K+1))+arb(C)*rr
    out=encode(v1,K,shift,stride,scale)*encode(fields['rho',1,0],K,shift,stride,scale)
    out+=encode(v2,K,shift,stride,scale)*encode(fields['rho',0,1],K,shift,stride,scale)
    rho=fields['rho',0,0]
    result={}
    for n in range(1,2*shift+1,2):
        coeffs=[2*out[(2*shift+n)*stride+k]/scale**k-(rho[('s',n)][k] if ('s',n)in rho else arb(0)) for k in range(K+1)]
        if any(coeffs):result[n]=arb_series(coeffs,prec=K+1)
    return result

def residual_majorant(e,r):
    """Scalar absolute Fourier-sum bound of F on radial disk radius r/8."""
    r=arb(r);m,R=e.mode_majorants(r)
    def sumabs(key):return sum((v.abs_upper()for v in m[key].values()),arb(0))
    rho=sumabs(('rho',0,0));rx=sumabs(('rho',1,0));ry=sumabs(('rho',0,1))
    u1=sumabs(('u1',0,0));u2=sumabs(('u2',0,0))
    # |x|,|y| angular coefficients sums are <= |r+z|.
    H=((arb(C)*(r+R)+u1)*rx+(arb(C)*(r+R)+u2)*ry+rho).abs_upper()
    return H,R

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--K',type=int,default=64);ap.add_argument('--r',default='1');ap.add_argument('--prec',type=int,default=768);args=ap.parse_args()
    e=Evaluator(args.prec,max_density_order=1,max_velocity_order=0);t=time.monotonic();f=residual_taylor(e,args.r,args.K);print('taylor',time.monotonic()-t,len(f),flush=True)
    H,R=residual_majorant(e,args.r);print('M',H,'R',R,'t',time.monotonic()-t,flush=True)
    print('F amplitude',sum((p[0]**2 for p in f.values()),arb(0)).sqrt(),'Kmag',max(float(abs(p[args.K]).upper())for p in f.values()))

def improved_majorant(e,r):
    """Cancellation-aware potential polynomial bound on disk |z-r|≤r/4.

    Shift grouped rational polynomial to z0=r²/(t+r²). All shifted
    coefficients are Arb enclosures. Bound |Z-z0| by exact Mobius difference.
    Bind r^n/(t+r²)^v using Z^v r^(n-2v) when v≥0.
    """
    from fields013 import derivative_series
    r=arb(r);D=r/4;R=r/8;gap=D-R;lo=r-D;hi=r+D;ss=r*r
    pm=defaultdict(lambda:arb(0));ctx.cap=max(ctx.cap,30)
    for (kind,n,b,t,v,p),prep in zip(e.groups,e.prepared):
        t=arb(t);lower=t+arb(9)*ss/16
        center=ss/(t+ss);delta=t*(2*r*D+D*D)/((t+ss)*lower)
        z=arb_series([center,1],prec=p.degree()+1)
        poly=arb_series([],prec=p.degree()+1)
        for a in reversed(prep[-1]):poly=poly*z+a
        bound=arb(0)
        for a in reversed(poly.coeffs()):bound=bound*delta+a.abs_upper()
        k=n//2; eps=n-2*k; alpha=b+k-v
        lower1=1+arb(9)*ss/16
        z1=ss/(1+ss)+(2*r*D+D*D)/((1+ss)*lower1)
        at=(1+ss)/(t+ss)+abs(1-t)*(2*r*D+D*D)/((t+ss)*lower)
        inverse_at=(t+ss)/(1+ss)+abs(1-t)*(2*r*D+D*D)/((1+ss)*lower1)
        bound*=hi**eps*z1**k*(lower1 if alpha<0 else 1+hi*hi)**rational_arb(alpha)
        bound*=at**v if v>=0 else inverse_at**(-v)
        pm[kind,n]+=bound
    cache={}
    def deriv(kind,i,j):
        key=kind,i,j
        if key not in cache:
            out=arb(0)
            for (kk,n),M in pm.items():
                if kk!=kind:continue
                for (a,b,N,t),v in derivative_series(kind,n,i,j).items():
                    out+=arb(abs(v))*math.factorial(a)*M/gap**a/(r-R)**b
            cache[key]=out
        return cache[key]
    def rho(i,j):return deriv('c',i+2,j+1)+deriv('c',i,j+3)+deriv('s',i+2,j)+deriv('s',i,j+2)
    u1=deriv('c',1,2)+deriv('s',1,1);u2=deriv('c',2,1)+deriv('s',2,0)
    H=((arb(C)*(r+R)+u1)*rho(1,0)+(arb(C)*(r+R)+u2)*rho(0,1)+rho(0,0)).abs_upper()
    return H,R
