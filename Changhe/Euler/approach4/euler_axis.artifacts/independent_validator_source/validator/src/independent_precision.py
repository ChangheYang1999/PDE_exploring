"""Independent mpmath differentiation of saved scalar expressions.

The reference evaluates the original monomial expression and differentiates
it with mpmath.diff. It does not use the float64 derivative recurrence.
"""
from __future__ import annotations
import mpmath as mp
import numpy as np


def mp_scalar(expansion,s,z):
    length=mp.mpf(str(expansion.length))
    result=mp.mpf('0')
    for term in expansion.terms:
        c=mp.mpf(str(term.coefficient)); beta=mp.mpf(str(term.beta))
        factor=(length*length+s+z*z)**(-beta) if expansion.kernel=='power' else mp.exp(-beta*(s+z*z))
        result+=c*s**term.i*z**term.j*factor
    return result


def reference_point(field,xyz,dps=65):
    with mp.workdps(dps):
        point=tuple(mp.mpf(str(v)) for v in xyz)
        c=mp.mpf(str(field.c_l))
        phi=lambda s,z:mp_scalar(field.phi,s,z)
        qfun=lambda s,z:mp_scalar(field.q,s,z)
        def velocity(x,y,z):
            s=x*x+y*y
            pz=mp.diff(phi,(s,z),(0,1)); ps=mp.diff(phi,(s,z),(1,0))
            q=qfun(s,z)
            return (-x*pz-y*q,-y*pz+x*q,2*phi(s,z)+2*s*ps)
        U=velocity(*point)
        J=mp.matrix(3,3)
        for i in range(3):
            for j in range(3):
                degree=tuple(int(k==j) for k in range(3))
                J[i,j]=mp.diff(lambda x,y,z:velocity(x,y,z)[i],point,degree)
        x,y,z=point;s=x*x+y*y;r=mp.sqrt(s)
        q=qfun(s,z)
        eta=lambda s,z:-8*mp.diff(phi,(s,z),(1,0))-4*s*mp.diff(phi,(s,z),(2,0))-mp.diff(phi,(s,z),(0,2))
        psiz=mp.diff(phi,(s,z),(0,1))
        Wz=c*z+U[2]
        rq=q+2*s*(c-psiz)*mp.diff(qfun,(s,z),(1,0))+Wz*mp.diff(qfun,(s,z),(0,1))-2*psiz*q
        re=(1+c)*eta(s,z)+2*s*(c-psiz)*mp.diff(eta,(s,z),(1,0))+Wz*mp.diff(eta,(s,z),(0,1))-2*q*mp.diff(qfun,(s,z),(0,1))
        primitive=[(1-c)*U[i]+sum(J[i,j]*(c*point[j]+U[j]) for j in range(3)) for i in range(3)]
        source=sum(J[i,j]*J[j,i] for i in range(3) for j in range(3))
        numbers={'velocity':list(U),'jacobian':[[J[i,j] for j in range(3)] for i in range(3)],
                 'primitive_without_pressure':primitive,'source':source,'q_residual':rq,'eta_residual':re}
        def strings(v):
            if isinstance(v,list):return [strings(a) for a in v]
            return mp.nstr(v,dps)
        return {key:strings(value) for key,value in numbers.items()}


def compare_precision(field,points,dps=65):
    rows=[]
    for point in np.asarray(points,dtype=np.float64):
        ref=reference_point(field,point,dps)
        U,J=field.cartesian(point,True)
        r=np.hypot(*point[:2]);z=point[2]
        red=field.reduced(r,z)
        actual={'velocity':U,'jacobian':J,'primitive_without_pressure':field.primitive_cartesian(point),
                'source':field.source(r,z),'q_residual':red['q'],'eta_residual':red['eta']}
        defects={}
        for key,value in actual.items():
            expected=np.asarray(ref[key],dtype=np.float64)
            delta=float(np.max(np.abs(np.asarray(value)-expected)))
            scale=float(np.max(np.abs(expected)))
            defects[key]={'max_abs_error':delta,'reference_scale':scale,'relative_error':delta/scale if scale else None}
        rows.append({'point':point.tolist(),'dps':dps,'defects':defects,'reference':ref})
    return rows
