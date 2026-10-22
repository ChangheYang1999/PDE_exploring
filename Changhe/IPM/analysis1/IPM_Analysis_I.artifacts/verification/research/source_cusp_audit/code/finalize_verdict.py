"""Pin the reviewed narrow source result; no acceptance of the full cusp theorem."""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert sys.flags.optimize==0
B=Path(__file__).resolve().parents[3];E=B/'research/source_cusp_audit/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
 def bad(x):raise ValueError(x)
 return json.loads(Path(p).read_text(),parse_constant=bad)
proof=B/'research/source_cusp_audit/PROOF.md';e=load(E/'elementary.json');b=load(E/'parameter_box.json')
assert e['status']=='PASS_ELEMENTARY_REQUIRES_REVIEW' and b['status']=='PASS_PARAMETER_BOX_REQUIRES_REVIEW'
assert e['proof_sha256']==b['proof_sha256']==sha(proof)
assert e['source_sha256']==sha(B/'research/source_cusp_audit/code/check_elementary.py') and b['source_sha256']==sha(B/'research/source_cusp_audit/code/check_parameter_box.py')
assert e['lead_snapshot_sha256']==sha(E/'lead_pcusp1_PROOF_snapshot.md')
assert b['modal_source_sha256']==sha(B/'research/modal_source/evidence/source_result.json')=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691'
audit=load(B/'research/modal_source/evidence/output_audit.json');assert audit['verdict']=='PASS' and audit['source_result_sha256']==b['modal_source_sha256']
assert e['polynomial_point_identity_checks']==27 and e['interval_containments']==14 and b['interval_endpoint_containments']==24 and b['input_box_containments']==3
for row in e['rows'].values():
 q=F(row['exact'])
 for eng in ['arb','iv']:assert F(row[eng+'_lower'])<=q<=F(row[eng+'_upper'])
for row in b['rows'].values():
 l,h=F(row['lower_exact']),F(row['upper_exact']);assert l<=h
 for eng in ['arb','iv']:assert F(row[eng+'_lower'])<=l<=h<=F(row[eng+'_upper'])
for row in b['nonresonance']:
 assert row['integer_below']<F(row['lower_exact'])<=F(row['upper_exact'])<row['integer_below']+1
files=['research/source_cusp_audit/PROOF.md','research/source_cusp_audit/code/check_elementary.py','research/source_cusp_audit/code/check_parameter_box.py','research/source_cusp_audit/code/finalize_verdict.py','research/source_cusp_audit/evidence/elementary.json','research/source_cusp_audit/evidence/parameter_box.json','research/source_cusp_audit/evidence/lead_pcusp1_PROOF_snapshot.md','research/canonical_inverse/PROOF.md','research/coupled_thresholds/PROOF.md','research/source_pole/PROOF.md','research/modal_source/PROOF.md','research/modal_source/evidence/source_result.json','research/modal_source/evidence/output_audit.json','research/modal_source/evidence/import_binding_audit.json']
reviews=[]
for tag in ['source_cusp_initial','source_cusp_closure','source_cusp_final']:
 m=B/'notes/reviews'/f'{tag}_metadata.json';r=B/'notes/reviews'/f'{tag}_response.md';j=load(m)
 assert j['actual_response_model']=='claude-opus-5-5' and j['stop_reason']=='end_turn' and r.exists()
 reviews.append({'tag':tag,'actual_model':j['actual_response_model'],'end_utc':j['end_utc']});files.extend([str(m.relative_to(B)),str(r.relative_to(B))])
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_NARROW_SCOPE','confirmed':['Exact frozen Fourier conjugation, semigroup inverse identification in the stated below-threshold graph domain, profile scaling and explicit nonzero profile forcing.','Compact smooth counterexample to the local source condition f_y(P)=0, including paired global parity, x^2 y factor, density germ, raw strain and far-coefficient preservation.','Conditional exponent algebra and strict parameter rectangle/nonresonance for the frozen mu=1 family only.'],'refuted':['Inference from a frozen local cusp theorem to membership in the prompt global P2/P3/P4 classes.','Necessity of the proposed purely local coupled source condition, on the stated exact normalization realization.'],'open':['Full finite-part construction and extension.','Uniform angular/localization and commutator estimates.','Sharp localized Sobolev lower bound and endpoint Holder theorem.','Parity-restricted profile-map codimension.','Actual nonunit-mu and variable-coefficient extension.','Global inverse, proximity to X3, existence, exclusion and decisive endpoint.'],'polynomial_point_checks':27,'exact_illustrative_interval_containments':14,'parameter_endpoint_containments':24,'parameter_source_containments':3,'nonresonance_intervals':4,'scope':'The linked source data are prior independently verified inputs. This calculation does not reintegrate them. Both illustrative decimals and certified rectangle have mu fixed to1; no exact solution parameter is identified. Explicit compact counterexample covers only the listed normalization functionals.','files':{p:sha(B/p) for p in files},'reviews':reviews}
(E/'verdict.json').open('x').write(json.dumps(result,indent=2)+'\n')
text='# Narrow source-cusp audit\n\n'+result['utc']+'; CONFIRMED on the stated narrow scope.\n\nThe Fourier formula, explicit nonzero profile integral and compact coupled-cokernel counterexample are proved in PROOF.md. The paired global perturbation preserves the x^2 y factor, density germ, canonical strain and far coefficients, but gives partial_y(Lbar h)(P)=2g. No global Fredholm index follows.\n\nThe rectangle A in[10.1507252,10.1507253],g in[29.7494906,29.7494908] has strict nonresonance and cusp-exponent margins for frozen mu=1. Fraction assertions and Arb320/iv160 checks passed. This does not replace the actual trial mu by1 or identify an exact solution source.\n\nThe full pcusp1 cusp theorem remains OPEN for its finite-part construction, localization, sharp Sobolev lower bound, endpoint regularity and codimension steps. The claimed inference to global P2/P3/P4 membership is REFUTED; local regularity alone does not establish the global PDE or center condition.\n\nActual Opus5.5 participated in three rounds, ending '+reviews[-1]['end_utc']+'. Source/evidence/reviews are pinned in evidence/verdict.json.\n'
(B/'research/source_cusp_audit/RESULT.md').open('x').write(text)
print(json.dumps({'utc':result['utc'],'status':result['status'],'files':len(files),'verdict_sha256':sha(E/'verdict.json')},indent=2))
