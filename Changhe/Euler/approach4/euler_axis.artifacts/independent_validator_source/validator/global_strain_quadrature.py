"""Independent full-space quadrature for an odd transported eta=e."""
import numpy as np
from scipy.special import roots_legendre,roots_jacobi

def strain_rule(c_l,nradial=24,nangle=96,cutoff=64.,extra_edges=()):
    if not .5<float(c_l)<1 or nradial<2 or nangle<2 or cutoff<1:raise ValueError('Unsupported parameters')
    beta=1/float(c_l);mu,angular=roots_legendre(nangle);mu=(mu+1)/2;angular=angular/2
    angular*=1.5*mu*(1-mu*mu)
    exponents=np.arange(-8,int(np.ceil(np.log2(cutoff)))+1)
    edges=sorted(set([0.,float(cutoff)]+[float(v)for v in 2.**exponents if v<cutoff]+[float(v)for v in extra_edges if 0<v<cutoff]))
    x,w=roots_legendre(nradial);radii=[];weights=[];bands=[]
    for lo,hi in zip(edges,edges[1:]):
        if lo==0:R=hi*(x+1)/2;wr=hi*w/2
        else:
            a,b=np.log(lo),np.log(hi);R=np.exp((a+b)/2+(b-a)*x/2);wr=(b-a)*w*R/2
        radii.extend(R);weights.extend(wr);bands.extend([len(set(bands))]*len(R))
    x,w=roots_jacobi(nradial,0,beta-1);t=(x+1)/2;w=w/2**beta
    radii.extend(cutoff/t);weights.extend(w*cutoff/t**(beta+1));bands.extend([-1]*nradial)
    return {'R':np.array(radii),'radial_weights':np.array(weights),'mu':mu,'angular_weights':angular,'band':np.array(bands),'edges':edges,'beta':beta,'cutoff':cutoff,'nradial':nradial,'nangle':nangle}

def strain_values(rule,e):
    R=rule['R'];mu=rule['mu'];e=np.asarray(e)
    if e.shape!=(len(R),len(mu))or not np.all(np.isfinite(e)):raise ValueError('Invalid integrand')
    terms=rule['radial_weights'][:,None]*rule['angular_weights'][None,:]*e
    return {'S':float(np.sum(terms)),'Spos':float(np.sum(np.maximum(terms,0))),'Sneg':float(-np.sum(np.minimum(terms,0))),'tail':float(np.sum(terms[rule['band']==-1])),'radial_contributions':np.sum(terms,axis=1)}
