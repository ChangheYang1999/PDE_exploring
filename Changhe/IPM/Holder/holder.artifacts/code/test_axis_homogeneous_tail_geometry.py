"""Independent floating attempts to break the signed-distance and branch bounds.

These tests are diagnostics. The all-point statements are proved separately.
"""
import math,random,json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def segment(p,a,b):
    vx,vy=b[0]-a[0],b[1]-a[1]
    t=max(0.,min(1.,((p[0]-a[0])*vx+(p[1]-a[1])*vy)/(vx*vx+vy*vy)))
    return math.hypot(p[0]-a[0]-t*vx,p[1]-a[1]-t*vy)
def ray(p,a,u):
    t=max(0.,(p[0]-a[0])*u[0]+(p[1]-a[1])*u[1])
    return math.hypot(p[0]-a[0]-t*u[0],p[1]-a[1]-t*u[1])
def signed_distance0(X,Y,b):
    # Independent geometry using the right-hand pieces plus the midline.
    segs=[((.5,0),(0,.5)),((.5,0),(0,-.5)),((.5,0),(.5+b,b)),((.5,0),(.5+b,-b))]
    ds=[X]+[segment((X,Y),v,w) for v,w in segs]
    ds+=[ray((X,Y),(.5+b,s*b),(math.sqrt(3)/2,s/2)) for s in [-1,1]]
    t=X-.5;height=abs(t) if t<=b else b+(t-b)/math.sqrt(3)
    return math.copysign(min(ds),height-abs(Y))
def signed_infinity(X,Y):
    ds=[X,ray((X,Y),(0,0),(math.sqrt(3)/2,.5)),ray((X,Y),(0,0),(math.sqrt(3)/2,-.5))]
    return math.copysign(min(ds),X/math.sqrt(3)-abs(Y))
def sp(v,a):return math.copysign(abs(v)**a,v)
def P(X,Y,a):
    r=math.hypot(X,Y)
    return 0. if r==0 else .5*(r**a+sp((X*X-Y*Y)/r,a))
def main():
    rng=random.Random(202610280906);rows=[]
    cases=[(.9,.35,-.3,10/11),(.75,.75,-.3,50/53),(.5,.75,-.15,1000/1021),(.3,1.5,0.,1000/1007)]
    for a,b,c,lam in cases:
        H=math.hypot(b+.5,b);B=max(H**a+abs(c),.5+2**(-a));maxsigned=0.;maxwitness=0.;worst=None
        for i in range(20000):
            if i%3==0:
                X=10**rng.uniform(-5,5); Y=X/math.sqrt(3)+rng.uniform(-1,1)*H
            else:
                r=10**rng.uniform(-7,8);theta=rng.uniform(-math.pi/2,math.pi/2)
                X=r*math.cos(theta);Y=r*math.sin(theta)
            s0=signed_distance0(X,Y,b);si=signed_infinity(X,Y)
            gs=2**(a-1)*sp(s0,a);gi=2**(a-1)*sp(si,a)
            h=2**(a-1)*X**a;f=max(-h,min(h,gs+c,-.5+lam*P(X-.5,Y,a)))
            rs=abs(s0-si)/H;rf=abs(f-gi)/B
            maxsigned=max(maxsigned,rs)
            if rf>maxwitness:maxwitness=rf;worst=[X,Y]
        assert maxsigned<=1+1e-8 and maxwitness<=1+1e-8
        rows.append(dict(alpha=a,b=b,samples=20000,max_signed_distance_ratio=maxsigned,max_witness_error_ratio=maxwitness,worst=worst))
    rec=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='DIAGNOSTIC ONLY, not a proof',rows=rows)
    out=ROOT/'05_team_audit/note14_certificate/homogeneous_tail/verification/geometry_diagnostic.json'
    out.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
if __name__=='__main__':main()
