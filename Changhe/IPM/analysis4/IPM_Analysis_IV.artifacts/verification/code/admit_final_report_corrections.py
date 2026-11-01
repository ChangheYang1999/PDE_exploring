"""Admit the final exact Candidate extraction and two report corrections."""
from pathlib import Path
import argparse,json
from certificate_admission import read,ref,checkref,reviewed,admit
ap=argparse.ArgumentParser();ap.add_argument('--topic',type=int,choices=[295,296,297],required=True);ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args()
if a.topic==295:
 base=Path('research/295_candidate_publication_audit');evidence=base/'verification/checks.json';d=read(evidence)
 assert d['all_checks_pass'] and d['branch_zero_generators']==416
 assert all(d[k]==10 for k in ['nonzero_potential_moments','density_coefficients','stream_coefficients','poisson_identities','publication_rational_pairs'])
 for r in d['inputs']+[d['publication_excerpt']]:checkref(r)
 result='Direct rational polar differentiation agrees with all416 branch-zero generators, ten nonzero potential moments, ten density coefficients, ten stream coefficients, ten Poisson identities and all ten published exact numerator/denominator pairs in the frozen Section8.5. Source, manifest and sector-table hashes match. The exact parameter is c=4076476460239181/2251799813685248, delta=1824676646553933/4076476460239181. Arithmetic runtime '+str(d['actual_elapsed_s'])+'seconds.'
 title='Candidate007 final exact input and publication transcription'
 claim='The archived leading profile, parameter and published exact coefficient table agree with the authoritative Candidate007 generators.'
 method='Independently sum branch-zero generators and differentiate their polar homogeneous terms with Fraction arithmetic, then compare all exact moments, density/stream coefficients, Poisson identities, input hashes and frozen table pairs.'
 scope='The finite input and transcription identities are PROVED. This does not establish exact stationarity of the candidate, compatibility at its first resonance, or infinite convergence at its stored rational exponent.'
elif a.topic==296:
 base=Path('research/296_primary_weight_amplitude');evidence=base/'verification/checks.json';d=read(evidence)
 assert d['all_checks_pass']
 title='Primary-weight conversion at nonunit amplitude'
 claim='After setting z=|epsilon|r^(-delta), division by z alone converts the unnormalized r^(-1) density and r^(-2) stream remainder bounds to the primary radial weights.'
 method='Take the exact ratio of radial powers, then test the universal conversion at delta1/2, epsilon2, r16 and the third homogeneous density term. Independently review the scope against the frozen report paragraph.'
 result='The correct conversion factor is |epsilon|/z=r^delta. The rational test gives old density weight1/8, primary weight1/2 and z1/2; division by z gives1/4, whereas multiplication by |epsilon|/z gives1/2. The original division rule is valid at unit amplitude or with an additionally amplitude-normalized left side.'
 scope='The unqualified division-by-z rule is REFUTED; the corrected identity is PROVED. All unit-amplitude displayed examples and certified radius exponents remain unchanged. No failure of a particular loose majorant is inferred from this normalization test.'
else:
 base=Path('research/297_asymptotic_growth_discontinuity');evidence=base/'verification/proof_scope.json';d=read(evidence)
 for r in d['files']:checkref(r)
 title='Discontinuity of the actual asymptotic growth constant'
 claim='For a finite odd sine profile with nonzero first harmonic, the actual coefficient-growth limsup varies smoothly over the nonresonant exponent parameters.'
 method='Combine the admitted Brjuno convergence theorem with the admitted dense-G_delta zero-radius theorem, and apply the Banach-valued Cauchy-Hadamard formula and the definition of continuity.'
 result='A(delta)=limsup ||f_n(delta)||_1^(1/n) is finite at every Brjuno delta/2 and infinite on a dense G_delta set of irrational delta. Therefore it is discontinuous at every Brjuno point and nowhere locally bounded on the full irrational parameter set. The same holds in c=1/(1-delta). Fixed finite coefficients and finite fitted statistics can still vary continuously away from their finitely many poles.'
 scope='The universal smoothness interpretation is REFUTED; the stated discontinuity consequence is PROVED. The report must attribute its observed mild parameter dependence to finite fitted estimates only. No discontinuity classification at infinite-valued points or on a restricted Brjuno sublevel set follows.'
review=reviewed(base,a.review)
admit(base,a.entry,title,claim,method,result,scope,evidence,review)
if a.topic in [296,297]:
 ledger=Path('VERIFY_REPORT.md');text=ledger.read_text();head,tail=text.rsplit(f'## V{a.entry} |',1)
 tail=tail.replace('**Verdict: CONFIRMED.**','**Verdict: REFUTED as written; correction CONFIRMED.**',1)
 ledger.write_text(head+f'## V{a.entry} |'+tail)
 receipt=base/'verification/admission.json';r=json.loads(receipt.read_text());r['original_claim_verdict']='REFUTED';r['corrected_statement_verdict']='PROVED';receipt.write_text(json.dumps(r,indent=2)+'\n')
(base/'sources/admit_final_report_corrections.py').write_bytes(Path(__file__).read_bytes())
