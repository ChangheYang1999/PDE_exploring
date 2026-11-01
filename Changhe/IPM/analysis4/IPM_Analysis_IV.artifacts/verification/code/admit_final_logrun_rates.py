"""Admit independently recomputed finite canonical-log rate statistics."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re
from flint import arb,ctx
from certificate_admission import ref,checkref,next_entry
from read_evidence_bytes import read_bytes
ctx.prec=768
base=Path('research/306_final_logrun_rates')
p=base/'verification/checks.json';d=json.loads(p.read_text())
assert d['all_checks_pass'] and len(d['cases'])==5
assert d['initial_two_thirds_cutoff_mismatch']['labeled_N']==348
assert d['initial_two_thirds_cutoff_mismatch']['required_N']==329
corrected=Path('../a4-num/notes/logrun_rates_by_run.json');raw=corrected.read_bytes();j=json.loads(raw)
snap=base/'sources/logrun_rates_corrected.json';snap.write_bytes(raw)
comparisons=[]
for r in d['cases']:
 assert r['all_increments_negative'] and r['all_precision_replays_overlap']
 assert len(r['comparisons'])==2 and all(x['within_rounding_bin'] for x in r['comparisons'])
 delta=r['delta'];key=next(k for k in j if k.startswith(delta));s=j[key]
 assert s['last_order_used']==r['N'] and s['increment_orders']==f"{r['N']-29}..{r['N']}"
 tolerance=arb(1)/10**(6 if delta=='2/3' else 12)
 for label,sk in [('mean_increment','mean_inc_per_order'),('root','root_test_at_N')]:
  assert abs(arb(r[label])-arb(str(s[sk])))<tolerance
  comparisons.append(dict(delta=delta,statistic=label,printed=s[sk],enclosure=r[label],absolute_difference_bound=tolerance.str(25)))
 assert sha256(read_bytes(Path(r['source']['path']))).hexdigest()==r['source']['sha256']
ledger,text=next_entry(628);now=datetime.now(timezone.utc).isoformat(timespec='seconds')
result=('For delta=4/9,2/5,9/20,1/2,2/3, respectively, the thirty-increment means reproduce as -0.328,-0.254,-0.338,-0.419,-0.691 and the final roots as 0.4576,0.5387,0.4450,0.3716,0.1952. '
        'The final orders are300,240,240,300,329. All150 increments are negative and all10 displayed mean/root rounding bins pass. '
        'The three newly decoded checkpoints contribute385583 coefficient positions per precision replay. '
        'The initial two-thirds JSON used N348 while labeling its row certified; the corrected table explicitly uses N329 and orders300..329. '
        'All five corrected table windows and its approximate scalar entries agree with the independent calculation.')
scope=('CONFIRMED as finite norm statistics under the input-enclosure hypotheses in the proof. REFUTED initial two-thirds cutoff label, now corrected. '
       'This admits no new all-order geometric law and does not rerun every nonlinear coefficient recurrence.')
proof=base/'PROOF.md';s=proof.read_text().replace('Status: verification protocol written before new computations.','Status: CONFIRMED finite computations under the stated input hypotheses; initial cutoff label corrected.')
s+=f'\n## Completed checks, V628\n\n{now}. {result}\n\n{scope}\n\nThe complete norm-and-rate computation took {d["actual_elapsed_s"]:.9f} real seconds. Checkpoint decoding handles exact three-part dyadic balls; the reused norm receipts have four-part dyadic encodings. The two initial decoder attempts failed before producing a result and supplied no numerical evidence.\n'
proof.write_text(s);ps=base/'sources/PROOF_at_V628.md';ps.write_bytes(proof.read_bytes())
receipt=base/'verification/admission_V628.json';receipt.write_text(json.dumps(dict(at=now,entry=628,all_checks_pass=True,checks=ref(p),proof=ref(ps),corrected_table=ref(snap),original_corrected_table_path=str(corrected),corrected_table_comparisons=comparisons,result=result,scope=scope),indent=2)+'\n')
ledger.write_text(text+f'\n## V628 | {now} | Five canonical-log finite decay rates\n\n**Claim.** The replacement finite rate table uses the stated canonical-prefix cutoffs and reproduces the five late means and roots.\n\n**Method.** Decode supplied exact dyadic coefficient balls, sum absolute values and recompute31 norms at768 and1536 bits for three runs; reuse independently audited norm enclosures for the other two; check telescoping identities, negativity and rounding bins. Compare the initial and corrected JSON cutoffs.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {receipt}.\n')
note=f'## {now} VERIFIER -> LEAD, NUMERICS: V628 confirms replacement rates and closes V624\n\n{result}\n\n{scope} Topic306 holds the exact windows, source hashes, coefficient-ball sums and original/corrected JSON. The proof uses the explicit329 cutoff for2/3. V624 is closed in the current numerics prose.\n\n'
n=Path('NOTES_FOR_TEAM.md');n.write_text(note+n.read_text())
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: V628 confirms five finite decay-rate pairs and corrected N329 cutoff; independent norm sums at two precisions. Two decoder schema errors were corrected before any admitted output.\n')
i=Path('research/INDEX.md');s=i.read_text();s+='\n306. [Final finite canonical-log rates](306_final_logrun_rates/PROOF.md): five explicit final windows, independent coefficient-ball norm sums, ten rounded diagnostics, and the corrected two-thirds cutoff (V628).\n';i.write_text(s)
(base/'sources/admit_final_logrun_rates.py').write_bytes(Path(__file__).read_bytes())
print(now,result,scope)
