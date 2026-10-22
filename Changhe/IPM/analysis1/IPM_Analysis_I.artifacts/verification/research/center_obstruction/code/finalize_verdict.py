"""Pin the checked narrow theorem and actual Opus closure."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
B=Path(__file__).resolve().parents[3];E=B/'research/center_obstruction/evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((E/'center_checks.json').read_text())
assert r['status']=='EXACT_ALGEBRA_AND_ENCLOSURES_CONFIRMED' and r['original_D_row_major_values_checked']==1820
assert sha(B/'research/center_obstruction/code/check_center.py')==r['code_sha256']
assert sha(B/'data_exact/modal_v2.json')==r['input_sha256']
assert sha(B/'research/modal_exactification/evidence/trial_v2_h0.008.npz')==r['original_npz_sha256']
assert r['residual_highest_frequency']==523 and r['density_positive_modes']==261 and r['residual_positive_modes']==262
review=B/'notes/reviews/center_obstruction_closure_metadata.json';m=json.loads(review.read_text())
assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn'
assert sha(B/'notes/reviews/center_obstruction_closure_request.txt')==m['input_sha256']
assert 'CLOSED and accepted' in (B/'notes/reviews/center_obstruction_closure_response.md').read_text()
da=json.loads((E/'dependency_audit.json').read_text());count=0
for path,info in da['dependencies'].items():
 p=B/path;assert sha(p)==info['sha256'];dep=json.loads(p.read_text())
 pins=dep.get('source_and_evidence_sha256',dep.get('files'))
 for f,h in pins.items():assert sha(B/f)==h;count+=1
proof=B/'research/center_obstruction/PROOF.md';reviewed_proof_hash=sha(proof)
s=proof.read_text().replace('closure review remains OPEN.', 'closure review was accepted at2026-10-20T19:23:37Z. Status: CONFIRMED for the narrow exact-modal-trial obstruction.')
proof.write_text(s)
paths=['research/center_obstruction/PROOF.md','research/center_obstruction/code/check_center.py','research/center_obstruction/code/finalize_verdict.py','research/center_obstruction/evidence/center_checks.json','research/center_obstruction/evidence/exact_modes.json','research/center_obstruction/evidence/dependency_audit.json','research/center_obstruction/evidence/source_snapshot.json','research/center_obstruction/evidence/lead_corner_at_1915.md','notes/reviews/center_obstruction_focus_metadata.json','notes/reviews/center_obstruction_focus_response.md','notes/reviews/center_obstruction_closure_metadata.json','notes/reviews/center_obstruction_closure_response.md']
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','method':'Exact trig and Laurent reconstruction, independent raw NPY layout check, Arb384 and mpmath.iv160, standalone differentiated Green and cone-divergence proof, actualOpus5.5 follow-up.','scope':'Exact repaired modal trial only: factor notC2, density C4,1 but notC5 at0; residual and either ordered rectangular remainder fail local product-weight L2 for A>=6. No existence or exclusion endpoint.','actual_review_model':m['actual_response_model'],'review_end_utc':m['end_utc'],'dependency_pins_checked':count,'reviewed_proof_sha256':reviewed_proof_hash,'post_review_edit':'Status sentence only.','files':{p:sha(B/p) for p in paths}}
(E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths),'dependency_pins':count}))
