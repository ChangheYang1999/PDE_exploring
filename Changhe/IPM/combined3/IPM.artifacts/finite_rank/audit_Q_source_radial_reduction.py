#!/usr/bin/env python3
"""Independent actual-field interval check of radial-vs-Cartesian reduction."""
import json,sys,math,hashlib,time
from pathlib import Path
from flint import arb,arb_series,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator
from certify_Q_source_constants import lap
ctx.prec=512

def combine(md,terms):
    out={}
    for i,j,c in terms:
        for key,p in md['rho',i,j].items():out[key]=out.get(key,arb(0))+c*p[0]
    return out
def energy(modes):
    out=arb(0)
    for (kind,n),v in modes.items():
        out+=(2 if n==0 else 1)*arb.pi()*v*v
    return out
def add_modes(x,y):
    out=dict(x)
    for k,v in y.items():out[k]=out.get(k,arb(0))+v
    return out
def diffzero(a,b):
    keys=set(a)|set(b)
    return all((a.get(k,arb(0))-b.get(k,arb(0))).contains(0) for k in keys)

st=time.time();e0=Evaluator(512,0,-1);e5=Evaluator(512,5,-1);rows=[]
for rs in ['1/100','1/2','3','100']:
    r=arb(rs);f=e0.modes_taylor(r,degree=5)['rho',0,0];direct=e5.modes_taylor(r,degree=0)
    rr=arb_series([r,1],prec=6)
    ll={};l2={};gl=arb(0);gl2=arb(0);hess=arb(0)
    for (kind,n),p in f.items():
        pL=lap(p,rr,n);pLL=lap(pL,rr,n)
        ll[kind,n]=pL[0];l2[kind,n]=pLL[0]
        weight=(2 if n==0 else 1)*arb.pi()
        gl+=weight*(pL[1]*pL[1]+n*n*pL[0]*pL[0]/(r*r))
        gl2+=weight*(pLL[1]*pLL[1]+n*n*pLL[0]*pLL[0]/(r*r))
        a=p.derivative().derivative()[0]
        b=n*(p.derivative()/rr-p/(rr*rr))[0]
        c=(p.derivative()/rr-n*n*p/(rr*rr))[0]
        hess+=weight*(a*a+2*b*b+c*c)
    dL=combine(direct,[(2,0,1),(0,2,1)])
    dLL=combine(direct,[(4,0,1),(2,2,2),(0,4,1)])
    dgL=[combine(direct,[(3,0,1),(1,2,1)]),combine(direct,[(2,1,1),(0,3,1)])]
    dgLL=[combine(direct,[(5,0,1),(3,2,2),(1,4,1)]),combine(direct,[(4,1,1),(2,3,2),(0,5,1)])]
    dh=[combine(direct,[(2,0,1)]),combine(direct,[(1,1,1)]),combine(direct,[(0,2,1)])]
    directgl=sum((energy(m) for m in dgL),arb(0));directgl2=sum((energy(m) for m in dgLL),arb(0))
    directhess=energy(dh[0])+2*energy(dh[1])+energy(dh[2])
    checks={'Delta_modes':diffzero(ll,dL),'Delta2_modes':diffzero(l2,dLL),
            'gradDelta_angular_norm':(gl-directgl).contains(0),
            'gradDelta2_angular_norm':(gl2-directgl2).contains(0),
            'Hessian_polar_angular_norm':(hess-directhess).contains(0)}
    assert all(checks.values())
    rows.append({'radius':rs,'checks':checks,'gradDelta_squared_angular_integral':gl.str(70),'gradDelta2_squared_angular_integral':gl2.str(70)})
    print(rs,checks,flush=True)
out={'status':'PASSED_ACTUAL_FIELD_INTERVAL_RADIAL_REDUCTION_AUDIT','rows':rows,'elapsed_seconds':time.time()-st,
     'producer_sha256':hashlib.sha256((HERE/'certify_Q_source_constants.py').read_bytes()).hexdigest(),
     'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Actual-field interval equality checks at four radii verify radial differential formulas against separately assembled Cartesian derivatives. Whole-plane coverage and analytic tails are separate certificate obligations.'}
(HERE/'Q_source_radial_reduction_audit.json').write_text(json.dumps(out,indent=2)+'\n')
