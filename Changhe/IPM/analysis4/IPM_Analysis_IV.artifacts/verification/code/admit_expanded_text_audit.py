"""Reject the invalid prototype and admit the tested expanded text inventory."""
from pathlib import Path
import json,re,sys
sys.path.insert(0,'code')
from certificate_admission import stamp,ref,next_entry
base=Path('research/301_final_claim_audit')
old=Path('artifacts/final_audit/expanded_text_hygiene_20261031T234620Z.json')
new=Path('artifacts/final_audit/expanded_text_hygiene_20261031T234744Z.json')
d=json.loads(new.read_text());assert d['files_with_hits']==4 and not d['decoding_errors']
assert sum(len(r['hits']) for r in d['hits'])==38
manifest=json.loads(Path('artifacts/publication/source_projection_manifest.json').read_text())
projection=max(Path('artifacts/final_audit').glob('*/publication_projection_checks.json'),key=lambda p:p.stat().st_mtime)
pj=json.loads(projection.read_text());assert pj['all_checks_pass']
now=stamp()
claim='The prototype expanded scan at23:46:20 establishes that the selected text has no local paths.'
result='REFUTED. The prototype regular expression requires literal question marks next to slashes, so it misses ordinary and JSON-escaped local paths. Its zero-hit result is invalid and is superseded by the tested scan at23:47:44. This is a publication-inventory defect, not a change to any mathematical or numerical admission.'
ledger,text=next_entry(648)
p=base/'verification/admission_V648.json'
p.write_text(json.dumps(dict(at=now,entry=648,verdict='REFUTED',claim=claim,result=result,invalid_scan=ref(old),replacement_scan=ref(new)),indent=2)+'\n')
ledger.write_text(text+f'\n## V648 | {now} | Invalid prototype path scan\n\n**Claim.** {claim}\n\n**Method.** Inspect the regular expression and test literal and JSON-escaped path separators against the known producer transcripts.\n\n**Result.** {result}\n\n**Verdict: REFUTED.** Evidence: {p}.\n')
claim='The corrected expanded scan covers the listed small text artifacts and has only the four documented source-transcript exceptions.'
result=f"The tested scanner checks {d['checked_files']} files and {d['checked_bytes']} bytes, including artifact JSON and JSONL. It finds four source transcripts and38 affected diagnostic lines, with no other matches and no UTF-8 errors. The separate projection check validates all four original and publication-copy pairs:38 changed diagnostic lines and1268 unchanged lines. The scope excludes code, scratch, task specifications, raw shifts, compressed evidence and binary files; compressed text has a separate inventory."
with (base/'PROOF.md').open('a') as f:f.write(f'\n## Expanded text-inventory verification, {now}\n\nFor the finite selected set, the scanner decodes UTF-8 and normalizes JSON-escaped slashes before matching a local path root or an em dash. Positive and negative separator controls execute before the scan. Every matching line is retained in the inventory. The four known original transcripts are excluded from publication and replaced using the byte-preservation projection check. This finite text check proves only the recorded inventory properties. It proves no mathematical assertion.\n\n{result}\n')
proof=base/'sources/PROOF_at_V649.md';proof.write_bytes((base/'PROOF.md').read_bytes())
ledger,text=next_entry(649);p=base/'verification/admission_V649.json'
p.write_text(json.dumps(dict(at=now,entry=649,verdict='CONFIRMED',all_checks_pass=True,claim=claim,result=result,scan=ref(new),projection=ref(projection),proof=ref(proof),scanner=ref('code/final_expanded_text_audit.py')),indent=2)+'\n')
ledger.write_text(text+f'\n## V649 | {now} | Expanded publication text inventory\n\n**Claim.** {claim}\n\n**Method.** Test literal and escaped separator controls, enumerate the finite text selection, and independently compare the publication projections.\n\n**Result.** {result}\n\n**Verdict: CONFIRMED.** This is a finite inventory check only. Evidence: {p}.\n')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V647 admitted Q9 root9. V648 rejects the untested prototype path regex; V649 admits the corrected expanded inventory and four byte-preserving publication projections.\n')
print(now,result)
