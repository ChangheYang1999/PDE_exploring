"""Collect completed twenty-branch prefix receipts without rerunning arithmetic."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from fractions import Fraction
import gzip, json
ROOT = Path('research/261_period_seven_eight_prefixes')
def read(p):
    raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def ref(p): return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def checkref(r): assert ref(Path(r['path']))=={k:r[k] for k in ('path','sha256')}
rows=[]
for Q in (7,8):
    for i in range(1,11):
        a=ROOT/f'verification/Q{Q}_root{i}_checks.json.gz'
        b=ROOT/f'verification/Q{Q}_root{i}_polar_replay.json.gz'
        c=ROOT/f'verification/Q{Q}_root{i}_review.json'
        d,p,r=map(read,(a,b,c))
        assert all(x['all_checks_pass'] and x['Q']==Q and x['root_index']==i and x['maximum_order']==8*Q for x in (d,p,r))
        assert (d['bits'],p['bits'])==(1536,2048)
        assert p['source']==ref(a) and r['source']==ref(a)
        for source in d['inputs']+[d['exact_prefix']]: checkref(source)
        assert len(d['cases'])==len(r['cases'])==4
        assert [x['N'] for x in d['cases']]==[2*Q,4*Q,6*Q,8*Q]
        for x,y in zip(d['cases'],r['cases']):
            assert (x['N'],x['q'],x['box'])==(y['N'],y['q'],y['box'])
            assert y['exact_scalar_identities']==6*Q
            checkref(x['box'])
        assert len(d['norms'])==len(p['norms'])==8*Q
        assert len(d['harmonics'])==len(p['harmonics'])==7
        assert d['exact_prefix_comparisons']==8*Q*Q
        assert d['direct_response_checks']==1
        assert p['independent_norm_comparisons']==16*Q and p['independent_tuning_comparisons']==7
        best=min(d['cases'],key=lambda x:(x['q'],x['N']))
        row=dict(Q=Q,root_index=i,best_N=best['N'],best_q=best['q'],radius_exponent=str(Fraction(best['q'],2)),s=d['s'],exact_prefix_comparisons=d['exact_prefix_comparisons'],cartesian_counts=d['counts'],polar_counts=p['counts'],independent_norm_comparisons=p['independent_norm_comparisons'],independent_tuning_comparisons=p['independent_tuning_comparisons'],scalar_identities=sum(x['exact_scalar_identities'] for x in r['cases']),cartesian_elapsed_s=d['actual_elapsed_s'],polar_elapsed_s=p['actual_elapsed_s'],scalar_elapsed_s=r['actual_elapsed_s'],cartesian=ref(a),polar=ref(b),scalar=ref(c))
        rows.append(row)
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_receipt_checks_pass=True,scope='Receipt integrity and counts, not a fresh arithmetic replay.',rows=rows)
(ROOT/'verification/collection.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'sources/collect_period_prefix_admission.py').write_bytes(Path(__file__).read_bytes())
for Q in (7,8):
    print('Q',Q,'q',[x['best_q'] for x in rows if x['Q']==Q],'N',[x['best_N'] for x in rows if x['Q']==Q])
print('totals', {k:sum(x[k] for x in rows) for k in ('exact_prefix_comparisons','independent_norm_comparisons','independent_tuning_comparisons','scalar_identities','cartesian_elapsed_s','polar_elapsed_s','scalar_elapsed_s')})
