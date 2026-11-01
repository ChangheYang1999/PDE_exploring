"""Exact profile-sign certificates from an already verified residue box."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
sys.set_int_max_str_digits(0)
ROOT=Path('research/210_three_fifths_profile_geometry')

def one(index):
    started=time.monotonic()
    rp=Path(f'research/205_three_fifths_prefix_radii/verification/root{index}_checks.json')
    rd=json.loads(rp.read_text());assert rd['all_checks_pass']
    selected=min(rd['cases'],key=lambda row:(row['q'],row['N']))
    cp=Path(selected['path']);cd=json.loads(cp.read_text());box=cd['adaptive'];q=box['q'];N=cd['N'];Q=cd['Q'];B=cd['B']
    reviewp=rp.with_name(f'root{index}_review.json');review=json.loads(reviewp.read_text());assert review['all_checks_pass']
    assert any(r['path']==str(cp) and r['sha256']==sha256(cp.read_bytes()).hexdigest() and r['strict_invariance'] for r in review['rows'])
    assert cd['h']==3 and Q==10 and B==4
    d=list(map(F,cd['initial_density']));xb=list(map(F,box['box'][Q:]));assert len(d)==N and len(xb)==Q
    op=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');ob=json.loads(op.read_text());assert ob['all_checks_pass']
    blo,bhi=map(F,ob['real_roots'][index-1]['interval']);eta1=1-bhi;eta2=1-9*bhi
    trials=[]
    for t in range(q//Q+1,q//Q+11):
        z=F(1,2**t);theta=F(2)**(q-Q*t);assert 0<theta<=F(1,2)
        u1=B*(sum(d[n-1]*z**(n-1) for n in range(2,N+1))+sum(xb[r-1]*z**(N+r-1) for r in range(1,Q+1)))
        u2=B*B*(sum(n*d[n-1]*z**(n-1) for n in range(2,N+1))+sum((N+r+Q*theta)*xb[r-1]*z**(N+r-1) for r in range(1,Q+1)))
        passed=u1<eta1 and (index>2 or u2<eta2)
        trials.append(dict(t=t,theta=str(theta),U1=str(u1),U2=str(u2),positive_margin=str(eta1),monotonicity_margin=str(eta2) if index<=2 else None,passes=passed))
        if passed:break
    assert passed
    record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,N=N,q=q,t=t,radius_exponent=str(F(5*t,3)),amplitude_exponent='5/3',positivity=True,angular_monotonicity=index<=2,trials=trials,inputs={str(p):sha256(p.read_bytes()).hexdigest() for p in [rp,cp,reviewp,op]},actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'root{index}_sign_checks.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['trials','inputs']}),flush=True)
    (ROOT/'sources'/'three_fifths_sign_bounds.py').write_bytes(Path(__file__).read_bytes())

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');a=ap.parse_args()
    for index in map(int,a.roots.split(',')):one(index)
