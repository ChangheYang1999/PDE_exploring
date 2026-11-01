"""Admit finite Q9 floating-data checks with independently verified saved bounds."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,gzip
from flint import arb,fmpq,ctx
ctx.prec=1024
root=Path('research/279_period_nine_floating_audit');p=root/'verification/checks.json.gz'
d=json.loads(gzip.decompress(p.read_bytes()));assert d['all_checks_pass'] and d['bits']==768
for r in d['inputs']+[r['source'] for r in d['results']]:assert sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']
limits={'norm_log':Fraction(5,10**11),'relative_exact':Fraction(125,10**14),'relative_binary':Fraction(125,10**14),'relative_root_effect':Fraction(35,10**16)}
for row in d['results']:
 assert row['announced_density_order']==306 and row['last_printed_order']==305 and row['maximum_fit_endpoint']==297
 assert row['norm_comparisons']==35 and row['response_comparisons']==32 and row['printed_fit_rounding_matches']
 for item in row['norms']:assert arb(item['absolute_log_discrepancy'])<arb(fmpq(limits['norm_log'].numerator,limits['norm_log'].denominator))
 for item in row['responses']:
  for key in ['relative_exact','relative_binary','relative_root_effect']:
   v=limits[key];assert arb(item[key])<arb(fmpq(v.numerator,v.denominator))
 assert [r['blocks'] for r in row['fits']]==[22,17,11]
 assert all(r['last_endpoint']==297 for r in row['fits'])
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
proof=root/'PROOF.md';before=root/'sources/PROOF_before_V568.md';before.write_bytes(proof.read_bytes())
s=proof.read_text().replace('Status: protocol and argument written before computation. Finite comparisons do not certify the high-order coefficient arrays.', 'Status: CONFIRMED in V568 on '+now+'. The protocol and argument preceded computation. Finite comparisons do not certify the high-order coefficient arrays.')
proof.write_text(s)
summary='All ten unit-normalized Q9 runs pass350 exact-root low-order norm comparisons,320 response comparisons at indices2..33 and60 line fits of printed block maxima. The maximum absolute logarithmic norm discrepancy is below5e-11; every response relative error is below1.25e-12 at either the exact root or its binary64 input, and the relative root-rounding effect is below3.5e-15. The producer announces last density order306 but prints norms only through305. Every fit ends at the last complete block endpoint297, with22,17,11 blocks for cutoff100,150,200. The four-decimal growth-base bins and two-decimal density RMS bins all agree. The initial verifier decimal decoder error was corrected before this successful0.8739618179-second run; its source and error record remain archived.'
ledger=Path('VERIFY_REPORT.md');s=ledger.read_text();assert '## V568 |' not in s
s+=f'\n## V568 | {now} | Period-nine floating runs and finite-fit attribution\n\n**Claim.** The printed Q9 responses, early norm data and line fits agree with independent exact and directed computations.\n\n**Method.** Evaluate the rational coefficient polynomials from267 and exact response formula from277 at the isolated algebraic roots and rounded binary64 inputs. Treat the printed decimal logs as exact rationals, solve the two-column normal equations, and check the printed rounding bins and every saved error bound independently at1024 bits.\n\n**Result.** {summary}\n\n**Verdict: CONFIRMED for these finite comparisons and printed-data statistics.** The high-order arrays are not enclosed by this audit. No asymptotic growth law or sharp convergence radius follows. Evidence: {p}.\n';ledger.write_text(s)
table=['# Period-nine printed-data density fits','',f'Checked {now}; V568. Unit amplitude; radius diagnostic A^(9/2). Complete block endpoint297. These are finite diagnostics, not bounds for the infinite series.','','| Root | Cutoff100 | Cutoff150 | Cutoff200 |','|---|---:|---:|---:|']
for r in d['results']:table.append('| '+str(r['root_index'])+' | '+' | '.join(arb(x['channels'][0]['R']).str(13) for x in r['fits'])+' |')
(root/'verification/FIT_TABLE.md').write_text('\n'.join(table)+'\n')
(root/'verification/admission.json').write_text(json.dumps(dict(at=now,entry=568,evidence=dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()),strict_error_bounds={k:str(v) for k,v in limits.items()},scope='Finite checks and printed-data fits only.'),indent=2)+'\n')
note=Path('NOTES_FOR_TEAM.md');note.write_text(f'## {now} VERIFIER -> LEAD: V568 admits Q9 floating-data checks\n\n{summary}\n\nThe radius diagnostics are tabulated in research/279_period_nine_floating_audit/verification/FIT_TABLE.md. They support the quoted finite range, with no asymptotic interpretation. Topic278 global-infimum certificate also passed; its proof review is still pending. I am preparing a longer Q9 prefix using the established175/261 majorant and these exact response lower bounds, starting with the third root.\n\n'+note.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V568 admitted Q9 finite norm/response/fit audit;350 norm checks,320 responses,60 fits, endpoint297. Starting longer Q9 prefix preparation.\n')
with Path('research/INDEX.md').open('a') as f:f.write(f'\nUpdate {now}: topic279 CONFIRMED in V568, finite data only.\n')
print(json.dumps(dict(at=now,entry=568)))
