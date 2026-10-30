"""Compare independent007 norms; weighted endpoints are distinct approximants."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/whole_plane_norms'
def H(p):return sha256(p.read_bytes()).hexdigest()
def main():
    start=time.monotonic();ctx.prec=2048
    labels=sys.argv[1:] or ['G0'];name='C1-N1-007-d2w-j7-e2bal'
    dest=BASE/f'verification/candidate007_{"_".join(labels)}_N3_v03.json';assert not dest.exists()
    peerfile=BASE/'source/candidate007/N3_norms_v02.json';peer=json.loads(peerfile.read_text())
    peercode=BASE/'source/candidate007/N3_e2norms.py';assert H(peercode)==peer['code_sha256']
    src=ROOT/f'research/candidate_audits/data/{name}/canonical.json';can=json.loads(src.read_text())
    items={tuple(k):Q(v) for k,v in zip(can['order'],can['coefficients']) if Q(v)}
    serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(items.items()))+'\n'
    assert sha256(serial.encode()).hexdigest()==can['canonical_serialization_sha256']==peer['canonical_sha256']
    assert can['source_sha256']==peer['source_sha256'] and Q(can['cl'])==Q(peer['cl'])
    rows=[]
    for label in labels:
        ownpath=BASE/f'verification/{name}_{label}_ball_2048.json';own=json.loads(ownpath.read_text())
        other=peer['norms']['rF' if label=='rF_proxy' else label]
        assert own['source_sha256']==H(src) and own['status']==other['status']=='FINITE'
        if label in ['P2','Q3']:
            # These two engines bound different polynomial approximants.
            # Compare complete norm intervals, not approximant endpoints.
            ol=arb(own['norm_lower_ball']); ou=arb(own['norm_upper_ball'])
            pl=arb(other['norm_lower']); pu=arb(other['norm_upper'])
            checks={'own_lower_below_peer_upper':bool(ol<pu),
                    'peer_lower_below_own_upper':bool(pl<ou),
                    'own_bounds_ordered':bool(ol<ou),
                    'peer_bounds_ordered':bool(pl<pu)}
        else:
            checks={side:arb(own[f'norm_{side}_ball']).overlaps(arb(other[f'norm_{side}'])) for side in ['lower','upper']}
        assert all(checks.values()),(label,checks)
        rows.append({'label':label,'own_lower':own['norm_lower_ball'],'own_upper':own['norm_upper_ball'],'peer_lower':other['norm_lower'],'peer_upper':other['norm_upper'],'overlap_checks':checks,'own_sha256':H(ownpath)})
    result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'canonical_entries':len(items),'canonical_semantic_sha256':peer['canonical_sha256'],'source_sha256':can['source_sha256'],'rows':rows,'inputs':{str(p.relative_to(ROOT)):H(p) for p in [src,peerfile,peercode,Path(__file__)]},'elapsed_seconds':time.monotonic()-start,'status':'All listed independent enclosures CONFIRMED; no existence claim'}
    dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
