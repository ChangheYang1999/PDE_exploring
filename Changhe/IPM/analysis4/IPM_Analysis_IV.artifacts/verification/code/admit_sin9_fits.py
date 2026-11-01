"""Admit independently enclosed finite sin9 statistics and their scope corrections."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
from flint import arb, fmpq, ctx
ctx.prec=1024
root=Path('research/276_single_harmonic_finite_fits')
p=root/'verification/sin9/checks.json';d=json.loads(p.read_text())
assert d['complete'] and d['bits']==2304 and d['N']==301 and d['M']==9
for name in ['prior','harmonics','source']:
 r=d[name];assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
line=[x for x in d['fits'] if x['model']=='n,1']
assert [x['L'] for x in line]==[100,150,200]
assert arb(line[0]['A'])<arb('2.04') and arb(d['endpoint100_to_N']['A'])>arb('2.11')
limit=fmpq(82651586141768218752124086777,415161675019179052311193843662848000)
ratio=arb(d['response']['minimum_response_value'])/arb(limit)
assert 121<ratio and ratio<123
assert arb(line[2]['R_fit'])>arb(line[0]['R_fit'])>arb(line[1]['R_fit'])
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
proof=root/'sources/PROOF_at_V565.md';proof.write_bytes((root/'PROOF.md').read_bytes())
peer=root/'sources/peer_sin9_fit_claim.md';assert 'three decades' in peer.read_text()
result='At unit amplitude, sin(9 theta), delta=4/7, N=301, the least-squares line fits on100..301,150..301,200..301 give A=2.0313238902181093,1.9818205180076986,2.1192376874616403 and radius diagnostics3.4563169282898507,3.3102634642205728,3.7223261224817040. The endpoint base on100..301 is2.1133526715908229 and its radius diagnostic is3.7042557192853549. The three-parameter fit bases are1.7836668125053427,3.1684273333045123,4.7852342780936998, with power exponents24.6579435924635,-103.339564918619,-202.319538945111. The last harmonic root is |H294|^(1/294)=1.9617793061611298. The finite response minimum is sigma42=2.428960189184506e-5.'
correction='The reported A=2.11 on100..301 is the endpoint statistic; the least-squares line base on that window is2.0313. The three displayed line-fit radius diagnostics vary nonmonotonically with the start of the window. Their values are estimates from finite data and do not establish an upper bound for the infinite convergence threshold or its decrease as N grows. The ratio sigma42/sigma_infinity lies in'+ratio.str(40)+' and is about122, so the response is about two decades, not three decades, above its exact positive limit. The varying finite slopes also do not prove an eventual acceleration law. These corrections leave the separately proved single-harmonic convergence theorem unchanged.'
entries=[(565,'Finite sin9 growth fits and response statistics','The finite fitted constants and response values are enclosed by independent interval arithmetic.','Decode the audited dyadic norm intervals at2304 bits, solve interval normal equations for the two specified models with nonzero pivots, and evaluate the exact V544 response limit.',result,'CONFIRMED for these finite interval statistics. No limiting growth constant or sharp radius follows.'),(566,'Sin9 fit attribution and infinite-tail interpretation','The quoted100..301 A=2.11 is a least-squares line fit, and sigma42 is three decades above its limit.','Compare endpoint and least-squares definitions, and divide the enclosed finite response by the exact rational limit.',correction,'REFUTED for the model attribution and three-decade comparison. OPEN for a sharp radius, a one-sided fitted bound or eventual growth acceleration.')]
ledger=Path('VERIFY_REPORT.md');text=ledger.read_text()
for i,title,claim,method,res,verdict in entries:
 assert f'## V{i} |' not in text
 text+=f'\n## V{i} | {now} | {title}\n\n**Claim.** {claim}\n\n**Method.** {method}\n\n**Result.** {res}\n\n**Verdict: {verdict}** Evidence: {p}.\n'
ledger.write_text(text)
def ref(x):return dict(path=str(x),sha256=sha256(x.read_bytes()).hexdigest())
(root/'verification/sin9/admission.json').write_text(json.dumps(dict(at=now,entries=[565,566],evidence=ref(p),proof=ref(proof),peer=ref(peer),exact_limit=str(limit),finite_to_limit_ratio=ratio.str(60),scope='Finite statistics, model attribution and scope correction.'),indent=2)+'\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> TEAM: V565/V566 sin9 fit check and corrections\n\n{result}\n\n{correction}\n\nV563/V564 also admit the coefficient checkpoint through301 and all32 continuum residual pairs. AtR2 the residual decreases20->40 and increases40->80; atR4 it decreases10->20->40->80. Please remove the unsupported upper-bound and decreasing-with-N wording from the final numerical report.\n\n'+notes.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V565/V566 admitted sin9 finite fits and corrected model attribution, finite-to-limit response ratio and unsupported tail interpretation.\n')
with Path('research/INDEX.md').open('a') as f:f.write(f'\nUpdate {now}: topics271/272 admit sin9 finite coefficients and32 continuum residual pairs(V563/V564); topic276 admits sin9 fits and scope corrections(V565/V566).\n')
print(json.dumps(dict(at=now,entries=[565,566],ratio=ratio.str(30))))
