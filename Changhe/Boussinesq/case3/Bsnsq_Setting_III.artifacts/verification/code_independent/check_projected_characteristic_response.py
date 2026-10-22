"""P200 controls, independent of every numerics-lane implementation."""
from pathlib import Path
import json, time
from datetime import datetime, timezone
import numpy as np
import sympy as sp
from smooth_modal_flow import reconstruct

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/200_projected_characteristic_response/verification'

def now():return datetime.now(timezone.utc).isoformat()

def exact_values(X,k):
 x,y=np.asarray(X,dtype=float);v=k*x*x;u=1+v
 theta=x*x/u;g=np.array([2*x/u**2,0.])
 omega=0. if x==0 else 2/(5*k*x)*np.sqrt(u)*(-np.expm1(-2.5*np.log1p(v)))
 return theta,g,omega

def exact_derivatives(X,k):
 x,y=np.asarray(X,dtype=float);v=k*x*x;u=1+v
 bracket=-np.expm1(-2.5*np.log1p(v))
 domega=(0. if x==0 else 2/(5*x)*(-np.sqrt(u)*bracket/k**2+
          x*x*bracket/(2*k*np.sqrt(u))+2.5*x*x/(k*u**3)))
 return np.array([-x**4/u**2,-4*x**3/u**3,0.,domega])

class Manufactured:
 def __init__(self,k):self.k=k
 def W(self,X):
  x,y=X;k=self.k
  return np.array([x*(1+k*x*x),(7-3*k*x*x)*y])
 def DW(self,X):
  x,y=X;k=self.k
  return np.array([[1+3*k*x*x,0.],[-6*k*x*y,7-3*k*x*x]])

def values_vector(row):return np.array([row['Theta'],*row['gradient'],row['Omega']])

