"""Exploratory double-precision shape search. Never a numerical certificate."""
import math, cmath, json, time
from pathlib import Path
from datetime import datetime,timezone
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
P=math.pi; R=math.sqrt(3)

def line(y,m,b):
    x=m*y+b; d=(x-1)**2+y*y
    q=(2*x-1)/d
    logratio=math.log1p(q) if abs(q)<.5 else math.log(x*x+y*y)-math.log(d)
    return (.5*logratio+m*cmath.phase(complex(y*y+x*(x-1),y)))/(2*P*(1+m*m))

def circle(th,t,a):
    z=cmath.exp(1j*th)
    def one(q):
        w=complex(q,a);wb=w.conjugate()
        return .5*math.log(abs(w+t*z))-.5*((t/wb)*z-t*t/(wb*wb)*cmath.log(wb*z+t)).real
    return (one(0)-one(-1))/(2*P)

def level(t,a):
    h=max(t,a+(R-2)*t)
    pos=line(t,0,1+t)-line(h,0,1+t)+line(h,1/R,1+(2*t-a)/R)
    neg=0.
    if t<min(a,.5):neg+=line(a,0,t)-line(t,0,t)
    if t<min(2*a,1/R):
        lo=min(P/6,max(math.asin(max(0.,1-a/t)),math.atan(math.sqrt(max(4*t*t-1,0.)))))
        neg+=circle(P/6,t,a)-circle(lo,t,a)
    h=max(t,a+t/2,a+2*t-R/2)
    neg-=line(h,-1/R,(2*t+a)/R)
    return 4*(pos+neg)

def value(alpha,a,limit=24):
    cuts=[-limit,limit]
    cuts += [math.log(t) for t in (a,.5,2*a,1/R,a/(3-R),R/2-a,(a*a+.25)/(2*a)) if t>0 and -limit<math.log(t)<limit]
    cuts=sorted(set(cuts)); mid=0; err=0
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        v,e=quad(lambda s:math.exp(alpha*s)*level(math.exp(s),a),lo,hi,epsabs=1e-10,epsrel=1e-10,limit=100)
        mid+=v;err+=e
    j0=(R*math.atan(1/a)-.5*math.log1p(1/a**2)-2*math.log(2))/P
    near=math.exp(-alpha*limit)*(4/P*(1/alpha+limit)+j0)
    far=alpha*3*R/(4*P)*math.exp(-(1-alpha)*limit)/(1-alpha)
    return 2**(alpha-1)*(near+alpha*mid+far),err

def main():
    rows=[];start=time.monotonic()
    for alpha in [.001,.01,.05,.1,.2,.3,.4,.5,.6,.7,.75,.8,.9,.95,.99]:
        opt=minimize_scalar(lambda a:-value(alpha,a)[0],bounds=(.02,1.2),method='bounded',options={'xatol':2e-6})
        a=round(float(opt.x),3); v,err=value(alpha,a);check,_=value(alpha,a,20)
        row=dict(alpha=alpha,shape_a=a,exploratory_value=v,quad_error_estimate=err,cutoff_check_difference=v-check,raw_optimizer_a=float(opt.x))
        rows.append(row);print(row,flush=True)
    out=dict(time_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),status='Exploratory floating-point search, not a proof or certificate.',rows=rows,elapsed_seconds=time.monotonic()-start)
    Path('data/structured_shape_exploration.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
