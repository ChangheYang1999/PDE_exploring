"""Validated integer Sobolev energies for (F,2xF,2yF).

F=sum_n f_n(r) sin(n theta), odd positive n. Orthogonality cancels all
cross terms between neighboring n in the two coordinate components.
All coefficients, Taylor derivative remainders and panel geometry are Arb.
"""
import math
from flint import arb

def derivative_cover(p,d,h,H,R,K):
    """Cover f^(d) on |r-center|<=h via degree K Taylor and Cauchy."""
    assert 0<=d<=3 and K>=2*d and h>=0 and R>0
    z=h/R
    assert z<arb(1)/2
    v=arb(0,h.abs_upper());out=arb(0)
    for k in range(K,d-1,-1):
        out=out*v+p[k]*(math.factorial(k)//math.factorial(k-d))
    factor=math.prod(range(K+2-d,K+2)) if d else 1
    tail=H*factor/R**d*z**(K+1-d)/(1-2*z)
    return out+arb(0,tail.abs_upper()),tail

def panel_energy(series,c,h,H,R,K,raw=False):
    """Nonnegative containing upper energy integrals on [c-h,c+h]."""
    c,h=arb(c),arb(h);radius=c+arb(0,h.abs_upper());assert radius>0
    E2=arb(0);E3=arb(0);rows=[]
    tails=[arb(0)]*4
    for n,p in sorted(series.items()):
        data=[derivative_cover(p,d,h,H,R,K)for d in range(4)]
        f,f1,f2,f3=[x[0]for x in data]
        tails=[max(a,x[1].abs_upper())for a,x in zip(tails,data)]
        g=f-f2-f1/radius+n*n*f/radius**2
        g1=f1-f3-f2/radius+(1+n*n)*f1/radius**2-2*n*n*f/radius**3
        s2=g*g;s3=s2+g1*g1+n*n*g*g/radius**2
        for sign in [-1,1]:
            a=radius*g-2*f1+sign*2*n*f/radius
            a1=g+radius*g1-2*f2+sign*2*n*(f1/radius-f/radius**2)
            s2+=2*a*a
            s3+=2*(a*a+a1*a1+(n+sign)**2*a*a/radius**2)
        e2=(2*h*arb.pi()*radius*s2).upper()
        e3=(2*h*arb.pi()*radius*s3).upper()
        E2+=e2;E3+=e3
        if raw:rows.append({'n':n,'derivative_enclosures':[[str(v.lower().fmpq()),str(v.upper().fmpq())]for v,t in data],'E2_upper':str(e2.fmpq()),'E3_upper':str(e3.fmpq())})
    out={'E2_upper':str(E2.upper().fmpq()),'E3_upper':str(E3.upper().fmpq()),'derivative_remainder_uppers':[str(t.upper().fmpq())for t in tails]}
    if raw:out['modal_rows']=rows
    return out