def main():
 start=now();clock=time.monotonic();x,y,k=sp.symbols('x y k',positive=True)
 u=1+k*x*x;W=sp.Matrix([x*u,(7-3*k*x*x)*y]);theta=x*x/u
 omega=2*sp.sqrt(u)/(5*k*x)*(1-u**(-sp.Rational(5,2)))
 checks={
 'divergence8':sp.simplify(sp.diff(W[0],x)+sp.diff(W[1],y)-8)==0,
 'temperature_transport':sp.simplify(W.dot(sp.Matrix([sp.diff(theta,x),0]))-2*theta)==0,
 'vorticity_transport':sp.simplify(W[0]*sp.diff(omega,x)+omega-sp.diff(theta,x))==0,
 'vorticity_leading_x':sp.limit(omega/x,x,0)==1,
 'minus_curl_not_source':sp.simplify(-sp.diff(W[1],x)-6*k*x*y)==0,
 'domega_k':sp.simplify(sp.diff(omega,k)-(2/(5*x)*(-sp.sqrt(u)*(1-u**(-sp.Rational(5,2)))/k**2+x*x*(1-u**(-sp.Rational(5,2)))/(2*k*sp.sqrt(u))+sp.Rational(5,2)*x*x/(k*u**3))))==0}
 phi=sp.symbols('phi',real=True)
 for n in range(10):
  angular=sp.integrate(sp.expand_trig(sp.sin(phi)**2*sp.cos(phi)*sp.cos(n*phi)),(phi,0,2*sp.pi))
  checks['strain_angular_mode_'+str(n)]=sp.simplify(angular-sp.pi/4*(int(n==1)-int(n==3)))==0
 t,b,L=sp.symbols('t b L',positive=True)
 r=L*sp.sqrt((1-t)**(-2*b)-1)
 # Verify the Jacobian through the squared radial identity to avoid branch ambiguity.
 dr=b*L**2/r*(1-t)**(-2*b-1)
 checks['radial_jacobian']=sp.simplify((1-t)**(b+1)*(r/L)*(1-t)**b*dr-b*L)==0
 z1,z2,cf,lam,cs=sp.symbols('z1 z2 cf lam cs',real=True)
 cv=sp.Matrix([2,-3]);z=sp.Matrix([z1,z2]);q=cv
 zp=z+q*(cs-cv.dot(z)-lam*cf)/cv.dot(q)
 checks['projected_total_strain']=sp.simplify(cv.dot(zp)+lam*cf-cs)==0
 checks['direction_total_strain']=sp.simplify(cv.dot(zp.diff(lam))+cf)==0
 rows=[];response=[]
 points=[[.2,.1],[.8,.4],[1.,1.],[-.7,.3],[.3,2.]]
 param=.2
 for point in points:
  target=np.r_[exact_values(point,param)[0],exact_values(point,param)[1],exact_values(point,param)[2]]
  for cutoff in [.01,.003,.001]:
   row=reconstruct(Manufactured(param),point,4.,1.,cutoff=cutoff,rtol=2e-12,atol=2e-14,
                   exact_seed=lambda X:exact_values(X,param))
   if row['status']!='COMPLETE':raise RuntimeError(row)
   row['exact']=target.tolist();row['absolute_errors']=np.abs(values_vector(row)-target).tolist()
   seed=np.array(row['seed_point']);row['outgoing_flux']=float(Manufactured(param).W(seed)@seed/np.linalg.norm(seed))
   rows.append(row)
  deriv_exact=exact_derivatives(point,param)
  for step in [2e-4,1e-4]:
   vv=[]
   for j in [-2,-1,1,2]:
    kk=param+j*step
    rr=reconstruct(Manufactured(kk),point,4.,1.,cutoff=.003,rtol=2e-12,atol=2e-14,
                  exact_seed=lambda X,kk=kk:exact_values(X,kk))
    vv.append(values_vector(rr))
   approx=(vv[0]-8*vv[1]+8*vv[2]-vv[3])/(12*step)
   response.append({'point':point,'step':step,'exact_derivative':deriv_exact.tolist(),
                    'finite_difference':approx.tolist(),'absolute_errors':np.abs(approx-deriv_exact).tolist()})
 # The correct finite-radius gradient differs from the uncorrected center jet.
 finite_seed=[]
 for compatible in [False,True]:
  rr=reconstruct(Manufactured(param),[.8,.4],4.,1.,cutoff=.03,rtol=2e-12,atol=2e-14,compatible_seed=compatible)
  finite_seed.append(rr)
 # Independent spatial differences of the finite-cutoff temperature check its reconstructed gradient.
 h=2e-5;grad=[]
 for axis in [0,1]:
  values=[]
  for j in [-2,-1,1,2]:
   point=np.array([.8,.4]);point[axis]+=j*h
   rr=reconstruct(Manufactured(param),point,4.,1.,cutoff=.03,rtol=2e-12,atol=2e-14,compatible_seed=True)
   values.append(rr['Theta'])
  grad.append((values[0]-8*values[1]+8*values[2]-values[3])/(12*h))
 gradient_comparison={'point':[.8,.4],'cutoff':.03,'spatial_difference':grad,
  'compatible_ODE_gradient':finite_seed[1]['gradient'],'uncorrected_ODE_gradient':finite_seed[0]['gradient'],
  'compatible_max_error':float(np.max(np.abs(np.array(grad)-finite_seed[1]['gradient']))),
  'uncorrected_max_error':float(np.max(np.abs(np.array(grad)-finite_seed[0]['gradient'])))}
 out={'started_utc':start,'ended_utc':now(),'elapsed_seconds':time.monotonic()-clock,
 'symbolic_checks':checks,'all_symbolic_passed':all(checks.values()),'exact_transport_tests':rows,
 'parameter_response_tests':response,'finite_radius_gradient_control':gradient_comparison,
 'max_exact_transport_error':max(max(r['absolute_errors']) for r in rows),
 'max_response_error':max(max(r['absolute_errors']) for r in response),
 'scope':'Manufactured scalar transport only, not inverse consistency, not B2 profile; all finite differences sampled.'}
 OUT.mkdir(parents=True,exist_ok=True);(OUT/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['exact_transport_tests','parameter_response_tests']},indent=2),flush=True)
 if not all(checks.values()):raise RuntimeError('symbolic failure')
 if out['max_exact_transport_error']>1e-7 or out['max_response_error']>1e-6:raise RuntimeError('manufactured error above diagnostic threshold')

if __name__=='__main__':main()
