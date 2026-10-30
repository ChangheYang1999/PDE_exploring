# Reproducing lane N4 results

Current index updated 2026-10-29T18:56:11.662967+00:00 through N4-442. Dated additions preserve historical records; AUDIT_SUMMARY.md gives the current synthesis. The N4 evidence index v03 is the completed49-root final integrity audit, N4-435, with7497 direct local comparisons and no errors. The N4 evidence index v02 is the earlier fifteen-root integrity audit. Earlier dated OPEN statements are historical, not the current status.

The claim ledger is VERDICT_LEDGER.md, in chronological order. It states which values are independently CONFIRMED and which remain OPEN. Mathematical statements, hypotheses and derivations are indexed in research/README.md. A successful numerical enclosure is not an existence proof.

## Local execution contract

Run only in this lane, using copied inputs. Do not execute source or peer files in their original directories. One busy job at a time, on CPU57, with one numerical-library thread and low priority. A standard command prefix is:

```sh
timeout 590 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/tmp" taskset -c 57 nice -n 19 python3 -B
```

Append one script and its arguments below. Run sequentially and inspect each log. No JavaScript/TypeScript, servers/listeners, RLScience or other cluster, remote computation, GPU, Lean/Lake builds, git commits/pushes or online posts are used or authorized. Keep the lane under3GB and require at least20GB free on the build volume before a new job. Inputs in other lanes and source directories are read-only.

## Exact whole-plane residual norms

Canonical copied refits are in audit/numerical_audit/research_code/refit_audit/data/. The independent potential differentiation and Fourier algebra are in audit/numerical_audit/research_code/radial_fourier/code/radial.py. The residual is reconstructed from those fields, not imported from the other numerical lane.

- `audit/numerical_audit/research_code/whole_plane_norms/code/pipeline.py d2 assemble --bits 1024` constructs the exact D0 cache and checks four direct field values. The current result already exists; reassembly is unnecessary for ordinary review.
- `audit/numerical_audit/research_code/whole_plane_norms/code/norm_ball.py d2 G0 --bits 2048` gives4.98881700456802480088.
- The same command with `G1`, `P2`, or `Q3` gives1.02914187145366935206,20.53676513985447384,128.14736344527713275. P2/Q3 include a certified one-sided approximation to the prescribed nonpolynomial weight. Their output records the error and polynomial degree.
- The label `rF_proxy` gives2331.5659950371196. This is a weighted L2 norm, not the actual negative Sobolev norm.
- `audit/numerical_audit/research_code/exact_negative_norm/code/negative_ball.py d2 2048` gives the actual homogeneous negative norm390.2168349091225232455. Its formula and full numerical value are independently CONFIRMED. The independent N3 enclosure is safely [390.21683490911,390.21683493557]; see audit/numerical_audit/research_code/exact_negative_norm/REVIEW_N3.md and verification/N3_d2_confirmation.json.
- Replace `d2` by `Mpen2` for the corresponding copied refit. Its D0 assembly and G0 record exist; other completed or pending components are recorded in status file.

Exact derivative caches are reproducible intermediates and consume most disk space. Do not construct all candidate derivative caches together. The norm driver can derive only the needed order transiently. Numerical JSON files can contain very large rational strings: inspect selected keys with Python, not unrestricted cat/head.

## Weak necessary conditions

- `audit/numerical_audit/research_code/weak_probe/code/evaluate.py d2 --p 2 3 4 --bits 1024` gives exact whole-plane rational test integrals. The p2 pairing is-0.02880208111290875489468. These values were independently reconstructed by T4 through the background weak identity and confirmed.
- `audit/numerical_audit/research_code/pure_l2_probe/code/evaluate.py` evaluates the necessary L2 radius0.00271973702015789 and excludes the closed radius27/10000 without a gradient cap.
- `audit/numerical_audit/research_code/pure_l2_probe/code/audit_t4.py` compares that result and T4's sharper relative gradient bound against independent inputs. Its execution status is in status file.
- `audit/numerical_audit/research_code/localized_weak_probe/code/evaluate.py d2` moves the rational probe through powers t^k. This is a diagnostic over the finite recorded k list, not an optimization theorem.
- `audit/numerical_audit/research_code/annular_weak_probe/code/sanity.py` checks its coordinate change against three explicit homogeneous-field scaling identities and the exact Bernstein derivative bound.
- `audit/numerical_audit/research_code/annular_weak_probe/code/evaluate.py d2` applies compact C1 tests to prescribed annuli. The proof justifies these tests for distributional L2 corrections. Execution status and independent review status are in the ledger.

## Global matrix and point certificates

The completed L2 signed cover is audit/numerical_audit/research_code/signed_matrices/verification/d2_L2_768.json. It has82 accepted leaves and no pending cells. The completed unweighted first-derivative cover is d2_M1_relative_768.json with227 accepted leaves. Both have exact coefficient and code hashes and are CONFIRMED by separate T4 covers:120 cells for theta<=2/25 and326 cells for M1>=9/10. The cross-checks are T4_global_confirmation.json and T4_M1_confirmation.json in the same verification directory. The relative cover includes accepted leaves from the preceding stage, with its parent hash. Running the existing certificate driver against a finished result does not independently replay it; a second auditor must reevaluate every final leaf or use a separate enclosure method.

The older global matrix certificates, independently confirmed, are in audit/numerical_audit/research_code/global_matrices/. The exact point and candidate audits are in audit/numerical_audit/research_code/point_witness/, audit/numerical_audit/research_code/background_points/ and audit/numerical_audit/research_code/candidate_audits/. Each point failure is a lower witness for a supremum or a necessary-condition exclusion; no point scan is used to certify a global upper bound.

## Exact asymptotics and scope

`audit/numerical_audit/research_code/sector_audit/code/extend_stationary.py --order 12` checks the exact stationary density/potential recursion against the frozen N1 table. It has already succeeded for all orders0..12. The later order16 extension and independent N1 comparison confirm3060 exact coefficients and13 forcing energies through16; see N4-098 and audit/numerical_audit/research_code/sector_audit/verification/. This finite algebra does not prove convergence of the formal series or any fixed-radius remainder bound.

The four-branch family lower bound and cutoffs are in audit/numerical_audit/research_code/l2_family_floor/ and audit/numerical_audit/research_code/l2_box_audit/. The corrected pure exterior-power formulas and the counterexample to unsupported tail lower bounds are in audit/numerical_audit/research_code/tail_claim_audit/. Do not infer a full-residual tail floor from its first asymptotic coefficient alone.

## Exact projected residual and candidate probes

The following commands use the same CPU and thread prefix above, sequentially.

- `audit/numerical_audit/research_code/projected_residual/code/build.py d2 --compare-full` constructs the exact first sine residual mode and compares every coefficient with the full D0 cache. Replace d2 by Mpen2 for the second reference. Existing projections are immutable to this script; do not rerun a builder merely to read its completed verification record.
- `audit/numerical_audit/research_code/projected_residual/code/build.py C1-N1-002-7branch-frf` builds the corresponding exact projection from its copied canonical candidate. Candidate003 and004 use their full directory IDs. Complete background angular modes enter the later denominator.
- `audit/numerical_audit/research_code/projected_residual/code/probe.py C1-N1-002-7branch-frf` evaluates the prescribed k=0,128,512,1024 localized tests. Their conclusions require the noncompact-test hypotheses in the proof, checked through the candidate's exact sector audit. Independent review status is in VERDICT_LEDGER.md.
- `audit/numerical_audit/research_code/localized_weak_probe/code/beta_scale.py d2` uses a beta recurrence for very large k, without expanding a polynomial of degree2k. Shared small k agree with the older direct-power method.
- `audit/numerical_audit/research_code/negative_norm_tail_audit/code/check.py` reproduces the factor-two counterexample for the frozen N1 outer-outer term.
- `audit/numerical_audit/research_code/negative_norm_split/code/evaluate.py d2 8356.474846731926 --binary64-radius` computes the exact radial split at the same binary64 radius used in N1's diagnostic. The complete finite Green formula and independent synthetic check are in its PROOF.md. Existing result files are preserved by the driver.
- `audit/numerical_audit/research_code/l2_box_audit/code/sharp_snapshot_points.py` independently evaluates T4-055's six sharp-ball point gaps using rational intervals and the N4 Cartesian field records. Read the ledger for execution status.

Scaled generator checks (finite tests, not whole-plane norm certificates):

```
python3 -B audit/numerical_audit/research_code/multiscale_generators/code/check_moments.py
python3 -B audit/numerical_audit/research_code/multiscale_generators/code/check_cartesian.py
```

The output files already exist; these scripts intentionally refuse to replace their final records. To repeat them, preserve the existing outputs and run in an isolated copy of this lane's relevant topic. Expected:5400 exact moment equalities,207 canonical interval overlaps,90 symbolic derivative accuracy checks,220 exact origin-zero checks. The symbolic comparisons are decimal accuracy checks only. The direct evaluator supports the origin and scaled denominators; existing global norm certificates do not automatically extend to those denominators.

## Later candidate and weighted audits

The current status is in AUDIT_SUMMARY.md, updated independently of historical result files. A displayed decimal is not a directed bound unless expressly stated.

- `audit/numerical_audit/research_code/generator_sector_audit/code/audit_candidate.py CANDIDATE_ID` copies and hash-checks a new immutable snapshot, checks exact origin and forbidden sectors, and computes point obstructions. It supports the reviewed scaled generator families. The007 regression is CONFIRMED in N4-110. This is not a multiscale full-plane norm integrator.
- `audit/numerical_audit/research_code/weighted_laplacian_audit/code/check.py` reproduces the d2 weighted Cartesian Laplacian norms and parameter cover. The existing output must be preserved. Together with the independently reviewed inverse floor and plateau estimate, the whole registered dyadic scheme is excluded for d2; state131 has a separate tail certificate in audit/numerical_audit/research_code/dyadic_tail_audit/.
- The007 signed cover is audit/numerical_audit/research_code/candidate_background_cover/verification/C1-N1-007-d2w-j7-e2bal_theta_2_25_768.json. Its223 leaves and independent T4 polar232-leaf cover are CONFIRMED by N4-140. The complete frozen review and validator are in that topic's peer_review/T4 folder; verification/T4_007_confirmation.json binds them. The internal partition audit alone would not supply this peer check.
- `audit/numerical_audit/research_code/projected_laplacian_audit/code/check.py` independently rebuilds modes1 and3, checks the Cartesian/polar Laplacian identity, and compares their weighted moment bounds and four-cell cover with T4. Consult the ledger for completion status.

Updated 2026-10-29T01:32:45+00:00. Reproduction jobs that need more than590 seconds must be detached and polled, with bounded stages where possible. Preserve all existing accepted outputs; do not rerun append helpers.

## Symmetry compression and later records

- `audit/numerical_audit/research_code/parity_budget_audit/code/check.py` independently reproduces all dimension12 radial Gram and coupling entries for008, the positive pivots, and five exact trace budgets. N4-116 is CONFIRMED. It uses the Fourier Gram formula and direct gradient integrals, separate from T4's density integration by parts.
- `audit/numerical_audit/research_code/parity_angular_audit/code/check.py 4 4` and the corresponding arguments `8 6` audit complementary angular blocks. Preserve existing output records. Each invocation compares every exact entry and final scalar ball against the frozen T4 record; read VERDICT_LEDGER.md for completed sizes.
- N4-113 confirms the007 selected-mode Laplacian audit and its partial dyadic exclusion for a>=4/5. The smaller range0<a<4/5 remains open for that test.
- `audit/numerical_audit/research_code/exact_negative_norm/code/negative_ball.py C1-N1-005-d2w-j7-x3 2048` completed with actual norm42.2834585352371. N4-117 remains OPEN pending independent peer reproduction.
- `audit record signed_compression_audit, proof` supplies an independent proof review of the signed finite-compression bound. It does not require computation and makes no candidate-specific spectral claim.

