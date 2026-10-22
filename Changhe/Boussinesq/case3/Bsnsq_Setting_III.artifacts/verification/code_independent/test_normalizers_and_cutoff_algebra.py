"""Independent exact polynomial denominators and cutoff residual formula checks."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from finite_difference import desingularized_residuals,cartesian_residuals
from cutoff_polynomial import CutoffPolynomial,cutoff

beta=3.
p=np.array([[0,0],[0,-4],[.2,-4],[-.7,.4],[2,-7],[1,2]],float)
x,y=p.T
th=lambda x,y:x*x*(1+x*x+y)
om=lambda x,y:x*(1+x*x+2*y)
ps=lambda x,y:x*(y+.5*y*y+.7)
vel=lambda q:np.column_stack((-q[:,0]*(1+q[:,1]),q[:,1]+.5*q[:,1]**2))
A=beta-1-y;B=(beta+1)*y+.5*y*y
NF=2*np.abs(A*(1+2*x*x+y))+np.abs(B)+abs(beta-2)*np.abs(1+x*x+y)
NG=np.abs(A*(1+3*x*x+2*y))+np.abs(2*B)+np.abs(1+x*x+2*y)+2*np.abs(1+2*x*x+y)
rows=[]
for h in [.04,.02,.01]:
 d=desingularized_residuals(th,om,ps,vel,p,beta,h)
 row={'step':h,'NF_error':float(np.max(abs(d['N_F']-NF))),'NG_error':float(np.max(abs(d['N_G']-NG)))}
 assert row['NF_error']<1e-8 and row['NG_error']<1e-8
 rows.append(row)
cutrows=[]
for beta in [1.,38/21,2.,3.,5.]:
 prof=CutoffPolynomial(8,beta=beta,a0=1.3,v0=.7)
 s=np.array([1.2,1.7,2.5,3.5]);p=np.column_stack((8*np.sqrt(s),np.zeros(len(s))))
 C,Cp,_=cutoff(s)
 bracket=2*prof.c*C*(1-C)+2*s*Cp*(beta-prof.c*C)
 expected=prof.a0*p[:,0]**2*bracket
 raw=cartesian_residuals(prof.theta,prof.omega,prof.psi,lambda q:prof.velocity(q,relative=True),p,beta,.002)
 err=float(np.max(abs(raw['R_Theta']-expected)/(1+abs(expected))))
 assert err<1e-8
 cutrows.append({'beta':beta,'scaled_error':err,'s_2p5_bracket':float(bracket[2]),'algebraic_midpoint':19/18-7*beta/12})
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','normalizer_checks':rows,'cutoff_formula_checks':cutrows,'normalizer_definition':'exact grouping of the prompt Cartesian normalizers, divided by x^2 or |x| with their axis limits; no positive floor'}
Path('verification/normalizers_and_cutoff_algebra.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
