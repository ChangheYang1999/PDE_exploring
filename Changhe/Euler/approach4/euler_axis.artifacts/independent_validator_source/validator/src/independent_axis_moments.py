"""Target-centred, absolutely convergent five-dimensional axis moments."""
import numpy as np
from scipy.special import roots_jacobi
from independent_pressure import geometric_edges,shell_nodes
from independent_weighted_identities import power_nodes

def axis_moments(field,z1,*,nradial=40,nangle=64,cutoff_factor=32):
    scale=max(field.phi.length,field.q.length,abs(z1));cutoff=cutoff_factor*scale
    mu,wm=roots_jacobi(nangle,1.,1.)
    rho,w=shell_nodes(geometric_edges(cutoff,scale),nradial)
    eta=field.eta(rho[:,None]*np.sqrt(1-mu*mu),z1+rho[:,None]*mu)
    inner_phi=.25*np.dot(w*rho,eta@wm)
    inner_dphi=.75*np.dot(w,eta@(mu*wm))
    alpha=field.alpha
    t,wt=power_nodes(nradial,alpha-1)
    R=cutoff/t;eta=field.eta(R[:,None]*np.sqrt(1-mu*mu),z1+R[:,None]*mu)
    tail_phi=.25*cutoff**2*np.dot(wt,(eta@wm)/t**(alpha+2))
    t,wt=power_nodes(nradial,alpha)
    R=cutoff/t;eta=field.eta(R[:,None]*np.sqrt(1-mu*mu),z1+R[:,None]*mu)
    tail_dphi=.75*cutoff*np.dot(wt,(eta@(mu*wm))/t**(alpha+2))
    value=float(inner_phi+tail_phi);derivative=float(inner_dphi+tail_dphi)
    return {'z1':float(z1),'phi_moment':value,'phi_z_moment':derivative,
            'phi_analytic':float(field.phi.evaluate(0.,z1)),'phi_z_analytic':float(field.phi.evaluate(0.,z1,0,1)),
            'S1_position_moment_defect':4*value+2*field.c_l*z1,
            'S1_strain_moment_defect':4*derivative/3-2/3,
            'cutoff':cutoff,'tail_phi':float(tail_phi),'tail_phi_z':float(tail_dphi),
            'nradial':nradial,'nangle':nangle,'principal_value_used':False,
            'scope':'The two S1 defects apply only when z1 is claimed to be an S1 source. General-field moment equalities test the inverse.'}
