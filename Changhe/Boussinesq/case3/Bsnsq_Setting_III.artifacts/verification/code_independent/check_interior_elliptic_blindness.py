"""P252 exact Cartesian controls and direct physical-annulus inverse manufacture."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import sympy as sp
from scipy.special import expit,roots_legendre
root=Path('research/252_interior_elliptic_blindness/verification');beg=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def check(name,passed,detail=None):checks.append({'name':name,'passed':bool(passed),'detail':detail})
x,y,R,A=sp.symbols('x y R A',real=True,nonzero=True);chi=sp.Function('chi');z=(x*x+y*y)/R**2
for n in [3,5,7,11]:
 p=sp.expand(sum((-1)**j*sp.binomial(n,2*j)*x**(n-2*j)*y**(2*j)for j in range((n+1)//2)))
 check('harmonic',sp.expand(sp.diff(p,x,2)+sp.diff(p,y,2))==0,n)
 check('odd_x',sp.expand(p.subs(x,-x)+p)==0,n)
 check('homogeneous_euler',sp.expand(x*sp.diff(p,x)+y*sp.diff(p,y)-n*p)==0,n)
 psi=A*p*chi(z);target=4*A/R**2*p*(z*sp.Subs(sp.diff(chi(sp.Symbol('s')),sp.Symbol('s'),2),sp.Symbol('s'),z)+(n+1)*sp.Subs(sp.diff(chi(sp.Symbol('s')),sp.Symbol('s')),sp.Symbol('s'),z))
 check('cartesian_product_laplacian',sp.simplify(sp.diff(psi,x,2)+sp.diff(psi,y,2)-target)==0,n)
 u=[-A*sp.diff(p,y),A*sp.diff(p,x)]
 check('interior_divergence',sp.expand(sp.diff(u[0],x)+sp.diff(u[1],y))==0,n)
 check('interior_vorticity',sp.expand(sp.diff(u[0],y)-sp.diff(u[1],x))==0,n)
 center_ok=all(sp.diff(v,x,i,y,j).subs({x:0,y:0})==0 for v in u for i in range(n-1)for j in range(n-1-i))
 check('all_center_velocity_jets_through_N_minus2',center_ok,{'N':n,'max_order':n-2})
 check('axis_velocity_amplitude',sp.simplify(u[0].subs(y,0))==0 and sp.simplify(u[1].subs(y,0)-A*n*x**(n-1))==0,n)
 if n==3:check('explicit_cubic_velocity',sp.expand(u[0]-6*A*x*y)==0 and sp.expand(u[1]-3*A*(x*x-y*y))==0)
# Stronger property: all moments with a homogeneous harmonic P_l vanish by a radial identity.
s=sp.symbols('s',positive=True);f=sp.Function('f')(s)
for n in [3,5,7,11]:
 check('matching_harmonic_moment_radial_total_derivative',sp.simplify(sp.diff(s**(n+1)*sp.diff(f,s),s)-s**n*(s*sp.diff(f,s,2)+(n+1)*sp.diff(f,s)))==0,n)
# Physical source: no radial Green formula, solver code, or inverse differential equation.
def quad(n,amp,radius,points,nr,na):
 q,w=roots_legendre(nr);sval=2.5+1.5*q;w=1.5*w;left=sval-1;right=4-sval
 ell=-1/left+1/right;c=expit(-ell);prod=expit(ell)*c
 ell1=left**-2+right**-2;ell2=-2*left**-3+2*right**-3
 cp=-prod*ell1;cpp=prod*((1-2*c)*ell1**2-ell2)
 theta=2*np.pi*(np.arange(na)+.173)/na;rad=radius*np.sqrt(sval)
 xx=rad[:,None]*np.cos(theta);yy=rad[:,None]*np.sin(theta)
 source=-4*amp/radius**2*rad[:,None]**n*np.cos(n*theta)[None,:]*(sval*cpp+(n+1)*cp)[:,None]
 weights=w[:,None]*radius**2/(2*na);uv=[]
 for px,py in points:
  dx,dy=px-xx,py-yy;rr=dx*dx+dy*dy;raw=np.array([np.sum(weights*source*dy/rr),np.sum(-weights*source*dx/rr)])
  rr0=xx*xx+yy*yy;v0=np.array([np.sum(-weights*source*yy/rr0),np.sum(weights*source*xx/rr0)])
  uv.append((raw,raw-v0,v0))
 return uv
rows=[]
for n in [3,5,7]:
 radius=2.;amp=1./(n*(radius/2)**(n-1));pts=np.array([[0.,0.],[1.,0.],[.31,-.62],[-.42,.23],[0.,.7]])
 exact=np.stack([amp*n*np.imag((pts[:,0]+1j*pts[:,1])**(n-1)),amp*n*np.real((pts[:,0]+1j*pts[:,1])**(n-1))],axis=1)
 for nr,na in [(48,64),(96,128),(192,256)]:
  vals=quad(n,amp,radius,pts,nr,na)
  for i,(raw,rel,v0)in enumerate(vals):
   rows.append({'N':n,'A':amp,'R':radius,'radial_nodes':nr,'angular_nodes':na,'point':pts[i].tolist(),'exact_velocity':exact[i].tolist(),'quadrature_absolute':raw.tolist(),'quadrature_relative':rel.tolist(),'quadrature_center':v0.tolist(),'absolute_error':float(np.linalg.norm(raw-exact[i])),'relative_error':float(np.linalg.norm(rel-exact[i]))})
 for metric in ['absolute_error','relative_error']:
  fine=max(a[metric]for a in rows if a['N']==n and a['radial_nodes']==192)
  check('direct_physical_annulus_inverse_fine',fine<2e-10,{'N':n,'metric':metric,'max_error':fine})
# Record finite quadrature moment checks; symbolic proof covers all harmonic polynomials.
for n in [3,5,7]:
 relevant=[a for a in rows if a['N']==n and a['radial_nodes']==192]
 check('canonical_center_matches_zero',max(np.linalg.norm(a['quadrature_center'])for a in relevant)<1e-11,n)
result={'started_utc':beg,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'checks':checks,'passed':sum(a['passed']for a in checks),'total':len(checks),'quadrature_rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((root.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Exact symbolic identities plus a floating manufactured inverse check. No production-state inverse error or coupled B2 conclusion.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['passed'],result['total'],'elapsed',result['elapsed_seconds']);print('failures',[a for a in checks if not a['passed']]);print('maxfine',max(a['absolute_error']for a in rows if a['radial_nodes']==192))
