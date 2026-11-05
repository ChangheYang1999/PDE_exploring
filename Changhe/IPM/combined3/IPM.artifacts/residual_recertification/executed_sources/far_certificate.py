"""Fresh exact-source exterior residual certificate, no historical norm input."""
import argparse, json, math, sys, time
from collections import defaultdict
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, arb, ctx
sys.dont_write_bytecode = True
ROOT=Path('/mnt/d/Changhe_D/PDE_exploring')
sys.path.insert(0,str(ROOT/'Changhe/IPM/combined3/IPM.artifacts/coercivity_residual'))
from fields013 import Evaluator,C,SOURCE_HASHES,rational_arb
from asymptotics013 import Expansion,hdiff

def group_polys(field):
    shift=max(n for k,n,p in field)+2
    dest={}
    for (kind,n,p),a in field.items():
        if (p,kind) not in dest: dest[p,kind]=[Q(0)]*(2*shift+1)
        dest[p,kind][shift+n]+=a/2
        dest[p,kind][shift-n]+=(a/2 if kind=='c' else -a/2)
    return {k:fmpq_poly(v) for k,v in dest.items()},shift

def residual_exact(a):
    rho=a.field('rho',0,0)
    floor=Q(-5);out=defaultdict(Q);omitted=defaultdict(lambda:arb(0))
    for (kind,n,p),v in rho.items():
        if p>=floor:out[kind,n,p]+=(C*p-1)*v
        else:omitted[p]+=arb(abs((C*p-1)*v))
    for uk,gk in [(('u1',0,0),('rho',1,0)),(('u2',0,0),('rho',0,1))]:
        A,sa=group_polys(a.field(*uk)); B,sb=group_polys(a.field(*gk))
        for (p,k),P in A.items():
            for (q,l),T in B.items():
                assert k!=l # both products have sine parity, no i*i sign.
                if p+q<floor:
                    # Fourier coefficient l1 product bound; polynomial
                    # coefficients each represent half a real mode.
                    omitted[p+q]+=arb(sum((abs(v)for v in P.coeffs()),Q(0))*sum((abs(v)for v in T.coeffs()),Q(0)))
                    continue
                PT=P*T
                for n in range(1,sa+sb+1):
                    v=2*PT[sa+sb+n]
                    if v:out['s',n,p+q]+=v
    return {k:v for k,v in out.items() if v},dict(omitted)

def differentiate(field,i,j):
    out=field
    for axis in 'x'*i+'y'*j:
        dest=defaultdict(Q); groups=defaultdict(dict)
        for (kind,n,p),v in out.items():groups[p][kind,n]=v
        for p,mm in groups.items():
            for (kind,n),v in hdiff(mm,p,axis).items():dest[kind,n,p-1]+=v
        out={k:v for k,v in dest.items() if v}
    return out

def add(*rows):
    out=defaultdict(lambda:arb(0))
    for row in rows:
        for p,v in row.items():out[p]+=v
    return dict(out)
def scale(row,c,p=Q(0)):return {k+p:c*v for k,v in row.items()}
def product(A,B):
    out=defaultdict(lambda:arb(0))
    for p,v in A.items():
        for q,w in B.items():out[p+q]+=v*w
    return dict(out)
def finite_abs(field):
    out=defaultdict(lambda:arb(0))
    for (kind,n,p),v in field.items():out[p]+=arb(abs(v))
    return dict(out)
def remainder(a,name,i,j,R):
    # For omitted q>=N each differentiated coefficient is bounded by
    # (|exponent|+2q+n+d)^d M/rad^q. Consecutive majorants have ratio
    # <= z*(1+2/(2N+d))^d < 8z, for every d>=0.
    rad=rational_arb(a.radius);z=1/(R*R*rad); assert 8*z<1
    N=a.degree+1; out=defaultdict(lambda:arb(0))
    for kind,n,exponent,M in a.majorants:
        d=i+j+(3 if kind=='c' else 2)
        count=2 if name=='rho' else 1
        aa=abs(exponent)+2*N+n+d
        out[exponent-d-2*N]+=count*M*rational_arb(aa)**d/rad**N/(1-8*z)
    return dict(out)
def minkowski(row,R,weight):
    ans=arb(0)
    for p,v in row.items():
        pp=p+weight; assert pp < -1, str(pp)
        ans+=v*R**rational_arb(pp+1)/rational_arb(-2*pp-2).sqrt()
    return (2*arb.pi()).sqrt()*ans
def serial_row(row):return [{'power':str(p),'coefficient_bound':v.str(95)}for p,v in sorted(row.items())]

