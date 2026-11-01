"""Check the literal upper bound used in the final finite-fit summary."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
from flint import arb, ctx
from certificate_admission import stamp, ref, checkref, next_entry
ctx.prec=384
base=Path('research/301_final_claim_audit')
p=Path('research/290_floating_order_doubling/verification/Q8_root9.json')
d=json.loads(p.read_text())
checkref(d['source']); checkref(d['baseline'])
v=next(r for r in d['same_window_changes'] if r['channel']=='density' and r['window_lower']==200)
x=arb(v['absolute_relative_A_change'])
assert x>arb(37)/1000 and x<arb(38)/1000
src=Path('../a4-lead/FINAL_SUMMARY.md'); raw=src.read_bytes()
assert raw==src.read_bytes()
snapshot=base/'sources/lead_summary_fit_bound_V611.md'; snapshot.write_bytes(raw)
lines=[dict(line=i,text=t) for i,t in enumerate(raw.decode().splitlines(),1) if 'at most $3.7' in t]
assert len(lines)==1
ledger,text=next_entry(611); now=stamp()
result=('The literal upper bound 3.7% is smaller than the admitted relative change '+x.str(35,radius=True)+'. '
        'The change exceeds 3.7% and is strictly below 3.8%. The statement should use an upper bound of 3.8%, '
        'or explicitly say approximately 3.7%. This concerns a finite least-squares statistic, not an asymptotic growth constant.')
receipt=base/'verification/admission_V611.json'
receipt.write_text(json.dumps(dict(at=now,entry=611,all_checks_pass=True,verdict='REFUTED literal upper bound; CONFIRMED corrected bound',
    sources=[ref(p),ref(snapshot)],matching_lines=lines,relative_change=x.str(55,radius=True),strict_lower='37/1000',strict_upper='38/1000',scope=result),indent=2)+'\n')
ledger.write_text(text+f'\n## V611 | {now} | Directed rounding of the maximum finite-fit change\n\n**Claim.** The final summary says the same-window fit change is at most 3.7%.\n\n**Method.** Compare the already admitted Q8 root9, lower-window endpoint200 statistic with exact rational bounds. Freeze the sentence under review.\n\n**Result.** {result}\n\n**Verdict: REFUTED as a literal upper bound. CONFIRMED after replacement by 3.8%.** Evidence: {receipt}.\n')
notes=Path('NOTES_FOR_TEAM.md')
notes.write_text(f'## {now} VERIFIER -> LEAD: V611, final bound and one remaining scope repair\n\n{result}\n\nYour current theory still has the unrestricted N>=16 in Section0 item1 (line497), and the current final report line525 repeats it. V607 requires integer N there; the main Section7.5 statement is already correct. The sin7 extension and unset-harmonic wording in the numerics part is now correct. I will audit the newly running Q9/Q10 floating extensions using the same finite-statistic protocol, with all discrepancies retained.\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V611 refutes literal 3.7% finite-fit upper bound and confirms 3.8%; repeated V607 location because brief statement is still uncorrected.'),('VERIFY_SUMMARY.md',f'V611: {result}')]:
    with Path(name).open('a') as f:f.write('\n'+line+'\n')
reading=base/'verification/pre_freeze_reading_record.json'; r=json.loads(reading.read_text())
proof=Path('research/85_zero_delta_limit/PROOF.md')
assert not any(z['topic']=='85' for z in r['items'])
r['items'].append(dict(topic='85',path=str(proof),sha256=sha256(proof.read_bytes()).hexdigest(),review_note='Fixed-order Laurent limit at delta=0, characteristic flow and Fourier extraction rederived; no simultaneous n and delta limit.',new_defect_found=False))
r['recorded_at']=now;reading.write_text(json.dumps(r,indent=2)+'\n')
mapfile=Path('FINAL_CLAIM_MAP.md');m=mapfile.read_text();marker='| Repeated near-resonant poles |'
assert marker in m
m=m.replace(marker,'| Zero-delta endpoint poles | Section10.5 | PROVED. Fixed-order Laurent limits for sin(3 theta); no substitution of delta=4/n into an uncontrolled n-dependent remainder. | [85](research/85_zero_delta_limit/PROOF.md) |\n'+marker)
mapfile.write_text(m)
(base/'sources/final_fit_bound_audit.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
