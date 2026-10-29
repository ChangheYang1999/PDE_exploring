"""Equivalent contractions for the verifier's Gaussian trial-field formulas."""
import numpy as np
from numpy.polynomial import legendre as leg
from scipy.special import expit, poch
from gaussian_trial_field import GaussianTrialField, smooth_step_jets
from fast_two_series import ORDERS

class FastGaussianTrialField(GaussianTrialField):
    def __init__(self,export,name):
        super().__init__(export,name)
        self.angular_matrices=[]
        for k in range(3):
            matrix=np.zeros((2*self.n,self.n))
            for j,c in enumerate(self.angular_coefficients):
                d=leg.legder(c,k);matrix[:len(d),j]=d
            self.angular_matrices.append(matrix)
        self.source_constants={ab:(float((-1)**sum(ab)*poch(self.p+1,sum(ab))),
            float((-1)**(sum(ab)-1)*poch(self.p+1,sum(ab)-1)) if sum(ab)>0 else 0.)for ab in ORDERS}

    def gaussian_values(self,x,m):
        x,m=np.broadcast_arrays(np.asarray(x,float),np.asarray(m,float))
        shape=x.shape;x=x.ravel();m=m.ravel()
        C=smooth_step_jets((x+6)/2);C=(C[0],C[1]/2,C[2]/4)
        d=(x[:,None]-self.centers)/self.width
        G=np.exp(-.5*d*d);Gx=-d*G/self.width;Gxx=(d*d-1)*G/self.width**2
        B=[np.empty((len(x),self.n)) for _ in range(3)]
        B[0][:,:-1]=C[0][:,None]*G
        B[1][:,:-1]=C[1][:,None]*G+C[0][:,None]*Gx
        B[2][:,:-1]=C[2][:,None]*G+2*C[1][:,None]*Gx+C[0][:,None]*Gxx
        tail=smooth_step_jets((x-2)/4)
        for k in range(3):B[k][:,-1]=tail[k]/4**k
        v=expit(2*x);g=np.exp(x-self.p*np.logaddexp(0.,2*x))
        q=1-2*self.p*v;qx=-4*self.p*v*(1-v)
        radial=[g[:,None]*B[0],g[:,None]*(B[1]+q[:,None]*B[0]),
            g[:,None]*(B[2]+2*q[:,None]*B[1]+(qx+q*q)[:,None]*B[0])]
        V=leg.legvander(m,2*self.n-1)
        angular=[V@matrix for matrix in self.angular_matrices]
        mixed=[a@self.theta for a in radial]
        return tuple(np.sum(mixed[i]*angular[j],axis=1).reshape(shape)for i,j in [(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)])

    def source_F(self,s,t):
        u=1+s+t;linear=self.b_s*s+self.b_z*t
        return {(a,b):u**(-self.p-1-a-b)*(c*linear+d*u*(a*self.b_s+b*self.b_z))
                for (a,b),(c,d) in self.source_constants.items()}
