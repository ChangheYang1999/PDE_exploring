"""Independent exact Cartesian audit of the numerical 122-case table."""
from datetime import datetime,timezone
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import json,time,argparse
from rational_scan_audit import compute


def prime(p):return p>=2 and all(p%d for d in range(2,int(p**.5)+1))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=float,default=500);args=ap.parse_args()
    start=time.monotonic();root=Path('research/57_prime_table');src=Path('../a4-num/notes/prime_congruence_sin1.json');snap=root/'sources/prime_congruence_sin1.json'
    if not snap.exists():snap.write_bytes(src.read_bytes())
    raw=snap.read_bytes();data=json.loads(raw);pairs=[(p,a) for p in range(5,62) if prime(p) for a in range(4,p,2) if p<4*a<3*p]
    assert len(pairs)==122 and [(r['p'],r['a']) for r in data['cases']]==pairs
    assert data['ok']==122 and data['mismatch']==0 and data['skipped']==0 and data['profile']=='sin1' and data['alpha1']=='1'
    rows=[]
    for expected in data['cases']:
        p,a=expected['p'],expected['a'];out=root/'verification'/f'p{p}_a{a}.json'
        if out.exists():r=json.loads(out.read_text())
        else:
            if time.monotonic()-start>args.seconds:break
            r=compute(Fraction(a,p),{1:'1'},p);q=Fraction(r['kappa_exact']);assert q.denominator%p
            residue=q.numerator*pow(q.denominator,-1,p)%p;pred=pow(-1,(a-4)//2,p)
            assert residue==pred==expected['kappa_residue_mod_p']==expected['predicted']
            assert not expected['kappa_is_zero'] and q and expected['status']=='OK' and expected['n0']==p and expected['j0']==a//2-1
            approx=float(q);err=abs(approx-expected['kappa_float'])/abs(approx);assert err<1e-14
            r.update(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),residue=residue,predicted=pred,matches_report=True,reported_float_relative_error=err)
            out.write_text(json.dumps(r,indent=2)+'\n')
            print(json.dumps(dict(delta=r['delta'],matches=True,elapsed_s=r['elapsed_s'])),flush=True)
        rows.append(dict(p=p,a=a,residue=r['residue'],reported_float_relative_error=r['reported_float_relative_error'],evidence=str(out)))
        summary=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),source_sha256=sha256(raw).hexdigest(),code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),expected_count=len(pairs),completed_count=len(rows),all_complete=len(rows)==len(pairs),checks=rows,actual_current_run_elapsed_s=time.monotonic()-start)
        (root/'verification/summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for name in ['prime_table_audit.py','rational_scan_audit.py','laurent_log_audit.py']:
        (root/'sources'/f'{name}.txt').write_bytes(Path('code',name).read_bytes())
    print('Completed',len(rows),'of',len(pairs),'elapsed',time.monotonic()-start,flush=True)

if __name__=='__main__':main()
