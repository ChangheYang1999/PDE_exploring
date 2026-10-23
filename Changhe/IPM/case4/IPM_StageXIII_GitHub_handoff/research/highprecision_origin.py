"""Independent Decimal Cartesian binomial algebra at the IPM origin.

No production spatial derivative or harmonic/radial recurrence is used here.
The expansion is about q=x²+y²=0; all supplied potential modes are analytic
there. Truncation diagnostics compare independently built polynomial orders.
They are numerical diagnostics, not a rigorous complex-analytic remainder.
"""
import math
import os
from decimal import Decimal, localcontext
import numpy as np

if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Origin numerical work requires the resource supervisor')
D=Decimal
ORDER=[(m,k) for m in range(4) for k in range(5)]+[(m,5) for m in range(4)]
KEYS=('f','fx','fy','psi','psix','psiy','ratio','q')


def add(a,b,scale=D(1),order=None):
    out=dict(a)
    for k,v in b.items():
        if order is None or sum(k)<=order:out[k]=out.get(k,D(0))+scale*v
    return {k:v for k,v in out.items() if v and (order is None or sum(k)<=order)}


def scale(a,v):return {k:c*v for k,c in a.items() if c*v}


def mul(a,b,order):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l<=order:
                key=(i+k,j+l);out[key]=out.get(key,D(0))+v*w
    return {k:v for k,v in out.items() if v}


def derivative(a,axis):
    out={}
    for (i,j),v in a.items():
        n=i if axis==0 else j
        if n:out[(i-(axis==0),j-(axis==1))]=v*n
    return out


def divide_y(a):
    if any(j==0 and v for (i,j),v in a.items()):raise ValueError('Parity violated in analytic y quotient')
    return {(i,j-1):v for (i,j),v in a.items()}


def _binomial(beta,dbeta,nmax):
    b=[D(1)];db=[D(0)]
    for n in range(1,nmax+1):
        db.append((db[-1]*(beta-n+1)+b[-1]*dbeta)/n)
        b.append(b[-1]*(beta-n+1)/n)
    return b,db


def _conv(a,b,nmax):
    out=[D(0)]*(nmax+1)
    for i,v in enumerate(a):
        for j,w in enumerate(b[:nmax+1-i]):out[i+j]+=v*w
    return out


def _exp_series(a,nmax):
    out=[a[0].exp()]+[D(0)]*nmax
    for n in range(1,nmax+1):out[n]=sum((D(k)*a[k]*out[n-k] for k in range(1,n+1)),D(0))/n
    return out


def radial_series(cl,m,mode,nmax,core_offset=None):
    gamma=1/cl;A=(3+gamma)/2;dA=-D('0.5')/(cl*cl)
    if core_offset is not None:
        offset,doffset=core_offset
        return _binomial(A-m-offset,dA-doffset,nmax)
    sigma=mode.get('sigma',0.)
    if isinstance(sigma,str):
        k={'zero':0,'delta':1,'2delta':2,'3delta':3}[sigma]
        sigma=D(k)*(1-gamma)/2;dsigma=D(k)/(2*cl*cl)
    else:sigma=D.from_float(float(sigma));dsigma=D(0)
    b=A-m-sigma;db=dA-dsigma;k=max(5-m,0)
    result=[D(0)]*(nmax+1);dresult=[D(0)]*(nmax+1)
    amplitude=D.from_float(float(mode.get('scale',1.)))
    if mode['family']=='global':
        if float(mode.get('alpha',0.)) or float(mode.get('beta',0.)):raise ValueError('Origin independent algebra presently supports supplied Legendre modes only')
        n=int(mode['n']);normal=D(2*n+1).sqrt() if mode.get('normalize',True) else D(1)
        # P_n(2t-1)=sum_j (-1)^(n-j) C(n,j)C(n+j,j)t^j.
        for j in range(min(n,nmax-k)+1):
            coeff=D((-1)**(n-j)*math.comb(n,j)*math.comb(n+j,j))*normal*amplitude
            radial,dradial=_binomial(b-k-j,db,nmax-k-j)
            for l,v in enumerate(radial):result[k+j+l]+=coeff*v
            for l,v in enumerate(dradial):dresult[k+j+l]+=coeff*v
    elif mode['family']=='local':
        c=D.from_float(float(mode['center']));w=D.from_float(float(mode['width']))
        log=[D(0)]+[D((-1)**(j+1))/j for j in range(1,nmax+1)]
        z=log[:];z[0]-=c;z=[v/w for v in z]
        g=_exp_series([-v/2 for v in _conv(z,z,nmax)],nmax)
        radial,dradial=_binomial(b-k,db,max(0,nmax-k))
        rv=_conv(radial,g,max(0,nmax-k));rd=_conv(dradial,g,max(0,nmax-k))
        for j,v in enumerate(rv):
            if k+j<=nmax:result[k+j]=amplitude*v
        for j,v in enumerate(rd):
            if k+j<=nmax:dresult[k+j]=amplitude*v
    else:raise ValueError('Unknown mode')
    return result,dresult


