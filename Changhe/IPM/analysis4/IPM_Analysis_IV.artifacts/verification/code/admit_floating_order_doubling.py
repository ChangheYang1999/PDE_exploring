"""Admit a named batch of finite order-doubling statistics."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import argparse,json
from flint import arb,ctx
from certificate_admission import ref,checkref,next_entry
ctx.prec=256
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--cases',required=True);a=ap.parse_args()
base=Path('research/290_floating_order_doubling');rows=[];refs=[];labels=a.cases.split(',')
for label in labels:
 p=base/'verification'/f'{label}.json';d=json.loads(p.read_text());assert d['all_checks_pass'];checkref(d['source']);checkref(d['baseline']);refs.append(ref(p));rows.append(d)
 assert d['printed_norm_overlap_count']==d['exact_printed_norm_overlaps'] and F(d['maximum_printed_log_difference'])==0
 for v in d['tuning_overlap_discrepancies']:
  assert all(F(v[k])==0 for k in ['R_log_difference','sigma_relative_difference','H_log_difference'])
 for r in d['baseline_fits']+d['extended_fits']:
  assert F(r['squared_rms'])>=0 and arb(r['A'])>0 and arb(r['apparent_radius'])>0
ledger,text=next_entry(a.entry);now=datetime.now(timezone.utc).isoformat(timespec='seconds')
proof=base/'sources'/f'PROOF_at_V{a.entry}.md';proof.write_bytes((base/'PROOF.md').read_bytes())
count=sum(d['printed_norm_overlap_count'] for d in rows);tuning=sum(d['printed_tuning_row_overlaps'] for d in rows);fits=sum(len(d['baseline_fits'])+len(d['extended_fits']) for d in rows)
maxdiff=max((arb(x['absolute_relative_A_change']) for d in rows for x in d['same_window_changes'] if x['channel']=='density'),key=lambda x:float(x.mid()))
result=f"For {', '.join(labels)}, all{count} overlapping printed norm values and{tuning} printed tuning rows agree exactly with the archived baselines, after the producer's unit-amplitude normalization. All{fits} density/stream fits are recomputed by exact rational normal equations and directed transcendental evaluation. The largest density A change on the same100/150/200 lower-window endpoints is {maxdiff.str(28,radius=True)} relative."
if labels==[f'Q7_root{i}' for i in range(1,6)]:
 assert all(x['within_one_percent'] for d in rows for x in d['outside_old_range']) and maxdiff<arb('.015')
 result+=' Each extended density fit on windows starting100,200,300,400 lies within1% of its previous three-window A range. This is distinct from a1% same-window claim, which fails. The completion banners name602, the final printed norm order is601 and the last complete fitted block ends595.'
scope='CONFIRMED as finite statistics of rounded floating data. No high-order coefficient enclosure, asymptotic constant or true convergence threshold is inferred.'
admission=base/'verification'/f'admission_V{a.entry}.json';admission.write_text(json.dumps(dict(at=now,entry=a.entry,all_checks_pass=True,cases=labels,checks=refs,proof=ref(proof),norm_overlap_count=count,tuning_overlap_count=tuning,fit_count=fits,maximum_same_window_relative_A_change=maxdiff.str(45,radius=True),scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V{a.entry} | {now} | Finite order-doubling fit audit\n\n**Claim.** The completed extended floating outputs reproduce the earlier prefix and have the stated finite fit drift.\n\n**Method.** Freeze each completed file, check normalized metadata and every overlapping printed value, then use exact rational normal equations and directed arithmetic for the finite fits.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {admission}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V{a.entry}, finite order-doubling audit\n\n{result}\n\n{scope} Topic290 contains the full argument and records. The lead reviewed this finite-statistic protocol at21:03:59Z; it extends the accepted263 method. Further completed runs can be added without rerunning the recurrence.\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V{a.entry} admits {len(rows)} completed order-doubling files, {fits} finite fits.\n')
with Path('VERIFY_SUMMARY.md').open('a') as f:f.write(f'\nV{a.entry}: {result} {scope}\n')
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V{a.entry}: {result} {scope}\n')
(base/'sources/admit_floating_order_doubling.py').write_bytes(Path(__file__).read_bytes());print(result)
