"""Freeze compact reconstructible text changes for the V616 repair."""
from pathlib import Path
from hashlib import sha256
from difflib import SequenceMatcher
import json
from certificate_admission import stamp, ref, next_entry
entry=617
ledger,text=next_entry(entry)
base=Path('research/301_final_claim_audit')
checks=[]
phrase='uniquely minimizes the combined unweighted Wiener norm'
for name,live in [('summary',Path('../a4-lead/FINAL_SUMMARY.md')),('theory',Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md')),('report',Path('../a4-lead/FINAL_REPORT.md'))]:
    old=base/'sources'/f'{name}_at_V613.md'
    raw=live.read_bytes(); assert raw==live.read_bytes()
    oldlines=old.read_text().splitlines(keepends=True); newlines=raw.decode().splitlines(keepends=True)
    changes=[]
    for tag,i,j,k,l in SequenceMatcher(None,oldlines,newlines,autojunk=False).get_opcodes():
        if tag!='equal': changes.append(dict(start=i,stop=j,replacement=newlines[k:l]))
    rebuilt=[]; cursor=0
    for change in changes:
        rebuilt+=oldlines[cursor:change['start']]+change['replacement']; cursor=change['stop']
    rebuilt+=oldlines[cursor:]
    assert ''.join(rebuilt).encode()==raw
    matches=[dict(line=i,text=line) for i,line in enumerate(newlines,1) if phrase in line]
    assert matches
    assert 'polar velocity' in ''.join(newlines)
    out=base/'sources'/f'{name}_changes_at_V617.json'
    out.write_text(json.dumps(dict(format='line-replacement-delta-v1',base=ref(old),live_name=str(live),result_sha256=sha256(raw).hexdigest(),changes=changes,matching_lines=matches),indent=2)+'\n')
    checks.append(ref(out))
now=stamp()
result='The current summary, theory introduction and assembled report explicitly name the combined unweighted Wiener norm of the leading polar velocity components. This closes the V616 wording clarification. The exact positive-strip counterexample remains valid and does not refute the correctly scoped Proposition8.4.'
scope='CONFIRMED for this wording repair; no other theorem or finite statistic is newly admitted.'
with (base/'PROOF.md').open('a') as f:
    f.write('\n## Velocity norm wording repair, V617\n\n'+result+'\n\n'+scope+'\n')
proof=base/'sources/PROOF_at_V617.md'; proof.write_bytes((base/'PROOF.md').read_bytes())
out=base/'verification/admission_V617.json'
out.write_text(json.dumps(dict(at=now,entry=entry,all_checks_pass=True,changes=checks,proof=ref(proof),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V617 | {now} | Leading velocity norm clarification closed\n\n**Claim.** The final text now states the precise velocity norm used by the variational theorem.\n\n**Method.** Check all three current documents and save reconstructible deltas from the V613 snapshots, verifying the reconstruction hashes. Compare the text with Proposition8.4 and topic304.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {out}.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: V617 closes velocity norm clarification\n\n{result}\n\n'+p.read_text())
for name,line in [('WORKLOG.md',f'{now}: V617 confirms named unweighted polar norm in all three current documents.'),('VERIFY_SUMMARY.md',f'V617: {result} {scope}')]:
    with Path(name).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/admit_velocity_wording_repair.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
