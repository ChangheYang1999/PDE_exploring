"""Separated radial evaluation from the proved Cartesian potential identities.

Only fixed angular features are cached. No production numerical module is used.
See research/homogeneous_tail_quadrature/PROOF.md.
"""
import copy
import hashlib
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np
import mpmath as mp
import torch
from mp_field import rational_harmonic

AXES=[()]+[(i,) for i in range(3)]+[(i,j) for i in range(3) for j in range(3)]


def decimal_angular(directions,modes,cache_dir=None):
    """Round exact rational polynomials evaluated with 70 decimal digits once."""
    directions=np.asarray(directions,dtype=np.float64);modes=np.asarray(modes,dtype=np.int64)
    digest=hashlib.sha256(directions.tobytes()+modes.tobytes()+b'decimal70-norm85-v1').hexdigest()
    path=Path(cache_dir)/('angular_'+digest+'.npz') if cache_dir else None
    if path and path.exists():
        with np.load(path) as f:
            if not np.array_equal(f['directions'],directions) or not np.array_equal(f['modes'],modes):raise ValueError('angular cache key mismatch')
            return f['values'].copy()
    with localcontext() as ctx,mp.workdps(85):
        ctx.prec=70;polys=[];powers=set()
        for ell,m,kind in modes:
            ell,m,kind=int(ell),int(m),int(kind)
            norm=Decimal(mp.nstr(mp.sqrt(mp.mpf(2*ell+1)*math.factorial(ell-m)/(4*mp.pi*math.factorial(ell+m)))*(mp.sqrt(2) if m else 1),84))
            row=[]
            for axes in AXES:
                poly=[]
                for power,c in rational_harmonic(ell,m,kind):
                    pp=list(power)
                    for axis in axes:c*=pp[axis];pp[axis]-=1
                    if c:
                        pp=tuple(pp);poly.append((pp,Decimal(c.numerator)/Decimal(c.denominator)));powers.add(pp)
                row.append(poly)
            polys.append((norm,row))
        degree=int(modes[:,0].max());values=np.empty((len(directions),len(modes),13))
        for i,n in enumerate(directions):
            pp=[]
            for coordinate in n:
                q=Decimal.from_float(float(coordinate));seq=[Decimal(1)]
                for _ in range(degree):seq.append(seq[-1]*q)
                pp.append(seq)
            mon={p:pp[0][p[0]]*pp[1][p[1]]*pp[2][p[2]] for p in powers}
            for k,(norm,row) in enumerate(polys):
                for j,poly in enumerate(row):values[i,k,j]=float(norm*sum((c*mon[p] for p,c in poly),Decimal(0)))
    if path:
        path.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(path,directions=directions,modes=modes,values=values)
    return values


