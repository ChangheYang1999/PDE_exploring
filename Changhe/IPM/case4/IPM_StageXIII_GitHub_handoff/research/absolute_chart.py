"""Separate analytic-center C5 chart for a future absolute-loss experiment.

The saved research candidates are never corrected or overwritten here. This
module preserves the full old 24-parameter potential family and its 19 tangent
directions. It changes the arithmetic convention of c0 explicitly: the center
identity is an exact analytic elimination rather than a saved binary64 c0.
"""
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Absolute C5 arithmetic requires a resource supervisor')

import json
from decimal import Decimal, localcontext
from pathlib import Path
import numpy as np
from absolute_common import BASE
from stage12_common import e
from stage12_chart import chart as historical_chart


def coefficients(p):
    """Unrounded analytic center elimination, supporting complex-step cl."""
    p = np.asarray(p)
    matrix = e.v.jet.matrices(p[0])
    c0 = (1-p[0]-matrix[6, 1:]@p[1:])/matrix[6, 0]
    return np.r_[c0, p[1:]]


def constraint_values(p):
    p = np.asarray(p)
    a,b,c,d,f,g,h,u,v,w,z,k = e.v.jet.matrices(p[0])@coefficients(p)
    cl=p[0]
    return np.asarray([2*(2*cl-1)*b+3*a*u, 2*c+a*v,
        4*(2*cl-1)*d+b*u+5*a*w,
        4*cl*f-5*b*v+9*c*u+3*a*z,
        4*g+3*c*v+a*k])


def constraint_jacobian(p):
    """Complex-step differentiates cl, every radial exponent and c0 chain."""
    p=np.asarray(p, dtype=float)
    result=np.empty((5,24))
    for i in range(24):
        probe=p.astype(complex);probe[i]+=1e-25j
        result[:,i]=np.imag(constraint_values(probe))/1e-25
    return result


def hp_report(p, precision=70):
    """Independent Decimal binomial-series constraints with exact center c0."""
    p=np.asarray(p,dtype=float)
    with localcontext() as ctx:
        ctx.prec=precision
        cl=Decimal.from_float(float(p[0]))
        columns=e.v.jet.series(cl, True)
        c=[Decimal(0)]+[Decimal.from_float(float(x)) for x in p[1:]]
        c[0]=(1-cl-sum((columns[j][6]*c[j] for j in range(1,24)),Decimal(0)))/columns[0][6]
        values=[sum((columns[j][i]*c[j] for j in range(24)),Decimal(0)) for i in range(12)]
        a,b,cy,d,f,g,h,u,v,w,z,k=values
        cc=[2*(2*cl-1)*b+3*a*u,2*cy+a*v,
            4*(2*cl-1)*d+b*u+5*a*w,
            4*cl*f-5*b*v+9*cy*u+3*a*z,4*g+3*cy*v+a*k]
        poisson=[3*(u+v)+b,20*w+6*z+4*d,6*z+20*k+2*f]
        center=cl+h-1
        return {'precision':precision,'center_convention':'analytic_center_elimination',
            'coefficients_decimal':[str(x) for x in c],
            'jets':dict(zip(e.v.jet.NAMES,map(str,values))),
            'constraints_decimal':list(map(str,cc)),
            'constraints':[float(x) for x in cc],
            'max_abs':float(max(abs(x) for x in cc)),
            'center_decimal':str(center),'center_abs':float(abs(center)),
            'poisson_max_abs':float(max(abs(x) for x in poisson)),
            'a0':float(a),'physical_bounds':bool(np.all(p>=e.v.LOW) and np.all(p<=e.v.HIGH))}


