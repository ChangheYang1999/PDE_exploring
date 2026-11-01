"""Audit finite period-three descriptions against independently retained norm balls."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=256
root=Path('research/189_reset350_conditional_audit')
source=root/'verification/checks.json';data=json.loads(source.read_text());rows={r['n']:r for r in data['rows']}
text=lambda x:x.str(35,radius=True)
results=[]
for n in [324,327,330,333,336,339,342,345]:
    item={'from':n,'to':n+3}
    for field in ['f','g']:
        item[field]=text(arb(rows[n+3]['fields'][field]['log10_norm'])-arb(rows[n]['fields'][field]['log10_norm']))
    results.append(item)
by_n={r['from']:r for r in results}
assert arb(by_n[330]['g'])>arb('-1.1')
assert arb(by_n[336]['f'])>arb('-1.61')
assert arb(by_n[339]['f'])<arb('-1.65')
assert arb(by_n[327]['f'])<arb('-2.14')
left=arb(rows[341]['shares']['stream_by_shift']['2/3']);right=arb(rows[344]['shares']['stream_by_shift']['2/3'])
assert right-left>arb('.006')
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
claim=next(part for part in Path('../a4-num/NOTES_FOR_TEAM.md').read_text().split('## ') if part.startswith('2026-10-31T14:15Z'))
(root/'sources/num_period3_claim_1415.md').write_text('Observed '+now+'\n\n## '+claim)
for name in ['period3_decrements_300_353.txt','stream_shares_341_350.txt']:
    (root/'sources'/name).write_bytes((Path('../a4-num/notes')/name).read_bytes())
result=dict(checked_at_utc=now,source=str(source),source_sha256=sha256(source.read_bytes()).hexdigest(),scope='Finite conditional norm balls of the reset continuation; no inherited uncertainty bound or infinite-cycle claim.',decrements=results,shares_341_344=[text(left),text(right)],share_difference=text(right-left),all_counterexamples_confirmed=True)
(root/'verification/period3_counterexamples.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/check_period3_claims.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result,indent=2))
