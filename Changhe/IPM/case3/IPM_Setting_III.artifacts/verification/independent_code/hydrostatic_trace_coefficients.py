"""Independent full-tail hydrostatic trace moments, result208 PROOF.md.
Only mpmath arithmetic; no producer modules or numerical differentiation.
"""
from fractions import Fraction
import mpmath as mp

def exactmp(v):
    if isinstance(v,Fraction):return mp.mpf(v.numerator)/v.denominator
    if isinstance(v,float):
        a,b=v.as_integer_ratio();return mp.mpf(a)/b
    return mp.mpf(v)

def angular_polynomials(count):
    out=[[1]]
    if count>1:out.append([-1,2])
    for k in range(1,count-1):
        a=[0]*(k+2)
        for j,t in enumerate(out[-1]):a[j]-=2*t;a[j+1]+=4*t
        for j,t in enumerate(out[-2]):a[j]-=t
        out.append(a)
    return out[:count]

def monomials(modes,pref=1):
    b=list(map(exactmp,modes));a=[mp.mpf(0)]*len(b)
    for v,T in zip(b,angular_polynomials(len(b))):
        for j,t in enumerate(T):a[j]+=v*t
    return [exactmp(pref)*v for v in a]

def weights(p,count):
    p=exactmp(p);J=mp.sqrt(mp.pi)*mp.gamma(1-p/2)/(2*mp.gamma((3-p)/2))
    I=[(1-p)*J/(p*(p+2)),-J/p,J/(3-p)]
    for j in range(2,count-1):I.append(I[-1]*(2*j-p-2)/(2*j+1-p))
    return I[:count]

def moments(a,p):
    p=exactmp(p);a=list(map(exactmp,a));I=weights(p,len(a));K=a[0];Q=(p-1)*K+(2*a[1]if len(a)>1 else 0)
    return dict(K=K,Q=Q,Cp=(p+1)*(p+2)*mp.fsum(v*w for v,w in zip(a,I)))

def Fq(s,a,p):
    s=exactmp(s);p=exactmp(p);rr=1+s*s;fv=[];qv=[]
    for j,a0 in enumerate(a):
        a0=exactmp(a0);m=2*j;t=p-1-2*j;h=rr**(t/2)
        fv.append(a0*s*h)
        qv.append(a0*s*h*(m*(m-1)+t*(2*m+1)/rr+t*(t-2)/(rr*rr)))
    return mp.fsum(fv),mp.fsum(qv)

def expansion(a,p,count):
    p=exactmp(p);d=[mp.mpf(0)]*count
    for j,a0 in enumerate(a):
        b=exactmp(a0);alpha=(p-1)/2-j
        for n in range(j,count):
            d[n]+=b;b*= (alpha-(n-j))/(n-j+1)
    return d

def integral_check(a,p,S=4,terms=100):
    p=exactmp(p);S=exactmp(S);d=expansion(a,p,terms);K=d[0];Q=2*d[1]
    loF=mp.quad(lambda s:s*Fq(s,a,p)[0],[0,1,S])
    loq=mp.quad(lambda s:s*Fq(s,a,p)[1],[0,1,S])
    tailF=mp.fsum(d[n]*S**(p+2-2*n)/(2*n-p-2)for n in range(2,terms))
    tailq=mp.fsum(2*n*(2*n-1)*d[n]*S**(p+2-2*n)/(2*n-p-2)for n in range(2,terms))
    return dict(moment=(p+1)*(p+2)*(loF-K*S**(p+2)/(p+2)-Q*S**p/(2*p)+tailF),q=loq-Q*S**p/p+tailq,tailF=tailF,tailq=tailq)

def trace_at(theta,modes,pref=1):
    theta=exactmp(theta);return exactmp(pref)*mp.sin(theta)*mp.fsum(exactmp(v)*mp.cos(2*k*theta)for k,v in enumerate(modes))

def stored_endpoint_data(q):
    # The shifted Chebyshev coordinate equals1 at t=1 exactly.
    b=[];bp=[]
    for k,row in enumerate(q.coeff):
        cc=[Fraction(float(v))for v in row]
        b.append(sum(cc,Fraction(0)))
        factor=2/(1-Fraction(float(q.tk[k])))if q.basis=='local'else Fraction(1)
        bp.append(factor*sum((j*j*v for j,v in enumerate(cc)),Fraction(0)))
    return b,bp
