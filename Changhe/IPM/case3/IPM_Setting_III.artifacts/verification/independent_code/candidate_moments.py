"""Independent angular integration of the canonical origin moment.

Uses Gaussian quadrature in log physical radius and a mapped infinite tail.
It does not use the numeric lane's differentiation or Green-function code.
"""
from dataclasses import asdict
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time
import numpy as np
from scipy.special import roots_legendre,roots_jacobi
from candidate_reader import Candidate
from direct_inverse import DirectInverse,Quadrature


def strain(candidate,nr=40,ntheta=128,rmin=1e-16,split=16.):
    z,w=roots_legendre(nr); z=(1+z)/2; w=w/2
    th=(np.arange(ntheta)+.5)*2*np.pi/ntheta
    project=np.sin(3*th)*2/ntheta
    def b3(r): return candidate.polar_density(r,th)@project
    edges=np.exp(np.linspace(np.log(rmin),np.log(split),int(np.ceil(np.log(split/rmin)/np.log(4)))+1))
    terms=[]
    for lo,hi in zip(edges[:-1],edges[1:]):
        span=np.log(hi/lo); r=lo*np.exp(span*z)
        terms.append(float(np.dot(w,b3(r)/r)*span))
    q=candidate.meta['p']
    beta=q*(1-candidate.meta['gamma'])-1
    jz,jw=roots_jacobi(nr,0,beta); jz=(jz+1)/2; jw=jw/2**(1+beta)
    r=split*jz**(-q)
    tail=float(np.dot(jw,q*b3(r)/(r*jz**(1+beta))))
    a0=float(candidate.endpoint_t_jets(0)[0,0])
    # Estimate the omitted origin integral with the explicit first radial jet.
    j=candidate.endpoint_t_jets(1)[1]
    b3_r2=(j[1]-j[2])/2*2**candidate.meta['p']/candidate.meta['L']
    origin=float(b3_r2*rmin)
    value=-a0/4+sum(terms)+tail+origin
    return {'c':value,'a0':a0,'cl_plus_c_minus_one':candidate.meta['cl']+value-1,
            'contact':-a0/4,'finite_integral':sum(terms),'infinite_tail':tail,
            'origin_prefix_estimate':origin,'radial':nr,'angular':ntheta,'rmin':rmin,'split':split,'tail_power':q}

if __name__=='__main__':
    output=[]
    for file in sys.argv[1:]:
        start=time.time(); c=Candidate(file,project_center=True)
        r=np.geomspace(1e-12,1e4,35); th=np.array([.01,.27,.62,1.31,2.2,4.7])
        cart=c.rho(r[:,None]*np.cos(th),r[:,None]*np.sin(th))
        polar=c.polar_density(r,th)
        records=[strain(c,n,a,1e-16,s) for n,a,s in [(24,64,4.),(40,128,16.),(64,256,64.)]]
        item={'utc':datetime.now(timezone.utc).isoformat(),'metadata':c.meta,'polar_cartesian_max_relative':float(np.max(np.abs(cart-polar)/np.maximum(1e-15,np.abs(cart)))),'moments':records,'elapsed_seconds':time.time()-start}
        output.append(item); print(json.dumps(item),flush=True)
        Path('evidence/candidate_moments.json').write_text(json.dumps(output,indent=2)+'\n')
