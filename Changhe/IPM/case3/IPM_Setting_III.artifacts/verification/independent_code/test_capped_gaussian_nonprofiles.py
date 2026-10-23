"""Separate supporting algebra and quadrature for the explicit capped nonprofiles."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
import mpmath as mp
mp.mp.dps=55
checks=[]
x,y=s.symbols('x y',real=True);z=s.symbols('z',positive=True);H=s.Function('H')
rad=x*x+y*y;stream=-x*y*H(rad)
ux=-s.diff(stream,y);uy=s.diff(stream,x)
f=4*H(z)+2*z*s.diff(H(z),z)
assert s.simplify(-s.diff(stream,x,2)-s.diff(stream,y,2)-s.diff(y*f.subs(z,rad),x))==0
checks.append('radial_elliptic_formula')
K=2*f+2*z*s.diff(f,z);Q=2*z*s.diff(f,z)-6*f+24*H(z)
cos4=(x**4-6*x*x*y*y+y**4)/rad**2;sin4=4*x*y*(x*x-y*y)/rad**2
assert s.simplify(s.diff(ux,x)-(K-Q*cos4).subs(z,rad)/8)==0
assert s.simplify((s.diff(ux,y)+s.diff(uy,x))/2+Q.subs(z,rad)*sin4/8)==0
checks.extend(['radial_strain11','radial_strain12'])
kx,ky,B,L=s.symbols('kx ky B L',real=True)
rhohat=-s.I*B*s.pi*L*ky/2
U1=kx*ky/(kx*kx+ky*ky)*rhohat;U2=-kx*kx/(kx*kx+ky*ky)*rhohat
S11=s.I*kx*U1;S12=s.I*(ky*U1+kx*U2)/2
assert s.factor(S11*S11+S12*S12-(B*s.pi*L*kx*ky/4)**2)==0
checks.append('Fourier_strain_vector_norm')
u,v,t=s.symbols('u v t',positive=True)
primitive=(2*t+u+v)/s.sqrt((t+u)*(t+v))
assert s.factor(s.diff(primitive,t)+(u-v)**2/(2*((t+u)*(t+v))**s.Rational(3,2)))==0
checks.append('heat_integral_primitive')
cstar=s.Rational(1,73746);C=16/cstar
assert C==1179936 and 4097<9**4 and s.Rational(3,7)<1-cstar
assert s.Rational(65,24)+s.Rational(1,100)<s.Rational(11,4)
assert s.Rational(11,4)*s.Rational(16,15)<3
assert s.Rational(11,4)**3*s.Rational(16,15)**2<25
assert s.Rational(6,7)**4>s.Rational(1,2)
assert s.Rational(9,13)**2*32/(15625*s.Rational(22,7))>s.Rational(1,10000)
assert s.integrate(x**4*(1-x)**4/(1+x*x),(x,0,1))==s.Rational(22,7)-s.pi
checks.extend(['cap_constants','rectangle_constants','strict_weighted_gap','pi_certificate'])
r=s.symbols('r',positive=True)
assert s.integrate(r,(r,0,1))+s.integrate(r**-3,(r,1,s.oo))==1
checks.append('weighted_denominator_integral')
rows=[]
for bv,lv in [(9,4),(20,15),(9,1179936*9)]:
    aa=mp.mpf(1)/(lv*lv)
    val=mp.quad(lambda q:((1+4*aa*q)*(1+4*q))**mp.mpf('-1.5'),[0,1,lv*lv,mp.inf])
    cg=-2*bv*aa*val;ref=-mp.mpf(bv)/(lv+1)**2
    err=abs(cg-ref)/abs(ref);assert err<mp.mpf('1e-45'),err
    rows.append({'B':bv,'L':lv,'canonical_c':mp.nstr(cg,45),'relative_error':mp.nstr(err,15)})
flat=[]
for zz in ['.01','.25','1','4','100']:
    z=mp.mpf(zz);g=mp.exp(-z);Hg=mp.quad(lambda u:u**3*mp.exp(-z/(u*u)),[0,1])
    K=2*(1-(1+z)*g);Q=4*(-1+(2-z)*g+6*(mp.mpf('.25')-Hg))
    # Reconstruct directly from rf'=-2zg to avoid a reused simplification.
    Q=-2*z*g-6*(1-g)+24*(mp.mpf('.25')-Hg)
    maximum=(abs(K)+abs(Q))/2
    assert maximum<=1+mp.mpf('1e-50'),(zz,maximum)
    flat.append({'z':zz,'sigma_over_origin':mp.nstr(maximum,40)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'gaussian_heat_inverse':rows,'flat_cap_supporting_samples':flat,'scope':'Exact identities and positive rational constants, with independent55-digit heat and flat-kernel quadrature. The continuum global cap and residual lower bound are proved in PROOF.md, not inferred from samples.'}
p=Path('research/capped_gaussian_nonprofiles/verification/checks.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
