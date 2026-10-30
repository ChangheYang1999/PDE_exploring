"""Validate frozen independent peer outputs without rerunning their jobs."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import sys
import time
from flint import arb, ctx, fmpq as Q

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/candidate_audits'
ARCHIVE = BASE/'peer_review/T4_007'
NAME = 'C1-N1-007-d2w-j7-e2bal'
def digest(p): return sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def same(a,b): assert arb(a).overlaps(arb(b)), (a,b)
def run():
    start=time.monotonic();ctx.prec=1024
    target=BASE/'verification/T4_007_confirmation.json';assert not target.exists()
    canonical=BASE/f'data/{NAME}/canonical.json'
    point=BASE/f'verification/{NAME}_point.json';own=load(point);peer=load(ARCHIVE/'point.json')
    assert peer['target_sha256']==digest(point)
    assert peer['canonical_sha256']==digest(canonical)
    assert peer['code_sha256']==digest(ARCHIVE/'point_reproduce.py')
    assert peer['canonical_coefficients_agree_exactly']
    for key,value in own['fields'].items(): same(value,peer['fields'][key])
    old={r['framework']:r for r in own['ball_exclusions']}
    count=0
    for row in peer['ball_exclusions']:
        for key in ['necessary_upper','gap','necessary_H2s_radius_lower']:
            same(row[key],old[row['framework']][key]);count+=1
        assert arb(row['gap'])>0
    projection=load(ARCHIVE/'projection.json')
    pf=ROOT/f'research/projected_residual/verification/{NAME}_first_mode.json.gz'
    if not pf.exists():
        pf=ROOT/f'research/projected_residual/data/{NAME}_first_mode.json.gz'
    assert projection['peer_sha256']==digest(pf)
    assert projection['canonical_sha256']==digest(canonical)
    assert projection['exact_polynomial_equality']
    assert projection['code_sha256']==digest(ARCHIVE/'projection_check.py')
    assert projection['helper_sha256']==digest(ARCHIVE/'projection_helper.py')
    assert projection['proof_sha256']==digest(ARCHIVE/'projection_PROOF.md')
    weakfile=ROOT/f'research/projected_residual/verification/{NAME}_probe_2048.json'
    weak=load(ARCHIVE/'weak.json');ourweak=load(weakfile)
    assert weak['peer_sha256']==digest(weakfile)
    assert weak['canonical_sha256']==digest(canonical)
    assert weak['code_sha256']==digest(ARCHIVE/'weak_reproduce.py')
    assert weak['helper_sha256']==digest(ARCHIVE/'weak_helper.py')
    assert weak['proof_sha256']==digest(ARCHIVE/'weak_PROOF.md')
    ownrows={r['k']:r for r in ourweak['probes']}
    weakcomparisons=0
    for row in weak['rows']:
        for key in ['pairing','A','B_weighted','C','D','gradient_sup_upper_ball','L2_radius_lower']:
            same(row[key],ownrows[row['k']][key]);weakcomparisons+=1
    bgfile=ROOT/f'research/background_sobolev/verification/{NAME}.json'
    bg=load(ARCHIVE/'background.json');ownbg=load(bgfile)
    assert bg['N4_target_sha256']==digest(bgfile)
    assert bg['source_sha256']==digest(canonical)
    assert bg['code_sha256']==digest(ARCHIVE/'background_reproduce.py')
    assert bg['proof_sha256']==digest(ARCHIVE/'background_PROOF.md')
    for name,row in bg['norms'].items():
        assert Q(row['rational_energy_over_pi_half'])==Q(ownbg['norms'][name]['unweighted_rational_sum'])
        same(row['norm'],ownbg['norms'][name]['norm_upper_ball'])
    same(bg['gradient_HS_norm'],ownbg['gradient_identity_conditional_HS_upper'])
    largebase=ROOT/'research/weighted_weak_audit/peer_review/T4_large'
    large=load(largebase/'results.json')
    largeownfile=ROOT/'research/weighted_weak_audit/verification/state131_scale_scan_2048.json'
    assert large['peer_sha256']==digest(largeownfile)
    assert large['code_sha256']==digest(largebase/'check.py')
    assert large['helper_sha256']==digest(largebase/'helper.py')
    assert large['proof_sha256']==digest(largebase/'PROOF.md')
    largeown={(r['a'],r['k']):r for r in load(largeownfile)['rows']};largecount=0
    for row in large['rows']:
        prior=largeown[row['a'],row['k']]
        for key in ['pairing','A','B_upper','C_upper','D','gradient_sup_upper','weighted_L2_radius_lower']:
            same(row[key],prior[key]);largecount+=1
    assert len(large['rows'])==len(largeown)==104
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'candidate':NAME,'field_overlaps':len(own['fields']),'point_comparisons':count,
         'projection_coefficients_compared_by_peer':projection['coefficients_compared'],
         'projection_exact_equality_by_peer':True,'weak_component_overlaps':weakcomparisons,
         'background_exact_rational_equalities':len(bg['norms']),
         'large_scale_component_overlaps':largecount,
         'peer_archive':{p.name:digest(p) for p in sorted(ARCHIVE.iterdir())},
         'large_archive':{p.name:digest(p) for p in sorted(largebase.iterdir())},
         'code_sha256':digest(Path(__file__)),'elapsed_seconds':time.monotonic()-start,
         'scope':'Confirms independent N4-091,092,095 reproductions; no existence or new inverse claim.'}
    target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if not isinstance(v,dict)},indent=2))
if __name__=='__main__':run()
