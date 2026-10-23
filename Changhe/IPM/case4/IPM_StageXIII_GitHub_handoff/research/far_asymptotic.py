"""Analytic leading power-tail diagnostic for the absolute quotient residual.

The asymptotic coefficient is not a uniform remainder bound. It complements
whole-radius expansion, shell integration, and the separate outer envelope.
"""
import math
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Far-asymptotic arithmetic requires the resource supervisor')
import numpy as np
from scipy.special import gammaln
from absolute_fields import _assemble,_falling,_core_exponents
from spectral_basis import _harmonics,tail_exponent,validate_mode

KEYS=('f','fx','fy','psix','psiy','ratio')


def _mode_amplitude(mode):
    n=int(mode['n']);a=float(mode.get('alpha',0.));b=float(mode.get('beta',0.))
    lognorm=(gammaln(a+1)+gammaln(b+1)-gammaln(a+b+2)) if n==0 else (gammaln(n+a+1)+gammaln(n+b+1)-math.log(2*n+a+b+1)-gammaln(n+1)-gammaln(n+a+b+1))
    normal=math.exp(-.5*lognorm) if mode.get('normalize',True) else 1.
    endpoint=math.exp(gammaln(n+a+1)-gammaln(a+1)-gammaln(n+1))
    return float(mode.get('scale',1.))*normal*endpoint


def leading_residual_coefficient(prepared,theta):
    """C(theta) in Rf(r,theta)=C(theta) r^(2 gamma-2)+o(...).

    For sigma=0 the linear transport cancels by homogeneity. The leading
    coefficient is the sigma=0 quadratic term plus linear sigma=delta term,
    delta=(1-gamma)/2. Local log-Gaussian modes decay faster than any power.
    Existing cores have no smaller positive sigma than delta. We refuse an
    added slower exponent because the stated leading-power formula changes.
    """
    theta=np.asarray(theta,dtype=float).ravel();xn=np.cos(theta);yn=np.sin(theta);t=np.ones_like(theta)
    cl=float(prepared['parameters'][0]);gamma=1/cl;delta=(1-gamma)/2;A=(3+gamma)/2
    zero={key:np.zeros_like(theta) for key in KEYS};first={key:np.zeros_like(theta) for key in KEYS}
    H={};records=[]
    def incorporate(m,beta,sigma,amplitude,source):
        if sigma>0 and sigma<delta:raise ValueError('A slower positive tail exponent changes the leading residual power')
        if sigma==0:target=zero;kind='sigma0'
        elif sigma==delta:target=first;kind='sigma_delta'
        else:return
        if m not in H:H[m]=_harmonics(xn,yn,t,m)
        F,_=_falling(beta,0.)
        values=_assemble(*H[m],xn,yn,t,F,2*m)
        for key in KEYS:target[key]+=amplitude*values[key]
        records.append({'source':source,'m':m,'sigma':float(sigma),'amplitude':float(amplitude),'kind':kind})
    for j,((m,beta,_,sigma,_),coef) in enumerate(zip(_core_exponents(cl),prepared['coefficients'])):
        incorporate(m,beta,sigma,float(coef),'core_'+str(j))
    for j,(mode,coef) in enumerate(zip(prepared['modes'],prepared['extra'])):
        if mode['family']=='local':continue
        m=validate_mode(mode);sigma,_=tail_exponent(mode,cl)
        incorporate(m,A-m-sigma,sigma,float(coef)*_mode_amplitude(mode),'extra_'+str(j))
    nonlinear=-zero['psiy']*zero['fx']+zero['psix']*zero['fy']+zero['ratio']*zero['f']
    linear=-2*cl*delta*first['f']
    coefficient=nonlinear+linear
    return {'theta':theta,'coefficient':coefficient,'sigma0_nonlinear':nonlinear,'sigma_delta_linear':linear,
        'gamma':gamma,'residual_power':2*gamma-2,'squared_residual_power':4*gamma-4,
        'participating_modes':records,'leading_term_may_cancel':True,
        'uniform_remainder_bound':False}


def leading_tail_estimate(prepared,log_radius,a_ref,angular_order=128,dilation=1.):
    z,w=np.polynomial.legendre.leggauss(angular_order);theta=(z+1)*np.pi/4;weight=w*np.pi/4
    info=leading_residual_coefficient(prepared,theta);p=info['residual_power'];factor=float(dilation)**(-p)
    square_integral=float(weight@(info['coefficient']*factor)**2)
    estimate=square_integral*math.exp(2*p*float(log_radius))/(-2*p*math.pi*float(a_ref)**2)
    return {'log_radius':float(log_radius),'radius':math.exp(float(log_radius)),
       'dilation':float(dilation),'residual_power':p,'angular_order':angular_order,
       'angular_coefficient_square_integral':square_integral,'leading_power_tail_estimate':estimate,
       'rigorous_error_bound':False,'uses_full_asymptotic_infinite_tail':True,
       'limitation':'leading coefficient only; compare consecutive exterior shells and the independent uniform envelope before accepting numerical tails'}


def run():
    from absolute_common import load_case,OUT,A_REF,atomic,provenance,sources
    from absolute_fields import prepare_candidate,residual
    rows={}
    z,w=np.polynomial.legendre.leggauss(96);theta=(z+1)*np.pi/4;wt=w*np.pi/4
    for label in ('stage11','combined','local','global'):
        model=prepare_candidate(load_case(label));info=leading_residual_coefficient(model,theta);C=info['coefficient'];p=info['residual_power']
        samples=[]
        for radius in (1e4,1e6,1e8,1e10,1e12):
            raw=residual(model,radius*np.cos(theta),radius*np.sin(theta));scaled=raw/radius**p
            samples.append({'radius':radius,'coefficient_l2_scaled_error':float(np.sqrt(wt@(scaled-C)**2)/max(1.,np.sqrt(wt@C**2))),
                'coefficient_max_abs_error':float(np.max(abs(scaled-C))),'sampled_Rf_max':float(np.max(abs(raw))),
                'leading_tail':leading_tail_estimate(model,math.log(radius),A_REF)})
        rows[label]={'residual_power':p,'coefficient_maximum_abs_sampled':float(np.max(abs(C))),
            'coefficient_l2':float(np.sqrt(wt@C**2)),'samples':samples,
            'sampled_asymptotic_error_not_uniform_remainder_bound':True}
    report={'completed':True,'candidates':rows,'asymptotic_formula':'C=N(sigma0,sigma0)-2cl*delta*F_delta; Rf~r^(2gamma-2)*C',
        'rigorous_uniform_remainder_bound':False,'a_ref':A_REF,'provenance':provenance(),'sources':sources()}
    atomic(OUT/'far_asymptotic_checks.json',report)
    print('Analytic far asymptotic diagnostics completed')

if __name__=='__main__':run()
