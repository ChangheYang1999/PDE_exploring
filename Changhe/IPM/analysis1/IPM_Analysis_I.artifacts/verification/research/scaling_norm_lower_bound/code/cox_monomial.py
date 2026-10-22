"""Independent path A: binary64 decode, Cox basis, monomial square integrals."""
from fractions import Fraction
import hashlib,json
from flint import fmpq as Q, fmpq_poly as P, fmpq_mat as Mat

def decode(s):
    f=float.fromhex(s)
    assert f.hex()==s or (f==0 and s in ['0x0.0p+0','-0x0.0p+0'])
    q=Fraction.from_float(f)
    return Q(q.numerator,q.denominator)

def basis(knots,span,degree=7):
    a=knots[span];d=knots[span+1]-a;assert d>0
    row={span:P([1])}
    for p in range(1,degree+1):
        out={}
        for i in range(span-p,span+1):
            z=P([])
            den=knots[i+p]-knots[i]
            if den and i in row:z+=P([(a-knots[i])/den,d/den])*row[i]
            den=knots[i+p+1]-knots[i+1]
            if den and i+1 in row:z+=P([(knots[i+p+1]-a)/den,-d/den])*row[i+1]
            out[i]=z
        row=out
    return [row[i] for i in range(span-degree,span+1)]

def modal(knots,S,span,degree=7):
    bs=basis(knots,span,degree)
    M=len(S);assert M and all(len(v)==len(knots)-degree-1 for v in S)
    left=Mat([[bs[j][i] for j in range(degree+1)] for i in range(degree+1)])
    right=Mat([[S[m][span-degree+j] for m in range(M)] for j in range(degree+1)])
    out=left*right
    return [P([out[i,m] for i in range(degree+1)]) for m in range(M)]

def angular(S):
    M=len(S);assert M>0
    H=[P([]) for j in range(M+1)]
    for m,p in enumerate(S):
        if m==0:
            H[0]+=p/4;H[1]+=p/4
        else:
            for n in [1+2*m,1-2*m,3+2*m,3-2*m]:
                assert n and n%2
                H[(abs(n)-1)//2]+=p*(Q(1,8) if n>0 else Q(-1,8))
    return H

def square_integral(p):
    z=p*p
    return sum((z[i]/(i+1) for i in range(len(z))),Q(0))

def digest(H,degree=7):
    a=[[str(p[i]) for i in range(degree+1)] for p in H]
    return hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()

def compute(knots,S,span):
    a=knots[span];b=knots[span+1];d=b-a;assert d>0
    H=angular(modal(knots,S,span))
    result=Q(0)
    for j,p in enumerate(H):
        B=-2*p-p.derivative()/d
        C=3*B+B.derivative()/d
        result+=(1+(2*j+1)**2)*square_integral(B)+square_integral(C)
    result*=d;assert result>=0
    return {'a':str(a),'b':str(b),'Q':str(result),'density_coefficients_sha256':digest(H),'density_coefficients':8*len(H)}
