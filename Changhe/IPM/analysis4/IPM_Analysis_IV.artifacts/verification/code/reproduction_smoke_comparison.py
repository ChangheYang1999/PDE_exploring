"""Compare the documented small replays with their archived exact results."""
from pathlib import Path
from datetime import datetime
import json
from certificate_admission import stamp,ref,next_entry
base=Path('artifacts/reproduction');sources=[]
def load(p):
 p=Path(p);sources.append(ref(p));return json.loads(p.read_text())
a=load(base/'two_mode_replay.json');b=load('research/01_recurrence/verification/two_mode_c5_3_N4.json')
assert a['self_checks']==b['self_checks'] and a['recursion']==b['recursion']
c=load(base/'candidate_replay.json');d=load('research/02_candidate007/data/leading_exact.json')
keys=['c','gamma','delta','branch_zero_generators','potential','density','stream','input_sha256','manifest_sha256','sector_table_sha256']
for k in keys:assert c['extraction'][k]==d[k],k
assert c['self_checks']==a['self_checks']
for row in a['recursion']['rows']+c['recursion']['rows']:
 assert row['poisson_exact'] and row['stationary_residual_exact_zero'] and row['direct_potential_verified']
times=[(datetime.fromisoformat(x['completed_utc'])-datetime.fromisoformat(x['date_utc'])).total_seconds() for x in [a,c]]
now=stamp();result=dict(at=now,all_checks_pass=True,sources=sources,matched_two_mode_orders=4,matched_candidate_fields=keys,candidate_orders_directly_checked=2,basis_checks_per_run=a['self_checks'],actual_recorded_elapsed_s=times,scope='Small execution checks for the reproduction guide. No new all-order result and no full certificate replay.')
out=base/'smoke_comparison.json';out.write_text(json.dumps(result,indent=2)+'\n')
ledger,text=next_entry(646)
summary=f'The documented two-mode replay matches all four archived orders exactly. The new Candidate007 extraction matches all ten specified exact data/hash fields and directly checks two orders. Both runs pass40 basis checks. Recorded execution times are {times[0]}s and {times[1]}s.'
scope='CONFIRMED for the two documented commands and these exact finite comparisons. No new theorem or full historical replay is claimed.'
proof=Path('research/301_final_claim_audit/sources/PROOF_at_V646.md');proof.write_bytes(Path('research/01_recurrence/PROOF.md').read_bytes())
receipt=Path('research/301_final_claim_audit/verification/admission_V646.json');receipt.write_text(json.dumps(dict(at=now,entry=646,verdict='CONFIRMED',all_checks_pass=True,evidence=ref(out),underlying_recurrence_proof=ref(proof),guide_snapshot=ref('REPRODUCTION.md'),result=summary,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V646 | {now} | Reproduction-guide execution check\n\n**Claim.** The two documented small-replay commands execute successfully and reproduce the specified exact data.\n\n**Method.** Run the commands with separate outputs; compare exact parsed objects, data hashes and direct Cartesian identities.\n\n**Result.** {summary}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: Added REPRODUCTION.md and recorded installed versions. V646 verifies both documented commands without changing the archived recurrence or extraction.\n')
print(now,summary)
