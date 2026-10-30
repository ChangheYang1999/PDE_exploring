"""Internal completeness and provenance checks, not an independent leaf replay."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime,timezone
import json,time,sys
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/candidate_background_cover'
name='C1-N1-007-d2w-j7-e2bal'
sys.path.insert(0,str(ROOT/'research/global_matrices/code'))
from cover import checktree
ctx.prec=1024;start=time.monotonic()
def H(p):return sha256(p.read_bytes()).hexdigest()
def endpoints(path):
 a,b,c,d=map(F,[0,1,-1,1])
 for letter in path:
  if letter=='t':b=(a+b)/2
  elif letter=='T':a=(a+b)/2
  elif letter=='z':d=(c+d)/2
  elif letter=='Z':c=(c+d)/2
  else:raise ValueError(letter)
 return a,b,c,d
p=BASE/f'verification/{name}_theta_2_25_768.json'
record=json.loads(p.read_text());assert record['all_pass'] and not record['pending']
assert record['complete_partition'] and record['signed_rate_at_least_two']
assert record['code_sha256']==H(BASE/'code/certify.py')
assert record['proof_sha256']==H(BASE/'PROOF.md')
assert record['source_sha256']==H(BASE/f'data/{name}_polynomials.json.gz')
assert record['canonical_sha256']==H(ROOT/f'research/candidate_audits/data/{name}/canonical.json')
assert record['enclosure_helpers_sha256']==H(ROOT/'research/global_matrices/code/cover.py')
paths=[r['path'] for r in record['accepted']]
assert len(set(paths))==len(paths);checktree(set(paths))
rectangles=[endpoints(path) for path in paths]
area=sum(((b-a)*(d-c) for a,b,c,d in rectangles),F(0));assert area==2
pairs=0
for i,(a,b,c,d) in enumerate(rectangles):
 for e,f,g,h in rectangles[i+1:]:
  assert max(a,e)>=min(b,f) or max(c,g)>=min(d,h)
  pairs+=1
bounds=[arb(r['bound']) for r in record['accepted']]
assert all(r['pass'] for r in record['accepted']) and all(v>=0 for v in bounds)
minimum=bounds[0]
for v in bounds[1:]:minimum=minimum.min(v)
kfile=ROOT/f'research/background_sobolev/verification/{name}.json'
assert record['HS_source_sha256']==H(kfile)
k=arb(json.loads(kfile.read_text())['gradient_identity_conditional_HS_upper'])
source=json.loads((ROOT/f'research/candidate_audits/data/{name}/canonical.json').read_text())
c=F(source['cl']);margin=arb(c.numerator)/c.denominator+1-arb(2)/25-k
assert margin>=2 and margin.overlaps(arb(record['signed_rate_lower']))
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,
     'certificate_sha256':H(p),'code_sha256':H(Path(__file__)),
     'accepted_count':len(paths),'pending_count':0,'exact_area':str(area),
     'disjoint_interior_pairs':pairs,'prefix_tree_complete':True,
     'all_saved_leaf_bounds_nonnegative':True,'minimum_saved_leaf_bound':minimum.str(90),
     'signed_rate':margin.str(90),'signed_rate_above_two':(margin-2).str(90),
     'all_declared_source_hashes_match':True,'elapsed_seconds':time.monotonic()-start,
     'scope':'Internal partition, saved-bound and provenance audit. Independent recomputation of leaf inequalities is still required for peer confirmation.'}
target=BASE/f'verification/{name}_complete_internal_audit.json';assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
