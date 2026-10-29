"""Full-space five-dimensional inverse of regular monomial power sources.

The radial integration is analytic in special functions. No finite outer
boundary is imposed. See research/eta_green_basis/PROOF.md for the derivation.
"""
from functools import lru_cache
from fractions import Fraction
from math import comb,factorial
from pathlib import Path
import json
import numpy as np
from scipy.special import hyp2f1,beta as beta_function,betainc,poch
from independent_fields import ScalarExpansion,PotentialField,Term
from piecewise_adapter import Taylor2

@lru_cache(None)
def gegenbauer_polynomial(ell):
    result={}
    for k in range(ell//2+1):
        p=ell-2*k;factor=Fraction(1)
        for h in range(ell-k):factor*=Fraction(3,2)+h
        result[p]=(-1)**k*factor*2**p/Fraction(factorial(k)*factorial(p))
    return result

@lru_cache(None)
def angular_decomposition(i,j):
    remaining={j+2*k:Fraction((-1)**k*comb(i,k)) for k in range(i+1)};out=[];d=2*i+j
    for ell in range(d,j%2-1,-2):
        polynomial=gegenbauer_polynomial(ell);coefficient=remaining.get(ell,Fraction(0))/polynomial[ell]
        if coefficient:
            out.append((ell,coefficient))
            for p,v in polynomial.items():remaining[p]=remaining.get(p,Fraction(0))-coefficient*v
    if any(remaining.values()):raise ArithmeticError('angular decomposition failed')
    return tuple(out)

@lru_cache(None)
def solid_harmonic(ell):
    out={}
    for p,c in gegenbauer_polynomial(ell).items():
        k=(ell-p)//2
        for i in range(k+1):
            key=(i,ell-2*i);out[key]=out.get(key,Fraction(0))+c*comb(k,i)
    return tuple((i,j,c) for (i,j),c in out.items() if c)


def radial_derivatives(t,ell,d,exponent,order=3):
    """h through h^(order), with angular/source coefficient one."""
    t=np.asarray(t,dtype=float);m=(d-ell)//2;A=(ell+d+5)/2;A2=m+1;B2=exponent-A2
    if m<0 or 2*m!=d-ell or B2<=0:raise ValueError('invalid source mode')
    H=hyp2f1(exponent,A,A+1,-t)
    result=[(t**(m+1)*H/(2*A)+.5*beta_function(B2,A2)*betainc(B2,A2,1/(1+t)))/(2*ell+3)]
    for derivative in range(1,order+1):
        n=derivative-1;value=np.zeros_like(t)
        for p in range(min(n,m)+1):
            k=n-p
            factor=comb(n,p)*factorial(m)/factorial(m-p)*(-1)**k*poch(exponent,k)*A/(A+k)
            value+=factor*t**(m-p)*hyp2f1(exponent+k,A+k,A+1+k,-t)
        result.append(-value/(4*A))
    if any(not np.all(np.isfinite(v)) for v in result):raise FloatingPointError('nonfinite radial inverse')
    return result


class GreenPotential:
    def __init__(self,source):
        if source.kernel!='power':raise ValueError('power sources required')
        if any(2*t.beta-2*t.i-t.j<=2 for t in source.terms):raise ValueError('source must decay faster than R^-2')
        self.source=source;self.length=source.length;self.cache=None
    def jet(self,s,z,order):
        if order not in range(4):raise ValueError('orders zero through three supported')
        s,z=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(z,dtype=float))
        if np.any(s<0):raise ValueError('s must be nonnegative')
        if self.cache is not None:
            ss,zz,oo,answer=self.cache
            if order<=oo and np.array_equal(s,ss) and np.array_equal(z,zz):return answer
        shape=s.shape;L=self.length;sv=s.ravel()/L**2;zv=z.ravel()/L;alg=Taylor2(order,s.size)
        sj=alg.variable(sv,(1,0));zj=alg.variable(zv,(0,1));tj=sj+alg.multiply(zj,zj);delta=tj.copy();delta[0]=0
        delta_powers=[alg.constant(1.)]
        for n in range(order):delta_powers.append(alg.multiply(delta_powers[-1],delta))
        maximum=max([2*x.i+x.j for x in self.source.terms],default=0)
        spowers=[alg.constant(1.)];zpowers=[alg.constant(1.)]
        for k in range(maximum):
            spowers.append(alg.multiply(spowers[-1],sj));zpowers.append(alg.multiply(zpowers[-1],zj))
        solids={};result=alg.constant(0.)
        for term in self.source.terms:
            if term.coefficient==0:continue
            d=2*term.i+term.j;amplitude=term.coefficient*L**(d+2-2*term.beta)
            for ell,angular in angular_decomposition(term.i,term.j):
                if ell not in solids:
                    solids[ell]=sum((float(c)*alg.multiply(spowers[i],zpowers[j]) for i,j,c in solid_harmonic(ell)),alg.constant(0.))
                derivatives=radial_derivatives(tj[0],ell,d,term.beta,order)
                radial=sum((delta_powers[n]*(derivatives[n]/factorial(n)) for n in range(order+1)),alg.constant(0.))
                result+=float(angular)*amplitude*alg.multiply(solids[ell],radial)
        answer={(a,b):(result[k]*factorial(a)*factorial(b)/L**(2*a+b)).reshape(shape) for k,(a,b) in enumerate(alg.indices)}
        self.cache=(s.copy(),z.copy(),order,answer)
        return answer
    def evaluate(self,s,z,ds=0,dz=0):return self.jet(s,z,ds+dz)[ds,dz]
    def dilate(self,L,amplitude):return GreenPotential(self.source.dilate(L,amplitude/L**2))


