"""Admit the final printed-fit ranking counterexample and correct scope."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from flint import arb,ctx
import json,re
ctx.prec=768
base=Path('research/305_final_conditional_fit_scope')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
checks=base/'verification/printed_fit_checks.json';d=json.loads(checks.read_text());assert d['all_checks_pass']
assert arb(d['fits']['power']['rms'])<arb(d['fits']['exponential']['rms'])
np=Path('research/266_later_conditional_continuations/N440/verification/checks.json');x=json.loads(np.read_text());assert x['all_checks_pass']
rows={r['n']:r for r in x['rows']}
log=lambda n:arb(rows[n]['fields']['f']['log10_norm'])
a=log(354)-log(353);b=log(438)-log(437);mean=(b-a)/28
assert mean>0
final=rows[440]['fields']['f']
now=datetime.now(timezone.utc).isoformat(timespec='seconds');entry=621
ledger=Path('VERIFY_REPORT.md');text=ledger.read_text();assert int(re.findall(r'^## V(\d+) ',text,re.M)[-1])==entry-1
snapshots=[]
for label,p in [('experiments',Path('../a4-num/FARFIELD_NUMERICAL_EXPERIMENTS.md')),('summary',Path('../a4-num/NUM_REPORT.md')),('notes',Path('../a4-num/NOTES_FOR_TEAM.md'))]:
 raw=p.read_bytes();lines=raw.decode().splitlines();matches=[dict(line=i,text=line) for i,line in enumerate(lines,1) if any(t in line for t in ['smallest residual','residual on every window','0.0013','96..102'])]
 q=base/'sources'/f'{label}_claim_excerpt.json';q.write_text(json.dumps(dict(at=now,source=str(p),source_sha256=sha256(raw).hexdigest(),matches=matches),indent=2)+'\n');snapshots.append(ref(q))
result=(f"On the seven printed multipliers at420..438, the power RMS is {d['fits']['power']['rms']}, while the exponential RMS is {d['fits']['exponential']['rms']}; power is strictly smaller. "
        f"The signed class-zero increment rises from {a.str(30)} at354 to {b.str(30)} at438; mean increase per period is {mean.str(30)}. "
        f"At440 the single density factorial-hump maximum is {final['factorial_log10_ratio']} at column{final['factorial_maximizer']}; the range4.4..5.1 and columns96..102 describes the last ten orders.")
verdict='REFUTED for the universal exponential-fit ranking on the stated printed data. CONFIRMED for the explicit finite correction; OPEN for infinite growth and canonical uncertainty after the reset.'
proof=base/'PROOF.md';s=proof.read_text().replace('Status: verification protocol and argument written before the arithmetic check. The finite numerical verdict is recorded below when the directed calculation completes.',f'Status: finite counterexample confirmed {now}; the universal ranking claim is refuted.')
s+='\n## Completed check, V621\n\n'+result+'\n\n'+verdict+'\n';proof.write_text(s)
ps=base/'sources/PROOF_at_V621.md';ps.write_text(s)
r=base/'verification/admission_V621.json';r.write_text(json.dumps(dict(at=now,entry=entry,checks=ref(checks),norm_source=ref(np),proof=ref(ps),source_excerpts=snapshots,class_zero_signed_increment_at354=a.str(40),class_zero_signed_increment_at438=b.str(40),mean_change_per_period=mean.str(40),final_hump=final['factorial_log10_ratio'],final_hump_column=final['factorial_maximizer'],verdict=verdict),indent=2)+'\n')
ledger.write_text(text+f'\n## V621 | {now} | Final conditional-fit scope counterexample\n\n**Claim.** The final exponential fit has the smallest residual on every printed-data window.\n\n**Method.** Recompute the seven-point least-squares normal equations with768-bit directed arithmetic on exact decimal inputs. Check the signed-increment and final-hump wording against the independent440 norm record.\n\n**Result.** {result}\n\n**Verdict: {verdict}** Evidence: {r}.\n')
note=f'''## {now} VERIFIER -> NUMERICS, LEAD: V621 correction to new final numerics text

The sentence "exponential model has the smallest residual on every window" is false for the stated printed-data fits at420..438. Independent exact-decimal regression gives power RMS4.2738994994e-5 versus exponential4.3527186333e-5 (your table already rounds these to4.3e-5 and4.4e-5). Please say the exponential fit is best on the longer tested windows, while power is marginally better on the final seven-point window. This changes no tail conclusion; no model is selected. Locations: experiments5.11b(b5) and6, NUM_REPORT7b, latest notes.

Also, the signed class-zero increment from354 to438 increases by about0.00164 per period; the negative sign describes the decreasing magnitude. The current -0.0013 sentence in experiments5.11b(b3) has the wrong sign/rate for those endpoints. The hump range4.4..5.1 at columns96..102 belongs to431..440; at440 alone it is4.79626058549 at102. Please identify the range explicitly. The exact checks are in topic305. Order440 arithmetic and monitor audits have passed and will be admitted next.

'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V621 refutes the new every-window exponential-fit ranking; records signed increment and single-order hump corrections. Topic305.\n')
with Path('research/INDEX.md').open('a') as f:f.write('\n305. [Final conditional-fit scope](305_final_conditional_fit_scope/PROOF.md): exact printed-data counterexample to the universal ranking, plus signed increment and final-order scope.\n')
(base/'sources/admit_final_conditional_fit_scope.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
