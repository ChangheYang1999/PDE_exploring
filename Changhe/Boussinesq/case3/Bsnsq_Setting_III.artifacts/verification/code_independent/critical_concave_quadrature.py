"""P268 compact-interval diagnostic in t=log y, independent of lead code.
The exact sign theorem is analytic. These adaptive values are not enclosures.
"""
from pathlib import Path
from datetime import datetime,timezone
import math,json,hashlib,time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit
V=Path('research/268_critical_axis_both_signs/verification');tick=time.monotonic();start=datetime.now(timezone.utc).isoformat();rows=[]
def cut(y):
 if y<=1:return 0.,0.
 if y>=2:return 1.,0.
 u=y*y-1;v=4-y*y;q=expit(-1/u+1/v)
 return q,q*(1-q)*2*y*(u**-2+v**-2)
for beta in [2.,2.5,3.,4.,10.]:
 d=1+1.5*beta;k=3+.5*beta;g=.5+1/beta;m=1-2/beta;kap=k/beta;p1=.5+2/beta
 def rhs(t,Y):
  y=math.exp(t);b,lr,r1,Gb,Ge,R=Y;rho=math.exp(lr);chi,cp=cut(y);bp=d+(beta-d)*chi;bpp=(beta-d)*cp
  return [y*bp,y*(d-bp)/b,y*(1/rho-beta*r1/2)/b,y*(k*Gb-4*rho**3*bpp)/b,y*(k*Ge-4*rho**2*r1+8/beta)/b,y*rho]
 for tol in [1e-9,1e-11,2e-13]:
  sol=solve_ivp(rhs,(0,math.log(2)),[d,0,2/beta,0,0,1],method='DOP853',rtol=tol,atol=tol/100)
  b,lr,r1,Gb,Ge,R=sol.y[:,-1];rho=math.exp(lr);z=b/beta;y0=z-2;C=rho/z**g;D=r1*math.sqrt(z)+z**(-1/beta)/C
  Kb=Gb/z**kap;Ke=(Ge-4*D*C*C*z**p1+2*C*z**g+8/(beta*k))/z**kap;Lb=k*Kb/(beta*C);Le=k*Ke/(beta*C);threshold=Lb/abs(Le)
  samples=[]
  for factor in [.5,2.]:
   la=factor*threshold;L=la**(m-1)*(Lb/la+Le);samples.append({'A':1.,'lambda':la,'coefficient_L':L})
  rows.append({'beta':beta,'tol':tol,'success':bool(sol.success),'nfev':sol.nfev,'b2':b,'rho2':rho,'R2':R,'rho_b_minus_dR':rho*b-d*R,'y0':y0,'C':C,'D1':D,'Kb':Kb,'Ke':Ke,'Lb':Lb,'Le':Le,'threshold_A':threshold,'fixed_A_samples':samples})
checks={'all15completed':all(x['success']for x in rows)and len(rows)==15,'strict_tail_shift':all(x['y0']>0 for x in rows),'Kb_positive_Ke_negative':all(x['Kb']>0>x['Ke']for x in rows),'fixed_A_bothsigns':all(x['fixed_A_samples'][0]['coefficient_L']>0>x['fixed_A_samples'][1]['coefficient_L']for x in rows),'independent_R_identity_tolerance':all(abs(x['rho_b_minus_dR'])<100*x['tol']for x in rows)}
sensitivity=[]
for beta in [2.,2.5,3.,4.,10.]:
 a,b=[x for x in rows if x['beta']==beta][-2:];sensitivity.append({'beta':beta,'max_change_Kb_Ke_threshold':max(abs(a[k]-b[k])for k in ['Kb','Ke','threshold_A'])})
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'rows':rows,'checks':checks,'sensitivity':sensitivity,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Finite adaptive diagnostic, no certified quadrature bound; analytic sign proof is independent.'};(V/'quadrature.json').write_text(json.dumps(out,indent=2)+'\n');print(out['elapsed_seconds'],checks)
for row in rows[2::3]:print(row['beta'],row['Kb'],row['Ke'],row['threshold_A'],row['fixed_A_samples'])
