"""Independent physical Cartesian evaluation using raw scalar differentiation."""
from core_generating_mp import from_data,number
from raw_generating_mp import differentiate,fields
import mpmath as mp

def inverse(G,x,y,s):
    if y==0:return mp.mpf(0),{'iterations':0,'scaled_equation_defect':'0','bracket_doublings':0}
    sign=1 if y>0 else -1;Y=abs(y);lo=mp.mpf(0);hi=max(mp.mpf(1),2*s*mp.root(Y,3));nd=0
    def f(e):return differentiate(G,x,e,1,0)
    while f(hi)<Y:
        hi*=2;nd+=1
        if nd>200:raise ArithmeticError('failed to bracket chart')
    A0=differentiate(G,x,mp.mpf(0),1,1)
    if A0<=0:raise ArithmeticError('nonpositive axis chart')
    e=min(Y/A0,(lo+hi)/2);tol=mp.power(10,-mp.mp.dps+25)
    for it in range(180):
        val=f(e)-Y;err=abs(val)/(1+Y)
        if err<tol:
            return sign*e,{'iterations':it+1,'scaled_equation_defect':mp.nstr(err,mp.mp.dps),'bracket_doublings':nd}
        if val<0:lo=e
        else:hi=e
        A=differentiate(G,x,e,1,1)
        if A<=0:raise ArithmeticError('nonpositive chart on iteration')
        trial=e-val/A
        e=trial if lo<trial<hi else (lo+hi)/2
    raise ArithmeticError(('physical inverse convergence',mp.nstr(x),mp.nstr(y),mp.nstr(err)))

def evaluate(G,a,s,x,y):
    e,diag=inverse(G,x,y,s);r,*_=fields(G,a,x,e)
    r['requested_y']=y;r['physical_location_defect']=r['y']-y
    r['Psi']=3*x*differentiate(G,x,e,1,0)+e*differentiate(G,x,e,0,1)-6*G(x,e)
    TT=[(3*x+r['U1'])*r['Theta_x'],(3*r['y']+r['U2'])*r['Theta_y'],-r['Theta']]
    if y:
        DT=[v/r['y'] for v in TT]
    else:
        DT=[(3*x+r['U1'])*r['Theta_xy'],(3+r['c'])*r['Theta_y'],-r['Theta_y']]
    r.update(R_Theta=sum(TT),N_Theta=sum(map(abs,TT)),D_Theta=sum(DT),ND_Theta=sum(map(abs,DT)))
    for key,den in [('R_Theta','N_Theta'),('D_Theta','ND_Theta')]:r[key+'_ratio']=abs(r[key])/r[den] if r[den] else None
    return r,diag

def serialize(r):
    if isinstance(r,dict):return {k:serialize(v) for k,v in r.items()}
    if isinstance(r,(list,tuple)):return [serialize(v) for v in r]
    if isinstance(r,mp.mpf):return mp.nstr(r,mp.mp.dps)
    return r
