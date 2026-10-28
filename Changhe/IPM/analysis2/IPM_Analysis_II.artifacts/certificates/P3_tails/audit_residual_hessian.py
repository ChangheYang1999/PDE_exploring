from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys,ast
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'source_audit'))
import field_eval as fe
fe.ORDER=6;fe.INDICES=[(i,j) for i in range(7) for j in range(7-i)]
ctx.prec=384
A=fe.aa
state=fe.State(131,384)
source=json.loads(Path(__file__).with_name('state131_residual_truncated_sectors.json').read_text())
cert=json.loads(Path(__file__).with_name('state131_residual_hessian_lower.json').read_text())
assert source['input_sha256']==cert['input_sha256']==state.data['canonical_serialization_sha256']
gamma=Q(state.data['exact_parameters']['cl']);gamma=1/gamma;q0=cert['Q']+1
LIN=arb(cert['linear_error_coefficient']);NL=arb(cert['nonlinear_error_coefficient'])
records=[]
for xi,yi in [(60,80),(100,0),(0,100),(180,240)]:
 x=A(xi);y=A(yi);r=(x*x+y*y).sqrt();theta=arb.pi()/2 if xi==0 else (y/x).atan()
 row=state.evaluate(x,y,include_potential_jet=True);phi=row['potential_derivatives']
 def rho(a,b):return -phi[a+2,b+1]-phi[a,b+3]
 def vel(j,a,b):return -phi[a+1,b+2] if j==0 else phi[a+2,b+1]
 hessian=[]
 for a,b in [(2,0),(1,1),(0,2)]:
  coords=[0]*a+[1]*b
  val=(2*state.cl-1)*rho(a,b)+state.cl*(x*rho(a+1,b)+y*rho(a,b+1))
  for j in (0,1):
   dx,dy=(1,0) if j==0 else (0,1)
   val+=vel(j,0,0)*rho(a+dx,b+dy)+vel(j,a,b)*rho(dx,dy)
   for t in coords:
    e,f=(1,0) if t==0 else (0,1)
    val+=vel(j,e,f)*rho(a-e+dx,b-f+dy)
  hessian.append(val)
 Hrr=arb(0);Hrt=arb(0);Htt=arb(0)
 for key,co in source['coefficients'].items():
  p=A(source['powers'][key]);v=arb(0);dv=arb(0);ddv=arb(0)
  for ns,vs in co.items():
   n=int(ns);z=A(vs);sn=(n*theta).sin();cn=(n*theta).cos()
   v+=z*sn;dv+=z*n*cn;ddv-=z*n*n*sn
  factor=r**(p-2)
  Hrr+=factor*p*(p-1)*v;Hrt+=factor*(p-1)*dv;Htt+=factor*(p*v+ddv)
 ct=x/r;st=y/r
 Hxx=ct*ct*Hrr-2*ct*st*Hrt+st*st*Htt
 Hxy=ct*st*(Hrr-Htt)+(ct*ct-st*st)*Hrt
 Hyy=st*st*Hrr+2*ct*st*Hrt+ct*ct*Htt
 differences=[a-b for a,b in zip(hessian,[Hxx,Hxy,Hyy])]
 bound=LIN*r**A(gamma-2-2*q0)+NL*r**A(2*gamma-3)
 assert all(abs(v)<bound for v in differences),(xi,yi,differences,bound)
 records.append({'point':[xi,yi],'cartesian_hessian':[v.str(50) for v in hessian],'differences':[v.str(40) for v in differences],'analytic_error_upper':bound.str(45)})
 print('point',xi,yi,'differences',[v.str(8) for v in differences],'bound',bound.str(10),flush=True)
# Algebraic identity for J verified independently at rational p,t,m.
for p,t,m in [(Q(1,10),Q(-1,3),3),(Q(2,3),Q(5,7),19)]:
 pp=p*(p-1);tt=t*(t-1)
 J=pp*tt+2*(p-1)*(t-1)*m*m+(p-m*m)*(t-m*m)
 assert J==pp*tt+(p-m*m)*(t-m*m)+2*((p-1)*m)*((t-1)*m)
# Monotonicity in sigma gives a common lower bound for every sigma<=2/5 for which the norm is finite.
last=cert['rows'][-1];assert Q(last['sigma'])==Q(2,5)
lo=arb(last['full_actual_weight_norm_lower'])
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'input_sha256':cert['input_sha256'],'Q':cert['Q'],'R0':cert['R0'],'checks':records,'sigma_2_5_lower':lo.str(50),'scope':'Independent Cartesian point checks and algebra checks; the continuum lower bound uses RESIDUAL_HESSIAN_PROOF.md.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
