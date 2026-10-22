"""Independent exact identities and finite area-preserving manufactured controls.

The analytic proof was written first in research/143_compact_thermal_deformations.
This script evaluates the defining equations directly and derives the formal
adjoint from the coefficients of the linearized differential operator.
"""
from pathlib import Path
import sys,time,datetime,json
import sympy as S
import numpy as np
from numpy.polynomial.legendre import leggauss
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic();checks=[]
x,y,b,a=S.symbols('x y beta a',real=True);q=4*a/b;k=b-2;l1=k/2;l2=1+3*b/2
W=S.Matrix([l1*x,l2*y-q*x*x/2]);eta=S.Function('eta')(x,y);p=S.Function('p')(x,y)
adv=lambda f:sum(W[i]*S.diff(f,z) for i,z in enumerate([x,y]))
perp=lambda f:S.Matrix([-S.diff(f,y),S.diff(f,x)])
Lap=lambda f:S.diff(f,x,2)+S.diff(f,y,2)
zero=lambda name,v:checks.append({'name':name,'pass':S.cancel(S.expand(v))==0})
Theta=a*x*x;Omega=q*x
zero('background_T',adv(Theta)-k*Theta)
zero('background_V',adv(Omega)+Omega-S.diff(Theta,x))
zero('background_div',S.diff(W[0],x)+S.diff(W[1],y)-2*b)
chi=adv(eta)-2*b*eta;tau=-sum(perp(eta)[i]*S.diff(Theta,z) for i,z in enumerate([x,y]));h=perp(eta);dv=perp(chi)
tdirect=adv(tau)-k*tau+sum(dv[i]*S.diff(Theta,z) for i,z in enumerate([x,y]))
zero('thermal_direct',tdirect)
comm=h.jacobian([x,y])*W-W.jacobian([x,y])*h
for j in [0,1]:zero('pushforward_component_'+str(j),dv[j]-comm[j])
f=-adv(Lap(chi))-Lap(chi)+sum(dv[i]*S.diff(Omega,z) for i,z in enumerate([x,y]))-S.diff(tau,x)
L=lambda f:-(adv(Lap(adv(f)-2*b*f))+Lap(adv(f)-2*b*f))-q*S.diff(adv(f)-2*b*f,y)-2*a*S.diff(x*S.diff(f,y),x)
zero('direct_vorticity_L',f-L(eta))
# Derive adjoint by its differential coefficients, independently of the proof formula.
expanded=S.expand(f);adj=0;coefficients=[]
for i in range(5):
 for j in range(5-i):
  jet=S.diff(eta,x,i,y,j);c=expanded.coeff(jet)
  if c!=0:
   adj+=(-1)**(i+j)*S.diff(c*p,x,i,y,j);coefficients.append((i,j,str(S.factor(c))))
lstar=lambda f:adv(Lap(-adv(f)+(1-2*b)*f))+4*b*Lap(-adv(f)+(1-2*b)*f)-q*(adv(S.diff(f,y))+4*b*S.diff(f,y))-2*a*x*S.diff(f,x,y)
zero('adjoint_from_independent_coefficients',adj-lstar(p))
for name,z in [('1',S.Integer(1)),('x',x),('y',y)]:zero('affine_weight_'+name,lstar(z))
p0=x*y/(x*x+y*y)**2
zero('singular_weight_at_y0',lstar(p0).subs(y,0)+3*q*(17*b+28)/(2*x**3))
# A source with nonzero vertical integral cannot lie in the compact thermal kernel.
T=S.Function('T')(x)
zero('integrated_y_ODE_coefficients',l1*x*S.diff(T,x)-(l2+k)*T-((b-2)*x*S.diff(T,x)-(5*b-2)*T)/2)
# Compactly supported test eta can be any sufficiently smooth bump; polynomial
# generators test independent derivatives and special beta2 without smoothness claims.
for beta0 in [S.Integer(2),S.Rational(9,4),S.Rational(7,2)]:
 for sign in [1,-1]:
  g=x*(1+2*x*x-y+3*y*y+x*x*y**3)
  dg=L(g).subs({b:beta0,a:sign});cg=(adv(g)-2*b*g).subs({b:beta0,a:sign});tg=(2*a*x*S.diff(g,y)).subs({b:beta0,a:sign})
  wg=W.subs({b:beta0,a:sign});ag=lambda z:sum(wg[i]*S.diff(z,t) for i,t in enumerate([x,y]))
  zero(f'finite_polynomial_T_beta{beta0}_a{sign}',ag(tg)-(beta0-2)*tg-2*sign*x*S.diff(cg,y))
  zero(f'finite_polynomial_V_beta{beta0}_a{sign}',dg+ag(Lap(cg))+Lap(cg)+(4*sign/beta0)*S.diff(cg,y)+S.diff(tg,x))
