"""Independent exact horizontal-slice/layer-cake reduction of the polygonal witness.
mpmath functions are exploratory. The separate Arb driver certifies finite integrals.
"""
import mpmath as mp

def line_primitive(y, slope, intercept):
    aa = 1+slope*slope
    def one(b):
        dd=(slope*y+b)**2+y*y
        # All uses below have positive imaginary argument on the active interval.
        return (mp.log(dd)/2-slope*mp.arg(mp.mpc(b,aa*y+slope*b)))/aa
    return (one(intercept)-one(intercept-1))/(2*mp.pi)

def circle_primitive(theta, t, a):
    zz=mp.exp(1j*theta)
    def one(q):
        center=mp.mpc(q,a); cb=mp.conj(center)
        return mp.log(abs(center+t*zz))/2-mp.re((t/cb)*zz-(t*t/(cb*cb))*mp.log(cb*zz+t))/2
    return (one(0)-one(-1))/(2*mp.pi)

def level(t,a):
    rt=mp.sqrt(3)
    switch=a+(rt-2)*t
    # Right positive component; the left one has the same integral.
    pos=mp.mpf(0)
    if switch>t:
        pos-=line_primitive(switch,0,1+t)-line_primitive(t,0,1+t)
    low=max(t,switch)
    pos+=line_primitive(low,1/rt,1+(2*t-a)/rt)
    # Central negative component, after reversing the sign of its density.
    neg=mp.mpf(0)
    if t<a and t<mp.mpf('.5'):
        neg+=line_primitive(a,0,t)-line_primitive(t,0,t)
    theta1=mp.pi/6
    if t<2*a and t<1/rt:
        theta0=max(mp.asin(max(mp.mpf(0),1-a/t)),mp.acos(min(mp.mpf(1),1/(2*t))))
        theta0=min(theta0,theta1)
        neg+=circle_primitive(theta1,t,a)-circle_primitive(theta0,t,a)
    low=max(t,a+t/2,a+2*t-rt/2)
    neg-=line_primitive(low,-1/rt,(2*t+a)/rt)
    return 4*(pos+neg)

def exploratory_integral(alpha,a):
    k=2**(alpha-1)*alpha
    # Logarithmic quadrature with explicit branch locations, finite tails omitted.
    cuts=[mp.mpf(-80),-10,-3,-1,0,2,5,10,20,40,80]
    cuts += [mp.log(x) for x in [a,mp.mpf('.5'),2*a,1/mp.sqrt(3),a/(3-mp.sqrt(3))] if x>0]
    cuts=sorted(set(cuts))
    return k*sum(mp.quad(lambda s:mp.exp(alpha*s)*level(mp.exp(s),a),[lo,hi]) for lo,hi in zip(cuts[:-1],cuts[1:]))

if __name__=='__main__':
    import json
    from pathlib import Path
    from datetime import datetime, timezone
    mp.mp.dps=50
    a=mp.mpf('.5')
    checks=[]
    for t in [mp.mpf('.01'),mp.mpf('.2'),mp.mpf('.5'),mp.mpf('2')]:
        theta=mp.mpf('.2')
        x=t*mp.cos(theta);y=a+t*mp.sin(theta)
        target=y/(2*mp.pi)*(1/(x*x+y*y)-1/((x-1)**2+y*y))*t*mp.cos(theta)
        got=mp.diff(lambda th:circle_primitive(th,t,a),theta)
        checks.append(dict(t=str(t),circle_derivative_error=str(got-target)))
    levels=[dict(t=str(t),J=str(level(t,a)),J_regularized=str(level(t,a)+4/mp.pi*mp.log(t)),tJ=str(t*level(t,a))) for t in map(mp.mpf,['1e-12','.001','.1','.5','1','10','10000','1e12'])]
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),scope='Exploratory mpmath; not a certificate',circle_checks=checks,levels=levels,I_half=str(exploratory_integral(mp.mpf('.5'),a)))
    Path('data/structured_layercake_exploration.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