def potential_polynomial(cl,m,order,mode=None,core_offset=None):
    if 2*m>order:return {},{}
    nmax=(order-2*m)//2;radial,dradial=radial_series(cl,m,mode,nmax,core_offset)
    out={};dout={}
    for j in range(m+1):
        angular=D((-1)**j*math.comb(2*m,2*j));hx=2*m-2*j;hy=2*j
        for n,(v,dv) in enumerate(zip(radial,dradial)):
            for l in range(n+1):
                key=(hx+2*l,hy+2*(n-l));fac=angular*math.comb(n,l)
                out[key]=out.get(key,D(0))+fac*v;dout[key]=dout.get(key,D(0))+fac*dv
    return {k:v for k,v in out.items() if v},{k:v for k,v in dout.items() if v}


def _fields(chi,order):
    dx=derivative(chi,0);dy=derivative(chi,1);lap=add(derivative(dx,0),derivative(dy,1))
    f=scale(divide_y(derivative(lap,1)),D(-1));psi=derivative(dx,1);psix=derivative(psi,0)
    result={'f':f,'fx':derivative(f,0),'fy':derivative(f,1),'psi':psi,'psix':psix,'psiy':derivative(psi,1),'ratio':divide_y(psix)}
    return {key:{k:v for k,v in poly.items() if sum(k)<=order} for key,poly in result.items()}


def field_series(prepared,order=12,derivatives=False,precision=90):
    cache=prepared['_taylor_cache'];key=('fields',order,derivatives,precision)
    if key in cache:return cache[key]
    with localcontext() as ctx:
        ctx.prec=precision
        cl=D.from_float(float(prepared['parameters'][0]));delta=(1-1/cl)/2
        offs=[D(0),D(1),D(2),delta,2*delta,3*delta];doffs=[D(0)]*3+[D(1)/(2*cl*cl),D(1)/(cl*cl),D(3)/(2*cl*cl)]
        cc=[D(v) for v in prepared['center_metadata']['coefficients_decimal']]
        extra=[D.from_float(float(v)) for v in prepared['extra']]
        core=[];corecl=[]
        for m,k in ORDER:
            chi,dchi=potential_polynomial(cl,m,order+4,core_offset=(offs[k],doffs[k]))
            core.append(_fields(chi,order));corecl.append(_fields(dchi,order))
        new=[];newcl=[]
        for mode in prepared['modes']:
            chi,dchi=potential_polynomial(cl,int(mode['m']),order+4,mode=mode)
            new.append(_fields(chi,order));newcl.append(_fields(dchi,order))
        total={k:{} for k in KEYS};dt={k:[] for k in KEYS} if derivatives else None
        for name in KEYS[:-1]:
            for c,v in zip(cc,core):total[name]=add(total[name],v[name],c,order)
            for c,v in zip(extra,new):total[name]=add(total[name],v[name],c,order)
            if derivatives:
                clpoly={}
                for c,v in zip(cc,corecl):clpoly=add(clpoly,v[name],c,order)
                for c,v in zip(extra,newcl):clpoly=add(clpoly,v[name],c,order)
                clpoly=add(clpoly,core[0][name],D(prepared['center_metadata']['c0_cl_decimal']),order)
                dt[name].append(clpoly)
                ss=[D(v) for v in prepared['center_metadata']['strain_decimal']]
                for j in range(1,24):
                    dc=-ss[j]/ss[0] if prepared['convention']=='center_chart' else D(0)
                    dt[name].append(add(core[j][name],core[0][name],dc,order))
                dt[name].extend(v[name] for v in new)
        total['q']=add(total['ratio'],{(0,0):cl-1},order=order)
        if prepared['convention']=='center_chart':total['q'].pop((0,0),None)
        if derivatives:
            dt['q']=[dict(v) for v in dt['ratio']]
            dt['q'][0]=add(dt['q'][0],{(0,0):D(1)},order=order)
            if prepared['convention']=='center_chart':
                for poly in dt['q']:poly.pop((0,0),None)
        result={'fields':total,'derivatives':dt,'order':order,'precision':precision,'method':'independent Cartesian Decimal binomial potential expansion; exact analytic center condition when selected'}
    cache[key]=result
    return result


