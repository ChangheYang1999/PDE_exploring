"""Finite Fourier transport projections using the independently derived inverse."""
from fractions import Fraction as F
import mpmath as mp
from smooth_mp_primitives import number


def polynomial_and_derivative(coeff,t):
    """Forward Chebyshev and differentiated recurrences, not Clenshaw."""
    t=mp.mpf(t);T0=mp.mpf(1);d0=mp.mpf(0)
    values=[number(coeff[0])];derivatives=[mp.mpf(0)]
    if len(coeff)>1:
        T1=t;d1=mp.mpf(1);values.append(number(coeff[1])*T1);derivatives.append(number(coeff[1]))
        for c in coeff[2:]:
            T2=2*t*T1-T0;d2=2*T1+2*t*d1-d0
            values.append(number(c)*T2);derivatives.append(number(c)*d2)
            T0,T1=T1,T2;d0,d1=d1,d2
    return mp.fsum(values),mp.fsum(derivatives)


def q_density_modes(model,r):
    s,w=model.density.coords(r);t=2*s-1 if s<mp.mpf('.5')else 1-2*w
    pairs=[polynomial_and_derivative(row,t)for row in model.coeff]+[(mp.mpf(0),mp.mpf(0))]
    sd=2*s*w/(w+2*model.kappa*s);g=[];e=[]
    for j in range(model.M):
        B,Bt=pairs[j];C,Ct=pairs[j+1]
        D=B-s*C/2 if j==0 else (B-s*C)/2
        Ds=2*Bt-C/2-s*Ct if j==0 else Bt-C/2-s*Ct
        gg=w*s**j*D
        derivative=-s**j*D+w*s**j*Ds
        if j:derivative+=w*j*s**(j-1)*D
        g.append(gg);e.append(gg+sd*derivative)
    return g,e


def q_modes(model,r):
    g,e=q_density_modes(model,r);p,d=model.coefficients(r)
    return g,e,[-2*j*v for j,v in enumerate(p,1)],d


def smooth_density_modes(model,r):
    r=number(r);L=number(model.L);alpha=number(model.alpha);z=(r/L)**2
    om=1/(1+z);s=z*om;w=mp.exp(-alpha*mp.log1p(z));t=1-2*w
    pairs=[polynomial_and_derivative(row,t)for row in model.coeff]+[(mp.mpf(0),mp.mpf(0))]
    sd=2*s*om;td=4*alpha*s*w;g=[];e=[]
    for j in range(model.M):
        B,Bt=pairs[j];C,Ct=pairs[j+1]
        D=B-s*C/2 if j==0 else (B-s*C)/2
        Dd=Bt*td-(sd*C+s*Ct*td)/2 if j==0 else (Bt*td-sd*C-s*Ct*td)/2
        gg=w*s**j*D;ee=(1-2*alpha*s)*gg+w*s**j*Dd
        if j:ee+=w*j*s**(j-1)*sd*D
        g.append(gg);e.append(ee)
    return g,e


def smooth_modes(model,r):
    g,e=smooth_density_modes(model,r);pq=model.modal_integrals(r)
    return g,e,[-(p+q)/2 for p,q in pq],[(-p+q)/2 for p,q in pq]


def convolve(ell,g,e,u,v):
    assert len(g)==len(e)and len(u)==len(v)
    out=[ell*0 for unused in range(len(g)+len(u))]
    for i,(gg,ee) in enumerate(zip(g,e)):
        k=2*i+1;out[i]+=ell*ee-gg
        for j,(uu,vv)in enumerate(zip(u,v),1):
            m=2*j;aa=uu*ee/2;bb=vv*k*gg/2
            out[i+j]+=aa+bb
            difference=k-m;out[(abs(difference)-1)//2]+=(1 if difference>0 else -1)*(aa-bb)
    return out


def direct_angular_residual(ell,g,e,u,v,theta):
    rho=mp.fsum(gg*mp.sin((2*i+1)*theta)for i,gg in enumerate(g))
    radial=mp.fsum(ee*mp.sin((2*i+1)*theta)for i,ee in enumerate(e))
    angular=mp.fsum((2*i+1)*gg*mp.cos((2*i+1)*theta)for i,gg in enumerate(g))
    ur=mp.fsum(uu*mp.cos(2*j*theta)for j,uu in enumerate(u,1))
    ut=mp.fsum(vv*mp.sin(2*j*theta)for j,vv in enumerate(v,1))
    return ell*radial-rho+ur*radial+ut*angular


def diagnostic(ell,r,rows,digits=75):
    r=number(r);g,e,u,v=rows;c=convolve(ell,g,e,u,v)
    densitysquare=mp.fsum(vv*vv for vv in g);residualsquare=mp.fsum(vv*vv for vv in c)
    values=dict(radius=r,R1_projection=mp.pi*r*c[0],R3_projection=mp.pi*r*c[1]if len(c)>1 else mp.mpf(0),angular_R_L2=mp.sqrt(mp.pi)*r*mp.sqrt(residualsquare),angular_rho_L2=mp.sqrt(mp.pi)*r*mp.sqrt(densitysquare),R_to_rho_angular_L2=mp.sqrt(residualsquare/densitysquare)if densitysquare else None,estimated_angular_abs_envelope=r*mp.fsum(abs(vv)for vv in c))
    out={k:mp.nstr(v,digits)if v is not None else None for k,v in values.items()}
    out['R_over_r_sine_coefficients']=[mp.nstr(v,digits)for v in c]
    out['rho_over_r_sine_coefficients']=[mp.nstr(v,digits)for v in g]
    return out
