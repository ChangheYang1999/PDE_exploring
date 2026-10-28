from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json
root=Path(__file__).resolve().parents[1]
beta,delta,gamma,sigma,s0=Q(17,2),Q(9,5),Q(-1,2),Q(25,4),Q(41,20)
values={'inner_log_weight':2*delta+8-beta,'outer_old':2*gamma+2-Q(5,4),'outer_new':2*gamma+2-Q(37,20),'angular_worst_power':8-2*Q(17,4),'graph_angular_regular_gap':sigma-1-3,'base_C5_gap':sigma-6,'bulk_C1_gap':s0-2}
assert values['inner_log_weight']==Q(31,10)>0
assert values['outer_old']==Q(-1,4)<0
assert values['outer_new']==Q(-17,20)<0
assert values['angular_worst_power']==Q(-1,2)>-1
assert all(values[k]>0 for k in ('graph_angular_regular_gap','base_C5_gap','bulk_C1_gap'))
source=Path('theory-working-files/Exist_cond.md')
(root/'evidence/lead_Exist_cond.md').write_bytes(source.read_bytes())
deps=['71_fractional_high_mapping','123_variable_order_coupling','164_perturbed_axis','166_perturbed_low_block','167_moving_tail_uniform','171_decoupled_uniform_family','172_decoupled_nonlinear']
report={'status':'PASS','date':datetime.now(timezone.utc).isoformat(),'scope':'Exact endpoint arithmetic and revision binding. The analytic argument is in PROOF.md.','values':{k:str(v) for k,v in values.items()},'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'lead_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{d:hashlib.sha256((root.parent/d/'PROOF.md').read_bytes()).hexdigest() for d in deps}}
(root/'evidence/check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
