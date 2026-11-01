"""Check a finite counterexample to a universal printed decay-rate summary."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import json,re

base=Path('research/300_half_ratio_diagnostics')
def ref(p):
    return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def endpoints(text):
    m=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',text)
    assert m,text
    c,r=map(Fraction,m.groups())
    return c-r,c+r

source=base/'verification/checks.json'
d=json.loads(source.read_text())
assert d['all_replays_overlap'] and d['increment_window']==[271,300]
mean=endpoints(d['statistics']['mean_step'])
minimum=endpoints(d['statistics']['minimum_step'])
maximum=endpoints(d['statistics']['maximum_step'])
assert mean[0]>Fraction('-0.69')
assert minimum[0]>Fraction('-0.421')
assert maximum[1]<Fraction('-0.417')
p=Path('../a4-num/FARFIELD_NUMERICAL_EXPERIMENTS.md')
raw=p.read_bytes();lines=raw.decode().splitlines()
i=next(i for i,s in enumerate(lines) if 'smooth law 10^-0.70 per order in every case computed' in s)
assert '1/2 to 300' in lines[i+1]
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
excerpt=base/'sources/decay_rate_claim_V624.json'
excerpt.write_text(json.dumps(dict(at=now,source=str(p),source_sha256=sha256(raw).hexdigest(),first_line=i+1,lines=lines[i:i+3]),indent=2)+'\n')
ledger=Path('VERIFY_REPORT.md');text=ledger.read_text()
assert int(re.findall(r'^## V(\d+) ',text,re.M)[-1])==623
result=(f"For delta=1/2 the mean density log10 increment on271..300 is {d['statistics']['mean_step']}. "
        "All thirty increments lie strictly between-0.421 and-0.417, disjoint from[-0.71,-0.69]. "
        "The common10^-0.70 per-order summary therefore fails for the explicitly included half-exponent run.")
verdict='REFUTED for the universal finite decay-rate description. CONFIRMED for the half-exponent counterexample. Infinite convergence remains OPEN.'
proof=base/'PROOF.md';proof.write_text(proof.read_text()+f'\nCompleted {now}, V624: {result} {verdict}\n')
ps=base/'sources/PROOF_at_V624.md';ps.write_bytes(proof.read_bytes())
r=base/'verification/admission_V624.json'
r.write_text(json.dumps(dict(at=now,entry=624,diagnostics=ref(source),claim=ref(excerpt),proof=ref(ps),mean_interval=[str(v) for v in mean],strict_increment_range=['-0.421','-0.417'],rejected_comparison_range=['-0.71','-0.69'],all_checks_pass=True,verdict=verdict),indent=2)+'\n')
ledger.write_text(text+f'\n## V624 | {now} | Half-exponent decay-rate counterexample\n\n**Claim.** Every listed canonical rational log run follows10^-0.70 per order, including delta=1/2 through300.\n\n**Method.** Apply the exact telescoping identity to V602 interval diagnostics; compare rational interval endpoints. Freeze the affected current clause by source hash.\n\n**Result.** {result}\n\n**Verdict: {verdict}** Evidence: {r}.\n')
note=f'''## {now} VERIFIER -> NUMERICS, LEAD: V624, remaining common-rate overstatement

Experiments Section6 still says "plain norms geometric with the smooth law10^-0.70 per order in every case computed" and includes delta1/2 through300. The checked half-exponent increments271..300 are all between-0.421 and-0.417; mean-0.4187091884615533 (V602). Please remove the universal rate or give the rates by run. The half case can be described by its checked root/ratio diagnostics, without an asymptotic claim. This is a finite summary correction, not a convergence verdict. Topic300 now contains the explicit counterexample and unchanged source evidence. V621 corrections in your23:07 note are acknowledged; I am checking the resulting current files separately.

'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V624 refutes the universal10^-0.70 finite decay-rate clause using the half-exponent interval witness from V602.\n')
(base/'sources/admit_half_decay_scope.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
