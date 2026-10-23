"""Exact secondary identities and independent reconstruction/kernel tests."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
import sympy as s
from secondary_basis import SecondaryBasis
from evaluate_secondary_state import ReconstructedSecondary
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient

root=Path('research/secondary_source_geometry/verification');root.mkdir(parents=True,exist_ok=True)
x,y,ell,e,f,g,H=s.symbols('x y ell e f g H');lx=2*ell-s.Rational(1,3)
rho=e*y**3+f*x*x*y**3+g*y**5
psi=(s.Rational(1,3)-ell)*x*y+H*(x**3*y-x*y**3)/2
R=s.expand((ell*x-s.diff(psi,y))*s.diff(rho,x)+(ell*y+s.diff(psi,x))*s.diff(rho,y)-rho)
P=s.Poly(R,x,y)
assert s.simplify(P.coeff_monomial(x*x*y**3)-(2*lx*f+s.Rational(9,2)*e*H))==0
assert s.simplify(P.coeff_monomial(y**5)-(s.Rational(2,3)*g-s.Rational(3,2)*e*H))==0
assert P.coeff_monomial(y**3)==0
# The primary relation would leave +2 e y^3. This check detects transplantation.
wrong=psi+s.Rational(2,3)*x*y
wrongR=s.expand((ell*x-s.diff(wrong,y))*s.diff(rho,x)+(ell*y+s.diff(wrong,x))*s.diff(rho,y)-rho)
assert s.Poly(wrongR,x,y).coeff_monomial(y**3)==2*e
# Exact Laurent coefficients of sin^3(theta) cos(2k theta).
z=s.symbols('z');si=(z-z**-1)/(2*s.I)
expected={3:[-s.Rational(1,4),s.Rational(3,8),-s.Rational(3,8),s.Rational(1,8),0,0],5:[0,-s.Rational(1,8),s.Rational(3,8),-s.Rational(3,8),s.Rational(1,8),0]}
for k in range(6):
 expr=s.expand(si**3*(z**(2*k)+z**(-2*k))/2)
 for n in (3,5):assert s.simplify(2*s.I*expr.coeff(z,n)-expected[n][k])==0

rng=np.random.default_rng(332);numerical=[]
for p in (1/3,.5,2/3):
 b=SecondaryBasis(5,6,p,1.);coeff=rng.normal(size=b.size)*.02;coeff[0]+=1
 state=root/'manufactured.npz';np.savez_compressed(state,coefficients=coeff,radial=b.N,angular=b.M,exponent=p,length=1.,cl=1/p,axis_order=3)
 obj=ReconstructedSecondary(state);ct=obj.center_and_tail()
 pts=np.array([[r*np.cos(t),r*np.sin(t)] for r in (1e-6,.02,.7,13.,1e4) for t in (.031,.71,1.5)])
 xx,yy=pts.T;val,gx,gy=b.evaluate(xx,yy,True);a=val@coeff;rx=gx@coeff;ry=gy@coeff
 density=float(max(abs(a-obj.rho(xx,yy))/np.maximum(1e-100,abs(a))))
 errors=[];component_errors=[]
 for h in (.003,.0015,.00075):
  fx,fy=cartesian_gradient(obj.rho,xx,yy,h,0.)
  component_errors.append(float(max(np.max(abs(fx-rx)/np.maximum(abs(rx),1e-100)),np.max(abs(fy-ry)/np.maximum(abs(ry),1e-100)))))
  errors.append(float(np.max(np.hypot(fx-rx,fy-ry)/np.maximum(np.hypot(rx,ry),1e-100))))
 ce=float(abs(b.center_strain()@coeff-ct['adaptive_center'][-1]['c']))
 he=float(abs(b.quartic_stream_difference()@coeff-ct['adaptive_center'][-1]['H']))
 fr,gr=b.fifth_density_rows();fe=float(abs(fr@coeff-ct['f_fifth_x2y3']));ge=float(abs(gr@coeff-ct['g_fifth_y5']))
 numerical.append({'p':p,'density_relative_error':density,'FD8_vector_relative_errors':errors,'FD8_component_relative_errors_including_roundoff_dominated_dx_near_origin':component_errors,'strain_difference':ce,'H_difference':he,'f_difference':fe,'g_difference':ge})
 print(json.dumps(numerical[-1]),flush=True)
 assert density<2e-11 and min(errors)<2e-9 and max(ce,he,fe,ge)<2e-10

b=SecondaryBasis(1,1,.5,1.);coeff=np.array([1.,0.]);state=root/'pure_cubic.npz'
np.savez_compressed(state,coefficients=coeff,radial=1,angular=1,exponent=.5,length=1.,cl=2.,axis_order=3)
obj=ReconstructedSecondary(state);ct=obj.center_and_tail()
assert abs(ct['adaptive_center'][-1]['c']+.5)<1e-12
assert abs(ct['adaptive_center'][-1]['H']-.125)<1e-12
velocity=[]
for q,(nr,nt,ne,of) in enumerate(((24,128,96,2.),(40,256,144,4.),(64,512,224,8.))):
 inv=DirectInverse(obj.rho,Quadrature(nr,nt,ne,of,1.,.5,16.,2.))
 hs=np.array([.03,.015,.0075]);slopes=np.array([inv.velocity(0.,h)[1]/h for h in hs])
 fit=np.polynomial.polynomial.polyfit(hs*hs,slopes,2)
 row={'q':q,'axis_slopes':slopes.tolist(),'extrapolated_c':float(fit[0]),'extrapolated_H':float(-2*fit[1])}
 velocity.append(row);print(json.dumps(row),flush=True)
assert abs(velocity[-1]['extrapolated_c']+.5)<3e-8 and abs(velocity[-1]['extrapolated_H']-.125)<3e-6
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':'Degree-five transport, wrong-primary-relation detection and all angular product coefficients','reconstruction':numerical,'canonical_axis_velocity':velocity,'scope':'Secondary implementation checks. No transport solution or primary endpoint.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
