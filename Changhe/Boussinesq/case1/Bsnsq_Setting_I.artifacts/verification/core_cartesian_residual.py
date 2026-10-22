"""Own safeguarded physical chart inversion and scalar eighth-order differences."""
from fractions import Fraction
import numpy as np
from core_quadrature_fields import FullCoreModel,core_derivatives,LD

class CorePhysicalModel(FullCoreModel):
    def mixed(self,x,e):
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            z=self.outer.mixed(x,e)
            g=core_derivatives(x,e,self.patches,self.se)
            z['y']=z['y']+g[1,0];z['A']=z['A']+g[1,1]
            z['B0']=z['B0']+g[2,0]
            if np.any(z['A']<=0) or any(np.any(~np.isfinite(z[k])) for k in ['y','A','B0']):
                raise ArithmeticError('bad full chart inverse query')
            return {k:z[k] for k in ['y','A','B0']}

    def invert(self,x,y,tol=LD('2e-17'),maxiter=90):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(y,dtype=LD))
        shape=x.shape;xx=abs(x.ravel());target=abs(y.ravel());sign=np.sign(y.ravel())
        active=target>0
        lo=np.zeros_like(target);hi=np.maximum(LD(1),2*np.cbrt(target))
        for _ in range(40):
            z=self.mixed(xx,hi);okay=z['y']>=target
            if np.all(okay):break
            hi[~okay]*=2
        else:raise ArithmeticError('could not bracket full chart inverse')
        azero=self.mixed(xx,np.zeros_like(xx))['A']
        e=np.minimum(target/azero,hi/2);e[~active]=0
        for iteration in range(maxiter):
            z=self.mixed(xx,e);error=z['y']-target
            relative=np.zeros_like(target);relative[active]=abs(error[active])/target[active]
            good=(relative<=tol)&(active|(error==0))
            if np.all(good):break
            lo=np.where(error<0,e,lo);hi=np.where(error>=0,e,hi)
            trial=e-error/z['A'];trial=np.where((trial>lo)&(trial<hi),trial,(lo+hi)/2)
            e=np.where(good,e,trial)
        else:raise ArithmeticError('full inverse relative tolerance not reached: '+str(np.max(relative)))
        return (e*sign).reshape(shape),{'iterations':iteration+1,'max_nonzero_relative_y_defect':str(np.max(relative)),
                                     'max_absolute_y_defect':str(np.max(abs(error))),'zero_y_count':int(np.sum(~active))}

    def divided_omega(self,x,e):
        x,e=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(e,dtype=LD))
        if np.any(x==0) or np.any(e==0):raise ValueError('use separate analytic axis limits')
        z=self.mixed_vorticity(x,e)
        return z['Omega']/(x*e)

WEIGHTS=[LD(4)/5,-LD(1)/5,LD(4)/105,-LD(1)/280]
def difference(fun,x,e,h,axis):
    out=np.zeros(np.broadcast_shapes(np.shape(x),np.shape(e)),dtype=LD)
    for j,w in enumerate(WEIGHTS,1):
        if axis==0:v=fun(x+j*h,e)-fun(x-j*h,e)
        else:v=fun(x,e+j*h)-fun(x,e-j*h)
        out+=w*v
    return out/h

def ratio(numerator,denominator):
    if np.any(denominator<0):raise ArithmeticError('negative normalizer')
    z=np.full(np.shape(denominator),np.nan,dtype=LD);good=denominator>0
    np.divide(abs(numerator),denominator,out=z,where=good)
    return z

def residual(model,x,e,factor=LD('0.0003')):
    x,e=np.broadcast_arrays(np.asarray(x,dtype=LD),np.asarray(e,dtype=LD))
    if np.any(x==0) or np.any(e==0):raise ValueError('nonzero coordinates required by divided evaluator')
    z=model.mixed_vorticity(x,e);y=z['y'];A=z['A'];B=z['B']
    f=z['Omega']/(x*e)
    hx=factor*np.maximum(abs(x),LD('0.02'));he=factor*np.maximum(abs(e),LD('0.02'))
    fx=difference(model.divided_omega,x,e,hx,0);fe=difference(model.divided_omega,x,e,he,1)
    oxe=e*f+x*e*fx;oe=x*f+x*e*fe
    ox=oxe-B/A*oe;oy=oe/A
    w1=3*x+z['U1'];w2=3*y+z['U2']
    terms=[w1*ox,w2*oy,z['Omega'],-z['Theta_x']]
    groups=[z['U1']*ox,z['U2']*oy,3*x*ox+3*y*oy+z['Omega'],-z['Theta_x']]
    R=sum(terms);N=sum(abs(q) for q in terms);N2=sum(abs(q) for q in groups)
    Dm=(w1/x+2)*f+w1*fx+e*fe-z['Theta_x']/(x*e)
    D=Dm*e/y;xy=x*y
    rt=w1*z['Theta_x']+w2*z['Theta_y']-z['Theta']
    nt=abs(w1*z['Theta_x'])+abs(w2*z['Theta_y'])+abs(z['Theta'])
    result={k:z[k] for k in ['x','eta','y','A','B','Omega','Psi','U1','U2','Theta','Theta_x','Theta_y']}
    result.update(Omega_x=ox,Omega_y=oy,R=R,N=N,N2=N2,q=ratio(R,N),q2=ratio(R,N2),
                  D=D,ND=N/abs(xy),ND2=N2/abs(xy),q_divided=ratio(D,N/abs(xy)),q2_divided=ratio(D,N2/abs(xy)),
                  temperature_R=rt,temperature_N=nt,temperature_q=ratio(rt,nt),
                  divided_consistency=abs(R-xy*D),grouped_consistency=abs(R-sum(groups)),hx=hx,he=he)
    for i,q in enumerate(terms):result['term'+str(i+1)]=q
    for i,q in enumerate(groups):result['group'+str(i+1)]=q
    if any(np.any(~np.isfinite(v)) for k,v in result.items() if k not in ['q','q2','q_divided','q2_divided','temperature_q']):
        raise ArithmeticError('nonfinite residual term')
    return result
