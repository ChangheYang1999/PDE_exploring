"""Admit the finite endpoint checks and report the unsafe lower-endpoint rounding."""
from pathlib import Path
import json
from certificate_admission import stamp,ref,checkref,next_entry
base=Path('research/307_final_numerical_summary');check=base/'verification/checks.json';d=json.loads(check.read_text())
assert d['all_checks_pass']
for r in d['source']+d['excerpts']:checkref(r)
ledger,text=next_entry(641);now=stamp()
result=('The necessary thresholds are 0.090297348070617..., 0.236597752797397... and 0.507476695384643... for sin7, sin9 and sin11. '
 'The decimals 0.0903, 0.2366 and 0.5075 in the numerical lane\'s stated proved brackets all round upward. '
 'Safe replacements are 0.0902973, 0.2365977 and 0.507476. The theorem lane already uses these safe values. '
 'The sin7 endpoint bases 0.5734 on100..300, 0.5739 on300..500 and 0.5736 on100..500 all round correctly. '
 'Their distinct windows explain the different values; there is no numerical discrepancy. The latter two physical diagnostics are approximately0.4994762251 and0.4992213002.')
scope=('REFUTED only as a claim that the three displayed lower endpoints follow by downward rounding from the cited necessary-radius certificates. '
 'This does not refute a stronger lower bound for the actual full series. The three endpoint computations are CONFIRMED as finite statistics. '
 'The asymptotic equivalence inferred from a finite ratio fit remains OPEN; the existing numerical-evidence heading does not supply an all-order estimate.')
p=base/'PROOF.md';s=p.read_text().replace('Status: audit protocol and elementary argument written before computation.',f'Status: finite endpoint checks CONFIRMED; unsafe certificate rounding REFUTED within the scope below, V641 at {now}.')
s+=f'\n## Completed checks\n\n{result}\n\n{scope}\n';p.write_text(s);snapshot=base/'sources/PROOF_at_V641.md';snapshot.write_bytes(p.read_bytes())
receipt=base/'verification/admission_V641.json';receipt.write_text(json.dumps(dict(at=now,entry=641,verdict='REFUTED',all_checks_pass=True,evidence=ref(check),proof=ref(snapshot),result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V641 | {now} | Final numerical-summary rounding and endpoint windows\n\n**Claim.** The stated proved brackets use justified lower endpoints, and the sin7 endpoint values agree with their stated windows.\n\n**Method.** Recompute all three exact gamma expressions at512 and1024bits; compare earlier certificates; decode the admitted sin7 norm balls and evaluate all three finite endpoint formulas.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
note=f'''## {now} VERIFIER -> NUMERICS, LEAD: V641, three small bracket repairs; sin7 endpoint difference is valid

In NUM_REPORT.md9b and FARFIELD_NUMERICAL_EXPERIMENTS.md5.13c/section6, replace the lower ends of the "proved bracket" displays:0.0903 ->0.0902973,0.2366 ->0.2365977,0.5075 ->0.507476. All three current displays round upward from the proved top-mode thresholds. The theory already has the safe values. This is a certificate-rounding defect, not a disproof of a stronger actual radius bound. Topic307 preserves the current excerpts and recomputes the constants at512/1024bits.

The sin7 endpoint0.5739 on300..500 is correct, while0.5736 is the distinct100..500 endpoint. V641 checks both plus100..300, so no repair to those values is needed.

For precision, NUM_REPORT item1's "i.e. ||f_n|| ~ C L^n n^-2 ... no factorial growth" should say "consistent on the stated finite window with a geometric law and a power correction; this fit alone gives no asymptotic equivalence." Its NUMERICAL EVIDENCE heading is retained. No new defect was found in the theorem statements.

'''
p=Path('NOTES_FOR_TEAM.md');p.write_text(note+p.read_text())
with Path('research/INDEX.md').open('a') as f:f.write(f'\n307. [Final numerical-summary rounding and finite windows](307_final_numerical_summary/PROOF.md). V641 confirms the three sin7 windows and gives safe necessary-radius decimals.\n')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V641 checks final numerical-summary rounding and all three sin7 endpoint windows. The first script attempt rejected a decimal string passed to fmpq; exact Fraction conversion fixed it before the successful0.02284s run. No failed output was used.\n')
(base/'sources/admit_final_numerical_summary.py').write_bytes(Path(__file__).read_bytes())
print(now,result)
