"""Compare independently produced026 structure and recorded rows; no peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from decimal import Decimal
import hashlib,json,time
B=Path(__file__).resolve().parents[1];N=B.parents[1].parent/'c1-n4'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();start=time.monotonic();checks=[]
def check(k,c):
 assert c,k
 checks.append(k)
p=B/'verification/result.json';q=B/'source/N4_result.json'
a=json.loads(p.read_text());b=json.loads(q.read_text())
for key in ['raw_sha256','potential_dimension','density_dimension','branch_exponents','noninteger_differences','exact_objective_rows','objective_weights_exact','attempted','accepted','rejected','FLOAT_sum_accepted_rounded_mesh_steps']:
 check(key,a[key]==b[key])
check('46 outside probes',a['outside_analytic_span']==[[x['n'],x['K']] for x in b['probe_rows']] and all(x['outside_span'] for x in b['probe_rows']))
check('heldout current bytes',a['heldout_sha256']==b['heldout_current_sha256'])
check('historical claim not independently witnessed',b['heldout_before_launch_independently_observed'] is False)
for own,peer in zip(a['iterations'],b['iterations']):
 for key in ['i','flag','pred','lambda','dRho2','dCoef']:check('iteration '+str(own['i'])+' '+key,own[key]==peer[key])
 check('iteration '+str(own['i'])+' objective before',Decimal(own['before'])==Decimal(peer['objective_before']))
 check('iteration '+str(own['i'])+' objective proposal',Decimal(own['proposal'])==Decimal(peer['objective_proposal']))
attestation=[]
for path,h in b['inputs'].items():
 src=N/path;actual=sha(src);check('peer source '+path,h==actual);attestation.append({'path':str(src),'sha256':actual})
for row in json.loads((B/'source/N4_snapshot.json').read_text())['files']:
 check('snapshot '+row['name'],any(x['name']==row['name'] and x['sha256']==row['sha256'] for x in a['snapshot_files']))
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'own_sha256':sha(p),'peer_sha256':sha(q),'peer_snapshot_sha256':sha(B/'source/N4_snapshot.json'),'check_count':len(checks),'checks':checks,'peer_inputs_attested_read_only':attestation,'status':'CONFIRMED independent agreement on026 structure, objective rows, probes and recorded iterations; historical save order remains OPEN; no foreign code executed'}
with (B/'verification/peer_comparison.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],len(checks),len(attestation),out['elapsed_seconds'])
