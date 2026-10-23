"""Prepared fixed-mesh absolute-loss residual/Jacobian; no optimizer is run.

For ds=d(log r), the user-defined loss is (pi*a_ref**2)^(-1) integral
Rf**2 ds dtheta on the first quadrant. The residual includes sqrt(2), so
0.5*dot(residual,residual) approximates that functional with no extra factor.
The mesh and a_ref remain fixed throughout an optimization epoch.
"""
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Absolute-loss arithmetic requires a resource supervisor')

from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator
from absolute_common import A_REF
from absolute_fields import prepare_candidate, residual as physical_residual


def array_hash(array):
    return hashlib.sha256(np.ascontiguousarray(array,dtype='<f8').tobytes()).hexdigest()


@dataclass(frozen=True)
class FrozenLogMesh:
    """A positive quadrature rule; finite coordinates never certify tails."""
    s: np.ndarray
    theta: np.ndarray
    weights: np.ndarray
    name: str='unnamed_fixed_log_mesh'

    def __post_init__(self):
        values=[np.asarray(x,dtype=float).ravel().copy() for x in (self.s,self.theta,self.weights)]
        if not len(values[0]) or len({len(x) for x in values})!=1:
            raise ValueError('Log-radius, angle and quadrature weights must have equal nonzero lengths')
        if not all(np.all(np.isfinite(x)) for x in values) or np.any(values[2]<=0):
            raise ValueError('Every quadrature coordinate must be finite and every weight positive')
        if np.any(values[1]<0) or np.any(values[1]>np.pi/2):
            raise ValueError('The stated functional integrates the first quadrant')
        if np.any(np.abs(values[0])>340):
            raise ValueError('This binary64 field implementation refuses unrepresentable radial nodes')
        for key,value in zip(('s','theta','weights'),values):
            value.setflags(write=False);object.__setattr__(self,key,value)

    @property
    def size(self):return len(self.s)

    @property
    def fingerprint(self):
        h=hashlib.sha256()
        for key in (self.s,self.theta,self.weights):
            h.update(np.ascontiguousarray(key,dtype='<f8').tobytes())
        return h.hexdigest()

    def coordinates(self,start=0,stop=None):
        stop=self.size if stop is None else stop
        radius=np.exp(self.s[start:stop]);angle=self.theta[start:stop]
        return radius*np.cos(angle),radius*np.sin(angle)

    def record(self):
        return {'schema':'absolute_loss_frozen_log_mesh_v1','name':self.name,
            'nodes':self.size,'log_radius_min':float(min(self.s)),
            'log_radius_max':float(max(self.s)),'angular_min':float(min(self.theta)),
            'angular_max':float(max(self.theta)),'mesh_sha256':self.fingerprint,
            'weights_are_ds_dtheta':True,'exact_whole_line_invariance_claimed':False,
            'whole_axis_qualified_by_mesh_alone':False}

    @classmethod
    def load(cls,path):
        with np.load(path,allow_pickle=False) as data:
            return cls(data['s'],data['theta'],data['weights'],Path(path).stem)


def tensor_gauss_mesh(s_min,s_max,radial_panels=24,radial_order=8,angular_order=48,name='fixed_gauss'):
    """Convenience test rule, explicitly a finite-interval approximation."""
    if not (s_min<s_max) or min(radial_panels,radial_order,angular_order)<1:
        raise ValueError('Invalid quadrature dimensions or interval')
    z,w=np.polynomial.legendre.leggauss(radial_order)
    edges=np.linspace(s_min,s_max,radial_panels+1)
    ss=np.concatenate([.5*((b-a)*z+a+b) for a,b in zip(edges[:-1],edges[1:])])
    sw=np.concatenate([.5*(b-a)*w for a,b in zip(edges[:-1],edges[1:])])
    zt,wt=np.polynomial.legendre.leggauss(angular_order)
    theta=(zt+1)*np.pi/4;tw=wt*np.pi/4
    s,t=np.meshgrid(ss,theta,indexing='ij')
    return FrozenLogMesh(s.ravel(),t.ravel(),np.outer(sw,tw).ravel(),name)


