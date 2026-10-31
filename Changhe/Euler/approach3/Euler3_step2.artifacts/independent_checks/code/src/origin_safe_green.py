"""Log-graded outer Green integration on the origin source panel."""
import math
import numpy as np
from partial_panel_green import PartialPanelGreen,barycentric_matrix


class OriginSafeGreen(PartialPanelGreen):
    def __init__(self,pressure,partial_order=None,max_log_width=math.log(2)):
        if not 0<max_log_width<=math.log(2):
            raise ValueError('Positive log width at most log(2) required')
        super().__init__(pressure,partial_order)
        self.max_log_width=float(max_log_width)
        self.counters['origin_graded_radii']=0

    def direct_coefficients(self,radii):
        radii=np.asarray(radii,dtype=float).reshape(-1)
        pc,dp=super().direct_coefficients(radii)
        b=self.edges[1]
        selected=np.flatnonzero((radii>0)&(radii<b/2))
        modes=np.flatnonzero(self.ell>=2)
        if not len(selected) or not len(modes):return pc,dp
        ell=self.ell[modes];den=2*ell+1;qpanel=self.q[:self.nr,modes]
        for index in selected:
            r=radii[index];si=r*self.qt
            qi=barycentric_matrix(2*si/b-1,self.t,self.bw)@qpanel
            inner=(r*self.qw[:,None]*qi*r*(si[:,None]/r)**(ell+2)).sum(axis=0)
            outer=(r/b)**ell*self.outer[1,modes]
            length=math.log(b/r);count=max(1,math.ceil(length/self.max_log_width))
            edges=np.linspace(0,length,count+1)
            terms=[]
            for lo,hi in zip(edges[:-1],edges[1:]):
                t=lo+(hi-lo)*self.qt;s=r*np.exp(t)
                q=barycentric_matrix(2*s/b-1,self.t,self.bw)@qpanel
                terms.append(((hi-lo)*self.qw[:,None]*q*s[:,None]**2*(r/s[:,None])**ell).sum(axis=0))
            outer+=np.sum(terms,axis=0)
            pc[index,modes]=(inner+outer)/den
            dp[index,modes]=(-(ell+1)*inner+ell*outer)/(r*den)
        self.counters['origin_graded_radii']+=len(selected)
        return pc,dp
