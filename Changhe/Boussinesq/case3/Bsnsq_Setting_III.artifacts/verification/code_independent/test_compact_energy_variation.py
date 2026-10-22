"""Own direct finite twist and symbolic variational controls for proof152.
No NUM or lead code is imported. Polynomial patches are manufactured controls,
not admissible full-plane profiles; the finite compact energy difference is real.
"""
from pathlib import Path
from datetime import datetime, timezone
import sys,time,json,hashlib
import sympy as S
import numpy as np
from numpy.polynomial.legendre import leggauss
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic();rows=[]
x,y,beta,a=S.symbols('x y beta a',real=True); coords=(x,y)
psi=S.Function('psi')(x,y);theta=S.Function('theta')(x,y);h=S.Function('h')(x,y)
grad=lambda u:S.Matrix([S.diff(u,z) for z in coords])
J=lambda u:S.Matrix([-S.diff(u,y),S.diff(u,x)])
lap=lambda u:S.diff(u,x,2)+S.diff(u,y,2)
W=beta*S.Matrix([x,y])+J(psi);om=-lap(psi);H=J(h)
adv=lambda u:(W.dot(grad(u)))
chi=adv(h)-2*beta*h;tau=-H.dot(grad(theta))
def check(name,v):
 z=S.cancel(S.expand(v));rows.append({'name':name,'pass':z==0})
 if z!=0:rows[-1]['defect']=str(z)
comm=H.jacobian(coords)*W-W.jacobian(coords)*H
for j in range(2):check('general_pushforward_'+str(j),comm[j]-J(chi)[j])
check('general_constant_divergence',sum(S.diff(W[i],coords[i]) for i in range(2))-2*beta)
t=adv(theta)-(beta-2)*theta
check('thermal_residual_covariance',adv(tau)+J(chi).dot(grad(theta))-(beta-2)*tau+H.dot(grad(t)))
# Derive compact variational derivative by extracting every h jet from the
# direct energy variation density, independently of the proposed formula.
def adjoint_density(density,maxorder):
 density=S.expand(density);out=S.Integer(0);remainder=density
 for i in range(maxorder+1):
  for j in range(maxorder+1-i):
   jet=S.diff(h,x,i,y,j);c=density.coeff(jet)
   out+=(-1)**(i+j)*S.diff(c,x,i,y,j);remainder-=c*jet
 check('jet_extraction_order'+str(maxorder)+'_'+str(len(rows)),remainder)
 return out
energy_density=grad(psi).dot(grad(chi))+y*tau
energy_adjoint=adjoint_density(energy_density,2)
mult=adv(om)+4*beta*om+S.diff(theta,x)
check('general_energy_Euler_derivative',energy_adjoint+mult)
f=adv(om)+om-S.diff(theta,x)
check('multiplier_residual_rewrite',mult-f-(4*beta-1)*om-2*S.diff(theta,x))
# A wholly polynomial local patch allows a separate exact vorticity derivative
# and its non-affine residual moment to be calculated directly.
q=4*a/beta;psip=(1+beta/2)*x*y-q*x**3/6;thp=a*x*x
wp=beta*S.Matrix([x,y])+J(psip);op=-lap(psip)
adp=lambda u:wp.dot(grad(u))
cp=adp(h)-2*beta*h;tp=-J(h).dot(grad(thp));dp=-lap(cp)
fdot=adp(dp)+dp+J(cp).dot(grad(op))-S.diff(tp,x)
check('polynomial_background_V',adp(op)+op-S.diff(thp,x))
check('polynomial_background_T',adp(thp)-(beta-2)*thp)
co=4*a*(5-1/beta)
check('polynomial_energy_multiplier',adp(op)+4*beta*op+S.diff(thp,x)-co*x)
for label,weight in [('mass',S.Integer(1)),('x',x),('y',y)]:
 check('linear_residual_affine_'+label,adjoint_density(weight*fdot,4))