The active process groups and pause/resume rules in status file take precedence over starting another computation. Do not use a historical wrapper that pauses only the old005 group while the priority007 group is running.

## New matrix and multiscale audits (2026-10-29T01:51:43.042687+00:00)

The successful commands are `audit/numerical_audit/research_code/generator_sector_audit/code/audit_candidate.py C1-N1-010-d2w-j7-x3bal-legqs`, `audit/numerical_audit/research_code/generator_sector_audit/code/compare010.py`, `audit/numerical_audit/research_code/candidate_audits/code/check_009_peers.py`, `audit/numerical_audit/research_code/parity_budget_audit/code/check_extended_v2.py`, `audit/numerical_audit/research_code/overlap_compression_audit/code/check.py`, `audit/numerical_audit/research_code/signed_compression_audit/code/check_matrix.py`, and `audit/numerical_audit/research_code/overlap_compression_audit/code/check_signed.py`. Use the standard single-worker prefix and a clean alternate verification target to avoid overwriting immutable completed results. The older check_extended.py rational solve was stopped, not accepted. N4-122..127 give results, scope and hashes.

## Candidate007 small-weight audit

`audit/numerical_audit/research_code/candidate007_weighted_laplacian/code/check.py --seconds 450` is a prepared resumable all-mode calculation. It requires the completed independently assembled007 D0 cache and assembly certificate; it has not yet run as of01:55Z. The manifest freezes code and input hashes. Completed mode records are immutable, partial sums are lower bounds only, and a full upper norm is produced only after every residual mode is present.

`audit/numerical_audit/research_code/origin_dyadic_ceiling/code/check.py` evaluates the new seven-cell conditional scalar obstruction using already confirmed modes1,3. Its first result passed, N4-128. The actual origin inverse theorem remains an explicit separately reviewed hypothesis. Read the topic's PROOF.md and REVIEW_T4.md before interpreting this as a candidate exclusion.


## Update 2026-10-29T02:17:02.141545+00:00: multiscale scalar moments and review status

The full candidate007 dyadic exclusion no longer awaits analytic review: N4-132 records Opus R1-017, and reviews/T1_REVIEWS_v14.md under audit/numerical_audit/research_code/origin_dyadic_ceiling/ records its explanatory corrections. The exclusion applies only to the registered sufficient scheme and hypotheses. Candidate010 point exclusions are independently confirmed by N4-136.

The new multiscale integrator is audit/numerical_audit/research_code/multiscale_moments/code/moments.py. Its PROOF.md states the exact admissible inputs and remainder bounds. Eight elementary formulas are checked by code/check.py; the saved verification/calibration.json is immutable. To rerun, copy that small topic to a fresh directory within this lane, remove only the copied verification/calibration.json, and run its copied code/check.py with the execution prefix above. Expected: eight overlaps, all nonnegative widths, then DONE 8. Do not execute a second busy job while the production queue or the all-mode checker is active.

This tool has no candidate-level assembly yet. In particular, the successful calibration does not certify candidate010's full-plane residual. Integer denominator multiplicities are an input precondition.


## Update 2026-10-29T02:22:00.159805+00:00: confirmed candidate007 G0 and signed cover

N4-139 confirms the complete G0 enclosure from the independent D0 cache against the frozen N3 beta-integral result. The completed comparison is audit/numerical_audit/research_code/whole_plane_norms/verification/candidate007_G0_N3.json; code/compare007.py performs the semantic coefficient and enclosure comparison. The saved output is immutable to that driver. N3v02 and compare007_v02.py are prepared for later independent G1/P2 checks; those checks have not run.

N4-140 confirms theta<=2/25 using the complete frozen T4 evidence under audit/numerical_audit/research_code/candidate_background_cover/peer_review/T4/. The local code/accept_t4.py checks every dependency hash, positive recorded margins, seed preservation, exact rectangle area and all26796 pairwise disjoint interiors, then compares the rate with N4's own cover. It does not reevaluate the peer's232 cell bounds; the independent peer code and outputs are preserved, and N4's original223-cell computation is separately complete. Neither cover supplies a high inverse or existence proof.

Update 2026-10-29T02:26:08.804786+00:00:009 background acceptance is in audit/numerical_audit/research_code/background_sobolev/code/accept009.py. Its frozen inputs and expected hashes are recorded in verification/T4_009_confirmation.json (SHA256 50ae0b3d7c678d21720c0eeb274f817455a37be93ea150547395dc735b3300b7); the checker is write-once, so rerun in an independent copy without that generated comparison file. It must pass four exact rational-energy equalities, five source checks, the column sum and both kappa overlaps. No large polynomial cache is used. For upcoming007 G1/P2 comparisons use compare007_v03.py, not v02 for weighted norms; see audit/numerical_audit/research_code/whole_plane_norms/COMPARISON_PROTOCOL.md.


## Independent review acceptance recorded 2026-10-29T02:30:23.499459+00:00

The immutable multiscale acceptance record is audit/numerical_audit/research_code/multiscale_moments/verification/T4_confirmation.json. Its checker code/accept_peer.py validates the frozen peer manifest and all calibration rows. The immutable selected-mode record is audit/numerical_audit/research_code/candidate007_weighted_laplacian/verification/selected_mode_confirmation.json. Its checker code/compare_selected.py compares49 mode/weight pairs and forms a partial sum. Both checkers intentionally refuse to overwrite their results. Reproduce in a fresh lane-local copy, preserving their relative paths, rather than rerunning on accepted outputs. Neither record is a full candidate residual norm.

## Candidate007 complete polar integrals and matched weak tests

The following commands are serialized behind the active queue. They preserve completed immutable records. Repetition for independent review requires an isolated copy with a new verification target.

- `audit/numerical_audit/research_code/candidate007_laplacian_fast/code/check.py --seconds 430` resumes exact polar Laplacian integration, outward polynomial products and all12 radial weights. All160 modes completed at02:42:31Z. The complete result and angular distribution are `verification/full.json` and `verification/angular_summary.json` in that topic. N4-147 remains OPEN peer. The older slow Cartesian calculation is retained only as a13-mode independent exact-product cross-check and need not be completed.
- `audit/numerical_audit/research_code/polar_derivative_norms/code/check.py state131 --labels P2` reproduced the retained weighted Cartesian Hessian enclosure (N4-148). State131 G1 and rF diverge.
- `audit/numerical_audit/research_code/polar_derivative_norms/code/check.py C1-N1-007-d2w-j7-e2bal --seconds 430` computes rF, G1 and P2 together without a large derivative cache. A full upper norm requires all160 modes. `code/compare007.py` checks every hash and total, exact canonical identity and the frozen independent N3 enclosures. Its live completion status is in status file. P2 comparisons use complete enclosing intervals, since the analytic weight approximants can differ.
- `audit/numerical_audit/research_code/weak_mesh_comparison/code/check.py` and `code/summarize.py` produced the matched k0..8 whole-plane pairing and denominator comparison. N4-146 confirms the k0 calibration and identifies the unmatched-k explanation. The newk1..8 exact values await peer reproduction.
- `audit/numerical_audit/research_code/laplacian_radial_band/code/check.py` computes exact radial annular energies of modes17..31, using incomplete power moments including the infinite annulus. This is a projection diagnostic. Only selected angular modes are integrated, and an annular fraction is not the complete annular fraction unless all modes are included.

Latest reproduction-note update: 2026-10-29T02:51:11.264686+00:00.


## Shift2 reproduction update 2026-10-29T03:13:12.295908+00:00

N4-149..155 have completed. Weak-row algebra, exact Gaussian-node pairing comparison and27-scale single-probe results are in research/weak_optimizer_audit, research/weak_radial_quadrature and research/extended_weak_probes; exact topic paths are in research/README.md. The rational n1 span audit is audit/numerical_audit/research_code/optimized_probe_audit/code/check.py (122.299167884seconds), with an exclusive immutable result. Candidate007 polar rF/G1/P2 and the complete N3 comparison passed (N4-153); no repeat is needed. The selected-mode radial annuli in audit/numerical_audit/research_code/laplacian_radial_band/verification/full.json remain OPENpeer. Candidate012 direct generator and canonical audits are in their named verification subfolders and cannot be overwritten.

The queued mode7 audit is audit/numerical_audit/research_code/angular_probe_audit/code/check.py. It uses frozen T4 polynomial/proof/code and an independently frozen OpusR1-022 review; its own Bernstein gradient cover and Cartesian fields differ from both peers. The exploratory80-probe angular scan is audit/theory_audit/research_code/angular_weak_probes/code/check.py --seconds430. Every computation is serialized by the wrappers named in status file. Reproducing an accepted exclusive output requires an isolated lane-local copy with a fresh verification target.


2026-10-29T03:19:13.754741+00:00: Topics64and65 completed. Mode7: audit/numerical_audit/research_code/angular_probe_audit/code/check.py, result candidate007_n7.json, independent of T4's polar fields and Taylor gradient bound; CONFIRMEDN4-157. Basis rank: audit/numerical_audit/research_code/basis_redundancy/code/check.py, result candidate007.json and1060 explicit relations; OPENpeerN4-158. Both checkers use exclusive creation of accepted result files; replay in a fresh lane-local output copy if needed. Frozen source and implementation hashes are recorded with every result. No foreign executable or cluster was invoked.


## Current reproduction update 2026-10-29T03:43:48.129620+00:00

All results through N4-169 are in the append-only ledger. Earlier statements that the007 all-mode table or Q3 is pending are superseded. No busy computation remains at this checkpoint.

- Eleven complete weighted-Laplacian norms: audit/numerical_audit/research_code/candidate007_laplacian_fast/verification/N3_comparison_v01.json, CONFIRMED N4-161. Its standalone comparison script is code/compare_n3.py if present; the authoritative code path/hash is stored in that result. The twelfth own weight remains OPEN peer.
- Complete007 rF,G1,P2: audit/numerical_audit/research_code/polar_derivative_norms/code/compare007.py and verification/candidate007_N3_comparison.json, CONFIRMED N4-153. All160 modes and every canonical entry are checked.
- Complete007 Q3: audit/numerical_audit/research_code/polar_third_derivative/code/check.py C1-N1-007-d2w-j7-e2bal --seconds430, then code/compare007.py. Accepted outputs are exclusive; do not rerun into them. All160 modes,2720 symmetry identities and12 fixtures pass. Driver completed in750.042seconds over two bounded stages, comparison1.497seconds. CONFIRMED N4-166. The state131 calibration is retained in verification/state131/full.json.
- Exact generator rank: audit/numerical_audit/research_code/basis_redundancy/code/check.py and reviews/T4_195/ACCEPTANCE.json, CONFIRMED N4-163. Exact constraint rank: audit/numerical_audit/research_code/constraint_rank/code/check.py, result verification/candidate007.json, OPEN peer N4-164. It imports only the frozen N1 origin algebra for a separate check, not the optimizer. Successful runtime0.856seconds. Failed preliminary scripts and logs are retained separately.
- Exact leading density: audit/numerical_audit/research_code/leading_tail_nonzero/code/check.py,0.074seconds, CONFIRMED N4-165. Raw generator and canonical sums, full Fourier differentiation and T4-203 agree exactly. This is the numerical condition for the separately audited weak tail-pinning application.
- N3 dyadic logic and candidate cover: audit/numerical_audit/research_code/dyadic_complete_cover/code/check.py,0.006seconds, two separate exclusive outputs. upper_bound_counterexample.json refutes the generic use of UB for exclusion (N4-168); candidate007.json confirms ten actual cells using containing norm balls (N4-169). No N3 source was changed.
- Candidate012 peer acceptance: audit/numerical_audit/research_code/generator_sector_audit/reviews/T4_204 contains the complete peer proof/code/result and22-check acceptance, N4-167.

