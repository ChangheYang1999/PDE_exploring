from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,math
import numpy as np
from scipy.optimize import brentq
started=time.monotonic()
a=1/6;b=11/6;eps=.5;M=98

def theta0(u):return u+(a-b)/4*np.sin(2*u)
def uinverse(v):return brentq(lambda u:theta0(u)-v,v-1,v+1,xtol=1e-14,rtol=1e-14)
def angular(t):
 f=t+eps/M*np.sin(M*t);fp=1+eps*np.cos(M*t);fpp=-eps*M*np.sin(M*t)
 u=uinverse(f);D=a*np.cos(u)**2+b*np.sin(u)**2
 q=fp**(-a/2)*np.cos(u);g=fp**(-b/2)*np.sin(u)
 qp=-a/2*fpp/fp*q-fp**(-a/2)*np.sin(u)*fp/D
 gp=-b/2*fpp/fp*g+fp**(-b/2)*np.cos(u)*fp/D
 return q,g,qp,gp,u
def H(z):
 r=np.hypot(*z);t=np.arctan2(z[1],z[0]);q,g,*_=angular(t)
 return np.array([r**a*q,r**b*g])
angles=np.linspace(-np.pi,np.pi,2049)
values=np.array([angular(t) for t in angles])
q,g,qp,gp=values[:,:4].T
identity=a*q*gp-b*qp*g
parity=[]
for t in angles[::8]:
 z=np.array([np.cos(t),np.sin(t)]);hz=H(z);hreflect=H(z*np.array([-1,1]))
 parity.append(np.max(np.abs(hreflect-hz*np.array([-1,1]))))
fd=[]
for r in [.25,1.,17.]:
 for t in [-1.23,-.33,.27,np.pi/4,1.39,2.4]:
  z=r*np.array([np.cos(t),np.sin(t)]);step=2e-7*r
  jac=np.column_stack([(H(z+step*np.eye(2)[j])-H(z-step*np.eye(2)[j]))/(2*step) for j in range(2)])
  fd.append({'r':r,'theta':t,'det':float(np.linalg.det(jac)),'error':float(abs(np.linalg.det(jac)-1))})
q0,g0,qp0,gp0,u0=angular(np.pi/4)
out={'written_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'parameters':{'alpha':a,'gamma':b,'epsilon':eps,'M':M},'theta_star':float(np.pi/4),'u_star':float(u0),'u_bounds':[float(np.pi/3),float(5*np.pi/12)],'q_star':float(q0),'qprime_over_q':float(qp0/q0),'exact_lower_bound':155/132,'bracket_at_star':float((a*q0-qp0)/np.sqrt(2)),'max_algebraic_area_error':float(np.max(np.abs(identity-1))),'max_reflection_error':float(max(parity)),'max_cartesian_FD_determinant_error':max(v['error'] for v in fd),'cartesian_FD':fd,'scope':'Numerical diagnostic for a geometry-only example. Exact global bijectivity, area identity, and strict negative bracket are proved in PROOF.md. No B2 profile claimed.'}
out['passed']=bool(np.pi/3<u0<5*np.pi/12 and qp0/q0>155/132 and out['bracket_at_star']<0 and out['max_algebraic_area_error']<1e-12 and out['max_reflection_error']<1e-11 and out['max_cartesian_FD_determinant_error']<1e-5)
root=Path('research/66_global_temperature_tail_geometry/verification');(root/'counterexample_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='cartesian_FD'},indent=2));assert out['passed']
