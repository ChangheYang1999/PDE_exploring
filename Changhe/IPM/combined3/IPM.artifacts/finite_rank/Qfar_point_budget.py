#!/usr/bin/env python3
"""Certified actual far coefficient sup candidates for the Q-norm split.

Only pointwise coefficient budgets are certified, not the low/high operator
localization or commutator join needed for an existence theorem.
"""
import sys,json,time
from pathlib import Path
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,C
from asymptotics013 import Expansion
st=time.time();e=Evaluator(384,max_density_order=2,max_velocity_order=1);a=Expansion(e,'far',degree=12)
rows=[];q=arb(21)/10;c=arb(C);mu=arb(1)/10;free=q*c/2
for R in [1000,10000,30000,100000]:
 bx=a.point_bound('rho',1,0,R);by=a.point_bound('rho',0,1,R);B=bx+by
 S=a.point_bound('u1',1,0,R)+(a.point_bound('u1',0,1,R)+a.point_bound('u2',1,0,R))/2
 source=(1+mu*mu)*(arb(3).sqrt()+1)*B;strain=q*S
 rows.append({'R':R,'gradient_l1_bound':B.str(60),'strain_op_bound':S.str(60),'low_source_proposed_bound':source.str(60),'low_strain_proposed_bound':strain.str(60),'free_qc_half':free.str(60),'proposed_low_budget_margin':(free-source-strain).str(60)})
 print(rows[-1],flush=True)
z={'status':'RIGOROUS_FAR_COEFFICIENT_POINT_BOUNDS_ONLY','rows':rows,'cut_mu':'1/10','elapsed_seconds':time.time()-st,'warning':'The low/cross/high operator decomposition is not proved by these coefficient comparisons. No existence claim.'}
(HERE/'Qfar_point_budget.json').write_text(json.dumps(z,indent=2)+'\n')
