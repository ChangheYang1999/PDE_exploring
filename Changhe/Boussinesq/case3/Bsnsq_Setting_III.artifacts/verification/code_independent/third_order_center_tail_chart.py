"""Packet125: six-pivot center-compatible first-tail chart, independent of NUM."""
from fractions import Fraction as Q
import numpy as np
from first_ladder_chart import (labels,keys as oldkeys,ladder,mono_from_cheb,
    cheb_from_mono,transport_derivative,BetaCase as OldCase,
    FirstLadderProblem as OldProblem,tail_checks)
from stream_basis import StreamBasis
from free_beta_stream import prepare_divided
from stream_local_jet_certificate import checks as local_checks


def keys(n,J,stream=True):
    extra=(3,1,0) if stream else (2,1,0)
    return [key for key in oldkeys(n,J,stream) if key!=extra]


def moments(beta,cs,n,J,stream=True):
    zero=beta*0;s=1/beta;gamma=c0=b0=c1=b1=zero;a=a1=zero
    for coef,(i,j,d) in zip(cs,labels(n,J)):
        v=0 if j%2 else (-1)**(j//2)
        w=0 if not j%2 else j*(-1)**((j-1)//2)
        if stream:
            k=1-s-d
            gamma+=coef*v;c0+=coef*w
            b0-=coef*(4*(k-2*i*i*s)-j*j)*v
            c1+=coef*(k-2*i*i*s-j*j)*v
            b1+=coef*(-6*k+5+12*i*i*s+j*j)*w
        else:a+=coef*v;a1+=coef*w
    return (gamma,c0,b0,c1,b1) if stream else (a,a1)


def decode(beta,eta,a0,n,J,freeC,freeD):
    if not 2<beta<3 or n<4 or J<2 or not a0:
        raise ValueError('packet125 requires 2<beta<3,n>=4,J>=2,a0!=0')
    if len(freeC)!=len(keys(n,J)) or len(freeD)!=len(keys(n,J,False)):
        raise ValueError('chart dimension mismatch')
    zero=beta*0;s=1/beta;mu=1+3*beta/2;M=2*beta+1;q0=4*a0/beta
    ind={key:i for i,key in enumerate(labels(n,J))}
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
            gamma,c0,b0,c1,b1=moments(beta,cs,n,J)
            dg=-eta-gamma;db=q0-b0
            v3=(db+4*(1-3*s)*dg)/(128*s)
            core(3,0,0,v3);core(2,0,0,dg/8+2*v3)
            gamma,c0,b0,c1,b1=moments(beta,cs,n,J)
            dc=1+beta/2-c0;db1=(q0+4*a0/mu)*c1/M-b1
            u3=(db1-18*s*dc)/(192*s)
            core(3,1,0,u3);core(2,1,0,dc/8+2*u3)
        else:
            a,a1=moments(beta,cs,n,J,False)
            core(2,0,0,(a0-a)/8);core(2,1,0,(2*a0*c1/mu-a1)/8)
        arrays.append(cs)
    return arrays


def exact_state(beta,eta,a0,n,J,freeC,freeD):
    beta,eta,a0=map(Q,(beta,eta,a0));uc,ud=list(map(Q,freeC)),list(map(Q,freeD))
    C,D=decode(beta,eta,a0,n,J,uc,ud)
    gamma,c0,b0,c1,b1=moments(beta,C,n,J);a,a1=moments(beta,D,n,J,False)
    assert (gamma,c0,b0,a)==(-eta,1+beta/2,4*a0/beta,a0)
    assert a1==2*a0*c1/(1+3*beta/2)
    assert (2*beta+1)*b1-c1*b0-2*a1==0
    data={'beta':str(beta),'eta':str(eta),'a0':str(a0),'ni':n,'nj':2*J,
        'leading_angular_count':J,'shifts':[0,1],'labels':labels(n,J),
        'C':list(map(str,C)),'D':list(map(str,D)),'freeC':list(map(str,uc)),
        'freeD':list(map(str,ud)),
        'representation':'packet125 rational six-pivot center and first-ladder/fractional-tail chart'}
    import json
    assert not any(local_checks(json.loads(json.dumps(data)))['nonzero'].values())
    return data


def verify_exact_state(data):
    import json
    built=exact_state(data['beta'],data['eta'],data['a0'],data['ni'],
        data['leading_angular_count'],data['freeC'],data['freeD'])
    for key,val in json.loads(json.dumps(built)).items():
        if data.get(key)!=val:raise ValueError('packet125 exact input mismatch: '+key)
    return True


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
                e=zero.copy();e[j]=1
                self.constant_columns.append(np.concatenate(self.coefficients(e[0],e[1:]))-base)
        self.constant_columns=np.stack(self.constant_columns,axis=1)
        rad=np.sqrt(1+np.sum(np.asarray(points)**2,axis=1))
        self.wF=rad**(1+3/reference_beta)/a0/np.sqrt(len(rad))
        self.wG=rad**(1+2/reference_beta)/a0/np.sqrt(len(rad));self.last=None

    def coefficients(self,eta,u):
        return [np.asarray(v,float) for v in decode(self.beta,eta,self.a0,self.n,self.J,u[:self.nc],u[self.nc:])]


class ThirdOrderProblem(OldProblem):
    def case(self,beta):
        beta=float(beta)
        if beta not in self.cache:
            self.cache[beta]=BetaCase(beta,self.n,self.J,self.points,self.reference_beta,self.a0);self.rebuilds+=1
        self.cache.move_to_end(beta)
        while len(self.cache)>3:self.cache.popitem(last=False)
        return self.cache[beta]
