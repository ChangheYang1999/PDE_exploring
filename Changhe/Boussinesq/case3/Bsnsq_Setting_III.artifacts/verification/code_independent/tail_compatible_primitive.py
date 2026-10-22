"""Independent nonlinear two-moment chart for horizontal primitive B2,130."""
from collections import OrderedDict
from fractions import Fraction as Q
from types import SimpleNamespace
import numpy as np
from free_beta_stream import make_chart
from horizontal_primitive_stream import PrimitiveProblem
from primitive_tail_moments import cheb,D,L,mul,scale,moment,directions,repair


def moment_matrices(beta,nj):
    beta=Q.from_float(float(beta));s=1/beta;m=1-2*s
    Lrows=[];Hrows=[]
    for sigma in [1,-1]:
        linear=[];H=np.zeros((nj,nj))
        for i in range(nj):
            pi=[Q(0)]*i+[Q(1)];linear.append(float(moment(m,L(2-2*s,pi),sigma)))
            for j in range(nj):
                pj=[Q(0)]*j+[Q(1)];qj=scale(L(2-s,pj),-1)
                h=scale(mul(D(pi),qj),s)
                # Separate exact moment of the other bilinear term avoids using
                # any finite-difference derivative of the constraint.
                H[i,j]=float(moment(m,h,sigma)+moment(m,scale(mul(pi,D(qj)),2-s),sigma))
        Lrows.append(np.array(linear));Hrows.append((H+H.T)/2)
    return np.array(Lrows),np.array(Hrows)

class TailChart:
    def __init__(self,basis):
        self.basis=basis;self.beta=basis.beta;self.m=1-2/self.beta;labels=basis.labels
        dropped=[labels.index((3,0,0)),labels.index((2,1,0))]
        self.free=[i for i in basis.freeC if i not in dropped]
        cols=[basis.freeC.index(i)for i in self.free]
        self.base=basis.Cbase;self.B=basis.Cnull[:,cols]
        self.d0,self.d1=map(lambda d:np.array(list(map(float,d))),directions(labels))
        self.size=len(self.free);nj=basis.nj
        self.P=np.zeros((nj,basis.n));self.P1=self.P.copy()
        for l,(i,j,d)in enumerate(labels):
            if d:continue
            t=np.array(list(map(float,cheb(j))))
            self.P[:len(t),l]=(-1)**i*t
            if i:self.P1[:len(t),l]=2*(-1)**(i-1)*i*i*t
        self.l,self.H=moment_matrices(self.beta,nj)
    def parameters(self,z,with_jac=False):
        C=self.base+self.B@z;p=self.P@C;p1=self.P1@C
        cs=np.array([p@H@p+l@p1 for H,l in zip(self.H,self.l)])
        a=(cs[0]+cs[1])/(2*(self.m+2));b=(cs[0]-cs[1])/(2*(self.m+3));v=np.r_[z,a,b]
        if not with_jac:return v
        jc=np.array([(2*p@H@self.P+l@self.P1)@self.B for H,l in zip(self.H,self.l)])
        Ja=(jc[0]+jc[1])/(2*(self.m+2));Jb=(jc[0]-jc[1])/(2*(self.m+3))
        return v,np.vstack((np.eye(len(z)),Ja,Jb))
    def coefficients(self,z):
        v=self.parameters(z);return self.base+self.B@z+v[-2]*self.d0+v[-1]*self.d1
    def raw_coefficients(self,z):return self.base+self.B@z

class TailPrimitiveProblem:
    def __init__(self,basis,points,reference_beta=None,order=32,regularization=0.):
        self.basis=basis;self.chart=TailChart(basis);self.size=self.chart.size;self.reg=regularization
        holder=SimpleNamespace(beta=basis.beta,s=basis.s,a0=basis.a0,psi=basis.psi,
             Cbase=self.chart.base,Cnull=np.column_stack((self.chart.B,self.chart.d0,self.chart.d1)))
        self.inner=PrimitiveProblem(holder,points,order,'sinh',0.,reference_beta)
    def residual(self,z):
        r=self.inner.residual(self.chart.parameters(z));return np.r_[r,self.reg*z]if self.reg else r
    def jacobian(self,z):
        v,Jv=self.chart.parameters(z,True);J=self.inner.jacobian(v)@Jv
        return np.vstack((J,self.reg*np.eye(len(z))))if self.reg else J
    def coefficients(self,z):return self.chart.coefficients(z)
    def diagnostics(self,z):return self.inner.diagnostics(self.chart.parameters(z))

class FreeBetaTailPrimitive:
    def __init__(self,ni,nj,points,reference_beta,order=32,regularization=0.):
        self.ni=ni;self.nj=nj;self.points=np.asarray(points);self.reference_beta=reference_beta;self.order=order;self.reg=regularization;self.cache=OrderedDict()
    def case(self,beta):
        beta=float(beta)
        if beta not in self.cache:
            b=make_chart(beta,self.ni,self.nj);self.cache[beta]=TailPrimitiveProblem(b,self.points,self.reference_beta,self.order,self.reg)
        self.cache.move_to_end(beta)
        while len(self.cache)>3:self.cache.popitem(last=False)
        return self.cache[beta]
    def residual(self,z):return self.case(z[0]).residual(z[1:])
    def jacobian(self,z):
        beta=z[0];h=min(1e-5*max(1.,abs(beta)),(beta-2)/4)
        Jc=self.case(beta).jacobian(z[1:]);Jb=(self.case(beta+h).residual(z[1:])-self.case(beta-h).residual(z[1:]))/(2*h)
        return np.column_stack((Jb,Jc))


def exact_serialized_coefficients(beta,labels,C,a0='1'):
    """Rational center projection followed by exact rational tail repair."""
    beta=Q.from_float(float(beta));labels=list(map(tuple,labels));C=list(map(lambda v:Q.from_float(float(v)),C))
    i0=labels.index((0,0,0));i1=labels.index((0,1,0));C[i0]=C[i1]=Q(0);c=b=Q(0)
    for(i,j,d),cc in zip(labels,C):
        v=0 if j%2 else (-1)**(j//2);w=0 if not j%2 else j*(-1)**((j-1)//2);k=1-1/beta-d
        c+=cc*w;b-=cc*(4*(k-2*i*i/beta)-j*j)*v
    C[i1]=1+beta/2-c;C[i0]=(4*Q(a0)/beta-b)/(-4*(1-1/beta))
    C,detail=repair(beta,labels,C)
    return str(beta),list(map(str,C)),detail
