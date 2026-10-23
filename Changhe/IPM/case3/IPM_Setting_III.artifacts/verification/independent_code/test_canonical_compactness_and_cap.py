"""Independent checks of the exact log-annulus strain and compensated patches.

No producer code is used. Fixed-domain polar integration of the Cartesian
source derivative is compared with the exact canonical center moment.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

th=sp.symbols('th',real=True);f,fp,D=sp.symbols('f fp D',real=True)
qx=sp.cos(th)*sp.sin(3*th)*(f+fp)-3*sp.sin(th)*sp.cos(3*th)*f
angular=sp.simplify(sp.integrate(sp.cos(th)*sp.sin(th)*qx,(th,0,2*sp.pi))/sp.pi)
assert sp.simplify(angular-f-fp/4)==0
A=2*D+1;a=4*D;b=e=-4*D
assert sp.expand(6*e-(a-2*A)*b)==-32*D
bump_width=.25;R0=.125

def eta_raw(t):
    t=np.asarray(t,dtype=float);out=np.zeros_like(t);good=np.abs(t)<bump_width
    out[good]=np.exp(-1/(1-(t[good]/bump_width)**2));return out
norm=quad(lambda t:float(eta_raw(t)),-bump_width,bump_width,epsabs=2e-14,epsrel=2e-14)[0]
def eta(t):return eta_raw(t)/norm

def cdf(t):
    if t<=-bump_width:return 0.
    if t>=bump_width:return 1.
    return quad(lambda s:float(eta(s)),-bump_width,t,epsabs=2e-14,epsrel=2e-14)[0]

def nodes(a,b,n):
    x,w=leggauss(n);return (a+b)/2+(b-a)*x/2,(b-a)*w/2

def patch_data(L,n):
    cuts=[-L-bump_width,-L+bump_width,-bump_width,bump_width]
    ts=[];ws=[]
    for lo,hi in zip(cuts,cuts[1:]):
        t,w=nodes(lo,hi,n);ts.extend(t);ws.extend(w)
    t=np.asarray(ts);w=np.asarray(ws)
    ff=np.array([cdf(float(z+L))-cdf(float(z)) for z in t]);df=eta(t+L)-eta(t)
    theta=2*np.pi*(np.arange(2*n)+.3141592653589793)/(2*n);ct=np.cos(theta);st=np.sin(theta)
    r=R0*np.exp(t);u=r[:,None]*ct;v=r[:,None]*st
    gx=ct*np.sin(3*theta)*(ff[:,None]+df[:,None])-3*st*np.cos(3*theta)*ff[:,None]
    gy=st*np.sin(3*theta)*(ff[:,None]+df[:,None])+3*ct*np.cos(3*theta)*ff[:,None]
    area=w[:,None]*r[:,None]**2*(np.pi/n)
    moment=float(np.sum(w[:,None]*ct*st*gx)*(np.pi/n)/np.pi)
    return dict(t=t,w=w,f=ff,df=df,u=u,v=v,gx=gx,area=area,moment=moment,
                sampled_grad=float(np.max(np.hypot(gx,gy))),
                partition_moment=float(w@ff),derivative_integral=float(w@df))

def at_point(data,P,sigma=1,tau=1):
    xx=sigma*(3+data['u']);yy=tau*(3+data['v']);dx=P[0]-xx;dy=P[1]-yy
    kernel=dx*dy/(np.pi*(dx*dx+dy*dy)**2)
    return float(np.sum(kernel*(sigma*tau)*data['gx']*data['area']))

def J_derivative_at(P,n):
    t,w=nodes(-bump_width,bump_width,n);theta=2*np.pi*(np.arange(2*n)+.2718281828459045)/(2*n)
    ct=np.cos(theta);st=np.sin(theta);r=np.exp(t);xx=r[:,None]*ct;yy=r[:,None]*st
    ee=eta(t)
    z=t/bump_width;de=ee*(-2*z)/(bump_width*(1-z*z)**2)
    gx=ct*np.sin(3*theta)*(ee[:,None]+de[:,None])-3*st*np.cos(3*theta)*ee[:,None]
    dx=P[0]-xx;dy=P[1]-yy;kernel=dx*dy/(np.pi*(dx*dx+dy*dy)**2)
    return float(np.sum(kernel*gx*w[:,None]*r[:,None]**2)*(np.pi/n))

rows=[]
for n in [48,96]:
    jp=J_derivative_at((3.,3.),n);j0=J_derivative_at((0.,0.),n)
    assert abs(j0-1)<3e-10,(n,j0)
    for L in [1.,4.,16.,64.,144.]:
        p=patch_data(L,n);eps=1/math.sqrt(L)
        center=sum(at_point(p,(0.,0.),s,t)for s in [-1,1]for t in [-1,1])
        other=sum(at_point(p,(3.,3.),s,t)for s in [-1,1]for t in [-1,1]if (s,t)!=(1,1))
        increment=eps*(p['moment']+other-center*jp)
        row=dict(order=n,L=L,epsilon=eps,source_integral_c=p['moment'],moment_error=p['moment']-L,
                 partition_moment=p['partition_moment'],derivative_integral=p['derivative_integral'],
                 sampled_q_gradient=p['sampled_grad'],gradient_uniform_bound=4+2*float(eta(0.)),
                 center_before_correction=eps*center,center_after_correction=eps*center*(1-j0),
                 strain_increment_at_P=increment,leading_increment=math.sqrt(L),
                 remainder_divided_by_epsilon=(increment-math.sqrt(L))/eps,J_center=j0,J_at_P=jp)
        assert abs(p['moment']-L)<2e-9*max(1,L),row
        assert p['sampled_grad']<=row['gradient_uniform_bound']+1e-12,row
        assert abs(row['remainder_divided_by_epsilon'])<1.,row
        assert abs(row['center_after_correction'])<1e-12,row
        rows.append(row)
comparisons=[]
for L in [1.,4.,16.,64.,144.]:
    rr=[r for r in rows if r['L']==L];difference=abs(rr[0]['strain_increment_at_P']-rr[1]['strain_increment_at_P'])
    assert difference<2e-8, (L,difference)
    comparisons.append(dict(L=L,quadrature_difference=difference))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',angular_source_identity=str(angular),
         common_cubic_defect='-32*D',rows=rows,comparisons=comparisons,
         scope='Exact angular and cubic identities; independent finite quadrature of canonical strain for compensated C-infinity patches. The arbitrary-sequence counterexample, weak cap closure and compactness theorem are analytic proofs in PROOF.md, not consequences of sampled cases.')
p=Path('research/canonical_compactness_and_cap/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
