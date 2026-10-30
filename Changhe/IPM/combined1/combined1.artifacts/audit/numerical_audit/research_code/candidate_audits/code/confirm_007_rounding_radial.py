"""Check frozen independent audits against the original N4 records."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction
import json
import sys
import time
from flint import arb, ctx

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
NAME = 'C1-N1-007-d2w-j7-e2bal'
def H(p): return sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def overlap(a,b): assert arb(a).overlaps(arb(b)), (a,b)
def archive_hashes(p): return {q.name:H(q) for q in sorted(p.iterdir()) if q.is_file()}
def run():
    start=time.monotonic();ctx.prec=1536
    dest=ROOT/'research/candidate_audits/verification/T4_007_rounding_radial_confirmation.json'
    assert not dest.exists()
    rbase=ROOT/'research/rounding_realization'
    rf=rbase/f'verification/{NAME}.json'
    own=load(rf);ap=rbase/'peer_review/T4';peer=load(ap/'results.json')
    for key,filename in [('proof_sha256','PROOF.md'),('code_sha256','check.py'),('helper_sha256','helper.py')]:
        assert peer[key]==H(ap/filename)
    assert peer['peer_result_sha256']==H(rf)
    assert peer['canonical_maps_agree_exactly'] and peer['rounded_generator_vectors_agree_exactly']
    assert peer['coefficient_count']==own['coefficient_count']==2982
    assert peer['changed_coefficients']==own['changed_coefficients']==421
    assert Fraction(peer['maximum_coefficient_error'])==Fraction(own['maximum_absolute_coefficient_error'])
    assert Fraction(peer['strain_difference'])==Fraction(own['strain_difference'])
    overlap(peer['a0_difference'],own['a0_difference_ball'])
    pl=peer['leading_sector'];ol=own['leading_nonzero_forbidden_sector']
    assert (pl['h'],pl['q'])==(ol['h'],ol['q'])==(1,0)
    assert Fraction(pl['exponent'])==Fraction(ol['exponent'])>-1
    overlap(pl['full_circle_norm'],ol['rounded_full_circle_norm'])
    assert arb(pl['full_circle_norm'])>0 and peer['rounded_residual_not_in_L2']
    assert len(own['points'])==len(peer['points'])==2
    count=0
    for a,b in zip(own['points'],peer['points']):
        assert a['point']==b['point']
        for k,v in a['differences'].items():
            overlap(v,b['differences'][k]);count+=1
        for k in ['exact_residual','rounded_residual']:overlap(a[k],b[k])
        assert all(b['comparisons'].values()) and b['residual_identity_agrees']
    bbase=ROOT/'research/background_radial_mass'
    bf=bbase/f'verification/{NAME}.json'
    ownb=load(bf);bp=bbase/'peer_review/T4';peerb=load(bp/'results.json')
    for key,filename in [('proof_sha256','PROOF.md'),('code_sha256','check.py'),('helper_sha256','helper.py')]:
        assert peerb[key]==H(bp/filename)
    assert peerb['peer_result_sha256']==H(bf)
    assert peerb['source_sha256']==H(ROOT/f'research/candidate_audits/data/{NAME}/canonical.json')
    assert peerb['mixed_derivatives_agree_exactly'] and peerb['full_rational_energies_agree']
    assert peerb['all_17_ball_comparisons_agree']
    assert Fraction(peerb['inner_radius'])==Fraction(ownb['inner_radius'])
    assert Fraction(peerb['outer_radius'])==Fraction(ownb['outer_radius_exact_binary64'])
    bcount=0
    for n,rows in ownb['derivative_squared_masses'].items():
        for region,v in rows.items():
            overlap(v,peerb['derivative_squared_masses'][n][region]);bcount+=1
    for region,v in ownb['kappa_squared_masses'].items():
        overlap(v,peerb['kappa_squared_masses'][region]);bcount+=1
    for key in ['kappa_full','kappa_exact_middle','reported_minus_exact_middle',
                'missing_origin_fraction_of_kappa_squared','missing_exterior_fraction_of_kappa_squared']:
        overlap(ownb[key],peerb[key]);bcount+=1
    assert count==16 and bcount==17
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'candidate':NAME,'code_sha256':H(Path(__file__)),
         'rounding_peer_archive':archive_hashes(ap),'radial_peer_archive':archive_hashes(bp),
         'original_rounding_sha256':H(rf),'original_radial_sha256':H(bf),
         'coefficient_count':2982,'changed_coefficients':421,
         'point_difference_overlaps':count,'radial_mass_overlaps':bcount,
         'leading_rounded_forbidden_sector_confirmed':True,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Confirms N4-096 leading-sector nonintegrability and point data and N4-097 radial masses. Higher rounded forbidden sectors were not independently recomputed by the peer.'}
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not isinstance(v,dict)},indent=2))
if __name__=='__main__':run()
