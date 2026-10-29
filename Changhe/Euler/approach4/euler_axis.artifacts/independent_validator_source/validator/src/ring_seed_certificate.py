"""Exact-rational checker for the decaying ring seed's global zero criterion.

The proof is research/decaying_ring_seed/PROOF.md. Decimal input parameters
are exact rationals. This checker neither fits parameters nor samples H.
"""
from fractions import Fraction as F
import json

def load_exact(path):
    with open(path) as f:return json.load(f,parse_float=F)

def parameters(row):
    c,A,b,a=map(F,[row['c'],row['Finf'],row['b'],row['rho1']]);n=row['n']
    if not isinstance(n,int) or isinstance(n,bool) or n<3:raise ValueError('n must be an integer >=3')
    B=c+(1+c)/2-A
    if not F(1,2)<c<F(3,4) or min(A,B,a,b)<=0:raise ValueError('outside the theorem hypotheses')
    return c,A,B,b,a,n,F(1)/(6*c)

def power_bound_valid(t,y,p,lower):
    t,y,p=F(t),F(y),F(p)
    if t<=0 or y<1 or p<=0:return False
    lhs=t.numerator**p.denominator*y.numerator**p.numerator
    rhs=t.denominator**p.denominator*y.denominator**p.numerator
    return lhs<=rhs if lower else lhs>=rhs

def S(x,n):return (1-(n-1)*x)/(1+x)**2

def cell_lower_bound(row,l,h,t):
    c,A,B,b,a,n,p=parameters(row);l,h,t=map(F,[l,h,t])
    if l<0 or h<=l:raise ValueError('invalid cell')
    u=(h/b)**3;y=1+u
    if not power_bound_valid(t,y,p,True):raise ValueError('false fractional-power lower bound')
    xl,xh=(l/a)**n,(h/a)**n;xstar=F(n+1,n-1)
    vals=[S(xl,n),S(xh,n)]
    if xl<=xstar<=xh:vals.append(S(xstar,n))
    return c+2*A*t*(1-3*p*u/(1+u))+2*B*min(vals)

def F_interval(row,rho,power_lower,power_upper):
    c,A,B,b,a,n,p=parameters(row);rho=F(rho);lo,hi=F(power_lower),F(power_upper)
    y=1+(rho/b)**3
    if rho<0 or not power_bound_valid(lo,y,p,True) or not power_bound_valid(hi,y,p,False) or lo>hi:
        raise ValueError('invalid potential power enclosure')
    return A*lo+B/(1+(rho/a)**n),A*hi+B/(1+(rho/a)**n)

def check_case(row,cert):
    c,A,B,b,a,n,p=parameters(row);cutoff=F(cert['cutoff'])
    if cutoff<=0 or (cutoff/a)**n<4*B*(n-1)/c:raise ValueError('uncertified infinite tail')
    end=F(0);smallest=None
    for index,cell in enumerate(cert['cells']):
        l,h=F(cell['left']),F(cell['right'])
        if l!=end:raise ValueError('gap or overlap in interval cover')
        bound=cell_lower_bound(row,l,h,cell['power_lower'])
        if bound<=0:raise ValueError('H not certified positive')
        smallest=bound if smallest is None else min(smallest,bound);end=h
    if end!=cutoff or smallest is None:raise ValueError('interval cover does not reach cutoff')
    bracket=cert['root_bracket'];l,h=F(bracket['left']),F(bracket['right'])
    if not 0<l<h:raise ValueError('invalid root bracket')
    fl=F_interval(row,l,bracket['left_power_lower'],bracket['left_power_upper'])
    fh=F_interval(row,h,bracket['right_power_lower'],bracket['right_power_upper'])
    if fl[0]<=c or fh[1]>=c:raise ValueError('root not strictly bracketed')
    return dict(cells=len(cert['cells']),minimum_certified_H_lower=str(min(smallest,c/2)),
                minimum_certified_H_lower_float=float(min(smallest,c/2)),root_rho_lower=str(l),root_rho_upper=str(h),
                cutoff=str(cutoff),zero_count_in_closed_half_plane=2,
                scope='Exact rational decimal parameters; two zeros, with the nonzero ring bracketed. Exact resonance and Euler equations are not certified.')
