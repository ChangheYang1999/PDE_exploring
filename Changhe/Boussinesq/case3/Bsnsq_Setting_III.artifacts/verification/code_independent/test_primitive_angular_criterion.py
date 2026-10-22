"""Independent arbitrary-precision controls for packet129; no solver code."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import mpmath as mp

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True)
tic=time.perf_counter();mp.mp.dps=55;records=[]

def source(kind,m,u,sigma):
    r2=1+u*u
    if kind=='cusp':return u*r2**((m-2)/2)
    if kind=='compatible':return 2*u*r2**((m-2)/2)+(m-2)*u**3*r2**((m-4)/2)
    if kind=='asymmetric':return sigma*u*r2**((m-3)/2)
    if kind=='odd_compatible':return sigma*(2*u*r2**((m-3)/2)+(m-3)*u**3*r2**((m-5)/2))
    raise ValueError(kind)

def radial_difference(kind,m,t,sigma):
    l=mp.log1p(t*t)
    if kind=='cusp':return mp.expm1((m-2)*l/2)
    if kind=='compatible':return m*mp.expm1((m-4)*l/2)+2*t*t*mp.exp((m-4)*l/2)
    if kind=='asymmetric':return sigma*t*mp.exp((m-3)*l/2)
    if kind=='odd_compatible':return sigma*t*((m-1)+2*t*t)*mp.exp((m-5)*l/2)

def radial(kind,m,sigma):
    a=1 if kind=='cusp'else m if kind=='compatible'else 0
    def tail(v):
        if not v:return mp.mpf(0)
        t=v**20
        return 20*v**19*t**(-1-m)*radial_difference(kind,m,t,sigma)
    return mp.quad(lambda u:source(kind,m,u,sigma),[0,1])-a/m+mp.quad(tail,[0,mp.mpf('.5'),1])

def angular(kind,m,sigma):
    def integrand(v):
        if v==0 or v==1:return mp.mpf(0)
        A=v**20;B=(1-v)**20;den=A+B
        theta=mp.pi*A/(2*den);complement=mp.pi*B/(2*den)
        sn,cs=(mp.sin(theta),mp.cos(theta))if v<=mp.mpf('.5')else(mp.cos(complement),mp.sin(complement))
        # Stable logarithm preserves the subtraction at the horizontal endpoint.
        lc=mp.log1p(-sn*sn)/2 if v<mp.mpf('.4')else mp.log(cs)
        if kind=='cusp':bracket=cs**(m-1)*mp.expm1((2-m)*lc)
        elif kind=='compatible':bracket=cs**(m-1)*(2*mp.expm1((2-m)*lc)+(m-2)*mp.expm1((4-m)*lc))
        elif kind=='asymmetric':bracket=sigma*cs*sn
        else:bracket=sigma*sn*(2*cs+(m-3)*cs**3)
        jac=10*mp.pi*v**19*(1-v)**19/den**2
        return bracket*sn**(-1-m)*jac
    return mp.quad(integrand,[0,mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1])

for ratio in ['1/10','1/3','3/4','9/10']:
    num,den=map(int,ratio.split('/'));m=mp.mpf(num)/den
    for kind in ['cusp','compatible','asymmetric','odd_compatible']:
        for sigma in [-1,1]:
            truth=-1/m if kind=='cusp'else sigma/(1-m)if kind=='asymmetric'else mp.mpf(0)
            r=radial(kind,m,sigma);a=angular(kind,m,sigma);err=max(abs(r-truth),abs(a-truth),abs(r-a))
            assert err<mp.mpf('1e-38'),(ratio,kind,sigma,err)
            records.append({'m':ratio,'kind':kind,'sigma':sigma,'exact':mp.nstr(truth,50),'radial':mp.nstr(r,50),'angular':mp.nstr(a,50),'max_error':mp.nstr(err,10)})
# One-sided cancellation: cusp + asymmetric/3, m=3/4.
m=mp.mpf(3)/4
one=[radial('cusp',m,k)+radial('asymmetric',m,k)/3 for k in [1,-1]]
assert abs(one[0])<mp.mpf('1e-40')and abs(one[1]+mp.mpf(8)/3)<mp.mpf('1e-40')
# A globally smooth pair has a nonsmooth homogeneous limit. Evaluate directly,
# including the divergent difference quotient and fixed-point scaling limit.
examples=[]
for m in [mp.mpf(1)/3,mp.mpf(3)/4]:
    target=((1+mp.mpf('.4')**2)**(m/2)-mp.mpf('.4')**m)/m
    errors=[]
    for lam in [10,1000,1000000]:
        val=((lam**-2+1+mp.mpf('.4')**2)**(m/2)-(lam**-2+mp.mpf('.4')**2)**(m/2))/m
        errors.append(abs(val-target))
    assert errors[2]<errors[1]<errors[0]
    quotients=[]
    for y in [mp.mpf('1e-3'),mp.mpf('1e-6'),mp.mpf('1e-9')]:
        T=((1+y*y)**(m/2)-y**m)/m
        quotients.append((T-1/m)/y)
    assert abs(quotients[2])>abs(quotients[1])>abs(quotients[0])
    examples.append({'m':str(m),'scaling_errors':list(map(str,errors)),'one_sided_quotients':list(map(str,quotients))})
result={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'precision_decimal_digits':mp.mp.dps,'constants':records,'one_sided_constants':list(map(str,one)),'smooth_regularization_examples':examples,'scope':'Manufactured numerical controls, not rigorous quadrature enclosures and not B2 profiles.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['elapsed_seconds'],len(records),flush=True)
