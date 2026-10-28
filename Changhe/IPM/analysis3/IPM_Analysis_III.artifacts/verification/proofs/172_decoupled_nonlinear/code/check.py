from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json
root=Path(__file__).resolve().parents[1]
beta,eta,delta,gamma=Q(17,2),Q(37,20),Q(9,5),Q(-1,2)
sigma,s0=Q(25,4),Q(41,20)
qB=(8-eta)/2
values={
 'inner_log_output_power':2*delta+8-beta,
 'outer_log_output_power':2*gamma+2-eta,
 'outer_trace_power':eta/2-2,
 'outer_jet_velocity_power':3-qB,
 'outer_jet_product_log_power':2*(gamma+2-qB)+2-eta,
 'base_smaller_source_inner_dr':Q(3),
 'base_larger_source_inner_dr1':7+2*delta-beta,
 'base_larger_source_inner_dr2':11-beta,
 'worst_inner_source_dr':beta-9,
 'worst_outer_source_dr':eta-5,
 'outer_separated_output_dr':2*gamma-3,
 'bulk_smaller_source_inner_dr':3+2*delta,
 'bulk_larger_source_inner_dr':7+2*delta-beta,
 'base_C5_embedding_gap':sigma-6,
 'bulk_C1_embedding_gap':s0-2,
}
for key in ['inner_log_output_power','base_C5_embedding_gap','bulk_C1_embedding_gap']:assert values[key]>0
for key in ['outer_log_output_power','outer_jet_product_log_power']:assert values[key]<0
for key in ['base_smaller_source_inner_dr','base_larger_source_inner_dr1','base_larger_source_inner_dr2','worst_inner_source_dr','bulk_smaller_source_inner_dr','bulk_larger_source_inner_dr']:assert values[key]>-1
for key in ['worst_outer_source_dr','outer_separated_output_dr']:assert values[key]<-1
assert values['outer_jet_product_log_power']==2*gamma-2
assert values['outer_trace_power']==2-qB==Q(-43,40)
assert values['inner_log_output_power']==Q(31,10)
assert values['outer_log_output_power']==Q(-17,20)
report={'status':'PASS','date':datetime.now(timezone.utc).isoformat(),
 'method':'Exact rational integrability and derivative inventory; analytical proof is separate.',
 'values':{key:str(value) for key,value in values.items()},
 'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [root.parent/'168_decoupled_family_mapping/PROOF.md',root.parent/'171_decoupled_uniform_family/PROOF.md',root.parent/'71_fractional_high_mapping/PROOF.md',root.parent/'63_cone_local_high_space/PROOF.md']}}
(root/'evidence/check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'proof_sha256':report['proof_sha256']}))