Replay only in a fresh lane-local output copy, preserving the named relative input paths or adapting a separately hashed driver. Do not overwrite accepted records or create another large polynomial cache for a comparison that already passed. Small scripts write all outputs within the lane and require no server, browser runtime, cluster or remote compute.


Later exact audit commands, preserving existing outputs:

```
python3 -B audit/numerical_audit/research_code/polar_third_derivative/code/accept_t4.py
python3 -B audit/numerical_audit/research_code/constraint_rank/code/accept_t4.py
python3 -B audit/numerical_audit/research_code/family_tail_equality/code/check.py
python3 -B audit/numerical_audit/research_code/taylor_repair_audit/code/check.py
```

These records cover N4-170 to174. The Taylor audit confirms the peer's five rational parameters and triangle bound; its complete combined norm is OPEN peer. The family-tail checker includes ten exact references and both multiscale comparisons. Run serially on CPU57 with one thread, using a copied topic or new output paths if repeating an immutable result. The successor weak driver in audit/numerical_audit/research_code/successor_weak_probes/code/check.py accepts candidate IDs and writes a separate result for each frozen mode7/mode1 probe; its current execution status is in status file.


Exact quotient construction (N4-175, OPEN peer for the new map):

```
python3 -B audit/numerical_audit/research_code/quotient_coordinates/code/reduce.py \
  audit/numerical_audit/research_code/basis_redundancy/source/candidate007.json \
  NEW_OUTPUT_DIRECTORY \
  --canonical-check audit/numerical_audit/research_code/basis_redundancy/source/canonical007.json
```

Use a fresh output directory inside the lane. Expected:1922 independent generators, all1660 Legendre shapes retained,262 monomials,1060 exact kernel identities, equality with every canonical007 coefficient and identical second reduction. The helper is standalone and does not import or run the optimizer. The reduced exact generator file represents the same reference; binary64 rounding and conditioning need separate checks.


At 2026-10-29T04:06:33.145542+00:00, topics74/75 completed in own CPU57 subprocesses while2664587 was explicitly stopped and then resumed. Record: audit/numerical_audit/research_code/successor_weak_probes/verification/serial_pause04.json. Both commands used the pyenv3.12 interpreter, -B, one thread, nice19, no foreign code execution:

```sh
python3 -B audit/numerical_audit/research_code/branch_tail_audit/code/check.py
python3 -B audit/numerical_audit/research_code/constraint_nullity_audit/code/check.py
```

These scripts write their result with exclusive creation, so a reproduction must use a fresh copied topic output directory. Their source manifests freeze the exact peer files and own verifier inputs; do not overwrite accepted records. Frozen successor008 completed two modes in its sequential queue, N4-176, with code and input hashes in each JSON.

## Registered forcing comparisons and directed endpoints (N4-180/181)

Read audit record registered_norm_assembly, proof and source/MANIFEST.json. Run the following only when no other lane computation is busy, after moving the write-once result to a separate local archive if rerunning.

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 taskset -c 57 nice -n 19 python3 -B audit/theory_audit/research_code/registered_norm_assembly/code/check.py
```

Expected: all four component overlaps, all five strict nesting comparisons and every rational endpoint check pass; sharpw lower ratio >3596535.57. The exact 1/7 fixture demonstrates the generic endpoint-format failure. This is an independent scalar assembly from confirmed component records, with no new integration or foreign code execution.

## Successor peer acceptance (2026-10-29T04:19:43.934868+00:00)

The four completed weak checks are retained in audit/numerical_audit/research_code/successor_weak_probes/verification/. The independent T4 evidence for008/009 is frozen under reviews/T4_225_231/. The acceptance script is code/accept_t4_successors.py thereunder. It uses only local copies and the original frozen N4 probe records. Its existing ACCEPTANCE.json is write-once; use an isolated local copy of that directory and adjust the output location when rerunning. Original serial pause and stdout are retained.012 remains OPEN independent reproduction.

## Quotient peer acceptance and remaining derivatives (2026-10-29T04:27:14.834946+00:00)

N4-185 freezes and accepts T4-230 under audit/numerical_audit/research_code/quotient_coordinates/reviews/T4_230/. Its own code/accept_t4.py verifies the frozen proof/code/result and all five exact input hashes. Preserve its write-once output when repeating in an isolated local copy. The original exact quotient construction remains reproducible with a fresh output directory.

The remaining007 polar derivative calculation uses the existing audited D0 cache and writes one small record per angular mode:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 taskset -c 57 nice -n 19 python3 -B audit/numerical_audit/research_code/remaining_derivative_norms/code/check.py --seconds 430
```

Run a stage only when this lane's other computation has finished. Read its PROOF.md first. Each stage checks input hashes and resumes completed mode records; partial records are lower bounds only. The complete record requires all160 modes, every modal Cartesian-trace identity, all radial cross terms, independent N3 interval comparisons and the weighted identity rD2^2=N_1^2-D2^2+2G1^2. Do not rerun once its write-once full.json exists. Current execution status is in status file.

## Successor and scaled calculations, 2026-10-29T05:02:37.726131+00:00

The proof and successful recorded commands in successor_monomial_probes are `code/check.py C1-N1-007-d2w-j7-e2bal` followed by `code/check.py C1-N1-013-pairU-from007`. Default n21,K522. They refuse to overwrite their existing result files. The007 calibration is mandatory for a successor. The whole-plane direct projection avoids another large residual cache. Candidate013 point commands are candidate_audits/code/points.py with arguments `C1-N1-013-pairU-from007 1/10 73/100`, then uniform_point.py and point_extensions.py with the candidate ID.

The scaled backend proof is audit record scaled_weak_backend, proof. Its exact fields and independent Cartesian fixtures are in code/fields.py and check_fields.py. The scalar positive-pole moment proof, implementation and31 calibration fixtures are in research/rational_pole_moments. The007 full calibration used weak.py and succeeded196. Use weak_v3.py for010; weak_v2.py is retained solely as the failed schema change documented202. No nontrivial scaled whole-plane result is certified until its candidate record and independent review exist. Poll the worker in status file before any new computation.

The affine Taylor lift reproduction is audit/numerical_audit/research_code/affine_taylor_lift_audit/code/check.py. Its198 result is immutable and binds the frozen peer parameters and own Cartesian jets, centered differences and norm table. The008/009 dyadic peer acceptance is successor_dyadic_probes/code/accept_t4_successors.py, result193. Preserve all accepted outputs.

## Stronger013 audit and first010 result, 2026-10-29T05:12:35.174845+00:00

The independent013 reproduction is audit/numerical_audit/research_code/factored_monomial_audit/code/check.py. Its write-once verification/result.json confirms T4-255 with necessary distance >0.00199234339; PROOF.md derives Cartesian fields, Gamma-Beta moments and independent v-coordinate gradient extrema. Frozen peer files have a manifest, and every1922 canonical coefficient is checked against the own source audit.

Candidate010's first completed scaled weak result is audit/numerical_audit/research_code/scaled_weak_backend/verification/C1-N1-010-d2w-j7-x3bal-legqs_n7.json. It used weak_v3.py with candidate ID and --modes 7 1. Mode7 is complete205; mode1 is still active at this entry. Do not rerun that command over existing outputs. The radius >0.022479506978 remains OPEN until an independent candidate-level calculation is accepted. Scalar primitive190 is now CONFIRMED203, with independent39fixture evidence and ACCEPTANCE.json in rational_pole_moments/reviews/T4.

2026-10-29T05:23:04.522757+00:00: N4-207 second010 mode record is complete in audit/numerical_audit/research_code/scaled_weak_backend/verification; expected mode1 floor31373471/50000000000. N4-208 independently accepts the frozen013 polar review in audit/numerical_audit/research_code/candidate_audits/reviews/T4_013, whose ACCEPTANCE.json binds all33 checks. Topic87's executable correction is audit/numerical_audit/research_code/far_pairing_audit/code/check_v2.py, not the failed check.py. It explicitly compares the stored first projection against the complete residual before evaluating any large-K pairings. The active queue is serial_queue_v4.py and its log04; earlier queue versions retain startup failures.

## Current acceptance and uniform-tail work through N4-225

Historical dated entries above retain their original execution status. They
are not current OPEN labels. As of this update, 010 modes7/1,013 point/full
weak,014 point/full weak, the omittedq4 coefficient, and all19 complete
far pairings have independent confirmation. See AUDIT_SUMMARY.md and the
latest corresponding verdict ledger entry.

| Record | Executed own source or acceptance | Expected retained result |
|---|---|---|
|209/221|audit/numerical_audit/research_code/far_pairing_audit/code/check_v2.py; reviews/T4/accept.py|19 pairings,15 model errors,241 acceptance comparisons|
|210|audit/numerical_audit/research_code/scaled_weak_backend/reviews/T4/ acceptance evidence|Independent scaled-field algebra confirmation|
|212/213/223|audit/numerical_audit/research_code/candidate_audits/code/audit.py, points.py, uniform_point.py, point_extensions.py; reviews/T4_014/accept_v2.py|014 exact structure and56 point/source comparisons|
|214/224|audit/numerical_audit/research_code/successor_factored_weak/code/check.py; candidate_audits/reviews/T4_014/accept_v2.py|014 n21,K522 full weak result and28 acceptance comparisons|
|215/219|audit/numerical_audit/research_code/scaled_weak_backend/reviews/T4_010/ acceptance evidence|010 mode7 andmode1 independent confirmations|
|216|audit/numerical_audit/research_code/large_index_weak/code/check.py|Six007 whole weak tests and complete matching envelopes|
|218|audit/numerical_audit/research_code/optimizer_quotient_audit/code/check.py|Exact007/013 quotient source agreement, rank1922 each|
|220|audit/numerical_audit/research_code/far_pairing_audit/reviews/T4/accept.py|36 omitted-q4 source/coefficient comparisons|
|222|audit/numerical_audit/research_code/uniform_first_mode_tail/code/check.py|Six complete positive Beta majorants and exact upper rationals|
|225|audit record full_test_tail, proof and verification/MANIFEST.json|Analytic extension to the full M+C denominator; no new arithmetic|

All paths in this table are relative to the lane root. Read each exact
manifest before reproducing: it lists the executed version and dependent
modules. The original 014 accept.py failed on a metadata field before
creating any acceptance; accept_v2.py binds the same raw input through the
hashed canonical record and succeeds. The first failure and both actual
pause/resume records are retained.

The large-index program uses scalar K and a factored t^K. Do not expand
t^K to a polynomial for K up to10^10. Both endpoint moments, the direct
and integration-by-parts pairings, and the exact gradient extrema are
checked. The complete result is verification/result.json, with a compact
TABLE.md alongside the proof. Independent confirmation of216 and222/225
is still pending at this entry.

Some recorded acceptance and priority wrappers explicitly stop a known
queue PID and resume it in finally. Their process-control portion is
historical operational code, not a mathematical dependency. Never rerun a
hardcoded PID wrapper against a later session: inspect current status file,
preserve accepted outputs, and reproduce the numerical body in an isolated
lane-local copy with fresh process control and an exclusive output path.
Do not run maintenance/record_*.py again; those append the chronological
ledger and are not numerical verifiers.

