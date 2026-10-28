"""Independent Cartesian audit of the extremal sampled matrix values."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,time
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'11_residual_norms/verification'))
from audit_norms import direct_chi,aq
ctx.prec=640
sys.set_int_max_str_digits(0)
rows=[];start=time.monotonic()
for p in sorted(HERE.glob('algebraic_*_matrix_grid.json')):
 d=json.loads(p.read_text());name=d['name'];src=json.loads((HERE/(name+'.json')).read_text());c=Q(src['cl'])
 A={tuple(k):Q(v) for k,v in zip(src['canonical_order'],src['canonical_coefficients'])}
 m=d['sampled_minimum'];r=arb(2)**aq(str(m['log2_radius']));theta=arb.pi()*aq(str(m['angle_pi_units']));x=r*theta.cos();y=r*theta.sin()
 chi=direct_chi(A,c,x,y)
 aa=2*aq(c)+1-2*chi[2,2]-chi[0,4];bb=2*aq(c)+1+chi[2,2];ab=chi[3,1]
 lm=(aa+bb-((aa-bb)**2+4*ab*ab).sqrt())/2
 rho=-chi[2,1]-chi[0,3];rx=-chi[3,1]-chi[1,3];ry=-chi[2,2]-chi[0,4]
 F=(aq(c)*x-chi[1,2])*rx+(aq(c)*y+chi[2,1])*ry-rho
 assert lm.is_finite() and F.is_finite() and lm.overlaps(arb(m['Mmin_arb'])) and F.overlaps(arb(m['F_arb']))
 rows.append({'name':name,'status':'CONFIRMED','log2_radius':m['log2_radius'],'angle_pi_units':m['angle_pi_units'],'Mmin':lm.str(60),'F':F.str(60),'violates_M_ge_19_over_5':bool(lm<arb(19)/5),'violates_M_positive':bool(lm<0)})
 print(name,'PASS',lm.str(15),'F',F.str(15),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'CONFIRMED','method':'640-bit Cartesian jets compared to separately generated polar radial/angular recurrence.','rows':rows,'seconds':time.monotonic()-start,'scope':'These individual values are certified. The minimum over the plane and the first continuous crossing are not certified.'}
(HERE/'matrix_grid_audit.json').write_text(json.dumps(out,indent=2)+'\n')
