"""Independent nested T1 evaluator using explicit interval polynomials.

See research/nested_trial_validation/PROOF.md. No primary implementation is
imported. Frozen coefficients pass through exact rational JSON registration.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, factorial
import hashlib, json
import numpy as np
from numpy.polynomial import legendre as leg
from scipy.special import expit, poch
from fast_gaussian_trial_field import FastGaussianTrialField
from gaussian_trial_field import smooth_step_jets, logpolar_derivatives
from fast_two_series import ORDERS
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
GAUSSIAN=BASE/'external_exports/T1_gaussian_nk_20261029T031456.661955Z'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def spline_interval_polynomials(breaks,degree=5):
    """Return [interval,basis,power] in powers of x - left endpoint."""
    breaks=np.asarray(breaks,float)
    if np.any(np.diff(breaks)<=0):raise ValueError('Nonincreasing knots')
    knots=np.r_[np.repeat(breaks[0],degree),breaks,np.repeat(breaks[-1],degree)]
    result=[]
    for left,right in zip(breaks[:-1],breaks[1:]):
        previous=np.zeros((len(knots)-1,degree+1))
        midpoint=(left+right)/2
        previous[:,0]=((knots[:-1]<=midpoint)&(midpoint<knots[1:])).astype(float)
        for d in range(1,degree+1):
            current=np.zeros((len(knots)-d-1,degree+1))
            for i in range(len(current)):
                den=knots[i+d]-knots[i]
                if den:
                    current[i]+=(left-knots[i])/den*previous[i]
                    current[i,1:]+=previous[i,:-1]/den
                den=knots[i+d+1]-knots[i+1]
                if den:
                    current[i]+=(knots[i+d+1]-left)/den*previous[i+1]
                    current[i,1:]-=previous[i+1,:-1]/den
            previous=current
        result.append(previous)
    return np.array(result)

def product_jets(a,b):
    return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])

def envelope_jets(x,nu):
    v=expit(2*x);g=np.exp(x-nu*np.logaddexp(0.,2*x));q=1-2*nu*v
    return g,g*q,g*(q*q-4*nu*v*(1-v))

class NestedTrialField:
    def __init__(self,registered_json):
        self.registration=Path(registered_json)
        record=json.loads(self.registration.read_text())
        if record['schema']!='e4.exact-nested-field.v1':raise ValueError('Unknown schema')
        for rel,digest in record['input_sha256'].items():
            if sha(ROOT/rel)!=digest:raise ValueError('Changed input: '+rel)
        self.record=record;self.export=ROOT/record['export'];self.name=record['name']
        self.parameters=json.loads((self.export/'results'/self.name/'summary.json').read_text())
        self.level=int(record['level']);self.na=int(record['angular_count']);self.ninterval=int(record['intervals']);self.nb=self.ninterval+5
        self.c_l=float(Fraction(record['c_l']));self.p=1/(2*self.c_l);self.K=float(Fraction(record['K']))
        self.coefficients=np.array([float(Fraction(v))for v in record['coefficients']])
        if self.coefficients.shape!=(4+(self.nb+4)*self.na,):raise ValueError('Coefficient shape')
        self.source=self.coefficients[:4]
        self.interior=self.coefficients[4:4+self.nb*self.na].reshape(self.nb,self.na)
        self.tails=self.coefficients[4+self.nb*self.na:].reshape(4,self.na)
        self.start=FastGaussianTrialField(GAUSSIAN,'gaussian_'+self.parameters['tag']+'_n20')
        with np.load(self.export/'inputs'/self.parameters['tag']/'start.npz',allow_pickle=False) as f:
            if not np.array_equal(f['coef'],self.start.coefficients):raise ValueError('Different starting field')
        if self.c_l!=self.start.c_l:raise ValueError('Different exponent')
        self.ps=self.start.ps;self.pz=self.start.pz+self.source[0]
        self.breaks=np.array([float(Fraction(v))for v in record['binary_breaks']])
        self.basis_polynomials=spline_interval_polynomials(self.breaks)
        self.polynomials=np.einsum('ibp,bj->ipj',self.basis_polynomials,self.interior)
        self.angular=[];self.tail_angular=[]
        for j in range(self.na):
            c=np.zeros(2*j+1);c[-1]=1;c=leg.legmul(c,[0.,1.]);self.angular.append(c)
            self.tail_angular.append(np.array([0.,2/5,0.,-2/5]) if j==1 else c)
        self.angular_matrices=[];self.tail_matrices=[]
        for order in range(3):
            matrices=[]
            for polys in [self.angular,self.tail_angular]:
                a=np.zeros((2*self.na,self.na))
                for j,c in enumerate(polys):
                    d=leg.legder(c,order);a[:len(d),j]=d
                matrices.append(a)
            self.angular_matrices.append(matrices[0]);self.tail_matrices.append(matrices[1])
        self.source_terms=[(self.source[0],0,1,self.p+1),(self.source[1],2,0,self.p+2),
                           (self.source[2],1,1,self.p+2),(self.source[3],0,2,self.p+2)]
        self.source_derivative_terms={}
        for A,B in ORDERS:
            row=[]
            for C,j,k,nu in self.source_terms:
                for i in range(min(A,j)+1):
                    for ell in range(min(B,k)+1):
                        h=A+B-i-ell
                        c=C*comb(A,i)*comb(B,ell)*factorial(j)/factorial(j-i)*factorial(k)/factorial(k-ell)*(-1)**h*poch(nu,h)
                        if c:row.append((c,j-i,k-ell,-nu-h))
            self.source_derivative_terms[A,B]=row

    def spline_values(self,x):
        x=np.asarray(x,float).ravel();out=[np.zeros((len(x),self.na))for _ in range(3)]
        hit=(x>self.breaks[0])&(x<self.breaks[-1])
        xx=x[hit];indices=np.searchsorted(self.breaks,xx,side='right')-1;u=xx-self.breaks[indices]
        selected=self.polynomials[indices]
        for d in range(3):
            y=np.zeros((len(xx),self.na))
            for p in range(5,d-1,-1):y=y*u[:,None]+selected[:,p,:]*factorial(p)/factorial(p-d)
            out[d][hit]=y
        return out

    def correction_values(self,x,mu):
        x,mu=np.broadcast_arrays(np.asarray(x,float),np.asarray(mu,float));shape=x.shape;x=x.ravel();mu=mu.ravel()
        V=leg.legvander(mu,2*self.na-1)
        angular=[V@a for a in self.angular_matrices];tailangle=[V@a for a in self.tail_matrices]
        left=smooth_step_jets(x+7);right=smooth_step_jets(7-x);right=(right[0],-right[1],right[2])
        common=product_jets(envelope_jets(x,self.p),product_jets(left,right))
        poly=self.spline_values(x)
        interior=product_jets(tuple(p for p in poly),tuple(a[:,None]for a in common))
        tau=smooth_step_jets((x-2)/2);tau=(tau[0],tau[1]/2,tau[2]/4)
        tailradial=[product_jets(envelope_jets(x,nu),tau)for nu in [self.p,2*self.p,self.p+1,3*self.p]]
        tailmixed=[np.stack([r[d]for r in tailradial],axis=1)@self.tails for d in range(3)]
        return tuple((np.sum(interior[i]*angular[j],axis=1)+np.sum(tailmixed[i]*tailangle[j],axis=1)).reshape(shape)
                     for i,j in [(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)])

    def source_F(self,s,t):
        u=1+s+t;out={}
        for ab,terms in self.source_derivative_terms.items():
            value=np.zeros_like(s)
            for C,j,k,nu in terms:value+=C*s**j*t**k*u**nu
            out[ab]=value
        return out

    def jets(self,r,z):
        r,z=np.broadcast_arrays(np.asarray(r,float),np.asarray(z,float))
        if np.any(r<0):raise ValueError('Negative cylindrical radius')
        shape=r.shape;r=r.ravel();z=z.ravel();s=r*r;t=z*z;R=np.hypot(r,z)
        base=self.start.jets(r,z);extra=self.source_F(s,t);F,Fs,Ft,Fss,Fst,Ftt=[extra[ab]for ab in ORDERS]
        d=dict(phi=z*F,phi_s=z*Fs,phi_z=F+2*t*Ft,phi_ss=z*Fss,phi_sz=Fs+2*t*Fst,phi_zz=2*z*(3*Ft+2*t*Ftt))
        hit=R>np.exp(-7.)
        if np.any(hit):
            mu=z[hit]/R[hit];add=logpolar_derivatives(R[hit],mu,self.correction_values(np.log(R[hit]),mu))
            for key in d:d[key][hit]+=add[key]
        for key in d:d[key]+=base[key]
        phi,ps,pz,pss,psz,pzz=[d[k]for k in ['phi','phi_s','phi_z','phi_ss','phi_sz','phi_zz']]
        wz=self.c_l*z+2*phi+2*s*ps;az=np.divide(wz,z,out=self.c_l+2*pz+2*s*psz,where=z!=0)
        d.update(eta_phi=-8*ps-4*s*pss-pzz,log_r_speed=self.c_l-pz,log_z_speed=az,A=2*pz-1,
                 A_r=4*r*psz,A_z=2*pzz,Drr=self.c_l-pz-2*s*psz,Drz=-r*pzz,Dzr=8*r*ps+4*r*s*pss,Dzz=self.c_l+2*pz+2*s*psz)
        return {key:value.reshape(shape)for key,value in d.items()}

    def phi(self,s,z):
        s=np.asarray(s,float)
        if np.any(s<0):raise ValueError('Negative squared radius')
        return self.jets(np.sqrt(s),z)['phi']