For any new command set TMPDIR to this lane's tmp directory and
OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1. Use the pinned
Python3.12.13 with-B, taskset-c57 and nice-n19. The active queue owns the
single busy computation slot; pause and resume it explicitly before a
separate computation. Stop launching if free space is below20GB or lane
usage reaches3GB. No JavaScript/TypeScript, servers, cluster or remote
compute, Lean/Lake, commits or posts are permitted.


## Current additions through N4-236 (2026-10-29T06:28:44.967229+00:00)

The007 D2/rD2/Pw1 computation is complete and CONFIRMED236. Its full.json
and ACCEPTANCE.json live under
audit/numerical_audit/research_code/remaining_derivative_norms/verification/C1-N1-007-d2w-j7-e2bal/.
Do not run the resumable command again over that completed directory.
All160 saved modes and both Hessian identities passed.

| Record | Own source or acceptance | Retained result |
|---|---|---|
|226|audit/numerical_audit/research_code/factored_pole_moments/code/|239 factored moment comparisons and five fixtures; OPEN peer|
|227|audit/numerical_audit/research_code/scaled_factored_weak/code/calibrate_v2.py|126 mixed-scale jets and full013 calibration; OPEN peer|
|228|audit/numerical_audit/research_code/large_index_weak/reviews/T4/|312 comparisons confirm216|
|229|audit/numerical_audit/research_code/heldout_probe_register/verification/register.json|25 probes fixed at06:10:00Z|
|230|audit/numerical_audit/research_code/uniform_first_mode_tail/reviews/T4/|1858 comparisons confirm222/225, cutoff K>=3000000|
|231|audit/numerical_audit/research_code/scaled_dyadic_probes/code/check.py|Complete010 modes1/3 and seven strict cells; OPEN peer|
|232|audit/numerical_audit/research_code/candidate_tailrec/code/check.py|Nine candidates, 90 exact recurrence coefficients each|
|233/234|audit/numerical_audit/research_code/candidate_audits/code/audit.py; audit/numerical_audit/research_code/generator_sector_audit/code/audit_candidate.py|015 exact structure confirmed, point gaps OPEN peer|
|235|audit/numerical_audit/research_code/candidate015_holdout/code/check.py|25 probes outside the recorded102-row analytic objective span|
|236|audit/numerical_audit/research_code/remaining_derivative_norms/code/check.py|All160 modes complete, independent N3 overlap, weighted identity|

The new candidate runner is
audit/numerical_audit/research_code/scaled_factored_weak/code/check_candidates.py, invoked with the
exact candidate ID and n,K pairs, and --objective-audit pointing to the
candidate-specific hash-bound result. Its first actual invocation is
recorded in audit/numerical_audit/research_code/scaled_factored_weak/logs/candidate015_launch.json.
It computes whole-plane direct and integration-by-parts pairings, full
M and C norms, exact critical-point gradient caps and a strict rational
distance floor. Candidate and backend peer review remain separate from
these internal checks. Preserve all write-once results and use a fresh
local copy for reproduction.

N4-237 (2026-10-29T06:37:16.297806+00:00): `audit/numerical_audit/research_code/scaled_factored_weak/code/check_candidates.py C1-N1-015-pairQ-quot013 19,600 23,600 --objective-audit audit/numerical_audit/research_code/candidate015_holdout/verification/result.json` produced the two immutable records named in237 at2048 bits. Do not rerun in place: its write-once guard intentionally rejects existing outputs. In an isolated permitted copy, expect floors351804115950603/10^18 and1232449584356253/10^18, all18 Cartesian field overlaps, full-plane direct/parts overlap and strict global gradient caps. Both records remain OPEN peer/backend review.

2026-10-29T06:44:00.211491+00:00: N4-238 uses audit/numerical_audit/research_code/n3_stronger_weak008/code/check.py at2048bits,144.687945439seconds, complete result hasha8d5669dd7df65fc9557c0a7099053ace3c0fcf8d2c6a04ca61b5f1a495c61eb.239 uses scaled_factored_weak/code/check_candidates.py with01523,2400 and1,6144 and the extended objective audit. Existing outputs are write-once; reproduce in an isolated permitted copy.

2026-10-29T06:47:14.939689+00:00:240 uses weighted_tail_candidate_review/code/check.py; all6 raw-generator maps match frozen T4 tables.241 uses candidate015_peer_review/code/check.py for89 comparison/binding checks. Both outputs are write-once and bind full source hashes. Storage deduplication_v02 changes only inode ownership and relative links, preserving every read path/content.

2026-10-29T06:52:25.094391+00:00:242uses generator_sector_audit/code/audit_candidate.py C1-N1-016-legqs25-quot013,7.065568281s.243uses candidate016_holdout/code/check.py reading frozen text only, result57a7fd0da9db3842f81de94fe3fc3a2d635a765bfd5a12769899b5799050db02. Outputs write-once.

2026-10-29T06:59:31.724934+00:00:244/245 run dyadic010_and_01523_review/code/check.py after fullproof, own acceptance0.409/0.116s.246runs scaled_factored_weak/code/check_candidates.py C1-N1-016-legqs25-quot013 23,2400 19,1800 --objective-audit audit/numerical_audit/research_code/candidate016_holdout/verification/result.json with absolute audit path. Use pinned sources and write-once outputs.

2026-10-29T07:03:57.838541+00:00:247 run scaled50_factored_weak/code/run_calibration.sh with CPU57/nice19/threads1; scalar0.672s,complete calibration226.057s.248 run scaled_quotient_rank/code/check.py (0.153s). Inputs and result hashes are in their write-once JSONs.

2026-10-29T07:06:49.928856+00:00:249 negative_norm007_peer/code/check.py,CPU57nice19threads1,7.131s. Uses own complete007Green artifact and frozen gzipN3result, verifies allhashes. Doesnot execute N3code.

2026-10-29T07:08:02.494554+00:00:250 numerics_v08_audit/code/check.py, exact scalar counterexample and hash-bound comparisons to accepted221 and248,0.014s, CPU57/nice19/threads1. No N1 code executed.

2026-10-29T07:10:39.632107+00:00:251 candidate016_point_peer/code/check.py, own scalar recomputation/hash comparisons,0.108s,CPU57nice19threads1; never executes peer code.

2026-10-29T07:14:03.773753+00:00:252 negative_norm_forcing_assembly/code/check.py,CPU57nice19threads1,0.388s. Reuses accepted components139/153/166/249 and source-hash bound comparisons. No foreign code or norm integration repeated.

2026-10-29T07:17:43.960114+00:00:253 candidate016_weak_peer/code/check.py,0.904sCPU57/nice19/threads1. Scalar roots/globalcritical amplitudes and everygroup plushashbindings; noforeigncodeexecuted.

2026-10-29T07:19:46.533957+00:00:254 generator_sector_audit/code/audit_candidate.py C1-N1-017-legqs50-quot013,7.054s;255 candidate017_holdout/code/check.py,0.294s. CPU57/nice19/threads1, noforeigncodeexecution.

2026-10-29T07:25:29.505336+00:00:256 scaled50_factored_weak/code/check_candidates.py C1-N1-017-legqs50-quot013 23,2400 --objective-audit audit/numerical_audit/research_code/candidate017_holdout/verification/result.json;215.718stotalincludingfieldassembly. Own data only,CPU57,nice19,OMP/OPENBLAS/MKL1.

2026-10-29T07:32:55.827112+00:00: 257/259 use scaled50_factored_weak/code/check_candidates.py for candidate 017 and probes (19,1800), (21,522), with candidate017_holdout/verification/result.json. The complete three-probe invocation is recorded in candidate017_launch.json; outputs are write-once. N4-258 uses candidate016_sector_peer/code/check.py, 35.095 seconds on CPU57, nice19, one thread. It recomputes raw homogeneous sectors and reads frozen peer evidence as data only. Reproduce in an isolated permitted copy; preserve accepted outputs.

2026-10-29T07:33:32.937113+00:00: Removed the unaccepted candidate005 derived D0 cache (482782064 bytes), retaining exact inputs, assembly code and all norm result certificates. Lane now 2484718517 unique file bytes; build free 255868637184 bytes. CACHE005_PRUNE_RESULT.json records the historical hash and isolated reproduction command. The cache is reproducible; no accepted result was removed.

## 2026-10-29T07:40:27.103451+00:00: N4-260 and N4-261

Run the own comparison programs audit/numerical_audit/research_code/candidate017_point_peer/code/check.py and audit/numerical_audit/research_code/candidate017_weak_peer/code/check.py sequentially in an isolated copy, preserving the bound inputs and fresh output paths. They do not execute frozen peer code. The complete own 017 moment program is audit/numerical_audit/research_code/scaled50_factored_weak/code/check_candidates.py. Result hashes are 4466a7942781aec9d386f4c0efab46bff486005d77c579dfecb01cdf6163cc55 and 63aacaa0b7b8aa0f8ebe7d44e120c6dc6439289cf8cdf90c5897369f8d5d8be1. Runtime and exact dependencies are stored in each JSON.

## 2026-10-29T07:41:30.657458+00:00: N4-262 through N4-264

In an isolated copy with fresh outputs, execute candidate017_sector_peer/code/check.py (33.011 s) and scaled_rank_peer/code/check.py (1.024 s), using CPU57 and one thread. For joint arithmetic run audit/numerical_audit/research_code/joint_scaled_factored_weak/code/run_calibration.sh sequentially: scalar fixtures 1.243 s, field and complete weak regression 271.010 s. Retain all hash-bound inputs and preserve the original accepted outputs. No frozen foreign code is executed. Full scalar results are the three verification JSON files linked by N4-264.

## 2026-10-29T07:48:17.724522+00:00: N4-265

In an isolated copy with a fresh target, execute audit/numerical_audit/research_code/scaled_factored_weak/code/check_candidates.py C1-N1-016-legqs25-quot013 21,522 --objective-audit audit/numerical_audit/research_code/candidate016_holdout/verification/result.json on CPU57, nice19 and one thread. Probe runtime 184.760 s, total 209.012 s. This reuses the accepted hash-bound radius 25 backend and preserves all original outputs.


## 2026-10-29T08:13:52.746376+00:00: N4-266 through N4-271

Reproduce in an isolated permitted copy with fresh write-once output paths,
CPU 57, nice 19, and OMP/OPENBLAS/MKL threads set to 1. Retain the exact
inputs and every recorded source hash. Do not execute frozen peer code.

- N4-266: audit/numerical_audit/research_code/scaled_envelope_comparison/code/check.py, calibration
  at 007 followed by the six 016/017 probes. ENTRY266.json binds the
  complete-envelope results and saved FLOAT comparisons.
- N4-267: audit/numerical_audit/research_code/candidate017_weak19_peer/code/check_v2.py checks all
  63 independent moment groups, four fixture results and source bindings.
  The failed first checker expected no repeated fixtures; its source and
  correction remain alongside the accepted result. Runtime 1.040 seconds.
- N4-268: audit/numerical_audit/research_code/scaled_background_hessian/code/check_v2.py computes
  007, 016 and 017 serially, in 69.886, 81.875 and 82.345 seconds. The
  exact rational 007 energy calibration is required. The first endpoint
  comparison failure is preserved in CALIBRATION_CORRECTION.md.
