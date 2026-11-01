"""Audit published percentage bounds against admitted finite fit statistics."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from certificate_admission import stamp,ref,checkref,next_entry
ctx.prec=768
base=Path('research/301_final_claim_audit'); rows=[];checks=[]
for Q in [7,8]:
    for i in range(1,11):
        p=Path('research/290_floating_order_doubling/verification')/f'Q{Q}_root{i}.json'
        d=json.loads(p.read_text());assert d['all_checks_pass'];checkref(d['source']);checkref(d['baseline'])
        checks.append(ref(p))
        for x in d['same_window_changes']:
            if x['channel']=='density':rows.append(dict(Q=Q,root=i,**x))
results=[]
for label,Q,maxroot,bound in [('Q7 first eight roots',7,8,F(15,1000)),('Q7 all ten roots',7,10,F(32,1000)),('Q8 all ten roots',8,10,F(38,1000))]:
    group=[r for r in rows if r['Q']==Q and r['root']<=maxroot]
    m=max(group,key=lambda r:float(arb(r['absolute_relative_A_change']).mid()))
    val=arb(m['absolute_relative_A_change'])
    for other in group:
        if other is not m:assert val>arb(other['absolute_relative_A_change'])
    assert val<arb(bound.numerator)/bound.denominator
    out=dict(label=label,root=m['root'],window_lower=m['window_lower'],maximum=m['absolute_relative_A_change'],strict_bound=str(bound),strict_comparisons=len(group)-1)
    if Q==8:
        radius_bound=(1+val)**4-1;assert radius_bound<arb(16)/100
        out['absolute_radius_change_upper_bound']=radius_bound.str(45,radius=True)
        out['strict_radius_bound']='4/25'
    results.append(out)
ledger,text=next_entry(615);now=stamp()
result=('For Q7 roots1..8 the maximum absolute same-window density A change is '+results[0]['maximum']+', strictly below1.5%. '
        'For all ten Q7 roots it is '+results[1]['maximum']+', strictly below3.2%. '
        'For all ten Q8 roots it is '+results[2]['maximum']+', strictly below3.8%. '
        'The corresponding Q8 absolute apparent-radius change is bounded above by '+results[2]['absolute_radius_change_upper_bound']+', strictly below16%. All maxima were ordered by strict directed comparisons.')
scope='CONFIRMED for the admitted finite floating-fit datasets only. These bounds compare fitted diagnostics, not true radii or asymptotic constants.'
with (base/'PROOF.md').open('a') as f:f.write('\n## Published finite percentage bounds, V615\n\nFor each specified finite set, strict interval comparisons select its largest absolute fitted A change. Compare that enclosure with the exact fractions15/1000,32/1000 and38/1000. If the signed relative A change is x with |x|<=m<1, the period-eight radius diagnostic changes by (1+x)^4-1; monotonicity and the binomial expansion give absolute change at most(1+m)^4-1. Its directed upper bound is below4/25. This argument concerns only the exact finite fits to printed data.\n')
proof=base/'sources/PROOF_at_V615.md';proof.write_bytes((base/'PROOF.md').read_bytes())
receipt=base/'verification/admission_V615.json';receipt.write_text(json.dumps(dict(at=now,entry=615,all_checks_pass=True,checks=checks,proof=ref(proof),results=results,result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V615 | {now} | Final finite percentage bounds\n\n**Claim.** The published Q7 and Q8 finite-fit percentage bounds round outward correctly.\n\n**Method.** Strict directed comparisons of every candidate maximum, exact rational percentage thresholds, and the fourth-power conversion to the Q8 apparent physical radius.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: V615 confirms finite percentage bounds\n\n{result}\n\n{scope}\n\n'+p.read_text())
for file,line in [('WORKLOG.md',f'{now}: V615 confirms Q7 1.5%/3.2%, Q8 3.8% and Q8 radius16% finite bounds.'),('VERIFY_SUMMARY.md',f'V615: {result} {scope}')]:
    with Path(file).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/admit_final_floating_bounds.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
