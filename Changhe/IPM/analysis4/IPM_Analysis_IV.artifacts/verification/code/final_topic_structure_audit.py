"""Check topic proof/index presence; retain a missing-link repair as evidence."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re,sys
sys.dont_write_bytecode=True
from certificate_admission import stamp,ref,next_entry
root=Path('research');index=root/'INDEX.md';before=index.read_text()
needle='2026-10-31T21:40:13+00:00: topic298 records the finite Q10 floating audit protocol'
assert needle in before
repaired=before.replace(needle,'2026-10-31T21:40:13+00:00: [topic298](298_period_ten_floating_audit/PROOF.md) records the finite Q10 floating audit protocol',1)
base=root/'301_final_claim_audit';now=stamp();rows=[]
for p in sorted(root.iterdir()):
 if not p.is_dir() or not re.match(r'^\d+_',p.name):continue
 q=p/'PROOF.md';name=p.name+'/PROOF.md'
 rows.append(dict(topic=int(p.name.split('_')[0]),directory=str(p),proof_exists=q.is_file(),proof_bytes=q.stat().st_size if q.is_file() else None,proof_sha256=sha256(q.read_bytes()).hexdigest() if q.is_file() else None,indexed_before=name in before,indexed_after=name in repaired,subdirectories=[c.name for c in sorted(p.iterdir()) if c.is_dir()]))
assert sorted(r['topic'] for r in rows)==list(range(1,308))
assert [r['topic'] for r in rows if not r['indexed_before']]==[298]
assert all(r['proof_exists'] and r['proof_bytes']>100 and r['indexed_after'] for r in rows)
ledger,text=next_entry(655)
index.write_text(repaired)
result='All307 numbered topic directories contain a nonempty PROOF.md. The initial structural test found one missing clickable reading-index link, topic298; its proof already existed and was linked in the claim map. The index reference is now clickable, and all307 proof paths are indexed. The chronological text and every mathematical proof are unchanged.'
scope='CONFIRMED for file and reading-index structure after repair. Presence is not a fresh reading, mathematical proof audit or numerical replay.'
with (base/'PROOF.md').open('a') as f:f.write(f'\n## Reading-index completeness, {now}\n\nEnumerate the numbered topic directories and require exactly the integers1 through307. Check that each contains a nonempty standalone proof and that the index contains its exact relative proof path. This finite structural comparison found only the missing topic298 hyperlink. Adding that link leaves the mathematical text unchanged.\n\n{result}\n\n{scope}\n')
proof=base/'sources/PROOF_at_V655.md';proof.write_bytes((base/'PROOF.md').read_bytes())
code=base/'sources/final_topic_structure_audit.py';code.write_bytes(Path(__file__).read_bytes())
p=base/'verification/admission_V655.json';p.write_text(json.dumps(dict(at=now,entry=655,verdict='CONFIRMED',all_checks_pass=True,topic_count=307,index_before_sha256=sha256(before.encode()).hexdigest(),index_after_sha256=sha256(repaired.encode()).hexdigest(),changed_before=needle,changed_after=needle.replace('topic298','[topic298](298_period_ten_floating_audit/PROOF.md)'),rows=rows,proof=ref(proof),algorithm=ref(code),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V655 | {now} | Reading-index structural completeness\n\n**Claim.** Every numbered research topic has a standalone proof and a clickable index entry.\n\n**Method.** Enumerate all307 directories, inspect proof presence and exact index paths, and repair the sole missing hyperlink.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V655 adds missing topic298 hyperlink and confirms307 indexed standalone proofs.\n')
print(now,result)
