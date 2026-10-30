"""Bind independent peer results and verify scalar acceptance conditions."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,time
from flint import arb,fmpq as Q,ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/successor_weak_probes'
D=BASE/'reviews/T4_236'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def A(q):
 q=Q(q);return arb(q.numerator)/arb(q.denominator)
start=time.monotonic();ctx.prec=512
manifest=json.loads((D/'MANIFEST.json').read_text())
for name,row in manifest['files'].items():assert H(D/name)==row['sha256']
rows=[]
for cand,name in [('012','C1-N1-012-e2balk1e7-from009')]:
 for n in [7,1]:
  peer=json.loads((D/f'{cand}_n{n}_result.json').read_text())
  inp=json.loads((D/f'{cand}_n{n}_input.json').read_text())
  ownpath=BASE/f'verification/{name}_n{n}.json';own=json.loads(ownpath.read_text())
  assert H(D/f'{cand}_n{n}_source.json')==H(ownpath)
  assert peer['peer_sha256']==H(D/f'{cand}_n{n}_input.json')
  assert peer['code_sha256']==H(D/'check.py') and peer['helper_sha256']==H(D/'polar_helper.py')
  assert peer['source_sha256']==own['canonical_sha256']
  assert peer['candidate']==cand and peer['angular_mode']==own['angular_mode']==n
  assert Q(peer['a'])==0 and Q(peer['C_U_exact'])==1
  probe_rel={7:'research/angular_probe_audit/source/T4_n7_a0.json',1:'research/optimized_probe_audit/source/T4_a0.json'}[n]
  assert H(ROOT/probe_rel)==own['inputs'][probe_rel]
  frozen_probe=json.loads((ROOT/probe_rel).read_text())
  assert peer['probe_coefficients']==inp['probe_coefficients']==frozen_probe['probe_coefficients']
  assert all(Q(v)==0 for k,v in peer['probe_coefficients'].items() if int(k)<(n-1)//2)
  assert all(peer['comparisons'].values())
  assert peer['sup_certificate']['accepted_cells']>0
  assert Q(peer['sup_certificate']['H_upper_exact'])==Q(own['H_upper_exact'])==Q(inp['H_upper_exact'])
  checks={key:bool(arb(peer[key]).overlaps(arb(own[key]))) for key in ['pairing','M','C','radius']}
  I,M,C=map(lambda key:arb(peer[key]),['pairing','M','C'])
  assert abs(I)>0 and M>0 and C>0
  distance=2*abs(I)/(M+C+((M+C)**2+4*A(own['H_upper_exact'])*abs(I)).sqrt())
  checks['root_formula']=distance.overlaps(arb(peer['radius']))
  floor=A(peer['strict_lower_exact'])
  checks['strict_floor_peer']=bool(floor<arb(peer['radius']))
  checks['strict_floor_own']=bool(floor<arb(own['radius']))
  assert all(checks.values()),checks
  rows.append({'candidate':name,'mode':n,'checks':checks,'strict_lower_exact':peer['strict_lower_exact'],'own_sha256':H(ownpath),'peer_sha256':H(D/f'{cand}_n{n}_result.json'),'peer_elapsed_seconds':peer['elapsed_seconds']})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','manifest_sha256':H(D/'MANIFEST.json'),'proof_sha256':H(D/'ACCEPTANCE_PROOF.md'),'code_sha256':H(__file__),'rows':rows,'elapsed_seconds':time.monotonic()-start}
with (D/'ACCEPTANCE.json').open('x') as s:json.dump(out,s,indent=2);s.write('\n')
print(json.dumps(out,indent=2))
