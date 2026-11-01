"""Admit proof-text coverage with immutable reading records and explicit scope."""
from pathlib import Path
from hashlib import sha256
import json,re
from certificate_admission import stamp,ref,next_entry
base=Path('research/301_final_claim_audit');v=635
ledger,text=next_entry(v);now=stamp()
pre_path=base/'verification/pre_freeze_reading_record.json';post_path=base/'verification/post_freeze_reading_record.json'
pre=json.loads(pre_path.read_text());post=json.loads(post_path.read_text())
p=Path('research/300_half_ratio_diagnostics/PROOF.md')
assert not any(int(r['topic'])==300 for r in post['items'])
post['items'].append(dict(topic='300',path=str(p),sha256=sha256(p.read_bytes()).hexdigest(),recorded_at=now,review_note='Reread the complete updated proof, including the V624 finite counterexample to a universal minus0.70 log increment. The telescoping ratio identity, ratio-versus-root distinction and exact finite window remain correct.',new_defect_found=False,also_in_pre_freeze_record=True))
post['recorded_at']=now;post_path.write_text(json.dumps(post,indent=2)+'\n')
paths=list(dict.fromkeys(re.findall(r'\]\((research/\d+_[^)]+/PROOF.md)\)',Path('FINAL_CLAIM_MAP.md').read_text())))
latest={int(r['topic']):r for d in (pre,post) for r in d['items']}
checks=[]
for path in paths:
 topic=int(path.split('/')[1].split('_')[0]);r=latest[topic]
 assert r['path']==path
 assert sha256(Path(path).read_bytes()).hexdigest()==r['sha256'],path
 assert r['new_defect_found'] is False
 checks.append(dict(topic=topic,path=path,sha256=r['sha256']))
assert len(paths)==134 and len(pre['items'])==68 and len(post['items'])==70 and len(latest)==136
copies=[]
for src,name in [(pre_path,'pre_readings'),(post_path,'post_readings'),(Path('FINAL_CLAIM_MAP.md'),'claim_map')]:
 out=base/'sources'/f'{name}_at_V{v}{src.suffix}';out.write_bytes(src.read_bytes());copies.append(ref(out))
proof=base/'sources'/f'PROOF_at_V{v}.md';proof.write_bytes((base/'PROOF.md').read_bytes())
scope='CONFIRMED for coverage and scope of the specified proof-text readings. No new theorem, full-report reread or fresh replay of all arithmetic certificates is claimed. Later appended proofs require separate checks.'
result='All134 distinct standalone proofs linked from the frozen claim map have a completed reading record matching their current bytes. The records contain68 historical and70 additional readings, covering136 distinct topics in total. Every complete reread has its examined hypotheses recorded; no new mathematical defect was found in this additional pass. Topic300 was reread after its finite-rate counterexample was appended.'
receipt=base/'verification'/f'admission_V{v}.json';receipt.write_text(json.dumps(dict(at=now,entry=v,all_checks_pass=True,records=copies,proof=ref(proof),mapped_proof_count=len(paths),pre_reading_count=68,additional_reading_count=70,distinct_reading_topics=136,checked_proofs=checks,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V{v} | {now} | Complete claim-map proof reading coverage\n\n**Claim.** Every standalone proof linked in the frozen claim map has been fully reread with its scope recorded.\n\n**Method.** Complete manual readings, normalized topic identifiers, immutable reading records and SHA-256 comparison against every linked proof.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V{v}, complete claim-map proof reading coverage\n\n{result}\n\n{scope} V632 still requests the three Q10 outward endpoint repairs. Q9roots1..2 are admitted; later cases remain pending.\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V{v} admits complete coverage of134 linked proof texts using68 historical and70 additional readings. No new all-certificate replay or full-report reread is asserted.\n')
(base/'sources/admit_final_reading_coverage.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