- N4-269: audit/numerical_audit/research_code/scaled_density_injectivity/code/check_v2.py, 0.499
  seconds, binds both serialized old-basis files and compares their exact
  shapes. The first byte-identity assumption and its correction remain
  in verification/DEVELOPMENT_CORRECTION.json. Full informal proof and
  frozen Opus review are included.
- N4-270: audit/numerical_audit/research_code/generator_sector_audit/code/audit_candidate.py
  C1-N1-018-legqs25-cont12, 9.074 seconds, exact structure and point jets.
- N4-271: audit/numerical_audit/research_code/candidate018_holdout/code/check.py verifies all
  inherited objective rows, raw candidate and parent shapes, and register
  timing. Its immutable result is in verification/result.json.

The current candidate 018 weak invocation is recorded in
audit/numerical_audit/research_code/scaled_factored_weak/verification/candidate018_launch.json.
The subsequent radial-partition calculation has its complete informal
proof in audit record hessian_radial_partition, proof; it is not yet run.
All numerical claims above retain their separate ledger verdicts.


## 2026-10-29T08:27:21.083498+00:00: N4-272 through N4-278

Use an isolated permitted copy with fresh output paths. Keep exact JSON
inputs, proof and code hashes; CPU57, nice19, one thread, no foreign code.
Existing outputs are write-once. The preceding 08:13 launch status is
historical: both018 probes and the radial partition have now completed.

- N4-272: scaled_factored_weak/code/check_candidates.py for018 with
  19,1800 and23,2400 and candidate018_holdout/verification/result.json.
  Probe runtimes190.645 and214.084s; total428.714s including fields.
- N4-273: hessian_radial_partition/code/check.py, two candidates serially,
  87.303 and87.544s. ENTRY273.json records5400 direct/recurrence overlaps.
- N4-274: joint_scaled_density_rank/code/check.py,0.446s,168 exact Laurent
  witnesses and abstract2426 shapes. No actual mixed snapshot bound yet.
- N4-275: candidate018_point_peer/code/check.py,77 comparisons/bindings.
- N4-276: candidate018_weak_peer/code/check.py,291 comparisons/bindings.
- N4-277: candidate018_sector_peer/code/check.py,32.811s,complete sectors.
- N4-278: candidate018_origin_peer/code/check_v2.py,0.435s. The preserved
  first version fails only at decimal-string parsing. Use the corrected
  exact rational endpoints and preserve DEVELOPMENT_CORRECTION.json.

Every path above is under research/. Independent input files are frozen
alongside the proofs. Moment and derivative checks need no server or JS.

## 2026-10-29T08:36:21.562936+00:00: N4-279 through282

Run in an isolated permitted copy with fresh output paths; preserve all
input hashes. CPU57nice19one thread; no foreigncode or server/JS.

-279: generator_sector_audit/code/audit_candidate.py C1-N1-019-legqs50-cont12.
-280: candidate019_holdout/code/check.py. Frozen launch/log/source text.
-281: joint_scaled_rank_peer/code/check.py. Independent T4-348 inputs
 are frozen; for offline replay replace peer reads by the manifest's
 retained copies and check every original source SHA. Existing checker
 reads the peer source text but executes only own code.
-282: scaled50_factored_weak/code/check_candidates.py
 C1-N1-019-legqs50-cont12 19,1800 --objective-audit
 audit/numerical_audit/research_code/candidate019_holdout/verification/result.json.
 All paths above except the argument are under research/.

Probe computation ended2026-10-29T08:34:44.411729+00:00; runtime178.663923s.
Existing outputs are write-once. ENTRY279_282.json binds these four records.

2026-10-29T08:40:48.763991+00:00: N4-283: audit/numerical_audit/research_code/candidate018_weak_n23_peer/code/check.py; inputs frozen in its data folder, own execution only, output write-once. The accepted n19 fixtures are reused only with identical complete backend source hashes.

2026-10-29T08:52:13.710725+00:00: N4-284..290 reproduction entry. All paths below are under research/.
- scaled_background_cover/code/certify.py build C1-N1-017-legqs50-quot013; requires retained007 reconstruction calibration. cover stage with --bits1536 --seconds420 --tau2/25 is incomplete and resumable with identicalinputs.
- scaled_rational_background_cover/code/certify.py fixtures --bits512;20fixturechecks. Actual candidate cover remains OPEN.
- expanded_objective_span/code/check.py: frozen launchers and earlier25-pair register, proposed row lists only.
- candidate019_point_peer/code/check.py; candidate019_origin_peer/code/check.py; candidate019_sector_peer/code/check.py.
- candidate019_weak_peer/code/check_v2.py: explicit accepted017 fixture reuse source binding. Original check.py's fixture-count failure retained.
All actual CLI option names require a space before their values. Use an isolated permitted copy with fresh output paths and identical hashes; all accepted outputs are write-once. No publisher code is executed.

N4-291: generator_sector_audit/code/audit_candidate.py C1-N1-020-legqs25p50-quot013. N4-292: candidate020_holdout/code/check.py, after frozen source MANIFEST. Accepted outputs are write-once; reproduce into a separate own verification target. Full proof and hashes are in both result records.

N4-293: joint_scaled_factored_weak/code/check_candidates.py C1-N1-020-legqs25p50-quot013 19,1800 --objective-audit audit/numerical_audit/research_code/candidate020_holdout/verification/result.json. N4-294: higher_mode_scaled_rank/code/check.py. Both accepted own outputs are write-once; reproduce separately, retaining exact source hashes and full informal proofs.

N4-295: candidate_angular_resolution/code/check.py. N4-296..298: candidate020_{point,origin,sector}_peer/code/check.py. N4-299: candidate020_weak_peer/code/check_v2.py; original check.py deliberately retains the rejected denominator-equality requirement. See DEVELOPMENT_CORRECTION.json and complete PROOF.md. All outputs are write-once. Reproduce in a separate own-lane subfolder with bound sources.

N4-300..302: audit/numerical_audit/research_code/n3_scaled_norm_audit/code/check.py domain and calibrate reproduce the exact domain audit and independent admissible finite calibration; audit/numerical_audit/research_code/n3_quadrature_partition/code/check.py reproduces the exact multiplicity counterexample. Existing result files are write-once; use a separate own-lane copy to rerun. No candidate norm certification follows from fixtures alone.

N4-303/304: run audit/numerical_audit/research_code/scaled_hessian_peer/code/check.py and then audit/numerical_audit/research_code/hessian_partition_peer/code/check.py in an own-lane copy with empty verification/result.json targets. Every retained source is hash-checked; peer code is not executed. All mathematical identities are in the standalone PROOF files. Initial failed parser/diagnostic logs are retained and explained.

N4-305: audit/numerical_audit/research_code/n3_synthetic_field_audit/code/check.py reproduces all exact fixture fields, independent Cartesian values and four integral norm bounds. It requires the frozen302 backend files and accepted own generator/moment helpers. Use an own-lane copy and an absent result target for replay.

N4-306: audit/numerical_audit/research_code/higher_mode_rank_peer/code/check.py verifies the exact shape list, Laurent witnesses and all input bindings. Run in an own-lane copy with an absent verification/result.json target. Both analytic proofs are necessary dependencies.

N4-307: audit/numerical_audit/research_code/angular_tensor_peer/code/check.py checks symbolic frame identities,168 exact cyclotomic midpoint moments and bound application to the retained shapes. Use an own-lane copy and an absent result target. Read the full proof for the general theorem; the checker alone is finite evidence.

N4-308: audit/numerical_audit/research_code/scaled_product_norms/code/check_fixtures.py. Use an own-lane copy with absent verification/fixtures.json. The full proof precedes code and accepted305 dependencies are hash-checked. The production.py path is prepared but was not used for this finite calibration.

2026-10-29T09:56:57.740894+00:00: N4-309: audit/numerical_audit/research_code/candidate017_background_margin/code/check.py binds complete_cover.json and its entire reconstruction/Hessian input graph, checks exact partition and strict rate. Run on an own-lane copy with absent output and frozen cover. It summarizes the full leaf run; it does not independently replay every cell.

2026-10-29T09:58:18.039066+00:00: N4-310: audit/numerical_audit/research_code/rational_bernstein_peer/code/check.py; source/ contains all12 peer-bound inputs. Use an own-lane copy with absent outputs/source destinations. Exact actual-denominator transforms, fixture/Taylor records and partial-tree scope are independently checked.

2026-10-29T10:04:39.247310+00:00: N4-311: audit/numerical_audit/research_code/scaled_reconstruction_peer/code/check.py; source/ and retained own-lane polynomial data are bound by verification/result.json. Recompute in a fresh own-lane copy with absent output destinations. No foreign code executes.

## Lossless frozen-fixture archives, 2026-10-29T11:59:05.365587+00:00

The following historical copied fixtures are stored as gzip archives to keep this lane below 3 GB. Each decoded stream was hashed and counted before the original was removed. Mathematical evidence bytes and all code hashes are unchanged. Before replaying a checker that expects the original path, restore only the required file with the listed command, subject to disk headroom, and preserve its archive. Neither file is used by the running candidate016 production.

- `audit/numerical_audit/research_code/signed_matrices/peer_review/T4_global_gradient.json`: decoded SHA256 `f137a2ab4cf3eb59d039426449b2942bb8e50969f066cf4c0473313475bb7876`; archive SHA256 `29c1530c6d42ba547b83b341b841a47bb596877870ecb26b4856d7925a942d4d`. Restore: `gzip -dk audit/numerical_audit/research_code/signed_matrices/peer_review/T4_global_gradient.json.gz`.
- `audit/numerical_audit/research_code/signed_matrices/peer_review/T4_M1_reconstruction.json`: decoded SHA256 `98cd44974ce6d9164944c01ae6b6b46b142f478fe99cd4f0fee3ec0005952632`; archive SHA256 `1965a3782a179bf5210fbb50fc631ab1833ea764176f086063e7ba61cd08ac81`. Restore: `gzip -dk audit/numerical_audit/research_code/signed_matrices/peer_review/T4_M1_reconstruction.json.gz`.

Byte counts and actual verification times: maintenance/archive_T4_fixtures_1159.json.

2026-10-29T12:07:13.437489+00:00: N4-348..350. Run audit/numerical_audit/research_code/candidate023_peer/code/check.py, candidate023_shape_peer/code/check.py and candidate023_weak_peer/code/check.py sequentially under the core57 launcher. Each refuses to overwrite its accepted result. Preserve accepted outputs; use a copied separate topic for replay. Every own and copied peer dependency is hash bound, with lossless gzip entries explicitly marked. These are comparison scripts and do not execute peer code. Runtime33.986187827,.676428879,.610548170seconds.

### Documentation audits N4-351 and N4-352

The frozen sources and complete source-inspection arguments are
audit record candidate016_report_display, proof and
audit record screen_quantity_audit, proof, each with verification/INSPECTION.json.
These are literal source and mathematical contract checks, not new numerical
runs. Hash the retained inputs and read the respective table and theory_v07
section5.6. N4-351 restores eleven scientific-notation exponents; N4-352 uses
the density difference for NC-T-SCREEN. Neither changes candidate status.

2026-10-29T12:35:23.624422+00:00: N4-353: audit/numerical_audit/research_code/candidate016_n3_weak_comparison/code/check.py under the standard one-core launcher; preserve failed-v01 source and CLOCK_CORRECTION.json. Resultf80a4f27fd5307cc43d67f70573895fde4a4ce6e702c86169e51800b4fa3f4cc. N4-354: audit/numerical_audit/research_code/joint_scaled_dyadic016/code/run_bound.py --calibration-only. Calibration23b2a80b950bb4ddce9cc741ececfaa31eff915c5cef16d7335bd172afdc668c; supplemental source closurec11f357d7f58b6bdba120bfb82b181543c8e662bf5b1081d1e8228696e9bde1b. Existing output paths are immutable; reproduce in a copied topic or change output location deliberately.

