"""Axis-regular tenth-order-vanishing spectral potential modes.

No historical engine is imported or changed. All arrays are float64, point-major.
Numeric callers must run under the experiment's verified resource supervisor.
"""
import math
import os
import numpy as np
from scipy.special import eval_jacobi, gammaln

FIELDS = ('chi', 'f', 'fx', 'fy', 'psi', 'psix', 'psiy', 'ratio')
_STIRLING = ((1,), (0,1), (0,-1,1), (0,1,-3,1), (0,-1,7,-6,1))


def _guard():
    if not os.environ.get('IPM_RESOURCE_SESSION'):
        raise RuntimeError('Numerical spectral evaluation requires the verified resource supervisor')


def tail_exponent(mode, cl):
    """Return sigma and d(sigma)/d(cl); negative exponents are forbidden."""
    value=mode.get('sigma',0.)
    if isinstance(value,str):
        names={'zero':0,'delta':1,'2delta':2,'3delta':3}
        if value not in names: raise ValueError('Unknown tail exponent '+value)
        k=names[value]; sigma=k*(1.-1./cl)/2.; derivative=k/(2.*cl*cl)
    else: sigma=float(value); derivative=0.
    if sigma<0 or not math.isfinite(sigma): raise ValueError('sigma must be nonnegative and finite')
    return sigma,derivative


def validate_mode(mode):
    family=mode['family'];m=int(mode['m'])
    if m<0 or m!=mode['m']: raise ValueError('m must be a nonnegative integer')
    if family=='global':
        n=int(mode['n'])
        if n<0 or n!=mode['n']: raise ValueError('n must be a nonnegative integer')
        if float(mode.get('alpha',0.))<=-1 or float(mode.get('beta',0.))<=-1: raise ValueError('Jacobi alpha,beta must exceed -1')
    elif family=='local':
        if not math.isfinite(float(mode['center'])) or not (0<float(mode['width'])<math.inf): raise ValueError('Invalid local center/width')
        if float(mode.get('sigma',0.))!=0: raise ValueError('Local modes use sigma=0; Gaussian gives superalgebraic decay')
    else: raise ValueError('Unknown basis family '+str(family))
    if not math.isfinite(float(mode.get('scale',1.))): raise ValueError('Invalid mode scale')
    return m


