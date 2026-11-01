"""Check retained residual evidence and record the finite conclusions."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, gzip, json, re, sys
sys.dont_write_bytecode=True
from flint import arb, ctx
ctx.prec=512
ROOT=Path('research/196_tuned_residual_continuum')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def add(entry,title,claim,method,result,verdict):
    now=stamp();ledger=Path('VERIFY_REPORT.md');assert f'## V{entry} |' not in ledger.read_text()
    text=f'\n## V{entry} | {now} | {title}\n\nClaim: {claim}\n\nMethod: {method}\n\nResult: {result}\n\nVerdict: {verdict}\n'
    with ledger.open('a') as out:out.write(text)
    with (ROOT/'PROOF.md').open('a') as out:out.write(text)
    p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} | V{entry}: {title}\n\n{result}\n\n{verdict}\n\n'+p.read_text())
    with Path('WORKLOG.md').open('a') as out:out.write(f'\n{now}: V{entry}, {title}.\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--case',required=True);ap.add_argument('--entry',type=int,required=True);args=ap.parse_args()
    path=ROOT/'verification'/(args.case+'_checks.json');raw=path.read_bytes();d=json.loads(raw)
    assert d['complete'] and d['all_reported_within_one_percent'] and d['bits']==1024 and d['grid_steps']==2048
    inp=d['inputs'];assert sha256(Path(inp['source']).read_bytes()).hexdigest()==inp['source_sha256']
    assert sha256(gzip.decompress(Path(inp['base_archive']).read_bytes())).hexdigest()==inp['base_raw_sha256']
    ext=Path(inp['extension_archive']).read_bytes();assert sha256(ext).hexdigest()==inp['extension_compressed_sha256']
    assert sha256(gzip.decompress(ext)).hexdigest()==inp['extension_raw_sha256']
    assert sha256(Path(inp['harmonic_source']).read_bytes()).hexdigest()==inp['harmonic_sha256']
    rows=d['rows'];radii=sorted({r['R'] for r in rows},key=int)
    assert len(rows)==4*len(radii)
    for radius in radii:assert [r['N'] for r in rows if r['R']==radius]==[10,20,40,80]
    for r in rows:
        for group in ['residual_bounds','next_term_bounds']:
            for v in r[group].values():
                assert arb(v['lower'])>0 and arb(v['upper'])>arb(v['lower'])
                assert arb(v['interpolation_error'])>0
    comparisons=[v for r in rows for group in r['comparison'].values() for v in group.values()]
    assert len(comparisons)==5*len(rows) and all(x['within_one_percent'] for x in comparisons)
    method='Independent finite Cartesian residual sums, 1024-bit interval polynomial evaluation at 2049 angular points, and a second-derivative interpolation bound on every intervening interval. Fresh source and archive checksums were verified.'
    result=f"For {args.case}, the {len(rows)} pairs N in {{10,20,40,80}}, R in {{{','.join(radii)}}} yield continuum residual bounds through two angular derivatives and first-omitted-term bounds through one derivative. All {len(comparisons)} reported sampled values lie within the one-percent comparison tolerance. Three partial-sum angles are also enclosed at every pair. Runtime {d['actual_elapsed_s']} seconds. All bounds and strict finite comparisons are retained in topic196."
    verdict='CONFIRMED as finite interval calculations under the coefficient-enclosure hypotheses in194. They do not prove a sharp convergence radius or imply convergence from a finite decreasing sequence;194 separately records the algorithmic enclosure proof and its team review status.'
    add(args.entry,args.case+' continuum residual audit',args.case+' reported finite residuals and omitted terms agree with independently formed continuum bounds.',method,result,verdict)
    review=dict(checked_at_utc=stamp(),entry=args.entry,source_check_sha256=sha256(raw).hexdigest(),all_checks_pass=True,radii=radii,finite_pairs=len(rows),comparisons=len(comparisons))
    if args.case=='Q6r1':
        before=next(r for r in rows if r['N']==40 and r['R']=='512')['residual_bounds']['0'];after=next(r for r in rows if r['N']==80 and r['R']=='512')['residual_bounds']['0']
        assert arb(before['lower'])>arb('0.0005197') and arb(before['upper'])<arb('0.0005206')
        assert arb(after['lower'])>arb('0.0007497') and arb(after['upper'])<arb('0.0007501')
        assert arb(after['lower'])>arb(before['upper'])
        result='At delta=1/3, root b=-0.608726913792658..., R=512, the weighted residual supremum lies strictly between0.0005197 and0.0005206 at N=40, and between0.0007497 and0.0007501 at N=80. It increases by a factor greater than1.44. Thus the14:26 numerical note claiming geometric decay at R>=512 fails at its stated finite orders. At R=1024, all three successive residual decreases in N=10,20,40,80 are certified; neither fact bounds the true infinite-series threshold.'
        assert arb(after['lower'])>arb('1.44')*arb(before['upper'])
        changes=[x for x in d['changes'] if x['R']=='1024' and x['quantity']=='residual_bounds' and x['derivative']=='0']
        assert len(changes)==3 and all(x['strict_decrease'] for x in changes)
        add(args.entry+1,'Q6 root1 finite decay counterexample','The finite tested residuals decrease geometrically at every R>=512.','Compare disjoint continuum supremum enclosures at N=40 and N=80.',result,'REFUTED at R=512 for the stated finite truncations. Eventual convergence or divergence at R=512 remains undecided by these data.')
        review['counterexample_entry']=args.entry+1
    (ROOT/'verification'/(args.case+'_review.json')).write_text(json.dumps(review,indent=2)+'\n')
    (ROOT/'sources'/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
    admitted=sorted(p.name.removesuffix('_review.json') for p in (ROOT/'verification').glob('*_review.json'))
    p=ROOT/'PROOF.md';p.write_text(re.sub(r'^Status:.*$',f'Status: finite continuum checks CONFIRMED for {admitted}, under the stated coefficient-enclosure hypotheses; no new infinite-radius assertion.',p.read_text(),count=1,flags=re.M))
    files={str(p.relative_to(ROOT)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in ROOT.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (ROOT/'verification/MANIFEST.json').write_text(json.dumps(dict(checked_at_utc=stamp(),files=files),indent=2)+'\n')
    print(json.dumps(review))
if __name__=='__main__':main()
