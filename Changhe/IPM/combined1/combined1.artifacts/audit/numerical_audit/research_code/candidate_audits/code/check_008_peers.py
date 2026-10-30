"""Check source identities and independently produced T4 enclosures for008."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/candidate_audits';P=B/'peer_review/T4_008';N='C1-N1-008-d2w-j7-x3bal'
def H(p):return sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def check(a,b):return bool(arb(a).overlaps(arb(b)))
ctx.prec=1024;start=time.monotonic()
point=B/f'verification/{N}_point.json';uniform=B/f'verification/{N}_uniform_point.json';background=ROOT/f'research/background_sobolev/verification/{N}.json';canonical=B/f'data/{N}/canonical.json'
pp=P/f'new_candidate_witness/verification/{N}.json';bp=P/f'background_norm_reproduction/verification/{N}_reproduction.json';up=P/'graded_point_008/verification/results.json'
p,u,b=map(load,[point,uniform,background]);pt,ut,bt=map(load,[pp,up,bp])
assert pt['candidate']==bt['candidate']==N
assert pt['target_sha256']==H(point) and bt['N4_target_sha256']==H(background)
assert pt['canonical_sha256']==bt['source_sha256']==H(canonical)==p['canonical_sha256']==b['source_sha256']
assert pt['snapshot_sha256']==H(B/f'data/{N}/d2w_j7_n4_X3bal_mid180_exact.json')
assert pt['code_sha256']==H(P/'new_candidate_witness/code/reproduce.py')
assert bt['code_sha256']==H(P/'background_norm_reproduction/code/reproduce_new_candidate.py')
assert bt['proof_sha256']==H(P/'background_norm_reproduction/PROOF.md')
for rel,digest in ut['inputs'].items():
 path={'data/own_point.json':pp,'source/N4_result.json':uniform}.get(rel,P/'graded_point_008'/rel)
 assert H(path)==digest,(rel,H(path),digest)
assert p['point']==pt['point'] and pt['canonical_coefficients_agree_exactly']
checks={f'field:{k}':check(v,pt['fields'][k]) for k,v in p['fields'].items()}
for row,peer in zip(p['ball_exclusions'],pt['ball_exclusions'],strict=True):
 assert row['framework']==peer['framework']
 for key in ['necessary_upper','gap','necessary_H2s_radius_lower']:
  checks[f"{row['framework']}:{key}"]=check(row[key],peer[key])
 checks[f"{row['framework']}:positive"]=bool(arb(peer['gap'])>0)
checks['uniform_upper']=check(u['uniform_graded_upper'],ut['uniform_values']['uniform_point_upper'])
checks['uniform_gap']=check(u['uniform_graded_gap'],ut['uniform_values']['uniform_positive_gap'])
checks['uniform_positive']=bool(arb(ut['uniform_values']['uniform_positive_gap'])>0)
for row in u['sharp_boxes']:
 peer=next(r for r in ut['finite_boxes'] if r['framework']==row['framework'])
 checks[row['framework']+':upper']=check(row['point_upper'],peer['upper'])
 checks[row['framework']+':gap']=check(row['gap'],peer['gap'])
 checks[row['framework']+':positive']=bool(arb(peer['gap'])>0)
for key,row in b['norms'].items():
 peer=bt['norms'][key]
 checks['exact_energy:'+key]=Q(row['unweighted_rational_sum'])==Q(peer['rational_energy_over_pi_half'])
 checks['norm:'+key]=check(row['norm_upper_ball'],peer['norm'])
checks['kappa']=check(b['gradient_identity_conditional_HS_upper'],bt['gradient_HS_norm'])
assert all(checks.values()),{k:v for k,v in checks.items() if not v}
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':N,'code_sha256':H(Path(__file__)),'inputs':{str(p.relative_to(ROOT)):H(p) for p in [point,uniform,background,canonical,pp,up,bp]},'checks':checks,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-106 point/uniform/sharp exclusions and N4-107 exact background energies and structured HS estimate.'}
dest=B/'verification/008_peer_comparison.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
print(out['verdict'],len(checks),'checks',out['elapsed_seconds'],flush=True)
