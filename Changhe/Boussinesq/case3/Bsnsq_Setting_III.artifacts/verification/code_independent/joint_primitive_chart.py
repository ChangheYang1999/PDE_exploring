"""Own joint center/tail trial map,134. No NUM imports or fitting code reuse."""
from collections import OrderedDict
from fractions import Fraction as Q
from types import SimpleNamespace
from math import comb
import numpy as np
from free_beta_stream import make_chart
from stream_basis import combine,derivative,evaluate_terms
from horizontal_primitive_stream import PrimitiveProblem
from tail_compatible_primitive import TailChart,exact_serialized_coefficients
from primitive_local_repair import residual_coefficients,project
from exact_bivariate import ordinary_stream_jet

JET_KEYS=((3,0),(1,2),(3,1),(1,3),(5,0),(3,2),(1,4))
EXTRA_POWERS=((1,3),(5,0),(1,4))
EXTRA_TERMS=[{(i,j,0,-8):1.}for i,j in EXTRA_POWERS]

def stream_row(terms,s):
    px=derivative(terms,0,s);py=derivative(terms,1,s)
    om=combine((-1,derivative(px,0,s)),(-1,derivative(py,1,s)))
    gauge=float(evaluate_terms(px,0.,0.,s))
    return {'Psi':terms,'U1':combine((-1,py)),'U2':combine((1,px),(-gauge,{(0,0,0,0):1.})),'Omega':om}

def jet_matrix(basis):
    matrix=np.zeros((len(JET_KEYS),basis.n));pos={key:k for k,key in enumerate(JET_KEYS)}
    for col,row in enumerate(basis.psi):
        for(a,b,ns,nc),v in row['Psi'].items():
            exponent=(ns*basis.s+nc)/2;choose=1.
            for k in range((5-a-b)//2+1):
                if k:choose*= (exponent-k+1)/k
                for ell in range(k+1):
                    key=(a+2*ell,b+2*(k-ell))
                    if key in pos:matrix[pos[key],col]+=v*choose*comb(k,ell)
    return matrix

def local_parameters(beta,a0,jet):
    """Polynomial map; supports complex perturbations without conjugation."""
    jet=dict(zip(JET_KEYS,jet));l1=(beta-2)/2;l2=(3*beta+2)/2
    r=residual_coefficients(beta,a0,jet);e=r[(2,1)]/(3*l2*(2*beta+1));jet[(1,3)]+=e
    r=residual_coefficients(beta,a0,jet)
    return np.array([e,r[(4,0)]/(10*l1*(3*l1+1)),r[(2,2)]/(12*l2*(l1+2*l2+1))])

class JointChart:
    def __init__(self,basis):
        self.basis=basis;self.tail=TailChart(basis);self.size=self.tail.size
        self.base=self.tail.base;self.M=np.column_stack((self.tail.B,self.tail.d0,self.tail.d1));self.jet=jet_matrix(basis)
    def parameters(self,z,with_jac=False):
        if with_jac:v,J=self.tail.parameters(z,True)
        else:v=self.tail.parameters(z)
        C=self.base+self.M@v;jet=self.jet@C;k=local_parameters(self.basis.beta,self.basis.a0,jet);out=np.r_[v,k]
        if not with_jac:return out
        # Complex differentiation is restricted to a seven-variable polynomial.
        h=1e-30;JK=np.zeros((3,len(jet)))
        for j in range(len(jet)):
            w=jet.astype(complex);w[j]+=1j*h;JK[:,j]=local_parameters(self.basis.beta,self.basis.a0,w).imag/h
        return out,np.vstack((J,JK@self.jet@self.M@J))
    def coefficients(self,z):
        v=self.parameters(z);return self.base+self.M@v[:-3],v[-3:]
    def raw_coefficients(self,z):return self.tail.raw_coefficients(z)

class JointPrimitiveProblem:
    def __init__(self,basis,points,reference_beta=None,order=32,regularization=0.):
        self.basis=basis;self.chart=JointChart(basis);self.size=self.chart.size;self.reg=regularization
        extra=[stream_row(t,basis.s)for t in EXTRA_TERMS]
        matrix=np.block([[self.chart.M,np.zeros((basis.n,3))],[np.zeros((3,self.size+2)),np.eye(3)]])
        holder=SimpleNamespace(beta=basis.beta,s=basis.s,a0=basis.a0,psi=basis.psi+extra,
             Cbase=np.r_[self.chart.base,np.zeros(3)],Cnull=matrix)
        self.inner=PrimitiveProblem(holder,points,order,'sinh',0.,reference_beta)
    def residual(self,z):
        r=self.inner.residual(self.chart.parameters(z));return np.r_[r,self.reg*z]if self.reg else r
    def jacobian(self,z):
        v,Jv=self.chart.parameters(z,True);J=self.inner.jacobian(v)@Jv
        return np.vstack((J,self.reg*np.eye(len(z))))if self.reg else J
    def coefficients(self,z):return self.chart.coefficients(z)
    def diagnostics(self,z):return self.inner.diagnostics(self.chart.parameters(z))

class FreeBetaJointPrimitive:
    def __init__(self,ni,nj,points,reference_beta,order=32,regularization=0.):
        self.ni=ni;self.nj=nj;self.points=np.asarray(points);self.reference_beta=reference_beta;self.order=order;self.reg=regularization;self.cache=OrderedDict()
    def case(self,beta):
        beta=float(beta)
        if beta not in self.cache:
            b=make_chart(beta,self.ni,self.nj);self.cache[beta]=JointPrimitiveProblem(b,self.points,self.reference_beta,self.order,self.reg)
        self.cache.move_to_end(beta)
        while len(self.cache)>3:self.cache.popitem(last=False)
        return self.cache[beta]
    def residual(self,z):return self.case(z[0]).residual(z[1:])
    def jacobian(self,z):
        beta=z[0];h=min(1e-5*max(1.,abs(beta)),(beta-2)/4)
        Jc=self.case(beta).jacobian(z[1:]);Jb=(self.case(beta+h).residual(z[1:])-self.case(beta-h).residual(z[1:]))/(2*h)
        return np.column_stack((Jb,Jc))

def serialize_coefficients(beta,labels,rawC,a0='1'):
    rb,rC,detail=exact_serialized_coefficients(beta,labels,rawC,a0)
    jet,_=ordinary_stream_jet(Q(rb),labels,list(map(Q,rC)),[Q(0)]*len(rC),8)
    k,_=project(Q(rb),Q(a0),jet)
    extra=[{'x_power':i,'y_power':j,'R_power':'-8','coefficient':str(c)}for(i,j),c in zip(EXTRA_POWERS,k)]
    return rb,rC,extra,detail
