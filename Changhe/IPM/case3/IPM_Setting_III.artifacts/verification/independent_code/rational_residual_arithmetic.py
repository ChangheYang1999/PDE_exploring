"""Exact fraction comparisons for stored finite residuals, result287."""
from fractions import Fraction as F
import math
EPS=F(1,2**52)
FACTOR=1024*EPS

def frac(x):
    if isinstance(x,F):return x
    if isinstance(x,int):return F(x)
    x=float(x)
    if not math.isfinite(x):raise ValueError('nonfinite input')
    return F.from_float(x)

def exact(x,y,c,jet,velocity):
    x,y,c=map(frac,(x,y,c));g,gx,gy=map(frac,jet[:3]);u,v=map(frac,velocity)
    if not c>1:raise ValueError('c must exceed one')
    wx,wy=c*x+u,c*y+v;a,b=wx*gx,wy*gy
    R=a+b-g;nf=abs(a)+abs(b)+abs(g)
    nv=abs(g)+abs(x*gx+y*gy)+abs(u*gx+v*gy)
    T=abs(c*x*gx)+abs(u*gx)+abs(c*y*gy)+abs(v*gy)+abs(g)
    S=abs(g)+abs(x*gx)+abs(y*gy)+abs(u*gx)+abs(v*gy)
    B=(abs(c*x)+abs(u)+abs(c*y)+abs(v))*(abs(gx)+abs(gy))+abs(g)
    Q=(wx*wx+wy*wy)*(gx*gx+gy*gy)
    return dict(x=x,y=y,c=c,g=g,gx=gx,gy=gy,u=u,v=v,W=[wx,wy],parts=[a,b],Rh=R,Nf=nf,Nv=nv,Q=Q,T=T,S=S,B=B,
                Wscale=[abs(c*x)+abs(u),abs(c*y)+abs(v)],partscale=[abs(c*x*gx)+abs(u*gx),abs(c*y*gy)+abs(v*gy)])

def inspect(x,y,c,jet,velocity,stored,require_wp=True):
    required={'Rh','Nf','Nv','Nbound','Rf','Rv','Rbound'}
    if require_wp:required|={'W','parts'}
    missing=required-set(stored)
    if missing:raise ValueError('missing fields '+','.join(sorted(missing)))
    z=exact(x,y,c,jet,velocity);scores={};conditions={};categories={}
    def condition(name,b,category='stored_data'):
        conditions[name]=bool(b);categories[name]=category
    def compare(name,got,want,scale):
        err=abs(frac(got)-want);budget=FACTOR*scale
        condition(name,err<=budget);scores[name]=float(err/budget) if budget else (0.0 if not err else math.inf)
    condition('exact triangle Nf',abs(z['Rh'])<=z['Nf'],'identity')
    condition('exact triangle Nv',abs(z['Rh'])<=z['c']*z['Nv'],'identity')
    condition('exact Cauchy square',(z['Nf']-abs(z['g']))**2<=z['Q'],'identity')
    for key,scale in [('Rh',z['T']),('Nf',z['T']),('Nv',z['S'])]:compare(key,stored[key],z[key],scale)
    for key,sk in [('W','Wscale'),('parts','partscale')]:
        if key in stored:
            for j in range(2):compare(key+str(j),stored[key][j],z[key][j],z[sk][j])
    n=frac(stored['Nbound']);E=FACTOR*z['B'];h=n-abs(z['g'])
    condition('Nbound nonnegative',n>=0)
    condition('Nbound squared enclosure',h+E>=0 and max(h-E,F(0))**2<=z['Q']<=(h+E)**2)
    for ratio,den,scale in [('Rf','Nf',z['T']),('Rv','Nv',z['S']),('Rbound','Nbound',z['B'])]:
        d=z[den] if den!='Nbound' else n
        val=stored[ratio];undefined=val is None or math.isnan(float(val))
        if d==0:
            condition(ratio+' zero denominator',z['Rh']==0 and undefined)
            scores[ratio]=0.0
        else:
            condition(ratio+' positive denominator',d>0,'stored_data' if den=='Nbound' else 'identity')
            condition(ratio+' defined',not undefined)
            if not undefined:
                v=frac(val);condition(ratio+' nonnegative',v>=0)
                error=abs(v*d-abs(z['Rh']));budget=FACTOR*(z['T']+abs(v)*scale)
                condition(ratio+' arithmetic',error<=budget)
                scores[ratio]=float(error/budget) if budget else (0.0 if not error else math.inf)
    if z['y']==0:
        condition('horizontal parity',z['g']==z['gx']==z['v']==0,'parity')
        condition('horizontal exact zero',z['Rh']==z['Nf']==z['Nv']==0,'identity')
    return dict(passed=all(conditions.values()),conditions=conditions,categories=categories,scores=scores,zero_denominators={k:(z[k]==0 if k!='Nbound' else n==0)for k in ['Nf','Nv','Nbound']})


def json_safe(value):
    """Keep failure diagnostics serializable, including a zero-budget violation."""
    if isinstance(value,float) and not math.isfinite(value):return repr(value)
    if isinstance(value,dict):return {k:json_safe(v)for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [json_safe(v)for v in value]
    return value


def point_matches(index,point):
    """Independent formula for the reporting index and physical coordinate."""
    if index not in range(333) or len(point)!=4:return False
    x,y,r,j=map(float,point)
    if not all(math.isfinite(t)for t in (x,y,r,j)):return False
    ring,angle=divmod(index,9);rr=10.0**(-3+ring/4);theta=angle*math.pi/16
    xx=0. if angle==8 else rr*math.cos(theta)
    yy=0. if angle==0 else rr*math.sin(theta)
    return j==angle and all(abs(a-b)<=64*float(EPS)*rr for a,b in [(x,xx),(y,yy),(r,rr)]) and (angle!=0 or y==0.) and (angle!=8 or x==0.)
