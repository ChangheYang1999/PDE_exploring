"""Physical potential fields for the separate absolute-loss study.

This module never imports or changes the live Stage XII campaign. Numerical
imports require its independent supervisor. The old free coefficients retain
meaning, but derivatives of the potential use unrounded analytic exponents.
Two interpretations are deliberately available: literal serialized c0, and the
constraint-defined analytic chart with implicit c0. Neither writes a candidate.
"""
import copy
import math
import os
from decimal import Decimal, localcontext
from pathlib import Path
import sys

if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Absolute-loss numerical work requires the resource supervisor')
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'base'))
import numpy as np
from spectral_basis import _harmonics, evaluate_modes

D = Decimal
KEYS = ('f','fx','fy','psi','psix','psiy','ratio')
CORE_ORDER = [(m,k) for m in range(4) for k in range(5)] + [(m,5) for m in range(4)]


def _offsets(cl):
    delta=(1-1/cl)/2
    return [0,1,2,delta,2*delta,3*delta]


def _core_exponents(cl):
    gamma=1/cl; delta=(1-gamma)/2
    offsets=[0.,1.,2.,delta,2*delta,3*delta]
    doffsets=[0.,0.,0.,.5/cl**2,1/cl**2,1.5/cl**2]
    A=(3+gamma)/2;dA=-.5/cl**2
    return [(m,A-m-offsets[k],dA-doffsets[k],offsets[k],doffsets[k]) for m,k in CORE_ORDER]


def center_data(cl):
    """Unrounded potential strain, f(0), and their analytic cl derivatives."""
    strain=[]; dstrain=[]; f=[];df=[]
    for m,b,db,_,_ in _core_exponents(float(cl)):
        strain.append(4*b*(b-1) if m==0 else (-24. if m==2 else 0.))
        dstrain.append(4*(2*b-1)*db if m==0 else 0.)
        f.append(-16*b*(b-1) if m==0 else (24*b if m==1 else 0.))
        df.append(-16*(2*b-1)*db if m==0 else (24*db if m==1 else 0.))
    return tuple(np.asarray(z) for z in (strain,dstrain,f,df))


def _decimal_center(cl, coefficients, convention, precision=90):
    with localcontext() as ctx:
        ctx.prec=precision
        L=D.from_float(float(cl));gamma=1/L;delta=(1-gamma)/2;A=(3+gamma)/2
        offsets=[D(0),D(1),D(2),delta,2*delta,3*delta]
        s=[];ds=[]
        for m,k in CORE_ORDER:
            b=A-m-offsets[k];db=-D('0.5')/(L*L)-(D(k-2)/(2*L*L) if k>=3 else D(0))
            s.append(4*b*(b-1) if m==0 else (D(-24) if m==2 else D(0)))
            ds.append(4*(2*b-1)*db if m==0 else D(0))
        c=[D.from_float(float(v)) for v in coefficients]
        original=c[0]
        literal_defect=L-1+sum((v*w for v,w in zip(s,c)),D(0))
        if convention=='center_chart':c[0]=(1-L-sum((s[j]*c[j] for j in range(1,24)),D(0)))/s[0]
        dc0=(-1-sum((ds[j]*c[j] for j in range(24)),D(0)))/s[0] if convention=='center_chart' else D(0)
        return {'coefficients_decimal':[str(v) for v in c], 'strain_decimal':[str(v) for v in s],
                'strain_cl_decimal':[str(v) for v in ds], 'c0_cl_decimal':str(dc0),
                'original_c0':str(original),'analytic_c0':str(c[0]),'c0_correction':str(c[0]-original),
                'literal_center_defect':str(literal_defect),'precision':precision}