class AbsoluteLossProblem:
    """Finite quadrature epoch over unchanged potential coefficients.

    ``jacobian`` has all 24+K raw physical columns. ``feasible_jacobian`` and
    ``operator`` retain the full 19+K C5 tangent. The field provider supplies
    complete analytic cl dependence, including eliminated c0, exponents and
    derivatives of all spatial fields. There is no residual denominator,
    candidate-dependent amplitude, gauge, or removed weak/scaling direction.
    """
    def __init__(self,candidate,mesh,a_ref,convention='center_chart',block_size=512):
        if convention!='center_chart':
            raise ValueError('Future whole-radius optimization requires the explicit analytic-center convention')
        self.case=json.loads(json.dumps(candidate))
        self.mesh=mesh;self.a_ref=float(a_ref);self.convention=convention
        self.block_size=int(block_size)
        if not (math.isfinite(self.a_ref) and self.a_ref>0) or self.block_size<=0:
            raise ValueError('The reference amplitude and block size must be fixed and positive')
        if self.a_ref!=A_REF:
            raise ValueError('a_ref must equal the fixed Stage XI reference amplitude in the immutable input index')
        self.p=np.asarray(candidate.get('core_parameters',[candidate['cl']]+candidate['coefficients'][1:]),dtype=float)
        self.extra=np.asarray(candidate.get('extra_coefficients',[]),dtype=float)
        if self.p.shape!=(24,) or len(self.extra)!=len(candidate.get('modes',[])):
            raise ValueError('Expected unchanged 24 core parameters and every selected new coefficient')
        self.root=np.sqrt(2*self.mesh.weights/(np.pi*self.a_ref*self.a_ref))
        self.root.setflags(write=False)
        self.fun_calls=self.jac_calls=0

    @property
    def physical_columns(self):return 24+len(self.extra)

    def prepare(self,p=None,extra=None):
        p=self.p if p is None else np.asarray(p,dtype=float)
        extra=self.extra if extra is None else np.asarray(extra,dtype=float)
        if p.shape!=(24,) or extra.shape!=self.extra.shape:
            raise ValueError('Physical coefficient dimensions changed within an epoch')
        return prepare_candidate(self.case,convention=self.convention,parameters=p,extra=extra)

    def blocks(self):
        for start in range(0,self.mesh.size,self.block_size):
            stop=min(start+self.block_size,self.mesh.size)
            x,y=self.mesh.coordinates(start,stop)
            yield start,stop,x,y

    def fun(self,p=None,extra=None):
        self.fun_calls+=1;prepared=self.prepare(p,extra);result=np.empty(self.mesh.size)
        for start,stop,x,y in self.blocks():
            raw=physical_residual(prepared,x,y,derivatives=False)
            result[start:stop]=self.root[start:stop]*np.asarray(raw)
        if not np.all(np.isfinite(result)):raise ValueError('Nonfinite absolute residual')
        return result

    def jacobian(self,p=None,extra=None):
        self.jac_calls+=1;prepared=self.prepare(p,extra)
        result=np.empty((self.mesh.size,self.physical_columns))
        for start,stop,x,y in self.blocks():
            _,draw=physical_residual(prepared,x,y,derivatives=True)
            draw=np.asarray(draw)
            if draw.shape!=(stop-start,self.physical_columns):
                raise ValueError('Field provider did not return all raw coefficient derivatives')
            result[start:stop]=self.root[start:stop,None]*draw
        if not np.all(np.isfinite(result)):raise ValueError('Nonfinite absolute Jacobian')
        return result

    def feasible_jacobian(self,core_tangent,p=None,extra=None,extra_scales=None):
        tangent=np.asarray(core_tangent,dtype=float)
        if tangent.shape!=(24,19):raise ValueError('All nineteen feasible core directions are required')
        scales=np.ones(len(self.extra)) if extra_scales is None else np.asarray(extra_scales,dtype=float)
        if scales.shape!=self.extra.shape or not np.all(np.isfinite(scales)) or np.any(scales==0):
            raise ValueError('Every extra direction must retain a finite nonzero coordinate scale')
        full=self.jacobian(p,extra)
        return np.column_stack((full[:,:24]@tangent,full[:,24:]*scales))

    def operator(self,core_tangent,p=None,extra=None,extra_scales=None):
        return AbsoluteJacobianOperator(self,core_tangent,p,extra,extra_scales)

    def objective(self,p=None,extra=None):
        r=self.fun(p,extra)
        return float(r@r/2)

    def require_whole_axis_qualification(self,qualification,candidate_sha256):
        """Fail closed: a fixed rule or derivative PASS is not a tail certificate."""
        required={'whole_axis_qualified':True,'mesh_sha256':self.mesh.fingerprint,
            'candidate_sha256':candidate_sha256,'a_ref':self.a_ref,
            'center_convention':self.convention}
        for key,value in required.items():
            if qualification.get(key)!=value:
                raise ValueError('Missing or mismatched whole-axis qualification: '+key)
        for key in ('origin_tail_error_abs','infinity_tail_error_abs','radial_quadrature_error_abs','angular_quadrature_error_abs'):
            value=qualification.get(key)
            if not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
                raise ValueError('A finite nonnegative integration error is required: '+key)
        if not qualification.get('neighborhood_validated',False):
            raise ValueError('A future optimization epoch needs qualification on its proposed trust neighborhood')
        return True


