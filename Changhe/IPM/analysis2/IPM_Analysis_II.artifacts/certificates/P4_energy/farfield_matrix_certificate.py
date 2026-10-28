"""Independent exterior M certificate, exact Fourier coefficients and absolute tails.
No floating trigonometric grid or sibling evaluator is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
from flint import arb, ctx
import json
ctx.prec=320
BASE=Path(__file__).resolve().parents[2]

def A(v):
    v=Q(v); return arb(v.numerator)/arb(v.denominator)

def add(T, kind, n, a):
    if n<0:
        n=-n
        if kind=='s': a=-a
    if not a or (kind=='s' and not n): return
    T[kind,n]=T.get((kind,n),Q(0))+a
    if not T[kind,n]: del T[kind,n]

def differentiate(T, s, axis):
    out={}
    for (kind,n), a in T.items():
        if axis=='x':
            add(out,kind,n+1,a*(s-n)/2)
            add(out,kind,n-1,a*(s+n)/2)
        elif kind=='c':
            add(out,'s',n+1,a*(s-n)/2)
            add(out,'s',n-1,-a*(s+n)/2)
        else:
            add(out,'c',n-1,a*(s+n)/2)
            add(out,'c',n+1,-a*(s-n)/2)
    return out

def binomial(v,k):
    b=Q(1)
    for i in range(k): b*= (v-i)/(i+1)
    return b

def cosine_bernstein_lower(T, depth=6):
    """Exact lower bound via z=cos(2theta), Bernstein subdivision on [-1,1]."""
    assert all(kind=='c' and n%2==0 for kind,n in T)
    degree=max(n//2 for kind,n in T)
    cheb=[[Q(1)],[Q(0),Q(1)]]
    for n in range(2,degree+1):
        pn=[Q(0)]*(n+1)
        for j,v in enumerate(cheb[-1]): pn[j+1]+=2*v
        for j,v in enumerate(cheb[-2]): pn[j]-=v
        cheb.append(pn)
    p=[Q(0)]*(degree+1)
    for (kind,n),v in T.items():
        for j,x in enumerate(cheb[n//2]): p[j]+=v*x
    # z=2u-1.
    power=[sum((p[k]*comb(k,j)*2**j*(-1)**(k-j) for k in range(j,degree+1)),Q(0)) for j in range(degree+1)]
    b=[sum((power[k]*Q(comb(j,k),comb(degree,k)) for k in range(j+1)),Q(0)) for j in range(degree+1)]
    leaves=[b]
    for level in range(depth):
        next_leaves=[]
        for row in leaves:
            tri=[row]
            while len(tri[-1])>1: tri.append([(u+v)/2 for u,v in zip(tri[-1],tri[-1][1:])])
            next_leaves.extend([[r[0] for r in tri], [r[-1] for r in reversed(tri)]])
        leaves=next_leaves
    return min(x for row in leaves for x in row)

def run(state, cut=6):
    d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
    c=Q(d['exact_parameters']['cl']); gamma=1/c; delta=1-gamma
    coeff=list(map(Q,d['canonical_coefficients']))
    p=[(3+gamma-j*delta)/2 for j in range(4)]
    assert all(0<pj<2 for pj in p)
    # A universal B=26 dominates |p_j-k| for all checkpoint indices.
    assert all(abs(p[j]-k)<26 for j,m,k in d['canonical_order'])
    absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,d['canonical_order']) if jj==j),Q(0)) for j in range(4)]
    sectors={}
    rho_y_leading_lower=None
    for j in range(4):
        for q in range(cut+1):
            T={}
            for v,(jj,m,k) in zip(coeff,d['canonical_order']):
                if jj==j: add(T,'c',2*m,v*binomial(p[j]-k,q))
            s=2*p[j]-2*q
            row={}
            polys={}
            for label,axes in [('chi22','xxyy'),('chi04','yyyy'),('chi31','xxxy')]:
                U=T
                for i,axis in enumerate(axes): U=differentiate(U,s-i,axis)
                row[label]=sum(map(abs,U.values()),Q(0))
                polys[label]=U
            ry={}
            for label in ('chi22','chi04'):
                for (kind,n),v in polys[label].items(): add(ry,kind,n,-v)
            row['rho_y']=sum(map(abs,ry.values()),Q(0))
            if j==0 and q==0:
                rho_y_leading_lower=cosine_bernstein_lower(ry)
            sectors[j,q]=row
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,
         'input_sha256':d['canonical_serialization_sha256'],'Q':cut,'B':26,'leading_rho_y_Bernstein_lower_exact':str(rho_y_leading_lower.numerator)+'/'+str(rho_y_leading_lower.denominator),'exterior':{}}
    for R in (100,300,1000,3000,10000):
        r=A(R); q0=cut+1
        ratio=A(Q(q0+26,q0+1)*Q(q0+15,q0+14)**4)/r**2
        assert ratio<1
        common=A(comb(q0+25,q0)*(2*q0+28)**4)*r**(-2*q0)/(1-ratio)
        tail=common*sum((A(absj[j])*r**A(-j*delta) for j in range(4)),arb(0))
        bounds={}
        for label in ('chi22','chi04','chi31'):
            value=sum((A(row[label])*r**A(-j*delta-2*q) for (j,q),row in sectors.items()),arb(0))
            bounds[label]=value+tail
        factor=r**A(gamma-1)
        row1=(2*bounds['chi22']+bounds['chi04']+bounds['chi31'])*factor
        row2=(bounds['chi22']+bounds['chi31'])*factor
        # row1 dominates row2 term by term.
        lo=2*A(c)+1-row1
        rho_lower=A(rho_y_leading_lower)-2*tail-sum((A(row['rho_y'])*r**A(-j*delta-2*q) for (j,q),row in sectors.items() if (j,q)!=(0,0)),arb(0))
        positive_rho_lo=None
        if rho_lower>0: positive_rho_lo=2*A(c)+1-row2
        out['exterior'][str(R)]={'lambda_min_lower_arb':lo.str(60),
            'common_tail_coefficient_arb':tail.str(40),
            'derivative_coefficients_arb':{k:v.str(40) for k,v in bounds.items()},
            'geometric_ratio_arb':ratio.str(40),
            'rho_y_lower_coefficient_arb':rho_lower.str(50),
            'positive_rho_improved_lambda_lower_arb':None if positive_rho_lo is None else positive_rho_lo.str(60)}
        print(state,R,'lower',lo.str(20),'rho_y lower',rho_lower.str(12),'improved',None if positive_rho_lo is None else positive_rho_lo.str(20),flush=True)
    Path(__file__).with_name(f'state{state:03d}_farfield_matrix.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    for state in (88,131): run(state)
