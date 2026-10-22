"""Smooth Cartesian rational bases for a separate exploratory solver.

Each basis is L^amplitude_degree (x/L)^i (y/L)^j
[1+(x*x+y*y)/L^2]^q. Derivative operators act on monomials
and radial powers by the product rule, through order three.
This implementation shares no code with the fitting lane.
"""
from dataclasses import dataclass,asdict
import numpy as np


@dataclass(frozen=True)
class Term:
    i:int
    j:int
    scale:float
    tail_order:int


def differentiate(terms,axis,scale):
    out={}
    inv=1/scale**2
    for (i,j,q),c in terms.items():
        n=i if axis==0 else j
        if n:
            key=(i-1,j,q) if axis==0 else (i,j-1,q)
            out[key]=out.get(key,0)+c*n
        if q:
            key=(i+1,j,q-1) if axis==0 else (i,j+1,q-1)
            out[key]=out.get(key,0)+2*c*q*inv
    return {key:c for key,c in out.items() if c!=0}


def evaluate_terms(terms,x,y,scale,divide_x=0):
    x,y=np.broadcast_arrays(x,y)
    z=1+(x*x+y*y)/scale**2
    out=np.zeros(x.shape)
    for (i,j,q),c in terms.items():
        if i<divide_x:
            raise ValueError('division by x is incompatible with polynomial parity')
        out+=c*x**(i-divide_x)*y**j*z**q
    return out


def expansion(term,beta,field,dx=0,dy=0):
    # Temperature leading degree 1-2/beta; stream leading 2-1/beta.
    if field=='psi':
        target=2-term.tail_order/beta
        amp=2
    elif field=='theta':
        target=1-(term.tail_order+1)/beta
        amp=1
    else:
        raise ValueError(field)
    q=(target-term.i-term.j)/2
    t={(term.i,term.j,q):term.scale**(amp-term.i-term.j)}
    for _ in range(dx):t=differentiate(t,0,term.scale)
    for _ in range(dy):t=differentiate(t,1,term.scale)
    return t


def combine(first,second,factor=1.):
    out=dict(first)
    for key,value in second.items():out[key]=out.get(key,0.)+factor*value
    return {key:value for key,value in out.items() if value!=0.}


def omega_expansion(term,beta,dx=0,dy=0):
    a=expansion(term,beta,'psi',dx+2,dy)
    b=expansion(term,beta,'psi',dx,dy+2)
    return {k:-v for k,v in combine(a,b).items()}


def make_terms(degree,scales=(1.,4.),tail_orders=(1,2),field='psi'):
    start=1 if field=='psi' else 2
    terms=[]
    for scale in scales:
        for tail in tail_orders:
            for i in range(start,degree+1,2):
                for j in range(degree-i+1):
                    terms.append(Term(i,j,scale,tail))
    return terms


def matrix(terms,beta,field,points,dx=0,dy=0,divide_x=0):
    p=np.atleast_2d(points)
    cols=[]
    for term in terms:
        e=omega_expansion(term,beta,dx,dy) if field=='omega' else expansion(term,beta,field,dx,dy)
        cols.append(evaluate_terms(e,p[:,0],p[:,1],term.scale,divide_x))
    return np.column_stack(cols)


class RationalProfile:
    def __init__(self,beta,psi_terms,theta_terms,psi_coeff,theta_coeff):
        self.beta=float(beta)
        self.psi_terms=psi_terms
        self.theta_terms=theta_terms
        self.psi_coeff=np.asarray(psi_coeff)
        self.theta_coeff=np.asarray(theta_coeff)
        self.v0=(matrix(psi_terms,beta,'psi',[[0,0]],dx=1)@self.psi_coeff).item()

    def value(self,field,x,y,dx=0,dy=0,divide_x=0):
        x,y=np.broadcast_arrays(x,y)
        p=np.column_stack((x.ravel(),y.ravel()))
        terms=self.theta_terms if field=='theta' else self.psi_terms
        coeff=self.theta_coeff if field=='theta' else self.psi_coeff
        result=matrix(terms,self.beta,field,p,dx,dy,divide_x)@coeff
        return result.reshape(x.shape)

    def psi(self,x,y):return self.value('psi',x,y)
    def theta(self,x,y):return self.value('theta',x,y)
    def omega(self,x,y):return self.value('omega',x,y)
    def relative(self,p):
        p=np.atleast_2d(p)
        return np.column_stack((-self.value('psi',p[:,0],p[:,1],dy=1),
                                self.value('psi',p[:,0],p[:,1],dx=1)-self.v0))

    def to_dict(self):
        return {'format':'verification-rational-v1','beta':self.beta,
                'psi_terms':[asdict(t) for t in self.psi_terms],
                'theta_terms':[asdict(t) for t in self.theta_terms],
                'psi_coeff':self.psi_coeff.tolist(),'theta_coeff':self.theta_coeff.tolist(),
                'absolute_velocity_convention':'U=grad_perp of displayed stream; report ordinary center moment convergence separately',
                'status':'exploratory candidate, not existence evidence'}

    @classmethod
    def from_dict(cls,data):
        return cls(data['beta'],[Term(**v) for v in data['psi_terms']],
                   [Term(**v) for v in data['theta_terms']],data['psi_coeff'],data['theta_coeff'])
