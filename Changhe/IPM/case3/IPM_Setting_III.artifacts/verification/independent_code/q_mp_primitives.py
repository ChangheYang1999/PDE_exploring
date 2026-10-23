"""Canonical Q inverse through finite compact-coordinate primitives.

Derivation precedes this code: research/q_full_inverse_primitives/PROOF.md.
No producer evaluator, inverse matrix or differentiation code is imported.
Construct MPQPrimitives inside the requested working-precision context.
"""
from fractions import Fraction as F
import math
import mpmath as mp
from q_high_precision_density import MPQDensity


def fraction(v):
    if isinstance(v,F):return v
    if isinstance(v,(str,int)):return F(v)
    return F(float(v))


def mf(v):
    v=fraction(v);return mp.mpf(v.numerator)/v.denominator


def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p


def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for k,v in enumerate(a):c[k]+=v
    for k,v in enumerate(b):c[k]+=v
    return trim(c)


def scale(a,c):return trim([v*c for v in a])
def shift(a):return [F(0)]+list(a)

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)


def chebyshev_power_rows(N,reverse=False):
    """T_n(2s-1), or T_n(1-2w), from a closed integer formula."""
    rows=[]
    for n in range(N+1):
        row=[(-1)**n if not reverse else 1]
        for k in range(1,n+1):
            numerator=n*4**k*math.comb(n+k,2*k);denominator=n+k
            assert numerator%denominator==0
            row.append((-1)**(k+(0 if reverse else n))*(numerator//denominator))
        rows.append(row)
    return rows


def convert(cc,rows):
    out=[F(0)]*len(cc)
    for n,v in enumerate(cc):
        for k,w in enumerate(rows[n]):out[k]+=v*w
    return trim(out)


def horner(cc,x):
    value=mp.mpf(0)
    for c in reversed(cc):value=value*x+c
    return value


def guard_digits(N,M,kappa):
    # Conservative numerical guard, not a certified error estimate.
    return 40+2*N+2*M+math.ceil((N+2)*math.log10(2+2*float(kappa)))


class MPQPrimitives:
    def __init__(self,coeff,L,kappa,ell):
        self.raw_coeff=[[fraction(v)for v in row]for row in coeff]
        self.raw_L=fraction(L);self.raw_kappa=fraction(kappa);self.raw_ell=fraction(ell)
        assert self.raw_L>0 and self.raw_kappa>1 and self.raw_coeff
        self.M=len(coeff);self.N=max(map(len,coeff))-1
        self.L=mf(self.raw_L);self.kappa=mf(self.raw_kappa);self.ell=mf(self.raw_ell)
        self.coeff=[[mf(v)for v in row]for row in self.raw_coeff]
        self.density=MPQDensity.__new__(MPQDensity)
        self.density.coeff=self.coeff;self.density.L=self.L
        self.density.kappa=self.kappa;self.density.ell=self.ell
        ps=chebyshev_power_rows(self.N);pw=chebyshev_power_rows(self.N,reverse=True)
        Bs=[convert(row,ps)for row in self.raw_coeff]+[[F(0)]]
        Bw=[convert(row,pw)for row in self.raw_coeff]+[[F(0)]]
        Hs=[];Hw=[]
        for j in range(self.M):
            ds=add(Bs[j],scale(shift(Bs[j+1]),-F(1,2) if j==0 else -1))
            dw=add(Bw[j],scale(add(Bw[j+1],scale(shift(Bw[j+1]),-1)),-F(1,2) if j==0 else -1))
            if j:ds=scale(ds,F(1,2));dw=scale(dw,F(1,2))
            Hs.append(mul(ds,[F(1),2*self.raw_kappa-1]))
            Hw.append(mul(dw,[2*self.raw_kappa,1-2*self.raw_kappa]))
        Hw.append([F(0)])
        self.Hs=[[mf(v)for v in row]for row in Hs]
        self.Hw=[[mf(v)for v in row]for row in Hw]
        self.alpha_w=[];self.alpha_e=[];self.K=[];self.beta_w=[]
        for j in range(1,self.M+1):
            K=2*self.raw_kappa*(j+1);Kb=2*self.raw_kappa*(j-1)
            f=mul([F((-1)**k*math.comb(2*j-1,k))for k in range(2*j)],Hw[j-1])
            self.alpha_w.append([mf(v)for v in f]);self.alpha_e.append([mf(F(k+1)-K)for k in range(len(f))]);self.K.append(mf(K))
            self.beta_w.append([mf(v/(Kb+k+1))for k,v in enumerate(Hw[j])])
        self.a=mf(sum(((-1)**k*v for k,v in enumerate(self.raw_coeff[0])),F(0)))
        self.c=-self.a/4+horner(self.beta_w[0],mp.mpf(1))/2
        self.delta=self.ell+self.c-1

    def moments(self,s,w):
        aa=[];bb=[]
        for j in range(1,self.M+1):
            K=self.K[j-1]
            if s<=mp.mpf('.5'):
                hk=self.Hs[j-1];top=2*j+len(hk)-1
                z=mp.exp(K*mp.log(w))*mp.hyp2f1(K,top,top+1,s)/top
                zz={top:z}
                for n in range(top-1,2*j-1,-1):
                    z=((n+1-K)*s*z+w)/n;zz[n]=z
                a=mp.fsum(h*s**k*zz[2*j+k]for k,h in enumerate(hk))*s**(j-1)/2
            else:
                lw=mp.log(w);terms=[]
                for k,(f,e) in enumerate(zip(self.alpha_w[j-1],self.alpha_e[j-1])):
                    if not f:continue
                    if not e:value=-mp.exp(K*lw)*lw
                    elif e>0:value=-mp.exp(K*lw)*mp.expm1(e*lw)/e
                    else:value=mp.exp((k+1)*lw)*mp.expm1(-e*lw)/e
                    terms.append(f*value)
                a=mp.fsum(terms)/(2*s**(j+1))
            b=s**(j-1)*w*horner(self.beta_w[j-1],w)/2
            aa.append(a);bb.append(b)
        return aa,bb

    def density_modes(self,s,w):
        t=2*s-1 if s<mp.mpf('.5') else 1-2*w
        B=[self.density.clenshaw(row,t)[0]for row in self.coeff]+[mp.mpf(0)]
        out=[]
        for j in range(self.M):
            d=B[j]-s*B[j+1]/2 if j==0 else (B[j]-s*B[j+1])/2
            out.append(w*s**j*d)
        return out+[mp.mpf(0)]

    def coefficients(self,r):
        s,w=self.density.coords(r);aa,bb=self.moments(s,w);b=self.density_modes(s,w)
        p=[(be-al)/2 for al,be in zip(aa,bb)]
        d=[(2*j*(aa[j-1]+bb[j-1])-b[j-1]-b[j])/2 for j in range(1,self.M+1)]
        return p,d

    def stream(self,x,y):
        x=mp.mpf(x);y=mp.mpf(y)
        if x==0 or y==0:return mp.mpf(0)
        r=mp.sqrt(x*x+y*y);theta=mp.atan2(y,x);p,_=self.coefficients(r)
        return r*r*mp.fsum(v*mp.sin(2*j*theta)for j,v in enumerate(p,1))

    def rho(self,x,y):
        x=mp.mpf(x);y=mp.mpf(y)
        if y==0:return mp.mpf(0)
        r=mp.sqrt(x*x+y*y);theta=mp.atan2(y,x)
        return r*self.density.at(r,theta)[0]

    def at(self,x,y):
        x=mp.mpf(x);y=mp.mpf(y);r=mp.sqrt(x*x+y*y)
        if not r:return dict(x=x,y=y,rho=mp.mpf(0),psi=mp.mpf(0),U=[mp.mpf(0),mp.mpf(0)],gradient=[mp.mpf(0),self.a],R=mp.mpf(0),Nf=mp.mpf(0),Nv=mp.mpf(0),R_Nf=None,R_Nv=None)
        theta=mp.atan2(y,x);cs=x/r;sn=y/r;p,d=self.coefficients(r)
        ur=-mp.fsum(2*j*v*mp.cos(2*j*theta)for j,v in enumerate(p,1))
        ut=mp.fsum(v*mp.sin(2*j*theta)for j,v in enumerate(d,1))
        ux=ur*cs-ut*sn;uy=ur*sn+ut*cs
        if x==0:ux=mp.mpf(0)
        if y==0:uy=mp.mpf(0)
        rho,gx,gy=self.density.at(r,theta)
        if x==0:gx=mp.mpf(0)
        if y==0:rho=gx=mp.mpf(0)
        tx=(self.ell*cs+ux)*gx;ty=(self.ell*sn+uy)*gy;rr=tx+ty-rho
        nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(cs*gx+sn*gy)+abs(ux*gx+uy*gy)
        psi=r*r*mp.fsum(v*mp.sin(2*j*theta)for j,v in enumerate(p,1)) if x and y else mp.mpf(0)
        return dict(x=x,y=y,rho=r*rho,psi=psi,U=[r*ux,r*uy],U_over_r=[ux,uy],gradient=[gx,gy],R=r*rr,R_over_r=rr,Nf=r*nf,Nv=r*nv,R_Nf=abs(rr)/nf if nf else None,R_Nv=abs(rr)/nv if nv else None)
