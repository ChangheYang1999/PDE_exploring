"""Compare the direct wrapper with the existing independent 007 audit."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,time
from flint import arb,ctx,fmpq as Q
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/generator_sector_audit'
name='C1-N1-007-d2w-j7-e2bal'
start=time.monotonic();ctx.prec=1024
def H(p):return sha256(p.read_bytes()).hexdigest()
p=BASE/f'verification/{name}_direct.json'
a=ROOT/f'research/candidate_audits/verification/{name}.json'
b=ROOT/f'research/candidate_audits/verification/{name}_point.json'
c=ROOT/f'research/candidate_audits/verification/{name}_uniform_point.json'
direct=json.loads(p.read_text());old=json.loads(a.read_text());point=json.loads(b.read_text())
assert direct['generator_sha256']==old['generator_sha256']
assert Q(direct['origin']['a0'])==Q(old['a0_exact'])
assert Q(direct['origin']['strain'])==Q(old['strain_exact'])
assert all(direct[k]==old[k] for k in ['B0n_exact','c_equal_state131','leading_potential_equal_state131','leading_density_equal_state131'])
original={Q(r['exponent']):r for r in old['sectors']}
count=0
for row in direct['sectors']:
 previous=original[Q(row['exponent'])]
 assert row['exact_zero']==previous['exact_zero']
 assert {int(k):Q(v) for k,v in row['sine_coefficients'].items()}=={int(k):Q(v) for k,v in previous['sine_coefficients'].items()}
 assert arb(row['full_circle_norm']).overlaps(arb(previous['full_circle_norm']))
 count+=len(row['sine_coefficients'])
fields={k:bool(arb(v).overlaps(arb(point['fields'][k]))) for k,v in direct['fields'].items()}
assert all(fields.values())
oldballs={r['framework']:r for r in point['ball_exclusions']}
ballchecks={}
for row in direct['ball_exclusions']:
 if row['framework'] in oldballs:
  ballchecks[row['framework']]=bool(arb(row['gap']).overlaps(arb(oldballs[row['framework']]['gap'])))
assert all(ballchecks.values())
# The separate 007 uniform theorem predates the generic candidate uniform file.
proof=ROOT/'research/point_witness/PROOF_UNIFORM_GRADED.md'
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'input_sha256':{str(v.relative_to(ROOT)):H(v) for v in [p,a,b,proof]},
     'code_sha256':H(Path(__file__)),'precision_bits':ctx.prec,
     'all_origin_and_normalization_checks':True,'sector_count':len(direct['sectors']),
     'nonzero_coefficient_equalities':count,'field_overlaps':fields,'ball_gap_overlaps':ballchecks,
     'elapsed_seconds':time.monotonic()-start,
     'scope':'Single-scale regression of a generic scaled-generator wrapper. Future candidate claims require their own audits.'}
output=BASE/'verification/007_regression.json';assert not output.exists()
output.write_text(json.dumps(out,indent=2)+'\n')
print('sectors',out['sector_count'],'coefficients',count,'fields',len(fields),'seconds',out['elapsed_seconds'])
