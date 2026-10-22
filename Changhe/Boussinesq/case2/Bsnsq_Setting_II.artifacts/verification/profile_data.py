"""Independent decoder of published numerical coefficient data.

Only the mathematical representation documentation in a2core.py was read.
No fitting-code routines are imported or copied. Evaluation uses NumPy's
Clenshaw polynomial evaluator and complex powers, avoiding the fitting grid.
"""
import io
import json
import hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from numpy.polynomial.chebyshev import chebval

class CoefficientProfile:
    def __init__(self,path):
        with np.load(path,allow_pickle=False) as z:
            self.ca=z['ca'].copy();self.cg=z['cG'].copy()
            self.beta=float(z['beta']);self.length=float(z['L'])
            self.sigma_a=float(z['sigma_a']);self.sigma_g=float(z['sigma_G'])
            self.mapname=str(z['mapname']) if 'mapname' in z.files else 'xi'
            self.beta_map=float(z['beta_map']) if 'beta_map' in z.files else self.beta
        if self.mapname not in ['xi','t']:
            raise ValueError('Unrecognized documented radial map')
        if self.mapname=='t' and self.beta_map<=0:
            raise ValueError('The t-map requires beta_map>0')
        self.tail_power=2*self.sigma_g-2
        if self.ca.shape!=self.cg.shape or self.ca.ndim!=2:
            raise ValueError('Unrecognized coefficient matrix shapes')

    def amplitude(self,p,coefficients,sigma):
        p=np.asarray(p,float); shape=p.shape[:-1]
        flat=p.reshape(-1,2);x,y=flat.T
        q=x*x+y*y;den=q+self.length**2
        if self.mapname=='xi':
            radial_weight=2*self.length**2/den
            argument=1-radial_weight
        else:
            log_weight=-np.log1p(q/self.length**2)
            t=np.exp(log_weight/(2*self.beta_map))
            argument=2*t-1
            radial_weight=np.exp(log_weight)
        polynomials=chebval(argument,coefficients.T)
        angular_square=(x+1j*y)**2/den
        angular_power=np.ones_like(angular_square)
        total=np.zeros(len(flat))
        for l in range(len(coefficients)):
            total+=angular_power.real*polynomials[l]
            angular_power*=angular_square
        return (radial_weight**sigma*total).reshape(shape)

    def a(self,p):return self.amplitude(p,self.ca,self.sigma_a)
    def G(self,p):return self.amplitude(p,self.cg,self.sigma_g)
    def theta(self,p):
        p=np.asarray(p,float)
        return p[...,0]**2*p[...,1]*self.a(p)
    def omega(self,p):
        p=np.asarray(p,float)
        return p[...,0]*p[...,1]*self.G(p)

    def metadata(self):
        return dict(beta=self.beta,L=self.length,M=self.ca.shape[0],N=self.ca.shape[1],
                    radial_map=self.mapname,beta_map=self.beta_map,
                    sigma_a=self.sigma_a,sigma_G=self.sigma_g,
                    effective_temperature_power=3-2*self.sigma_a,
                    effective_vorticity_power=2-2*self.sigma_g,
                    a0=float(self.a([[0,0]])[0]),G0=float(self.G([[0,0]])[0]))

    def leading_amplitude(self,coefficients,sigma,phi):
        """Coefficient of r^(-2 sigma), not a claim it is nonzero."""
        endpoint=1 if self.mapname=='xi' else -1
        radial_coefficients=coefficients@(endpoint**np.arange(coefficients.shape[1]))
        scale_factor=((2 if self.mapname=='xi' else 1)*self.length**2)**sigma
        angular=np.cos(2*np.asarray(phi)[:,None]*np.arange(len(coefficients))[None,:])
        return scale_factor*(angular@radial_coefficients)


def snapshot(source,target,status="exploratory control, not a published solution candidate"):
    """Read one immutable byte snapshot; discard redundant fitting history."""
    raw=Path(source).read_bytes()
    with np.load(io.BytesIO(raw),allow_pickle=False) as z:
        payload={k:z[k].copy() for k in ['ca','cG','beta','L','sigma_a','sigma_G']}
        for key in ['mapname','beta_map','a0_target']:
            if key in z.files:payload[key]=z[key].copy()
        hist=json.loads(str(z['hist'])) if 'hist' in z.files else []
        last=hist[-1] if hist else None
    np.savez_compressed(target,**payload)
    meta=dict(timestamp=datetime.now(timezone.utc).isoformat(),source=str(source),
              source_sha256=hashlib.sha256(raw).hexdigest(),
              source_last_history_row=last,
              status=status)
    Path(target).with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
    return meta
