"""Own controls for packet145. No numerics or lead code imported.
The all-radius limit is proved before these manufactured finite instances.
"""
from pathlib import Path
import datetime,time,json,sys
import sympy as S
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import expit
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic();exact=[]
x,y,b=S.symbols('x y beta',real=True)
def zero(name,v):exact.append({'name':name,'pass':S.cancel(S.expand(v))==0})
psi=S.Function('psi')(x,y);th=S.Function('Theta')(x,y)
lap=lambda f:S.diff(f,x,2)+S.diff(f,y,2)
div=lambda u:S.diff(u[0],x)+S.diff(u[1],y)
v=S.Matrix([-S.diff(psi,y),S.diff(psi,x)]);w=b*S.Matrix([x,y])+v;om=-lap(psi);f=w.dot(S.Matrix([S.diff(om,x),S.diff(om,y)]))+om-S.diff(th,x);t=w.dot(S.Matrix([S.diff(th,x),S.diff(th,y)]))-(b-2)*th
p=S.diff(psi,x);q=S.diff(psi,y);J=(x*om+th/(3*b-2))*w-x*th*S.Matrix([1,0])-S.Matrix([p*q,(q*q-p*p)/2])+(1-3*b)*(psi*S.Matrix([1,0])-x*S.Matrix([p,q]))
zero('general_flux_divergence_with_thermal_correction',div(J)-x*f-t/(3*b-2))
zero('stress_sign',div(S.Matrix([p*q,(q*q-p*p)/2]))-v[0]*om)
zero('affine_laplacian_flux',div(psi*S.Matrix([1,0])-x*S.Matrix([p,q]))-x*om)
chi=S.Function('chi')(x,y);Q=S.Function('Q')(x,y)
zero('compensator_is_compact_laplacian',-lap(chi*Q)+lap(Q)+lap((chi-1)*Q))
delta,rho,g,corr,dt,be,source=S.symbols('delta rho g interaction dtheta btransport esource')
zero('scaled_residual_after_fixed_point',(g+delta*corr-dt+source+be).subs(source,rho*(-g+dt-delta*corr))-((1-rho)*(g+delta*corr-dt)+be))
s=S.symbols('s',positive=True)
zero('impulse_scaling_exponent',1+2-2*s-(3-2*s));zero('thermal_scaling_exponent',(1-2*s)-1+2*s)
z=S.symbols('theta',real=True);m=S.symbols('m');A=S.Function('A')(z)
zero('angular_integration_by_parts_weight',S.trigsimp(m*S.cos(z)**2+S.diff(S.cos(z)*S.sin(z),z)-((m+2)*S.cos(z)**2-1)))
# Exact opposite signs among smooth nonnegative trial angular functions.
angular_signs=[]
for beta in [S.Rational(9,4),S.Integer(3),S.Integer(6)]:
 sval=1/beta
 def trigint(i,j):return S.simplify(2*S.gamma(S.Rational(1,2)+i)*S.gamma(S.Rational(1,2)+j)/S.gamma(i+j+1))
 simple=-((3-2*sval)*trigint(2,0)-trigint(1,0))
 narrow=-((3-2*sval)*(trigint(2,6)+trigint(2,0)/1000)-(trigint(1,6)+trigint(1,0)/1000))
 angular_signs.append({'beta':str(beta),'A_cos2_m1_over_pi':str(S.simplify(simple/S.pi)),'A_cos2_sin12_plus_cos2_over1000_m1_over_pi':str(S.simplify(narrow/S.pi)),'pass':bool(simple<0 and narrow>0)})
# Direct volume and boundary quadratures of a nonthermal polynomial example.
psi0=x*y+x**3*y/7-x*y*y/5+x**5/31;th0=x*x*(1+y+x*x/11+y*y/13)
px=S.diff(psi0,x);py=S.diff(psi0,y);v0=S.Matrix([-py,px]);om0=-lap(psi0);volume=[]
for beta in [2.,2.5,4.]:
 w0=beta*S.Matrix([x,y])+v0;f0=w0.dot(S.Matrix([S.diff(om0,x),S.diff(om0,y)]))+om0-S.diff(th0,x);t0=w0.dot(S.Matrix([S.diff(th0,x),S.diff(th0,y)]))-(beta-2)*th0
 jj=(x*om0+th0/(3*beta-2))*w0-x*th0*S.Matrix([1,0])-S.Matrix([px*py,(py*py-px*px)/2])+(1-3*beta)*(psi0*S.Matrix([1,0])-x*S.Matrix([px,py]))
 vf=S.lambdify((x,y),x*f0+t0/(3*beta-2),'numpy');jf=S.lambdify((x,y),list(jj),'numpy')
 for radius in [.7,1.3,2.]:
  g,wt=leggauss(24);rs=radius*(g+1)/2;rw=radius*wt/2;ang=2*np.pi*(np.arange(96)+.31)/96
  rr,aa=np.meshgrid(rs,ang,indexing='ij');xx=rr*np.cos(aa);yy=rr*np.sin(aa)
  vol=float(np.sum(rw[:,None]*rr*(2*np.pi/96)*vf(xx,yy)))
  jx,jy=jf(radius*np.cos(ang),radius*np.sin(ang));flux=float(radius*(2*np.pi/96)*np.sum(jx*np.cos(ang)+jy*np.sin(ang)));err=abs(vol-flux)
  volume.append({'beta':beta,'radius':radius,'volume':vol,'boundary':flux,'error':err,'pass':err<2e-10})
