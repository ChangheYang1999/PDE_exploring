"""Check the narrow text repairs requested in V607, V608 and V611."""
from pathlib import Path
import json
from certificate_admission import stamp,ref,next_entry
base=Path('research/301_final_claim_audit');now=stamp();ledger,text=next_entry(613)
inputs={'theory':Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md'),'summary':Path('../a4-lead/FINAL_SUMMARY.md'),'numerics':Path('../a4-lead/report_parts/numerics.md'),'report':Path('../a4-lead/FINAL_REPORT.md')}
snaps={}
for name,p in inputs.items():
 raw=p.read_bytes();assert raw==p.read_bytes()
 out=base/'sources'/f'{name}_at_V613.md';out.write_bytes(raw);snaps[name]=out
s={k:p.read_text() for k,p in snaps.items()}
integer='$c=2N+\\sqrt5$, $N\\in\\mathbb Z$, $N\\ge16$'
assert integer in s['theory'] and integer in s['report']
assert 'by less than $3.8\\%$' in s['summary']
assert 'about $3.71\\%$' in s['numerics']
assert 'extending the run from order 300 to 500' in s['numerics']
assert 'where the free stream harmonic at order 300, not yet set in the earlier run, was checked separately' in s['numerics']
assert 'covers every order below the first stream resonance' in s['summary']
assert 'When the first condition holds and every later response $\\sigma_k$ is' in s['theory']
assert 'The prime-denominator parameters of Theorems P and P\' are dense' in s['theory']
result='The frozen theory and report now require integer N in the explicit large-c family. The summary uses a strict 3.8% bound and the numerics uses about 3.71%, both consistent with the admitted 3.712335% finite maximum. The sin7 text says extension from300 to500 and separately identifies the previously unset order300 stream harmonic. The summary restricts the Candidate finite majorant to orders below the first resonance. Theory introductory wording now retains the nonzero later-response condition and attributes density to the prime-denominator theorems.'
scope='CONFIRMED for these text repairs only. V607 and V611 refutations of the superseded wording remain in the ledger. This is not an admission of all statements in the frozen files.'
with (base/'PROOF.md').open('a') as f:f.write('\n## Narrow wording repair, V613\n\nThe integer restriction excludes the rational counterexample in topic302. The certified finite maximum in V611 is below0.038 but above0.037, so less than3.8% is a valid upper bound while about3.71% is an approximation. The sin7 overlap excludes a harmonic not present in the old snapshot. First compatibility alone does not imply later nonzero responses, and a below-resonance majorant makes no assertion at the resonance. These are scope repairs, not new convergence arguments.\n')
proof=base/'sources/PROOF_at_V613.md';proof.write_bytes((base/'PROOF.md').read_bytes())
receipt=base/'verification/admission_V613.json';receipt.write_text(json.dumps(dict(at=now,entry=613,all_checks_pass=True,snapshots={k:ref(p) for k,p in snaps.items()},proof=ref(proof),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V613 | {now} | Final wording repairs\n\n**Claim.** The current text repairs the specified hypotheses, finite-fit bound and overlap qualifications.\n\n**Method.** Freeze the four current documents and compare the exact revised statements with the admitted counterexample, directed finite bounds and overlap checks.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: V613 confirms final wording repairs\n\n{result}\n\n{scope}\n\n'+p.read_text())
for name,line in [('WORKLOG.md',f'{now}: V613 confirms the specified final wording repairs.'),('VERIFY_SUMMARY.md',f'V613: {result} {scope}')]:
 with Path(name).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/admit_final_wording_repairs.py').write_bytes(Path(__file__).read_bytes())
print(now,'V613',scope)
