"""Check a finite counterexample to norm-independent velocity minimization."""
from pathlib import Path
from fractions import Fraction as F
import json,time
from certificate_admission import stamp,ref,next_entry
start=time.monotonic();base=Path('research/304_velocity_norm_scope');P=F(3,2)
def inverse(a):
    return {j:-a.get(j-1,F(0))/(2*(2*j+P))+a.get(j,F(0))/(2*(2*j-P)) for j in [1,2]}
c=inverse({0:F(1),1:F(1,7)});s=inverse({0:F(1)})
assert c=={1:0,2:F(-1,77)} and s=={1:F(-1,7),2:0}
def norm(b,exp_sigma):return sum((2*j+P)*exp_sigma**(2*j)*abs(v) for j,v in b.items())
values={name:{str(e):str(norm(b,F(e))) for e in [1,4]} for name,b in [('cancellation',c),('single',s)]}
assert norm(c,F(1))==F(1,14)<norm(s,F(1))==F(1,2)
assert norm(c,F(4))==F(128,7)>norm(s,F(4))==8
src=Path('research/301_final_claim_audit/sources/summary_at_V613.md')
lines=src.read_text().splitlines();chosen=[dict(line=i,text=t) for i,t in enumerate(lines,1) if 'uniquely minimizes the leading velocity norm' in t]
assert len(chosen)==1
now=stamp();out=base/'verification/checks.json';out.write_text(json.dumps(dict(at=now,all_checks_pass=True,source=ref(src),paragraph=chosen,values=values,actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
ledger,text=next_entry(616)
result='At gamma=1/2 and bandwidth3 the cancellation polynomial sin(theta)+(1/7)sin(3theta) has V_0=1/14, versus1/2 for sin(theta). At sigma=log4 these norms become128/7 and8, so the cancellation polynomial is no longer minimizing. The theory already specifies the correct norm; the summary should name the combined unweighted Wiener norm of the leading polar velocity components.'
scope='CONFIRMED for the unweighted polar norm in Proposition8.4. A norm-independent interpretation is REFUTED by the exact example. The currently unspecified summary phrase requires clarification, not a change to the theorem.'
receipt=base/'verification/admission_V616.json';receipt.write_text(json.dumps(dict(at=now,entry=616,all_checks_pass=True,checks=ref(out),proof=ref(base/'PROOF.md'),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V616 | {now} | Norm of the leading-velocity minimizer\n\n**Claim.** The summary\'s shear-approximation family minimizes the leading velocity norm.\n\n**Method.** Compare with the explicitly defined V_sigma in Proposition8.4; compute both polar velocity norms of two degree-at-most3 profiles by exact rational Poisson inversion.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: V616, one norm clarification in the summary\n\n{result}\n\nSuggested replacement in Section4 Shape: "uniquely minimizes the combined unweighted Wiener norm of the leading polar velocity components". The theory\'s Proposition8.4 is already correct. This distinguishes the proved variational statement from other analytic norms and from full-series growth.\n\n'+p.read_text())
for file,line in [('WORKLOG.md',f'{now}: V616 verifies the unweighted norm scope and an exact positive-strip counterexample.'),('VERIFY_SUMMARY.md',f'V616: {result} {scope}')]:
    with Path(file).open('a') as f:f.write('\n'+line+'\n')
(base/'sources/velocity_norm_scope.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