def residual_series(prepared,order=12,derivatives=False,precision=90):
    cache=prepared['_taylor_cache'];key=('residual',order,derivatives,precision)
    if key in cache:return cache[key]
    with localcontext() as ctx:
        ctx.prec=precision
        data=field_series(prepared,order,derivatives,precision);ff=data['fields'];cl=D.from_float(float(prepared['parameters'][0]))
        wx=add({(1,0):cl},ff['psiy'],D(-1),order);wy=add({(0,1):cl},ff['psix'],order=order)
        rf=add(add(mul(wx,ff['fx'],order),mul(wy,ff['fy'],order),order=order),mul(ff['q'],ff['f'],order),order=order)
        dr=[]
        if derivatives:
            df=data['derivatives']
            for j in range(24+len(prepared['extra'])):
                z=add(mul(wx,df['fx'][j],order),mul(wy,df['fy'][j],order),order=order)
                z=add(z,mul(ff['q'],df['f'][j],order),order=order)
                z=add(z,mul(ff['fx'],df['psiy'][j],order),D(-1),order)
                z=add(z,mul(ff['fy'],df['psix'][j],order),order=order)
                z=add(z,mul(ff['f'],df['q'][j],order),order=order)
                if j==0:
                    z=add(z,mul({(1,0):D(1)},ff['fx'],order),order=order)
                    z=add(z,mul({(0,1):D(1)},ff['fy'],order),order=order)
                dr.append(z)
        result={'residual':rf,'derivatives':dr if derivatives else None,'order':order,'precision':precision,'constant':str(rf.get((0,0),D(0))),
                'degree_l1_coefficients':{str(n):str(sum((abs(v) for k,v in rf.items() if sum(k)==n),D(0))) for n in range(order+1)}}
    cache[key]=result
    return result


def evaluate_series(poly,x,y):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));out=np.zeros_like(x)
    # Sum from largest degree to constant. Each residual degree coefficient
    # was formed before binary64 rounding, so no cancelled low-degree O(1) terms.
    for (i,j),v in sorted(poly.items(),key=lambda kv:sum(kv[0]),reverse=True):out+=float(v)*x**i*y**j
    return out


def origin_diagnostics(prepared,radius=.02,a_ref=1.,orders=(12,16),precision=90):
    rows=[]
    for order in orders:
        s=residual_series(prepared,order,False,precision);p=s['residual']
        constant=p.get((0,0),D(0))
        if constant:
            integral=None;divergent=True
        else:
            integral=0.;divergent=False
            for (i,j),v in p.items():
                for (k,l),w in p.items():
                    degree=i+j+k+l
                    if degree:
                        angular=.5*math.exp(math.lgamma((i+k+1)/2)+math.lgamma((j+l+1)/2)-math.lgamma((degree+2)/2))
                        integral+=float(v)*float(w)*radius**degree/degree*angular/(math.pi*a_ref*a_ref)
        theta=np.linspace(0,math.pi/2,129);rv=evaluate_series(p,radius*np.cos(theta),radius*np.sin(theta))
        # A coefficient triangle bound applies to this polynomial only, not
        # automatically to the uncomputed analytic remainder.
        bound=sum(float(abs(v))*radius**sum(k) for k,v in p.items())
        rows.append({'order':order,'precision':precision,'constant_residual_decimal':str(constant),'divergent_at_origin':divergent,
            'polynomial_origin_integral':integral,'polynomial_boundary_sampled_max':float(np.max(abs(rv))),
            'polynomial_boundary_coefficient_l1_bound':bound,'degree_l1_coefficients':s['degree_l1_coefficients']})
    delta=None if any(r['polynomial_origin_integral'] is None for r in rows) else abs(rows[-1]['polynomial_origin_integral']-rows[-2]['polynomial_origin_integral'])
    return {'radius':radius,'rows':rows,'successive_order_integral_difference':delta,
       'remainder_rigorous_bound':False,'limitation':'order refinement and direct overlap checks are numerical truncation diagnostics; no rigorous continuous remainder enclosure is asserted'}
