"""Independent stable linear momentum term from the proved radial identity.

No production imports. Internal scratch jets have valid values/first derivatives
only; their second derivatives are not used or exposed.
"""
import numpy as np
import torch
from radial_primary import RadialJet2
from tensor_grid import decimal_angular


def _radial_first(field,rho):
    c,w=field.c_l,field.omega
    q=RadialJet2(rho,torch.ones_like(rho))
    s=(q+field.r0**2).power(.5);sr=s*(1/field.r0)
    core=(q+field.r0**2).power(-1)*field.r0**2
    logsr=RadialJet2(.5*torch.log1p(rho/field.r0**2),.5/(rho+field.r0**2),-.5/(rho+field.r0**2)**2)
    phase=logsr*(field.ms*w/c);cs,sn=phase.cos(),phase.sin()
    xx=q*(s+field.r0).power(-2);tt=2*xx-1
    cheb=[q*0+1,tt]
    for _ in range(2,max(len(v) for v in field.coeff.values())):cheb.append(2*tt*cheb[-1]-cheb[-2])
    ratio=q*(q+float(field.channels.get('R1') or field.r0)**2).power(-1)
    damp=q*0+1
    for _ in range(int(field.channels['core_damp'])):damp=damp*ratio
    def amplitude(name):
        co=field.coeff[name];b=cheb[0]*co[0]
        for k in range(1,len(co)):b=b+cheb[k]*co[k]
        return b if name in ('A','C') else damp*b
    def twist(b):return b*cs-b.select(field.partner)*field.sign*sn
    def term(name,nu,delta,twisted=True):
        b=amplitude(name)
        # Only value/first derivative of this derivative jet will be consumed.
        bq=RadialJet2(b.d,b.h,torch.zeros_like(b.h))
        value=b*(delta+c*nu*core)+2*c*q*bq
        rotation=b.select(field.partner)*(w*field.sign*field.ms)
        value=value+(core*rotation if twisted else rotation)
        if twisted:value=twist(value)
        return sr.power(-nu)*value
    tor=term('A',field.alpha+field.ls,0.)
    pol=term('C',field.alpha+field.ls-1,0.)
    if len(field.coeff['B']):tor=tor+term('B',2*field.alpha+1+field.ls,-1.)
    if len(field.coeff['D']):pol=pol+term('D',2*field.alpha+field.ls,-1.)
    if len(field.coeff['E']):pol=pol+term('E',2*field.ls+1,1-c*(field.ls+3),False)*(field.ls>=2)
    return tor.v,pol.v,pol.d


def linear_values(field,points,cache_dir=None):
    """Return A U at physical points, using fixed full field coefficients."""
    points=np.asarray(points,dtype=np.float64)
    if points.ndim!=2 or points.shape[1]!=3 or not np.isfinite(points).all():raise ValueError('finite Nx3 points required')
    if not len(points):return np.empty((0,3),dtype=np.float64)
    radii=np.linalg.norm(points,axis=1);positive=radii>0
    normalized=points.copy();normalized[positive]/=radii[positive,None]
    angular=decimal_angular(normalized,field.modes,cache_dir)
    y=torch.as_tensor(points,device=field.device,dtype=torch.float64)
    r=torch.as_tensor(radii[:,None],device=field.device,dtype=torch.float64)
    n=torch.as_tensor(normalized,device=field.device,dtype=torch.float64)
    tab=torch.as_tensor(angular,device=field.device,dtype=torch.float64)
    H,h=tab[:,:,0],tab[:,:,1:4]
    with torch.no_grad():
        f,g,gq=_radial_first(field,r*r)
        ell=field.ls
        powers0=r**ell;powers1=r**(ell-1);powers2=r**(ell+1)
        cross=torch.linalg.cross(h,n[:,None,:].expand_as(h),dim=-1)
        vals=(f*powers0)[:,:,None]*cross+((ell+1)*g+2*r*r*gq)[:,:,None]*powers1[:,:,None]*h-(2*ell*gq*powers2)[:,:,None]*n[:,None,:]*H[:,:,None]
        # At the origin normalized==0, so only degree-one grad H survives.
        ans=vals.sum(1)
        if not bool(torch.isfinite(ans).all()):raise FloatingPointError('nonfinite independent linear velocity')
    return ans.cpu().numpy()
