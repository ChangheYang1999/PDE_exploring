"""Write the current complete verifier handoff from admitted results."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
last=max(map(int,re.findall(r'^## V(\d+) \|',Path('VERIFY_REPORT.md').read_text(),re.M)))
reviewed={}
review_entries=[]
for receipt in Path('research/301_final_claim_audit/verification').glob('admission_V*.json'):
 data=json.loads(receipt.read_text())
 entry=data.get('entry',0)
 if entry>=657 and data.get('reviewed_proofs'):
  review_entries.append(entry)
  for item in data['reviewed_proofs']:
   assert item['path'] not in reviewed or reviewed[item['path']]==item['sha256']
   reviewed[item['path']]=item['sha256']
review_last=max(review_entries)
review_count=len(reviewed)
q9=json.loads(Path('research/301_final_claim_audit/verification/admission_V651.json').read_text());assert q9['all_checks_pass']
store=json.loads(Path('artifacts/storage/inventory_latest.json').read_text())
compression_manifest=max(Path('artifacts/storage').glob('json_compression_*.json'),
                         key=lambda x:x.stat().st_mtime_ns)
def latest(pattern):
 p=max(Path('artifacts/final_audit').glob(pattern),key=lambda x:x.stat().st_mtime_ns)
 return p,json.loads(p.read_text())
evidence_path,evidence=latest('*/admission_reference_checks.json')
local_path,local=latest('*/local_reference_inventory.json')
Path('VERIFY_SUMMARY.md').write_text(f'''# Independent verification summary

Updated {now}, through V{last}. The mathematical and numerical checks and all reported corrections are complete. Publication inventories have been checked within the scopes stated below; any later edits need a new comparison. Superseded claims and their corrections remain in the chronological [verification ledger](VERIFY_REPORT.md). Use the [claim map](FINAL_CLAIM_MAP.md) and [research index](research/INDEX.md) for exact hypotheses and standalone proofs.

## Main conclusion

**Nontrivial convergent infinite far-field series exist.** If 0 < delta < 1 is irrational and delta/2 is Brjuno, every nonzero finite real odd sine polynomial generates a real analytic exterior solution. The density, stream and common potential converge absolutely, with every fixed weighted Cartesian derivative, on each closed exterior strictly beyond the sufficient radius. Analytic leading data are also covered, in a smaller angular strip. The proof bounds products of small divisors along the recursion trees. See [13](research/13_lead_theory_audit/PROOF.md), [14](research/14_analytic_data/PROOF.md) and [76](research/76_error_level_majorant/PROOF.md).

At delta = 1/sqrt(5), unit sin(theta) has sufficient exterior R = 2^26, and the unnormalized Candidate 007 leading profile has R = 2^42. The same radii hold at the specified quadratic irrational within 2e-32 of the stored reference delta. At c = 2N + sqrt(5), with integer N >= 16, unit sin(theta) has sufficient exterior R = 128. These are sufficient radii, not sharp boundaries.

At rational delta = 2h/Q, where h and Q are coprime positive integers and Q > 2h, the tuned pure density and stream series converge for a nonzero finite real odd sine polynomial if the first compatibility condition vanishes and the subsequent affine responses have a positive uniform modulus bound. The first tuning index depends on whether h = 1 or h >= 2. First compatibility alone does not suffice. The common potential may require finitely many logarithms even when density and stream are pure powers. See [119](research/119_tuned_rational_series/PROOF.md), [131](research/131_general_odd_period_majorant/PROOF.md), [132](research/132_general_period_potential/PROOF.md) and [145](research/145_general_rational_convergence/PROOF.md).

There are **87 individually certified rational profiles**, all with explicit sufficient radii: 76 two-mode profiles, seven modified Candidate-shaped profiles and four single harmonics. [CERTIFIED_RADII.md](CERTIFIED_RADII.md) records the exact parameters, root ordering, amplitude powers and receipts. V606 checks all 87 certificate hashes and all radius and amplitude transformations in the lead's table. Necessary top-mode radius bounds are separate from these sufficient bounds.

For every fixed finite real odd sine profile with nonzero first harmonic, the pure series has radius zero on a dense G_delta set of irrational parameters. Its growth limsup is finite at every Brjuno point and infinite densely, so it is discontinuous at every Brjuno point on the full irrational parameter set. This is consistent with stability on bounded Brjuno sublevel sets. See [31](research/31_prime_denominator_obstruction/PROOF.md), [32](research/32_constructive_divergence/PROOF.md), [42](research/42_real_profile_prime_obstruction/PROOF.md) and [297](research/297_asymptotic_growth_discontinuity/PROOF.md).

Every fixed canonical truncation at every c > 1 is realized to its stated finite order by an exact exterior solution. The solution and radius depend on the truncation, regularity and weight. No single solution realizing a whole divergent series is proved. Prescribed multipoles and the canonical whole-plane velocity require their separate hypotheses. No global stationary extension is claimed.

## Candidate 007

The exact stored parameter is c = 4076476460239181/2251799813685248, with delta = 1824676646553933/4076476460239181. Independent Cartesian and polar extraction agree on ten nonzero leading harmonics. V599 checks the 416 branch-zero generators, ten potential moments, ten density coefficients, ten stream coefficients and the final exact table. All eight stored pure branches were checked earlier. This does not establish exact stationarity of the stored numerical object. See [02](research/02_candidate007/PROOF.md) and [295](research/295_candidate_publication_audit/PROOF.md).

The stored-parameter recursion has finite checks through order 500, including norms, Poisson equations and selected complete nonlinear sums. Its density norm root at order 500 is about 3.51133. Its first stream resonance is order 8152952920478362, where compatibility remains open. The seven modified Candidate-shaped profiles at delta = 4/9 are different exact constructions; at restored original amplitude their common sufficient exterior is R > 2^54.

## Finite computations and their limits

The canonical delta = 1/2 logarithmic unit-sine series is checked through order 300, with 2,255,534 polynomial Poisson comparisons, an exact Cartesian prefix through order 12 and complete nonlinear sums at orders 8, 12, 20, 40, 80, 160 and 300. Its density norm root at order 300 is about 0.371589. The ratio fit on orders 200 through 300 gives L about 0.383858 and a about 1.83745; the final ratio is about 0.381072. A finite ratio fit and an nth-root statistic are different quantities. See [291](research/291_canonical_half_finite/PROOF.md) and [300](research/300_half_ratio_diagnostics/PROOF.md).

The canonical delta = 2/3 continuation is checked through order 440 in [266](research/266_later_conditional_continuations/PROOF.md). Every result after the order-329 midpoint reset is conditional on those loaded midpoints. Small later arithmetic radii do not recover discarded uncertainty. The finite fits do not establish a limiting multiplier, power law or exponential law. Rounding reverses the ranking of two models on the final seven-point window: the printed data favor the power fit slightly, while the unrounded data favor the exponential fit. Neither comparison selects an infinite growth law.

The tuned sin(7 theta) run at delta = 4/5 is checked through order 500. V604 includes 2,006,500 Poisson comparisons, 501,000 denominator checks, all 500 density norms and complete nonlinear sums at orders 400 and 500. The old terminal free harmonic at order 300 is checked separately; the unset terminal stream harmonic at order 500 is excluded from a full stream norm. The line fits give density growth bases from about 0.5709968 to 0.5738023, with apparent physical radii from about 0.4963546 to 0.4994049. These are finite diagnostics.

All 44 extended floating runs at Q = 7, 8, 9 and 10 have been checked as finite printed datasets. Rounded roots and floating arithmetic prevent these checks from certifying all high-order coefficients at the exact algebraic roots.

| Period | Printed norm components agreeing | Complete tuning rows agreeing | Recomputed finite fits | Strict bound on same-window density-base change |
|---|---:|---:|---:|---:|
| Q = 7 and 8 | 12060 / 12060 | 769 / 770 | 360 | 3.2% for Q = 7; 3.8% for Q = 8 |
| Q = 9 | 6100 / 6100 | 318 / 320 | 180 | 6% |
| Q = 10 | 8372 / 8372 | 388 / 392 | 252 | 7.1% |

Every differing tuning component is retained explicitly and differs by 10^-12 in the printed value. For Q = 9 the maximum density-base change is about 5.92396%, at root 8 with lower endpoint 200; the derived apparent-radius change is below 29.6%. For Q = 10 the corresponding maxima are about 7.00794% and 30.46086%, at root 14 with lower endpoint 100. These apparent radii are finite statistics, not proved convergence boundaries. V615, V633 and V651 give the strict comparisons, windows and outward display ranges.

## Corrections, review and reproducibility

The final reviews repaired the amplitude factor in the primary radial weight, restored the integer hypothesis in the large-c family, named the precise velocity norm in its minimization theorem, corrected several rounded bounds and distinguished finite fits from asymptotic claims. In particular, the safe necessary-radius lower endpoints for sin7, sin9 and sin11 are 0.0902973, 0.2365977 and 0.507476. V643 verifies their integration in all three numerical texts. V653 verifies the final Q9 insertion. V656 closes an obsolete progress sentence about the completed finite-edge ball reruns: at order 300 their nonconstant factorial columns are strictly below the constant column, with degree 1 maximal among the nonconstant columns. This is a statement about the two modified recursions. The corresponding earlier refutations remain in the ledger.

V652 closes reading coverage for all 135 current standalone proofs linked in the claim map: 133 are unchanged from V635, and the updated topic 303 and added topic 307 have been read in full. The complete 502-line lead summary was read at V637; V638 corrects a clerical line-count typo in that receipt. V657 through V{review_last} add final complete rereads of {review_count} distinct proof texts covering convergence, divergence, multipoles, conditional criteria, arithmetic, fixed deficits, highest modes, genericity, projection limits, nontermination and profile geometry. V674 confirms that the 142 rereads include all 135 mapped proofs and seven additional supporting proofs, with matching current hashes. It also accepts the final lead report stamps and the three final-order status cells in the numerics report. The final lead summary has 501 lines after its two-line checkpoint stamp became one line. These rereads found no new defect. The larger assembled report was checked by result family and changed passages. This is not a new cover-to-cover reading of the entire assembled report or a fresh replay of every historical numerical certificate.

[REPRODUCTION.md](REPRODUCTION.md) gives executed low-order commands and explains the archive manifests. V646 confirms exact agreement of both final smoke replays. [PUBLICATION_INDEX.md](PUBLICATION_INDEX.md) records the finite file checks, operational exclusions and four publication projections of raw diagnostic transcripts. V648 rejects a faulty prototype path scan; V649 confirms the corrected expanded scan. These are provenance and text checks, not mathematical proofs.

The lead lane is configured for the main model; the actual service model identity was not independently attested. Findings and counterarguments were exchanged through team files throughout the campaign. No Lean verification is claimed. Some independent implementations share an exact arithmetic library; the affected receipts state that limit.

Canonical rational logarithmic convergence, compatibility at Candidate 007's stored parameter, necessity of the Brjuno condition, sharp convergence radii and a global stationary extension remain open.
''')
p=Path('FINAL_CLAIM_MAP.md');s=p.read_text();s=re.sub(r'^Updated [^\n]+',f'Updated {now}.',s,count=1,flags=re.M)
a=s.index('## Final checks');b=s.index('The canonical rational logarithmic convergence question',a)
s=s[:a]+f'''## Final checks

- V652 closes reading coverage for all 135 current mapped proofs. Of the 134 read at V635, 133 are unchanged; topic 303 is updated and topic 307 is added. The complete 502-line summary was read at V637, with its clerical count corrected in V638. This is not a new full-report reading or replay of every old certificate.
- V657 through V{review_last} add final manual rereads of {review_count} distinct proof texts covering convergence, divergence, exterior scope, conditional criteria, genericity, projection limits and profile geometry. No new defect was found; no new arithmetic replay is claimed.
- V674 confirms that the 142 rereads cover all 135 mapped proofs and seven supporting proofs. The final lead report hashes are accepted; three numerics status cells match the completed logs. The final lead summary has 501 lines after its stamp edit.
- Topic 266 is complete through conditional order 440, V622/V623. It retains the order-329 midpoint condition, external provenance and stated nonlinear-replay limits.
- Topics 305 and 306 separate the printed and unrounded fit rankings and check the five replacement finite decay rates. The 2/3 canonical window ends at order 329. V629 closes their prose repairs.
- Topic 290 checks all Q7/Q8 extensions; all printed norm overlaps agree, with the sole tuning discrepancy explicit. V615 gives strict finite percentage bounds.
- Topic 303 checks all Q9/Q10 extensions. V633 gives Q10 bounds of 2% for four-window spread, 7.1% for same-window density-base change and 31% for apparent-radius change. V651 gives the corresponding Q9 bounds of 1.4%, 6% and 29.6%. These are statistics of finite rounded-root floating runs.
- Topic 307 closes the necessary-radius decimal repairs in all three current numerical texts, V643. The different sin7 endpoint windows are all valid finite statistics.
- V653 admits the final Q9 report and summary insertion. V656 closes the finite-edge status correction. The summary and theory remained byte-identical during that last repair. All known substantive report corrections are closed.
- V655 confirms that all 307 numbered topics have a nonempty standalone proof and a reading-index link. This structural inventory is separate from the 135 mapped proof readings.
- PUBLICATION_INDEX.md gives the latest finite evidence and text checks, their actual times and their exclusions. Later edits require a new comparison.

'''+s[b:];p.write_text(s)
refs=[]
for name in dict.fromkeys(re.findall(r'\]\(([^)]+)\)',s)):
 q=Path(name.split('#')[0]);assert q.is_file(),q;refs.append(dict(path=str(q),sha256=sha256(q.read_bytes()).hexdigest()))
Path('artifacts/final_claim_map_sources.json').write_text(json.dumps(dict(at=now,scope='Current linked-file inventory, not a fresh proof or complete artifact audit.',map_sha256=sha256(p.read_bytes()).hexdigest(),sources=refs),indent=2)+'\n')
Path('RUN_STATUS.md').write_text(f'''# Verifier lane handoff

Updated {now}. Shift 4 began 2026-10-31T19:49:25Z. Team cutoff is 2026-11-01T00:57:42Z. Ledger through V{last}; next V{last+1}. Topics through 307; next 308.

## RESUME_HERE

At a new shift run date -u, read PROMPT.md fully, then this file and the peers' RUN_STATUS.md, NOTES_FOR_TEAM.md and reports. The prompt was reread in full in this shift, most recently at 00:25Z. Write only this lane. Never ask. No JavaScript/TypeScript, servers or listeners, remote or paid compute, RLScience or other clusters, GPU, Lean/lake, commits, pushes or posts. Use cores 17/18 at nice 19, at most two busy jobs, with one library thread. Heavy jobs use scratch/core17.lock or core18.lock. Each command finishes within ten minutes. Evidence paths stay relative.

The lead is configured for the main model. Actual service model identity is not independently attested. Collaboration is through team files.

## Final state and resumption

1. All Q9/Q10 cases are admitted. V650 is Q9 root 10; V651 gives all final Q9 ranges, signs and strict bounds: 1.4% spread, 6% density-base change, 29.6% apparent-radius change. There are 6100 identical norm components, 318/320 identical tuning rows, two explicit printed discrepancies and 180 finite fits. The audit-only coordinator PID 2771227 exited after all 24 Q9/Q10 cases completed at 23:50:13Z. No lane computation remains active.
2. All known report corrections are closed: final Q9 integration V653 and completed finite-edge reruns V656. V674 confirms the final snapshot post_freeze_20261101T003558Z. The lead theory is unchanged; only the lead summary and report stamps changed. The three numerics status-cell updates were checked against complete retained logs. Compare any later changes against this final snapshot. No further arithmetic replay is needed unless a substantive claim or input changes.
3. The evidence, local-reference, expanded text, compressed text and publication-projection checks pass within their stated scopes. Refresh the relevant inventories after later edits. Code/final_expanded_text_audit.py is the corrected scanner. V648 rejects its earlier prototype result at 23:46:20; V649 admits the tested version at 23:47:44. Exactly four known raw producer transcripts need the publication projections.
4. The readable status and handoff are current through the ledger entry above. The lead marked its reports final at 00:34Z; V674 accepts their final hashes. All required research and review work is complete. Any later change requires a new comparison before 00:57:42Z. code/write_final_verifier_state.py updates the current state; do not run the obsolete code/refresh_final_verifier_state.py. No pending user answer or approval exists.

## Completed checks

All 87 rational profiles have explicit sufficient radii, V606. Candidate extraction and table: V599. Amplitude correction: V600. Canonical half series through 300: V601/V602. Sin7 through 500: V604. Conditional 2/3 through 440: V622/V623, always conditional on order-329 midpoints. Q7/Q8: V609/V610/V615. Q10: V630/V633, prose repairs closed V637. Numerical bracket repairs closed V643. Low-order smoke replays: V646. All 135 current mapped proof readings: V652. V657 through V{review_last} add final complete manual rereads of {review_count} distinct proof texts in the convergence, divergence, exterior-scope, genericity, obstruction and profile-geometry chains. No new defect was found. V674 checks that these 142 rereads include all 135 mapped proofs and seven additional supporting proofs, with every current proof hash matching its reread receipt. Infinite theorem statements have not changed in these late checks.

REPRODUCTION.md has a hash in V646 and must not be edited without preserving that historical version. The assembled report has not been newly read cover to cover; the complete summary and changed passages have been checked.

## Evidence and storage

Storage inventory at {store['checked_at_utc']}: {store['unique_allocated_bytes']} allocated bytes, {store['unique_bytes']} unique bytes, {store['shared_free_bytes']} shared free bytes. Keep below 3 GB and avoid large copies. Closed JSON is losslessly archived through {compression_manifest}; code/read_evidence_bytes.py resolves original paths. Preserve current radius inputs and all immutable admission references.

The latest admission-reference audit, {evidence['checked_at_utc']}, checks {evidence['admission_count']} retained receipts and {evidence['reference_count']} embedded references with statuses {evidence['status_counts']}. The local inventory is dated {local['at']}. PUBLICATION_INDEX.md records the exact artifact paths and scopes. These are provenance checks, not a fresh replay of every old computation.
''')
Path('FINAL_AUDIT_PLAN.md').write_text(f'''# Final verification work

Updated {now}. Team cutoff: 2026-11-01T00:57:42Z. Only files count.

1. Complete: 87 sufficient-radius certificates, Candidate extraction and order 500, canonical half order 300, sin7 order 500, conditional two-thirds order 440, and all 44 Q7 to Q10 floating extensions, each within its receipt's scope.
2. Complete: all 135 current mapped proof readings, V652; complete 502-line lead summary at V637/V638; later changed passages. No fresh full-report reading or replay of all historical arithmetic is claimed.
3. Complete: final Q9 insertion V653 and finite-edge correction V656. All known report corrections are closed.
4. Complete within scope: publication and evidence inventories, with actual times and exclusions in PUBLICATION_INDEX.md. Readable handoff and claim map are current.
5. Complete: final report freeze V674, snapshot post_freeze_20261101T003558Z. Only the version stamps changed in the lead reports, and the three numerics completion cells match the retained logs. Any later change needs a new comparison; no research or computational job remains active.
''')
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: Rewrote readable live summary and handoff through V{last}. All known mathematical, numerical and report corrections are closed; any later edits require a new comparison.\n')
print(now,last,len(refs))
