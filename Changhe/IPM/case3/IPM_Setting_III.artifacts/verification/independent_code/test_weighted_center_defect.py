"""Independent Gaussian potential test with a deliberately nonzero center defect."""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import sympy as s
import numpy as np
import mpmath as mp
x,y,E,q,l,r,mu=s.symbols('x y E q l r mu',real=True)
dx=lambda z:s.diff(z,x)-2*x*E*s.diff(z,E)
dy=lambda z:s.diff(z,y)-2*y*E*s.diff(z,E)
psi=-q*x*y*E;rho=q*y*(4-2*x*x-2*y*y)*E
a=4*q;c=-q;delta=l-q-1
U=s.Matrix([-dy(psi),dx(psi)]);X=s.Matrix([x,y]);W=l*X+U
h=rho-a*y;v=U-s.Matrix([q*x,-q*y]);g=s.Matrix([dx(h),dy(h)])
R=s.expand(W.dot(s.Matrix([dx(rho),dy(rho)]))-rho);F=s.expand(R-a*delta*y)
DF=s.Matrix([dx(F),dy(F)]);Dv=v.jacobian([x,y])+s.Matrix([[s.diff(z,E)*(-2*x*E),s.diff(z,E)*(-2*y*E)] for z in v])
DU=U.jacobian([x,y])+s.Matrix([[s.diff(z,E)*(-2*x*E),s.diff(z,E)*(-2*y*E)] for z in U]);S=(DU+DU.T)/2
checks=[]
def zero(name,val):
 assert s.expand(val)==0,(name,s.expand(val));checks.append(name)
zero('Poisson from independently chosen Gaussian stream',-dx(dx(psi))-dy(dy(psi))-dx(rho))
zero('divergence',dx(U[0])+dy(U[1]))
zero('scalar residual with nonzero center correction',W.dot(g)-h+a*v[1]-F)
for j in range(2):
 adv=W[0]*dx(g[j])+W[1]*dy(g[j])
 zero('differentiated residual component '+str(j),adv+(l-1)*g[j]+(DU.T*g)[j]+a*Dv[1,j]-DF[j])
zero('origin residual leading coefficient',s.diff(R,y).subs({x:0,y:0,E:1})-a*delta)

# Exact angular integration of Cartesian polynomials; no angular grid or producer code.
def angular(expr):
 pp=s.Poly(s.expand(expr),x,y);out=0
 for (i,j),coeff in pp.terms():
  if i%2 or j%2:continue
  factor=2*s.gamma(s.Rational(i+1,2))*s.gamma(s.Rational(j+1,2))/s.gamma(s.Rational(i+j+2,2))
  out+=coeff*r**(i+j)*factor
 return s.factor(out)
scalars={'h2':h*h,'g2':g.dot(g),'v2h':v[1]*h,'Fh':F*h,'XUh2_num':X.dot(U)*h*h,'XUg2_num':X.dot(U)*g.dot(g),'Sg':g.dot(S*g),'Dvhg':s.Matrix([Dv[1,0],Dv[1,1]]).dot(g),'DFg':DF.dot(g),'Dv2':sum(z*z for z in Dv),'F2':F*F,'DF2':DF.dot(DF),'hflux':W.dot(X)*h*h,'gflux':W.dot(X)*g.dot(g)}
funcs={k:s.lambdify((r,E,q,l),angular(val),'mpmath',cse=True) for k,val in scalars.items()}
mp.mp.dps=60
records=[]
for ng in (48,96):
 nd,ww=np.polynomial.legendre.leggauss(ng)
 for amp,ell in [('0.3','1.6'),('-0.2','2.3')]:
  av=mp.mpf(amp);lv=mp.mpf(ell)
  for weight in ('1.5','2','2.5'):
   muv=mp.mpf(weight);mv=muv+1
   vals={key:mp.mpf(0) for key in funcs if key not in ('hflux','gflux')}
   for lo,hi in zip((-12,-8,-4,0,4,8),(-8,-4,0,4,8,12)):
    for nn,wt in zip(nd,ww):
     lr=mp.mpf(str((lo+hi)/2+(hi-lo)*nn/2));rv=mp.exp(lr);ev=mp.exp(-rv*rv);wg=mp.mpf(str(wt*(hi-lo)/2))
     for key,fn in funcs.items():
      if key in ('hflux','gflux'):continue
      expweight=mv if key in ('h2','v2h','Fh','XUh2_num','F2') else muv
      factor=rv**(2-2*expweight)
      if key in ('XUh2_num','XUg2_num'):factor/=rv*rv
      vals[key]+=wg*factor*fn(rv,ev,av,lv)
   boundaries={}
   for key,wv in [('hflux',mv),('gflux',muv)]:
    end=[]
    for lr in (-12,12):
     rv=mp.exp(lr);end.append(funcs[key](rv,mp.exp(-rv*rv),av,lv)*rv**(-2*wv))
    boundaries[key]=end[1]-end[0]
   scalar=((mv-1)*lv-1)*vals['h2']+mv*vals['XUh2_num']+4*av*vals['v2h']-vals['Fh']+boundaries['hflux']/2
   grad=(muv*lv-1)*vals['g2']+muv*vals['XUg2_num']+vals['Sg']+4*av*vals['Dvhg']-vals['DFg']+boundaries['gflux']/2
   sr=abs(scalar)/max(vals['h2'],abs(vals['Fh']))
   gr=abs(grad)/max(vals['g2'],abs(vals['DFg']))
   assert sr<mp.mpf('1e-8') and gr<mp.mpf('1e-8'),(ng,amp,weight,sr,gr)
   N=max((muv*muv+1)/(muv*muv-1),(muv*muv+9)/(9-muv*muv))
   normratio=mp.sqrt(vals['Dv2']/vals['g2']);assert normratio<=N
   records.append({'nodes_per_panel':ng,'amplitude':amp,'ell':ell,'mu':weight,'center_delta':str(lv-av-1),'scalar_annulus_identity_relative_error':str(sr),'gradient_annulus_identity_relative_error':str(gr),'derivative_inverse_norm_ratio_on_annulus':str(normratio),'Nodd':str(N),'corrected_scalar_residual_ratio_on_annulus':str(mp.sqrt(vals['F2']/vals['h2'])),'corrected_gradient_residual_ratio_on_annulus':str(mp.sqrt(vals['DF2']/vals['g2']))})
# Separate complex rank-one odd-mode test, retaining high modes and radial frequencies.
sv=[]
for muv in (1.1,1.5,2.,2.5,2.9):
 bound=max((muv*muv+1)/(muv*muv-1),(muv*muv+9)/(9-muv*muv));maximum=0
 for nn in range(1,102,2):
  for xi in (0.,.01,.2,1.,10.,100.):
   z=muv+1j*xi;vec=np.array([z,1j*nn]);mat=np.outer(vec,vec)/(nn*nn-z*z)
   value=float(np.linalg.svd(mat,compute_uv=False)[0]);maximum=max(maximum,value);assert value<=bound*(1+1e-13)
 sv.append({'mu':muv,'maximum_sampled':maximum,'bound':bound})
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'manufactured_nonzero_center_rows':records,'odd_multiplier_samples':sv,'scope':'Exact polynomial Gaussian potential and residual identities, exact angular integration, two radial rules on log-radius [-12,12] with exact boundary flux included. Whole-plane convergence and infinite uncorrected residual norm are analytic statements in PROOF.md; numerical norms here remain finite-annulus diagnostics.'}
Path('research/weighted_center_defect/verification/checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'energy_rows':len(records),'odd_multiplier_samples':1530}),flush=True)
