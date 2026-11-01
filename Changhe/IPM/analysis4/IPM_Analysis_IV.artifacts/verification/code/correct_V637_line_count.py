"""Keep the original receipt and append its clerical line-count correction."""
from pathlib import Path
import json
from certificate_admission import ref,next_entry,stamp
from reconstruct_text_delta import reconstruct
base=Path('research/301_final_claim_audit')
source=base/'verification/post_freeze_20261031T233028Z/summary.json'
raw=reconstruct(source);count=len(raw.decode().splitlines());assert count==502
old=base/'verification/admission_V637.json';d=json.loads(old.read_text())
assert d['summary_line_count']==502 and '511-line' in d['result']
ledger,text=next_entry(638);now=stamp()
result=('V637 correctly stored summary_line_count=502 but accidentally called the same document a 511-line summary in its result prose. '
        'The exact reconstructed summary contains502 lines. The entire document was read; the statement about reading coverage is unchanged. '
        'The original receipt is retained, and this entry corrects its clerical number.')
receipt=base/'verification/admission_V638.json';receipt.write_text(json.dumps(dict(at=now,entry=638,verdict='CONFIRMED',corrected_line_count=count,incorrect_prose_count=511,source=ref(source),original_receipt=ref(old),result=result,scope='Clerical evidence metadata only; no mathematical claim changed.'),indent=2)+'\n')
ledger.write_text(text+f'\n## V638 | {now} | V637 summary line-count correction\n\n**Claim.** The summary read in V637 had511 lines.\n\n**Method.** Reconstruct the exact summary bytes from the stored hash-bound delta and count splitlines.\n\n**Result.** {result}\n\n**Verdict: REFUTED for511; CONFIRMED for502.** Evidence: {receipt}.\n')
with (base/'PROOF.md').open('a') as f:f.write(f'\n## Clerical correction, V638\n\n{now}. {result}\n')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V638 corrects V637 prose line count511 to502 while retaining the original receipt. Evidence audit23:31:39 passes103 receipts and652 references:647 direct,4 historical and1 lossless.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: clerical correction to V637\n\nV637 read the complete502-line summary; its result prose accidentally said511. The receipt already stored502. V638 records the correction without altering the original receipt. No mathematical scope or verdict changed. The current evidence audit passes all652 references across103 receipts.\n\n'+p.read_text())
p=Path('code/admit_Q10_prose_repair.py');s=p.read_text().replace("'The entire current 511-line summary was reread", "f'The entire current {len(summary.splitlines())}-line summary was reread")
p.write_text(s)
print(now,result)
