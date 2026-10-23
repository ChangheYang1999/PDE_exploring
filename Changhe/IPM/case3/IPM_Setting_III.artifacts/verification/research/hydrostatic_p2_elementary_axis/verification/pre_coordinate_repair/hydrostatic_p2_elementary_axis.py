"""Result240: exact rational elementary axis primitive, independent of the tail series."""
from fractions import Fraction as F
from math import comb
import mpmath as mp

def rational_polynomial(k):
    """Odd polynomial P(t), exactly, with ascending coefficient order."""
    k=list(map(F,k));d=len(k)-1
    out=[F(0)]*max(2,2*d-2)
    if len(k)>2:out[1]=-3*k[2]
    for j in range(3,len(k)):
        for m in range(j-2):
            v=k[j]*(-1)**m*comb(j-3,m)
            out[2*m+1]+=v/F(2*m+1)
            out[2*m+3]+=3*v/F(2*m+3)
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def horner(a,x):
    z=mp.mpf(0)
    for c in reversed(a):z=z*x+c
    return z

def coordinate(C,y):
    """Positive root w, solved monotonically in log(w), no near-one t subtraction."""
    C=mp.mpf(C);y=mp.mpf(y)
    if y==0:return mp.mpf(1)
    if y<0 or C<=0:raise ValueError('C>0,y>=0 required')
    # Inverting in t is well conditioned near the origin; w near infinity.
    if y<C:
        t=min(mp.mpf('.5'),y/C)
        for unused in range(100):
            dt=(C*t/(1-t*t)**2-y)/(C*(1+3*t*t)/(1-t*t)**3)
            tn=t-dt
            if not 0<=tn<1:tn=t/2
            if abs(tn-t)<=mp.eps*max(mp.mpf(1),abs(tn))*8:return 1-tn*tn
            t=tn
    w=min(mp.mpf('.75'),mp.sqrt(C/y))
    for unused in range(100):
        f=mp.log(C)+mp.log1p(-w)/2-2*mp.log(w)-mp.log(y)
        wp=w-f/(-1/(2*(1-w))-2/w)
        if not 0<wp<1:wp=w/2 if wp<=0 else (1+w)/2
        if abs(wp-w)<=mp.eps*abs(wp)*8:return wp
        w=wp
    raise ArithmeticError('coordinate Newton did not converge')

class Axis:
    def __init__(self,C,H,k,P=None):
        self.C=mp.mpf(C);self.H=list(map(mp.mpf,H));self.k=list(map(mp.mpf,k))
        self.P=list(map(mp.mpf,P)) if P is not None else None
        if self.P is None:raise ValueError('supply exact precomputed polynomial P')
        if self.H[0]!=0 or self.k[0]!=0:raise ValueError('zero constants required')
        self.H1=[j*self.H[j]for j in range(1,len(H))]
        self.H2=[j*self.H1[j]for j in range(1,len(self.H1))]
    def evaluate(self,y):
        y=mp.mpf(y);w=coordinate(self.C,y);t=mp.sqrt(1-w)
        k1=self.k[1]if len(self.k)>1 else mp.mpf(0);k2=self.k[2]if len(self.k)>2 else mp.mpf(0)
        # atanh(t)=log(1+t)-log(w)/2 prevents catastrophic 1-t subtraction.
        V=self.C*(2*k1*t/w+(4*k2-k1)*(mp.log1p(t)-mp.log(w)/2)+horner(self.P,t))
        H=horner(self.H,w);H1=horner(self.H1,w);H2=horner(self.H2,w);k=horner(self.k,w)
        d=2-mp.mpf('1.5')*w;a=w*(1-w)/d;ap=((1-2*w)*d+mp.mpf('1.5')*w*(1-w))/d**2
        G=y*H;G1=H-a*H1
        G2=((1-ap)*H1-a*H2)*(-a/y) if y else mp.mpf(0)
        W=2*y+V;T=W*G1;R=T-G;R1=(1+k)*G1+W*G2
        nf=abs(T)+abs(G);nv=abs(G)+abs(y*G1)+abs(V*G1)
        return dict(y=y,w=w,G=G,G1=G1,G2=G2,k=k,V=V,R=R,R1=R1,Nf=nf,Nv=nv,R_Nf=abs(R)/nf if nf else None,R_Nv=abs(R)/nv if nv else None,stationary=R1*G-R*G1,positive_denominator=bool(G>0 and T>0))
