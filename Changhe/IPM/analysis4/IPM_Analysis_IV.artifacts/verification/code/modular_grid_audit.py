"""Replay the completed modular grids and compare independent polar residues."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd
import argparse,json,sys,time
sys.dont_write_bytecode=True
from flint import fmpz
ROOT=Path('research/225_modular_cartesian_scan')
def digest(path):
    raw=path.read_bytes()
    return dict(path=str(path),bytes=len(raw),sha256=sha256(raw).hexdigest())
def audit(profile):
    start=time.monotonic();directory=ROOT/'verification'/profile
    manifest_path=directory/'manifest.json';manifest=json.loads(manifest_path.read_text())
    expected=[]
    for Q in range(5,121):
        for h in range(2,Q):
            if gcd(Q,h)!=1 or 2*h>=Q:continue
            if profile=='cand007' and not (5*h>Q and 4*h<Q):continue
            expected.append((Q,h))
    assert len(expected)=={'cand007':217,'sin1':2074}[profile]
    assert manifest['complete'] and manifest['all_nonzero'] and manifest['Qmax']==120
    assert expected==list(map(tuple,manifest['requested_pairs']))==list(map(tuple,manifest['completed_pairs']))
    primes=set();files=[];rows={};exact_matches=0;divisions=support=ordered=0
    for Q,h in expected:
        path=directory/f'Q{Q}_h{h}.json';r=json.loads(path.read_text())
        assert (r['profile'],r['Q'],r['h'],r['delta'],r['first_resonance'],r['mode'])==(profile,Q,h,str(F(2*h,Q)),Q,2*h-3)
        assert r['all_checks_pass'] and r['certified_nonzero']
        if profile=='cand007':
            source=r['source'];assert sha256(Path(source['path']).read_bytes()).hexdigest()==source['sha256']
        else:assert r['source'] is None
        assert r['attempts'] and r['attempts'][-1]['kappa']
        for attempt in r['attempts']:
            p=attempt['prime'];primes.add(p);assert fmpz(p).is_prime()
            assert 0<=attempt['kappa']<p and 0<=attempt['forcing']<p
            assert (attempt['forcing']+(2*h-2)*attempt['kappa'])%p==0
            assert attempt['ordered_pairs']==Q*(Q-1)//2
            assert attempt['checked_divisions']>Q and attempt['support_and_symmetry_checks']>Q
            assert len(attempt['final_density_sha256'])==64
            divisions+=attempt['checked_divisions'];support+=attempt['support_and_symmetry_checks'];ordered+=attempt['ordered_pairs']
        exact_matches+=len(r['exact_references']);files.append(digest(path));rows[(Q,h)]=r
    peerpath=Path('../a4-lead/code/modscan')/f'scan_{profile}_Q120.jsonl'
    peer=[];peerreceipt=None
    if peerpath.exists():
        raw=peerpath.read_bytes();peerhash=sha256(raw).hexdigest();snapshot=ROOT/'sources'/f'polar_{profile}_{peerhash[:12]}.jsonl';snapshot.write_bytes(raw);peerreceipt=dict(path=str(peerpath),bytes=len(raw),sha256=peerhash,snapshot=str(snapshot))
        for line in raw.splitlines():
            if not line.strip():continue
            try:r=json.loads(line)
            except json.JSONDecodeError:continue
            if 'Q' not in r or 'residues' not in r:continue
            key=(r['Q'],r['h']);assert key in rows
            ours={v['prime']:v['kappa'] for v in rows[key]['attempts']}
            compared=0
            for p,kap in r['residues']:
                if p in ours:assert kap==ours[p],(profile,key,p,kap,ours[p]);compared+=1
            assert compared and r['status']=='nonzero'
            peer.append(key)
        assert len(set(peer))==len(peer)
    B=20 if profile=='cand007' else 2
    overflow_bound=(B*60+1)*(max(primes)-1)**2
    assert overflow_bound<2**63-1
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
        profile=profile,complete_grid=True,points=len(expected),all_nonzero=True,primes=sorted(primes),
        exact_rational_reference_matches=exact_matches,total_checked_divisions=divisions,
        total_support_and_symmetry_checks=support,total_ordered_pairs=ordered,
        polar_compared_points=len(peer),polar_complete=set(peer)==set(expected),polar_source=peerreceipt,
        int64_convolution_upper_bound=overflow_bound,manifest=digest(manifest_path),files=files,
        actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'{profile}_grid_review.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='files'}),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--profiles',default='cand007,sin1');a=ap.parse_args()
    for profile in a.profiles.split(','):audit(profile)
    (ROOT/'sources/modular_grid_audit.py').write_bytes(Path(__file__).read_bytes())
