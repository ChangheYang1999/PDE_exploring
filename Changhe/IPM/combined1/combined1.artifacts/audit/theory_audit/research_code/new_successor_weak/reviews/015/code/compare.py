from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic()
a=R/'data/015/canonical.json';b=B/'source/N4_canonical.json'
x=json.loads(a.read_text());y=json.loads(b.read_text())
u=R/'verification/015_build.json';v=B/'source/N4_result.json'
xx=json.loads(u.read_text());yy=json.loads(v.read_text())
assert sha(a)==xx['canonical_sha256'] and sha(b)==yy['canonical_sha256']
assert Q(x['cl'])==Q(y['cl'])==Q(yy['c_exact'])
def mapping(data):
 d={tuple(k):Q(c) for k,c in zip(data['order'],data['coefficients'],strict=True) if Q(c)}
 assert len(d)==sum(bool(Q(c)) for c in data['coefficients'])
 return d
mx,my=mapping(x),mapping(y);assert mx==my and len(mx)==1922
assert xx['source_sha256']==yy['generator_sha256']
assert Q(xx['a0_exact'])==Q(yy['a0_exact'])>0
assert Q(xx['strain_exact'])==Q(yy['strain_exact'])==1-Q(x['cl'])
assert xx['origin_identities_exact'] and yy['B0n_exact']
assert yy['all_forbidden_zero']
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'termwise_rational_map_equal':True,'nonzero_terms':len(mx),'exact_c_origin_strain_slope_equal':True,'peer_all_forbidden_zero':True,'inputs':{str(p):sha(p) for p in [a,b,u,v,Path(__file__),R/'PROOF.md']},'peer_top_level_keys':list(yy),'scope':'Independent canonical polynomial and origin agreement; first four profile comparison is in own build, not independently repeated here.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['elapsed_seconds'],out['scope']);print('Peer keys:',list(yy))
