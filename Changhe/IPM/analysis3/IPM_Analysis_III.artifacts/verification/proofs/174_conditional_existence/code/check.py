from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
k=Q(1615536043799051,9007199254740992)
values={'k':k,'tail_remainder_exponent':2*k-1,'high_tail_exponent':Q(-1,2),'bulk_holder_ceiling':Q(41,20)-2,'residual_knot_gap':Q(13,2)-Q(25,4),'inner_correction_exponent':Q(9,5)}
assert 0<k<Q(1,4)
assert values['tail_remainder_exponent']<values['high_tail_exponent']
assert values['bulk_holder_ceiling']>0 and values['residual_knot_gap']>0
lead=root.parent/'173_high_low_embeddings/evidence/lead_Exist_cond.md'
deps=['59_moving_tail_iteration','71_fractional_high_mapping','167_moving_tail_uniform','171_decoupled_uniform_family','172_decoupled_nonlinear','173_high_low_embeddings']
report={'status':'PASS','date':datetime.now(timezone.utc).isoformat(),'scope':'Exact exponents and proof revision binding; no certification of the open inverse or smallness hypotheses.','values':{k:str(v) for k,v in values.items()},'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'lead_snapshot_sha256':hashlib.sha256(lead.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{d:hashlib.sha256((root.parent/d/'PROOF.md').read_bytes()).hexdigest() for d in deps}}
(root/'evidence/check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