def _t_power_derivatives(t,k):
    out=[]
    for h in range(5):
        out.append(np.zeros_like(t) if h>k else math.factorial(k)//math.factorial(k-h)*t**(k-h))
    return out


def _s_from_t(jets,u):
    return [sum((coef*u**l*jets[l] for l,coef in enumerate(_STIRLING[h])),np.zeros_like(u)) for h in range(5)]


def _radial(mode,t,u,s,beta,dbeta):
    """g^(j)=R^(beta-j) F_j, j=0..4; return F and d_cl F."""
    m=int(mode['m']);k=max(5-m,0);tp=_t_power_derivatives(t,k)
    if mode['family']=='global':
        n=int(mode['n']);alpha=float(mode.get('alpha',0.));b=float(mode.get('beta',0.))
        # Unit Jacobi-weighted L2(dt) normalization; Legendre uses unit weight. Generalized norm uses log-Gamma.
        lognorm=(gammaln(alpha+1)+gammaln(b+1)-gammaln(alpha+b+2)) if n==0 else (gammaln(n+alpha+1)+gammaln(n+b+1)-math.log(2*n+alpha+b+1)-gammaln(n+1)-gammaln(n+alpha+b+1))
        normal=math.exp(-.5*lognorm) if mode.get('normalize',True) else 1.
        poly=[];rising=1.
        for h in range(5):
            if h: rising*=n+alpha+b+h
            poly.append(np.zeros_like(t) if h>n else normal*rising*eval_jacobi(n-h,alpha+h,b+h,2*t-1))
        jets=[sum((math.comb(h,j)*tp[j]*poly[h-j] for j in range(h+1)),np.zeros_like(t)) for h in range(5)]
        sj=_s_from_t(jets,u)
    else:
        st=_s_from_t(tp,u);width=float(mode['width']);z=(s-float(mode['center']))/width
        gauss=np.exp(-.5*z*z);hermite=[np.ones_like(z),z]
        for h in range(1,4): hermite.append(z*hermite[-1]-h*hermite[-2])
        gj=[(-1.)**h*hermite[h]*gauss/width**h for h in range(5)]
        sj=[sum((math.comb(h,j)*st[j]*gj[h-j] for j in range(h+1)),np.zeros_like(t)) for h in range(5)]
    F=[];dF=[];djet=[np.zeros_like(t) for _ in range(5)]
    for j in range(5):
        F.append(sj[0]);dF.append(djet[0])
        if j<4:
            djet=[dbeta*sj[h]+(beta-j)*djet[h]+djet[h+1] for h in range(4-j)]
            sj=[(beta-j)*sj[h]+sj[h+1] for h in range(4-j)]
    return F,dF


def _harmonics(xn,yn,t,m):
    """Normalized homogeneous harmonic derivatives and analytic y quotients."""
    degree=2*m;z=xn+1j*yn;powers={};power=np.ones_like(z)
    for j in range(degree+1):
        if j>=degree-3:powers[j]=power
        power=power*z
    hcache={};dcache={}
    def H(a,b):
        d=a+b
        if (a,b) not in hcache:
            hcache[(a,b)]=np.zeros_like(xn) if d>degree else math.prod(range(degree-d+1,degree+1))*np.real((1j**b)*powers[degree-d])
        return hcache[(a,b)]
    # S_n=Im(z^n)/yn, V_n=(partial_yn S_n)/yn, polynomial recurrences.
    S=[np.zeros_like(xn),np.ones_like(xn)];V=[np.zeros_like(xn),np.zeros_like(xn)]
    for j in range(1,max(1,degree-1)):
        S.append(2*xn*S[-1]-t*S[-2]);V.append(2*xn*V[-1]-2*S[-3]-t*V[-2])
    def D(a):
        # partial_x^a(partial_y H / y), effective homogeneous degree degree-a-2.
        if a not in dcache:
            dcache[a]=np.zeros_like(xn) if degree-a-1<1 else -math.prod(range(degree-a,degree+1))*S[degree-a-1]
        return dcache[a]
    Dy=np.zeros_like(xn) if degree<2 else -degree*yn*V[degree-1]
    return H,D,Dy


def _one(xn,yn,t,u,s,cl,mode,cl_derivative,harmonic=None):
    m=validate_mode(mode);sigma,dsigma=tail_exponent(mode,cl) if mode['family']=='global' else (0.,0.)
    A=(3.+1./cl)/2.;dA=-.5/(cl*cl);beta=A-m-sigma;dbeta=dA-dsigma
    F,dF=_radial(mode,t,u,s,beta,dbeta);H,D,Dy=_harmonics(xn,yn,t,m) if harmonic is None else harmonic;L=2*m
    h=H(0,0);hx=H(1,0);hy=H(0,1);hxx=H(2,0);hyy=H(0,2);hxy=H(1,1)
    def assemble(F):
        d0=4*((L+1)*F[1]+t*F[2]);d1=4*((L+2)*F[2]+t*F[3]);d2=4*((L+3)*F[3]+t*F[4])
        return {
            'chi':h*F[0],
            'f':-D(0)*d0-2*h*d1,
            'fx':-D(1)*d0-2*xn*D(0)*d1-2*hx*d1-4*xn*h*d2,
            'fy':-Dy*d0-4*hy*d1-4*yn*h*d2,
            'psi':hxy*F[0]+(2*yn*hx+2*xn*hy)*F[1]+4*xn*yn*h*F[2],
            'psix':H(2,1)*F[0]+(4*xn*hxy+2*hy+2*yn*hxx)*F[1]+(4*xn*xn*hy+8*xn*yn*hx+4*yn*h)*F[2]+8*xn*xn*yn*h*F[3],
            'psiy':H(1,2)*F[0]+(4*yn*hxy+2*hx+2*xn*hyy)*F[1]+(4*yn*yn*hx+8*xn*yn*hy+4*xn*h)*F[2]+8*xn*yn*yn*h*F[3],
            'ratio':D(2)*F[0]+(4*xn*D(1)+2*D(0)+2*hxx)*F[1]+(4*xn*xn*D(0)+8*xn*hx+4*h)*F[2]+8*xn*xn*h*F[3]}
    values=assemble(F);ders=assemble(dF) if cl_derivative else None
    orders={'chi':0.,'f':2.,'fx':2.5,'fy':2.5,'psi':1.,'psix':1.5,'psiy':1.5,'ratio':2.}
    scale=float(mode.get('scale',1.))
    for key in FIELDS:
        factor=scale*np.exp((A-sigma-orders[key])*s)
        if cl_derivative: ders[key]=factor*(ders[key]+dbeta*s*values[key])
        values[key]=factor*values[key]
    return values,ders


def evaluate_modes(x,y,cl,modes,cl_derivative=False):
    """Return fields for each potential coefficient as shape (n_points,n_modes).

    With cl_derivative=True return (fields, d_fields_d_cl), otherwise fields.
    Axis values are analytic extensions, including ratio=psi_x/y. The historical
    engine is never reevaluated through this module. cl is an unrounded analytic
    exponent for new modes only. For empty modes outputs have shape (N,0).
    """
    _guard();cl=float(cl)
    if not (1.<cl<math.inf): raise ValueError('cl must exceed one')
    x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float));x=x.ravel();y=y.ravel()
    q=x*x+y*y;R=1.+q;u=1./R;t=q*u;s=np.log1p(q);root=np.sqrt(R);xn=x/root;yn=y/root
    out={key:np.empty((len(x),len(modes))) for key in FIELDS}
    dout={key:np.empty_like(out[key]) for key in FIELDS} if cl_derivative else None
    harmonics={}
    for j,mode in enumerate(modes):
        m=validate_mode(mode)
        if m not in harmonics:harmonics[m]=_harmonics(xn,yn,t,m)
        values,ders=_one(xn,yn,t,u,s,cl,mode,cl_derivative,harmonics[m])
        for key in FIELDS:
            out[key][:,j]=values[key]
            if cl_derivative:dout[key][:,j]=ders[key]
    return (out,dout) if cl_derivative else out


def metadata(modes):
    return {'count':len(modes),'maximum_angular_m':max((validate_mode(q) for q in modes),default=0),
            'minimum_potential_origin_degree':min((2*max(5,int(q['m'])) for q in modes),default=None),
            'new_mode_exponents':'unrounded analytic; historical core evaluator unchanged',
            'jacobi_default':'unit-L2(dt) normalized Legendre, alpha=beta=0',
            'axis_quotients':'symbolic homogeneous harmonic recurrences; no y division',
            'canonical_identity':'psi=chi_xy, rho=-partial_y Laplacian(chi)'}
