"""Extended tensor-grid vorticity from the exact finite potential identity.

See research/vorticity_potentials/PROOF.md. Positive radii only; the Cartesian
SpatialField evaluator handles the origin. No production numerical imports.
"""
import numpy as np
from extended_grid import DT,ExtendedGridField
from extended_spatial import Jet3,SpatialField

class VorticityGrid:
    def __init__(self,field,directions):
        self.angular=ExtendedGridField(field,directions)
        self.spatial=SpatialField(field)
        self.directions=self.angular.directions
        self.ell=self.angular.ell
        self.c=self.spatial.c;self.omega=self.spatial.omega
    def synthesize(self,radii,f,g,derivative=True):
        r=np.asarray(radii,dtype=DT).reshape(-1,1);q=r*r;ell=self.ell
        if np.any(r<=0):raise ValueError('positive radii required; use SpatialField at the origin')
        a=(ell+1)*g.v+2*q*g.d;b=-2*ell*g.d
        vc=[f.v*r**ell,a*r**(ell-1),b*r**(ell+1)]
        u=sum(c@v for c,v in zip(vc,self.angular.vectors)).reshape(len(r),len(self.directions),3)
        if not derivative:return u
        ap=(ell+3)*g.d+2*q*g.h;bp=-2*ell*g.h
        dc=[2*f.d*r**(ell+1),f.v*r**(ell-1),a*r**(ell-2),2*ap*r**ell,b*r**ell,2*bp*r**(ell+2)]
        du=sum(c@v for c,v in zip(dc,self.angular.matrices)).reshape(len(r),len(self.directions),3,3)
        return u,du
    def values(self,radii):
        r=np.asarray(radii,dtype=DT).reshape(-1,1);q=r*r
        f,g=self.spatial.radial(q)
        u,du=self.synthesize(r,f,g)
        b=Jet3(-4*q*g.h-(4*self.ell+6)*g.d,-4*q*g.t-(4*self.ell+10)*g.h)
        om,dom=self.synthesize(r,b,f)
        fl,gl=self.spatial.radial(q,stable=True)
        linear=self.synthesize(r,fl,gl,False)
        bl=Jet3(-4*q*gl.h-(4*self.ell+6)*gl.d)
        lv=self.synthesize(r,bl,fl,False)
        nonlinear=np.einsum('raij,raj->rai',dom,u)-np.einsum('raij,raj->rai',du,om)
        result={'U':u,'DU':du,'Omega':om,'DOmega':dom,'linear':linear,'linear_vorticity':lv,'nonlinear_vorticity':nonlinear,'vorticity_residual':lv+nonlinear,'divergence':np.trace(du,axis1=-2,axis2=-1)}
        if not all(np.isfinite(a).all() for a in result.values()):raise FloatingPointError('nonfinite tensor vorticity')
        return result


class VorticityPoints:
    """Cartesian scattered-point evaluation, including the origin."""
    def __init__(self,field):self.spatial=SpatialField(field)
    def values(self,points):
        from extended_grid import real_angular
        from extended_spatial import assemble,curl
        p=np.asarray(points,dtype=DT).reshape(-1,3);sf=self.spatial
        table=real_angular(p,sf.modes)
        angular=(table[:,:,0],table[:,:,1:4],table[:,:,4:].reshape(len(p),len(sf.modes),3,3),None)
        q=np.sum(p*p,axis=1).reshape(-1,1);f,g=sf.radial(q)
        u,du,_=assemble(p,sf.ell,f,g,angular,hessian=False)
        b=Jet3(-4*q*g.h-(4*sf.ell+6)*g.d,-4*q*g.t-(4*sf.ell+10)*g.h)
        om,dom,_=assemble(p,sf.ell,b,f,angular,hessian=False)
        fl,gl=sf.radial(q,stable=True)
        linear,dlinear,_=assemble(p,sf.ell,fl,gl,angular,hessian=False)
        lv=curl(dlinear)
        nonlinear=np.einsum('nij,nj->ni',dom,u)-np.einsum('nij,nj->ni',du,om)
        result={'U':u,'DU':du,'Omega':om,'DOmega':dom,'linear':linear,'linear_vorticity':lv,'nonlinear_vorticity':nonlinear,'vorticity_residual':lv+nonlinear,'divergence':np.trace(du,axis1=-2,axis2=-1)}
        if not all(np.isfinite(a).all() for a in result.values()):raise FloatingPointError('nonfinite scattered vorticity')
        return result