class AbsoluteC5Chart:
    """A local 19-dimensional implicit C5 chart with cl-free normal corrections.

    The 19 original tangent vectors are retained as free-coordinate seeds.
    Five normal vectors span the original two quadratic eliminations and three
    coefficient-only corrections. They are orthonormalized, never truncated.
    All five analytic-center constraints are corrected together. This chart is
    a prepared interface, not an optimization or a refit of saved candidates.
    """
    version='absolute_loss_analytic_center_full19_c5_v1'

    def __init__(self, p, record=None, tolerance=1e-10, target=3e-12):
        self.base=np.asarray(p,dtype=float).copy()
        self.tolerance=float(tolerance);self.target=float(target)
        if record is None:
            record=json.loads((BASE/'results/chart_coefficient_normal.json').read_text())
        old=historical_chart(self.base,record)
        self.free=old.base_tangent.copy()
        original_normals=np.column_stack((np.eye(24)[:,old.zpair],old.base_geometry['R']@old.e))
        if not np.array_equal(original_normals[0],np.zeros(5)):
            raise ValueError('Historical normal directions unexpectedly contain cl')
        self.normal=np.zeros((24,5))
        self.normal[1:]=np.linalg.qr(original_normals[1:],mode='reduced')[0]
        # All normal seeds have zero cl; QR must preserve that row exactly.
        if not np.array_equal(self.normal[0],np.zeros(5)):
            raise ValueError('Normal correction would alter cl')
        self._verify(self.base)
        self.base_tangent=self.tangent(self.base)
        self.complete=np.column_stack((self.base_tangent,self.normal))
        rank=np.linalg.matrix_rank(self.complete)
        if rank!=24 or np.linalg.norm(self.base_tangent[0])==0:
            raise ValueError('A core direction, including cl, was lost')

    def _bounds(self,p):
        if p.shape!=(24,) or not np.all(np.isfinite(p)) or np.any(p<e.v.LOW) or np.any(p>e.v.HIGH):
            raise ValueError('Outside unchanged original physical parameter bounds')

    def _verify(self,p):
        self._bounds(p);report=hp_report(p)
        if report['max_abs']>=self.tolerance or report['poisson_max_abs']>=self.tolerance or abs(report['a0'])<=1e-12:
            raise ValueError('Analytic-center C5 point fails independent feasibility/nondegeneracy')
        return report

    def tangent(self,p):
        g=constraint_jacobian(p);a=g@self.normal
        if np.linalg.cond(a)>1e10:
            raise ValueError('Analytic-center C5 normal system is unresolved')
        return self.free-self.normal@np.linalg.solve(a,g@self.free)

    def lift_delta(self,q,derivative=False):
        q=np.asarray(q,dtype=float)
        if q.shape!=(19,) or not np.all(np.isfinite(q)):
            raise ValueError('Expected all nineteen finite core coordinates')
        if not np.any(q):
            return (self.base.copy(),self.base_tangent.copy()) if derivative else self.base.copy()
        seed=self.base+self.free@q;z=np.zeros(5);p=seed.copy()
        self._bounds(p);history=[]
        for it in range(24):
            hp=hp_report(p);c=np.asarray(hp['constraints']);size=float(np.linalg.norm(c))
            history.append({'iteration':it,'constraint_norm':size,'max_abs':hp['max_abs']})
            if hp['max_abs']<self.target:break
            g=constraint_jacobian(p);a=g@self.normal
            if np.linalg.cond(a)>1e10:raise ValueError('C5 correction lost numerical invertibility')
            dz=np.linalg.solve(a,-c)
            for alpha in (1.,.5,.25,.125,.0625,.03125,.015625):
                zz=z+alpha*dz;trial=seed+self.normal@zz
                try:self._bounds(trial)
                except ValueError:continue
                if np.linalg.norm(hp_report(trial)['constraints'])<size:
                    p,z=trial,zz;break
            else:raise ValueError('C5 correction cannot improve independent constraints')
        report=self._verify(p)
        if float(p[0]).hex()!=float(seed[0]).hex():
            raise ValueError('Coefficient-only corrector changed free cl')
        self.last_diagnostics={'version':self.version,'iterations':history,
            'final':report,'normal_corrections_leave_cl_fixed':True,
            'all_19_core_directions_retained':True}
        return (p,self.tangent(p)) if derivative else p