# Finite nonlinear area-preserving twist in two disks. All quantities are computed
# from the inverse coordinate map and its explicit Jacobian, not from residual formula L.
numeric=[]
for beta0,a0 in [(2.,1.),(2.5,1.),(3.5,-1.)]:
 for n in [24,36,52]:
  g,w=leggauss(n);rr=.45*(g+1)/2;wr=.45*w/2;angles=2*np.pi*(np.arange(128)+.37)/128
  rad,ang=np.meshgrid(rr,angles,indexing='ij');weights=np.broadcast_to(wr[:,None]*rad*(2*np.pi/128),rad.shape).ravel()
  defects=np.zeros(6);maxthermal=0.;maxdet=0.;maxchange=0.
  for mirror in [1.,-1.]:
   center=np.array([mirror*1.3,.4]);r=rad.ravel();theta=ang.ravel();alpha=mirror*.7*(1-r*r/.45**2)**8
   alphapr=-mirror*.7*16*r/.45**2*(1-r*r/.45**2)**7
   # X are integration points; Y=Phi^{-1}(X).
   Y=center+np.column_stack([r*np.cos(theta-alpha),r*np.sin(theta-alpha)])
   X=center+np.column_stack([r*np.cos(theta),r*np.sin(theta)])
   z=Y-center;Jz=np.column_stack([-z[:,1],z[:,0]])
   rot=np.empty((len(r),2,2));rot[:,0,0]=np.cos(alpha);rot[:,0,1]=-np.sin(alpha);rot[:,1,0]=np.sin(alpha);rot[:,1,1]=np.cos(alpha)
   inside=np.eye(2)[None,:,:]+(alphapr/r)[:,None,None]*Jz[:,:,None]*z[:,None,:]
   DP=np.einsum('nij,njk->nik',rot,inside)
   w0=np.column_stack([(beta0-2)*Y[:,0]/2,(1+1.5*beta0)*Y[:,1]-(2*a0/beta0)*Y[:,0]**2])
   w1=np.einsum('nij,nj->ni',DP,w0)
   grad0=np.column_stack([2*a0*Y[:,0],np.zeros(len(Y))])
   grad1=np.linalg.solve(np.swapaxes(DP,1,2),grad0[...,None])[...,0]
   th0=a0*X[:,0]**2;th1=a0*Y[:,0]**2
   residual=np.einsum('ni,ni->n',w1,grad1)-(beta0-2)*th1
   maxthermal=max(maxthermal,float(np.max(abs(residual))));maxdet=max(maxdet,float(np.max(abs(np.linalg.det(DP)-1))))
   maxchange=max(maxchange,float(np.max(abs(th1-th0))))
   for power in range(1,7):defects[power-1]+=np.sum(weights*(th1**power-th0**power))
  numeric.append({'beta':beta0,'a':a0,'radial_order':n,'angle_count':128,'max_abs_thermal_residual':maxthermal,'max_det_error':maxdet,'max_temperature_change':maxchange,'power_moment_differences':defects.tolist(),'pass':maxthermal<2e-12 and maxdet<2e-14 and max(abs(defects))<3e-11 and maxchange>.02})
# Necessary moments for linearized perturbations also detect a nonthermal perturbation.
for beta0 in [2.,2.5,3.5]:
 coeffs=[2*beta0+n*(beta0-2) for n in range(1,7)]
 checks.append({'name':f'positive_moment_coefficients_beta{beta0}','pass':min(coeffs)>0,'coefficients':coeffs})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_controls':checks,'operator_coefficients':coefficients,'nonlinear_compact_twist_controls':numeric,'all_pass':all(z['pass'] for z in checks+numeric),'scope':'Exact symbolic identities and sampled manufactured verification. No full cokernel, finite-support solvability, profile existence, or uniform numerical certification.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_pass':result['all_pass'],'exact_count':len(checks),'nonlinear_count':len(numeric),'elapsed_seconds':result['elapsed_seconds'],'max_moment_error':max(abs(t) for z in numeric for t in z['power_moment_differences'])},indent=2))
if not result['all_pass']:raise SystemExit(1)
