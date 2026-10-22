"""Physical mode and radial energies, independent of coefficient-center proxies."""
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import roots_jacobi


def physical_energy_distribution(state, vector, H, active, order=32, delta=.25, R=1.):
    b=state.bb;L=state.L;active=np.asarray(active)
    cuts_r=np.array([.1,1.,10.,100.,1000.,10000.,1.e6])
    cuts_t=-np.expm1(-np.log1p((cuts_r/L)**2)/(2*b))
    edges=np.unique(np.r_[state.edges,cuts_t]);edges.sort()
    a=np.zeros(state.K*state.nb);a[active]=vector;a=a.reshape(state.K,state.nb)
    mode_energy=[]
    for k in range(state.K):
        ii=np.flatnonzero(active//state.nb==k);z=vector[ii]
        mode_energy.append(float(z@H[np.ix_(ii,ii)]@z))
    radial=np.zeros(len(cuts_r)+1)
    for parity in [0,1]:
        ts=[];ws=[]
        for lo,hi in zip(edges[:-1],edges[1:]):
            for sign in [-1,1]:
                p=sign*delta;alpha=1-b*p if hi==1 else 0.;gamma=p/2+parity if lo==0 else 0.
                xx,ww=roots_jacobi(order,alpha,gamma)
                t=lo+(hi-lo)*(1+xx)/2;u=1-t
                eta2=-np.expm1(2*b*np.log(u))
                logrem=(1-b*p)*np.log(u)+(p/2+parity)*np.log(eta2)
                if lo==0:logrem-=gamma*np.log(t)
                if hi==1:logrem-=alpha*np.log(u)
                ts.append(t);ws.append(b*L*L*(L/R)**p*((hi-lo)/2)**(1+alpha+gamma)*ww*np.exp(logrem))
        t=np.concatenate(ts);w=np.concatenate(ws)
        B=BSpline(state.knots,np.eye(state.nb),state.degree,extrapolate=False)(t)
        ks=np.arange(parity,state.K,2);angular=np.pi*np.where(ks==0,2.,1.)
        val=B@a[ks].T;energy=w*np.sum(angular[None,:]*val**2,axis=1)
        radial+=np.bincount(np.searchsorted(cuts_t,t,side='right'),weights=energy,minlength=len(radial))
    total=float(vector@H@vector)
    return {'norm_squared':total,'mode_energy':mode_energy,'mode_fraction':(np.array(mode_energy)/total).tolist(),'radial_cuts':cuts_r.tolist(),'radial_energy':radial.tolist(),'radial_fraction':(radial/total).tolist(),'mode_partition_relative_error':abs(sum(mode_energy)/total-1),'radial_partition_relative_error':abs(float(radial.sum())/total-1),'order':order,'delta':delta,'R':R,'scope':'Physical weighted energies of represented finite-basis fields; radial integrals are floating-point Gauss-Jacobi quadrature, not enclosures.'}
