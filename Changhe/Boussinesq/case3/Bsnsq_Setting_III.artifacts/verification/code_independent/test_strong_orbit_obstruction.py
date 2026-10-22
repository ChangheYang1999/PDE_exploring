"""Exact local controls and counterexamples for the independently written179."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import sympy as s
r=Path('research/179_strong_unstable_neighborhood_obstruction/verification');data=json.loads((r/'inputs.json').read_text());start=time.monotonic();now=datetime.now(timezone.utc).isoformat();rows=[];negative=[]
x,y,t,u0,v0,alpha,k=s.symbols('x y t u0 v0 alpha k',real=True);T=s.symbols('T',nonnegative=True)
def check(name,e):
 z=s.simplify(e);rows.append({'name':name,'difference':str(z),'pass':z==0});assert z==0,(name,z)
def system(W1,W2,theta,omega):
 return [s.diff(W1,x)+s.diff(W2,y)-4,omega+s.diff(W2,x)-s.diff(W1,y),W1*s.diff(theta,x)+W2*s.diff(theta,y),W1*s.diff(omega,x)+W2*s.diff(omega,y)+omega-s.diff(theta,x)]
# This coupled local model is the important exception to harmonic=>constant Theta.
for d in data['thermal_powers']:
 for j,e in enumerate(system(4*x,0,y**d,0)):check(f'local_exception_thermal_degree{d}_eq{j}',e)
 assert s.diff(y**d,y)!=0
 negative.append({'name':f'harmonic_field_does_not_force_constant_temperature_degree{d}','W':['4*x','0'],'Theta':str(y**d),'Omega':'0','pass':True,'scope':'Coupled local example only; no compact zero arc, no B2 jet or broad far-field condition.'})
# Even coupled analyticity alone does not imply Omega=0 without the open zero side.
for kval in data['shear_parameters']:
 kv=s.Rational(kval);W1=0;W2=kv*x+4*y;omega=-kv;theta=-kv*x
 for j,e in enumerate(system(W1,W2,theta,omega)):check(f'analytic_nonzero_curl_k{kval}_eq{j}',e)
 negative.append({'name':f'analytic_velocity_can_have_nonzero_vorticity_k{kval}','W':[str(W1),str(W2)],'Theta':str(theta),'Omega':str(omega),'pass':True,'scope':'Coupled local example, but not B2 parity, center jet, compact arc or sublinear correction.'})
# Exact coordinate-model projection; no claim this coordinate field is a B2 profile.
for aval in data['projection_parameters']:
 a=s.Rational(aval);v=v0*s.exp(-4*T);I=a*v0*(1-s.exp(-4*T))/4;u=u0*s.exp(-I);P=u0*s.exp(-a*v0/4)
 check(f'projection_v_ODE_{aval}',s.diff(v,T)+4*v)
 check(f'projection_u_ODE_{aval}',s.diff(u,T)+a*u*v)
 check(f'projection_Iprime_{aval}',s.diff(I,T)-a*v)
 check(f'projection_tail_{aval}',a*v0/4-I-a*v0*s.exp(-4*T)/4)
 check(f'projection_limit_{aval}',s.limit(u,T,s.oo)-P)
 check(f'projection_nonzero_factor_{aval}',P/u0-s.exp(-a*v0/4))
# Div-curl identities used to produce harmonic components.
f=s.Function('f')(x,y);g=s.Function('g')(x,y);div=s.diff(f,x)+s.diff(g,y);curl=s.diff(g,x)-s.diff(f,y)
check('laplacian_W1_divcurl',s.diff(f,x,2)+s.diff(f,y,2)-s.diff(div,x)+s.diff(curl,y))
check('laplacian_W2_divcurl',s.diff(g,x,2)+s.diff(g,y,2)-s.diff(div,y)-s.diff(curl,x))
# The forced affine exceptional field has a full vertical zero line.
px,py,q=s.symbols('px py q',real=True);W1=4*(x-px);W2=0
check('exceptional_zero_ray_plus',W1.subs({x:px,y:py+q}))
check('exceptional_zero_ray_minus',W1.subs({x:px,y:py-q}))
check('exceptional_divergence',s.diff(W1,x)+s.diff(W2,y)-4)
check('exceptional_curl',s.diff(W2,x)-s.diff(W1,y))
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':rows,'negative_controls':negative,'passed':len(rows),'negative_passed':len(negative),'all_passed':all(x['pass']for x in rows+negative),'scope':'Exact local formulas and necessity controls; no formal global topological proof and no B2 candidate.'}
(r/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in ('checks','negative_controls')},indent=2))
