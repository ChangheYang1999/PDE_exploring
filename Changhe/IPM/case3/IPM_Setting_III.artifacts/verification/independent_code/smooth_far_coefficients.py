"""Exact-formula far coefficients; proof is result85."""
import mpmath as mp
from fractions import Fraction as F
from smooth_mp_primitives import number

def coefficients(model,theta):
    theta=number(theta);si=mp.sin(theta);cs=mp.cos(theta)
    alpha=number(model.alpha);L=number(model.L);p=number(model.p);ell=number(model.ell)
    def C(k,l):return model.C[k][l]if 0<=k<model.M and l<len(model.C[k])else F(0)
    sums=[]
    for l in range(2):sums.append(mp.fsum(number(C(k,l))*mp.cos(2*k*theta)for k in range(model.M)))
    derivative=mp.fsum(-2*k*number(C(k,0))*mp.sin(2*k*theta)for k in range(model.M))
    t0=L**(2*alpha)*si*sums[0];t1=L**(4*alpha)*si*sums[1]
    dt0=L**(2*alpha)*(cs*sums[0]+si*derivative)
    modes=[]
    for j in range(1,model.M+1):
        s=j*C(j,0)-(F(1)if j==1 else F(1,2))*(model.alpha+j-1)*C(j-1,0)+(model.alpha-j-1)*C(j+1,0)/2
        modes.append(L**(2*alpha)*number(s)/(4*j*j-(p+1)**2))
    vr=mp.fsum(-2*j*b*mp.cos(2*j*theta)for j,b in enumerate(modes,1))
    vt=mp.fsum((p+1)*b*mp.sin(2*j*theta)for j,b in enumerate(modes,1))
    e1=(ell*(2*p-1)-1)*t1+p*vr*t0+vt*dt0
    gx=p*cs*t0-si*dt0;gy=p*si*t0+cs*dt0
    nf=ell*(abs(cs*gx)+abs(si*gy))+abs(t0);nv=(1+p)*abs(t0)
    defect=number(model.ell*model.p-1)
    return dict(Theta0=t0,Theta1=t1,Theta0_prime=dt0,V_r=vr,V_theta=vt,E1=e1,leading_defect=defect,Nf_coefficient=nf,Nv_coefficient=nv,R_Nf_limit=abs(defect*t0)/nf if nf else None,R_Nv_limit=abs(defect*t0)/nv if nv else None,source_coefficients=[(4*j*j-(p+1)**2)*b for j,b in enumerate(modes,1)])

def at_point(model,x,y):
    x=number(x);y=number(y);r=mp.hypot(x,y)
    if not r:return None
    p=number(model.p);v=coefficients(model,mp.atan2(y,x));v.pop('source_coefficients')
    v['R_leading_term']=v['leading_defect']*r**p*v['Theta0']
    v['R_second_term']=r**(2*p-1)*v['E1']
    v['R_two_terms']=v['R_leading_term']+v['R_second_term']
    return {k:mp.nstr(a,model.digits)if a is not None else None for k,a in v.items()}
