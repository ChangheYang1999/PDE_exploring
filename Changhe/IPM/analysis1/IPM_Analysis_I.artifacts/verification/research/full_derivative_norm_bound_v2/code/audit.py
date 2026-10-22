"""Whole saved-stream audit, independent reversed exact reduction and tail replay."""
from protocol import *
import argparse,time
from math import gcd,prod
import bounds

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);args=ap.parse_args();full=args.tag=='full';tag=args.tag;started=now();tick=time.monotonic()
    pins,deps,freeze=source();summary=load(OUT/(tag+'_summary.json'));assert summary['full_middle'] is full and summary['cells']==(7809 if full else 6)
    assert summary['status']==('COMPUTED_COMPLETE_DERIVATIVE_NORM_BOUNDS_REQUIRES_INDEPENDENT_AUDIT' if full else 'PASS_SIX_CELL_DERIVATIVE_PREPARATION_DIAGNOSTIC_ONLY')
    rehash(summary['files']);path=OUT/(tag+'_rows.jsonl');assert sha(path)==summary['rows_sha256']
    assert sha(OUT/(tag+'_tails.json'))==summary['tails_sha256'] and sha(OUT/(tag+'_restarts.jsonl'))==summary['restarts_sha256']
    refs=radial_rows();cells=list(range(7809)) if full else SMOKE;rows=[];hasher=hashlib.sha256();header=footer=None;equalities=0;compact_checks=0
    with path.open('rb') as f:
        for raw in f:
            assert raw.endswith(b'\n');z=parse(raw)
            if header is None:
                assert z['type']=='header' and z['schema']=='full-physical-derivative-norm-v1' and z['engines']==['arb512','iv200'] and z['source_freeze_sha256']==sha(OUT/'source_freeze.json') and z['cells']==cells and z['sources']==summary['files'] and z['parents']==deps and z['compact_endpoint_bits']==128;header=z
            elif z['type']=='cell':
                assert footer is None and z['cell']==cells[len(rows)];i=z['cell'];r=refs[i]
                assert z['actual_linear_identity_checks']==24044
                assert z['a']==r['a'] and z['b']==r['b'] and z['h']==r['h'] and z['array_manifest']==r['array_manifest']
                assert F(z['a'])<F(z['b']) and F(z['b'])-F(z['a'])<=F(z['h']) and 522*F(z['h'])<1
                if full and rows:assert rows[-1]['b']==z['a']
                assert len(z['exact_convolutions'])==4
                eq=0
                for v in z['exact_convolutions']:
                    C=int(v['coefficient_bound']);Q=int(v['modulus_product']);mods=v['moduli'];assert C>=0 and Q==prod(mods) and Q>2*C and v['all_equal'] is True
                    assert v['coefficients']==sum(v['lengths'])-1 and all(type(n) is int and n>0 for n in v['lengths']) and len(v['sha256'])==64
                    for j,m in enumerate(mods):assert 1<m<1<<63 and m%2 and all(gcd(m,n)==1 for n in mods[:j])
                    eq+=v['coefficients']
                assert eq==z['all_product_coefficient_equalities'];equalities+=eq
                for name in ['arb512','iv200']:
                    b=z['bounds'][name];assert {k:len(v) for k,v in b.items()}=={'B':3,'C':2,'dV':3,'dW':3,'error':3,'norm_squares':2}
                    for vals in b.values():
                        for v in vals:assert 0<=dyad(v['lo'])<=dyad(v['hi']);compact_checks+=1
                rows.append(z)
            else:
                assert footer is None and z['type']=='footer' and z['complete'] is True and z['cells']==len(rows)==len(cells) and z['prior_stream_sha256']==hasher.hexdigest() and z['all_product_coefficient_equalities']==equalities;footer=z
            hasher.update(raw)
    assert footer is not None and equalities==summary['all_product_coefficient_equalities']
    if full:assert F(rows[0]['a'])==bounds.A and F(rows[-1]['b'])==bounds.B
    tail=load(OUT/(tag+'_tails.json'));assert tail['counts']=={'inner_derivative_equalities':14672,'outer_derivative_equalities':10524,'weighted_moment_intersections':3508}
    # Independent exact reversed accumulation of every saved outward cell upper.
    for name in ['arb512','iv200']:
        for p in range(2):
            exact=sum((dyad(row['bounds'][name]['norm_squares'][p]['hi']) for row in reversed(rows)),F(0))
            assert exact==F(summary['engines'][name]['middle_bound_sums_exact'][p])
            exact+=sum(dyad(tail['bounds'][name][key][p]['hi']) for key in ['inner_norm_squares','outer_norm_squares'])
            box=summary['engines'][name]['whole_plane_bound_squares'][p];assert F(box['lower_exact'])<=exact<=F(box['upper_exact'])
            bound=F(summary['strict_decimal_ceilings'][p]);assert bound>0 and bound*bound>exact
            assert bound>F(summary['engines'][name]['whole_plane_norm_bounds'][p]['upper_exact'])
    events=[parse(s) for s in (OUT/(tag+'_restarts.jsonl')).read_text().splitlines()];required=set(REPLAY if full else SMOKE)
    for ev in events:
        assert ev['source_freeze_sha256']==summary['source_freeze_sha256'] and 0<=ev['completed']<=len(cells)
        if ev['last_completed'] is not None:assert ev['last_completed']==cells[ev['completed']-1];required.add(ev['last_completed'])
        if ev['completed']<len(cells):
            assert ev['first_uncompleted']==cells[ev['completed']];required.add(ev['first_uncompleted'])
        else:assert ev['first_uncompleted'] is None
    rehash(summary['files']);out={'start_utc':started,'utc':now(),'status':'PASS_COMPLETE_SAVED_DERIVATIVE_STREAM_AND_EXACT_REDUCTION','full_middle':full,'cells':len(rows),'all_product_coefficient_equalities':equalities,'compact_order_checks':compact_checks,'required_replay_cells':sorted(required),'rows_sha256':sha(path),'summary_sha256':sha(OUT/(tag+'_summary.json')),'tails_sha256':sha(OUT/(tag+'_tails.json')),'restarts_sha256':sha(OUT/(tag+'_restarts.jsonl')),'source_freeze_sha256':sha(OUT/'source_freeze.json'),'files':summary['files'],'seconds':time.monotonic()-tick,'scope':'Saved-stream and exact-sum validation, not a replacement for whole executed convolution comparisons. Whole selected cell and complete tail replay still required.'}
    write(OUT/(tag+'_audit.json'),out);print(canonical({k:v for k,v in out.items() if k!='files'}),flush=True)
if __name__=='__main__':main()
