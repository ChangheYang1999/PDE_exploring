"""Admit the final finite file while preserving its nonzero printed discrepancy."""
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
import json
from certificate_admission import stamp,ref,checkref,next_entry
ctx.prec=512
base=Path('research/290_floating_order_doubling');p=base/'verification/Q8_root10.json';d=json.loads(p.read_text())
assert d['all_checks_pass'] and d['last_printed_order']==599 and d['last_complete_block']==592
checkref(d['source']);checkref(d['baseline'])
assert d['printed_norm_overlap_count']==d['exact_printed_norm_overlaps']==606 and F(d['maximum_printed_log_difference'])==0
nonexact=[]
for v in d['tuning_overlap_discrepancies']:
 assert F(v['R_log_difference'])==F(v['sigma_relative_difference'])==0
 if F(v['H_log_difference'])!=0:nonexact.append(v)
assert len(nonexact)==1 and nonexact[0]['k']==18 and F(nonexact[0]['H_log_difference'])==F(1,10**12)
assert d['printed_tuning_row_overlaps']==36
for r in d['baseline_fits']+d['extended_fits']:
 assert F(r['squared_rms'])>=0 and arb(r['A'])>0 and arb(r['apparent_radius'])>0
allrows=[]
for Q in [7,8]:
 for i in range(1,11):
  q=base/'verification'/f'Q{Q}_root{i}.json';e=json.loads(q.read_text());checkref(e['source']);checkref(e['baseline']);allrows.append((q,e))
maxima=[]
for Q in [7,8]:
 candidates=[(e['root_index'],x['window_lower'],arb(x['absolute_relative_A_change'])) for _,e in allrows if e['Q']==Q for x in e['same_window_changes'] if x['channel']=='density']
 root,lo,value=max(candidates,key=lambda x:float(x[2].mid()));maxima.append(dict(Q=Q,root=root,window_lower=lo,relative_A_change=value.str(40,radius=True)))
count=sum(e['printed_norm_overlap_count'] for _,e in allrows);tuning=sum(e['printed_tuning_row_overlaps'] for _,e in allrows);fits=sum(len(e['baseline_fits'])+len(e['extended_fits']) for _,e in allrows)
assert count==12060 and tuning==770 and fits==360
ledger,text=next_entry(610);now=stamp();proof=base/'sources/PROOF_at_V610.md';proof.write_bytes((base/'PROOF.md').read_bytes())
result='Q8 root10 has606 identical printed norm values and35 completely identical tuning rows. At k18 the sole different component is log10|H|:134.824726365054 in the order304 baseline and134.824726365053 in the order600 extension, an exact printed difference10^-12; R and sigma still agree. The baseline amplitude is1 and the extension amplitude1/8. All18 fits are recomputed from the printed norm data. Across all20 Q7/Q8 extensions,12060 norm overlaps are identical,769 of770 tuning rows are identical, and360 finite fits have been recomputed. '
result+='Maximum same-lower-window density A drifts are '+', '.join(f'Q{r["Q"]}: root{r["root"]}, lower endpoint{r["window_lower"]}, relative {r["relative_A_change"]}' for r in maxima)+'.'
scope='Finite fit and overlap audit CONFIRMED with the explicit exception. Exact equality of every printed tuning entry is REFUTED. No coefficient enclosure, error bound for the true root, or asymptotic convergence threshold follows.'
receipt=base/'verification/admission_V610.json';receipt.write_text(json.dumps(dict(at=now,entry=610,all_checks_pass=True,checks=ref(p),proof=ref(proof),nonexact_tuning_entries=nonexact,all_case_checks=[ref(q) for q,e in allrows],total_norm_overlaps=count,total_tuning_rows=tuning,total_fits=fits,maximum_same_window_drifts=maxima,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V610 | {now} | Final floating overlap and fit audit, with one printed discrepancy\n\n**Claim.** Q8 root10 reproduces the earlier finite statistics, with any printed discrepancies identified explicitly.\n\n**Method.** Compare exact decimal strings as fractions, verify every unchanged source hash, and use the existing exact normal-equation fit audit. The attempted all-equal batch admission failed before writing any ledger entry; its failure is retained here.\n\n**Result.** {result}\n\n**Verdict.** {scope} Evidence: {receipt}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> LEAD: V609/V610 complete all20 doubled-order floating files\n\n{result}\n\n{scope} Please say identical norm overlaps; the tuning overlaps have the single last-decimal exception above. The V609 batch covers Q8roots5..9.\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V609/V610 close all20 floating extensions; one10^-12 printed harmonic-log difference is explicitly retained, not rounded away.'),('VERIFY_SUMMARY.md',f'V610: {result} {scope}')]:
 with Path(name).open('a') as f:f.write('\n'+line+'\n')
with (base/'PROOF.md').open('a') as f:f.write(f'\nCompleted {now}, V610: {result} {scope}\n')
(base/'sources/admit_floating_rounding_exception.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
