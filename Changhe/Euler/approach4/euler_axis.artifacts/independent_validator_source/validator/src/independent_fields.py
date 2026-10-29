"""Independent axisymmetric fields and exact analytic jets in s=r**2,z.

No solver-lane modules are imported. A scalar is a finite sum of monomials
c*s**i*z**j times either (L**2+s+z**2)**(-beta) or exp(-beta*(s+z**2)).
Derivative coefficients are built by elementary product rules, independently
of the Cartesian finite-difference and torch checks in the tests.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from math import sqrt
import json
from pathlib import Path
import numpy as np


@dataclass(frozen=True)
class Term:
    coefficient: float
    i: int
    j: int
    beta: float


class ScalarExpansion:
    def __init__(self, terms, *, kernel="power", length=1.0):
        if kernel not in ("power", "gaussian"):
            raise ValueError(kernel)
        if length <= 0:
            raise ValueError("length must be positive")
        self.terms = tuple(t if isinstance(t, Term) else Term(*t) for t in terms)
        if any(t.i < 0 or t.j < 0 for t in self.terms):
            raise ValueError("nonnegative monomial degrees required")
        self.kernel, self.length = kernel, float(length)

    @lru_cache(maxsize=None)
    def differentiated(self, ds=0, dz=0):
        terms = {(t.i, t.j, t.beta): 0.0 for t in self.terms}
        for t in self.terms:
            terms[t.i, t.j, t.beta] += t.coefficient
        for direction in ([0]*ds + [1]*dz):
            result = {}
            def add(key, value):
                result[key] = result.get(key, 0.0) + value
            for (i,j,b), c in terms.items():
                if direction == 0:
                    if i:
                        add((i-1,j,b), c*i)
                    add((i,j,b+1 if self.kernel == "power" else b), -b*c)
                else:
                    if j:
                        add((i,j-1,b), c*j)
                    add((i,j+1,b+1 if self.kernel == "power" else b), -2*b*c)
            terms = {key: value for key,value in result.items() if value != 0.0}
        return tuple(Term(c,i,j,b) for (i,j,b),c in terms.items())

    def evaluate(self, s, z, ds=0, dz=0):
        s,z = np.broadcast_arrays(np.asarray(s,dtype=np.float64),np.asarray(z,dtype=np.float64))
        rho = self.length**2+s+z*z
        out = np.zeros_like(rho)
        if self.kernel == "power":
            # Scale monomials before powers to avoid huge intermediate values.
            u, v = s/rho, z/np.sqrt(rho)
            for t in self.differentiated(ds,dz):
                out += t.coefficient * np.power(u,t.i) * np.power(v,t.j) * np.power(rho,t.i+0.5*t.j-t.beta)
        else:
            for t in self.differentiated(ds,dz):
                out += t.coefficient*np.power(s,t.i)*np.power(z,t.j)*np.exp(-t.beta*(s+z*z))
        return out

    def jet(self, s,z,order):
        return {(a,b): self.evaluate(s,z,a,b) for a in range(order+1) for b in range(order+1-a)}

    def dilate(self, L, amplitude):
        if self.kernel == "power":
            terms = [Term(t.coefficient*amplitude*L**(2*t.beta-2*t.i-t.j),t.i,t.j,t.beta) for t in self.terms]
            return ScalarExpansion(terms,kernel=self.kernel,length=self.length*L)
        return ScalarExpansion([Term(t.coefficient*amplitude/L**(2*t.i+t.j),t.i,t.j,t.beta/L**2) for t in self.terms],kernel=self.kernel,length=self.length*L)

    def as_dict(self):
        return {"kernel":self.kernel,"length":self.length,"terms":[[t.coefficient,t.i,t.j,t.beta] for t in self.terms]}

    @classmethod
    def from_dict(cls,d):
        return cls(d["terms"],kernel=d.get("kernel","power"),length=d.get("length",1.0))


class PotentialField:
    def __init__(self,phi,q,c_l=0.6):
        self.phi,self.q,self.c_l=phi,q,float(c_l)
        if not 0 < self.c_l < 1:
            raise ValueError("this validator requires 0<c_l<1")
        self.alpha=(1-self.c_l)/self.c_l

    def cylindrical(self,r,z,order=3):
        r,z=np.broadcast_arrays(np.asarray(r,dtype=np.float64),np.asarray(z,dtype=np.float64))
        s=r*r
        p=self.phi.jet(s,z,max(2,order))
        q=self.q.jet(s,z,1)
        ur=-r*p[0,1]
        ut=r*q[0,0]
        uz=2*p[0,0]+2*s*p[1,0]
        ur_r=-p[0,1]-2*s*p[1,1]
        ur_z=-r*p[0,2]
        ut_r=q[0,0]+2*s*q[1,0]
        ut_z=r*q[0,1]
        uz_r=8*r*p[1,0]+4*r*s*p[2,0]
        uz_z=2*p[0,1]+2*s*p[1,1]
        eta=-8*p[1,0]-4*s*p[2,0]-p[0,2]
        source=ur_r**2+p[0,1]**2+uz_z**2-2*q[0,0]*ut_r+2*ur_z*uz_r
        result={"r":r,"z":z,"s":s,"phi":p,"q":q,"U":np.stack((ur,ut,uz),axis=-1),"eta":eta,
                "ur_r":ur_r,"ur_z":ur_z,"ut_r":ut_r,"ut_z":ut_z,"uz_r":uz_r,"uz_z":uz_z,
                "ur_over_r":-p[0,1],"source":source,"divergence":ur_r-p[0,1]+uz_z}
        if order>=3:
            result["eta_s"]=-12*p[2,0]-4*s*p[3,0]-p[1,2]
            result["eta_z"]=-8*p[1,1]-4*s*p[2,1]-p[0,3]
        return result

    def cartesian(self,xyz,with_jacobian=False):
        xyz=np.asarray(xyz,dtype=np.float64)
        x,y,z=np.moveaxis(xyz,-1,0)
        s=x*x+y*y
        p=self.phi.jet(s,z,2 if with_jacobian else 1)
        q=self.q.jet(s,z,1 if with_jacobian else 0)
        U=np.stack((-x*p[0,1]-y*q[0,0],-y*p[0,1]+x*q[0,0],2*p[0,0]+2*s*p[1,0]),axis=-1)
        if not with_jacobian:
            return U
        J=np.empty(U.shape+(3,),dtype=np.float64)
        J[...,0,0]=-p[0,1]-2*x*x*p[1,1]-2*x*y*q[1,0]
        J[...,0,1]=-2*x*y*p[1,1]-q[0,0]-2*y*y*q[1,0]
        J[...,0,2]=-x*p[0,2]-y*q[0,1]
        J[...,1,0]=-2*x*y*p[1,1]+q[0,0]+2*x*x*q[1,0]
        J[...,1,1]=-p[0,1]-2*y*y*p[1,1]+2*x*y*q[1,0]
        J[...,1,2]=-y*p[0,2]+x*q[0,1]
        J[...,2,0]=8*x*p[1,0]+4*x*s*p[2,0]
        J[...,2,1]=8*y*p[1,0]+4*y*s*p[2,0]
        J[...,2,2]=2*p[0,1]+2*s*p[1,1]
        return U,J

    def reduced(self,r,z):
        d=self.cylindrical(r,z,3)
        ur,ut,uz=np.moveaxis(d["U"],-1,0)
        Wr,Wz=self.c_l*d["r"]+ur,self.c_l*d["z"]+uz
        q=d["q"][0,0]
        qterms=np.stack((q,Wr*2*d["r"]*d["q"][1,0],Wz*d["q"][0,1],2*d["ur_over_r"]*q),axis=-1)
        eterms=np.stack(((1+self.c_l)*d["eta"],Wr*2*d["r"]*d["eta_s"],Wz*d["eta_z"],-2*q*d["q"][0,1]),axis=-1)
        gamma=d["s"]*q
        gamma_r=2*d["r"]*q+2*d["r"]*d["s"]*d["q"][1,0]
        gamma_z=d["s"]*d["q"][0,1]
        return {"q":np.sum(qterms,axis=-1),"eta":np.sum(eterms,axis=-1),"q_terms":qterms,"eta_terms":eterms,
                "gamma":(1-2*self.c_l)*gamma+Wr*gamma_r+Wz*gamma_z,"divergence":d["divergence"],"elliptic":np.zeros_like(q)}

    def primitive_cylindrical(self,r,z,pressure_gradient=None):
        d=self.cylindrical(r,z,2)
        ur,ut,uz=np.moveaxis(d["U"],-1,0)
        Wr,Wz=self.c_l*d["r"]+ur,self.c_l*d["z"]+uz
        radial=(1-self.c_l)*ur+Wr*d["ur_r"]+Wz*d["ur_z"]-d["r"]*d["q"][0,0]**2
        swirl=(1-self.c_l)*ut+Wr*d["ut_r"]+Wz*d["ut_z"]+d["ur_over_r"]*ut
        axial=(1-self.c_l)*uz+Wr*d["uz_r"]+Wz*d["uz_z"]
        out=np.stack((radial,swirl,axial),axis=-1)
        if pressure_gradient is not None:
            grad=np.asarray(pressure_gradient,dtype=np.float64)
            out[...,0]+=grad[...,0]
            out[...,2]+=grad[...,1]
        return out

    def primitive_cartesian(self,xyz,pressure_gradient=None):
        U,J=self.cartesian(xyz,True)
        W=self.c_l*np.asarray(xyz,dtype=np.float64)+U
        out=(1-self.c_l)*U+np.einsum('...ij,...j->...i',J,W)
        if pressure_gradient is not None:
            out=out+pressure_gradient
        return out

    def source(self,r,z):
        return self.cylindrical(r,z,2)["source"]

    def eta(self,r,z):
        return self.cylindrical(r,z,2)["eta"]

    def dilate(self,L):
        return PotentialField(self.phi.dilate(L,L),self.q.dilate(L,1),self.c_l)

    def as_dict(self):
        return {"format":"verifier-monomial-envelope-v1","c_l":self.c_l,"phi":self.phi.as_dict(),"q":self.q.as_dict()}

    def save(self,path):
        Path(path).write_text(json.dumps(self.as_dict(),indent=2)+'\n')

    @classmethod
    def load(cls,path):
        d=json.loads(Path(path).read_text())
        if d.get("format")!="verifier-monomial-envelope-v1":
            raise ValueError("unrecognized candidate format; an explicit independent adapter is required")
        return cls(ScalarExpansion.from_dict(d["phi"]),ScalarExpansion.from_dict(d["q"]),d["c_l"])


def manufactured_gaussian(a=0.3,b=0.7,c=-0.2,c_l=0.6):
    return PotentialField(ScalarExpansion([(1,0,0,1),(a,0,1,1)],kernel="gaussian"),ScalarExpansion([(b,0,0,1),(c,0,1,1)],kernel="gaussian"),c_l)


def manufactured_power(c_l=0.6):
    alpha=(1-c_l)/c_l
    return PotentialField(ScalarExpansion([(0.31,0,0,alpha/2),(-0.23,0,1,(alpha+1)/2),(0.11,1,0,(alpha+2)/2),(0.07,0,2,(alpha+2)/2)]),ScalarExpansion([(0.47,0,0,(alpha+1)/2),(0.19,0,1,(alpha+2)/2),(-0.13,1,0,(alpha+3)/2)]),c_l)
