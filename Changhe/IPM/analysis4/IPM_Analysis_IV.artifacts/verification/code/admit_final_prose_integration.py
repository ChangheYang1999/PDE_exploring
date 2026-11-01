"""Check the explicit post-freeze order440 and finite-rate wording changes."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from certificate_admission import next_entry,ref,checkref
base=Path('research/301_final_claim_audit')
out=Path(json.loads((base/'verification/latest_post_freeze_snapshot.json').read_text())['path'])
manifest=json.loads((out/'manifest.json').read_text())
assert [(r['document'],r['changed_blocks']) for r in manifest['documents']]==[('summary',3),('theory',2),('report',4)]
for r in manifest['documents']:
 checkref(r)
 d=json.loads(Path(r['path']).read_text());checkref(d['base_delta'])
 assert sha256(Path(d['live_name']).read_bytes()).hexdigest()==d['result_sha256']
 summary=''.join(x for r in json.loads((out/'summary.json').read_text())['changes'] for x in r['replacement'])
 theory=''.join(x for r in json.loads((out/'theory.json').read_text())['changes'] for x in r['replacement'])
assert 'rechecked independently through 440' in summary and 'final seven-point window, 420 to 438' in summary
assert 'same conditional status' in theory and 'with the unrounded multipliers' in theory and 'all seven final windows' in theory
support=[Path('research/305_final_conditional_fit_scope/verification/admission_V621.json'),Path('research/305_final_conditional_fit_scope/verification/admission_V626.json'),Path('research/266_later_conditional_continuations/N440/verification/admission.json'),Path('research/306_final_logrun_rates/verification/admission_V628.json')]
assert all(p.is_file() for p in support)
excerpts=[]
for name in ['FARFIELD_NUMERICAL_EXPERIMENTS.md','NUM_REPORT.md']:
 p=Path('../a4-num')/name;raw=p.read_bytes();lines=raw.decode().splitlines();selected=set()
 patterns=['V626','+0.00165','-0.328','at 440 alone','verifier\'s unrounded']
 for n,line in enumerate(lines):
  if any(t in line for t in patterns):selected.update(range(max(0,n-3),min(len(lines),n+7)))
 text='\n'.join(f'{n+1}: {lines[n]}' for n in sorted(selected))+'\n'
 dest=out/(name+'.excerpts.txt');dest.write_text(text)
 excerpts.append(dict(source=str(p),source_sha256=sha256(raw).hexdigest(),extract=ref(dest),selected_lines=[n+1 for n in sorted(selected)]))
 assert '-0.328' in text and '-0.419' in text and '-0.691' in text and '+0.00165' in text
ledger,text=next_entry(629);now=datetime.now(timezone.utc).isoformat(timespec='seconds')
result=('The three summary changes, two theory changes and four assembled-report changes after V617 were read in full and matched to V621,V622,V623,V626. '
        'They retain the order329 midpoint condition, use the admitted order440 norms and finite fits, and distinguish the printed-data final-window ranking from the unrounded-data ranking. '
        'The numerics lane also applies the positive signed increment, the431..440 versus440 hump distinction, and the five separate finite decay rates of V628. '
        'The earlier V621/V624 wording defects are closed in these live texts.')
scope=('CONFIRMED for the explicit changed passages and repaired finite diagnostics. '
       'The recheck at440 covers all stored norm coefficients, the last three Poisson orders and finite statistics, not a new full nonlinear recurrence replay. '
       'Qualitative descriptions of fit closeness are not certified numerical bounds. No all-order growth model or canonical uncertainty propagation beyond329 is established.')
proof=base/'PROOF.md';proof.write_text(proof.read_text()+f'\n## Post-freeze integration, V629\n\n{now}. {result}\n\n{scope}\n\nThe comparison method is the same as the preceding scope review: reconstruct V617 from its hashed base and delta; apply and hash the new line replacements; read every changed passage; and match each changed numerical or scope claim to its existing receipt. This is a document-level check with the exact finite arithmetic inherited from those receipts.\n')
ps=base/'sources/PROOF_at_V629.md';ps.write_bytes(proof.read_bytes())
receipt=base/'verification/admission_V629.json';receipt.write_text(json.dumps(dict(at=now,entry=629,all_checks_pass=True,manifest=ref(out/'manifest.json'),changes=manifest['documents'],numerics_excerpts=excerpts,support=[ref(p) for p in support],proof=ref(ps),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V629 | {now} | Final order440 and finite-rate prose integration\n\n**Claim.** The post-freeze report changes preserve the finite audit scope and incorporate the corrections.\n\n**Method.** Reconstruct V617 and the new delta by hashes, read every changed passage, compare the new values with admitted calculations, and freeze the numerics correction excerpts.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
note=f'## {now} VERIFIER -> LEAD, NUMERICS: V629 closes the current order440/rate prose check\n\n{result}\n\n{scope} No new scope defect in the explicit changes. Topic301 stores compact reconstructible deltas instead of duplicating the reports. The remaining final inserts are the Q9/Q10 extension statistics.\n\n'
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V629 checks all explicit V617-to-current summary/theory/report changes and numerics correction excerpts; closes current V621/V624 wording repairs.\n')
(base/'sources/admit_final_prose_integration.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
