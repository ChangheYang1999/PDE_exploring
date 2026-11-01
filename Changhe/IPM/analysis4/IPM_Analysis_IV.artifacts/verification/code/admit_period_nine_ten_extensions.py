"""Admit finite extension statistics, including their printed discrepancies."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
from flint import arb,ctx
from certificate_admission import stamp,ref,checkref,next_entry
ctx.prec=512
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--cases',required=True);a=ap.parse_args()
base=Path('research/303_period_nine_ten_floating_extensions');labels=a.cases.split(',');rows=[];refs=[]
for label in labels:
    p=base/'verification'/f'{label}.json';d=json.loads(p.read_text());assert d['all_checks_pass']
    checkref(d['source']);checkref(d['baseline']);refs.append(ref(p));rows.append(d)
    assert d['printed_norm_overlap_count']-d['exact_norm_overlap_count']==len(d['norm_differences'])
    assert all(F(v['difference'])==F(v['new'])-F(v['old']) for v in d['norm_differences']+d['tuning_differences'])
    assert d['printed_tuning_overlap_count']-d['exact_tuning_overlap_count']==len({v['k'] for v in d['tuning_differences']})
    for r in d['baseline_fits']+d['extended_fits']:
        assert F(r['squared_rms'])>=0 and arb(r['A'])>0 and arb(r['apparent_radius'])>0
ledger,text=next_entry(a.entry);now=stamp();proof=base/'sources'/f'PROOF_at_V{a.entry}.md';proof.write_bytes((base/'PROOF.md').read_bytes())
norm=sum(d['printed_norm_overlap_count'] for d in rows);norm_equal=sum(d['exact_norm_overlap_count'] for d in rows)
tuning=sum(d['printed_tuning_overlap_count'] for d in rows);tuning_equal=sum(d['exact_tuning_overlap_count'] for d in rows)
fits=sum(len(d['baseline_fits'])+len(d['extended_fits']) for d in rows)
diffs=[dict(Q=d['Q'],root=d['root_index'],**v) for d in rows for v in d['tuning_differences']]
maxdiff=max((abs(F(v['difference'])) for v in diffs),default=F(0))
maxima=[]
for Q in sorted({d['Q'] for d in rows}):
    cand=[(d['root_index'],x) for d in rows if d['Q']==Q for x in d['same_window_changes'] if x['channel']=='density']
    root,x=max(cand,key=lambda p:float(arb(p[1]['absolute_relative_A_change']).mid()))
    for other_root,other in cand:
        if other_root==root and other['window_lower']==x['window_lower']:continue
        assert arb(x['absolute_relative_A_change'])>arb(other['absolute_relative_A_change']), (Q,root,other_root)
    maxima.append(dict(Q=Q,root=root,**x))
result=(f"For {', '.join(labels)}, {norm_equal} of {norm} printed norm overlaps and {tuning_equal} of {tuning} complete tuning rows are identical. "
        f"There are {len(diffs)} differing tuning components, with maximum absolute printed difference {maxdiff}. "
        f"All {fits} finite density/stream fits are recomputed from exact decimal fractions. "+
        ' '.join(f"At Q={r['Q']}, the largest same-window density A change in this batch is {r['absolute_relative_A_change']} at root{r['root']}, lower endpoint{r['window_lower']}." for r in maxima))
scope='CONFIRMED as finite statistics of printed rounded-root floating data. Every discrepancy remains explicit. No high-order coefficient enclosure, asymptotic constant, or true convergence boundary is inferred.'
receipt=base/'verification'/f'admission_V{a.entry}.json';receipt.write_text(json.dumps(dict(at=now,entry=a.entry,all_checks_pass=True,cases=labels,checks=refs,proof=ref(proof),norm_overlap_count=norm,identical_norm_overlap_count=norm_equal,tuning_overlap_count=tuning,identical_tuning_overlap_count=tuning_equal,tuning_differences=diffs,fit_count=fits,maxima=maxima,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V{a.entry} | {now} | Q9/Q10 finite extension statistics\n\n**Claim.** The new completed floating extensions have reproducible finite statistics with all changes quantified.\n\n**Method.** Compare immutable source files and metadata componentwise; solve finite normal equations exactly; enclose exponentials with directed arithmetic.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V{a.entry}, Q9/Q10 finite extension statistics\n\n{result}\n\n{scope} See topic303 for per-window A, apparent radius and every printed discrepancy.\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V{a.entry} admits {len(rows)} Q9/Q10 extension cases and {fits} finite fits with discrepancies retained.'),('VERIFY_SUMMARY.md',f'V{a.entry}: {result} {scope}')]:
    with Path(name).open('a') as f:f.write('\n'+line+'\n')
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V{a.entry}: {result} {scope}\n')
(base/'sources/admit_period_nine_ten_extensions.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