def prepare_candidate(case, convention='center_chart', parameters=None, extra=None):
    """Prepare a read-only interpretation of saved coefficients.

    parameters is [cl, c1,...,c23]. In literal mode c0 remains the serialized c0;
    its derivative is zero. In center_chart mode c0 is an implicit analytic
    function of all 24 raw parameters, before enforcing the other five Taylor
    constraints. Changing p in this API does not perform a C5 projection.
    """
    if convention not in ('literal','center_chart'):raise ValueError('Unknown interpretation')
    case=copy.deepcopy(case)
    p=np.asarray(parameters if parameters is not None else case.get('core_parameters',[case['cl']]+case['coefficients'][1:]),dtype=float)
    if p.shape!=(24,) or not np.all(np.isfinite(p)) or p[0]<=1:raise ValueError('Expected finite cl>1 plus 23 old coefficients')
    extras=np.asarray(case.get('extra_coefficients',[]) if extra is None else extra,dtype=float)
    modes=copy.deepcopy(case.get('modes',[]))
    if len(modes)!=len(extras) or not np.all(np.isfinite(extras)):raise ValueError('Invalid extra coefficients/modes')
    coeff=np.r_[float(case['coefficients'][0]),p[1:]]
    dec=_decimal_center(p[0],coeff,convention)
    coeff=np.asarray([float(v) for v in dec['coefficients_decimal']])
    strain,dstrain,_,_=center_data(p[0])
    dc0=np.zeros(24)
    if convention=='center_chart':
        dc0[0]=float(dec['c0_cl_decimal']);dc0[1:]=-strain[1:]/strain[0]
    result={'case':case,'convention':convention,'parameters':p,'p':p,'extra':extras,'modes':modes,
            'coefficients':coeff,'c0_derivative':dc0,'center_metadata':dec,'_taylor_cache':{}}
    result['metadata']={'interpretation':convention,'core_exponents':'unrounded analytic potential derivatives',
       'saved_candidate_modified':False,'reference_amplitude_optimization_dependent':False,**dec}
    return result


def _falling(beta, dbeta):
    F=[1.];dF=[0.]
    for j in range(4):
        dF.append(dF[-1]*(beta-j)+F[-1]*dbeta)
        F.append(F[-1]*(beta-j))
    return F,dF


def _assemble(H,Dfun,Dy,xn,yn,t,F,L):
    h=H(0,0);hx=H(1,0);hy=H(0,1);hxx=H(2,0);hyy=H(0,2);hxy=H(1,1)
    d0=4*((L+1)*F[1]+t*F[2]);d1=4*((L+2)*F[2]+t*F[3]);d2=4*((L+3)*F[3]+t*F[4])
    return {'f':-Dfun(0)*d0-2*h*d1,
       'fx':-Dfun(1)*d0-2*xn*Dfun(0)*d1-2*hx*d1-4*xn*h*d2,
       'fy':-Dy*d0-4*hy*d1-4*yn*h*d2,
       'psi':hxy*F[0]+(2*yn*hx+2*xn*hy)*F[1]+4*xn*yn*h*F[2],
       'psix':H(2,1)*F[0]+(4*xn*hxy+2*hy+2*yn*hxx)*F[1]+(4*xn*xn*hy+8*xn*yn*hx+4*yn*h)*F[2]+8*xn*xn*yn*h*F[3],
       'psiy':H(1,2)*F[0]+(4*yn*hxy+2*hx+2*xn*hyy)*F[1]+(4*yn*yn*hx+8*xn*yn*hy+4*xn*h)*F[2]+8*xn*yn*yn*h*F[3],
       'ratio':Dfun(2)*F[0]+(4*xn*Dfun(1)+2*Dfun(0)+2*hxx)*F[1]+(4*xn*xn*Dfun(0)+8*xn*hx+4*h)*F[2]+8*xn*xn*h*F[3]}


def core_matrices(cl,x,y,cl_derivative=False):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));x=x.ravel();y=y.ravel()
    q=x*x+y*y;R=1+q;u=1/R;t=q*u;s=np.log1p(q);root=np.sqrt(R);xn=x/root;yn=y/root
    mats={key:np.empty((len(x),24)) for key in KEYS};dmats={key:np.empty_like(v) for key,v in mats.items()} if cl_derivative else None
    harmonics={m:_harmonics(xn,yn,t,m) for m in range(4)}
    orders={'f':2.,'fx':2.5,'fy':2.5,'psi':1.,'psix':1.5,'psiy':1.5,'ratio':2.}
    A=(3+1/cl)/2
    for j,(m,b,db,sigma,dsigma) in enumerate(_core_exponents(cl)):
        F,dF=_falling(b,db);values=_assemble(*harmonics[m],xn,yn,t,F,2*m)
        ders=_assemble(*harmonics[m],xn,yn,t,dF,2*m) if cl_derivative else None
        for key in KEYS:
            factor=np.exp((A-sigma-orders[key])*s)
            mats[key][:,j]=factor*values[key]
            if cl_derivative:dmats[key][:,j]=factor*(ders[key]+db*s*values[key])
    return (mats,dmats) if cl_derivative else mats


