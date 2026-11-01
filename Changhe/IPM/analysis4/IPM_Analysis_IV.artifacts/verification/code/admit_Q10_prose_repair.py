"""Record the checked Q10 range repair and the complete summary reread."""
from pathlib import Path
from hashlib import sha256
import json
from flint import arb,ctx
from certificate_admission import ref,checkref,next_entry,stamp
from reconstruct_text_delta import reconstruct
ctx.prec=512
base=Path('research/301_final_claim_audit')
folder=base/'verification/post_freeze_20261031T233028Z'
manifest=json.loads((folder/'manifest.json').read_text())
for r in manifest['documents']:
    checkref(r);d=json.loads(Path(r['path']).read_text())
    assert reconstruct(r['path'])==Path(d['live_name']).read_bytes()
summary=reconstruct(folder/'summary.json').decode()
report=reconstruct(folder/'report.json').decode()
for pair in ['$5.224$ to $5.286$','$1.341$ to $1.348$','$0.9218$ to $0.9265$']:
    assert pair in report
for pair in ['$5.224$ to $5.285$','$1.341$ to $1.347$','$0.9219$ to $0.9265$']:
    assert pair not in report
assert 'less than $7.1\\%$, mostly downward' in summary
assert 'no bound on the true radius' in report
assert 'double-precision tuned runs with their fits' in report
support=[base/'verification/admission_V633.json',base/'verification/admission_V635.json',base/'verification/admission_V629.json']
for p in support:assert p.is_file()
ledger,text=next_entry(637);now=stamp()
result=('The latest Q10 paragraph uses all three corrected outward endpoints from V632. V633 supplies the exact-decimal fit checks for all fourteen ranges and the strict 2%, 7.1% and 31% finite bounds. '
        'The new artifact-list wording is consistent with the listed tuned-series computations. The entire current 511-line summary was reread across this final pass, alongside the earlier full rereads of all134 mapped standalone proofs. '
        'No additional mathematical scope defect was found. The summary changes relative to V617 consist of the dated header, the Q10 finite-radius range and drift sentence, and the already checked order440 paragraph.')
scope=('CONFIRMED for these document edits and their finite numerical provenance. The full 6423-line assembled report was not reread line by line in this pass; its changed blocks and the mapped proofs were checked. '
       'The proof rereads do not constitute a fresh replay of every historical numerical certificate. The Q10 data remain floating finite-order evidence, and the canonical logarithmic series remains OPEN.')
proof=base/'PROOF.md';proof.write_text(proof.read_text()+f'\n## Q10 range repair and complete summary reread, V637\n\n{now}. {result}\n\n{scope}\n\nThe historical pre-repair report is reconstructed exactly by sources/report_at_V632_delta.json, whose SHA-256 equals the source hash in the unmodified V632 receipt. The new range comparison is therefore auditable even after the live report changes.\n')
snapshot=base/'sources/PROOF_at_V637.md';snapshot.write_bytes(proof.read_bytes())
receipt=base/'verification/admission_V637.json';receipt.write_text(json.dumps(dict(at=now,entry=637,verdict='CONFIRMED',all_checks_pass=True,changes=manifest['documents'],support=[ref(p) for p in support],historical_report_delta=ref(base/'sources/report_at_V632_delta.json'),proof=ref(snapshot),summary_line_count=len(summary.splitlines()),report_line_count=len(report.splitlines()),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V637 | {now} | Q10 repaired ranges and complete summary reread\n\n**Claim.** The final Q10 wording incorporates the outward-range corrections and preserves the finite scope.\n\n**Method.** Reconstruct and hash the V617-to-current deltas, inspect every changed block, compare the three repaired endpoints with V632/V633, and reread the entire current summary against the mapped standalone proofs.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
note=f'## {now} VERIFIER -> LEAD: V637 closes the Q10 range repair\n\nAll three repaired Q10 endpoints match V632/V633. The whole current summary has been reread; no new scope defect was found. All134 mapped standalone proofs were reread in V635. Changed report blocks are checked, without claiming a fresh line-by-line reading of all6423 report lines or replay of every old certificate. The exact pre-repair report hash from V632 is now reconstructible from a compact delta, so the historical audit is preserved. Q9 roots1..3 are admitted; the remaining queue is being monitored.\n\n'
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V637 closes the corrected Q10 ranges and records a complete current-summary reread; exact historical V632 report preserved by delta.\n')
(base/'sources/admit_Q10_prose_repair.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
