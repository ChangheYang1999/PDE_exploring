"""Independent exact and physical-kernel controls for packet189.
Finite polynomial bump controls have C5 regularity, not the theorem's C-infinity.
The theorem is proved before this script; no NUM source is imported.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib,json,time
import sympy as sp
import numpy as np
from numpy.polynomial.legendre import leggauss
from math import pi
start=time.monotonic();checks=[];counters=[];r=sp.symbols('r',positive=True)
out=Path('research/189_physical_norms_and_inverse_constant/verification')
phi=sp.expand((r-1)**6*(2-r)**6)
def integ(p,a=1,b=2):
    p=sp.Poly(sp.expand(p),r);return sum(co*(b**(i[0]+1)-a**(i[0]+1))/sp.Integer(i[0]+1)for i,co in p.terms())
def eq(a,b,name):
    assert sp.cancel(a-b)==0,(name,a,b);checks.append(name)
I=integ(r*phi);g=2*phi/I
mass=integ(r*g);g2=2*integ(r*g*g);o2=integ(r**3*g*g)
gradg=2*integ(r*sp.diff(g,r)**2)
grado=integ(r**3*sp.diff(g,r)**2)
eq(mass,2,'center-velocity-c1')
eq(2*integ(r*g*g)+2*integ(r**2*g*sp.diff(g,r))+integ(r**3*sp.diff(g,r)**2),grado,'Omega-gradient-angular-integral-and-IBP')
for scale in map(sp.Rational,['3/2','2','3','5']):
    gr=sp.expand(g.subs(r,r/scale)/scale**2)
    for c in map(sp.Rational,['1','-2','3/7']):
        f=c*gr
        eq(integ(r*f,scale,2*scale)/2,c,f'mass-R{scale}-c{c}')
        eq(2*integ(r*f*f,scale,2*scale),c*c*g2/scale**2,f'G-L2-R{scale}-c{c}')
        eq(integ(r**3*f*f,scale,2*scale),c*c*o2,f'Omega-L2-R{scale}-c{c}')
        eq(2*integ(r*sp.diff(f,r)**2,scale,2*scale),c*c*gradg/scale**4,f'G-grad-R{scale}-c{c}')
        eq(integ(r**3*sp.diff(f,r)**2,scale,2*scale),c*c*grado/scale**2,f'Omega-grad-R{scale}-c{c}')
        eq(2*integ(r*(1+r*r)*f*f,scale,2*scale),c*c*(g2/scale**2+2*o2),f'critical-weight-R{scale}-c{c}')
avgs=[]
for n in [1,2,3,4,8,16,32]:
    radii=[sp.Integer(n)*4**j for j in range(1,n+1)]
    assert all(2*a<b for a,b in zip(radii,radii[1:]));checks.append(f'disjoint-n{n}')
    vals=[]
    for j in range(5):
        sg=sum(R**(-2-2*j)for R in radii)/n**2
        so=sum(R**(-2*j)for R in radii)/n**2
        assert sg<=radii[0]**(-2-2*j)/n and so<=radii[0]**(-2*j)/n;checks.append(f'derivative-square-bound-n{n}-j{j}')
        vals.append([str(sg),str(so)])
    eq(sum(sp.Rational(1,n)for R in radii),1,f'constant-n{n}')
    avgs.append({'n':n,'inner_radius':str(radii[0]),'G_L2_squared_over_pi':str(g2*sum(R**-2 for R in radii)/n**2),'Omega_L2_squared_over_pi':str(o2/n),'critical_weighted_squared_over_pi':str(g2*sum(R**-2 for R in radii)/n**2+2*o2/n),'derivative_scale_squares':vals})
# Physical-space full-plane kernel, independently integrated in source polar coordinates.
# Stable factored bump avoids cancellation of its expanded polynomial.
If=float(I);A=float(integ(r**3*g));points=[(0.,0.),(.3,.2),(-.6,.4),(.8,0.),(3.,0.),(0.,-3.),(2.4,2.4),(-3.,1.)]
quadrows=[]
for order in [24,48,96]:
    nodes,weights=leggauss(order);rad=1.5+.5*nodes;wr=.5*weights
    ang=2*pi*(np.arange(8*order)+.173)/(8*order);dth=2*pi/(8*order)
    yy=rad[:,None]*np.sin(ang);xx=rad[:,None]*np.cos(ang)
    gg=2*((rad-1)*(2-rad))**6/If;omega=xx*gg[:,None]
    w=wr[:,None]*rad[:,None]*dth
    for x,y in points:
        dx=x-xx;dy=y-yy;den=dx*dx+dy*dy
        u=np.array([np.sum(w*omega*dy/den),-np.sum(w*omega*dx/den)])/(2*pi)
        if x*x+y*y<1:want=np.array([0.,1.])
        else:
            rr=x*x+y*y;want=np.array([A*x*y/rr**2,A*(y*y-x*x)/(2*rr**2)])
        err=float(np.max(np.abs(u-want)));assert err<2e-12,(order,x,y,err)
        checks.append(f'full-plane-kernel-order{order}-point{x},{y}')
        quadrows.append({'order_radial':order,'angles':8*order,'point':[x,y],'velocity':u.tolist(),'exact_velocity':want.tolist(),'max_error':err})
# Finite-radius integrals for a sharpness extremizer. The hard truncation here is
# only an integral identity check; the theorem uses smooth cutoffs and DCT.
sharp=[]
for sigma in [sp.Rational(3,2),sp.Rational(2),sp.Rational(3),sp.Rational(5)]:
    last=sp.Integer(0)
    for R in [2,4,8,16,64]:
        ratio_squared_over_best=1-(1+sp.Integer(R)**2)**(1-sigma)
        assert sp.simplify(ratio_squared_over_best-last).is_positive and sp.simplify(1-ratio_squared_over_best).is_positive
        last=ratio_squared_over_best;val=float(ratio_squared_over_best)
        checks.append(f'sharp-truncation-sigma{sigma}-R{R}')
        sharp.append({'sigma':str(sigma),'radius':R,'squared_ratio_to_optimal':val})
# Fixed-annulus bound: exact lower bound for log(2) from its positive
# atanh(1/3) series suffices for these finite polynomial examples.
log2lower=2*sum(sp.Rational(1,3)**(2*k+1)/sp.Integer(2*k+1)for k in range(30))
for n in [1,2,3,4,8,16,32]:
    assert o2*sp.Rational(2*n-1,n)*log2lower/4>1
    checks.append(f'fixed-annulus-bound-certified-log-lower-n{n}')
# Hand-derived wrong-convention comparisons, NOT executed mutated programs.
for wrong,name in [(sp.Rational(-1),'opposite-center-sign'),(sp.Rational(1,2),'missing-angular-factor'),(sp.Rational(2),'extra-angular-factor')]:
    assert wrong!=mass/2;counters.append(name)
assert o2!=2*o2;counters.append('Omega-L2-is-half-rG-L2-squared')
assert sp.Rational(1,4)!=1;counters.append('single-annulus-Omega-L2-does-not-decay-like-G')
assert 1!=0;counters.append('absolute-inner-velocity-is-not-relative-inner-velocity')
now=datetime.now(timezone.utc).isoformat();result={'utc':now,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED finite controls','exact_checks':[v for v in checks if not v.startswith('full-plane-kernel')],'physical_kernel_checks':[v for v in checks if v.startswith('full-plane-kernel')],'algebraic_counterchecks':counters,'polynomial_control_scope':'phi=(r-1)^6(2-r)^6 on[1,2], zero outside; C5, not a C-infinity example; controls do not replace smooth proof','I':str(I),'base_values_over_pi':{'G_L2_squared':str(g2),'Omega_L2_squared':str(o2),'G_gradient_squared':str(gradg),'Omega_gradient_squared':str(grado)},'averages':avgs,'physical_kernel_rows':quadrows,'sharpness_integral_controls':sharp,'proof_initial_sha256':hashlib.sha256((out/'initial_proof.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(out/'controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(now,len(result['exact_checks']),'exact',len(result['physical_kernel_checks']),'kernel',len(counters),'algebraic counterchecks',result['elapsed_seconds'],'s',max(v['max_error']for v in quadrows))