2026-10-29T12:50:14.981898+00:00: N4-355: standard single-thread core57 launcher with audit/numerical_audit/research_code/joint_scaled_dyadic016/code/run_bound.py; source-bound result16a4a6ac... and bound c3ec1e20..., exact logs retained. N4-356..358: maintenance/run_024_and_v12.py ran the v12 checker, source freezer, point and shape comparisons; weak stage failed on a nonexistent adapter key. N4-359: corrected exact-register membership via maintenance/run_024_weak_v02.py, all349 checks pass; failed code/log retained. Never rerun exclusive-write successful outputs in place. Current remaining016 run: maintenance/run016_remaining_weak.py, sources/proof bound in preparation, row outputs immutable, wrapper resumes4035071 in finally.

2026-10-29T13:05:33.146059+00:00: N4-360 reproduction: standard core57 nice19 one-thread ownPython -B audit/numerical_audit/research_code/candidate016_remaining_weak/code/check.py. Existing immutable row outputs are reused only after input rebinding. Completed record maintenance/run016_remaining_weak.json;941.239s actual pause. Candidate025 serial launcher maintenance/run025_audits.py is active; per-step bound source companions live in candidate025_holdout/verification.

2026-10-29T13:08:20.245125+00:00: N4-361..363 were run serially with audit/numerical_audit/research_code/candidate025_holdout/code/run_bound.py shape, point, prefix under maintenance/run025_audits.py. Its exact record maintenance/run025_audits.json gives times, logs and runner hashes. Never rerun into existing immutable result paths; preserve and use a new explicitly versioned destination. The weak step is still running.

2026-10-29T13:12:37.186709+00:00: N4-364 completed maintenance/run025_audits.py weak step,318.123695277609s actual calculation, complete wrapperpause360.088773297146s. N4-365 comparison executed maintenance/run025_shape_peer_v02.py after failedv01. Bothcode/log/source_startversions retained. Source resulta7f4dcbdb6e64b5e919c423542b0f207f0c750bbed56f983b0e0245e25066548; comparisonstatements govern narrow history/step projection scope.

2026-10-29T13:21:32.364741+00:00: N4-366 to369 complete the own actual026 audit:2414 unchanged shapes,81 rows,46 outside probes; exact origin and positive six scalar/graded point gaps; complete16-sector prefix; whole-plane fixed-c correction distance>0.001355907204057457 at(19,1800). Independent T4 replay remains OPEN. See verdict ledger entries and their immutable result/source hashes. Serial commands are recorded in maintenance/run026_audits.json. Direct-point result139ac353... and bound companion7a65cce0... are distinct; the earlier status conflated their names.

2026-10-29T13:22:20.744465+00:00: N4-370 and371 independently accept actual025 point/origin/full-prefix and complete three-scale weak distance through T4-438 to441. Own raw2918 terms, all16 sector maps and63 weak integrals are covered. Strict fixed-c stationary-correction floor0.002065801265578052. See candidate025_peer/verification/result.json (b2a43e50ba8a028477e726319754ff5284864f410dfbe02a9b2645bdf28f1cfd) and candidate025_weak_peer/verification/result.json (f7f9ad2642275863bc2764062a1321e76093f1130d34fabcb5db220a26696b43); complete proof/source graphs retained. Main016 resumed after36.321898 seconds.

2026-10-29T13:25:31.388542+00:00: N4-372 audits exact numerics_v13 publication7ae8af17... with23 checks and300 FLOAT table entries. Several literal ranges/counts,024MID16 labels and endpoint-certificate attributions are refuted; actual025/026 certificates are unaffected. See audit/numerical_audit/research_code/numerics_v13_audit/verification/result.json (5411f621fee6cd61b094b05a0f7ec82182306cda06b3679120c0a9064d2b0a04) and its PROOF/source manifest.

2026-10-29T13:28:55.744514+00:00: N4-373 accepts actual016 G1 in[3.726906948019883998020959016407,3.726906948019883998020959016410], complete31 groups/30176 ordered pairs, minimum1730 bits. Resulte6808de8a032b8542d38ffc4b4731f2ace9a5e45898dcfab07792c4e63cbf943. G0/rF already341; P2 and Hardy remain OPEN.

2026-10-29T13:37:41.078783+00:00: N4-374 confirms ten actual016 scalar forcing-threshold failures from accepted G0 and G1 only. Common lower502.57580659137, sharpw lower745.109145778602; sharpw factor>3542234. Result1b402adaa66ee89e620efdd8ec79b40ee953c90c9389a48b502c99fc97313f2c, proofed8f4a073d6242d4648074b92f2803a1a598538aaddea8083fe2700f2dc18abf. Full P2/H remain OPEN; no inverse, correction nonexistence or existence conclusion.

2026-10-29T13:42:36.600411+00:00: N4-375 is audit/numerical_audit/research_code/continuation027_float_audit/verification/result.json (1831c9f4602774e9af8e3228cd54e6850cce482a03def1d75750bde1fcee14a3). Its checker performs only finite copied-FLOAT comparisons; no027snapshotacceptance. Reproduce in a fresh lane-local tree because the accepted result is write-once.

2026-10-29T13:46:12.248519+00:00: N4-376 selected direct-binding integrity is in audit/numerical_audit/research_code/final_evidence_integrity/verification/result_v02.json (cdbba883ae42f24d0bc17ae25647a8603d0aababa559940b268e4b16c07881ce). The accepted check_v02.py understands the explicitly documented N4-370 decoded-gzip convention. Do not run either write-once version on its accepted outputs. All original results remain unchanged.

2026-10-29T13:55:18.194780+00:00: N4-377 to379 accept actual026 shape, point, origin, complete prefix and all63 whole-plane weak integrals through T4-446 to450. Strict conditional fixed-c correction floor0.001355907204057457. Shape result a83e5fe77d461ca8c5f99c4c9cbf241f26be1a8dcc558f4d3fd2c55df32f46b3, point/prefix 8de25f826d0a199ddd499707e42ac8ef24469239d14e907fd944b55d30d374e3, weak d24a035e4171ce42cc86d94879bfa4bfe60ecb4a19c8cdeb6309cb0a7a3d2b9f. Supplemental imported-source scope and retained initial checker failure are explicit in verdict ledger. Main016 resumed13:52:18Z; P2 and own Hardy remain incomplete.

2026-10-29T13:56:44.341969+00:00: N4-380 reciprocally accepts T4-451 and N4-374. All ten specified candidate016 sufficient scalar forcing tests fail from accepted G0/G1 alone. Result 43f06a3fb7f657fdd5eaaafb637d3089134ed2a44eb04ed51327cee6d8d4cb3e. The saved-moment consistency check repeats no integration and yields no correction-distance or dyadic conclusion.

N4-381 selected report audit: audit/numerical_audit/research_code/final_scope_audit/code/check_v02.py, result_v02.json. The checker binds98 listed direct inputs using SCHEMA_v02.json and verifies22 assertions. Original v01 path-schema failure remains in logs/final_scope_audit.out. A clean replay must use a staged own copy because output creation is exclusive; do not overwrite the accepted result. This is no new integral computation or complete report audit.

2026-10-29T14:11:34.697320+00:00: N4-382 confirms candidate015 whole-plane projected Laplacian energies for modes1 and3 and all seven conditional dyadic cells, minimum strict ratio >1.242922259074. Own2048-bit integration agrees with all fourteen N3 exact mode energies and seven totals. Result 24bdc65df109a3002e4bdd6ac8676e955a606466c3fb046a4d04bcd91e741266; run maintenance/run015_dyadic_peer_v02.py with CPU57,nice19,threads1 and own TMPDIR after the recorded source freeze, preserving its earlier serialization failure. Outputs are write-once; use an isolated own output version for any fresh replay. No full upper norm or nonexistence follows.

2026-10-29T14:14:52.014606+00:00: N4-383 accepts three015 complete weak comparisons, including the sharp (23,2400) strict correction floor0.003033479200692324. The complete N4-239 moment source is independently reproduced by N3, and the identical global gradient cap is inherited from independently accepted N4-253. Main result c9350681334bee416f3fa085203b3ebd3c4e383654d61e3c9a477f95288a5375; cap transfer 68c78c8e4e21d20463d5958c183d7630c4c48b98a531fc2b71fc0c2fd7439a0e. The finite comparison executes no field integration. Four other N3 probes and own first-mode6144 remain outside this acceptance.

2026-10-29T14:21:08.655129+00:00: N4-384 accepts three017 complete weak comparisons and freshly bounds all global gradient critical values. Result 4f49a7b95ec6fdbbb274161149037c0b77d449db3e4daf3d02b08d46a110d996. Strict conditional floors at (21,522),(23,2400),(19,1800) are0.000596123050327423,0.001068502321536437,0.00167183069831928. The first is newly independently reproduced but remains an unregistered diagnostic. Three other N3 probes remain outside acceptance. Version1 input-schema failure is retained. Reproduce with code/check_v02.py in candidate017_three_weak_peer after reading its PROOF_v02.md.

2026-10-29T14:27:43.047363+00:00: N4-385 is a selected documentary consistency repair. research/final_handoff_status_refresh contains standalone proof, seven bound completed-result hashes and immutable before/after own summary copies. Result eb4ac9c976267944757b9f52720eb0789efe97b3d21f4c6d27b6ad287a928fb4. No mathematical calculation was repeated.017 mode-Hardy code is prepared only (PREPARE_v03); do not count its files as a result. Read status file for serialization and post016 sequence.

N4-386: audit/numerical_audit/research_code/final_table_trace/code/check_documentary_v02.py verifies the frozen105-row linkage and two exact documentary defects. Inputs and raw output hashes are in verification/documentary_v02.json; alias supplement PROOF_v02.md precedes execution. The checker creates its result exclusively; retain accepted outputs when reproducing in a separate own copy. One-sentence summary repair and frozen before/after digests are in verification/own_summary_repair_v01.json. No full-plane integral is replayed by this trace.

N4-387, 2026-10-29T14:49:46Z: audit/numerical_audit/research_code/final_table_trace/code/check_distance_v02.py verifies nineteen principal accepted distances against source/distance_contract_v01.json and the frozen report. Read DISTANCE_PROOF.md and DISTANCE_PROOF_v02.md first. The original run used CPU57, one thread and nice19 with the active dyadic child paused and restored. Result verification/distance_v02.json is immutable (9db8a391298b84c35edf5940c6cd4d0ac1d855248e0db661242bb752e4b38905); do not rerun into its exclusive path. This checks recorded sources and rational displays, not spatial integration. Version1 and its failed canonical-link assumption are retained.

N4-388: `audit/numerical_audit/research_code/numerics_v14_review/code/check_v02.py` checks the frozen publication against23 explicitly bound inputs and the original proof. It writes `verification/result_v02.json` once; use a copied output tree for a fresh replay. The first parser and its five punctuation failures are retained. No peer script is executed, and all ratios remain FLOAT observations.

N4-389: `audit/numerical_audit/research_code/candidate017_dyadic_preparation/code/run_bound.py` binds the complete own dynamic-module closure and runs `code/check.py` for fresh007 calibration plus017 projected modes1 and3 at a=1/4,7/4. It retains four mode JSON files, complete group decompositions, a numerical result and before/after source records. Existing outputs are write-once; a fresh run needs a copied output tree. `code/check_acceptance.py` checks the retained47-file acceptance and minimum ratio without replaying the expensive integrals. The seven-cell cover uses only two weights and retains its exact conditional framework hypotheses.

