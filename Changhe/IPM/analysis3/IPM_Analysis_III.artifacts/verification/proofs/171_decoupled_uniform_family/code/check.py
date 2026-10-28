from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json
root=Path(__file__).resolve().parents[1]
beta,eta,delta=Q(17,2),Q(37,20),Q(9,5)
k=Q(1615536043799051,9007199254740992)
qstar=Q(1,5)
a_min,a_max=Q(18,5),Q(4)
m=Q(55267,50000)
values={
 'inner_scalar_perturbation':2*delta+8-beta,
 'outer_scalar_weight':8-eta,
 'axis_evaluation_outer_at_qstar':qstar+eta/2-5,
 'axis_HS_outer_at_qstar':2*(qstar+eta/2-5)+(8-eta),
 'separated_outer_dr_at_qstar':2*qstar-3,
 'inner_weighted_velocity_rate':2-delta,
 'scalar_kappa':k+Q(3,40),
 'uniform_margin':m,
 'perturbed_margin':m/2,
 'fixed_Garding_epsilon':m/4,
 'conditional_transport_inverse_upper':2/m,
 'min_angular_square_power':8-2*a_max,
 'max_angular_square_power':8-2*a_min,
 'min_angular_integrability_gap':9-2*a_max,
 'high_far_residual_gap_at_qstar':Q(1,2)-2*qstar,
}
assert values['inner_scalar_perturbation']>0
assert values['axis_HS_outer_at_qstar']<0
assert values['separated_outer_dr_at_qstar']<-1
assert values['inner_weighted_velocity_rate']>0
assert values['scalar_kappa']>0
assert values['min_angular_integrability_gap']>0
assert values['high_far_residual_gap_at_qstar']>0
assert Q(5,2)<a_min<=a_max<Q(9,2)
assert a_min>3
assert Q(21,4)<1/k<Q(23,4)
assert max(k,Q(4,21))<qstar<Q(1,4)
assert values['conditional_transport_inverse_upper']==Q(100000,55267)
report={'status':'PASS','date':datetime.now(timezone.utc).isoformat(),
 'method':'Exact rational endpoint and conditional-margin audit; analytical proof is separate.',
 'values':{key:str(value) for key,value in values.items()},
 'example_tail_interval':['21/4','23/4'],'example_qstar':'1/5',
 'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [root.parent/'168_decoupled_family_mapping/PROOF.md',root.parent/'167_moving_tail_uniform/PROOF.md',root.parent/'160_family_margin/evidence/audit.json']}}
(root/'evidence/check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'proof_sha256':report['proof_sha256']}))