check('polynomial_weighted_residual_energy',adjoint_density(psip*fdot,4)-(4*beta-2)*co*x)
# h=mirror R^2/18 (1-r^2/R^2)^9 in two disks generates the explicit twist
# alpha=-mirror epsilon(1-r^2/R^2)^8. Its cutoff is C8, enough for these controls.
# The standalone proof uses C-infinity bumps and does not infer it from C8 data.
R=.45;cx=1.3;cy=.4;numeric=[]
for b0,a0 in [(2.25,1.),(3.5,1.),(6.,-1.)]:
 for n in [24,36,52]:
  g,weights=leggauss(n);rr=R*(g+1)/2;wr=R*weights/2;ang=2*np.pi*(np.arange(160)+.317)/160
  r,phi=np.meshgrid(rr,ang,indexing='ij');area=np.broadcast_to(wr[:,None]*r*(2*np.pi/160),r.shape).ravel();r=r.ravel();phi=phi.ravel()
  expected=-4*a0*(5-1/b0)*np.pi*cx*R**4/90
  derivatives=[];errors=[];maxT=0.;maxDet=0.;raw=[]
  for epsabs in [.04,.02,.01]:
   energies=[]
   for eps in [epsabs,-epsabs]:
    de=0.;dtheta=0.
    for mirror in [1.,-1.]:
     center=np.array([mirror*cx,cy]);alpha=-mirror*eps*(1-r*r/R**2)**8
     dalpha=mirror*eps*16*r/R**2*(1-r*r/R**2)**7
     X=center+np.column_stack([r*np.cos(phi),r*np.sin(phi)])
     Y=center+np.column_stack([r*np.cos(phi-alpha),r*np.sin(phi-alpha)])
     z=Y-center;Jz=np.column_stack([-z[:,1],z[:,0]])
     rot=np.empty((len(r),2,2));rot[:,0,0]=np.cos(alpha);rot[:,0,1]=-np.sin(alpha);rot[:,1,0]=np.sin(alpha);rot[:,1,1]=np.cos(alpha)
     DP=np.einsum('nij,njk->nik',rot,np.eye(2)[None,:,:]+(dalpha/r)[:,None,None]*Jz[:,:,None]*z[:,None,:])
     Wbefore=np.column_stack([(.5*b0-1)*Y[:,0],(1+1.5*b0)*Y[:,1]-2*a0/b0*Y[:,0]**2])
     Vnew=np.einsum('nij,nj->ni',DP,Wbefore)-b0*X
     Vold=np.column_stack([-(1+.5*b0)*X[:,0],(1+.5*b0)*X[:,1]-2*a0/b0*X[:,0]**2])
     thnew=a0*Y[:,0]**2;thold=a0*X[:,0]**2
     de+=np.dot(area,.5*np.sum(Vnew**2-Vold**2,axis=1)+X[:,1]*(thnew-thold))
     dtheta+=np.dot(area,thnew-thold)
     gradient=np.linalg.solve(np.swapaxes(DP,1,2),np.column_stack([2*a0*Y[:,0],np.zeros(len(r))])[...,None])[...,0]
     residual=np.sum((Vnew+b0*X)*gradient,axis=1)-(b0-2)*thnew
     maxT=max(maxT,float(np.max(abs(residual))));maxDet=max(maxDet,float(np.max(abs(np.linalg.det(DP)-1))))
    energies.append(float(de));raw.append({'epsilon':eps,'energy_difference':float(de),'temperature_mass_difference':float(dtheta)})
   value=(energies[0]-energies[1])/(2*epsabs);derivatives.append(value);errors.append(abs(value-expected))
  ratios=[errors[i]/errors[i+1] for i in range(2)]
  ok=maxT<5e-13 and maxDet<5e-15 and errors[-1]<3e-8 and all(3.8<v<4.2 for v in ratios)
  numeric.append({'beta':b0,'a':a0,'radial_order':n,'angles':160,'expected_derivative':expected,'centered_derivatives':derivatives,'absolute_errors':errors,'error_reduction_factors':ratios,'max_thermal_residual':maxT,'max_det_error':maxDet,'values':raw,'pass':bool(ok)})
res={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_controls':rows,'nonlinear_twists':numeric,'all_pass':all(r['pass'] for r in rows+numeric),'proof_sha256':hashlib.sha256(Path('research/152_compact_energy_variation/PROOF.md').read_bytes()).hexdigest(),'scope':'Independent symbolic and finite compact controls. Polynomial background is a local patch, not a B2 profile; C8 manufactured cutoff tests the implementation, while the proof uses smooth bumps. No absolute energy sign or residual repair is inferred.'}
(root/'results.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'all_pass':res['all_pass'],'exact_count':len(rows),'finite_twists':len(numeric),'elapsed_seconds':res['elapsed_seconds'],'max_finest_derivative_error':max(v['absolute_errors'][-1] for v in numeric)},indent=2))
if not res['all_pass']:raise SystemExit(1)
