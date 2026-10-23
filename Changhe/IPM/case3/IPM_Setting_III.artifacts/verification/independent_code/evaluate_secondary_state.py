"""Scalar Cartesian reconstruction and adaptive center checks for the secondary basis."""
import numpy as np
from scipy.integrate import quad
from evaluate_smooth_state import ReconstructedSmooth,main

class ReconstructedSecondary(ReconstructedSmooth):
    branch='SECONDARY cubic-axis, globally divisible by y^3'
    def __init__(self,path):
        super().__init__(path)
        with np.load(path,allow_pickle=False) as d:
            if int(d['axis_order'])!=3:raise ValueError('Secondary cubic-axis state required')
    def rho(self,x,y):
        original=super().rho(x,y)
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
        scale=np.maximum(self.L,np.hypot(x,y));xx=x/scale;yy=y/scale;ll=self.L/scale
        return original*yy*yy/(ll*ll+xx*xx+yy*yy)
    def center_and_tail(self):
        j=np.arange(self.N+1);sign=(-1.)**j
        center=self.coeff@sign;derivative=self.coeff@np.where(j==0,0.,-sign*j*j)
        e=float(center[0]/self.L**2);common=self.a*(-center[0]+2*derivative[0])/self.L**2
        d1=center[1] if self.M>1 else 0.
        f=float((common+d1/self.L**2-center[0]/self.L**2)/self.L**2)
        g=float((common-d1/self.L**2-center[0]/self.L**2)/self.L**2)
        d3=(-.25,.375,-.375,.125);d5=(0.,-.125,.375,-.375,.125)
        def integrands(u):
            sig=1-u**(1/self.a);t=1-2*u
            cs=sum(d3[k]*sig**k*self.polynomial(k,t) for k in range(min(self.M,len(d3))))/(2*self.a)
            hh=2*u**(1/self.a)/(self.a*self.L**2)*sum(d5[k]*sig**(k-1)*self.polynomial(k,t) for k in range(1,min(self.M,len(d5))))
            return cs,hh
        rows=[]
        for tol in (1e-8,1e-10,1e-12):
            c,ce=quad(lambda u:integrands(u)[0],0,1,epsabs=tol,epsrel=tol,limit=250)
            H,he=quad(lambda u:integrands(u)[1],0,1,epsabs=tol,epsrel=tol,limit=250)
            rows.append({'requested_tolerance':tol,'c':c,'c_error_estimate':ce,'H':H+e/8,'H_error_estimate':he})
        c=rows[-1]['c'];H=rows[-1]['H'];K=float(self.L**(1-self.p)*sum((-1.)**np.arange(self.M)*self.coeff.sum(axis=1)))
        return {'branch':self.branch,'a0':0.,'b_cubic_x2y':0.,'e3':e,'K':K,'secondary_scale':(K/e)**(1/(3-self.p)) if e and K/e>0 else None,'adaptive_center':rows,'cubic_axis_normalization_defect':self.cl+c-1/3,'source_eigenvalues':[self.cl-c,self.cl+c],'f_fifth_x2y3':f,'g_fifth_y5':g,'T5x':2*(2*self.cl-1/3)*f+4.5*e*H,'T5y':2*g/3-1.5*e*H,'scope':'Separate secondary branch. a0 identically zero is intentional and cannot meet the primary endpoint.'}
if __name__=='__main__':main(reconstructor=ReconstructedSecondary,output_root='evidence/secondary_evaluations')
