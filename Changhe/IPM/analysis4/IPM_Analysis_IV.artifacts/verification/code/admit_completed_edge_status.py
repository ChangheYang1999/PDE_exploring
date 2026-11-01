"""Close an obsolete operational claim using retained finite interval evidence."""
from pathlib import Path
from hashlib import sha256
from math import factorial
import json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from read_evidence_bytes import read_bytes
from certificate_admission import stamp,ref,next_entry
from reconstruct_text_delta import reconstruct
ctx.prec=512
base=Path('research/301_final_claim_audit')
snap=base/'verification/post_freeze_20261031T235419Z/report.json'
report=reconstruct(snap).decode()
a=report.index('Truncated recursions (floating-point');b=report.index('\n\n',a)
passage=report[a:b]
assert 'ball-arithmetic reruns with all columns kept are in progress' in passage
checks=[];out=[]
for k,t in [(1,'084803'),(3,'094155')]:
 p=Path(f'research/102_edge_recurrence_reference/verification/arb_edge{k}_20261031T{t}Z/checks.json');raw=read_bytes(p);d=json.loads(raw)
 assert d['maximum_order']==d['source_maximum_order']==300 and len(d['rows'])==300
 assert not d['exact_failures'] and not d['poisson_failures']
 row=d['rows'][-1];assert row['n']==300
 for field in ['density','stream']:
  r=row[field];logs=list(map(arb,r['column_log10_norms']));ratios=[logs[q]+arb(factorial(q)).log()/arb(10).log()-logs[0] for q in range(1,len(logs))]
  assert len(logs)==r['degree']+1
  assert all(x<0 for x in ratios)
  assert all(ratios[0]>x for x in ratios[1:])
  assert ratios[0].overlaps(arb(r['factorial_max'])) and r['factorial_argmax']==1 and r['strict_max']
  out.append(dict(K=k,field=field,order=300,nonconstant_columns=len(ratios),maximum_log_ratio=ratios[0].str(35,radius=True),all_below_constant=True,unique_maximizing_nonconstant_degree=1))
 checks.append(dict(path=str(p),sha256=sha256(raw).hexdigest(),completed_at=d['checked_at_utc']))
ledger,text=next_entry(654);now=stamp()
result=('The sentence that the K=1 and K=3 ball reruns remain in progress is obsolete. Completed checks already existed at08:53:33Z and09:45:18Z and were admitted in V217/V220 and V251. Recomputing all98 density and99 stream nonconstant factorial-column ratios at order300 in each run gives394 strict negative comparisons; degree1 is the unique nonconstant maximum in each of the four lists. The floating runs alone cannot establish the omitted columns, but the completed ball checks resolve that finite issue.')
scope='REFUTED for the current operational sentence and the unqualified claim that the finite maxima remain unestablished. The finite correction is CONFIRMED. No new assertion about the full nonlinear series or its infinite growth follows.'
replacement=('The floating runs alone do not control the dropped columns. The completed 1024-bit ball reruns retain all columns through order300; independent checks confirm the finite column maxima and the modified recurrence (V217/V220 for K=1, V251 for K=3). At order300 every nonconstant factorial column is smaller than the constant column, and degree1 gives the largest nonconstant column for both density and stream in both runs.')
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V654. {result}\n\n{scope}\n')
proof=base/'sources/PROOF_at_V654.md';proof.write_bytes((base/'PROOF.md').read_bytes())
code=base/'sources/admit_completed_edge_status.py';code.write_bytes(Path(__file__).read_bytes())
p=base/'verification/admission_V654.json';p.write_text(json.dumps(dict(at=now,entry=654,verdict='REFUTED',all_checks_pass=True,report_snapshot=ref(snap),obsolete_passage=passage,checks=checks,column_checks=out,proof=ref(proof),algorithm=ref(code),result=result,scope=scope,suggested_replacement=replacement),indent=2)+'\n')
ledger.write_text(text+f'\n## V654 | {now} | Completed finite-edge reruns omitted from current status\n\n**Claim.** The K=1 and K=3 ball reruns remain in progress and the omitted finite factorial maxima are not established.\n\n**Method.** Read the saved completed interval audits; independently recompute all394 nonconstant factorial-column comparisons at order300.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {p}.\n')
n=Path('NOTES_FOR_TEAM.md');n.write_text(f'## {now} VERIFIER -> LEAD: V654 small stale-status repair in numerical overview\n\n{result}\n\nIn report_parts/numerics.md, replace the clause beginning "so the truncated maxima are not established" through "are in progress" with the following, or an equivalent finite statement:\n\n{replacement}\n\nThe paragraph heading may retain the floating-data attribution for its original statistics, but the added sentence must identify the completed ball reruns. No further computation is needed.\n\n'+n.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V654 catches obsolete edge-rerun status;394 strict finite interval comparisons reconfirm the correction.\n')
print(now,result)
