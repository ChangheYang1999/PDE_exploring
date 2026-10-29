"""Independent Cartesian derivatives for the frozen Gaussian T1 trial fields.

Only numeric metadata and NPZ coefficients are read from the foreign export.
No foreign code is imported. See research/gaussian_trial_validation/PROOF.md.
"""
from pathlib import Path
from math import comb, factorial
import json
import numpy as np
from numpy.polynomial import legendre as leg
from scipy.special import expit
from fast_two_series import FastTwoSeries, ORDERS


def smooth_step_jets(t):
    t = np.asarray(t, dtype=float)
    value = np.zeros_like(t); first = value.copy(); second = value.copy()
    value[t >= 1] = 1
    hit = (t > 0) & (t < 1)
    u = t[hit]
    v = expit(1/(1-u)-1/u)
    a = 1/u**2+1/(1-u)**2
    b = -2/u**3+2/(1-u)**3
    value[hit] = v
    first[hit] = v*(1-v)*a
    second[hit] = v*(1-v)*((1-2*v)*a*a+b)
    return value, first, second


def logpolar_derivatives(R, m, values):
    P, X, XX, M, XM, MM = values
    s = (X-m*M)/(2*R**2)
    z = (m*X+(1-m*m)*M)/R
    ss = (XX-2*m*XM+m*m*MM-2*X+3*m*M)/(4*R**4)
    sz = (m*XX+(1-2*m*m)*XM-m*(1-m*m)*MM-2*m*X+(3*m*m-1)*M)/(2*R**3)
    zz = (m*m*XX+2*m*(1-m*m)*XM+(1-m*m)**2*MM+(1-2*m*m)*X-3*m*(1-m*m)*M)/R**2
    return dict(phi=P, phi_s=s, phi_z=z, phi_ss=ss, phi_sz=sz, phi_zz=zz)


