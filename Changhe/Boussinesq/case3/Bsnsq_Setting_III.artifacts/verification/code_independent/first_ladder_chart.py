"""Packet117: own first nonlinear and constant-velocity tail chart.

Coordinates are exact rational inputs when requested. No NUM code is imported.
"""
from fractions import Fraction as Q
import numpy as np
from fractional_tail_chart import BetaCase as OldCase, FractionalTailProblem as OldProblem
from stream_basis import StreamBasis
from free_beta_stream import prepare_divided
from stream_fractional_tail_certificate import trim, add, scale, mul, deriv, cheb, transport_derivative


def labels(n,J):
    return [(i,j,d) for d in (0,1) for i in range(n) for j in range(2*J)]


def keys(n,J,stream=True):
    a=[(0,j,0) for j in range(J)]
    a += [(i,j,0) for i in range(2,n) for j in range(2*J)]
    a += [(i,j,1) for i in range(1,n) for j in range(2*J)]
    piv={(2,0,0),(3,0,0),(2,1,0)} if stream else {(2,0,0)}
    return [v for v in a if v not in piv]


def lap_angular(p,k):
    return scale(add(add(scale(p,k*k-1),scale(mul([0,1],deriv(p)),-3)),
                     mul([1,0,-1],deriv(deriv(p)))),-1)


def inverse_lap(p,k):
    """Descending monomials, independent of the U-polynomial test inverse."""
    zero=k*0; out=[zero]*(len(p)+2)
    for j in reversed(range(len(p))):
        out[j]=(p[j]+(j+2)*(j+1)*out[j+2])/((j+1)**2-k*k)
    return trim(out[:-2])


def mono_from_cheb(c):
    p=[0]
    for j,v in enumerate(c):p=add(p,scale(cheb(j),v))
    return p


def cheb_from_mono(p):
    a=list(p);out=[a[0]*0]*len(a)
    for j in reversed(range(len(a))):
        t=cheb(j);q=a[j]/t[-1];out[j]=q
        for k,v in enumerate(t):a[k]-=q*v
    return trim(out)


def ladder(beta,P,Qp):
    s=1/beta;m=1-2*s;k=2-s
    A=lap_angular(P,k)
    R0=add(mul([0,1],P),scale(mul([1,0,-1],deriv(P)),-1))
    dQ=add(mul([m,0,2-m],Qp),scale(mul([0,1,0,-1],deriv(Qp)),-1))
    B=add(add(scale(mul(R0,A),-s),scale(mul(P,add(mul([1,0,-1],deriv(A)),scale(mul([0,1],A),-1))),k)),scale(dQ,-1))
    C=add(scale(mul(R0,Qp),m),scale(mul(P,add(mul([1,0,-1],deriv(Qp)),scale(mul([0,1],Qp),-2))),k))
    return inverse_lap(B,2-2*s),C