def run(args):
    ctx.prec=args.precision;t=time.monotonic();e=Evaluator(args.precision)
    a=Expansion(e,'far',degree=args.degree)
    print('expansion',time.monotonic()-t,flush=True)
    if args.prefix_input:
        previous=json.loads(Path(args.prefix_input).read_text())
        assert previous['source_hashes']==SOURCE_HASHES
        assert previous['expansion_degree']>=2 and args.degree>=2
        f={(row['kind'],row['harmonic'],Q(row['power'])):Q(row['coefficient_exact']) for row in previous['residual_finite_terms']}
        assert all(k[2]>=-5 for k in f)
        # Terms q>=3 of either potential cannot affect residual powers >=-5.
        maxima={kind:max(n+2*b-2*v for kk,n,b,tt,v,p in e.groups if kk==kind) for kind in ['c','s']}
        density_max=max(maxima['c']-3,maxima['s']-2)
        density_omitted=max(maxima['c']-3-6,maxima['s']-2-6)
        assert density_omitted < -5
        assert density_max+density_omitted-1 < -5
        omitted=defaultdict(lambda:arb(0))
        for (kind,n,p),v in a.field('rho',0,0).items():
            if p<-5:omitted[p]+=arb(abs((C*p-1)*v))
        for uk,gk in [(('u1',0,0),('rho',1,0)),(('u2',0,0),('rho',0,1))]:
            AA=finite_abs(a.field(*uk));BB=finite_abs(a.field(*gk))
            for p,v in AA.items():
                for q,w in BB.items():
                    if p+q<-5:omitted[p+q]+=v*w
        omitted=dict(omitted)
    else:
        f,omitted=residual_exact(a)
    print('residual',time.monotonic()-t,len(f),'leading',max(k[2]for k in f),flush=True)
    R=arb(args.radius)
    angular_cap=2*max(n for kind,n,b,t,v,p in e.groups)+6
    assert angular_cap<=330
    P={};E={}
    for name,maxd in [('rho',4),('u1',3),('u2',3)]:
        for k in range(maxd+1):
            for i in range(k+1):
                j=k-i;key=name,i,j
                P[key]=finite_abs(a.field(name,i,j));E[key]=remainder(a,name,i,j,R)
    rows=[]
    for k in range(4):
        for i in range(k+1):
            j=k-i
            err=add(scale(E['rho',i+1,j],arb(C),Q(1)),scale(E['rho',i,j+1],arb(C),Q(1)),scale(E['rho',i,j],arb(abs(C*k-1))))
            for ii in range(i+1):
                for jj in range(j+1):
                    coeff=math.comb(i,ii)*math.comb(j,jj)
                    for name,dx,dy in [('u1',1,0),('u2',0,1)]:
                        uk=name,ii,jj;gk='rho',i-ii+dx,j-jj+dy
                        err=add(err,scale(add(product(P[uk],E[gk]),product(E[uk],P[gk]),product(E[uk],E[gk])),arb(coeff)))
            finite=finite_abs(differentiate(f,i,j));whole=add(finite,err)
            # Omitted finite residual terms have angular degree <= 324.
            # Each Cartesian derivative has Fourier l1 operator norm
            # <= |power|+degree; the degree grows by at most one.
            omitted_deriv={p-k:v*rational_arb(abs(p)+330+k)**k for p,v in omitted.items()}
            err=add(err,omitted_deriv);whole=add(finite,err)
            vals={str(w):minkowski(whole,R,Q(w)).str(95) for w in (0,1)}
            rows.append({'i':i,'j':j,'norm_upper':vals,'finite_absolute_powers':serial_row(finite),'remainder_absolute_powers':serial_row(err)})
            print('derivative',i,j,vals,flush=True)
    out={'status':'FRESH_SOURCE_EXTERIOR_CERTIFICATE','source_hashes':SOURCE_HASHES,'fixed_c':str(C),'radius_exact':args.radius,'expansion_degree':args.degree,'analytic_u_radius_exact':str(a.radius),'precision':args.precision,'elapsed_seconds':time.monotonic()-t,'residual_finite_terms':[{'kind':k,'harmonic':n,'power':str(p),'coefficient_exact':str(v)}for(k,n,p),v in sorted(f.items())],'potential_majorants':[{'kind':k,'harmonic':n,'exponent':str(p),'M':M.str(95)}for k,n,p,M in a.majorants],'derivatives':rows}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--radius',default='100000000000000000000');p.add_argument('--degree',type=int,default=2);p.add_argument('--precision',type=int,default=512);p.add_argument('--prefix-input');p.add_argument('--output',default='/tmp/residual_recertification/far_certificate.json');run(p.parse_args())
