"""Independent scalar ODE diagnostic for P264, compact interval only.
The analytic proof does not depend on these floating-point measurements.
"""
from pathlib import Path
from datetime import datetime,timezone
import math,json,hashlib,time
import numpy as np
from scipy.integrate import solve_ivp
V=Path('research/264_critical_axis_data/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
def cutoff(y):
 if y<=1:return 0.,0.,0.
 if y>=2:return 1.,0.,0.
 a=y*y-1;c=4-y*y;z=-1/a+1/c
 if z>=0:e=math.exp(-z);ch=1/(1+e)
 else:e=math.exp(z);ch=e/(1+e)
 # Use the small exponential, preserving derivatives when ch rounds to one.
 fac=e/(1+e)**2
 zp=2*y*(a**-2+c**-2);zpp=2*(a**-2+c**-2)+8*y*y*(c**-3-a**-3)
 return ch,fac*zp,fac*(zpp+(1-2*ch)*zp*zp)
rows=[]
for beta in [2.,2.5,3.,4.,10.]:
 d=(3*beta+2)/2;k=(beta+6)/2;gamma=.5+1/beta;p=.5+2/beta
 def deriv(y,state):
  rho,r1,Gb,Ge=state;ch,chp,chpp=cutoff(y);b=y*(d+(beta-d)*ch);bp=d+(beta-d)*(ch+y*chp);bpp=(beta-d)*(2*chp+y*chpp)
  return [(d-bp)*rho/b,(1/rho-beta*r1/2)/b,(k*Gb-4*rho**3*bpp)/b,(k*Ge-4*rho**2*r1+8/beta)/b]
 for tol in [1e-9,1e-11,2e-13]:
  sol=solve_ivp(deriv,(1.,2.),[1.,2/beta,0.,0.],method='DOP853',rtol=tol,atol=tol/100,dense_output=True,max_step=.05)
  rho,r1,Gb,Ge=sol.y[:,-1];C=rho/2**gamma;D1=r1*math.sqrt(2)+2**(-1/beta)/C;Kb=Gb/2**(k/beta)
  Ke=(Ge-4*D1*C*C*2**p+2*C*2**gamma+8/(beta*k))/2**(k/beta);Lb=Kb*k/(beta*C);Le=Ke*k/(beta*C)
  A=2+2*abs(Lb)/abs(Le);L=Lb/A+Le
  yy=np.linspace(1,2,401);st=sol.sol(yy);u=st[0]**2*st[1]-2/beta
  tails=[]
  for Y in [1e2,1e4,1e8]:
   I=L*Y**(-1+2/beta)+4*D1*C*p*Y**(-1+1/beta)-2*gamma/Y
   tails.append({'y':Y,'I':I,'critical_scaled_I':Y**(1-2/beta)*I,'exact_tail_formula_limit':L})
  row={'beta':beta,'rtol':tol,'success':bool(sol.success),'nfev':sol.nfev,'C':C,'D_over_A':D1,'K_b':Kb,'K_eta':Ke,'L_b':Lb,'L_eta':Le,'A_chosen':A,'L':L,'min_sampled_u':float(u.min()),'max_sampled_u':float(u.max()),'tail_samples':tails,'scope':'floating scalar ODE tolerance comparison, not an interval enclosure or a full profile'}
  if beta==2:
   row['beta2_finite_limit_shifts']=[{'target':target,'I0':target-L,'computed_limit':L+(target-L)}for target in [-2.,0.,3.]]
  rows.append(row)
 print(beta,'L',L,'Le',Le,'A',A,'nfev',sol.nfev,flush=True)
comparison=[]
for beta in [2.,2.5,3.,4.,10.]:
 group=[r for r in rows if r['beta']==beta];comparison.append({'beta':beta,'L_difference_last_two':group[-1]['L']-group[-2]['L'],'all_success':all(r['success']for r in group),'all_Le_negative':all(r['L_eta']<0 for r in group),'all_L_negative':all(r['L']<0 for r in group)})
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'rows':rows,'comparisons':comparison,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Independent compact-interval ODE diagnostic. Smooth construction and sign proof are analytic in PROOF.md. No full-plane PDE/inverse is solved.'};(V/'quadrature.json').write_text(json.dumps(out,indent=2)+'\n');print('seconds',out['elapsed_seconds'])
