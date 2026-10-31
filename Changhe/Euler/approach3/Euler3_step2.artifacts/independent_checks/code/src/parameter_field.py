"""Analytic physical-parameter derivatives, independent of production AD.

The underlying radial spatial jets come from the frozen independent route.
Parameter differentiation here uses explicit envelope and phase formulas.
"""
import copy
import numpy as np
import torch
from radial_primary import RadialPrimaryExchangeField, RadialJet2


class ParameterField(RadialPrimaryExchangeField):
    def at(self, c_l, omega):
        other = copy.copy(self)
        other.c_l, other.omega = float(c_l), float(omega)
        other.alpha = (1.0-other.c_l)/other.c_l
        other.kappa = other.radial_ratio = other.omega/other.c_l
        return other

    def radial_with_parameter(self, rho, parameter=None, exterior=False):
        q = RadialJet2(rho, torch.ones_like(rho))
        sr = (q if exterior else q+self.r0**2).power(.5)*(1/self.r0)
        if exterior:
            logsr = sr.log()
        else:
            # Preserve tiny core twists without subtracting nearly equal floats.
            logsr = RadialJet2(
                0.5*torch.log1p(rho/self.r0**2),
                0.5/(rho+self.r0**2),
                -0.5/(rho+self.r0**2)**2,
            )
        angle = logsr*(self.omega/self.c_l)
        cs, sn = (angle*self.ms).cos(), (angle*self.ms).sin()
        if exterior:
            cheb = [q*0+1]
        else:
            xx = q*((q+self.r0**2).power(.5)+self.r0).power(-2)
            tt = 2*xx-1
            cheb = [q*0+1, tt]
            for _ in range(2, max(len(v) for v in self.coeff.values())):
                cheb.append(2*tt*cheb[-1]-cheb[-2])

        def amplitude(name):
            a = self.coeff[name]
            if exterior:
                return (q*0+1)*a.sum(0)
            v = cheb[0]*a[0]
            for k in range(1, len(a)):
                v = v+cheb[k]*a[k]
            return v

        if parameter not in (None, 'c_l', 'omega'):
            raise ValueError('physical parameter must be c_l or omega')
        kp = (-self.omega/self.c_l**2 if parameter == 'c_l' else 1/self.c_l)
        phase_p = logsr*(self.ms*kp)

        def term(name, exponent, alpha_multiple=1, twisted=True):
            a = amplitude(name)
            if twisted:
                ap = a.select(self.partner)*self.sign
                av = a*cs-ap*sn
            else:
                av = a
            envelope = sr.power(exponent)
            if parameter is None:
                return envelope*av
            value = q*0
            if parameter == 'c_l' and alpha_multiple:
                value = value + envelope*av*logsr*(alpha_multiple/self.c_l**2)
            if twisted:
                value = value + envelope*(-a*sn-ap*cs)*phase_p
            return value

        tor = term('A', -self.alpha-self.ls)
        pol = term('C', 1-self.alpha-self.ls)
        if not exterior and any(len(self.coeff[n]) for n in ('B','D','E')):
            ratio = q*(q+float(self.channels.get('R1') or self.r0)**2).power(-1)
            damp = q*0+1
            for _ in range(int(self.channels['core_damp'])):
                damp = damp*ratio
            if len(self.coeff['B']):
                tor = tor+damp*term('B', -2*self.alpha-1-self.ls, 2)
            if len(self.coeff['D']):
                pol = pol+damp*term('D', -2*self.alpha-self.ls, 2)
            if len(self.coeff['E']):
                pol = pol+damp*term('E', -2*self.ls-1, 0, False)*(self.ls >= 2)
        return tor, pol

    def torch_parameter_values(self, y, parameter=None, exterior=False):
        rho = (y*y).sum(1, keepdim=True)
        if exterior and bool(torch.any(rho <= 0)):
            raise ValueError('exterior excludes the origin')
        f,g = self.radial_with_parameter(rho, parameter, exterior)
        H,h,K = self.table.values(y)
        A = (self.ls+1)*g.v+2*rho*g.d
        Ap = (self.ls+3)*g.d+2*rho*g.h
        B = -2*self.ls*g.d
        Bp = -2*self.ls*g.h
        eye = torch.eye(3,device=y.device,dtype=y.dtype)
        cross = torch.linalg.cross(h,y[:,None,:].expand_as(h),dim=-1)
        u = (f.v[:,:,None]*cross+A[:,:,None]*h+B[:,:,None]*y[:,None,:]*H[:,:,None]).sum(1)
        dt = 2*f.d[:,:,None,None]*cross[:,:,:,None]*y[:,None,None,:]
        dt = dt+f.v[:,:,None,None]*(torch.linalg.cross(K.transpose(-1,-2),y[:,None,None,:].expand_as(K),dim=-1).transpose(-1,-2)+torch.linalg.cross(h[:,:,None,:].expand_as(K),eye[None,None,:,:].expand_as(K),dim=-1).transpose(-1,-2))
        dp = A[:,:,None,None]*K+2*Ap[:,:,None,None]*h[:,:,:,None]*y[:,None,None,:]+B[:,:,None,None]*(eye[None,None,:,:]*H[:,:,None,None]+y[:,None,:,None]*h[:,:,None,:])+2*Bp[:,:,None,None]*H[:,:,None,None]*y[:,None,:,None]*y[:,None,None,:]
        return u, (dt+dp).sum(1)

    def parameter_values(self, points, parameter=None, exterior=False):
        points = np.asarray(points, dtype=float)
        uu,dd = [],[]
        with torch.no_grad():
            for start in range(0, len(points), self.chunk):
                y = torch.as_tensor(points[start:start+self.chunk], device=self.device, dtype=torch.float64)
                u,d = self.torch_parameter_values(y, parameter, exterior)
                uu.append(u.cpu().numpy()); dd.append(d.cpu().numpy())
        return np.concatenate(uu),np.concatenate(dd)

    def source_parameter(self, points, parameter=None):
        _, d = self.parameter_values(points)
        if parameter is None:
            return np.einsum('nij,nji->n',d,d)
        _, dp = self.parameter_values(points,parameter)
        return 2*np.einsum('nij,nji->n',d,dp)


def momentum(points,u,du,gradp,c_l,omega):
    jy=np.stack((-points[:,1],points[:,0],np.zeros(len(points))),axis=1)
    ju=np.stack((-u[:,1],u[:,0],np.zeros(len(points))),axis=1)
    w=c_l*points-omega*jy+u
    return (1-c_l)*u+np.einsum('nij,nj->ni',du,w)+omega*ju+gradp


def momentum_parameter(points,u,du,up,dup,gradpp,c_l,omega,parameter):
    jy=np.stack((-points[:,1],points[:,0],np.zeros(len(points))),axis=1)
    ju=np.stack((-u[:,1],u[:,0],np.zeros(len(points))),axis=1)
    jup=np.stack((-up[:,1],up[:,0],np.zeros(len(points))),axis=1)
    w=c_l*points-omega*jy+u
    if parameter=='c_l':
        explicit=-u;wp=points+up
    elif parameter=='omega':
        explicit=ju;wp=-jy+up
    else:
        raise ValueError(parameter)
    return explicit+(1-c_l)*up+np.einsum('nij,nj->ni',du,wp)+np.einsum('nij,nj->ni',dup,w)+omega*jup+gradpp
