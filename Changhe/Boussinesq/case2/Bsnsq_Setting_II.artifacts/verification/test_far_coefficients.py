"""Independent analytic and high-precision validation of far coefficients."""
import json,sys,time,tempfile,copy
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import mpmath as mp
import sympy as sp
from profile_data import CoefficientProfile
from far_coefficients import radial_endpoints,angular,stream_modes,evaluate

mp.mp.dps=100
rows=[]
z=sp.symbols('z')
for n in range(9):
    got=sp.diff(sp.chebyshevt(n,z),z).subs(z,-1)
    wanted=0 if n==0 else (-1)**(n-1)*n*n
    assert got==wanted
phi=np.linspace(.03,1.54,193)
for l in range(8):
    c=np.zeros(l+1);c[l]=1
    m=stream_modes(c);got=np.sin(phi[:,None]*(2*np.arange(1,len(m)+1)))@m
    exact=np.cos(phi)*np.sin(phi)*np.cos(2*l*phi)
    assert np.max(np.abs(got-exact))<2e-15
# Check angular derivatives against a separate symbolic derivative.
p=sp.symbols('p')
c=np.array([.7,-.2,.09])
for temp in [True,False]:
    expr=sp.cos(p)*sp.sin(p)*(sp.cos(p) if temp else 1)*sum(float(x)*sp.cos(2*j*p) for j,x in enumerate(c))
    want=sp.lambdify(p,sp.diff(expr,p),'numpy')(phi)
    _,got=angular(c,phi,temp)
    assert np.max(np.abs(got-want))<1e-14


def normalized_mp(obj,c,sigma,r,angle):
    """Direct Clenshaw-free polynomial evaluation of the actual stored sigma."""
    r=mp.mpf(r);a=mp.mpf(angle);L=mp.mpf(obj.length);sig=mp.mpf(sigma)
    ratio=r*r/(r*r+L*L)
    if obj.mapname=='xi':v=2*ratio-1;weight=(2*L*L/(r*r+L*L))**sig
    else:v=2*(1+r*r/(L*L))**(-1/(2*mp.mpf(obj.beta_map)))-1;weight=(1+r*r/(L*L))**(-sig)
    total=mp.mpf(0)
    for l,row in enumerate(c):
        polynomial=sum(mp.mpf(float(cc))*mp.chebyt(n,v) for n,cc in enumerate(row))
        total+=ratio**l*mp.cos(2*l*a)*polynomial
    return r**(2*sig)*weight*total


def endpoints_mp(obj,c,sigma,angle):
    L=mp.mpf(obj.length);d=1/mp.mpf(obj.beta);sig=mp.mpf(sigma);phi=mp.mpf(angle)
    k=2 if obj.mapname=='xi' else 1
    a0=sum((k*L*L)**sig*mp.cos(2*l*phi)*sum(mp.mpf(float(cc))*(1 if k==2 else (-1)**n)
               for n,cc in enumerate(row)) for l,row in enumerate(c))
    if k==2:return a0,mp.mpf(0)
    a1=sum(2*L**(2*sig+d)*mp.cos(2*l*phi)*sum(mp.mpf(float(cc))*(-1)**(n-1)*n*n
               for n,cc in enumerate(row)) for l,row in enumerate(c))
    return a0,a1

source='data/control_snapshots/tmap_T4_beta3.npz'
obj=CoefficientProfile(source)
# A near-equal but distinct compactification exponent cannot share this expansion.
near=copy.copy(obj);near.beta_map=near.beta+2.0**(-40)
try:
    radial_endpoints(near,near.ca,near.sigma_a)
except ValueError:
    unequal_map_rejected=True
else:
    raise AssertionError('Unequal beta_map was accepted')
for name,c,sigma in [('a',obj.ca,obj.sigma_a),('G',obj.cg,obj.sigma_g)]:
    for angle in ['0.19','0.53','0.97','1.33']:
        e0,e1=endpoints_mp(obj,c,sigma,angle)
        r=mp.mpf('1e120');d=1/mp.mpf(obj.beta)
        extracted=(normalized_mp(obj,c,sigma,r,angle)-e0)*r**d
        err=abs(extracted-e1)
        assert err<mp.mpf('1e-25'),str(err)
        c0,c1=radial_endpoints(obj,c,sigma)
        numerical=np.cos(2*float(angle)*np.arange(len(c1)))@c1
        assert abs(float(e1)-numerical)<2e-8
        rows.append(dict(field=name,angle=angle,radius=str(r),next_exact=str(e1),
                         extracted=str(extracted),absolute_error=str(err),
                         floating_endpoint_error=abs(float(e1)-numerical)))
report=dict(timestamp=datetime.now(timezone.utc).isoformat(),source=source,precision_digits=mp.mp.dps,unequal_map_rejected=unequal_map_rejected,
            algebraic_tests='Chebyshev endpoint derivatives n0..8, sine product l0..7, symbolic angular derivatives',
            interpretation='Normalize by actual stored envelope power before extracting the fractional correction. No PDE claim.',
            rows=rows)
Path('runs/far_coefficient_tests.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
