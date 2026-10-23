"""Exact finite-operand residual arithmetic, including undefined ratios."""
from fractions import Fraction as F

def exact(v):
    return v if isinstance(v,F)else F(float(v))

def residual(jet,velocity,c,x,y):
    g,gx,gy=map(exact,jet[:3]);v1,v2=map(exact,velocity);c,x,y=map(exact,[c,x,y])
    a=(c*x+v1)*gx;b=(c*y+v2)*gy;r=a+b-g
    nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy)
    return dict(R=r,Nf=nf,Nv=nv,Rf=abs(r)/nf if nf else None,Rv=abs(r)/nv if nv else None)

def decomposition(jet,producer_jet,velocity,map_velocity,c,x,y):
    g,gx,gy=map(exact,jet[:3]);gp,gpx,gpy=map(exact,producer_jet[:3]);v1,v2=map(exact,velocity);m1,m2=map(exact,map_velocity);c,x,y=map(exact,[c,x,y])
    a=residual(jet,velocity,c,x,y);b=residual(producer_jet,map_velocity,c,x,y)
    dv=(v1-m1)*gx+(v2-m2)*gy
    dj=(c*x+m1)*(gx-gpx)+(c*y+m2)*(gy-gpy)-(g-gp)
    return dict(R_reference=a['R'],R_producer=b['R'],velocity_term=dv,jet_term=dj,difference=a['R']-b['R'],identity=a['R']-b['R']==dv+dj)
