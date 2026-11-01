"""Replay retained exact response certificates and record a completed branch."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse,json,re,sys
sys.set_int_max_str_digits(0)
ROOT=Path('research/163_other_candidate_shaped_roots')
def unpack(v):
    return F(v[0])*F(2)**int(v[1]),F(v[2])*F(2)**int(v[3])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=int,required=True);ap.add_argument('--entry',type=int,required=True);args=ap.parse_args();i,v=args.root,args.entry
    now=datetime.now(timezone.utc).isoformat(timespec='seconds');ledger=Path('VERIFY_REPORT.md');assert f'## V{v} |' not in ledger.read_text()
    folder=ROOT/'verification';p=folder/f'root{i}_checks.json';raw=p.read_bytes();d=json.loads(raw);c=json.loads((folder/f'root{i}_coverage.json').read_text());r=json.loads((folder/f'root{i}_radius.json').read_text());s=F(d['lower_bound'])
    assert d['all_index_lower_bound_proved'] and d['all_finite_checks_pass'] and d['arithmetic_bits']==768
    assert len(d['finite'])==52 and [x['k'] for x in d['finite']]==list(range(1,53))
    assert d['full_dense_overlap_indices']==list(range(46,53)) and d['sparse_dense_overlap_count']==3
    for row in d['finite']+[dict(exact_dyadic=d['sigma_infinity_exact_dyadic'])]:
        mid,rad=unpack(row['exact_dyadic']);assert rad>=0 and abs(mid)-rad>s
    for path,key in [('research/156_candidate_shaped_compatibility/verification/polynomial.json','source_sha256'),('research/156_candidate_shaped_compatibility/verification/checks.json','root_source_sha256')]:
        assert sha256(Path(path).read_bytes()).hexdigest()==d[key]
    previous=F(0);target=F(1,182);counts=dict(accepted=0,empty=0)
    for node in sorted(c['nodes'],key=lambda x:F(x['a'])):
        address=node['address'];assert set(address)<=set('01');width=target/F(2**len(address));a=int(address or '0',2)*width;b=a+width
        assert a==F(node['a'])==previous and b==F(node['b']);previous=b
        low=(1/b+2)/4;lower=max(46,-(-low.numerator//low.denominator));upper=None if not a else ((1/a+2)/4).__floor__()
        assert lower==node['lower'] and upper==node['upper']
        if node['status']=='accepted':
            mid,rad=unpack(node['response_exact_dyadic']);assert rad>=0 and abs(mid)-rad>s
        else:assert node['status']=='empty' and upper is not None and upper<lower
        counts[node['status']]+=1
    assert previous==target and counts=={k:c[k] for k in counts} and c['split']==sum(counts.values())-1
    assert c['exact_replay_pass'] and F(c['lower_bound'])==s
    box=list(map(F,r['box']));image=list(map(F,r['image']));old=list(map(F,r['previous_image']))
    assert all(0<=x<b for x,b in zip(image,box)) and any(x>=b for x,b in zip(old,box))
    q=r['z_dyadic_exponent'];assert F(r['radius_dyadic_exponent'])==F(9*q,4)
    assert F(r['exact_leading_norm_upper'])<F(r['a']) and F(r['s'])==s
    assert F(r['original_amplitude'])**9<2**38
    restored=r['restored_amplitude_sufficient_integer_exponent'];assert restored>F(9*q+38,4)
    review=dict(checked_at_utc=now,root_index=i,entry=v,verdict='CONFIRMED',finite_checks=52,coverage=counts,splits=c['split'],exact_partition_replay=True,retained_box_inequalities_pass=True,source_check_sha256=sha256(raw).hexdigest(),lower_bound=str(s),radius_summary=d['radius_summary'])
    (folder/f'root{i}_review.json').write_text(json.dumps(review,indent=2)+'\n')
    result=f"Root{i}, b={d['root_ball']}, satisfies |sigma_k|>{s} for every integer k>=1. All52finite checks, seven full/compact comparisons and three sparse/dense comparisons pass. The exact compact cover has{c['accepted']}accepted leaves,{c['empty']}empty leaves and{c['split']}splits. An independent address-based rational replay confirms every endpoint, integer exclusion and retained lower bound. The limiting response is{d['sigma_infinity']}. The original145majorant with a={r['a']} passes at q={q}, giving normalized R>2^({r['radius_dyadic_exponent']})|epsilon|^(9/4) and restored original-amplitude R>2^{restored}. Actual root computation{d['actual_elapsed_s']}seconds."
    with ledger.open('a') as f:f.write(f"\n## V{v} | {now} | Candidate-shaped root{i} uniform response\n\nClaim: this compatible Candidate-shaped root yields a convergent tuned exterior series at delta=4/9.\n\nMethod: independent768-bit Cartesian response calculation, compact all-index interval coverage, exact rational certificate replay, and the already reviewed145majorant.\n\nResult: {result}\n\nVerdict: CONFIRMED. This branch is PROVED, including convergence of all weighted derivatives and the common potential under145. It does not establish an optimal radius or convergence at the original stored exponent. Evidence163/root{i}.\n")
    p=ROOT/'PROOF.md';t=p.read_text();admitted=sorted({1,2,4,5}|{int(x.stem.split('_')[0][4:]) for x in folder.glob('root*_review.json')});pending=sorted({6,7}-set(admitted))
    status='Status: roots'+','.join(map(str,admitted))+' are PROVED by the reviewed theorem145 and certificate construction158. Root3 is proved separately in158. '+('Roots'+','.join(map(str,pending))+' remain pending.' if pending else 'All seven branches are proved.')
    t=re.sub(r'^Status:.*$',status,t,count=1,flags=re.M)+f'\n## Root{i} completion at {now}\n\n{result} PROVED by V{v}.\n';p.write_text(t)
    p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} | V{v}: Candidate-shaped root{i} all-index certificate completed\n\n{result}\n\n'+p.read_text())
    with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V{v} admits163root{i}, uniform s={s}, old normalized exponent{r["radius_dyadic_exponent"]}, restored exponent{restored}; full exact cover replay passed.\n')
    p=Path('research/INDEX.md');t=p.read_text();t=re.sub(r'^163\..*$',f'163. [Other compatible Candidate-shaped profiles](163_other_candidate_shaped_roots/PROOF.md): PROVED roots{",".join(map(str,admitted))}; root3 separately158; pending{",".join(map(str,pending)) or "none"}.',t,flags=re.M);p.write_text(t)
    (ROOT/'sources'/'admit_candidate_response.py').write_bytes(Path(__file__).read_bytes())
    files={}
    for p in ROOT.rglob('*'):
        if p.is_file() and p.name not in ['MANIFEST.json','progress.json'] and p.suffix!='.log' and '.partial.' not in p.name:
            b=p.read_bytes();files[str(p.relative_to(ROOT))]=dict(bytes=len(b),sha256=sha256(b).hexdigest())
    (folder/'MANIFEST.json').write_text(json.dumps(dict(checked_at_utc=now,admitted_roots=admitted,files=files),indent=2)+'\n');print(now,f'V{v}',f'root{i}','admitted')
if __name__=='__main__':main()
