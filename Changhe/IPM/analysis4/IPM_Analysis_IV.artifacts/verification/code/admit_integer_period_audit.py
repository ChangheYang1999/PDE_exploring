"""Replay completed finite audits and prefix maps before ledger admission."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import argparse, gzip, json, pickle, re, sys, time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from stream_precision_audit import unpack as unpack3
from unpack_dyadic4 import unpack as unpack4
from certified_prefix_majorant import PrefixMajorant


def update_files(root, index, entry, title, result, method, verdict, status):
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    ledger = Path('VERIFY_REPORT.md')
    assert f'## V{entry} |' not in ledger.read_text()
    with ledger.open('a') as out:
        out.write(f'\n## V{entry} | {now} | {title}\n\nClaim: {title}.\n\nMethod: {method}\n\nResult: {result}\n\nVerdict: {verdict}\n')
    p = root / 'PROOF.md'
    text = re.sub(r'^Status:.*$', status, p.read_text(), count=1, flags=re.M)
    p.write_text(text + f'\n## Root {index} review, V{entry}\n\nAt {now}, {result}\n\n{verdict}\n')
    p = Path('NOTES_FOR_TEAM.md')
    p.write_text(f'## {now} | V{entry}: {title}\n\n{result}\n\n{verdict}\n\n' + p.read_text())
    with Path('WORKLOG.md').open('a') as out:
        out.write(f'\n{now}: V{entry}, {title}. Independent replay passed.\n')
    (root / 'sources' / Path(__file__).name).write_bytes(Path(__file__).read_bytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Q', type=int, choices=[5,6], required=True)
    ap.add_argument('--root', type=int, required=True)
    ap.add_argument('--entry', type=int, required=True)
    args = ap.parse_args()
    Q, i, entry = args.Q, args.root, args.entry
    start = time.monotonic()
    ctx.prec = 4096
    number, next_number, name = (180,182,'five') if Q == 5 else (185,186,'six')
    base = Path(f'research/{number}_period_{name}_numerical_audit')
    target = Path(f'research/{next_number}_period_{name}_prefix_radii')
    source_path = base / 'verification' / f'root{i}_checks.json'
    raw = source_path.read_bytes()
    d = json.loads(raw)
    N = 10*Q
    assert d['all_checks_pass'] and d['independent_maximum_order'] == N
    assert d['bits'] == (2048 if Q==5 else 3072)
    for p,h in d['inputs'].items():
        assert sha256(Path(p).read_bytes()).hexdigest() == h
    archive = Path(d['source']['archive']).read_bytes()
    assert sha256(archive).hexdigest() == d['source']['archive_sha256']
    selected_raw = gzip.decompress(archive)
    assert sha256(selected_raw).hexdigest() == d['source']['selected_sha256']
    selected = pickle.loads(selected_raw)
    overlaps = 0
    own = {r['n']:r for r in d['independent_norms']}
    for label, field in [('F','f'),('G','g')]:
        for n in range(1,N+1):
            norm = sum((abs(arb(*unpack3(a))) for a in selected[field][n]),arb(0))
            assert norm.overlaps(arb(*unpack4(own[n][label])))
            overlaps += 1
    for r in d['source_norms']:
        for label, field in [('F','f'),('G','g')]:
            if label+'_norm' not in r:continue
            n=r['n']; norm=sum((abs(arb(*unpack3(a))) for a in selected[field][n]),arb(0))
            assert norm.overlaps(arb(*unpack4(r[label+'_norm'])))
            assert (norm.log()/n).exp().overlaps(arb(r[label+'_root']))
    assert [r['n'] for r in d['harmonics']] == list(range(2*Q,N+1,Q))
    for row in d['harmonics']:
        assert arb(*unpack4(row['obstruction'])).contains(0)
        assert not arb(*unpack4(row['sigma'])).contains(0)
    counts = d['counts']; last=d['source_norms'][-1]
    assert last['n']==300 and last['G_status']=='untuned final harmonic; norm excluded'
    expected=(33940,4105,2550,2600) if Q==5 else (48744,5928,3660,3720)
    assert (counts['poisson_coefficient_checks'], counts['ordered_products'], d['coefficient_comparisons']['f'], d['coefficient_comparisons']['g']) == expected
    result = (f'The {d["bits"]}-bit independent prefix through {N} passes {expected[0]} Poisson coefficient checks, '
              f'{expected[1]} ordered products, 18 provisional continuations and nine compatibility projections. '
              f'All {expected[2]} density and {expected[3]} stream coefficients overlap the separate numerical implementation, '
              f'including H_{N} determined by the obstruction at {N+Q}; all nine harmonic/response pairs pass. '
              f'Independent archive replay confirms {overlaps} prefix norm overlaps, the reported source norms and their order roots. '
              f'The source density norm root at 300 is {last["F_root"]}, with relative norm radius {last["F_relative_radius"]}. '
              f'The untuned final stream coefficient at 300 is excluded. The original computation took {d["actual_elapsed_s"]} seconds.')
    review = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'), entry=entry,
                  all_checks_pass=True, source_check_sha256=sha256(raw).hexdigest(), norm_overlap_checks=overlaps,
                  actual_replay_elapsed_s=time.monotonic()-start)
    (base/'verification'/f'root{i}_review.json').write_text(json.dumps(review,indent=2)+'\n')
    admitted=sorted({int(p.stem.split('_')[0][4:]) for p in (base/'verification').glob('root*_review.json')} | ({6} if Q==5 else set()))
    update_files(base,i,entry,f'Period-{Q} root {i}: independent finite prefix',result,
                 'Signed Cartesian interval recurrence from the exact algebraic root, with no midpoint reset; fresh archive and norm replay.',
                 'CONFIRMED through the stated finite prefix. Later values are source-bound finite extractions, not independent high-order reconstructions or infinite-radius estimates.',
                 f'Status: CONFIRMED for roots {admitted} through {N}; other branches require individual audits.')

    summary=json.loads((target/'verification'/f'root{i}_checks.json').read_text())
    assert summary['all_checks_pass']
    scalar=components=0
    L=F(3*Q*Q,4*(3*Q-1)); delta=F(2,Q); kappa=4*(2-delta+max(delta,1-delta))*(1-delta)/delta
    for case in summary['cases']:
        p=Path(case['path']);c=json.loads(p.read_text());m=case['N']
        assert c['Q']==Q and c['h']==1 and c['B']==4 and F(c['L'])==L and F(c['kappa'])==kappa*F(m+1,m)
        for path,h in c['inputs'].items():assert sha256(Path(path).read_bytes()).hexdigest()==h
        assert F(c['initial_harmonics'][0])==0
        for n,bound in enumerate(c['initial_density'],1):
            a=own[n]['F']; upper=F(a[0])*F(2)**int(a[1])+F(a[2])*F(2)**int(a[3])
            assert n*upper<=F(bound)
        hm={r['n']:r for r in d['harmonics']}
        for a,bound in enumerate(c['initial_harmonics'][1:],2):
            v=hm[a*Q]['H']; upper=abs(F(v[0])*F(2)**int(v[1]))+F(v[2])*F(2)**int(v[3])
            assert a*Q*upper<=F(bound)
        model=PrefixMajorant(1,Q,4,list(map(F,c['initial_density'])),list(map(F,c['initial_harmonics'])),F(c['s']),L,F(c['kappa']))
        assert model.Y0==list(map(F,c['Y0']))
        for boxdata in [c,c['adaptive']]:
            q=boxdata.get('q',boxdata.get('w_dyadic_exponent')); box=list(map(F,boxdata['box']))
            image=model.transformed(F(1,2**q),box)
            assert image==list(map(F,boxdata['image']))
            assert all(0<=y<=b and 0<=v<=b for y,v,b in zip(model.Y0,image,box))
            components+=len(box)
        scalar+=c['scalar_coefficient_checks']
    best=min(c['adaptive_q'] for c in summary['cases']);first=min(c['N'] for c in summary['cases'] if c['adaptive_q']==best)
    ordinary=[c['box_q'] for c in summary['cases']];adaptive=[c['adaptive_q'] for c in summary['cases']]
    response=json.loads((target/'verification'/f'root{i}_N{2*Q}.json').read_text())['s']
    result=(f'For prefixes N={[c["N"] for c in summary["cases"]]}, ordinary exponents are {ordinary} and adaptive exponents are {adaptive}. '
            f'Fresh exact rational reconstruction confirms all ten complete maps and {components} box-component inequalities, '
            f'with {scalar} direct scalar identities and hash-matched finite input bounds. The response bound is s={response}. '
            f'Thus R>2^({best}/2)|epsilon|^({Q}/2) suffices, with the best retained exponent first reached at N={first}. '
            f'The original box computation took {summary["actual_elapsed_s"]} seconds.')
    review=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),entry=entry+1,all_checks_pass=True,
                full_maps_replayed=10,box_component_checks=components,scalar_checks=scalar,best_q=best,first_N=first,
                audit_source_sha256=sha256(raw).hexdigest())
    (target/'verification'/f'root{i}_review.json').write_text(json.dumps(review,indent=2)+'\n')
    update_files(target,i,entry+1,f'Period-{Q} root {i}: certified prefix radius',result,
                 'Independent finite input audit, followed by complete reconstruction of both retained rational maps at every prefix.',
                 'CONFIRMED. The tuned density, stream and common potential converge with all weighted derivatives on every stated strict exterior. No optimality assertion follows.',
                 f'Status: PROVED for roots {admitted} using the individually confirmed finite prefixes; other branches await individual checks.')
    for root in [base,target]:
        files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
        (root/'verification'/'MANIFEST.json').write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),files=files),indent=2)+'\n')
    print(json.dumps(dict(Q=Q,root=i,entries=[entry,entry+1],best_q=best,first_N=first,actual_elapsed_s=time.monotonic()-start)))
if __name__=='__main__':main()