class AbsoluteJacobianOperator(LinearOperator):
    """Recomputed point blocks avoid storing a full node-by-mode Jacobian.

    This trades repeated field evaluations for bounded memory. It is supplied
    for subsequent benchmarking and LSMR use, not asserted faster than dense.
    No singular value threshold or normal equation is involved.
    """
    def __init__(self,problem,core_tangent,p=None,extra=None,extra_scales=None):
        self.problem=problem
        self.p=problem.p.copy() if p is None else np.asarray(p,dtype=float).copy()
        self.extra=problem.extra.copy() if extra is None else np.asarray(extra,dtype=float).copy()
        self.tangent=np.asarray(core_tangent,dtype=float).copy()
        self.scales=np.ones(len(self.extra)) if extra_scales is None else np.asarray(extra_scales,dtype=float).copy()
        if self.tangent.shape!=(24,19) or self.scales.shape!=self.extra.shape or np.any(self.scales==0) or not np.all(np.isfinite(self.scales)):
            raise ValueError('Complete 19+K finite nonzero coordinate map required')
        self.prepared=problem.prepare(self.p,self.extra)
        super().__init__(dtype=np.dtype(float),shape=(problem.mesh.size,19+len(self.extra)))

    def _matvec(self,v):
        v=np.asarray(v,dtype=float).ravel()
        raw=np.r_[self.tangent@v[:19],self.scales*v[19:]]
        result=np.empty(self.shape[0])
        for start,stop,x,y in self.problem.blocks():
            _,draw=physical_residual(self.prepared,x,y,derivatives=True)
            result[start:stop]=self.problem.root[start:stop]*(np.asarray(draw)@raw)
        return result

    def _rmatvec(self,w):
        w=np.asarray(w,dtype=float).ravel();raw=np.zeros(self.problem.physical_columns)
        for start,stop,x,y in self.problem.blocks():
            _,draw=physical_residual(self.prepared,x,y,derivatives=True)
            raw+=np.asarray(draw).T@(self.problem.root[start:stop]*w[start:stop])
        return np.r_[self.tangent.T@raw[:24],self.scales*raw[24:]]
