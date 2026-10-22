"""Independent symbolic and Cartesian-FD audit of packet100, no lane imports."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,resource
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
import sympy as s
import numpy as np
from scipy.optimize import brentq
from finite_difference import derivative
root=Path('research/100_mixed_chart_verification/verification')
start=time.monotonic(); out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','exact':{},'fd':[]}
q,y,be,ka=s.symbols('q y beta kappa',real=True)
la=be/2-1;mu=3*be/2+1
S=s.Function('S')(q,y)
J=s.diff(S,q,y);Sy2=s.diff(S,y,2)
# h(q) generalizes kappa q^k; use an independently integrated primitive.
h=s.Function('h')(q);I=s.Function('I')(q)
B=(mu*s.diff(S,q)+h-la*q*s.diff(S,q,2))/J
Wx=la*q*J+Sy2*B
Psi=2*be*S-la*q*s.diff(S,q)-be*y*s.diff(S,y)+I
Dx=lambda f:s.diff(f,q)/J
Dy=lambda f:s.diff(f,y)-Sy2*s.diff(f,q)/J
L=lambda f:la*q*s.diff(f,q)+B*s.diff(f,y)
checks={'divergence':Dx(Wx)+Dy(B)-2*be,
        'vertical_inverse':Dx(Psi)-B+be*y,
        'horizontal_inverse':-Dy(Psi)-Wx+be*s.diff(S,y),
        'temperature':L(q*q)-(be-2)*q*q,
        'eta_flow':L(s.diff(S,q))-mu*s.diff(S,q)-h,
        'area_jacobian':Dx(q)*Dy(s.diff(S,q))-Dy(q)*Dx(s.diff(S,q))-1}
for key,e in checks.items():
 v=s.simplify(e.subs(s.diff(I,q),h));out['exact'][key]=str(v);assert v==0,(key,v)
for k in (4,6,8,10,12,20):
 b=s.Rational(2)+s.Rational(8,k-3)
 for key,e in [('stream_kernel',2*be-la*(k+1)),('flow_kernel',mu-la*k)]:
  v=s.simplify(e.subs(be,b));assert v==0;out['exact'][f'{key}_k{k}']=str(v)
# Known exact PDE manufacture; it is excluded by non-sublinear velocity.
a0=s.Rational(7,5);d=4*a0/(be*(be+6))
Pm=q*y-d*q**3/3
jm=s.diff(Pm,q,y); bm=mu*s.diff(Pm,q)-la*q*s.diff(Pm,q,2)
wm=s.Matrix([la*q,bm]);om=-s.diff(bm,q)
rr=la*q*s.diff(om,q)+bm*s.diff(om,y)+om-2*a0*q
for key,e in [('polynomial_vorticity_residual',rr),('polynomial_center_jet',s.diff(om,q)-4*a0/be)]:
 v=s.factor(e);assert v==0;out['exact'][key]=str(v)
# Global proper positive-J chart, deliberately NOT a sublinear B2 profile.
P=q*(y+y**3/s.Integer(21))+q**3*y/s.Integer(11)+q**5/s.Integer(37)
x=s.diff(P,y);JJ=s.diff(P,q,y);YY=s.diff(P,y,2)
for b,k,kval in [(s.Integer(3),4,s.Integer(0)),(s.Integer(10),4,s.Rational(2,7))]:
 ll=b/2-1;mm=3*b/2+1
 BB=(mm*s.diff(P,q)+kval*q**k-ll*q*s.diff(P,q,2))/JJ
 WW=ll*q*JJ+YY*BB
 PP=2*b*P-ll*q*s.diff(P,q)-b*y*s.diff(P,y)+kval*q**(k+1)/(k+1)
 px=lambda f:s.diff(f,q)/JJ
 py=lambda f:s.diff(f,y)-YY*s.diff(f,q)/JJ
 OM=-px(BB)+py(WW)
 RES=ll*q*s.diff(OM,q)+BB*s.diff(OM,y)+OM-2*q/JJ
 symbols=[x,JJ,WW,BB,PP,OM,RES,2*q/JJ]
 fn=s.lambdify((q,y),symbols,'numpy',cse=True)
 def values(xv,yv):
  xv,yv=np.broadcast_arrays(np.asarray(xv,dtype=float),np.asarray(yv,dtype=float));qs=[]
  for a,bb in zip(xv.ravel(),yv.ravel()):
   scale=max(1.,abs(a));qs.append(brentq(lambda z:z*(1+bb*bb/7)+z**3/11-a,-scale,scale,xtol=5e-15,rtol=1e-15))
  qs=np.array(qs).reshape(xv.shape)
  vals=fn(qs,yv)
  return np.array([np.broadcast_to(v,xv.shape) for v in vals]),qs
 points=np.array([[.17,-.41],[.53,.72],[1.11,-.34],[.79,1.07],[0.,.51],[-.53,.72]])
 vals,qs=values(*points.T)
 for step in (.04,.02,.01):
  dxpsi=derivative(lambda xx,yy:values(xx,yy)[0][4],points,0,step)
  dypsi=derivative(lambda xx,yy:values(xx,yy)[0][4],points,1,step)
  dxw=derivative(lambda xx,yy:values(xx,yy)[0][2],points,0,step)
  dyw=derivative(lambda xx,yy:values(xx,yy)[0][3],points,1,step)
  dxom=derivative(lambda xx,yy:values(xx,yy)[0][5],points,0,step)
  dyom=derivative(lambda xx,yy:values(xx,yy)[0][5],points,1,step)
  dxt=derivative(lambda xx,yy:values(xx,yy)[1]**2,points,0,step)
  dyt=derivative(lambda xx,yy:values(xx,yy)[1]**2,points,1,step)
  residual=vals[2]*dxom+vals[3]*dyom+vals[5]-dxt
  out['fd'].append({'beta':float(b),'kappa':float(kval),'step':step,
   'inverse_error':float(max(np.max(abs(dxpsi-(vals[3]-float(b)*points[:,1]))),np.max(abs(-dypsi-(vals[2]-float(b)*points[:,0]))))),
   'divergence_error':float(np.max(abs(dxw+dyw-2*float(b)))),
   'temperature_error':float(np.max(abs(vals[2]*dxt+vals[3]*dyt-(float(b)-2)*qs**2))),
   'vorticity_residual_agreement':float(np.max(abs(residual-vals[6]))),
   'J_min':float(vals[1].min()),'PDE_residual_max':float(abs(vals[6]).max())})
  print(out['fd'][-1],flush=True)
 # Nonzero kappa necessarily needs the extra stream term.
 if kval:
  defect=s.simplify(px(PP-kval*q**(k+1)/(k+1))-BB+b*y+kval*q**k/JJ)
  assert defect==0;out['exact']['omitted_resonance_defect']='-kappa*q^k/J (vertical velocity)'
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
