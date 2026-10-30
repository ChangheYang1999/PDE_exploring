"""Read-only certificate validation, then write a fresh final audit record."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction
import json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1]
R=B.parent.parent
ctx.prec=1024
start=time.monotonic()
def H(p):return sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def cover(paths):
    leaves=set(paths)
    assert len(leaves)==len(paths)
    for p in leaves:assert set(p)<=set('tTzZ')
    while leaves!={''}:
        p=max(leaves,key=len);assert p
        q=p[:-1]+{'t':'T','T':'t','z':'Z','Z':'z'}[p[-1]]
        assert q in leaves and p[:-1] not in leaves
        leaves.remove(p);leaves.remove(q);leaves.add(p[:-1])
statep=B/'verification/candidate007_signed_cover_v2.json';d=read(statep)
seedp=B/'verification/candidate007_signed_cover.json';seed=read(seedp)
gradp=B/'verification/gradient_reconstruction_v2.json';grad=read(gradp)
peerp=B/'source/N4_L2_cover.json';peer=read(peerp)
hsp=R/'research/background_norm_reproduction/verification/C1-N1-007-d2w-j7-e2bal_reproduction.json';hs=read(hsp)
expected={'code_sha256':B/'code/certify_v2.py','proof_sha256':B/'PROOF.md',
 'branch_addendum_sha256':B/'BRANCH_CORRELATION.md','seed_certificate_sha256':seedp,
 'source_sha256':B/'data/canonical.json','N4_cover_sha256':peerp,'reconstruction_sha256':gradp}
for key,path in expected.items():assert d[key]==H(path),(key,path)
assert grad['canonical_sha256']==H(B/'data/canonical.json')
assert grad['N4_polynomial_sha256']==H(B/'source/N4_polynomials.json.gz')
assert grad['code_sha256']==d['code_sha256'] and grad['all_gradient_coefficients_match']
assert seed['code_sha256']==H(B/'code/certify.py') and seed['proof_sha256']==H(B/'PROOF.md')
assert d['precision_bits']==seed['precision_bits']==1024
assert d['all_pass'] and d['complete_partition'] and not d['pending']
cover([row['path'] for row in d['accepted']])
cover([row['path'] for row in seed['accepted']]+seed['pending'])
cover([row['path'] for row in peer['accepted']]);assert not peer['pending']
final={row['path']:row for row in d['accepted']}
for row in seed['accepted']:
    old=dict(row);old['source_code_sha256']=seed['code_sha256'];assert final[row['path']]==old
margins=[]
for row in d['accepted']:
    assert row['pass'];margin=arb(row['schur_lower']);assert margin>=0
    margins.append(margin)
    if 'source_code_sha256' in row:assert row['source_code_sha256']==seed['code_sha256']
assert hs['source_sha256']==d['source_sha256']
cq=Fraction(grad['cl']);c=arb(cq.numerator)/cq.denominator
kappa=arb(hs['gradient_HS_norm']);rate=c+1-arb(2)/25-kappa
assert rate>2 and rate.overlaps(arb(peer['signed_rate_lower']))
minimum=margins[0]
for m in margins[1:]:minimum=minimum.min(m)
inputs={str(p.relative_to(R)):H(p) for p in [*expected.values(),B/'code/certify.py',
 B/'source/N4_polynomials.json.gz',R/'research/weak_probe_audit/code/reproduce.py',hsp,Path(__file__)]}
result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':d['candidate'],
 'status':'CONFIRMED independent full-plane theta<=2/25 and signed L2 rate>2',
 'precision_bits':ctx.prec,'accepted_cells':len(d['accepted']),'original_N4_cells':len(peer['accepted']),
 'seed_accepted_cells':len(seed['accepted']),'pending_cells':0,'root_partition_verified':True,
 'seed_rows_preserved':True,'all_schur_margins_nonnegative':True,
 'minimum_recorded_schur_margin':minimum.str(80),'theta_upper_exact':'2/25',
 'kappa':kappa.str(80),'signed_rate':rate.str(80),'signed_rate_at_least_two':True,
 'source_sha256':d['source_sha256'],'cover_sha256':H(statep),'inputs':inputs,
 'recorded_completed_cover_seconds':d['elapsed_seconds'],'validation_seconds':time.monotonic()-start,
 'scope':'Signed unweighted L2 condition only. Other high inverse and nonlinear closure hypotheses are separate.'}
out=B/'verification/FINAL_VALIDATION.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='inputs'},indent=2))
