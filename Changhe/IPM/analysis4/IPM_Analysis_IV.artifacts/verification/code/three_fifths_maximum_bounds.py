"""Exact endpoint and derivative bounds for the last two 3/5 profiles."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
ROOT=Path('research/214_three_fifths_interior_maximum')
def one(index):
    assert index in [3,4]
    started=time.monotonic()
    rp=Path(f'research/205_three_fifths_prefix_radii/verification/root{index}_checks.json')
    rd=json.loads(rp.read_text());assert rd['all_checks_pass']
    selected=min(rd['cases'],key=lambda row:(row['q'],row['N']))
    cp=Path(selected['path']);cd=json.loads(cp.read_text());box=cd['adaptive'];q=box['q'];N=cd['N'];Q=cd['Q'];B=cd['B']
    vp=rp.with_name(f'root{index}_review.json');vd=json.loads(vp.read_text());assert vd['all_checks_pass']
    assert any(r['path']==str(cp) and r['sha256']==sha256(cp.read_bytes()).hexdigest() and r['strict_invariance'] for r in vd['rows'])
    assert cd['h']==3 and Q==10 and B==4
    d=list(map(F,cd['initial_density']));xb=list(map(F,box['box'][Q:]));assert len(d)==N and len(xb)==Q
    op=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');od=json.loads(op.read_text());assert od['all_checks_pass']
    blo,bhi=map(F,od['real_roots'][index-1]['interval']);assert F(1,9)<blo<bhi<1
    trials=[]
    for t in range(q//Q+1,q//Q+16):
        z=F(1,2**t);eta=F(2)**(q-Q*t);assert 0<eta<=F(1,2)
        u1=B*(sum(d[n-1]*z**(n-1) for n in range(2,N+1))+sum(xb[r-1]*z**(N+r-1) for r in range(1,Q+1)))
        u2=B**2*(sum(n*d[n-1]*z**(n-1) for n in range(2,N+1))+sum((N+r+Q*eta)*xb[r-1]*z**(N+r-1) for r in range(1,Q+1)))
        u4=B**4*(sum(n**3*d[n-1]*z**(n-1) for n in range(2,N+1))+sum(((N+r)**3+3*(N+r)**2*Q*eta+F(27,4)*(N+r)*Q**2*eta+8*Q**3*eta)*xb[r-1]*z**(N+r-1) for r in range(1,Q+1)))
        margins=[1-bhi,min(1+3*blo,9*blo-1),72*blo]
        passed=all(u<m for u,m in zip([u1,u2,u4],margins))
        trials.append(dict(t=t,eta=str(eta),U1=str(u1),U2=str(u2),U4=str(u4),margins=list(map(str,margins)),passes=passed))
        if passed:break
    assert passed
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,root_index=index,N=N,q=q,t=t,radius_exponent=str(F(5*t,3)),amplitude_exponent='5/3',unique_first_quadrant_maximum=True,positivity=True,trials=trials,inputs={str(p):sha256(p.read_bytes()).hexdigest() for p in [rp,cp,vp,op]},actual_elapsed_s=time.monotonic()-started)
    (ROOT/'verification'/f'root{index}_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'sources'/'three_fifths_maximum_bounds.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k not in ['trials','inputs']}),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');a=ap.parse_args()
    for i in map(int,a.roots.split(',')):one(i)