class EtaGreenField(PotentialField):
    def __init__(self,eta,q,c_l):
        self.eta_expansion=eta
        super().__init__(GreenPotential(eta),q,c_l)
    def cylindrical(self,r,z,order=3):
        d=super().cylindrical(r,z,order);s=d['s'];e=self.eta_expansion.jet(s,d['z'],1 if order>=3 else 0)
        d['elliptic_defect']=d['eta']-e[0,0];d['eta_from_potential']=d['eta'];d['eta']=e[0,0]
        if order>=3:
            d['elliptic_s_defect']=d['eta_s']-e[1,0];d['elliptic_z_defect']=d['eta_z']-e[0,1]
            d['eta_s']=e[1,0];d['eta_z']=e[0,1]
        return d
    def reduced(self,r,z):
        result=super().reduced(r,z);d=self.cylindrical(r,z,3);result['elliptic']=d['elliptic_defect']
        return result
    def dilate(self,L):return EtaGreenField(self.eta_expansion.dilate(L,1/L),self.q.dilate(L,1),self.c_l)
    def leading_polynomials(self):
        from numpy.polynomial import Polynomial as Poly
        A=Poly([0.]);B=Poly([0.]);mu=Poly([0.,1.]);one=Poly([1.,0.,-1.]);terms=[]
        for name,source,power in [('eta',self.eta_expansion,self.alpha+2),('q',self.q,self.alpha+1)]:
            for t in source.terms:
                actual=2*t.beta-2*t.i-t.j
                status='leading' if abs(actual-power)<2e-11 else ('faster' if actual>power else 'slower')
                terms.append(dict(field=name,coefficient=t.coefficient,decay_power=actual,classification=status))
                if status=='slower' and t.coefficient:raise ValueError('source slower than declared tail')
                if status!='leading':continue
                if name=='q':B+=t.coefficient*one**t.i*mu**t.j
                else:
                    for ell,angular in angular_decomposition(t.i,t.j):
                        den=ell*(ell+3)+self.alpha*(3-self.alpha)
                        cc=np.zeros(ell+1)
                        for n,v in gegenbauer_polynomial(ell).items():cc[n]=float(v)
                        A+=t.coefficient*float(angular)*Poly(cc)/den
        return A,B,terms
    def reporting_gauge(self):
        from scipy.special import roots_legendre
        from independent_farfield import angular_data,evaluate_vector
        A,B,terms=self.leading_polynomials();mu,w=roots_legendre(max(64,len(A.coef)+len(B.coef)+8))
        data=angular_data(self.alpha,A,B);F=evaluate_vector(data,mu,'F')
        norm=float(2*np.pi*np.sum(w[:,None]*F*F))
        if norm<=0 or not np.isfinite(norm):raise ValueError('no nonzero leading tail')
        L=norm**(-1/(2+2*self.alpha))
        return self.dilate(L),dict(dilation_L=L,input_leading_squared_norm=norm,reported_leading_squared_norm=L**(2+2*self.alpha)*norm)
    def as_dict(self):return dict(format='verifier-eta-green-v1',c_l=self.c_l,eta=self.eta_expansion.as_dict(),q=self.q.as_dict())
    @classmethod
    def load(cls,path):
        d=json.loads(Path(path).read_text())
        if d.get('format')!='verifier-eta-green-v1':raise ValueError('unrecognized source representation')
        return cls(ScalarExpansion.from_dict(d['eta']),ScalarExpansion.from_dict(d['q']),d['c_l'])