## N4-390: finite composition for 24 fixed-c weak exclusions

Run `audit/numerical_audit/research_code/h18_coverage_peer/code/check_v02.py` with the standard prefix after pausing the actual sole busy job. It checks 150 frozen or explicitly retained source records, all 24 strict weak inequalities, exact canonical bridges and eight scalar ceilings, plus the original graded/trans/statL bounds. Result `audit/numerical_audit/research_code/h18_coverage_peer/verification/result_v02.json` has hash f73dceb02100e4b51ac311f17ab1c47e03329db988a4468daa185d92b03ca438. The proof and three storage/display supplements precede the relevant checker versions. No peer code is executed and no integral is replayed. T2 nearest-rounded `root_lower` strings are presentation only; the own JSON stores directed rational floors. Frozen T4-459 and Opus T2 sections1-4 are accepted with their exact scope.

N4-391: run audit/numerical_audit/research_code/n3_final_table_scope/code/check_v03.py under the standard CPU57/nice19/threads1 environment, serialized with active production. It reads its frozen table, ledger extracts and accepted source records and produces verification/result_v03.json. v01/v02 failures are preserved; the frozen table already contains the007 status repair. No integration is rerun.

N4-392: completed production audit/numerical_audit/research_code/scaled_product_norms/code/production.py C1-N1-016-legqs25-quot013 --bits2048, then maintenance/accept016_full.py under standardCPU57nice19threads1 after main exits. Immutable full source and comparison_G0_rF_G1_P2_v01.json are preserved. N4-393: maintenance/run016_full_forcing_v03.py uses code/check_v03.py and exact dyadic endpoint rounding supplement; v02 failed output is retained. All ten sufficient tests and five same-parameter weighted forcing orderings are recorded. Do not rerun its exclusive output wrappers over existing files. Current016 mode-Hardy launch in maintenance/run016_hardy_launch.json; no second busy job.

N4-394: audit record dual_convergence_scope, proof and code/check.py give the exact nested-subspace counterexample and source-scope check. Accepted result verification/result.json bbb5aa6221d07eb0bcfd70f4acf65022d4817a85f2705a14763d097180423a8c,8checks. It refutes completeness inferred from two lower-bound values alone; it is not an IPM norm calculation. Use a fresh output path for a replay and preserve the accepted JSON.

N4-395: audit record weight_uniform_budget_peer, proof gives the exact spaces, matrix, constants, positive-denominator elimination, Bernstein proof and fixed-c composition. DECIMAL_PROOF_v02.md and SOURCE_PROOF_v03.md preserve two decoder/path failures. Successful checker code/check_v03.py produces verification/result_v03.json ad8ce179bfb5864570c97303f76db5d03de8bb92e7716a9a2d03698452ce2088,537checks177inputs40leaves. It independently reconstructs every proposed polynomial and every leaf coefficient; no peer code or residual integral runs. Preserve accepted output and use a fresh path for a replay. Finer Opus supremum estimates are outside this acceptance.

N4-396: audit/numerical_audit/research_code/candidate016_dual_lower/code/check.py reconstructs complete candidate016 projections from frozen exact data, independently integrates polar gradient energies and complete pairings, and assembles the two-mode lower bound and exact energy comparison. Its PROOF.md and verification/PROOF_FIRST.json precede the checker. Accepted verification/result.json e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa,38checks100inputs,4096bits. Use a copied output tree for replay because records are exclusive. The wrapper maintenance/run016_dual_priority.py paused/resumed the actual Hardy PID; do not reuse its historical process IDs. No peer code or solver executes.

Candidate016 pairing export repair: `audit/numerical_audit/research_code/candidate016_pairing_archive/code/check.py` freshly reconstructs both complete modes and all262 integrals; its existing successful records are immutable. For a rerun, copy the topic to a separate permitted workspace and redirect exclusive output paths. `verification/result.json` binds all sources and four650digit group archives; N4-399 records566passingchecks. This sidecar preserves and repairs the archive limitation of the original396/398 displays.

N4-400: candidate016_reciprocal_audits/code/check_v02.py binds the T4-466/467/470 proofs and accepted numerical records. N4-401: numerics_v15_review/code/check_v02.py performs the complete finite table/diagnostic audit. Both use exclusive outputs; preserve accepted results and use a fresh output path for replay.

N4-402: audit/numerical_audit/research_code/candidate016_archive_peer/code/check_v02.py checks every external source, exact grouped trial energy and all262 saved pairing groups. It preserves the failed source-label reader. N4-403: audit/numerical_audit/research_code/candidate016_angular_tail_bound/code/check.py --prefix 7 --version v01 produced the initial complete-tail certificate; select a new unused version for a larger prefix. It binds the source-certified groups and complete392 norm, without a new integral. Improved upper acceptance requires the separately recorded Opus reviews.

N4-404: audit/numerical_audit/research_code/candidate016_upper_opus_primary/code/check_v02.py independently reproduces the frozen primary Opus fixture fractions and full source bindings. Preserve its exclusive accepted result. The original decoder failure is retained. The positive-pole closed form is checked by polynomial identity and elementary integrals, without quadrature.

N4-405: audit/numerical_audit/research_code/numerics_v16_review/code/check.py repeats the complete own v15 finite audit against the frozen v16 publication and independently checks its new scalar data. Result71cdc0221e65657690aa3dfaec7ea0365faa3a0af4daddf8310b3a1703eee44f. All source values remain FLOAT; exact rational rounding checks are not PDE certificates. Preserve the exclusive output.

N4-406: own `audit/numerical_audit/research_code/upper_review_cancellation_peer/code/check.py` d7c7812e08ffcbf3941596877613962ed950a8c0f663367ee4ea715bcad44bb9 passes65checks. Proof precedes checker; source/MANIFEST.json binds exact JSON and peer files. Run through maintenance/with_single_worker.py onCPU57nice19threads1. Result 58e8e50e27a652e87963b0cfc4bcf9620d96317449b0aedadcb3f69b8338efc9. Peer code is text only.

N4-407: `audit/numerical_audit/research_code/candidate016_prefix_reciprocal/code/check_v02.py` 63685f36e664ecf53ad44ce070719431ec08d97a811d95d541f5f1d0e377740a passes438checks. Proof and source/MANIFEST.json bind the full dependencies. Original decimal-parser failure preserved. Use maintenance/with_single_worker.py; CPU57nice19threads1. Result eae57c4cdecf828199e5481ede1f22b7863d0c25b90ea683f420139d9740fed9.

N4-408: audit/numerical_audit/research_code/candidate016_upper_opus_reciprocal/code/check.py c92d21f026b998dbba12deee8f2608bb0bea70ce20ff97ece26e377513e9997b,834 checks and236 bindings, exclusive result 0a40e839e8be246d64554e3094d750ac38298c752e57cea3567832e534321add. No peer execution. N4-409: angular_tail_bound/code/check.py --prefix 31 --version v02 produced 01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41,2063 checks. For a replay use an unused version. Both short commands used maintenance/with_single_worker.py to pause and resume the actual multimode worker.

N4-410: audit/numerical_audit/research_code/candidate016_reviewed_upper/code/check.py a65ed67387d83bc1a1c7a41d822793a1c55a8ae585a80dfa72c622c98bda27e8;44 checks and254 bindings. Exclusive result d50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0. The general review condition is explicitly discharged, with the full omitted-mode proof included. No new integral or peer code is executed.

N4-411: audit/numerical_audit/research_code/frozen_report_1630_numerical/code/check_v02.py6204fd81;2455checks,1011bindings. Exact frozen report and matrix, own ledger,2023distance source edges. Result4decacd81c56e968084ee27055867d99e6c0e47556d5be9e4424dd2aefa886d9. Preserve exclusive output and original count105 failure. No peer execution or new integration.

N4-412: research/opposite_H_E2_order/code/check.py 281eb633b39b2e65c18472bd0cfd86a98dc978d71b7b25989eadbd14b11fee4f;12checks259bindings. Exclusive accepted resultab22cad41e4573fd832a7cb6150765e3e1b5e7c204818f4cdf887946491e27cd. Exact decimal-ball endpoints and rational squares only; preserve output for a replay.

N4-413: audit/numerical_audit/research_code/candidate017_conditional_totals/code/check_v02.py e8f98143982466c50345cf4f2342a15e61539fe8a0fbc6cf02bb6cfc8fbd44a1;441checks29bindings, result309a3946afa3d503e0b3559b787ca92d910cf043e11a85c6ff3228770cac0e52. Exact endpoint arithmetic; original upper-endpoint containment failure and corrected proof preserved. This is conditional total arithmetic, not source integration.

N4-414: audit/numerical_audit/research_code/partial_hardy_opus_reciprocal/code/check_v03.py 918668fda387b0e5a6c8b56da079a937405aedba20f19151379886629f0d3c2c;411checks282local67externalbindings. Exclusive resultec6e0347be958bf966347706be09ed02a7c036bedcca121e30a9ecbd5de3661a. Both schema failures and proof supplements retained. Run only through maintenance/with_single_worker.py withCPU57nice19threads1; no peer code or new integration.

N4-415: run `audit/numerical_audit/research_code/sharpw_fixed_norm_optimum/code/check_v02.py` with the executioncontract. Saved result800f9b6249ecd533367620fd1a12b1659d322b7fcc854a6832223b5de662ce9b;72checks. Outputexclusive; use a newversion for another fullrun. Immutable sourcecopiesand FAILED_v01remain.

N4-416: candidate016_multimode_dual_cross/code/check.py completed all16modes,6925checks,2130groups, resultc89c1735aa4dc582c4d32fd1d729613cf5a6ead38c9e1ed349869ef13a5381cf. Read standalonePROOF first. Outputs exclusive; fresh execution requires a copied permitted output tree. Complete source reconstruction and exact moments take about41real minutes onCPU57, with recorded short pauses. No peer execution.

N4-417: angular_tail_bound/code/check.py --prefix31 --versionv03 --multimode (arguments separated in the actual command). Result285dac39d93e32574c214d00cef9764087c0718c19b4042398c7ec728b530840,2065checks. N4-418: candidate016_multimode_complete_bounds/code/check.py --tail-version v03 --version v01,4430checks, result8eec600612f7719a1c0cbcb408d1665659b8d2c06d861f032a102651953c3728. For repeat choose unused versionnames; sourcebytesandaccepted outputs remainimmutable. Runthroughmaintenance/with_single_worker.py,CPU57nice19threads1.

N4-419: candidate007_origin_tolerance/code/check_v02.py d9860c555c8b20e7f93393c709322dae368855deb5dc33503c4cca530a1cb085,exact fmpqaxisjet,3005checks0.091s. Result25b9433e24295a2a934423c4204d176e661d652ec512fd962bb2ad5f3afa06da;exclusiveoutput,retain original failure andnewproof supplement. RunthroughsingleworkerhelperCPU57nice19threads1.

N4-420: audit/numerical_audit/research_code/numerics_final_literal_audit/code/check_v02.py 1f7d4524b10f6583dc31f5263920bdf78c1080b296dad9b8a68b7e2762d7bd7e;626 checks and600 printed values/factors. Result8158262abd44beccee63605aeacf061304b7bbe207abc827b1cdc10ecf28009b, exclusive output. Read PROOF and ERRATA_v02 first. Run with the single-worker helper, CPU57, nice19 and one thread. Preserved diagnostic v01 is not the accepted result.

