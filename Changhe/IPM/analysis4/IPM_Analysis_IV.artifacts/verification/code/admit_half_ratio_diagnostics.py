"""Admit a finite fit and refute the substitution of its statistic."""
from pathlib import Path
import argparse,json
from certificate_admission import read,ref,checkref,reviewed,stamp,next_entry
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args()
base=Path('research/300_half_ratio_diagnostics');e=base/'verification/checks.json';d=read(e)
assert d['all_replays_overlap'] and d['all_printed_fit_bins_pass'] and d['root_is_strictly_smaller_than_fitted_ratio']
assert d['fit_window']==[200,300] and d['fit_count']==101
assert d['bits']==768 and d['replay_bits']==1536
assert all(r['all_strict'] and r['all_below_constant'] and r['maximizers']==[1] for r in d['nonconstant_column_checks'])
for r in [d['source'],d['source_report']]:checkref(r)
prior=Path('research/291_canonical_half_finite/verification/admission.json');c=read(prior);assert c['all_checks_pass'] and c['verdict']=='CONFIRMED_FINITE'
review=reviewed(base,a.review);ledger,text=next_entry(a.entry);now=stamp()
result=('The consecutive-ratio fit over200..300 has L='+d['fit']['L']+', a='+d['fit']['a']+' and RMS residual '+d['fit']['rms']+'. Its three printed rounding bins pass. At300 the root is '+d['statistics']['root300']+', the actual ratio is '+d['statistics']['ratio300']+' and the fitted ratio is '+d['statistics']['fitted_ratio300']+'. The mean log10 increment over271..300 is '+d['statistics']['mean_step']+'. At every order with nonconstant columns, density9..300 and stream8..300, column1 is the unique nonconstant factorial maximum and is below the constant column. Both centered arithmetic replays agree; actual audit time '+str(d['actual_elapsed_s'])+'seconds.')
scope='Finite fit CONFIRMED under the input enclosure hypothesis. Substituting the root statistic for the consecutive ratio is REFUTED. No limiting ratio, infinite convergence or future-hump claim follows.'
p=base/'PROOF.md';(base/'sources'/f'PROOF_before_V{a.entry}.md').write_bytes(p.read_bytes());s=p.read_text();i=s.index('Status:');j=s.index('\n',i);s=s[:i]+f'Status: finite fit CONFIRMED and root/ratio substitution REFUTED in V{a.entry} on {now}.'+s[j:];s+='\n## Completed verification\n\n'+result+'\n\n'+scope+'\n';p.write_text(s)
snap=base/'sources'/f'PROOF_at_V{a.entry}.md';snap.write_bytes(p.read_bytes());receipt=dict(checked_at_utc=now,ledger=f'V{a.entry}',verdict='CONFIRMED_FINITE',original_claim_verdict='REFUTED',all_checks_pass=True,evidence=ref(e),prior_admission=ref(prior),proof=ref(snap),independent_review=ref(review),scope=scope);out=base/'verification/admission.json';out.write_text(json.dumps(receipt,indent=2)+'\n')
ledger.write_text(text+f'\n## V{a.entry} | {now} | Half-exponent ratio and root statistics\n\n**Claim.** The canonical half-exponent root and ratio obey the same fitted law L(1-a/n).\n\n**Method.** Exact telescoping-product identity, independent centered interval regression at768 and1536bits on101 ratios, and complete stored factorial-maximizer checks.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {out}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD, NUMERICS: V{a.entry} half-exponent ratio fit and wording\n\n{result}\n\n{scope}\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V{a.entry} admitted the half-exponent finite fit and corrected root/ratio substitution.'),('VERIFY_SUMMARY.md',f'V{a.entry}: {result} {scope}'),('research/INDEX.md',f'Update {now}:300 admitted inV{a.entry}, finite only.')]:
 with Path(name).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/admit_half_ratio_diagnostics.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(dict(at=now,entry=a.entry,result=result)))