def fields(prepared,x,y,derivatives=False,block_size=2048):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));x=x.ravel();y=y.ravel()
    p=prepared['parameters'];c=prepared['coefficients'];extra=prepared['extra'];modes=prepared['modes'];ncol=24+len(extra)
    out={key:np.empty(len(x)) for key in KEYS+('q',)}
    dout={key:np.empty((len(x),ncol)) for key in out} if derivatives else None
    strain,dstrain,_,_=center_data(p[0]);dc0=prepared['c0_derivative'];active=np.flatnonzero(extra!=0)
    for lo in range(0,len(x),block_size):
        hi=min(len(x),lo+block_size);xx=x[lo:hi];yy=y[lo:hi]
        if derivatives:M,Mc=core_matrices(p[0],xx,yy,True)
        else:M=core_matrices(p[0],xx,yy)
        for key in KEYS:
            out[key][lo:hi]=M[key]@c
            if derivatives:
                d=dout[key][lo:hi];d[:,0]=Mc[key]@c+M[key][:,0]*dc0[0]
                d[:,1:24]=M[key][:,1:]+M[key][:,:1]*dc0[None,1:]
        if prepared['convention']=='center_chart':
            # This is algebraically the physical cl-1+ratio for the implicit
            # center-compatible potential, not a change to the saved PDE.
            out['q'][lo:hi]=(M['ratio']-strain[None,:])@c
        else:out['q'][lo:hi]=p[0]-1+out['ratio'][lo:hi]
        if derivatives:
            dout['q'][lo:hi,:24]=dout['ratio'][lo:hi,:24]
            dout['q'][lo:hi,0]+=1
        for jlo in range(0,len(modes),32):
            jhi=min(len(modes),jlo+32)
            if derivatives:V,Vc=evaluate_modes(xx,yy,p[0],modes[jlo:jhi],True)
            else:V=evaluate_modes(xx,yy,p[0],modes[jlo:jhi])
            cc=extra[jlo:jhi]
            for key in KEYS:
                out[key][lo:hi]+=V[key]@cc
                if derivatives:
                    dout[key][lo:hi,0]+=Vc[key]@cc
                    dout[key][lo:hi,24+jlo:24+jhi]=V[key]
            out['q'][lo:hi]+=V['ratio']@cc
            if derivatives:
                dout['q'][lo:hi,0]+=Vc['ratio']@cc
                dout['q'][lo:hi,24+jlo:24+jhi]=V['ratio']
    # Polynomial evaluation prevents subtracting O(1) center strains for tiny r.
    small=np.hypot(x,y)<=.02
    if np.any(small):
        from highprecision_origin import field_series,evaluate_series
        polys=field_series(prepared,order=12,derivatives=derivatives)
        for key in out:
            out[key][small]=evaluate_series(polys['fields'][key],x[small],y[small])
            if derivatives:
                for j,poly in enumerate(polys['derivatives'][key]):dout[key][small,j]=evaluate_series(poly,x[small],y[small])
    return (out,dout) if derivatives else out


def residual(prepared,x,y,derivatives=False):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));x=x.ravel();y=y.ravel();cl=prepared['parameters'][0]
    if derivatives:ff,df=fields(prepared,x,y,True)
    else:ff=fields(prepared,x,y)
    wx=cl*x-ff['psiy'];wy=cl*y+ff['psix']
    rf=wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f']
    if derivatives:
        dr=wx[:,None]*df['fx']+wy[:,None]*df['fy']+ff['q'][:,None]*df['f']-ff['fx'][:,None]*df['psiy']+ff['fy'][:,None]*df['psix']+ff['f'][:,None]*df['q']
        dr[:,0]+=x*ff['fx']+y*ff['fy']
    small=np.hypot(x,y)<=.02
    if np.any(small):
        from highprecision_origin import residual_series,evaluate_series
        series=residual_series(prepared,order=12,derivatives=derivatives)
        rf[small]=evaluate_series(series['residual'],x[small],y[small])
        if derivatives:
            for j,poly in enumerate(series['derivatives']):dr[small,j]=evaluate_series(poly,x[small],y[small])
    return (rf,dr) if derivatives else rf


def exact_dilation_fields(prepared,x,y,factor,derivatives=False):
    """Exact evaluation at X/lambda, never a basis refit."""
    factor=float(factor)
    if not factor>0:raise ValueError('Dilation factor must be positive')
    z=fields(prepared,np.asarray(x)/factor,np.asarray(y)/factor,derivatives)
    ff,dd=z if derivatives else (z,None)
    scales={'f':1.,'fx':1/factor,'fy':1/factor,'psi':factor*factor,'psix':factor,'psiy':factor,'ratio':1.,'q':1.}
    ff={k:v*scales[k] for k,v in ff.items()}
    if derivatives:dd={k:v*scales[k] for k,v in dd.items()}
    return (ff,dd) if derivatives else ff
