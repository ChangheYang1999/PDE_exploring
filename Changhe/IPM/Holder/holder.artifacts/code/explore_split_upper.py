"""Exploratory upper-plan integrals. Floating calculations are not certificates."""
import numpy as np
from scipy.integrate import quad
from math import pi,sin,cos,sqrt,acos,log
from pathlib import Path
import json

def an(alpha,n):
    return n/pi*quad(lambda t:sin(n*t)*(2*sin(t))**alpha,0,pi/(2*n),epsabs=1e-11)[0]

def far(alpha,R,terms=50):
    return sum(2*(n+1)*.25**n*an(alpha,2*n+3)*R**(alpha-2*n-1)/(2*n+1-alpha) for n in range(terms))

def mid(alpha,beta,R,rho=.5):
    def funr(r):
        if r==0:return 0.
        v=(r*r+.25-rho*rho)/r
        if v>=1: th=0.
        elif v<=-1: th=pi/2
        else: th=acos(v)
        def fth(theta):
            w=r*complex(cos(theta),sin(theta)); g=w/(pi*(w*w-.25)**2)
            return abs((complex(cos(2*beta),sin(2*beta))*g).real)
        v1=quad(fth,th,pi-th,epsabs=1e-9,limit=150)[0]
        return v1*r*(2*r)**alpha
    vals=quad(funr,0,.5-rho,epsabs=1e-8,limit=100)[0] if rho<.5 else 0
    vals+=quad(funr,.5-rho,.5+rho,epsabs=1e-7,limit=180)[0]
    if R>.5+rho: vals+=quad(funr,.5+rho,R,epsabs=1e-8,limit=150)[0]
    return vals

def cross(alpha,beta,rho=.5):
    phase=complex(cos(2*beta),sin(2*beta))
    def fr(r):
        def ft(t):
            z=r*complex(cos(t),sin(t)); w=.5+z
            return abs((phase/(2*pi*(1+z)**2)).real)*(2*abs(w))**alpha*r
        return quad(ft,0,2*pi,epsabs=1e-9,limit=120)[0]
    return quad(fr,0,rho,epsabs=1e-8,limit=100)[0]

if __name__=='__main__':
    rows=[]
    for alpha in [.1,.3,.5,.75,.9]:
        for rho in [.35,.45,.5]:
            R=1.
            near=2*an(alpha,2)*rho**alpha/alpha; tail=far(alpha,R)
            vals=[]
            for beta in [0,pi/16,pi/8,3*pi/16,pi/4]:
                m=mid(alpha,beta,R,rho); c=cross(alpha,beta,rho)
                vals.append(dict(beta=beta,near=near,middle=m,cross=c,far=tail,total=near+m+c+tail))
            row=dict(alpha=alpha,rho=rho,R=R,values=vals)
            rows.append(row);print(row,flush=True)
    Path('data/split_upper_exploration.json').write_text(json.dumps(rows,indent=2)+'\n')
