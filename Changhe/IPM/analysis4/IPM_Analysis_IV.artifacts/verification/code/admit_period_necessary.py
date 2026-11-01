from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,os
now=datetime.now(timezone.utc).isoformat(timespec='seconds');root=Path('research/259_period_seven_eight_necessary_radii');p=root/'verification/checks.json';d=json.loads(p.read_text());assert d['all_checks_pass']
lead=Path('../a4-lead/NOTES_FOR_TEAM.md').read_text();note=lead[lead.index('## 2026-10-31T18:42:43Z'):].split('\n## ',1)[0];lp=root/'sources/lead_derivation_1842Z.md';lp.write_text(note+'\n')
listed={7:['.3441017','5.956143e-5','5.740541e-7','6.838151e-6','1.009437e-4','4.448449e-4','1.261427e-3','3.379089e-3','1.098633e-2','.1014339'],8:['.7213489','1.110938e-4','5.257627e-7','1.962667e-5','9.601229e-5','2.893045e-4','7.775502e-4','2.179840e-3','8.234541e-3','.1127887']}
for group in d['groups']:
 Q=group['Q'];assert len(group['exact_top_checks'])==2*Q
 for row,claim in zip(group['rows'],listed[Q]):assert F(claim)<F(row['radius_bounds_exact'][0])
p=root/'PROOF.md';s=p.read_text().replace('Status: complete argument written before the arithmetic check. Independent review and directed constants are pending.','Status: PROVED in V535. The independent lead derivation of18:42Z agrees, every exact highest-sector check passes, and all constants are enclosed twice in directed arithmetic.')
s+='\n## Completed directed constants\n\nAll30 highest-sector coefficients through2Q agree with the exact Cartesian polynomials. Fresh512-bit and1024-bit root/gamma evaluations overlap. Every decimal lower bound in the independent18:42Z derivation lies strictly below the directed enclosure. The base radii are R_H=0.91368025953574548913... for Q7 and0.76889062508510007962... for Q8.\n\n| Q | Increasing root | Certified necessary radius constant, rounded down |\n|---|---:|---:|\n'
for group in d['groups']:
 for row,claim in zip(group['rows'],listed[group['Q']]):s+=f"| {group['Q']} | {row['root_index']} | {claim} |\n"
s+='\nMultiply each entry by |epsilon|^(Q/2). These lower constants are weaker than the exact strict thresholds in the statement. They do not determine a convergence boundary.\n';p.write_text(s)
rec=dict(admitted_at_utc=now,verdict='PROVED',ledger='V535',arithmetic=dict(path=str(root/'verification/checks.json'),sha256=sha256((root/'verification/checks.json').read_bytes()).hexdigest()),independent_derivation=dict(path=str(lp),sha256=sha256(lp.read_bytes()).hexdigest()),proof=dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()),lead_decimal_bounds_verified=listed)
(root/'verification/admission.json').write_text(json.dumps(rec,indent=2)+'\n')
p=Path('VERIFY_REPORT.md');assert '## V535 ' not in p.read_text()
with p.open('a') as f:f.write(f'''

## V535 | {now} | Necessary radii for every Q7 andQ8 two-mode branch

**Claim.** For each of the20 admitted branches in253 and256, uniform weighted termwise convergence through two angular derivatives requires R>(|b_i|/R_H)^(Q/2)|epsilon|^(Q/2), with R_H as in259.

**Method.** Specialize the proved highest-sector asymptotic, compare all30 exact top coefficients through2Q with the Cartesian prefix, and recompute roots and gamma constants independently at512 and1024 bits. Compare with the lead's independent18:42Z derivation and every one of its20 rounded lower bounds.

**Result.** All exact coefficients and directed overlaps pass. R_H is0.91368025953574548913... at Q7 and0.76889062508510007962... at Q8. All20 quoted lower bounds are strictly below the directed thresholds. At the exact threshold the highest Fourier coefficient of the second angular derivative grows as n^((Q+1)/(3Q)), so the strict boundary term test fails. Later free harmonics cannot alter that highest sector.

**Verdict: CONFIRMED and PROVED.** These are necessary lower bounds, not an optimal radius or an improvement of the sufficient bound. Evidence: research/259_period_seven_eight_necessary_radii/PROOF.md, verification/checks.json and admission.json. The arithmetic took9.43seconds.
''')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'''## {now} VERIFIER -> LEAD: V535 admits all Q7/Q8 necessary radii; minor method label correction

Topic259's independent512/1024-bit calculation agrees with your18:42Z note. All30 exact highest-sector coefficients pass, and all20 of your displayed lower bounds are strictly below the directed enclosures. V535 admits the strict necessary threshold and your rounded constants. Receipts are in259; the formula and boundary growth n^((Q+1)/(3Q)) are proved.

The existing sufficient Q7/Q8 radii already use the Remark5 resonance-block/prefix system, with N=2Q and e1=0: both period_seven_certificate.py and period_eight_certificate.py instantiate PrefixMajorant. Your description as a Remark4 box should be corrected. Longer independently certified prefixes could improve them; I am preparing that calculation.

Topic260 finite checks also passed:40,60,84 positive-frequency coefficients at Q4,Q5,Q6, and Euclidean remainder degrees[8,4,3,2,1,0], [10,5,4,3,2,1,0], [12,6,5,4,3,2,1,0]. Full potential density/stream reconstruction is exact. The first attempt had a rational-string parser error before computation; the repaired run took1.96seconds. With the existing Q3 result230 and Q7/Q8 result258, this would prove that all40 integer-period two-mode profiles require a first-period potential logarithm. Your260 review is still requested.

'''+p.read_text())
p=Path('research/INDEX.md');s=p.read_text().replace('Conditional necessary-radius specialization and directed arithmetic protocol.','PROVED necessary-radius specialization and directed constants (V535).');p.write_text(s)
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V535 admits Q7/Q8 necessary radii after independent lead agreement and20 directed decimal comparisons. Topic260 exact polar, Euclidean and potential checks pass; review pending. Corrected the Q7/Q8 sufficient-box method label in a team note.\n')
p=Path('VERIFY_SUMMARY.md');s=p.read_text();s+='\nUpdate '+now+': V535 proves the necessary radius thresholds for all20 Q7/Q8 branches. Exact top coefficients and512/1024-bit constants agree with the independent lead derivation.\n';p.write_text(s)
print(now,'V535 admitted')
