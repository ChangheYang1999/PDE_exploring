"""High-precision field from exact rational harmonic polynomials and basis definitions.

No production numerical code is imported. Parameter derivatives are obtained by
mpmath differentiation of the basis definition, including the reduced tail solve.
"""
import math
from fractions import Fraction
from functools import lru_cache
import numpy as np
import mpmath as mp


@lru_cache(maxsize=None)
def rational_harmonic(ell,m,kind):
    out={}
    for j in range((ell-m)//2+1):
        c=Fraction((-1)**j*math.factorial(2*ell-2*j),2**ell*math.factorial(j)*math.factorial(ell-j)*math.factorial(ell-2*j-m))
        for b in range(m+1):
            phase=(1 if b%4==0 else -1 if b%4==2 else 0) if kind==0 else (1 if b%4==1 else -1 if b%4==3 else 0)
            if not phase:continue
            w=math.comb(m,b)*phase
            for a0 in range(j+1):
                for a1 in range(j-a0+1):
                    a2=j-a0-a1
                    power=(m-b+2*a0,b+2*a1,ell-2*j-m+2*a2)
                    coefficient=c*w*Fraction(math.factorial(j),math.factorial(a0)*math.factorial(a1)*math.factorial(a2))
                    out[power]=out.get(power,Fraction(0))+coefficient
    return tuple((power,value) for power,value in out.items() if value)


def harmonic(mode,y):
    ell,m,kind=mode
    norm=mp.sqrt(mp.mpf(2*ell+1)*math.factorial(ell-m)/(4*mp.pi*math.factorial(ell+m)))*(mp.sqrt(2) if m else 1)
    values=[]
    for axes in [()]+[(i,) for i in range(3)]+[(i,j) for i in range(3) for j in range(3)]:
        terms=[]
        for pp,c in rational_harmonic(ell,m,kind):
            powers=list(pp);value=mp.mpf(c.numerator)/c.denominator
            for axis in axes:
                value*=powers[axis];powers[axis]-=1
            if not value:continue
            for axis in range(3):value*=y[axis]**powers[axis]
            terms.append(value)
        values.append(norm*mp.fsum(terms))
    return values[0],values[1:4],[values[4+3*i:7+3*i] for i in range(3)]


def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


class MPField:
    def __init__(self,field,reduced=True):
        self.modes=[tuple(map(int,m)) for m in field.modes]
        self.lookup={m:i for i,m in enumerate(self.modes)}
        self.coeff={key:[[mp.mpf(float(x)) for x in row] for row in field.arrays[key]] for key in ['A','C','B','D','E']}
        self.r0=mp.mpf(field.r0);self.r1=mp.mpf(float(field.channels.get('R1') or field.r0))
        self.damp=int(field.channels['core_damp']);self.reduced=reduced

    def column(self,name,index,c,w):
        ell,m,kind=self.modes[index]
        a=[row[index] for row in self.coeff[name]]
        n=len(a)
        if not self.reduced or not n:return a
        if name in ['A','C']:
            qc=self.lookup[(ell,m,0)];qs=self.lookup[(ell,m,1)] if m else None
            free=[mp.mpc(self.coeff[name][k][qc],self.coeff[name][k][qs] if m else 0) for k in range(n-2)]
            alpha=(1-c)/c;shift=0 if name=='A' else 1
            P=(alpha+ell-shift)/2+mp.j*m*w/(2*c)
            i=n-2;j=n-1
            ki=mp.mpf(8)*i*i*(i*i-1)/3;kj=mp.mpf(8)*j*j*(j*j-1)/3
            b0=-mp.fsum(k*k*z for k,z in enumerate(free))
            b1=mp.fsum((P-mp.mpf(8)*k*k*(k*k-1)/3)*z for k,z in enumerate(free))
            det=i*i*(kj-P)-j*j*(ki-P)
            u=(b0*(kj-P)-j*j*b1)/det
            v=(i*i*b1-(ki-P)*b0)/det
            a=[mp.im(z) if kind else mp.re(z) for z in free+[u,v]]
        elif name in ['B','D'] and n>=2:
            a[-1]=-mp.fsum(k*k*a[k] for k in range(n-1))/(n-1)**2
        return a

    def radial(self,index,q,c,w,which):
        ell,m,kind=self.modes[index]
        partner=self.lookup[(ell,m,1-kind)] if m else index
        sign=1 if kind else -1
        sr=mp.sqrt(1+q/self.r0**2);alpha=(1-c)/c
        angle=m*w/(2*c)*mp.log1p(q/self.r0**2)
        t=2*q/(mp.sqrt(q+self.r0**2)+self.r0)**2-1
        def amplitude(name,j):
            coefficients=self.column(name,j,c,w)
            return mp.fsum(a*mp.chebyt(k,t) for k,a in enumerate(coefficients))
        def term(name,exponent,twisted=True):
            av=amplitude(name,index)
            if twisted:av=av*mp.cos(angle)-sign*amplitude(name,partner)*mp.sin(angle)
            return sr**exponent*av
        damping=(q/(q+self.r1**2))**self.damp
        if which=='T':
            value=term('A',-alpha-ell)
            if self.coeff['B']:value+=damping*term('B',-2*alpha-1-ell)
        else:
            value=term('C',1-alpha-ell)
            if self.coeff['D']:value+=damping*term('D',-2*alpha-ell)
            if self.coeff['E'] and ell>=2:value+=damping*term('E',-2*ell-1,False)
        return value

    def values(self,point,c,w):
        y=list(map(mp.mpf,point));c=mp.mpf(c);w=mp.mpf(w);q=mp.fsum(x*x for x in y)
        terms={p:{'U':[[] for _ in range(3)],'DU':[[[] for _ in range(3)] for _ in range(3)]} for p in [None,'c_l','omega']}
        for index,mode in enumerate(self.modes):
            ell=mode[0];H,h,K=harmonic(mode,y);hy=cross(h,y)
            for p in terms:
                vals={}
                for which in ['T','S']:
                    fun=lambda qq,cc,ww:self.radial(index,qq,cc,ww,which)
                    vals[which]=[mp.diff(fun,(q,c,w),(d,int(p=='c_l'),int(p=='omega'))) for d in range(3)]
                f,fp,_=vals['T'];g,gp,gpp=vals['S']
                A=(ell+1)*g+2*q*gp;Ap=(ell+3)*gp+2*q*gpp;B=-2*ell*gp;Bp=-2*ell*gpp
                for i in range(3):
                    terms[p]['U'][i].extend([f*hy[i],A*h[i],B*y[i]*H])
                    for j in range(3):
                        ej=[mp.mpf(int(k==j)) for k in range(3)]
                        ky=cross([K[k][j] for k in range(3)],y);hej=cross(h,ej)
                        terms[p]['DU'][i][j].extend([2*fp*y[j]*hy[i],f*ky[i],f*hej[i],A*K[i][j],2*Ap*y[j]*h[i],B*int(i==j)*H,B*y[i]*h[j],2*Bp*y[j]*y[i]*H])
        result={};scales={}
        for p in terms:
            result[p]={'U':[mp.fsum(a) for a in terms[p]['U']],'DU':[[mp.fsum(a) for a in row] for row in terms[p]['DU']]}
            scales[p]={'U':[mp.fsum(abs(x) for x in a) for a in terms[p]['U']],'DU':[[mp.fsum(abs(x) for x in a) for a in row] for row in terms[p]['DU']]}
        base=result[None];u=base['U'];du=base['DU'];jy=[-y[1],y[0],mp.mpf(0)];ju=[-u[1],u[0],mp.mpf(0)];W=[c*y[i]-w*jy[i]+u[i] for i in range(3)]
        for p in ['c_l','omega']:
            up=result[p]['U'];dp=result[p]['DU'];jup=[-up[1],up[0],mp.mpf(0)]
            wp=[(y[i] if p=='c_l' else -jy[i])+up[i] for i in range(3)]
            extra=[-v for v in u] if p=='c_l' else ju
            result[p]['momentum_without_pressure']=[mp.fsum([extra[i],(1-c)*up[i],w*jup[i]]+[du[i][j]*wp[j]+dp[i][j]*W[j] for j in range(3)]) for i in range(3)]
            us= scales[None]['U'];ds=scales[None]['DU'];ups=scales[p]['U'];dps=scales[p]['DU']
            jus=[us[1],us[0],mp.mpf(0)];jups=[ups[1],ups[0],mp.mpf(0)]
            ws=[abs(c*y[j])+abs(w*jy[j])+us[j] for j in range(3)];wps=[abs(y[j] if p=='c_l' else jy[j])+ups[j] for j in range(3)]
            extras=us if p=='c_l' else jus
            scales[p]['momentum_without_pressure']=[mp.fsum([extras[i],abs(1-c)*ups[i],abs(w)*jups[i]]+[ds[i][j]*wps[j]+dps[i][j]*ws[j] for j in range(3)]) for i in range(3)]
        return result,scales
