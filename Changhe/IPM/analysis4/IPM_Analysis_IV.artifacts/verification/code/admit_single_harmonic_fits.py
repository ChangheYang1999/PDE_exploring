"""Admit finite single-harmonic fit enclosures and preserve rounding findings."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
root=Path('research/276_single_harmonic_finite_fits')
p=root/'verification/sin7/checks.json';d=json.loads(p.read_text())
assert d['complete'] and d['bits']==2304 and d['N']==300
assert [x['claim'] for x in d['printed_rounding_checks'] if not x['matches_rounding']]==['endpoint A on100..N']
for key in ['prior','harmonics','source']:
 v=d[key];assert sha256(Path(v['path']).read_bytes()).hexdigest()==v['sha256']
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
proof=root/'sources/PROOF_at_V560.md';proof.write_bytes((root/'PROOF.md').read_bytes())
peer=Path('../a4-num/NOTES_FOR_TEAM.md').read_text();start=peer.index('## 2026-10-31T19:49Z');end=peer.find('\n## ',start+1)
(root/'sources/peer_sin7_fit_claim.md').write_text(peer[start:end if end>=0 else None])
result='At unit amplitude, delta=4/5, N=300, the line fits on100..300,150..300,200..300 give A=0.5702545450301333,0.5703274806547007,0.5692391734460261 and radius diagnostics0.4955482470541255,0.4956274741708521,0.4944455518331242. The three-parameter fits on the same windows give A=0.5634513261490833,0.5893764865847989,0.6527989788736893, with power exponents2.271193432155037,-7.221274783875922,-33.96010386538003. The last H295 root is0.5534959495760131; the finite response minimum is at k59, sigma=-7.673234043937715e-6, with decreasing modulus fromk6 through59.'
correction='The100..300 endpoint base is0.5733992421918456, which rounds to0.573 at three decimals, not the reported0.574. Its radius diagnostic is0.4989665054036415. The straight-line fits give radius diagnostics about0.4944..0.4956; the value0.5164056757302152 comes from the150..300 three-parameter fit. The displayed0.50..0.52 range therefore mixes different statistics and is not the range of the stated line and endpoint fits. These corrections do not affect the separately proved convergence theorem.'
entries=[(560,'Finite sin7 growth fits and response statistics','The finite fitted constants and response trend agree with independent interval arithmetic.','Decode audited2048-bit norm intervals exactly at2304 bits; form two-column and three-column normal equations on inclusive integer windows; prove all pivots exclude zero; evaluate directed logarithms, residuals and powers.',result,'CONFIRMED for the recorded finite interval statistics. No asymptotic law or sharp convergence radius follows.'),(561,'Sin7 endpoint rounding and fit-model attribution','The stated0.574 endpoint constant and0.50..0.52 straight-line radius range have the stated numerical meanings.','Compare the entire computed interval with the stated rounding bin and distinguish each fitted model.',correction,'REFUTED as stated; corrected finite statistics are inV560 and the accompanying receipt.')]
ledger=Path('VERIFY_REPORT.md');s=ledger.read_text()
for i,title,claim,method,res,verdict in entries:
 assert f'## V{i} |' not in s
 s+=f'\n## V{i} | {now} | {title}\n\n**Claim.** {claim}\n\n**Method.** {method}\n\n**Result.** {res}\n\n**Verdict: {verdict}** Evidence: {p}.\n'
ledger.write_text(s)
def ref(q):return dict(path=str(q),sha256=sha256(q.read_bytes()).hexdigest())
(root/'verification/sin7/admission.json').write_text(json.dumps(dict(at=now,entries=[560,561],evidence=ref(p),proof=ref(proof),peer=ref(root/'sources/peer_sin7_fit_claim.md'),scope='Finite statistics and correction only.'),indent=2)+'\n')
lead=Path('../a4-lead/NOTES_FOR_TEAM.md').read_text().split('\n## ',1)[0]
for name in ['271_single_harmonic_finite_audit','272_single_harmonic_residuals']:
 q=Path('research')/name/'sources/lead_review_200450Z.md';q.write_text(lead+'\n')
 q.with_name('lead_review_200450Z.json').write_text(json.dumps(dict(recorded_at=now,review=ref(q),finding='Lead independently reviewed the four branch protocols and found no objection; preserves exact compatibility hypotheses.'),indent=2)+'\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> TEAM: V560/V561 sin7 finite fits; two corrections\n\n{result}\n\n{correction}\n\nThe initial parser and precision-loading errors are preserved as verifier errors; the completed receipt is276/verification/sin7/checks.json. Your20:04:50Z protocol review is preserved in271/272. T9(d) was already admittedV557 at20:01:04Z; its exact statement and all ten downward-rounded constants are in274.\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V560/V561 admitted sin7 finite fits and corrected endpoint rounding/model attribution. Preserved lead271/272 protocol review. Parser initially failed on insufficient exact dyadic loading precision;2304-bit rerun completed in{d["actual_elapsed_s"]}s.\n')
print(now)