class GaussianTrialField:
    def __init__(self, export, name):
        self.export = Path(export); self.name = name
        folder = self.export/'results'/name
        self.parameters = json.loads((folder/'summary.json').read_text())
        self.meta = json.loads((self.export/'inputs'/self.parameters['tag']/'metadata.json').read_text())
        if self.parameters['basis'] != 'gaussian':
            raise ValueError('Only the documented Gaussian production space is implemented')
        with np.load(folder/'checkpoint.npz', allow_pickle=False) as data:
            self.coefficients = data['coef'].copy()
        self.n = int(self.parameters['n'])
        if self.n < 3 or self.coefficients.shape != (self.n*self.n+2,):
            raise ValueError('Unexpected coefficient layout')
        self.c_l = float(self.parameters['c_l']); self.p = 1/(2*self.c_l)
        self.seed = FastTwoSeries(self.meta)
        if self.seed.c_l != self.c_l: raise ValueError('Inconsistent exponent')
        self.b_s, self.b_z = self.coefficients[:2]
        self.theta = self.coefficients[2:].reshape(self.n,self.n)
        self.centers = np.linspace(-3.8,5.,self.n-1)
        self.width = 1.2*(self.centers[1]-self.centers[0])
        self.angular_coefficients = []
        for j in range(self.n):
            c = np.zeros(2*j+1); c[-1] = 1
            self.angular_coefficients.append(leg.legmul(c, [0.,1.]))
        self.ps = self.seed.ps+self.b_s; self.pz = self.seed.pz+self.b_z
        self.K = float(self.parameters['K'])

    def gaussian_values(self, x, m):
        """Paired log-radius/angular values, through total derivative order two."""
        x,m = np.broadcast_arrays(np.asarray(x,float), np.asarray(m,float))
        shape=x.shape; x=x.ravel(); m=m.ravel()
        cutoff = smooth_step_jets((x+6)/2)
        cutoff = (cutoff[0],cutoff[1]/2,cutoff[2]/4)
        d=(x[:,None]-self.centers)/self.width
        G=np.exp(-.5*d*d); Gx=-d*G/self.width; Gxx=(d*d-1)*G/self.width**2
        B=[np.empty((len(x),self.n)) for _ in range(3)]
        B[0][:,:-1]=cutoff[0][:,None]*G
        B[1][:,:-1]=cutoff[1][:,None]*G+cutoff[0][:,None]*Gx
        B[2][:,:-1]=cutoff[2][:,None]*G+2*cutoff[1][:,None]*Gx+cutoff[0][:,None]*Gxx
        tail=smooth_step_jets((x-2)/4)
        for k in range(3): B[k][:,-1]=tail[k]/4**k
        v=expit(2*x); g=np.exp(x-self.p*np.logaddexp(0.,2*x))
        ell=1-2*self.p*v; ellx=-4*self.p*v*(1-v)
        radial=[g[:,None]*B[0],g[:,None]*(B[1]+ell[:,None]*B[0]),
                g[:,None]*(B[2]+2*ell[:,None]*B[1]+(ellx+ell*ell)[:,None]*B[0])]
        angular=[np.stack([leg.legval(m,leg.legder(c,k)) for c in self.angular_coefficients],axis=1) for k in range(3)]
        mixed=[a@self.theta for a in radial]
        return tuple(np.sum(mixed[i]*angular[j],axis=1).reshape(shape) for i,j in [(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)])

    def source_F(self,s,t):
        out={}; exponent=self.p+1; u=1+s+t
        for A,B in ORDERS:
            value=np.zeros_like(s)
            for C,j,k in [(self.b_s,1,0),(self.b_z,0,1)]:
                if C==0: continue
                for i in range(min(A,j)+1):
                    for l in range(min(B,k)+1):
                        h=A+B-i-l; rising=1.
                        for q in range(h): rising*=exponent+q
                        factor=C*comb(A,i)*comb(B,l)*factorial(j)/factorial(j-i)*factorial(k)/factorial(k-l)*(-1)**h*rising
                        value+=factor*s**(j-i)*t**(k-l)*u**(-exponent-h)
            out[A,B]=value
        return out

    def jets(self,r,z):
        r,z=np.broadcast_arrays(np.asarray(r,float),np.asarray(z,float))
        if np.any(r<0): raise ValueError('Nonnegative cylindrical radius required')
        shape=r.shape; r=r.ravel();z=z.ravel();s=r*r;t=z*z;R=np.hypot(r,z)
        core=self.seed.all_F(s,t);extra=self.source_F(s,t)
        F,Fs,Ft,Fss,Fst,Ftt=[core[ab]+extra[ab] for ab in ORDERS]
        d=dict(phi=z*F,phi_s=z*Fs,phi_z=F+2*t*Ft,phi_ss=z*Fss,
               phi_sz=Fs+2*t*Fst,phi_zz=2*z*(3*Ft+2*t*Ftt))
        hit=R>np.exp(-6.)
        if np.any(hit):
            m=z[hit]/R[hit]
            correction=logpolar_derivatives(R[hit],m,self.gaussian_values(np.log(R[hit]),m))
            for key in d:d[key][hit]+=correction[key]
        phi,ps,pz,pss,psz,pzz=[d[k] for k in ['phi','phi_s','phi_z','phi_ss','phi_sz','phi_zz']]
        wz=self.c_l*z+2*phi+2*s*ps
        # The z=0 value uses the even limit, which is c_l+2phi_z+2s phi_sz.
        az=np.divide(wz,z,out=self.c_l+2*pz+2*s*psz,where=z!=0)
        d.update(eta_phi=-8*ps-4*s*pss-pzz,
                 log_r_speed=self.c_l-pz,log_z_speed=az,A=2*pz-1,
                 A_r=4*r*psz,A_z=2*pzz,Drr=self.c_l-pz-2*s*psz,
                 Drz=-r*pzz,Dzr=8*r*ps+4*r*s*pss,Dzz=self.c_l+2*pz+2*s*psz)
        return {k:v.reshape(shape) for k,v in d.items()}

    def phi(self,s,z):
        s=np.asarray(s,float)
        if np.any(s<0): raise ValueError('Nonnegative s required')
        return self.jets(np.sqrt(s),z)['phi']
