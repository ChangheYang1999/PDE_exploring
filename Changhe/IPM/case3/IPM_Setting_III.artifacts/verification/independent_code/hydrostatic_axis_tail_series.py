"""Independent complete axis inverse via finite polynomial/incomplete-beta series."""
import mpmath as mp
from fractions import Fraction as F

def exactmp(t):
    t=F(t);return mp.mpf(t.numerator)/t.denominator

def horner(a,w):
    out=mp.mpf(0)
    for v in reversed(a):out=out*w+v
    return out

def coordinate(P,C,y):
    P=mp.mpf(P);C=mp.mpf(C);y=mp.mpf(y)
    if not y>0:raise ValueError('positive axis only')
    u=mp.log(min(mp.mpf('.5'),(C/y)**(1/P)))
    for _ in range(100):
        w=mp.exp(u);value=mp.log(C/y)+mp.log1p(-w)/2-P*u;der=-P-w/(2*(1-w));nxt=u-value/der
        if nxt>=0:nxt=u/2
        if abs(nxt-u)<mp.eps*16*(1+abs(u)):return mp.exp(nxt)
        u=nxt
    raise ArithmeticError('log-w inversion did not converge')

def moment(k,P,C):
    return C*mp.fsum(j*k[j]*mp.beta(j-P,mp.mpf('1.5'))for j in range(1,len(k)))

def velocity(P,C,k,y,N=96,m0=None):
    w=coordinate(P,C,y);m0=moment(k,P,C)if m0 is None else m0
    bn=[mp.mpf(1)]
    for n in range(1,N+1):bn.append(bn[-1]*(n-mp.mpf('1.5'))/n)
    powers=[w**n for n in range(N+1)];terms=[];bounds=[]
    for j in range(1,len(k)):
        a=j-P;terms.append(j*k[j]*w**a*mp.fsum(bn[n]*powers[n]/(a+n)for n in range(N+1)))
        bounds.append(abs(j*k[j])*w**(a+N+1)/(a+N+1))
    ans=y*horner(k,w)+m0-C*mp.fsum(terms);bound=C/(1-w)*mp.fsum(bounds)
    return dict(w=w,V2=ans,remainder_bound=bound)

def axis_jet(P,C,H,y):
    w=coordinate(P,C,y);hh=horner(H,w);dh=horner([j*H[j]for j in range(1,len(H))],w)
    return y*hh,hh-w*(1-w)/(P+(mp.mpf('.5')-P)*w)*dh

def residual(P,C,H,k,c,y,N=96,m0=None):
    yy=mp.mpf(y);g,gy=axis_jet(P,C,H,yy);v=velocity(P,C,k,yy,N,m0);a=(c*yy+v['V2'])*gy;R=a-g;nf=abs(a)+abs(g)
    return dict(y=yy,g=g,gy=gy,V2=v['V2'],w=v['w'],R=R,Nf=nf,y_signed_R_Nf=yy*R/nf,remainder_bound=v['remainder_bound'])
