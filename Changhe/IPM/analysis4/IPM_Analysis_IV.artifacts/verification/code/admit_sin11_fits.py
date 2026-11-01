"""Admit finite interval statistics for the completed sin(11 theta) run."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,gzip,re
from flint import arb,ctx
ctx.prec=1024
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);args=ap.parse_args()
root=Path('research/276_single_harmonic_finite_fits');p=root/'verification/sin11/checks.json';d=json.loads(p.read_text())
assert d['complete'] and (d['M'],d['h'],d['Q'],d['N'],d['bits'])==(11,2,9,306,2304)
for key in ['prior','harmonics','source']:
 r=d[key];assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
prior=json.loads(gzip.decompress(Path(d['prior']['path']).read_bytes()));assert prior['all_checks_pass']
for key in ['source','harmonics','log']:
 r=prior[key];assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
line=[x for x in d['fits'] if x['model']=='n,1'];assert [x['L'] for x in line]==[100,150,200]
roundings=[]
for row,aq,rq in zip(line,['4.965','4.984','4.202'],['36.8','37.1','25.3']):
 for key,q,unit in [('A',aq,'0.001'),('R_fit',rq,'0.1')]:
  assert abs(arb(row[key])-arb(q))<arb(unit)/2
  roundings.append(dict(L=row['L'],key=key,quoted=q,unit=unit))
assert abs(arb(d['endpoint100_to_N']['A'])-arb('4.321'))<arb('0.0005')
assert abs(arb(d['endpoint100_to_N']['R_fit'])-arb('26.9'))<arb('0.05')
harm=json.loads(Path(d['harmonics']['path']).read_text());sig={int(n):arb(v) for n,v in harm['sigma'].items()}
assert all(sig[9*k]<0 for k in range(14,34))
assert all(abs(sig[9*(k+1)])<abs(sig[9*k]) for k in range(14,33))
assert d['response']['minimum_response_index']==33 and d['response']['last_harmonic_order']==297
ledger=Path('VERIFY_REPORT.md');s=ledger.read_text();assert max(map(int,re.findall(r'^## V(\d+) \|',s,re.M)))==args.entry-1
now=datetime.now(timezone.utc).isoformat(timespec='seconds');tag=f'V{args.entry}'
def ref(x):return dict(path=str(x),sha256=sha256(x.read_bytes()).hexdigest())
proof=root/'sources'/f'PROOF_at_{tag}.md';proof.write_bytes((root/'PROOF.md').read_bytes())
peer=Path('../a4-num/NOTES_FOR_TEAM.md').read_text();start=peer.index('## 2026-10-31T20:40Z');end=peer.find('\n## ',start+4);peerpath=root/'sources/peer_sin11_fit_claim.md';peerpath.write_text(peer[start:end])
result=('At unit amplitude, sin(11 theta), delta=4/9 and N=306, the least-squares line bases on100..306,150..306,200..306 are4.9651550669,4.9838545182,4.2024396403; their radius diagnostics are36.8000863000,37.1126573690,25.2858955630. The endpoint100..306 base is4.3210240103 with diagnostic26.9196884247. The line-fit RMS residuals in log10 norm are3.3355828585,2.8438130787,1.2027845374. The three-parameter bases are5.0788858878,1.1875832477,1.6041393741, with power exponents-4.3421725831,319.0418138385,241.4572925073. The last harmonic root is|H297|^(1/297)=3.4250655682. Responses at k14..33 are negative with strictly decreasing moduli; the smallest stored modulus is0.000184584868537565 at k33. All eight quoted line/endpoint rounding bins pass. Arithmetic took'+str(d['actual_elapsed_s'])+'seconds.')
verdict='CONFIRMED for finite interval statistics under the coefficient-enclosure hypotheses of topic271. The fitted values are neither upper nor lower bounds for the infinite convergence threshold, and the changing fit windows establish no asymptotic law.'
receipt=dict(at=now,entry=tag,evidence=ref(p),proof=ref(proof),peer=ref(peerpath),roundings=roundings,scope=verdict)
assert not (p.parent/'admission.json').exists();(p.parent/'admission.json').write_text(json.dumps(receipt,indent=2)+'\n')
ledger.write_text(s+f'\n## {tag} | {now} | Finite sin11 growth fits and response statistics\n\n**Claim.** The quoted sin11 fit and response statistics agree with independent interval calculations.\n\n**Method.** Decode audited dyadic norms at2304 bits, solve the two specified normal-equation systems with nonzero pivots, check quoted rounding bins, and compare successive response intervals.\n\n**Result.** {result}\n\n**Verdict: {verdict}** Evidence: {p}.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> TEAM: {tag}, sin11 finite statistics confirmed\n\n{result}\n\n{verdict} The finite coefficient audit has also passed; its combined ledger admission with the continuum residual calculation is pending that queued calculation.\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: {tag} admitted sin11 finite fits and all quoted rounding bins.'),('research/INDEX.md',f'Update {now}: topic276 sin11 finite statistics admitted in{tag}.'),('VERIFY_SUMMARY.md',f'{tag}: sin11 unit-amplitude delta4/9,N306 line bases4.9652,4.9839,4.2024 and diagnostics36.8,37.1,25.3; endpointbase4.3210,diagnostic26.9. Finite statistics only.')]:
 with Path(name).open('a') as f:f.write('\n'+line+'\n')
print(json.dumps(dict(at=now,entry=tag)))
