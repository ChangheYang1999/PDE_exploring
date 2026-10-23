"""Exact finite-polynomial P=2 axis inverse and logarithmic constant; result234 proof."""
import mpmath as mp
from hydrostatic_axis_tail_series import coordinate, horner

def at(a,j):return a[j] if j<len(a) else mp.mpf(0)

def constants(C,H,k):
    C=mp.mpf(C);k1,k2=at(k,1),at(k,2);h1,h2,h3=(at(H,j)for j in (1,2,3))
    b=C*(k2-k1/4);terms=[j*k[j]*mp.beta(j-2,mp.mpf('1.5'))for j in range(3,len(k))]
    m=C*(k1*(-mp.mpf('.5')-mp.log(2))+k2*(4*mp.log(2)-3)+mp.fsum(terms))-b*mp.log(C)
    K=h1*mp.sqrt(C);Q=k1*mp.sqrt(C)/2;c2=C*(h2-h1/4);c3=C**mp.mpf('1.5')*(h3-h2/2-h1/32);r2=-c2+2*K*Q
    return dict(K=K,Q=Q,c2=c2,c3=c3,B_log=b,M=m,r2=r2,
                residual_sqrt=r2/(2*K) if K else None,residual_log=b/4,
                residual_constant=m/4-c3/K-r2*(2*c2+r2)/(4*K*K)if K else None)

def regular_integrand(k,v):
    s=mp.sqrt(1-v)
    return -at(k,1)/(2*(1+s)**2)-2*at(k,2)/(1+s)+s*horner([j*k[j]for j in range(3,len(k))],v)

def integral_I0(k):return mp.quad(lambda v:regular_integrand(k,v),[0,mp.mpf('.5'),1])

def beta_I0(k):
    return at(k,1)*(mp.mpf('.5')-mp.log(2))+2*at(k,2)*(2*mp.log(2)-2)+mp.fsum(j*k[j]*mp.beta(j-2,mp.mpf('1.5'))for j in range(3,len(k)))

def velocity(C,k,y,N=128,I0=None):
    C=mp.mpf(C);y=mp.mpf(y)
    if N<2 or at(k,0)!=0:raise ValueError('N>=2 and k(0)=0 required')
    w=coordinate(2,C,y);I0=beta_I0(k)if I0 is None else I0
    bn=[mp.mpf(1)]
    for n in range(1,N+1):bn.append(bn[-1]*(n-mp.mpf('1.5'))/n)
    powers=[w**n for n in range(N+len(k)+1)];terms=[];bounds=[]
    for j in range(1,len(k)):
        terms.append(j*k[j]*mp.fsum(bn[n]*powers[j+n-2]/(j+n-2)for n in range(max(0,3-j),N+1)))
        bounds.append(abs(j*k[j])*powers[j+N-1]/(j+N-1))
    A=2*at(k,2)-at(k,1)/2
    ans=y*horner(k,w)+C*(at(k,1)*(1/w-1)-A*mp.log(w)+I0-mp.fsum(terms))
    return dict(w=w,V2=ans,remainder_bound=C*mp.fsum(bounds)/(1-w))

def axis_jet(C,H,y):
    y=mp.mpf(y);w=coordinate(2,C,y);h=horner(H,w);dh=horner([j*H[j]for j in range(1,len(H))],w)
    return y*h,h-w*(1-w)/(2-mp.mpf('1.5')*w)*dh

def residual(C,H,k,y,N=128,I0=None):
    y=mp.mpf(y);g,gy=axis_jet(C,H,y);v=velocity(C,k,y,N,I0);a=(2*y+v['V2'])*gy;R=a-g;nf=abs(a)+abs(g)
    return dict(y=y,g=g,gy=gy,V2=v['V2'],w=v['w'],R=R,Nf=nf,y_signed_R_Nf=y*R/nf if nf else None,remainder_bound=v['remainder_bound'])
