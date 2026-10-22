"""Independent path B: literal hex, de Boor modal recurrence, Legendre squares."""
import hashlib,json,re
from flint import fmpq as Q, fmpq_poly as P
HEX=re.compile(r'(-?)0x([0-9a-f]+)\.([0-9a-f]+)p([+-]?[0-9]+)\Z')

def decode(s):
    m=HEX.fullmatch(s);assert m,('invalid finite hex',s)
    sign,whole,fraction,exponent=m.groups()
    n=int(whole+fraction,16)*(-1 if sign else 1);e=int(exponent)-4*len(fraction)
    return Q(n*(1<<e)) if e>=0 else Q(n,1<<(-e))

def modal(knots,S,span,degree=7):
    lo=knots[span];width=knots[span+1]-lo;assert width>0
    out=[]
    for coeff in S:
        assert len(coeff)==len(knots)-degree-1
        work=[P([coeff[span-degree+j]]) for j in range(degree+1)]
        for r in range(1,degree+1):
            for j in range(degree,r-1,-1):
                i=span-degree+j;den=knots[span+j+1-r]-knots[i];assert den>0
                t=P([(lo-knots[i])/den,width/den])
                work[j]=(1-t)*work[j-1]+t*work[j]
        out.append(work[degree])
    return out

def angular(S):
    M=len(S)
    def A(i):
        if i==0:return S[0]
        return S[abs(i)]/2 if abs(i)<M else P([])
    return [(A(j)-A(j+1)+A(j-1)-A(j+2))/4 for j in range(M+1)]

def legendre(degree=7):
    ans=[P([1])]
    if degree:
        z=P([-1,2]);ans.append(z)
        for l in range(1,degree):ans.append(((2*l+1)*z*ans[-1]-l*ans[-2])/(l+1))
    return ans

LEG=legendre()
def square_integral(p):
    assert p.degree()<=7
    rem=P(p);result=Q(0)
    for l in range(7,-1,-1):
        q=rem[l]/LEG[l][l]
        rem-=q*LEG[l]
        result+=q*q/(2*l+1)
    assert not rem and result>=0
    return result

def digest(H,degree=7):
    h=hashlib.sha256();h.update(b'[')
    for j,p in enumerate(H):
        if j:h.update(b',')
        h.update(b'[')
        for k in range(degree+1):
            if k:h.update(b',')
            h.update(json.dumps(str(p[k])).encode())
        h.update(b']')
    h.update(b']');return h.hexdigest()

def compute(knots,S,span):
    a=knots[span];b=knots[span+1];d=b-a;assert d>0
    H=angular(modal(knots,S,span));result=Q(0)
    for j in reversed(range(len(H))):
        p=H[j];B=-(2*p+p.derivative()/d);C=B.derivative()/d+3*B
        result+=square_integral(C)+((2*j+1)**2+1)*square_integral(B)
    result*=d;assert result>=0
    return {'a':str(a),'b':str(b),'Q':str(result),'density_coefficients_sha256':digest(H),'density_coefficients':8*len(H)}
