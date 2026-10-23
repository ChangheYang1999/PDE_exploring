"""Exact power substitution for the independently implemented hydrostatic inverse."""
import numpy as np
from independent_hydrostatic import VerticalInverse,finite_nodes,finite_rule

class PowerVerticalInverse(VerticalInverse):
    def at(self,x,y):
        x=float(x);y=float(y);xx=abs(x);yy=abs(y);sx=-1 if x<0 else 1;sy=-1 if y<0 else 1
        R=self.tail_scale*max(self.inner_scale,xx,yy,1.)
        inner,iw=finite_nodes(0.,yy,self.order,self.inner_scale)
        outer,ow=finite_nodes(yy,R,self.order,self.inner_scale)
        z,lw=finite_rule(self.tail_order);u=(z+1)/2;P=1/(1-self.p)
        tails=R/u**P;weights=lw/2*P*R*u**(-P-1)
        jt=self.jet(xx,tails);jo=self.jet(xx,outer);ji=self.jet(xx,inner)
        tx=float(np.dot(weights,jt[:,1]));txx=float(np.dot(weights,jt[:,3]))
        Ix=float(np.dot(ow,jo[:,1]))+tx;Ixx=float(np.dot(ow,jo[:,3]))+txx
        Jx=float(np.dot(iw*inner,ji[:,1]));Jxx=float(np.dot(iw*inner,ji[:,3]))
        V1=-sx*Ix;V2=sy*(Jxx+yy*Ixx);Phi=sx*sy*(Jx+yy*Ix)
        if x==0:V1=0.;Phi=0.
        if y==0:V2=0.;Phi=0.
        return dict(V=[V1,V2],Phi=Phi,dV2_dy=Ixx,tail_V=[-sx*tx,sy*yy*txx],R_split=R,finite_order=self.order,tail_order=self.tail_order,tail_power=P,tail_method='t=R/u**P, ordinary Gauss-Legendre')
