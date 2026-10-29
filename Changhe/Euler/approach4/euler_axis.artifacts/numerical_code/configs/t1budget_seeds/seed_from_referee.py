"""Reproducible positive-strain T1 seeds, not Euler solutions.

Coordinates: s=r**2; z is signed. The saved grid is x=log(R),
mu=z/R in [0,1]. Reflect phi and eta oddly, and q evenly.
The source is supplied analytically: phi=eta=0 and q=K.

Example:
    import seed
    metadata, grid = seed.load(.60)
    value = seed.phi(0.25, 0.5, .60)
"""
import os
for _key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS",
             "NUMEXPR_NUM_THREADS"):
    os.environ[_key]="1"
import json
from pathlib import Path
import numpy as np

_DIRECTORY=Path(__file__).resolve().parent

def parameters(c=.60):
    """Return the recorded normalization and numerical accuracy metadata."""
    return json.loads((_DIRECTORY/f"c{c:.2f}.json").read_text())

def phi(s,z,c=.60,aspect=None):
    """Closed-form potential z*(1+3*z*z)/(2*(1+a*s+z*z)**(1+1/(2*c)))."""
    if aspect is None:
        aspect=parameters(c)["radial_aspect_parameter"]
    s,z=np.asarray(s),np.asarray(z)
    return .5*z*(1+3*z*z)/(1+aspect*s+z*z)**(1+1/(2*c))

def positive_existence_family(s,z,c,B,L=1.):
    """The rigorously positive asymptotic family in ../sign/PROOF.md.

    Positivity is proved for B sufficiently large, then L sufficiently
    large; the proof does not certify particular finite parameter values.
    """
    p=1/(2*c);beta=(1-p)/2;d=p+beta
    s,z=np.asarray(s),np.asarray(z)
    return .5*z*(1+s/L**2+B*z*z)**beta/(1+s/L**2+z*z)**d

def load(c=.60):
    """Return metadata and independent arrays, including computed q and eta."""
    meta=parameters(c)
    with np.load(_DIRECTORY/f"c{c:.2f}.npz",allow_pickle=False) as archive:
        grid={key:archive[key].copy() for key in archive.files}
    return meta,grid

def self_test():
    """Check saved data, source jets, strain quadrature, and axis identity."""
    import resource
    resource.setrlimit(resource.RLIMIT_AS,(1800*1024**2,1800*1024**2))
    from scipy.integrate import simpson
    from scipy.interpolate import CubicSpline
    from scipy.special import roots_legendre,eval_gegenbauer
    results=[]
    for c in (.55,.60,.68,.74):
        meta,g=load(c)
        x,mu=g["x"],g["m"]
        R=np.exp(x)[:,None];s=R*R*(1-mu*mu);z=R*mu
        exact=phi(s,z,c)
        assert np.max(np.abs(g["phi"]-exact))<2e-12
        assert np.all(np.isfinite(g["q"])) and np.all(np.isfinite(g["eta"]))
        assert np.max(np.abs(g["q"]-meta["K"]*g["h"]))<2e-12
        assert np.max(np.abs(g["eta"]-meta["K2"]*g["e"]))<2e-12
        S=1.5*simpson(simpson(g["e"]*mu*(1-mu*mu),x=mu,axis=1)
                      *R[:,0],x=x)
        # S in metadata uses the directly transformed reference kernel,
        # which has slightly different finite-domain and interpolation error.
        assert S>0 and abs(S/meta["S"]-1)<.003
        assert abs(meta["K2"]*meta["S"]-.5)<2e-14
        w=c*R[:,0]+2*phi(0,R[:,0],c)
        eaxis=2*g["h"][:,-1]*(g["h"][:,-1]-1)/w
        axis_error=float(np.max(abs(g["e"][:,-1]-eaxis))/np.max(abs(eaxis)))
        assert axis_error<1e-4
        nodes,weights=roots_legendre(meta["angular_quadrature"])
        phiq=phi(R*R*(1-nodes*nodes),R*nodes,c)
        recon=g["poisson_radial"]@np.array(
            [eval_gegenbauer(int(l),1.5,nodes) for l in g["poisson_ls"]])
        def norm(v):
            radial=(v*v)@(weights*(1-nodes*nodes))*R[:,0]**5
            return np.sqrt(CubicSpline(x,radial).integrate(np.log(.05),np.log(8.)))
        defect=norm(phiq-recon)/norm(phiq)
        assert abs(defect-meta["defect"])<2e-10
        # The exact source value and the positive axial cubic coefficient.
        assert abs(float(phi(0,1e-6,c))/1e-6-.5)<1e-11
        assert (2-1/(2*c))/2>0
        results.append(dict(c=c,S_grid=float(S),axis_error=axis_error,
                            defect=float(defect),status="passed"))
    print(json.dumps(results,indent=2))
    return results

if __name__=="__main__":
    self_test()