def moments(beta,cs,n,J,stream=True):
    zero=beta*0;gamma=c=b=zero;s=1/beta
    for coef,(i,j,d) in zip(cs,labels(n,J)):
        v=0 if j%2 else (-1)**(j//2)
        w=0 if not j%2 else j*(-1)**((j-1)//2)
        gamma+=coef*v
        if stream:
            c+=coef*w;b-=coef*(4*(1-s-d-2*i*i*s)-j*j)*v
    return (gamma,c,b) if stream else gamma


def decode(beta,eta,a0,n,J,freeC,freeD):
    if not 2<beta<3 or n<4 or J<2 or not a0:raise ValueError('packet117 requires 2<beta<3,n>=4,J>=2,a0!=0')
    if len(freeC)!=len(keys(n,J)) or len(freeD)!=len(keys(n,J,False)):raise ValueError('chart dimension mismatch')
    zero=beta*0;s=1/beta;ind={key:i for i,key in enumerate(labels(n,J))}
    P,Qp=map(mono_from_cheb,(freeC[:J],freeD[:J]));P10,Q10=ladder(beta,P,Qp)
    arrays=[]
    for vals,stream,lead,first in [(freeC,True,P,P10),(freeD,False,Qp,Q10)]:
        cs=[zero for _ in ind]
        def angular(poly,d,factor=1,i=0):
            for j,v in enumerate(cheb_from_mono(poly)):
                if v:cs[ind[i,j,d]]+=v*factor
        def core(i,j,d,v):
            cs[ind[i,j,d]]+=v;cs[ind[0,j,d]]-=(-1)**i*v
            if d==0:
                q=(-1)**(i-1)*i*i
                cs[ind[0,j,d]]-=q*v;cs[ind[1,j,d]]-=q*v
        angular(lead,0);angular(first,0,Q(1,2),0);angular(first,0,Q(1,2),1)
        angular(transport_derivative(lead,1-s if stream else -1-2*s),1,eta/beta)
        for (i,j,d),v in zip(keys(n,J,stream)[J:],vals[J:]):core(i,j,d,v)
        if stream:
            gamma,c,b=moments(beta,cs,n,J)
            dg=-eta-gamma;dc=1+beta/2-c;db=4*a0/beta-b
            v3=(db+4*(1-3*s)*dg)/(128*s)
            core(3,0,0,v3);core(2,0,0,dg/8+2*v3);core(2,1,0,dc/8)
        else:core(2,0,0,(a0-moments(beta,cs,n,J,False))/8)
        arrays.append(cs)
    return arrays


def exact_state(beta,eta,a0,n,J,freeC,freeD):
    beta,eta,a0=map(Q,(beta,eta,a0));uc,ud=list(map(Q,freeC)),list(map(Q,freeD))
    C,D=decode(beta,eta,a0,n,J,uc,ud)
    assert moments(beta,C,n,J)==(-eta,1+beta/2,4*a0/beta)
    assert moments(beta,D,n,J,False)==a0
    return {'beta':str(beta),'eta':str(eta),'a0':str(a0),'ni':n,'nj':2*J,
            'leading_angular_count':J,'shifts':[0,1],'labels':labels(n,J),
            'C':list(map(str,C)),'D':list(map(str,D)),'freeC':list(map(str,uc)),
            'freeD':list(map(str,ud)),'representation':'packet117 rational first-ladder and fractional-tail center chart'}


def verify_exact_state(data):
    import json
    built=exact_state(data['beta'],data['eta'],data['a0'],data['ni'],data['leading_angular_count'],data['freeC'],data['freeD'])
    for key,val in json.loads(json.dumps(built)).items():
        if data.get(key)!=val:raise ValueError('packet117 exact input mismatch: '+key)
    return True


def tail_checks(data):
    """Re-extract endpoint and derivative from serialized ordinary coefficients."""
    from stream_fractional_tail_certificate import checks as constant_checks,angular
    beta=Q(data['beta']);P=angular(data,'C',0);Qp=angular(data,'D',0)
    first=[]
    for name in ['C','D']:
        a=[Q(0)]
        for (i,j,d),v in zip(data['labels'],data[name]):
            if d==0 and i:a=add(a,scale(cheb(j),Q(v)*2*(-1)**(i-1)*i*i))
        first.append(a)
    desired=ladder(beta,P,Qp)
    defects=[add(a,scale(b,-1))for a,b in zip(first,desired)]
    result=constant_checks(data)
    result.update(first_ladder_stream_nonzero=any(defects[0]),first_ladder_temperature_nonzero=any(defects[1]),
       P10=list(map(str,first[0])),Q10=list(map(str,first[1])),
       first_ladder_stream_defect=list(map(str,defects[0])),first_ladder_temperature_defect=list(map(str,defects[1])))
    return result


class BetaCase(OldCase):
    def __init__(self,beta,n,J,points,reference_beta=2.5,a0=1.):
        self.beta,self.n,self.J,self.a0=float(beta),n,J,a0
        self.basis=StreamBasis(beta,n,2*J,a0=a0);self.data=prepare_divided(self.basis,points)
        self.nc,self.nd=len(keys(n,J)),len(keys(n,J,False));self.size=self.nc+self.nd
        self.nonlinear=[0]+list(range(1,1+J))+list(range(1+self.nc,1+self.nc+J))
        self.constant_columns=[];zero=np.zeros(1+self.size)
        base=np.concatenate(self.coefficients(0.,zero[1:]))
        for j in range(len(zero)):
            if j in self.nonlinear:self.constant_columns.append(np.zeros_like(base))
            else:
                e=zero.copy();e[j]=1;self.constant_columns.append(np.concatenate(self.coefficients(e[0],e[1:]))-base)
        self.constant_columns=np.stack(self.constant_columns,axis=1)
        rad=np.sqrt(1+np.sum(np.asarray(points)**2,axis=1))
        self.wF=rad**(1+3/reference_beta)/a0/np.sqrt(len(rad))
        self.wG=rad**(1+2/reference_beta)/a0/np.sqrt(len(rad));self.last=None

    def coefficients(self,eta,u):
        return [np.asarray(v,float)for v in decode(self.beta,eta,self.a0,self.n,self.J,u[:self.nc],u[self.nc:])]

    def coefficient_jacobian(self,eta,u):
        z=np.r_[eta,u];cols=self.constant_columns.copy()
        for j in self.nonlinear:
            p=z.copy();q=z.copy();p[j]+=1;q[j]-=1
            cols[:,j]=(np.concatenate(self.coefficients(p[0],p[1:]))-np.concatenate(self.coefficients(q[0],q[1:])))/2
        return np.split(cols,2,axis=0)

    def jacobian_eta_coefficients(self,eta,u):
        if self.last is None or self.last[0]!=eta or not np.array_equal(self.last[1],u):self.residual(eta,u)
        q=self.last[2];directions={}
        for name,cols in zip(['C','D'],self.coefficient_jacobian(eta,u)):
            directions[name]={k:mat@cols for k,mat in self.data[name].items()}
        c,d=directions['C'],directions['D'];x=self.data['points'][:,0,None];col=lambda k:q[k][:,None]
        df=c['aV']*(2*col('f')+x*col('fx'))+col('A')*(2*d['f']+x*d['fx'])+c['U2']*col('fy')+col('B')*d['fy']-(self.beta-2)*d['f']
        dg=c['aV']*(col('g')+x*col('gx'))+col('A')*(c['g']+x*c['gx'])+c['U2']*col('gy')+col('B')*c['gy']+c['g']-(2*d['f']+x*d['fx'])
        return np.vstack((self.wF[:,None]*df,self.wG[:,None]*dg))


class FirstLadderProblem(OldProblem):
    def case(self,beta):
        beta=float(beta)
        if beta not in self.cache:
            self.cache[beta]=BetaCase(beta,self.n,self.J,self.points,self.reference_beta,self.a0);self.rebuilds+=1
        self.cache.move_to_end(beta)
        while len(self.cache)>3:self.cache.popitem(last=False)
        return self.cache[beta]
