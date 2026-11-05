#!/usr/bin/env python3
"""Actual uniform far Cvs3 Gaussian high/cross certificate."""
import sys,json,time,hashlib
from pathlib import Path
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator
from asymptotics013 import Expansion
ctx.prec=384
st=time.time(); e=Evaluator(384,max_density_order=2,max_velocity_order=0)
a=Expansion(e,'far',degree=12)
mu=arb(1)/10; cchi=arb(2)
Cstar=4*arb(2).sqrt()/arb.pi().sqrt()+(arb.pi()/2).sqrt()
rows=[]
for R in [1000,10000,30000,100000]:
    bx=a.point_bound('rho',1,0,R); by=a.point_bound('rho',0,1,R)
    xx=a.point_bound('rho',2,0,R); xy=a.point_bound('rho',1,1,R); yy=a.point_bound('rho',0,2,R)
    B=(bx*bx+by*by).sqrt(); D=(xx*xx+2*xy*xy+yy*yy).sqrt()
    L=D+cchi*B/R
    row={'R':R,'gradient_Euclidean_bound':B.str(70),'Hessian_Frobenius_bound':D.str(70),'Kfar_Frobenius_Lipschitz_bound':L.str(70),'Cvs3_high_cross_error_mu01':(2*Cstar*L/mu).str(70),'Cvs3_high_cross_error_mu1':(2*Cstar*L).str(70)}
    rows.append(row);print(row,flush=True)
z={'status':'RIGOROUS_FAR_CVS3_HIGH_CROSS_BOUND','mu':'1/10','cutoff_gradient_factor':'2','Cstar':Cstar.str(70),'rows':rows,'elapsed_seconds':time.time()-st,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE.parent/'coercivity_residual'/'fields013.py',HERE.parent/'coercivity_residual'/'asymptotics013.py']},'warning':'Only the displayed Cvs3 far high/cross estimate is closed. This does not establish total IPM coercivity or existence.'}
(HERE/'Gaussian_Riesz_far_bounds.json').write_text(json.dumps(z,indent=2)+'\n')
