"""Independent controls for packet128; polynomial, mp, FD and physical inverse."""
import sys,json,time,hashlib
from pathlib import Path
from datetime import datetime,timezone
from types import SimpleNamespace
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import least_squares
from horizontal_primitive_stream import (rows_from_terms,PrimitiveProblem,FreeBetaPrimitive,
    horizontal_nodes,stream_rows,matrices,projected,calculate,adaptive_primitive)
from free_beta_stream import make_chart
from stream_basis import evaluate_terms,combine
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative as fd

root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
start=time.perf_counter();result={'started_utc':datetime.now(timezone.utc).isoformat(),'checks':{}}
def save(name,value):
 result['checks'][name]=value;result['elapsed_seconds']=time.perf_counter()-start
 (root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(name,value,flush=True)
def error(a,b):return float(np.max(abs(np.asarray(a)-np.asarray(b))/(1+abs(np.asarray(b)))))
def polynomial_terms(expr,x,y):
 return {(i,j,0,0):float(v) for (i,j),v in sp.Poly(expr,x,y).terms()}

x,y,z=sp.symbols('x y z',real=True);points=np.array([[0.,0.],[0.,.6],[0.,-.7],[.3,.2],[-.4,.7],[1.2,-.9],[2.,.3]])
polychecks=[]
for beta in [sp.Rational(5,2),sp.Rational(7,2)]:
 a0=sp.Rational(1);c=1+beta/2;q=4*a0/beta
 P=c*x*y-q*x**3/6+sp.Rational(3,7)*x
 D=sp.Rational(17,100)*x*y**3+sp.Rational(7,100)*x**3*y+sp.Rational(1,100)*x**5
 psi=P+z*D;om=-sp.diff(psi,x,2)-sp.diff(psi,y,2)
 W1=beta*x-sp.diff(psi,y);W2=beta*y+sp.diff(psi,x)-sp.diff(psi,x).subs({x:0,y:0})
 F=sp.expand(W1*sp.diff(om,x)+W2*sp.diff(om,y)+om)
 th=sp.integrate(F,x);th=sp.expand(th-th.subs(x,0));RF=sp.cancel((W1*sp.diff(th,x)+W2*sp.diff(th,y)-(beta-2)*th)/x**2)
 assert sp.expand(F-sp.diff(th,x))==0
 assert sp.expand(th.subs(z,0)-a0*x*x)==0 and sp.expand(RF.subs(z,0))==0
 S=sp.cancel(th/x**2);H=sp.cancel(F/x)
 b=SimpleNamespace(beta=float(beta),s=float(1/beta),a0=1.,Cbase=np.array([1.,0.]),Cnull=np.array([[0.],[1.]]))
 rows=rows_from_terms([polynomial_terms(P,x,y),polynomial_terms(D,x,y)],b.s)
 case=PrimitiveProblem(b,points,32,'linear',rows=rows)
 for zz in [0.,.4,-.3]:
  f=case.fields(np.array([zz]),True);e={}
  for key,ex in [('H',H),('Hy',sp.diff(H,y)),('S',S),('Sy',sp.diff(S,y)),('RF',RF),('JR',sp.diff(RF,z))]:
   v=sp.lambdify((x,y,z),ex,'numpy')(points[:,0],points[:,1],zz)
   e[key]=error(f[key].ravel(),np.broadcast_to(v,(len(points),)))
  assert max(e.values())<2e-12,e
  polychecks.append({'beta':str(beta),'z':zz,'relative_errors':e})
 # Forced recovery is a numerical solver test, not a homogeneous profile.
 truth=np.array([.37]);target=case.residual(truth)
 fit=least_squares(lambda a:case.residual(a)-target,np.array([-.11]),jac=case.jacobian,max_nfev=60,gtol=1e-12,xtol=1e-12,ftol=1e-12)
 assert abs(fit.x[0]-.37)<1e-9
 polychecks.append({'forced_fit_error':float(abs(fit.x[0]-.37)),'nfev':fit.nfev})
save('exact_symbolic_polynomial_controls',polychecks)

rng=np.random.default_rng(128);jchecks=[]
for beta in [2.2,2.5,3.5]:
 b=make_chart(beta,2,3);v=rng.normal(size=b.nc)*.017;direction=rng.normal(size=b.nc);direction/=np.linalg.norm(direction)
 case=PrimitiveProblem(b,points,24,'sinh');h=2e-4
 d=(-case.residual(v+2*h*direction)+8*case.residual(v+h*direction)-8*case.residual(v-h*direction)+case.residual(v-2*h*direction))/(12*h)
 err=error(case.jacobian(v)@direction,d);assert err<2e-8,err
 free=FreeBetaPrimitive(2,3,points,beta,24);zz=np.r_[beta,v];hb=3e-4
 db=(-free.residual(zz+np.r_[2*hb,np.zeros(b.nc)])+8*free.residual(zz+np.r_[hb,np.zeros(b.nc)])-8*free.residual(zz-np.r_[hb,np.zeros(b.nc)])+free.residual(zz-np.r_[2*hb,np.zeros(b.nc)]))/(12*hb)
 eb=error(free.jacobian(zz)[:,0],db);assert eb<2e-7,eb
 f=case.fields(v);assert abs(f['S'][0]-1)<2e-11
 jchecks.append({'beta':beta,'C_directional_relative_error':err,'beta_column_relative_error':eb})
save('five_point_coefficient_derivatives',jchecks)

# Direct Chebyshev definition, independent of monomial spatial differentiation.
mp.mp.dps=45;b=make_chart(2.5,3,4);index=b.labels.index((2,3,1));rr=stream_rows(b)[index]
bb=mp.mpf('2.5');ss=1/bb
fpsi=lambda xx,yy:xx*(1+xx*xx+yy*yy)**(-ss/2)*mp.chebyt(2,2*(1+xx*xx+yy*yy)**(-ss/2)-1)*mp.chebyt(3,yy/mp.sqrt(1+xx*xx+yy*yy))
om=lambda xx,yy:-mp.diff(fpsi,(xx,yy),(2,0))-mp.diff(fpsi,(xx,yy),(0,2))
mpchecks=[]
for xx,yy in [('0','.7'),('.31','-.42')]:
 xx,yy=mp.mpf(xx),mp.mpf(yy)
 if xx==0:
  vals={'Q':mp.diff(om,(xx,yy),(1,0)),'Qx':mp.mpf(0),'Qy':mp.diff(om,(xx,yy),(1,1)),
        'Qxy':mp.mpf(0),'Qyy':mp.diff(om,(xx,yy),(1,2))}
 else:
  fq=lambda a,b:om(a,b)/a
  vals={k:mp.diff(fq,(xx,yy),ij)for k,ij in [('Q',(0,0)),('Qx',(1,0)),('Qy',(0,1)),('Qxy',(1,1)),('Qyy',(0,2))]}
 vals.update(av=-mp.diff(fpsi,(xx,yy),(1,1))if xx==0 else -mp.diff(fpsi,(xx,yy),(0,1))/xx,
     bv=mp.diff(fpsi,(xx,yy),(1,0))-mp.diff(fpsi,(mp.mpf(0),mp.mpf(0)),(1,0)))
 errs={k:error(evaluate_terms(rr[k],float(xx),float(yy),b.s),float(v))for k,v in vals.items()}
 assert max(errs.values())<2e-10,errs
 mpchecks.append({'point':[str(xx),str(yy)],'errors':errs})
save('direct_chebyshev_45digit_derivatives',mpchecks)

# An explicitly resolved Gaussian core has a closed primitive, independently of PDE data.
core=[]
for rad in [1.,100.,1e8]:
 row={'x':rad,'exact_scaled_primitive':float(-np.expm1(-rad*rad)/2)}
 for rule in ['linear','sinh']:
  for order in [16,32,64,128]:
   nodes,w=horizontal_nodes([[rad,0.]],order,rule);v=float(np.sum(w.ravel()*np.exp(-nodes[:,0]**2))*rad*rad)
   row[f'{rule}_{order}']=v
 assert abs(row['sinh_128']-row['exact_scaled_primitive'])<2e-8,row
 core.append(row)
assert core[-1]['linear_128']==0
save('missed_core_and_quadrature_refinement',core)
for tiny in [0.,1e-300,-1e-300,1e-10,-1e-10]:
 _,ww=horizontal_nodes([[tiny,.2]],32,'sinh');assert abs(ww.sum()-.5)<2e-14
save('smooth_quadrature_axis_limit',{'x_values':[0.,1e-300,-1e-300,1e-10,-1e-10],'weight_sum':.5})

b=make_chart(2.5,2,3);v=rng.normal(size=b.nc)*.009;C=b.Cbase+b.Cnull@v
qp=np.array([[0.,.6],[.71,-.32],[7.3,1.2],[103.,-2.1]])
adapt=adaptive_primitive(b,C,qp,eps=2e-11);qchecks=[]
for order in [16,32,64]:
 case=PrimitiveProblem(b,qp,order,'sinh');f=case.fields(v)
 row={'order':order,'S_relative_error':error(f['S'],[q['S']for q in adapt]),'Sy_relative_error':error(f['Sy'],[q['Sy']for q in adapt])};qchecks.append(row)
assert max(qchecks[-1]['S_relative_error'],qchecks[-1]['Sy_relative_error'])<2e-8,qchecks
save('adaptive_primitive_comparison',{'comparisons':qchecks,'adaptive_values':adapt})

# Differentiate the computed quadrature temperature, including moving nodes.
fp=np.array([[.13,.29],[.71,-.32],[2.3,1.2],[17.,-2.1]])
def temp(xx,yy):
 shape=np.broadcast_shapes(np.shape(xx),np.shape(yy));xx,yy=np.broadcast_arrays(xx,yy)
 c=PrimitiveProblem(b,np.column_stack((xx.ravel(),yy.ravel())),64,'sinh')
 return c.fields(v)['Theta'].reshape(shape)
e=PrimitiveProblem(b,fp,64,'sinh').fields(v);fdchecks=[]
for step in [2e-3,1e-3]:
 tx=fd(temp,fp,0,step,order=1,radius=3);ty=fd(temp,fp,1,step,order=1,radius=3)
 rg=fp[:,0]*e['H']-tx
 rt=fp[:,0]*e['A']*tx+e['B']*ty-(b.beta-2)*e['Theta']
 row={'step':step,'vorticity_absolute_max':float(abs(rg).max()),'thermal_independent_relative_error':error(rt,fp[:,0]**2*e['RF']),
      'Theta_y_relative_error':error(ty,e['Theta_y'])};fdchecks.append(row)
assert fdchecks[-1]['vorticity_absolute_max']<3e-7 and fdchecks[-1]['thermal_independent_relative_error']<3e-7,fdchecks
save('seven_point_Cartesian_temperature_derivatives',fdchecks)

ip=np.array([[.4,-.7],[1.1,.3],[0.,.8]])
prepared=b.prepare(ip);target=np.column_stack((prepared['psi']['U1']@C,prepared['psi']['U2']@C));inverses=[]
for rad,order in [(8.,24),(12.,40),(18.,56)]:
 inv=CartesianInverse(b.omega_callable(C),InverseSettings(radius=rad,core_radial_order=order//2,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/b.beta))
 actual=inv.relative(ip);err=float(abs(actual-target).max());inverses.append({'radius':rad,'order':order,'max_absolute_velocity_error':err})
assert inverses[-1]['max_absolute_velocity_error']<3e-7,inverses
save('independent_Duffy_full_plane_inverse',inverses)
result['status']='ALL_CONTROLS_PASSED';result['ended_utc']=datetime.now(timezone.utc).isoformat();result['elapsed_seconds']=time.perf_counter()-start
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n')
print('ALL_CONTROLS_PASSED',result['elapsed_seconds'],flush=True)
