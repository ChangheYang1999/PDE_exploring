"""Pin completed independent exterior evidence and check every public decimal exactly."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/outer_majorant/evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
r=json.loads((E/'outer_result.json').read_bytes());a=json.loads((E/'outer_iv_audit.json').read_bytes())
assert r['status']=='COMPUTED_REQUIRES_INDEPENDENT_AUDIT' and a['status']=='PASS'
assert a['primary_result_sha256']==sha(E/'outer_result.json')
assert r['source_sha256']==a['primary_source_sha256']==sha(BASE/'research/outer_majorant/code/certify_outer.py')
assert a['source_sha256']==sha(BASE/'research/outer_majorant/code/audit_outer_iv.py')
assert r['proof_sha256']==a['proof_sha256']==sha(BASE/'research/outer_majorant/PROOF.md')
assert a['enclosure_checks']==4394 and a['exact_C6_join_checks']==1834 and a['exact_Cox_archive_checks']==2096
assert a['exact_Green_polynomial_scalar_checks']==17748 and a['exact_coefficient_scalar_checks']==8908
bounds=[('0','absolute_W','17145164'),('0','weighted_delta_0','5740483'),('0','weighted_delta_1/2','121375357'),('0','weighted_delta_2888063583571445/9007199254740992','40621858'),('9','absolute_W','0.498894793'),('9','weighted_delta_0','0.033247226')]
comparisons=[]
for T,key,upper in bounds:
 pair=[]
 for result in [r,a]:
  case=next(row for row in result['cases'] if row['T_exact']==T)['values'][key]
  lo,hi=F(case['lower_exact']),F(case['upper_exact']);assert 0<=lo<=hi<F(upper)
  pair.append(str(hi))
 comparisons.append({'T_exact':T,'quantity':key,'strict_public_upper_exact':upper,'primary_upper_exact':pair[0],'independent_upper_exact':pair[1]})
for result in [r,a]:
 q=result['exterior_L2_majorant'];assert 0<=F(q['lower_exact'])<=F(q['upper_exact'])<F(4949755)
comparisons.append({'T_exact':'0','quantity':'exterior_L2_majorant','strict_public_upper_exact':'4949755','primary_upper_exact':r['exterior_L2_majorant']['upper_exact'],'independent_upper_exact':a['exterior_L2_majorant']['upper_exact']})
files=['research/outer_majorant/PROOF.md','research/outer_majorant/code/finalize_verdict.py','research/outer_majorant/code/extract_final_span.py','research/outer_majorant/code/certify_outer.py','research/outer_majorant/code/audit_outer_iv.py','research/outer_majorant/evidence/final_span.json','research/outer_majorant/evidence/final_span_extract.json','research/outer_majorant/evidence/exact_outer_coefficients.json','research/outer_majorant/evidence/outer_result.json','research/outer_majorant/evidence/outer_iv_audit.json','research/outer_majorant/evidence/final_proof_serialized_run.json','research/modal_repair/PROOF.md','research/modal_repair/evidence/audit_verdict.json','research/modal_repair/evidence/independent_gauss_iv.json','research/modal_green/PROOF.md','research/middle_residual/PROOF.md','research/middle_residual/code/modal_setup.py','research/middle_residual/code/build_knot_moments.py','research/middle_residual/code/audit_knots.py','research/middle_residual/evidence/setup_checks.json','research/middle_residual/evidence/setup_provenance.json','research/middle_residual/evidence/knot_manifest.json','research/middle_residual/evidence/knot_audit.json','research/ball_transport/PROOF.md','research/ball_transport/code/dyadic_ball.py','notes/reviews/outer_majorant_theorem_closure_metadata.json','notes/reviews/outer_majorant_theorem_closure_response.md','notes/reviews/outer_source_closure2_metadata.json','notes/reviews/outer_source_closure2_response.md']
for tag in ['outer_majorant_theorem_closure','outer_source_closure2']:
 m=json.loads((BASE/f'notes/reviews/{tag}_metadata.json').read_bytes());assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn'
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','method':'Exact affine modal reconstruction and finite Green inverse with Arb384; independent Laurent/Cox reconstruction, backward polynomial recurrence and antiderivative propagation with mpmath.iv160; exact comparisons for seven public bounds; actual Opus5.5 substantive follow-ups.','scope':'Entire exterior zeroth-order absolute, weighted and stated L2 residual majorants for the exact normalized modal trial, with shared previously audited canonical interior moments. Coarse bounds do not close an inverse theorem or prove distance to X3.','actual_review_model':'claude-opus-5-5','checks':r['checks'],'independent_enclosures':a['enclosure_checks'],'public_bound_comparisons':comparisons,'files':{f:sha(BASE/f) for f in files},'archive_sha256':r['dependency_pins']['archive'],'input_sha256':r['dependency_pins']['input']}
(E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'verdict_sha256':sha(E/'verdict.json'),'public_strict_checks':14,'minimum_abs_lower_denominator_exact':r['checks']['minimum_abs_lower_denominator_exact']}))
