"""Admit exact global Q9 response infima after independent proof review."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json
from flint import arb,ctx
ctx.prec=1536
root=Path('research/278_period_nine_response_infima');p=root/'verification/checks.json.gz'
d=json.loads(gzip.decompress(p.read_bytes()));assert d['all_checks_pass'] and d['bits']==1024
for item in d['inputs']:assert sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256']
assert [r['candidate_index'] for r in d['rows']]==[8,7,4,7,None,None,9,9,8,8]
positive=zero=finite=equality=extra=0
for row in d['rows']:
 assert row['K']==19 and arb(row['infimum'])>0
 for c in row['tail_coefficients']:
  if c['exact_zero']:assert c['degree']==89 and row['candidate_index'] is None and arb(c['enclosure']).is_zero();zero+=1
  else:assert arb(c['enclosure'])>0;positive+=1
 for r in row['finite_checks']:
  if r['candidate']:assert arb(r['gap']).is_zero() and r['k']==row['candidate_index'];equality+=1
  else:assert arb(r['gap'])>0;finite+=1
 extra+=row['finite2000_comparisons']
 if row['candidate_index'] is None:assert row['finite2000_comparisons']==1998 and arb(row['finite2000_smallest_gap'])>0
assert (positive,zero,finite,equality,extra)==(898,2,162,8,3996)
peer=Path('../a4-lead/NOTES_FOR_TEAM.md').read_text();start=peer.index('## 2026-10-31T20:26:02Z');end=peer.find('\n## ',start+3)
review=peer[start:end if end!=-1 else None];assert 'both ACCEPTED' in review
rp=root/'sources/lead_review_20261031T202602Z.md';rp.write_text(review+'\n')
# The same review explicitly covers the Q9 prefix specialization.
Path('research/280_period_nine_prefixes/sources/lead_review_20261031T202602Z.md').write_text(review+'\n')
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
proof=root/'PROOF.md';(root/'sources/PROOF_before_V569.md').write_bytes(proof.read_bytes())
s=proof.read_text().replace('Status: proof and verification protocol written before computation. The conclusions require all listed inequalities to pass. No floating-point sample establishes a global infimum.',f'Status: PROVED, independently reviewed and admitted in V569 on {now}. The proof preceded computation and every required inequality passed. No floating-point sample establishes a global infimum.')
s=s.replace('The proposed exact conclusion is','The exact conclusion is');proof.write_text(s)
result='For delta=2/9 and the ten ordered algebraic compatibility roots, the global response modulus has unique minimizing indices 8,7,4,7 at roots1-4 and9,9,8,8 at roots7-10. At roots5 and6 its positive infimum is the limiting modulus and is not attained at any finite index. At every root the infinite tail certificate starts at k=19:898 shifted numerator coefficients are strictly positive and two leading coefficients vanish identically. All162 nondefining finite comparisons are strict; the other eight are exact defining equalities. A further3996 comparisons prove that the finite minima through2000 for roots5 and6 occur uniquely at2000. The ten global infima are approximately4575994.50395485,0.928753186732,0.000335595818181,0.000432597417132,0.00157823576986,0.00428563674028,0.00683709197395,0.0999473496198,0.122548496427,2006.76186694. Actual computation time0.7912919130seconds.'
ledger=Path('VERIFY_REPORT.md');s=ledger.read_text();assert '## V569 |' not in s
s+=f'\n## V569 | {now} | Exact global response infima at period nine\n\n**Claim.** The ten period-nine responses attain their global minimum at the stated finite indices, except at roots5 and6 where the infimum is the nonattained limiting modulus.\n\n**Method.** Apply the exact degree89 rational identity ofV567. Shift the denominator and signed numerator comparison polynomials by19, prove every required coefficient positive on the entire isolated root interval, and check all smaller integer indices. Recheck the saved strict inequalities at1536 bits and the source hashes. The lead independently accepted the complete argument at20:26:02Z.\n\n**Result.** {result}\n\n**Verdict: CONFIRMED; the global-infimum theorem is PROVED.** No monotonicity of the tail or sharp density-series radius is asserted. Evidence: {p}; review: {rp}.\n';ledger.write_text(s)
def ref(q):return dict(path=str(q),sha256=sha256(q.read_bytes()).hexdigest())
(root/'verification/admission.json').write_text(json.dumps(dict(at=now,entry=569,all_checks_pass=True,evidence=ref(p),proof=ref(proof),review=ref(rp),positive_tail_coefficients=positive,exact_zero_coefficients=zero,strict_finite_comparisons=finite,defining_equalities=equality,extra_finite_comparisons=extra),indent=2)+'\n')
lines=['# Global period-nine response infima','',f'PROVED in V569, {now}. Unit leading amplitude. Values below are directed enclosures; the exact definitions are in PROOF.md.','','| Root | Global minimizing index | Infimum of modulus |','|---|---:|---|']
for r in d['rows']:lines.append(f"| {r['root_index']} | {r['candidate_index'] if r['attained'] else 'Not attained; limit'} | {r['infimum']} |")
(root/'verification/INFIMA.md').write_text('\n'.join(lines)+'\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: V569 admits all ten Q9 global infima\n\n{result}\n\nYour20:26:02Z review is preserved with both278 and280. The T9 Values paragraph may now state these global minima and the two nonattained limiting infima as PROVED. The existing exterior bounds remain valid;280 is running the longer-prefix improvement with rational bounds strictly below these infima.\n\n'+p.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V569 admitted all ten global Q9 response infima after independent lead review and1536-bit receipt recheck.\n')
with Path('research/INDEX.md').open('a') as f:f.write(f'\nUpdate {now}:278 is PROVED inV569;280 protocol independently accepted, computation/replay underway.\n')
print(json.dumps(dict(at=now,entry=569,counts=[positive,zero,finite,equality,extra])))
