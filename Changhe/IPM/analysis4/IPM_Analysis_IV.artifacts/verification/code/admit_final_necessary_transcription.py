from pathlib import Path
import json
from certificate_admission import stamp,ref,checkref,next_entry
base=Path('research/301_final_claim_audit');p=base/'verification/necessary_radius_transcription.json';d=json.loads(p.read_text())
assert d['all_checks_pass'] and d['count']==50
for r in d['sources']:checkref(r)
ledger,text=next_entry(608);now=stamp()
result='All50 checked printed necessary-radius constants are strictly below the admitted exact lower endpoints: ten branches each at delta2/7,1/4,2/9; fourteen at1/5; three at4/7; and sin7,sin9,sin17. The complete root ordering atQ7 throughQ10 agrees. This is a transcription and downward-rounding audit of the22:18:28 frozen report, with no new gamma-function evaluation.'
scope='CONFIRMED for these50 decimals only. The underlying theorem requires the stated uniform termwise convergence through two angular derivatives; these are necessary bounds, not sufficient or sharp radii.'
receipt=base/'verification/admission_V608.json';receipt.write_text(json.dumps(dict(at=now,entry=608,all_checks_pass=True,checks=ref(p),scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V608 | {now} | Final necessary-radius decimal audit\n\n**Claim.** The50 selected published necessary-radius decimals are valid downward roundings of the admitted directed bounds.\n\n**Method.** Parse the frozen corollary lists, preserve root order and compare exact decimal fractions with each exact rational lower endpoint.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V608,50 necessary-radius decimals pass\n\n{result}\n\n{scope}\n\nOne remaining numerical prose clarification: the sin7 paragraph should say extension from300 to500 rather than doubling; the exact overlap excludes the previously unset g300 harmonic at frequency238, which was separately checked against H300. Source arithmetic is1024bits; the independent audit used2048bits and fit replay3072bits. No precision correction is needed to your1024bit source label.\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V608 confirms50 final necessary-radius downward roundings; notified exact sin7 overlap qualifier and300-to500 wording.'),('VERIFY_SUMMARY.md',f'V608: {result} {scope}')]:
 with Path(name).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/admit_final_necessary_transcription.py').write_bytes(Path(__file__).read_bytes())
print(now,'V608',scope)
