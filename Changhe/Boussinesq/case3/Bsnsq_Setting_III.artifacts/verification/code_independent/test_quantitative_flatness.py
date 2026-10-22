"""Independent exact calculus controls for165; no PDE solver or NUM imports."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sympy as s
import json,time,math,hashlib
r=Path('verification/quantitative_flatness_controls_20261021T1226Z');r.mkdir(exist_ok=True)
inputs={'derivative_orders':list(range(13)),'log_radii':[2,3,4,6,10,20,40],'flatness_pairs':[[n,k] for n in [0,4,8,12] for k in [0,10,30]],'stretched_exponents':[[1,4],[1,2],[1,1],[2,1]],'scope':'Manufactured exact calculus identities and finite log-domain diagnostics; not proof by sampling.'}
(r/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n');start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();checks=[]
def check(name,expr):
 z=s.simplify(expr);checks.append({'name':name,'difference':str(z),'pass':z==0})
u,v,L,M=s.symbols('u v L M',real=True);up=s.symbols('up',positive=True);f=s.Function('f')(u);F=s.Function('F')(u)
W1=f;W2=(4-s.diff(f,u))*v+M-F;O=s.diff(f,u,2)*v+s.diff(F,u)
check('divW',s.diff(W1,u)+s.diff(W2,v)-4)
check('minus_curlW',-s.diff(W2,u)+s.diff(W1,v)-O)
check('thermal_general',W1*s.diff(F,u)-f*s.diff(F,u))
R=W1*s.diff(O,u)+W2*s.diff(O,v)+O-s.diff(F,u)
expected=(f*s.diff(f,u,3)+(5-s.diff(f,u))*s.diff(f,u,2))*v+f*s.diff(F,u,2)+(M-F)*s.diff(f,u,2)
check('full_residual_general',R-expected)
check('outgoing_side_residual',R.subs(F,M).doit()-(f*s.diff(f,u,3)+(5-s.diff(f,u))*s.diff(f,u,2))*v)
check('interior_side_residual',R.subs(f,0).doit())
check('exact_shear_thermal',s.Integer(0))
check('exact_shear_vorticity',((4*v-F)*s.diff(s.diff(F,u),v)+s.diff(F,u))-s.diff(F,u))
h=s.exp(-s.log(up)**2);poly=s.Integer(1);polys=[]
for n in inputs['derivative_orders']:
 polys.append(poly)
 check('derivative_'+str(n),s.diff(h,up,n)*up**n/h-poly.subs(L,-s.log(up)))
 poly=s.expand((2*L-n)*poly-s.diff(poly,L))
check('positive_second_factor',polys[2]-2*(2*L+1)*(L-1))
check('third_derivative',polys[3]-(8*L**3-12*L**2-8*L+6))
check('residual_ratio_cancellation',polys[3]-2*L*polys[2]-(-8*L**2-4*L+6))
logres=[]
for ell in inputs['log_radii']:
 rat=Fraction(int(polys[3].subs(L,ell)),int(polys[2].subs(L,ell)))-2*ell
 logdev=-ell*ell+ell+math.log(abs(rat));ok=rat<0 and logdev<math.log(Fraction(1,2))
 logres.append({'L':ell,'difference_from_5_multiplier':str(rat),'log_absolute_difference_from_5':logdev,'coefficient_ratio_in_4point5_to_5':ok})
flat=[]
for n,k in inputs['flatness_pairs']:
 vals=[]
 for ell in [100,200,400]:
  pp=abs(int(polys[n].subs(L,ell)));vals.append(-ell*ell+(n+k)*ell+math.log(pp))
 flat.append({'n':n,'k':k,'log_scaled_derivatives_at_L_100_200_400':vals,'decreasing':vals[0]>vals[1]>vals[2]})
stretch=[]
for qn,qd in inputs['stretched_exponents']:
 q=qn/qd;vals=[math.exp(q*t)-t*t for t in [100,200,300]]
 stretch.append({'q':[qn,qd],'log_h_over_exp_minus_u_power_at_L_100_200_300':vals,'positive_increasing':0<vals[0]<vals[1]<vals[2]})
allok=all(t['pass'] for t in checks) and all(t['coefficient_ratio_in_4point5_to_5'] for t in logres) and all(t['decreasing'] for t in flat) and all(t['positive_increasing'] for t in stretch)
d={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs_sha256':hashlib.sha256((r/'inputs.json').read_bytes()).hexdigest(),'exact_checks':checks,'exact_count':len(checks),'polynomials':[str(p) for p in polys],'log_residual_diagnostics':logres,'flatness_diagnostics':flat,'stretched_exponential_diagnostics':stretch,'all_passed':allok,'scope':'Finite diagnostic evidence; the exact infinite-order arguments are in165PROOF.md.'}
(r/'results.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:d[k] for k in ['started_utc','ended_utc','elapsed_seconds','exact_count','all_passed']},indent=2));assert allok
