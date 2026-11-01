"""Close current mapped proof-text coverage after the final Q9 admission."""
from pathlib import Path
from hashlib import sha256
import json,re,sys
sys.path.insert(0,'code')
from certificate_admission import stamp,ref,next_entry,checkref
base=Path('research/301_final_claim_audit');oldp=base/'verification/admission_V635.json';old=json.loads(oldp.read_text())
oldrows={r['path']:r for r in old['checked_proofs']}
paths=list(dict.fromkeys(re.findall(r'\]\(([^)]+/PROOF\.md)\)',Path('FINAL_CLAIM_MAP.md').read_text())))
assert len(paths)==135 and len(oldrows)==134
unchanged=[];changed=[];added=[]
for name in paths:
 r=ref(name)
 if name in oldrows:
  if r['sha256']==oldrows[name]['sha256']:unchanged.append(name)
  else:changed.append(r)
 else:added.append(r)
assert len(unchanged)==133 and len(changed)==1 and '/303_' in changed[0]['path'] and len(added)==1 and '/307_' in added[0]['path']
now=stamp();snapshots=[]
for r in changed+added:
 topic=Path(r['path']).parent.name.split('_')[0]
 p=base/'sources'/f'proof{topic}_at_V652.md';p.write_bytes(Path(r['path']).read_bytes());snapshots.append(dict(original_path=r['path'],snapshot=ref(p)))
result='All135 current standalone proof links are covered. Of the134 files read at V635,133 remain byte-identical. The complete topic303 protocol and later finite Q9 admission appendices have been reread through V650; the added topic307 proof and V643 repair closure have also been read in full. These two current texts are preserved as immutable snapshots. Their added content changes finite diagnostic checks, not the infinite convergence theorems.'
scope='CONFIRMED for current proof-text identity and reading coverage. This does not claim a fresh replay of every historical arithmetic certificate or a new complete reading of the assembled report.'
with (base/'PROOF.md').open('a') as f:f.write(f'\n## Final mapped proof-text coverage, {now}\n\nCompare each current proof hash to the V635 inventory. An unchanged hash transfers only the recorded reading coverage, not a new computation. Read each changed or added proof in full and retain it separately. The resulting partition has133 unchanged proofs, one updated protocol and one added numerical-scope proof.\n\n{result}\n\n{scope}\n')
proof=base/'sources/PROOF_at_V652.md';proof.write_bytes((base/'PROOF.md').read_bytes())
ledger,text=next_entry(652);p=base/'verification/admission_V652.json'
p.write_text(json.dumps(dict(at=now,entry=652,verdict='CONFIRMED',all_checks_pass=True,previous_inventory=ref(oldp),current_map=ref('FINAL_CLAIM_MAP.md'),unchanged_proofs=unchanged,changed_and_added_snapshots=snapshots,proof=ref(proof),result=result,scope=scope),indent=2)+'\n')
# The live map may change later. Preserve this exact inventory map first.
mp=base/'sources/claim_map_at_V652.md';mp.write_bytes(Path('FINAL_CLAIM_MAP.md').read_bytes());d=json.loads(p.read_text());d['current_map']=ref(mp);p.write_text(json.dumps(d,indent=2)+'\n')
ledger.write_text(text+f'\n## V652 | {now} | Current mapped proof-text coverage\n\n**Claim.** Every current standalone proof linked in the claim map has a recorded complete reading.\n\n**Method.** Compare all current hashes with V635 and reread the changed or added texts; preserve immutable snapshots.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V652 closes135 current mapped proof readings:133 unchanged,303 updated and307 added.\n')
print(now,result)