class TensorGridField:
    def __init__(self,field,directions,angular='decimal70',cache_dir=None):
        self.field=field;self.directions=np.asarray(directions,dtype=float)
        if not np.allclose(np.linalg.norm(self.directions,axis=1),1,rtol=0,atol=2e-14):raise ValueError('unit angular directions required')
        n=torch.as_tensor(self.directions,device=field.device,dtype=torch.float64);eye=torch.eye(3,device=n.device,dtype=n.dtype)
        if angular=='decimal70':
            values=torch.as_tensor(decimal_angular(self.directions,field.modes,cache_dir),device=n.device,dtype=n.dtype)
            H,h,K=values[:,:,0],values[:,:,1:4],values[:,:,4:].reshape(len(n),len(field.modes),3,3)
        elif angular=='float64':H,h,K=field.table.values(n)
        else:raise ValueError('unknown angular reference')
        nn=n[:,None,:];C=torch.linalg.cross(h,nn.expand_as(h),dim=-1)
        D=torch.linalg.cross(K.transpose(-1,-2),n[:,None,None,:].expand_as(K),dim=-1).transpose(-1,-2)+torch.linalg.cross(h[:,:,None,:].expand_as(K),eye[None,None].expand_as(K),dim=-1).transpose(-1,-2)
        vectors=[C,h,nn*H[:,:,None]]
        matrices=[C[:,:,:,None]*nn[:,:,None,:],D,K,h[:,:,:,None]*nn[:,:,None,:],eye[None,None]*H[:,:,None,None]+nn[:,:,:,None]*h[:,:,None,:],H[:,:,None,None]*nn[:,:,:,None]*nn[:,:,None,:]]
        self.vectors=[v.transpose(0,1).reshape(len(field.modes),-1).contiguous() for v in vectors]
        self.matrices=[v.transpose(0,1).reshape(len(field.modes),-1).contiguous() for v in matrices]
        self.angular_method=angular

    def values(self,radii,parameter=None,exterior=False):
        field=self.field;r=torch.as_tensor(np.asarray(radii),device=field.device,dtype=torch.float64).reshape(-1,1)
        if bool(torch.any(r<=0)):raise ValueError('tensor grid excludes r<=0')
        rho=r*r
        f,g=field.radial_with_parameter(rho,parameter,exterior)
        if parameter is not None and hasattr(field,'coeff_partial'):
            extra=copy.copy(field);extra.coeff=field.coeff_partial[parameter]
            fc,gc=extra.radial_with_parameter(rho,None,exterior);f=f+fc;g=g+gc
        ell=field.ls;A=(ell+1)*g.v+2*rho*g.d;Ap=(ell+3)*g.d+2*rho*g.h;B=-2*ell*g.d;Bp=-2*ell*g.h
        vc=[f.v*r**ell,A*r**(ell-1),B*r**(ell+1)]
        dc=[2*f.d*r**(ell+1),f.v*r**(ell-1),A*r**(ell-2),2*Ap*r**ell,B*r**ell,2*Bp*r**(ell+2)]
        u=sum(c@v for c,v in zip(vc,self.vectors));du=sum(c@v for c,v in zip(dc,self.matrices))
        return u.reshape(len(r),len(self.directions),3),du.reshape(len(r),len(self.directions),3,3)

    def source_tensors(self,radii,parameters=(None,'c_l','omega'),exterior=False):
        with torch.no_grad():
            _,du=self.values(radii,None,exterior)
            result={}
            for parameter in parameters:
                dp=du if parameter is None else self.values(radii,parameter,exterior)[1]
                result[parameter]=(1 if parameter is None else 2)*torch.einsum('naij,naji->na',du,dp)
        return result

    def sources(self,radii,parameters=(None,'c_l','omega'),exterior=False):
        return {p:q.cpu().numpy() for p,q in self.source_tensors(radii,parameters,exterior).items()}


class GridSource:
    """Source protocol used by radial_pressure_v2, with an angular cache."""
    def __init__(self,field,parameter=None,angular='decimal70',cache_dir=None):
        self.field=field;self.parameter=parameter;self.angular=angular;self.cache_dir=cache_dir;self.grid=None
    def grid_values(self,radii,directions):
        if self.grid is None or not np.array_equal(self.grid.directions,directions):self.grid=TensorGridField(self.field,directions,self.angular,self.cache_dir)
        return self.grid.sources(radii,(self.parameter,))[self.parameter]
    def __call__(self,points):return self.field.source_parameter(points,self.parameter)
    def leading_tail(self,directions):
        if self.grid is None or not np.array_equal(self.grid.directions,directions):self.grid=TensorGridField(self.field,directions,self.angular,self.cache_dir)
        return self.grid.sources([1.],(None,self.parameter),exterior=True)

    def leading_coefficients(self,directions,labels,projection):
        values=self.leading_tail(directions)
        a=values[self.parameter][0]@projection
        base=values[None][0]@projection
        m=labels[:,1];c=self.field.c_l;w=self.field.omega
        if self.parameter is None:b=np.zeros_like(a)
        elif self.parameter=='c_l':b=base*(2/c**2-1j*m*w/c**2)
        elif self.parameter=='omega':b=base*(1j*m/c)
        else:raise ValueError(self.parameter)
        return a,b

    def projected_values(self,radii,directions,projection):
        if self.grid is None or not np.array_equal(self.grid.directions,directions):self.grid=TensorGridField(self.field,directions,self.angular,self.cache_dir)
        if not hasattr(self,'_projection_source') or self._projection_source is not projection:
            self._projection_source=projection
            self._projection_real=torch.as_tensor(projection.real.copy(),device=self.field.device,dtype=torch.float64)
            self._projection_imag=torch.as_tensor(projection.imag.copy(),device=self.field.device,dtype=torch.float64)
        f=self.grid.source_tensors(radii,(self.parameter,))[self.parameter]
        if not bool(torch.isfinite(f).all()):raise FloatingPointError('Nonfinite tensor-grid source')
        return (f@self._projection_real).cpu().numpy()+1j*(f@self._projection_imag).cpu().numpy()
