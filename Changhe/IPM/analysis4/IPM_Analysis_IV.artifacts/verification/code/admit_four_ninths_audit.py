"""Record a manually authorized, completed four-ninths finite audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,re
ROOT=Path('research/183_four_ninths_numerical_audit')
def brief(text):return text.lstrip('[').split(' +/- ')[0][:25]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=int,required=True);ap.add_argument('--entry',type=int,required=True);args=ap.parse_args();i=args.root;v=args.entry
    ledger=Path('VERIFY_REPORT.md');assert f'## V{v} |' not in ledger.read_text()
    now=datetime.now(timezone.utc).isoformat(timespec='seconds');p=ROOT/'verification'/f'root{i}_checks.json';o=json.loads(p.read_text())
    assert o['all_checks_pass'] and o['independent_maximum_order']==72 and o['bits']==3072
    assert o['coefficient_comparisons']==dict(f=5256,g=5328)
    assert o['prior179_norm_overlaps']==72 and o['prior179_harmonic_overlaps']==7 and len(o['harmonics'])==8
    assert [x['n'] for x in o['harmonics']]==list(range(9,73,9))
    a=Path(o['source']['archive']).read_bytes();assert sha256(a).hexdigest()==o['source']['archive_sha256'];assert sha256(gzip.decompress(a)).hexdigest()==o['source']['selected_sha256']
    c=o['counts'];assert c['poisson_coefficient_checks']==73368 and c['ordered_products']==8964 and c['provisional_continuations']==16 and c['compatibility_projections']==8
    fits=o['finite_least_squares'];assert [q['last'] for q in fits]==[300,306]
    last=o['source_norms'][-1];assert last['n']==306 and last['G_status']=='untuned final harmonic; norm excluded'
    description=f"The150..300 and150..306 finite fits give A_fit={brief(fits[0]['A'])}... and{brief(fits[1]['A'])}..., with converted statistics{brief(fits[0]['radius_statistic'])}... and{brief(fits[1]['radius_statistic'])}.... SourceF306 norm root{brief(last['F_root'])}..., relative norm radius{last['F_relative_radius']}. SourceG306is untuned and excluded."
    review=dict(checked_at_utc=now,verdict='CONFIRMED',entry=v,root_index=i,counts=c,source_sha256=o['source']['sha256'],selected_sha256=o['source']['selected_sha256'],full_check_sha256=sha256(p.read_bytes()).hexdigest(),finite_fits=[{k:q[k] for k in ['first','last','A','radius_statistic']} for q in fits],scope='Independent coefficient prefix through72; later source-bound norms and finite regression only')
    (ROOT/'verification'/f'root{i}_review.json').write_text(json.dumps(review,indent=2)+'\n')
    admitted=sorted({1}|{int(q.stem.split('_')[0][4:]) for q in (ROOT/'verification').glob('root*_review.json')});pending=sorted(set(range(1,5))-set(admitted))
    p=ROOT/'PROOF.md';t=p.read_text();status='Status: CONFIRMED for roots'+','.join(map(str,admitted))+' through72. '+('Roots'+','.join(map(str,pending))+' remain in progress.' if pending else 'All four requested roots completed.')
    t=re.sub(r'^Status:.*$',status,t,count=1,flags=re.M);t+=f"\n## Completed root{i} audit\n\nAt {now}, all73368Poisson checks,8964ordered products,16provisional continuations and eight compatibility projections pass. All5256density and5328stream coefficients agree by interval overlap with the independent source, together with eightH/sigma pairs;179 contributes72norm and sevenpair overlaps. Runtime{o['actual_elapsed_s']}seconds. Selected archive hashes pass. {description} These finite statistics do not prove an infinite convergence boundary. V{v}.\n";p.write_text(t)
    with ledger.open('a') as f:f.write(f"\n## V{v} | {now} | Four-ninths root{i} independent audit and finite fits\n\nClaim: the root{i} branch has consistent tuned coefficients through72 and the reported finite norm growth.\n\nMethod: independent3072-bit Cartesian recurrence from the exact algebraic root interval without resets; H72tuned through81; separate Poisson differentiation and coefficientwise comparison. Interval normal equations give the two finite least-squares fits. Selected archive hashes are replayed.\n\nResult:73368Poisson checks,8964ordered products,16provisional continuations,eight compatibility projections,5256density and5328stream overlaps,eightH/sigma pairs,72earliernorms and sevenearlierpairs all pass. Actual runtime{o['actual_elapsed_s']}seconds. {description} Source rawSHA{o['source']['sha256']}.\n\nVerdict:CONFIRMED independent finite prefix through72 and source-bound later statistics. Neither fitted statistic is an infinite-radius bound. Evidence183/root{i}.\n")
    p=Path('NOTES_FOR_TEAM.md');p.write_text(f"## {now} | V{v}: four-ninths root{i} independent prefix and finite fits\n\nAll73368Poisson checks and all5256F/5328Gcoefficients through72 pass, includingH72tuned via81. {description} The source beyond72 has not been independently recomputed.\n\n"+p.read_text())
    with Path('WORKLOG.md').open('a') as f:f.write(f"\n{now}: V{v} confirms183root{i} through72 and its finite fit statistics. No infinite-radius inference.\n")
    p=Path('research/INDEX.md');t=p.read_text();t=re.sub(r'^183\..*$',f"183. [Four-ninths numerical audit](183_four_ninths_numerical_audit/PROOF.md): CONFIRMED roots{','.join(map(str,admitted))} through72 and finite source statistics through306; remaining roots{','.join(map(str,pending)) or 'none'}.",t,flags=re.M);p.write_text(t)
    files={}
    for folder in [ROOT/'sources',ROOT/'verification']:
        for p in folder.rglob('*'):
            if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log':
                b=p.read_bytes();files[str(p.relative_to(ROOT))]=dict(bytes=len(b),sha256=sha256(b).hexdigest())
    (ROOT/'verification/MANIFEST.json').write_text(json.dumps(dict(checked_at_utc=now,admitted_roots=admitted,pending_roots=pending,files=files),indent=2)+'\n')
    print(now,f'V{v}',f'root{i}','admitted')
if __name__=='__main__':main()
