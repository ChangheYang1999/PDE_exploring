#!/usr/bin/env python3
"""Exact actual-stream derivative expansions and endpoint norm bounds.

No inherited files are modified. All input imports run with Python -B.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json,math
from pathlib import Path
import sys,time
from flint import fmpq as Q,arb,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,rational_arb
from asymptotics013 import Expansion,homog_series,hdiff
ALPHAS=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]

def add(out,kind,n,p,a):
    if n<0:n=-n;a=-a if kind=='s' else a
    if kind=='s' and n==0:return
    out[kind,n,p]+=a

def stream(ex):
    out=defaultdict(Q)
    for (kind,n,p),a in ex.pot.items():
        dx,dy=(1,1) if kind=='c' else (1,0)
        for (k,N),b in homog_series(kind,n,p,dx,dy).items():add(out,k,N,p-dx-dy,a*b)
    return {k:v for k,v in out.items() if v}

def coord(modes,axis):
    out=defaultdict(Q)
    for (kind,n,p),a in modes.items():
        if axis=='x':add(out,kind,n+1,p+1,a/2);add(out,kind,n-1,p+1,a/2)
        elif kind=='c':add(out,'s',n+1,p+1,a/2);add(out,'s',n-1,p+1,-a/2)
        else:add(out,'c',n-1,p+1,a/2);add(out,'c',n+1,p+1,-a/2)
    return {k:v for k,v in out.items() if v}

def lap(modes):
    return {(kind,n,p-2):a*(p*p-n*n) for (kind,n,p),a in modes.items() if p*p!=n*n}

def derivative(modes,axis):
    out=defaultdict(Q)
    for (kind,n,p),a in modes.items():
        for (k,N),b in hdiff({(kind,n):Q(1)},p,axis).items():add(out,k,N,p-1,a*b)
    return {k:v for k,v in out.items() if v}

def derivative_components(modes,j):
    for _ in range(j//2):modes=lap(modes)
    return [modes] if j%2==0 else [derivative(modes,'x'),derivative(modes,'y')]

def cartesian_ops(j):
    k=j//2;out=[]
    for l in range(k+1):
        for axis in [None] if j%2==0 else ['x','y']:
            out.append((2*l+(axis=='x'),2*(k-l)+(axis=='y'),math.comb(k,l),0 if axis in [None,'x'] else 1))
    return out

def remainder_components(ex,alpha,j,R):
    out=[[] for _ in range(1 if j%2==0 else 2)]
    groups=defaultdict(int);ax,ay=alpha
    for dx,dy,c,component in cartesian_ops(j):
        for bx in range(min(ax,dx)+1):
            for by in range(min(ay,dy)+1):
                coef=c*math.comb(dx,bx)*math.comb(dy,by)*math.factorial(ax)//math.factorial(ax-bx)*math.factorial(ay)//math.factorial(ay-by)
                xx,yy=dx-bx,dy-by;kappa=ax+ay-bx-by
                assert xx+yy>=1
                name,ii,jj,sign=('u2',xx-1,yy,1) if xx>=1 else ('u1',0,yy-1,-1)
                groups[component,name,ii,jj,kappa]+=sign*coef
    for (component,name,i,k,kappa),coef in groups.items():
        if not coef:continue
        for a,p in ex.remainder_terms(name,i,k,R):out[component].append((abs(coef)*a,p+kappa))
    return out

def component_L2(modes,remainder,R,side):
    radial=defaultdict(lambda:arb(0))
    for (kind,n,p),a in modes.items():
        den=2*p+2 if side=='origin' else -2*p-2
        assert den>0
        angular=2*arb.pi() if n==0 else arb.pi()
        radial[kind,n]+=angular.sqrt()*arb(abs(a))*R**rational_arb(p+1)/rational_arb(den).sqrt()
    val=sum((v*v for v in radial.values()),arb(0)).sqrt()
    err=arb(0)
    for a,p in remainder:
        den=2*p+2 if side=='origin' else -2*p-2
        assert den>0
        err+=a*R**rational_arb(p+1)/rational_arb(den).sqrt()
    return val+(2*arb.pi()).sqrt()*err

def log_integral(p,R,lam,side):
    p=rational_arb(p)
    if side=='origin':
        assert lam*R<=2 and p+3>0
        return lam*R**(p+3)/(p+3)
    gamma=-p-2;assert gamma>0
    if lam*R<=2:
        T=2/lam
        # gamma=1 is absent for the actual fractional profile exponents.
        assert gamma!=1
        return lam*(T**(1-gamma)-R**(1-gamma))/(1-gamma)+T**(-gamma)*(2/gamma+2/(gamma*gamma))
    return R**(-gamma)*((2+2*(lam*R/2).log())/gamma+2/(gamma*gamma))

def critical_log_bound(comps,rems,R,lam,side):
    val=arb(0)
    for modes,rem in zip(comps,rems):
        for (_,_,p),a in modes.items():val+=arb(abs(a))*log_integral(p,R,lam,side)
        for a,p in rem:val+=a*log_integral(p,R,lam,side)
    # The angular absolute bound contributes 2pi and the normalized lemma
    # contributes (2pi)^-1; these factors cancel exactly.
    return val

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--side',choices=['origin','far'],required=True)
    ap.add_argument('--radius',required=True);ap.add_argument('--degree',type=int,default=18)
    ap.add_argument('--precision',type=int,default=512);ap.add_argument('--lambda-value',default='1/100000')
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();ctx.prec=args.precision
    tick=time.monotonic();e=Evaluator(args.precision,0,0);ex=Expansion(e,args.side,args.degree)
    print('expansion_complete',args.side,time.monotonic()-tick,flush=True)
    psi=stream(ex);rr=arb(Q(args.radius));lam=arb(Q(args.lambda_value));records=[]
    for ai,alpha in enumerate(ALPHAS):
        f=psi
        for axis in 'x'*alpha[0]+'y'*alpha[1]:f=coord(f,axis)
        energy={};critical=None
        for j in range(3+sum(alpha),8):
            comps=derivative_components(f,j);rems=remainder_components(ex,alpha,j,rr)
            norms=[component_L2(cc,rem,rr,args.side) for cc,rem in zip(comps,rems)]
            en=sum((x*x for x in norms),arb(0));energy[str(j)]=str(en.upper().fmpq())
            if j==4+sum(alpha):critical=critical_log_bound(comps,rems,rr,lam,args.side)
        records.append({'alpha':list(alpha),'energy_upper_exact':energy,'critical_log_low_upper_exact':str(critical.upper().fmpq())})
        print('alpha_complete',alpha,'seconds',time.monotonic()-tick,flush=True)
    deps=[Path(__file__),HERE.parent/'coercivity_residual/fields013.py',HERE.parent/'coercivity_residual/asymptotics013.py']
    out={'status':'EXACT_STREAM_ENDPOINT_UPPERS','side':args.side,'radius':args.radius,'lambda':args.lambda_value,
         'precision':args.precision,'degree':args.degree,'records':records,'seconds':time.monotonic()-tick,
         'bindings':{str(p.relative_to(HERE.parent)):sha256(p.read_bytes()).hexdigest() for p in deps},
         'whole_operator_bound':'NOT CLAIMED','stationary_existence':'NOT CLAIMED'}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
