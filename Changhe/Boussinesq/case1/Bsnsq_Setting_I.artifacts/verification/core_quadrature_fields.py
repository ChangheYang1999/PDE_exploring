"""Full generating fields for independent whole-plane quadrature.

Scalar Chebyshev derivative recurrences, not fitting-code Taylor jets. Exact
identities and limitations: verification_methods/core_quadrature_fields/PROOF.md.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import numpy as np
from checked_core_source import bind
from scaled_generating_data import ScaledModel
from cheb_generating_components import recurrence3
from cheb_generating_data import LD

ORDERS = [(i, j) for i in range(4) for j in range(4-i)]
OUTER_KEYS = set('c a0 J Kw m beta alpha se gam'.split())


def number(s):
    # The source binder has proved these are the original finite binary64 data.
    return LD(float(Fraction(s)))


def scalar_factors(x, degree, R, L):
    """d^k [x exp(-x^2/L^2) T_i(2x^2/(R^2+x^2)-1)], k<=3."""
    x = np.asarray(x, dtype=LD).ravel()
    r2 = R*R
    d = r2+x*x
    z = (x-R)*(x+R)/d  # stable at the T_odd root x=R
    z1 = 4*r2*x/d**2
    z2 = 4*r2*(r2-3*x*x)/d**3
    z3 = -48*r2*x*(r2-x*x)/d**4
    raw = recurrence3(z, degree)
    chain = [raw[0], raw[1]*z1,
             raw[2]*z1*z1+raw[1]*z2,
             raw[3]*z1**3+3*raw[2]*z1*z2+raw[1]*z3]
    l2 = L*L
    g = np.exp(-x*x/l2)
    gd = [g, -2*x/l2*g, (4*x*x/l2**2-2/l2)*g,
          (12*x/l2**2-8*x**3/l2**3)*g]
    products = [sum(comb(k,j)*gd[j]*chain[k-j] for j in range(k+1))
                for k in range(4)]
    return [x*products[k]+(k*products[k-1] if k else 0) for k in range(4)]


def prefactor_derivatives(x, e, s):
    E = 1+x*x+(e/s)**6
    ex, exx = 2*x, LD(2)
    ee, eee, eeee = 6*e**5/s**6, 30*e**4/s**6, 120*e**3/s**6
    q = LD(1)/3
    f0, f1, f2, f3 = [E**(q-k)*np.prod([q-j for j in range(k)], dtype=LD)
                       for k in range(4)]
    return {(0,0):f0, (1,0):f1*ex, (0,1):f1*ee,
            (2,0):f2*ex**2+f1*exx, (1,1):f2*ex*ee,
            (0,2):f2*ee**2+f1*eee,
            (3,0):f3*ex**3+3*f2*ex*exx,
            (2,1):f3*ex**2*ee+f2*exx*ee,
            (1,2):f3*ex*ee**2+f2*ex*eee,
            (0,3):f3*ee**3+3*f2*ee*eee+f1*eeee}


def prepare_patches(data):
    return [(number(p['R']), number(p['L']),
             np.array([[number(v) for v in row] for row in p['coefficients']], dtype=LD))
            for p in data['patches']]


def core_derivatives(x, e, patches, s):
    x, e = np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(e,dtype=LD))
    shape = x.shape
    x, e = x.ravel(), e.ravel()
    F = prefactor_derivatives(x,e,s)
    result = {ij:np.zeros_like(x) for ij in ORDERS}
    for R,L,c in patches:
        rx, re = scalar_factors(x,len(c)-1,R,L),scalar_factors(e,c.shape[1]-1,R,L)
        contracted = [c.T@rx[k] for k in range(4)]
        H = {(i,j):np.sum(contracted[i]*re[j],axis=0) for i,j in ORDERS}
        for i,j in ORDERS:
            result[i,j] += sum(comb(i,k)*comb(j,l)*F[k,l]*H[i-k,j-l]
                               for k in range(i+1) for l in range(j+1))
    return {ij:v.reshape(shape) for ij,v in result.items()}


def add_core(x, e, outer, derivatives, s, amplitude):
    """Combine stable outer fields with exact-algebra core corrections."""
    x,e = np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(e,dtype=LD))
    g = derivatives
    pc = {(i,j):3*x*g[i+1,j]+e*g[i,j+1]+(3*i+j-6)*g[i,j]
          for i in range(3) for j in range(3-i)}
    Ao,Bo,Aox,Aoe,Box = [outer[k] for k in ('A','B','Ax','Ae','Bx')]
    A,B,Ax,Ae,Bx = Ao+g[1,1],Bo+g[2,0],Aox+g[2,1],Aoe+g[1,2],Box+g[3,0]
    if np.any(~np.isfinite(A)) or np.any(A<=0):
        raise ArithmeticError('nonpositive or nonfinite full chart')
    bo,b = Bo/Ao,B/A
    To = Box/Ao-2*Bo*Aox/Ao**2+(Bo*Bo+1)*Aoe/Ao**3
    T = Bx/A-2*B*Ax/A**2+(B*B+1)*Ae/A**3
    poe = -Ao*outer['U1']
    poee = Ao**2*outer['Psi_yy']+(Aoe/Ao)*poe
    poxe = -2*Ao+3*x*Aox+e*Aoe
    omega = (outer['Omega']+2*(b-bo)*poxe
             -(b*b-bo*bo+1/A**2-1/Ao**2)*poee+(T-To)*poe
             -pc[2,0]+2*b*pc[1,1]-(b*b+1/A**2)*pc[0,2]+T*pc[0,1])
    pyy = (outer['Psi_yy']+(1/A**2-1/Ao**2)*poee
           -(Ae/A**3-Aoe/Ao**3)*poe+pc[0,2]/A**2-Ae/A**3*pc[0,1])
    result = dict(x=x,eta=e,y=outer['y']+g[1,0],A=A,B=B,Ax=Ax,Ae=Ae,Bx=Bx,
                  U1=outer['U1']+(1/Ao-1/A)*poe-pc[0,1]/A,
                  U2=outer['U2']-(b-bo)*poe+pc[1,0]-b*pc[0,1],
                  Omega=omega,Psi=outer['Psi']+pc[0,0],Psi_yy=pyy,Psi_xx=-omega-pyy,
                  normalized_A=A/(1+x*x+(e/s)**6)**(LD(1)/3),
                  Theta=amplitude*e,Theta_x=-amplitude*B/A,Theta_y=amplitude/A)
    if any(np.any(~np.isfinite(v)) for v in result.values()):
        raise ArithmeticError('nonfinite full field')
    return result


class FullCoreModel:
    def __init__(self, source_json, outer_source):
        self.data,self.binding = bind(source_json)
        self.se,self.a = number(self.data['s']),number(self.data['a'])
        self.patches = prepare_patches(self.data)
        # Explicitly separate the outer component. Never silently ignore a core.
        with np.load(self.data['source'],allow_pickle=False) as full, np.load(outer_source,allow_pickle=False) as outer:
            if set(outer.files)!=OUTER_KEYS:
                raise ValueError('outer component must contain exactly the nine physical outer arrays')
            for k in OUTER_KEYS:
                a,b = full[k],outer[k]
                if a.dtype!=b.dtype or a.shape!=b.shape or a.tobytes()!=b.tobytes():
                    raise ValueError(('outer component mismatch',k))
        self.outer = ScaledModel(outer_source)
        if self.se != self.outer.se or self.a != self.outer.a:
            raise ValueError('JSON and outer scale/amplitude mismatch')
        self.binding['outer_source_sha256'] = hashlib.sha256(Path(outer_source).read_bytes()).hexdigest()

    def mixed_vorticity(self,x,e,diagnostic=False):
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            outer = self.outer.mixed_vorticity(x,e,diagnostic=True)
            core = core_derivatives(x,e,self.patches,self.se)
            result = add_core(x,e,outer,core,self.se,self.a)
        if diagnostic:
            result['core_G'] = core[0,0]
            result['core_A'] = core[1,1]
        return result

    def source(self,x,e):
        z = self.mixed_vorticity(x,e)
        return {k:z[k] for k in ('y','A','Omega')}
