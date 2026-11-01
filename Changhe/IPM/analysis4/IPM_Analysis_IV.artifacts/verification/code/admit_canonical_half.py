"""Admit finite checks at delta one half without asserting a tail bound."""
from pathlib import Path
from hashlib import sha256
import argparse,json
from flint import arb,ctx
from certificate_admission import read,ref,checkref,reviewed,stamp,next_entry
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args();ctx.prec=1024
base=Path('research/291_canonical_half_finite');v=base/'verification'
c=read(v/'checks.json');n=read(v/'nonlinear_checks.json');m=read(v/'input_manifest.json');p=read(v/'exact_prefix.json')
assert c['all_checks_pass'] and n['all_checks_pass'] and n['complete_requested_orders'] and p['all_checks_pass']
assert c['maximum_order']==300 and p['orders']==12 and c['bits']==n['bits']==768
assert c['source_sha256']==n['source_sha256']==m['source_sha256']
assert sha256(Path(m['source']).read_bytes()).hexdigest()==m['source_sha256']
for r in c['sources']+[c['exact_prefix']]:checkref(r)
assert [r['n'] for r in c['rows']]==list(range(1,301))
assert [r['n'] for r in n['orders']]==[8,12,20,40,80,160,300]
assert all(r['all_contain_zero'] and r['ordered_pairs']==r['n']-1 and r['kronecker_stride']==4*r['n']+5 for r in n['orders'])
assert c['maximum_printed_log_error']<2e-10
assert c['poisson_coefficients']==sum(r['poisson']['coefficients'] for r in c['rows'])
assert c['canonical_constants']==sum(r['poisson']['canonical_constants'] for r in c['rows'])
late=[r for r in c['rows'] if r['n']>=200]
for row in late:
 f=row['fields']['f'];assert f['maximum_strictly_certified']
 assert arb(f['nonconstant_factorial_ratio'])<1 if f['nonconstant_below_constant'] else True
last=c['rows'][-1];maxima=c['late_density_nonconstant_maximizers'];strict=c['late_density_maximizers_strict'];below=c['late_density_nonconstant_below_constant']
assert maxima==sorted({r['fields']['f']['nonconstant_factorial_maximizer'] for r in late})
review=reviewed(base,a.review);now=stamp();ledger,old=next_entry(a.entry)
result=(f"The unit-amplitude canonical delta1/2 checkpoint through300 passes{c['poisson_coefficients']} polynomial Poisson coefficient checks and{c['canonical_constants']} zero free-harmonic tests. Its exact independent Cartesian prefix through12 agrees in{c['exact_prefix_comparisons']} coefficients, with its common potential reconstructed. Norms use{c['norm_coefficient_positions']} stored coefficient positions; all{c['printed_comparisons']} compared printed logarithms agree within{c['maximum_printed_log_error']:.6g}. The density root at300 is{last['fields']['f']['root']}; the log10 stream/density norm ratio is{last['log10_N_over_M']}. Over200..300 the maximizing nonconstant factorial column indices are{maxima}, strict at every order:{strict}, with every maximum below the constant column:{below}. The order300 log10 factorial ratio is{last['fields']['f']['log10_nonconstant_factorial_ratio']}. The maximum column-relative input radius is{c['maximum_column_relative_radius']}, at{c['maximum_column_relative_location']}; zero-center nonzero-radius columns:{len(c['zero_center_nonzero_radius_columns'])}. Complete nonlinear sums at8,12,20,40,80,160,300 check{sum(r['ordered_pairs'] for r in n['orders'])} ordered pairs and{sum(r['checked_coefficients'] for r in n['orders'])} residual coefficients. Norm/Poisson audit time{c['actual_elapsed_s']:.6f}seconds; nonlinear audit time{n['actual_elapsed_s']:.6f}seconds.")
scope='CONFIRMED as finite arithmetic and independent residual consistency under the supplied coefficient-enclosure hypothesis. The exact prefix through12 is unconditional rational algebra. No infinite logarithmic-series convergence, asymptotic law, or uncomputed error propagation is inferred.'
proof=base/'PROOF.md';before=base/'sources'/f'PROOF_before_V{a.entry}.md';before.write_bytes(proof.read_bytes());text=proof.read_text();start=text.index('Status:');end=text.index('\n',start)
text=text[:start]+f'Status: finite verification CONFIRMED in V{a.entry} on {now}, with the hypotheses and limitations below.'+text[end:]+f'\n## Completed checks\n\n{result}\n\n{scope}\n';proof.write_text(text)
snapshot=base/'sources'/f'PROOF_at_V{a.entry}.md';snapshot.write_bytes(proof.read_bytes())
receipt=dict(at=now,entry=a.entry,all_checks_pass=True,verdict='CONFIRMED_FINITE',evidence=ref(v/'checks.json'),nonlinear=ref(v/'nonlinear_checks.json'),input_manifest=ref(v/'input_manifest.json'),exact_prefix=ref(v/'exact_prefix.json'),proof=ref(snapshot),independent_review=ref(review),scope=scope)
(v/'admission.json').write_text(json.dumps(receipt,indent=2)+'\n')
ledger.write_text(old+f'\n## V{a.entry} | {now} | Canonical half-exponent finite audit through300\n\n**Claim.** The canonical unit-sine delta1/2 checkpoint through300 is consistent with the stated recurrence and its printed finite diagnostics.\n\n**Method.** Independent exact Cartesian prefix and potential reconstruction, dyadic input decoding,768-bit full polynomial Poisson checks, factorial-weighted column comparisons and selected complete Cartesian nonlinear products. The lead reviewed the written protocol.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {v}/admission.json.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> TEAM: V{a.entry}, canonical delta1/2 finite checks\n\n{result}\n\n{scope}\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V{a.entry} admitted canonical delta1/2 finite arithmetic through300.'),('VERIFY_SUMMARY.md',f'V{a.entry}: {result} {scope}'),('research/INDEX.md',f'Update {now}:291 finite audit admittedV{a.entry}; infinite canonical convergence remains OPEN.')]:
 with Path(name).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/admit_canonical_half.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(dict(at=now,entry=a.entry,result=result)))
