"""Second local nonlinear forcing, including genuine higher-order resonances."""
import numpy as np
from numpy.polynomial import Polynomial as Poly
from numpy.polynomial.legendre import poly2leg
from independent_farfield import angular_data


def bilinear_advection(F,G,exponent_G):
    """Angular coefficients of (R^-a F dot grad)(R^-b G).

    Input vector triples are (radial, polar/sin(theta), swirl/sin(theta)).
    Output uses the same convention. Its radial homogeneity is -a-b-1.
    """
    fr,c,b=F;gr,d,h=G
    mu=Poly([0.,1.]);s2=Poly([1.,0.,-1.]);beta=exponent_G
    radial=-beta*fr*gr-s2*c*gr.deriv()-s2*(c*d+b*h)
    polar=-beta*fr*d+c*(mu*d-s2*d.deriv())+c*gr-mu*b*h
    swirl=-beta*fr*h+c*(mu*h-s2*h.deriv())+b*gr+mu*b*d
    return radial,polar,swirl


def second_forcing(alpha,A,B):
    first=angular_data(alpha,A,B)
    F=[first['FR'],first['C'],first['B']]
    G=[first['GR'],first['GV'],first['GW']]
    N=[x+y for x,y in zip(bilinear_advection(F,G,2*alpha+1),bilinear_advection(G,F,alpha))]
    s2=Poly([1.,0.,-1.])
    source=-3*alpha*N[0]-(s2*N[1]).deriv()
    modes=poly2leg(source.coef)
    pressure_power=3*alpha+1
    ell=np.arange(len(modes));eigen=ell*(ell+1)-pressure_power*(pressure_power-1)
    resonant=np.flatnonzero(np.abs(eigen)<1e-11)
    logs={int(l):float(modes[l]/(2*pressure_power-1)) for l in resonant}
    return {'first':first,'N':N,'source':source,'source_legendre':modes,
            'pressure_power':pressure_power,'eigenvalues':eigen,'resonant_log_coefficients':logs}
