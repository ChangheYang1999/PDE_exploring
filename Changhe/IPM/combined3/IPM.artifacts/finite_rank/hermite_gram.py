#!/usr/bin/env python3
"""Certified smooth-Hermite test Gram for <W J^q phi_i,W J^q phi_j>.

All polynomial arithmetic is exact Fraction. All special functions use Arb.
No profile-dependent operator or tail is certified by this Gram alone.
"""
import argparse, json, math
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from flint import arb, ctx


def add(*polys):
    out={}
    for p in polys:
        for ij,v in p.items():
            out[ij]=out.get(ij,Q(0))+v
    return {ij:v for ij,v in out.items() if v}


def scale(p,c):return {ij:v*c for ij,v in p.items() if v*c}


def mul(p,r):
    out={}
    for (i,j),v in p.items():
        for (k,l),w in r.items():
            ij=i+k,j+l
            out[ij]=out.get(ij,Q(0))+v*w
    return {ij:v for ij,v in out.items() if v}


def diff(p,k):
    out={}
    for ij,v in p.items():
        if ij[k]:
            new=list(ij);new[k]-=1
            out[tuple(new)]=v*ij[k]
    return out


def hermite(n,k,alpha):
    if n==0:return {(0,0):Q(1)}
    x={(1,0) if k==0 else (0,1):Q(1)/alpha}
    pp={(0,0):Q(1)};p=scale(x,2)
    for m in range(1,n):pp,p=p,add(scale(mul(x,p),2),scale(pp,-2*m))
    return p


def arbq(x):return arb(x.numerator)/x.denominator


def packet(v):
    # Arb string is an enclosure, not an uncertified decimal float.
    return {'ball':v.str(70),'midpoint':str(v.mid()),'radius':str(v.rad())}


def build(max_degree=7,alpha=Q(1),bits=256,q=Q(21,10)):
    ctx.prec=bits
    ids=[(m,n) for total in range(max_degree+1) for m in range(total+1) for n in [total-m] if m%2==0 and n%2==1]
    a2=alpha*alpha
    z=arbq(1/a2)
    aq=arbq(q)
    pi=arb.pi()
    @lru_cache(None)
    def moment(i,j,s):
        if i%2 or j%2:return arb(0)
        k,l=i//2,j//2
        # integral x^(2k)y^(2l) exp(-r²/alpha²)(1+r²)^s dxdy
        return ((arb(k)+arb('0.5')).gamma()*(arb(l)+arb('0.5')).gamma()*z.hypgeom_u(k+l+1,arbq(Q(k+l+2)+s)))
    def integ(poly,s):return sum((arbq(v)*moment(*ij,s) for ij,v in poly.items()),arb(0))
    ps=[];ds=[];norms=[]
    for m,n in ids:
        p=mul(hermite(m,0,alpha),hermite(n,1,alpha))
        ps.append(p)
        ds.append([add(diff(p,j),scale(mul(p,{(1,0) if j==0 else (0,1):Q(1)}),-1/a2)) for j in range(2)])
        # Fourier unitary Hermite normalization: alpha^-1 pi^-1/2 /sqrt(2^(m+n)m!n!)
        norms.append(1/(arbq(alpha)*pi.sqrt()*arb(2**(m+n)*math.factorial(m)*math.factorial(n)).sqrt()))
    bs=[]
    for i,ij in enumerate(ids):
        row=[]
        for j,jj in enumerate(ids):
            p0=add(mul(ps[i],ps[j]),scale(add(*(mul(ds[i][k],ds[j][k]) for k in range(2))),4))
            p1=add(*(mul({(1,0) if k==0 else (0,1):Q(1)},add(mul(ds[i][k],ps[j]),mul(ps[i],ds[j][k]))) for k in range(2)))
            p2=mul({(2,0):Q(1),(0,2):Q(1)},mul(ps[i],ps[j]))
            phase=(-1)**((sum(ij)-sum(jj))//2)
            val=phase*norms[i]*norms[j]*(integ(p0,q)+4*aq*integ(p1,q-1)+4*aq*aq*integ(p2,q-2))
            row.append(val)
        bs.append(row)
    # B is symmetric positive, hence operator norm <= max absolute row sum.
    rows=[sum((abs(v) for v in row),arb(0)) for row in bs]
    upper=max(v.upper() for v in rows)
    return {'schema':'ipm-hermite-gram-v1','status':'RIGOROUS_ARB_GRAM_ONLY','q':str(q),'alpha':str(alpha),'bits':bits,'basis':[list(x) for x in ids],'definition':'phi_mn^alpha(x,y)=alpha h_m(alpha*x)h_n(alpha*y), h_n normalized physicists Hermite function; m even,n odd','B':[[packet(v) for v in row] for row in bs],'operator_norm_upper_by_row_sum':str(upper),'moment_count':moment.cache_info().currsize,'warning':'No profile-dependent A entries, finite-rank tail or IPM closure assertion is made.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--degree',type=int,default=7);p.add_argument('--alpha',default='1');p.add_argument('--bits',type=int,default=256);p.add_argument('--output',type=Path)
    args=p.parse_args();r=build(args.degree,Q(args.alpha),args.bits)
    if args.output:args.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='B'},indent=2))
if __name__=='__main__':main()
