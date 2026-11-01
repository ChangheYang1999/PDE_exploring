"""Admit finite printed-versus-unrounded class-zero regressions."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,re
from flint import arb,ctx
ctx.prec=768
base=Path('research/305_final_conditional_fit_scope')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
p=base/'verification/all_window_fit_checks.json';d=json.loads(p.read_text())
assert d['all_checks_pass'] and d['all_precision_replays_overlap']
assert len(d['coefficient_rounding_checks'])==31 and len(d['printed_statistic_rounding_checks'])==49
for r in d['windows']:
 assert r['unrounded']['strict_rms_ranking']==['exponential','power','inverse_order']
 assert r['printed']['strict_rms_ranking']==(['power','exponential','inverse_order'] if r['window'][0]==420 else ['exponential','power','inverse_order'])
for r in d['printed_sources']+[d['unrounded_source'],d['printed_table']]:assert ref(Path(r['path']))['sha256']==r['sha256']
last=d['windows'][-1]['unrounded']['fits']
assert arb(last['exponential']['rms'])<arb(last['power']['rms'])
ledger=Path('VERIFY_REPORT.md');text=ledger.read_text();assert int(re.findall(r'^## V(\d+) ',text,re.M)[-1])==625
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
result=(f"All31 printed class-zero multipliers on348..438 fall within their rounding bins for the independently audited unrounded values. All49 printed regression statistics on the seven windows reproduce within their stated rounding bins. "
        f"There are42 distinct regressions, replayed at768 and1536 bits. The printed-data ranking is exponential, power, inverse-order on the first six windows and power, exponential, inverse-order on420..438. "
        f"For unrounded data, the ranking is exponential, power, inverse-order on all seven windows. On420..438 the unrounded exponential RMS is {last['exponential']['rms']} and the power RMS is {last['power']['rms']}. "
        "Thus rounding changes the last-window ranking; the earlier counterexample applies precisely to the stated printed-data table.")
scope='CONFIRMED as finite regressions of the specified conditional-on329 continuation. This is a matched class-zero comparison, distinct from fitting every order in V622. No infinite tail model is selected.'
proof=base/'PROOF.md';proof.write_text(proof.read_text()+f'\n## Complete replay, V626\n\nCompleted {now}. {result}\n\n{scope}\n')
ps=base/'sources/PROOF_at_V626.md';ps.write_bytes(proof.read_bytes())
r=base/'verification/admission_V626.json';r.write_text(json.dumps(dict(at=now,entry=626,all_checks_pass=True,checks=ref(p),proof=ref(ps),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V626 | {now} | All final class-zero fits and rounding reversal\n\n**Claim.** All seven printed fit windows reproduce, and the effect of rounding is explicitly quantified.\n\n**Method.** Freeze the printed cycle diagnostics; compare all31 bins against V622 inputs; solve42 regressions at768 and1536 bits with two residual identities; check49 printed statistic bins.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {r}.\n')
note=f'''## {now} VERIFIER -> LEAD, NUMERICS: V626, complete fit replay and precise rounding reversal

All seven final printed-data windows reproduce (49 statistic bins), and all31 class-zero multipliers348..438 agree with the corresponding unrounded coefficient-derived values within the printed bins. I also fitted the identical class-zero windows using those unrounded values. On420..438, unrounded exponential RMS1.10211e-5 < power3.21563e-5, whereas printed power4.27390e-5 < exponential4.35272e-5. The unrounded exponential model has the least residual on all seven windows. This confirms a rounding-induced reversal, not an asymptotic selection. Topic305 contains42 distinct fits at two precisions.

The existing table explicitly uses printed multipliers, so V621's correction remains necessary there. A separately labeled unrounded-data comparison can state the additional ranking. The lead theory14.16 final440 sentence also still says the linear model has the smallest residual without distinguishing inputs; please keep it consistent with the printed numbers or explicitly identify the unrounded comparison. V622's all-order vector regressions use a different sampling set; do not substitute their parameters for class-zero fits.

'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V626 confirms all seven final printed fit windows and exhibits a last-window ranking reversal for matched unrounded data;42 fits,49 printed bins,31 coefficient bins.\n')
(base/'sources/admit_final_window_fit_replay.py').write_bytes(Path(__file__).read_bytes())
print(now,scope)
