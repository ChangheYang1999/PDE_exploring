"""Full exact prefix comparison, supplementing the independent direct computation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];N=B.parents[1].parent/'c1-n4';ctx.prec=1024
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();start=time.monotonic();checks=[]
def check(label,condition):
 assert condition,label
 checks.append(label)
a=json.loads((B/'data/exact_sectors.json').read_text());b=json.loads((B/'source/N4_prefix_result.json').read_text())
check('same exact raw',a['raw_sha256']==b['raw_sha256']=='2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3')
check('all sixteen rows',len(a['sectors'])==len(b['rows'])==16)
for own,peer in zip(a['sectors'],b['rows']):
 for k in ['K','L','exponent_exact','density','stream','residual','residual_zero']:
  check(str((own['K'],own['L']))+' '+k,own[k]==peer[k])
 check(str((own['K'],own['L']))+' norm',arb(own['angular_norm']).overlaps(arb(peer['full_circle_norm'])))
attested=[]
for path,h in b['inputs'].items():
 check('peer source '+path,sha(N/path)==h);attested.append({'path':str(N/path),'sha256':h})
inputs={str(p.relative_to(B)):sha(p) for p in [B/'PROOF.md',B/'data/exact_sectors.json',B/'verification/result.json',B/'source/N4_prefix_result.json',B/'source/N4_prefix_PROOF.md',B/'source/N4_prefix_check.py',Path(__file__)]}
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'check_count':len(checks),'checks':checks,'peer_inputs_attested_read_only':attested,'status':'CONFIRMED all sixteen exact density, stream and residual maps match the independent N4 prefix, including the three beyond the old rectangular list; no foreign code executed'}
with (B/'verification/full_prefix_comparison.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(r['utc'],len(checks),len(attested),r['elapsed_seconds'])