# Compensator first moment is zero, but its transported moment is O(delta),
# generally nonzero. Use a compact C7 stream phi=x(1-r^2)^8 on the unit disk.
phi=x*(1-x*x-y*y)**8;bb=-lap(phi);u=S.Matrix([-x*y*y,y**3/3]);g,wt=leggauss(24);rs=(g+1)/2;rw=wt/2;ang=2*np.pi*(np.arange(96)+.37)/96;rr,aa=np.meshgrid(rs,ang,indexing='ij');xx=rr*np.cos(aa);yy=rr*np.sin(aa);weights=rw[:,None]*rr*(2*np.pi/96)
mass=float(np.sum(weights*S.lambdify((x,y),x*phi,'numpy')(xx,yy)));b_fun=S.lambdify((x,y),bb,'numpy');b_x_moment=float(np.sum(weights*xx*b_fun(xx,yy)));comp=[]
for delta0 in [.1,.03,.001]:
 w0=3*S.Matrix([x,y])+delta0*u;expr=x*(w0.dot(S.Matrix([S.diff(bb,x),S.diff(bb,y)]))+bb)
 actual=float(np.sum(weights*S.lambdify((x,y),expr,'numpy')(xx,yy)));pred=-2*delta0*mass
 comp.append({'delta':delta0,'int_x_b':b_x_moment,'int_x_transport_b':actual,'predicted':pred,'error':abs(actual-pred),'pass':abs(b_x_moment)<1e-10 and abs(actual-pred)<2e-10 and abs(actual)>1e-6})
# Scaling limit control with a smooth manufactured reference residual
# f_*(X)=x(1+r^2)^(-(1+2s)/2), whose homogeneous angular coefficient is cos(theta).
limits=[]
for beta in [2.25,3.,6.]:
 sval=1/beta
 for order in [128,256]:
  g,wt=leggauss(order);a1=2.5*(g+1);w1=2.5*wt;a2=5+1.5*(g+1);w2=1.5*wt;rs=np.r_[a1,a2];rw=np.r_[w1,w2]
  z=(a2-5)/3;cut=expit(-1/z+1/(1-z));rh=np.r_[np.zeros_like(a1),cut]
  expected=np.pi*np.sum(rw*(1-rh)*rs**(2-2*sval));rows=[]
  for R in [2.,10.,100.,1000.,10000.]:
   actual=np.pi*np.sum(rw*(1-rh)*rs**3*R**(1+2*sval)/(1+(R*rs)**2)**((1+2*sval)/2))
   rows.append({'R':R,'scaled_impulse':float(actual),'limit':float(expected),'error':float(abs(actual-expected))})
  limits.append({'beta':beta,'radial_order_per_piece':order,'rows':rows,'pass':rows[-1]['error']<2e-5 and rows[-1]['error']<rows[0]['error']/1e5})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_checks':exact,'angular_sign_controls':angular_signs,'bounded_domain_flux_controls':volume,'compensator_controls':comp,'manufactured_scaling_limits':limits,'all_pass':all(z['pass'] for z in exact+angular_signs+volume+comp+limits),'scope':'Independent exact identities and finite manufactured quadrature controls. No actual135 residual or reference temperature tail was computed. No interval proof or full B2 endpoint.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_pass':result['all_pass'],'counts':[len(z) for z in [exact,angular_signs,volume,comp,limits]],'elapsed_seconds':result['elapsed_seconds'],'max_flux_error':max(z['error'] for z in volume),'max_compensator_error':max(z['error'] for z in comp)},indent=2))
if not result['all_pass']:raise SystemExit(1)
