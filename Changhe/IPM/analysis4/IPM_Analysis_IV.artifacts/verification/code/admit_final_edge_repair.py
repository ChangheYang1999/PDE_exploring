"""Close the finite-edge report correction against its retained comparisons."""
from pathlib import Path
import json,sys,difflib
sys.dont_write_bytecode=True
from certificate_admission import stamp,ref,next_entry
from reconstruct_text_delta import reconstruct
base=Path('research/301_final_claim_audit')
old=base/'verification/post_freeze_20261031T235419Z'
new=base/'verification/post_freeze_20261031T235941Z'
texts={k:reconstruct(new/f'{k}.json').decode() for k in ['summary','theory','report']}
for k in ['summary','theory']:
 assert texts[k]==reconstruct(old/f'{k}.json').decode()
before=reconstruct(old/'report.json').decode()
changes=[(t,a,b,c,d) for t,a,b,c,d in difflib.SequenceMatcher(a=before.splitlines(),b=texts['report'].splitlines(),autojunk=False).get_opcodes() if t!='equal']
assert len(changes)==2 and changes[0][1:]==(2,3,2,3)
a=texts['report'].index('Truncated recursions (floating-point');b=texts['report'].index('\n\n',a)
passage=texts['report'][a:b]
assert 'ball-arithmetic reruns with all columns kept are in progress' not in texts['report']
expected=('The completed 1024-bit ball reruns of both truncated recursions keep all columns through order 300 (the finite\ncolumn maxima and the modified recurrence were checked independently): at order 300 every nonconstant factorially\nweighted log column is smaller than the constant column, and log degree 1 gives the largest nonconstant column for both\ndensity and stream in both runs.')
assert expected in passage
certpath=base/'verification/admission_V654.json';cert=json.loads(certpath.read_text())
assert cert['all_checks_pass']
rows=cert['column_checks'];assert len(rows)==4
assert {(r['K'],r['field']) for r in rows}=={(1,'density'),(1,'stream'),(3,'density'),(3,'stream')}
assert sum(r['nonconstant_columns'] for r in rows)==394
assert all(r['all_below_constant'] and r['unique_maximizing_nonconstant_degree']==1 and r['order']==300 for r in rows)
ledger,text=next_entry(656);now=stamp()
result=('The obsolete in-progress sentence is replaced by the completed finite-ball result. The new statement agrees with all394 strict comparisons in V654: at order300 every nonconstant factorial column is below the constant column, and degree1 is the unique nonconstant maximum for density and stream in each of the K=1 and K=3 recursions. Only that paragraph and the report timestamp changed. The summary and theory are byte-identical to the V653 snapshot.')
scope='CONFIRMED for the report correction. V654 is closed. No infinite-growth claim is added; no new full-report reading or numerical replay is claimed.'
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V656. {result}\n\n{scope}\n')
proof=base/'sources/PROOF_at_V656.md';proof.write_bytes((base/'PROOF.md').read_bytes())
code=base/'sources/admit_final_edge_repair.py';code.write_bytes(Path(__file__).read_bytes())
p=base/'verification/admission_V656.json';p.write_text(json.dumps(dict(at=now,entry=656,verdict='CONFIRMED',all_checks_pass=True,previous_snapshots=[ref(old/f'{k}.json') for k in texts],current_snapshots=[ref(new/f'{k}.json') for k in texts],finite_comparisons=ref(certpath),proof=ref(proof),algorithm=ref(code),accepted_passage=passage,result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V656 | {now} | Final finite-edge report correction\n\n**Claim.** The revised finite-edge paragraph correctly reports the completed ball reruns.\n\n**Method.** Read both exact changed blocks; compare all four column conclusions with V654 and require identical summary and theory snapshots.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
n=Path('NOTES_FOR_TEAM.md');n.write_text(f'## {now} VERIFIER -> LEAD: V656 closes V654; all current report corrections complete\n\n{result}\n\n{scope}\n\nAll44 Q7/Q8/Q9/Q10 extensions are admitted within their finite scope. V653 closed the final Q9 insertion. I am refreshing the final inventories and handoff; no additional computation is needed. Any later edits will be checked against this snapshot.\n\n'+n.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V656 closes final finite-edge paragraph repair; all current report corrections complete.\n')
print(now,result)