N4-421: audit/numerical_audit/research_code/candidate016_final_reciprocal/code/check.py 6eb5442df84e658e155ebd9d54f4d58da14475646f83e464907ad8990cf159f8;180checks,17local and85read-only peer bindings. Result 2778e91c9f90071a0845408847694da82c6343d8259fe99f1677c7a2eff95157. Exclusive output. Run only with the CPU57 single-worker helper; no peer program executes.

N4-422 (2026-10-29T17:29:56.785821+00:00): standard single-worker launcher with audit/numerical_audit/research_code/numerics_final_repairs/code/check_v02.py.233checks,396local bindings,600display transfers; result_v02.json SHA256b18059380aec73b7e387bc40013d7f9d4420f47175d0ae17662b7e57a65d42b7. Scope is frozen text and serialized finite data. FAILED_v01 is a mistaken tight-endpoint expectation, corrected by the proof-first subset supplement. No publisher code or numerical field replay.

N4-423 (2026-10-29T17:35:12.234434+00:00): `audit/numerical_audit/research_code/final_literal_reciprocal/code/check.py`, SHA256 522a792a803f3efeaf7aec2a26ee2cddbfd267619e6fe59fae26e7a5102a6b6c; immutable result `audit/numerical_audit/research_code/final_literal_reciprocal/verification/result.json`, 7f63e1f28fd7f60a83513302f300bb7cf1152b25fc86de8c3e304026b125a442. Exact finite Cartesian and serialized-decimal replay,4128 checks. Use an isolated own-lane staging copy with an unused output path; never overwrite an accepted result. No peer execution.

N4-424 (2026-10-29T17:39:11.684797+00:00): audit/numerical_audit/research_code/numerics_final_repairs/code/check_v03.py 07f6990dbb7ba26ca3e296e1b4b599d899a9f6c684ea07f3dadd05161423fc9d;226checks402bindings. Result_v03.json 857cdac52d9e3598787d36dc8b7976566be5580233f091b6f6ffde1c6779e303. Use the standard CPU57nice19 single-worker wrapper and an unused output path in an isolated own-lane copy; accepted versions are exclusive. No peer program executes.

N4-425 (2026-10-29T17:44:01.820245+00:00): audit/numerical_audit/research_code/candidate017_dual_residual_replay/code/check_v03.py fafafa578079ecc47c75c6a1d3d11af0e89a8882aa17957e5d8f8d8509e96fd6;4096bits650digit exports,1339groups5704checks,2278.883752077s. Result7e093982e733237262819ca3ad0486f85bdc4d31c69d73a99e382dbad5c3ab06. Exclusive16mode andgroup outputs require an isolated own-lane staging copy with unused paths, CPU57nice19threads1. Never execute the retained peer programs. Full017upper/E2 remains OPEN.

N4-426 (2026-10-29T17:52:13.254111+00:00): audit/numerical_audit/research_code/candidate017_final_reciprocal/code/check_v02.py d252a906798eaf1c9c1eb2ad6ee136d3aaa20a4f7912c40abf02a138dce4cb5c, 984 checks, 243 local and 59 external bindings. Immutable result ead4de91e21981335ef4d4ce12a8085929fd5f1d6c64ea3b4bb3421c782c2b74. The first failure on a symlink alias is preserved in logs/candidate017_final_reciprocal.out; ALIAS_PROOF_v02.md explains the repair. Use the CPU57 nice19 one-thread wrapper and an unused output path. It executes no peer code and repeats no field integral.

N4-427/428 (2026-10-29T17:55:25.534067+00:00): standard single-worker launcher with candidate016_angular_tail_bound/code/check.py --prefix 47 --version v04 --multimode, then candidate016_multimode_complete_bounds/code/check.py --tail-version v04 --version v02. Resultsd1d90c2295662dd1288a3a77d100b0b9cc3cdfbfb8a8345399145c7cba3f0bff and42e43b1b5240309fad4ab3d7579dfe557ae15a89ead61b9a4991da18a4950513. All paths under research/. Existing result versions are immutable. Generic proofs and accepted Opus reviews apply to every complete prefix; no new source integrals in these compositions.

N4-429 (2026-10-29T18:02:05.316069+00:00): audit/numerical_audit/research_code/final_threshold_displays/code/check.py with the standard CPU57 nice19 one-thread wrapper;37 exact checks,16 bindings,0.010790654s. Result20599622969276b7f9005d4434a6f1a313e68be6fb508a5542c2b9f04e168cba. Use an isolated own-lane staging copy and unused output path. No peer execution or integral replay.

N4-430/431 (2026-10-29T18:09:52.834469+00:00): run candidate016_angular_tail_bound/code/check.py --prefix 63 --version v05 --multimode, then candidate016_multimode_complete_bounds/code/check.py --tail-version v05 --version v03, under CPU57nice19single-threadedPython. Existing outputs are immutable, so use fresh output versions for reproduction. Results dc1dfe24d70ba74c405e317864391dcb01e0a8188bbf8eb97edaefbe11ef9066 and6c5f02dc951d92cff7df788228594d2137e5f41b5bdea58b17b8505cb40cd3ee.

N4-432: candidate017_opus_residual_review/code/check.py performs2290exactchecks of raw regularity, fixtures and extracts, no peerexecution. Outputec2d4e90b3666a0b5d2c5b605a650a4cad0ef358b1881d2dc64ffc02570e8bdb. Freeze PROOF_FIRST precedescode at18:11:09.561717Z.

## Final reciprocal acceptance, 2026-10-29T18:18:18.076686+00:00

`audit/numerical_audit/research_code/final_peer_acceptance/code/check.py` uses own exact rational comparisons, no peer program or source integration. Run with the same CPU57/nice19/single-thread Python3.12.13 convention above. Its immutable first result records1099 checks,506 local and57 external bindings and SHA2562a0f29c6682109ce7b34d8aa8bd31b03fa6e8e0d82308a22e2a1beab04bf62e2. An existing result is never overwritten; a replay needs a new own-lane output copy/version and retained input identities. The complete source and analytic hypotheses remain in PROOF.md and its named accepted dependencies.

N4-434: run audit/numerical_audit/research_code/candidate016_width_decomposition/code/check.py under the standard serialCPU57/nice19 environment.23 exact checks, no integrals, resulted3c52666d41a2b49a99ff86f2a4608ffef6cfcb35952e9f016dcf2da1ce0275. Existing result paths are exclusive; use an isolated own copy for a rerun.

N4-435: maintenance/freeze_final_integrity.py --draft audit/numerical_audit/research_code/final_evidence_integrity/source/DRAFT_SELECTION_1826.json --version v03, followed by audit/numerical_audit/research_code/final_evidence_integrity/code/check_v04.py --version v03. Both completed at18:30Z. All targets already exist and are exclusive; preserve them. The result checks only the explicitly listed current direct local bindings.

N4-436: audit/numerical_audit/research_code/numerics_final_freeze_transfer/code/check.py, standard singleCPU57/nice19 prefix, completed414checks407bindings. Roote6635aed5d8382e25af9ba4b5fc6e01952e133a9eb52f5da4c6892252ab00c7e. It compares whole bytes and rebinds424; it does not repeat numerical integrals.

N4-437: `nice -n 19 taskset -c 57 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -B audit/numerical_audit/research_code/final_report_numerical/code/check_v03.py --version vNN` uses its matching frozen manifest. Existingv01outputs are immutable; replay in an isolated own-lane copy or newversion. Expected3278checks1258bindings, result520ab822b1c7695ea64e37c04a25ca54a6654daf8f07e50b100b4350969ae3a7. No source integration.

N4-438: inspect audit record final_energy_share_attribution, proof and result.json, then reproduce code/check.py in an isolated own-lane copy with no existing result. Use CPU57 nice19, one thread, Python-B. No original peer program is executed.

## N4-439 finite display audit

The frozen result is immutable. To reproduce in a new copied lane or version, keep both proof-first manifests and choose a new exclusive output path before running code/check_v02.py in research/final_numerical_display_audit under the execution prefix above. Expected342checks23bindings; no source integral. The original check.py failure is retained in verification/run.log; the corrected cover history is justified in COVER_PROOF_v02.md.

## N4-440 finite peer acceptance

The standalone proof and copied T4-509 inputs are in research/final_energy_peer_acceptance. A fresh exclusive output path is required before replaying code/check.py with the execution prefix. Expected 83 checks, 27 bindings, 12 original share endpoints. The checker derives both interval propagations and executes no peer program.

## N4-441 rounded-table peer acceptance

audit record rounded_table_peer_acceptance, proof states the exact three-row scope. Its code/check.py uses copied13peerinputs and own accepted endpoints; expected63checks23bindings. Replay in a fresh copy or with an exclusive new output path, with the stated CPU57/nice19 prefix. No source or peer code is executed.

## N4-442 final theory receipt

audit record theory_final_rerun_receipt, proof states the finite string-comparison scope. code/check.py uses69copied output pairs and three sideJSON pairs, with no T1 code execution. Expected329checks152bindings,51byte-identical15timing-only3rc-trailer-only. Replay only in a fresh copy or exclusive output path with the CPU57/nice19 prefix.

## N4-443 frozen report and current manifests

Read audit record final_report_diff, proof and both alias-repair notes, then execute code/check_v02.py in a fresh lane copy with CPU57/nice19 and an exclusive output path. It reads the nominated snapshot and N1 artifact directories without writing to or executing them. Expected4970 checks,37 local bindings,739 read-only external hashes,108 rows,18 report hunks; required literal repairs F1/F2 are expected findings. The current external mutable T4 addenda digest may grow without altering the frozen through510snapshot. The original failed checker and log are retained. This run checked manifests, not a numerical optimizer restart or all historical mathematical calculations.

## N4-444 selected postfreeze integrity

audit/numerical_audit/research_code/postfreeze_evidence_integrity/code/check.py checks the eight roots436through443 and every one of their1937direct local inputs, under CPU57/nice19 with one thread. Expected5464checks,1515unique local files,zeroerrors. Both result and the N4 post-freeze evidence index v01 are created exclusively. Replay in a fresh complete lane copy, or use a copied checker with fresh output names, keeping its expected input hashes and read scope unchanged. No peer program or historical numerical calculation is executed. The739external hashes retained by443 are provenance here, not freshly checked a second time.

## N4-445 optional producer-note rounding

audit/numerical_audit/research_code/producer_share_display/code/check_v02.py has26exact rational checks and10bindings. Read PROOF.md together with PROOF_v02.md, which fixes the initial own hand-transcribed y bracket. Preserve the failed version and use a fresh exclusive output path. The finite counterexample concerns what follows from four coarse premise endpoints; it is not an actual candidate norm or fractional-share counterexample.

## N4-446 report repair acceptance

audit/numerical_audit/research_code/final_report_repair_acceptance/code/check.py checks the copied19:14report and reproduction table against the1900copy.928checks29bindings. Read PROOF.md first; run in a fresh own copy with an exclusive unused result path. All inputs are local; copied T4 source is inert. The future coordinator final copy is not audited by this command.

## N4-447 final separate postfreeze index

audit/numerical_audit/research_code/postfreeze_evidence_integrity/code/check_v02.py validates11selectedroots436through446 and every1994direct local edge.5633checks23root-levelbindings1547uniqueownfiles. Read PROOF_v02.md and source/selection_v02.json first. Replay only in a fresh owncopy with exclusive unused result/index paths; preservebothversions. This does not replay mathematical computations or rehash739externalprovenanceentries.
