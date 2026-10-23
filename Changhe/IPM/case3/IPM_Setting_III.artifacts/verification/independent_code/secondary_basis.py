"""Restricted smooth y^3-leading basis and independently derived center rows."""
import math
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.special import roots_jacobi
from smooth_basis import SmoothBasis

class SecondaryBasis(SmoothBasis):
    def evaluate(self,x,y,gradient=False):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
        scale=np.maximum(self.L,np.hypot(x,y));xx=x/scale;yy=y/scale;ll=self.L/scale
        den=ll*ll+xx*xx+yy*yy;factor=yy*yy/den
        original=super().evaluate(x,y,gradient)
        if not gradient:return factor[...,None]*original
        value,gx,gy=original
        fx=-2*xx*yy*yy/(scale*den*den)
        fy=2*yy*(ll*ll+xx*xx)/(scale*den*den)
        return factor[...,None]*value,factor[...,None]*gx+fx[...,None]*value,factor[...,None]*gy+fy[...,None]*value
    def center_slope(self):return np.zeros(self.size)
    def cubic_axis_row(self):return super().center_slope()/self.L**2
    def moment(self,power):
        z,wt=roots_jacobi(max(32,self.N+2),0,power);u=(z+1)/2
        return (wt/2**(power+1))@C.chebvander(1-2*u,self.N)
    def sigma_moment(self,k,extra=0):
        return sum((-1.)**j*math.comb(k,j)*self.moment((j+extra)/self.a) for j in range(k+1))
    def center_strain(self):
        row=np.zeros((self.M,self.N+1))
        for k,d in enumerate((-.25,.375,-.375,.125)[:self.M]):row[k]=d*self.sigma_moment(k)/(2*self.a)
        return row.reshape(-1)
    def quartic_stream_difference(self):
        row=(self.cubic_axis_row()/8).reshape(self.M,self.N+1)
        for k,d in enumerate((0.,-.125,.375,-.375,.125)[:self.M]):
            if k:row[k]+=2*d*self.sigma_moment(k-1,1)/(self.a*self.L**2)
        return row.reshape(-1)
    def fifth_density_rows(self):
        br,er=super().cubic_density_rows();ar=super().center_slope()
        return br/self.L**2-ar/self.L**4,er/self.L**2-ar/self.L**4
    def metadata(self):return {**super().metadata(),'axis_order':3,'factor':'y^2/(L^2+r^2)'}
