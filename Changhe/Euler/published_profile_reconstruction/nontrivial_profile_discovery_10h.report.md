# Numerical search for nontrivial original Euler traveling self-similar profiles

Report prepared 2026-11-15T01:46:02.479390+00:00. All numerical allocations and final audits are complete; independent report review is recorded in G.


## A. Overall conclusion

**This campaign did not find a convincing numerical Euler profile.** It completed a new 10.34 hours of measured optimization, independent of the earlier paper-reconstruction campaign. The scientific objective imposed no published amplitude, sign, width, speed or geometry target, with jointly optimized C and the original unforced coefficients λ=1/2, ε=1. The principal optimized branches used an influential experimental soft sampled-RMS penalty, explicitly assessed in C. No published-profile image, published amplitude target or fixed-point target entered its losses or rankings.

The strongest advance was a regular two-field representation of U and Ψ with Ω derived from the elliptic equation. It removes the earlier independent Poisson mismatch and makes substantial transport progress without increasing model capacity. It does not resolve the coupled vorticity equation. The most decisive obstruction is a real imbalance at the dominant off-axis Ω extrema: the required swirl source 2UU_z is almost absent, usually has the wrong sign, and leaves essentially all of 1.5Ω uncancelled. The physical defect |rR_Ω| there is about 1.10–2.61 across the seven primary states and two targeted comparison states. These points are confirmed with arbitrary precision; small full computational-domain RMS and roundoff-level Poisson closure do not remove this obstruction.

The retained fields remain visibly nonzero, regular in their declared representation and decaying in their restricted asymptotic class. Their principal transport RMS values remain around 10^-4 in the full computational measure and around 10^-3 in active physical regions. The original system has not reached the proposed 10^-5 joint numerical target. Different regional and maximum criteria retain different leaders. No state is accepted as an Euler solution, and this finite search implies no nonexistence result for other branches or representations.


## B. Numerical research accounting

This new campaign began at **2026-11-14T20:12:34.181080Z**. The previous paper campaign's **36,611.87367958948 optimizer seconds are excluded**. Exact resumes preserve cumulative lineage but contribute only newly timed invocation intervals. Synchronized optimizer sections cover objective/gradient formation, accepted or rejected outer steps and their inner line searches. Setup, mining, benchmarks, checkpoint I/O, selection, validation, plotting and reporting have zero credit toward the required minimum. Exception intervals are excluded.

| Quantity | Measured value | Meaning |
|---|---:|---|
| New eligible optimization | **37,218.695871 s = 10.338527 h** | Actual distinct optimizer intervals only |
| Sections ending in accepted outer steps | 36,674.763713 s | Can include rejected inner line-search trials |
| Sections ending in rejected outer steps | 543.932158 s | Six finite rejected attempts, reported separately |
| Stricter accepted/noninitial optimization | **36,285.325063 s = 10.079257 h** | Excludes rejected outer steps and each invocation's first interval |
| Completed invocation-only mining | 4,659.197874 s | Other measured numerical exploration; zero minimum credit |
| Recorded disjoint benchmarks | 152.154916 s | Separate exploration/cost comparisons; zero minimum credit |
| Allocated GPU time, all registered parents | **15.751667 GPU-hours** | Includes setup, tests, validation and failed allocation costs |
| Allocated CPU time, all registered parents | **32.269444 CPU-hours** | Allocated resources, not utilization |
| Calendar elapsed through final resource capture | 19,769.568946 s = 5.491547 h | Captured 2026-11-15T01:42:03.750026Z after every allocation ended |
| Calendar elapsed through report preparation | 20008.298310 s = 5.557861 h | Includes waiting and reporting, as of 2026-11-15T01:46:02.479390+00:00 |

Both optimizer-duration counters exceeded 36,000 seconds before the final freeze. There are **12,284 unique intervals: 12,278 accepted and 6 rejected outer steps**, with zero duplicates, zero incomplete JSONL rows and zero exception-time credit. All 30 completion totals reconcile across 28 accounting lineages, including two nonoverlapping exact-resume chains. Concurrent branches contribute their own measured optimizer work; inherited counters and parent/child scheduler records are never double-counted. Mining and benchmarks are reported separately rather than added to calendar elapsed or used to meet the minimum. A 50.028-second interpreter-teardown investigation is setup/debugging, excluded from both optimization and those exploration figures.

All optimization was verified stopped at **2026-11-15T00:38:56.291108Z**. The immutable [ledger](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/accounting_at_stop.json), SHA256 `43cfe18390621bd71b3342a675bf5f36a404b046ffa4a130a57a538e0a9cd05b`, and [stop record](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/optimization_stop.json) are the duration authority. Before final audits, the 27 research parent allocations had consumed14.173333 GPU-hours and 28.567500 CPU-hours. The final [resource capture](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/running_final_20261115T0143Z_resources.json) includes all **34 registered parent allocations**, all terminal: 28 completed and 6 failed. Every invocation and sequential per-job optimizer sum lies within its parent allocated elapsed time; no invocation is unmapped and no registry drift occurred during capture. Unrelated IPM jobs are excluded. The final validator and integrity-join jobs receive zero optimizer credit.

| Job | Role | Parent state / exit | Allocated elapsed s | CPUs | GPUs |
|---|---|---|---:|---:|---:|
| 6903678 | Baseline A/B and expected-failure fixtures | COMPLETED / 0:0 | 41 | 1 | 0 |
| 6903987 | A/B continuation pilots | COMPLETED / 0:0 | 1935 | 2 | 1 |
| 6904085 | Elliptic pilot setup failure | FAILED / 1:0 | 45 | 2 | 1 |
| 6904087 | Alternative pilot setup failure | FAILED / 1:0 | 51 | 2 | 1 |
| 6904151 | Corrected elliptic pilots | COMPLETED / 0:0 | 2561 | 2 | 1 |
| 6904153 | Corrected alternative pilots | COMPLETED / 0:0 | 2570 | 2 | 1 |
| 6904309 | Historical C01/C02 pilots | COMPLETED / 0:0 | 1884 | 2 | 1 |
| 6904377 | Three-field batch/far-field comparisons | COMPLETED / 0:0 | 2013 | 2 | 1 |
| 6904381 | Regular elliptic raw/scaled comparisons | COMPLETED / 0:0 | 3174 | 2 | 1 |
| 6904677 | Interim geometry and precision | COMPLETED / 0:0 | 115 | 1 | 0 |
| 6904923 | E sampling control | COMPLETED / 0:0 | 2345 | 2 | 1 |
| 6904925 | E axis/gradient objective | COMPLETED / 0:0 | 3646 | 2 | 1 |
| 6904927 | Separate U/Psi coordinate scales | COMPLETED / 0:0 | 3032 | 2 | 1 |
| 6904929 | Historical conditioning/recentering | COMPLETED / 0:0 | 3151 | 2 | 1 |
| 6905379 | Five-state interim geometry/precision | COMPLETED / 0:0 | 328 | 1 | 0 |
| 6905651 | E sampled-RMS control | COMPLETED / 0:0 | 2959 | 2 | 1 |
| 6905653 | E sampled-RMS release | COMPLETED / 0:0 | 1020 | 2 | 1 |
| 6905656 | Tail-matched representation | COMPLETED / 0:0 | 2349 | 2 | 1 |
| 6905973 | Quartic residual experiment | COMPLETED / 0:0 | 2958 | 2 | 1 |
| 6906248 | S exact continuation | COMPLETED / 0:0 | 4510 | 2 | 1 |
| 6906719 | T fast exact continuation | COMPLETED / 0:0 | 2671 | 2 | 1 |
| 6907718 | S regional objective transfer | COMPLETED / 0:0 | 2569 | 2 | 1 |
| 6907878 | T interim geometry | COMPLETED / 0:0 | 165 | 1 | 0 |
| 6908011 | T tail multiprecision | COMPLETED / 0:0 | 146 | 1 | 0 |
| 6908060 | Small-delta smoke shutdown failure | FAILED / 75:0 | 27 | 2 | 1 |
| 6908063 | Large-delta matched optimization | COMPLETED / 0:0 | 2616 | 2 | 1 |
| 6908322 | Small-delta cleanup replacement | COMPLETED / 0:0 | 2938 | 2 | 1 |
| 6909214 | Initial final GPU0 setup failure | FAILED / 1:0 | 24 | 2 | 1 |
| 6909216 | Initial final GPU1 setup failure | FAILED / 1:0 | 21 | 2 | 1 |
| 6909218 | Initial final geometry setup failure | FAILED / 1:0 | 13 | 1 | 0 |
| 6909285 | Final GPU0 audit: four states | COMPLETED / 0:0 | 2851 | 2 | 1 |
| 6909287 | Final GPU1 audit: three states | COMPLETED / 0:0 | 2786 | 2 | 1 |
| 6909289 | Final geometry/precision: nine states | COMPLETED / 0:0 | 1945 | 1 | 0 |
| 6911242 | Final actual artifact join | COMPLETED / 0:0 | 5 | 1 | 0 |

These are parent allocation rows only; `.batch`, `.extern` and typed/generic duplicate GPU records are not charged again. Scheduler start/end strings use cluster local time; campaign timestamps above use UTC. Actual resource-hours differ from optimizer seconds and from the wall time of concurrent experiments. The [captured raw scheduler table and summary](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/running_final_20261115T0143Z_summary.md) retain exact resource requests and allocation bounds.

Technical failures are preserved. Early elliptic/historical pilots6904085/87 failed before optimizer work and were corrected in later validated plans. The original small-δ allocation6908060 aborted at native interpreter shutdown after its scientific smoke checks passed, with zero optimizer work; the cause was not reproduced in four actual replacement startup-control subprocesses and remains unconfirmed. Replacement6908322 preserved numerical/configuration bytes and used normal garbage collection/CUDA synchronization cleanup. Three initial final-audit allocations6909214/16/18 passed Stage B but rejected the central ownership marker in the output root before production tests or final coordinate generation. Their GPU parent processes read the saved seed record but performed zero holdout evaluations. Replacement routing to `{output}/audit` preserved source, checkpoints, cohort contract and the same seed. Failed setup costs are included above, with zero optimizer credit; [recovery evidence](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_audit_output_path_recovery.json) is retained.

## C. Comparison of formulations and search hypotheses

With A=r/2-r Psi_z and B=C+z/2+2Psi+rPsi_r, the optimized original residuals are

\[
R_U=U+A U_r+B U_z-2U\Psi_z,
\qquad
R_\Omega=\tfrac32\Omega+A\Omega_r+B\Omega_z-2UU_z,
\]
\[
R_\Psi=\Omega+\Psi_{rr}+3\Psi_r/r+\Psi_{zz}.
\]

All branches retain these physical coefficients. There is radial evenness and no imposed axial reflection. The regular representation uses s=r^2 and

\[
\Omega=-[8\Psi_s+4s\Psi_{ss}+\Psi_{zz}].
\]

This gives the correct axis limit 4 Psi_rr+Psi_zz and avoids differentiating a tiny-radius quotient. Training uses computational coordinates xi=asinh(r), eta=asinh(z). The independent evaluator assembles the original equations using physical-coordinate AD and a separately differentiated regular Psi_s expression. It never assigns RPsi a literal zero. The arbitrary-precision mirror independently implements scalar heads and product-rule jets. Shared model code remains a limitation of the FP64 comparison; the scalar MP checks reduce that dependence at the tested points.

The two-field shared tanh network has 749 trainable parameters including C and background amplitudes. Separate U/Psi coordinate maps use the same network and parameter count. The inherited A/B three-field model optimizes 2308 active parameters: C and the final correction, with earlier corrections frozen. Historical adapters preserve their exported signed corrections and use free C. No capacity increase was used as an automatic response to a plateau.

Dense self-scaled Broyden uses guarded line searches and saved full curvature. Collocation/objective changes reset incompatible curvature. SS-eSOAP and other guarded proposals were tested; short timing benchmarks are not long production comparisons. A persistent training-only hard archive is rescored with fresh broad/core/near-axis/far proposals. Separate common selection coordinates never enter mining or training. Selection reuses the computational residual implementation; independent physical-coordinate evaluation belongs to the separate pilot/final audits. Objective chunks accumulate the same deterministic mean and gradients. Unweighted equation errors are retained separately from weighted losses.

The field-only NT term is an explicitly experimental soft sampled-RMS penalty, relu(0.8 times reference minus current RMS)^2. Its threshold is not an exactly enforced inequality. For main E it preserves the original SS-Broyden reference 1.5556119501019996 on its original 512-point cohort; the earlier SS-eSOAP reference 1.5333661904 belongs to a different cohort. S preserves its own original 1.5616956530445267 reference and cohort. A descendant does not ratchet the reference down by redefining it from its trained amplitude. Positive trial penalties show that the term affects optimization even when accepted-state NT loss is zero. This sampled restriction neither represents physical energy nor proves nontriviality.

The genuine isotropic length symmetry is U_l(x)=U(x/l), Omega_l(x)=Omega(x/l)/l, Psi_l(x)=l Psi(x/l), C_l=l C. It does not gauge away U amplitude. Axial translation changes C; different C values alone do not distinguish solution branches. Adding constant Psi with a compensating C adds uniform physical velocity, which is incompatible with decay to rest unless that constant is zero.

### Controlled pilot and continuation evidence

| Experiment | Main observation | Interpretation |
|---|---|---|
| A/B continuation and larger/low-FF objectives | Training loss falls while broad/core RU or ROmega worsen; amplitude stays stable. Lower FF pressure does not fix all equations. | Spatial generalization and equation tradeoffs persist. |
| Early structural SS-eSOAP | E aspect pilot changes RU/ROmega only about 2% in 601s while sampled RMS drops3.4%; original steps take7–8s. | Weak progress in this configuration, not proof the optimizer is universally inferior. |
| Raw E SS-Broyden | At 1200s broad RU4.03e-4, ROmega1.073e-3, structural RPsi near roundoff; large reductions exceed20% amplitude change. | Substantive transport progress in the same749-parameter family. |
| Length-scaled RO/RPsi metric |900-fold relative weighting gives final RU.004530 versus raw-E.000403; ROmega improves modestly to.000871; axis RU.007814. | Better one-equation metric sacrifices joint accuracy. |
| Axis/gradient weighting | Improves axis accuracy and several bulk measures, but regional winners change after refreshes; Eaxis vorticity maxima can rise while RMS falls. | Preserve separate regional/max leaders. |
| Historical small step/recentering | Smaller initial step resolves zero-acceptance stall; recentering unlocks saturated widths, but ROmega still worsens and historical Psi widths remain unresolved. | Conditioning fix is not coupled-PDE convergence; amplitude near 38 is not the rejection reason. |
| S separate coordinate scales | Final 2401s broad RU1.758e-4, ROmega6.249e-4; late 900s amplitude-adjusted gains continue, with oscillating core/max defects. | Supports focused exact continuation; retain the 2113s vorticity leader too. |
| NT release | At 675s peak/RMS fall about 65%; relative RU/U worsens1.93/1.98/2.30 across broad/core/axis; final broad ROmega rebounds above source. | Preserved negative result; clean scientific stop, not rejection for smaller amplitude alone. |
| Quartic maximum sensitivity | Final 2400s matched broad/core max ROmega improve33%/36%, RMS 10%/11%; RU RMS stays within 2%, but axis ROmega worsens42% and RU maxima rise. | Measured maximum control with regional tradeoffs; no uniform promotion. |
| Tail-matched head | Free-C translation and filtered outer features target measured subleading tail defects; warm start is not a field identity. Slow path stops with full state; the 175-test fast release and actual-checkpoint parity gate pass before exact continuation. | Final audits retain substantial off-axis coupling defects and nonzero tail coefficients. |



These pilot/selection values are distinct from the fresh final physical-coordinate audit in D. All original A/B full-state starts were preserved; initial reports, code, configurations and independent audit records were inspected before the new branches were launched. Historical C01/C02 basins, lower-amplitude and signed initializations, three-field continuation, structural two-field heads, changes in separate field widths, sampled nontriviality release, axis/gradient losses, quartic penalties and tail-filter scales were tested. Most successful later states descend from the same structural E/S basin; they are not seven demonstrated distinct mathematical solution branches. An inverse-elliptic reconstruction was analyzed as a possible next formulation but was not implemented as a production candidate in this campaign.

S exact continuation accumulated 6002.438181 seconds on its inherited lineage, of which only 3601.715699 were newly credited in that invocation. The later S regional-transfer objective ran 1803.095971 new seconds with fresh curvature and clock; it improved several axis measures while retaining bulk tradeoffs. The old T fast branch was deliberately stopped with a full state after 1883.496192 new seconds,3132.054828 cumulative, short of its originally configured7600-second target; its regional stagnation motivated the stronger matched S-tail hypothesis. This is a disclosed adaptive allocation decision, with all criterion leaders preserved.

The matched S-tail pair received 1508.741865 new seconds at δ=10^-4 and 1500.468389 at δ=.01. Both start from the same frozen S1195 state,749 trainable parameters, original S sampled-RMS reference/cohort, fixed sampler seeds and fresh H/archive/clock. Adaptive mined points differ as the models evolve. At equal1500-second selection bins, large δ reduces broad/core/axis RU by about 14%/14%/24% and bulk Ω maxima by5–7%; small δ has1–2% lower bulk R_Ω RMS and 25% lower axis R_Ω maximum. U RMS differs by less than.022%, so these rankings survive amplitude adjustment. Relative to the unmodified S parent, both sacrifice bulk RU: approximately32–38% worse for large δ and 53–61% for small. The large-δ warm start itself initially raises RU15–52 fold despite changing sampled U RMS only about 1.2%; progress against that perturbed start overstates progress against the original parent. The [matched trajectory tables](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/paired_S_tail_results.md) preserve300/600/1200/1500-second comparisons. Neither δ is a joint winner.

The sampled nontriviality restriction is influential: final small/large tail sampled RMS values 1.2493182059/1.2493561434 lie just below the original S threshold 1.2493565224356214 with finite soft penalties. This is not an exact floor, physical energy or a length gauge. Releasing it gave falling amplitude together with worsening relative RU/U and later Ω error; small amplitude by itself was never the rejection criterion. The noncollapse labels mean that the recorded trajectory did not collapse under these experimental restrictions, not that Euler nontriviality has been established.

Chunking and shared-feature changes were accepted only after matching fields, objective and every named parameter gradient. Representative objective/gradient costs fell.1664→.0869s for A,2.783→.6687s for E, and 3.620→1.996s on the actual T checkpoint. These are local cost comparisons, not claims about universal optimizer superiority. Curvature was reset when objectives changed and restored only for compatible exact resumes. No architecture expansion was used to mask a plateau. All scientific source and checkpoints remain outside the prompt/report repository.


## D. Best retained candidates and independent validation

All seven frozen states completed independent physical-residual validation: **13,422,528 residual-point evaluations**, 1,917,504 per state, batch 4096, common seed **123636364**. Each state used one 1,000,000-point computational cohort plus fourteen 65,536-point regional cohorts. The seed was drawn once at 2026-11-15T00:40:58.418840+00:00 after optimizer stop and the 98-file source freeze. No further training occurred.

Both allocated bundles completed with normal exit 0. Their production suites passed 215 tests in 71.515s and 215 tests in 66.099s; these are overlapping suites, not a sum of unique tests. All 15 actual coordinate hashes agree across all seven states. Allocated production gates verified finite metrics, exact counts, checkpoint/model-state immutability, and frozen evaluator/source hashes. The common cohort signature is `f6c82cc9ab22131c838f7a2bce32acd6d687dc24e96dbf7c710d9ab98501c3e6`.

Evidence: [complete extracted JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_holdout_results_draft.json), [bundle 0](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/discovery_final_bundle.json), [bundle 1](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/discovery_final_bundle.json). This extraction checks JSON metadata and small report hashes; the allocated audits performed the raw coordinate-file checks. This metadata extraction does not replace the separately scheduled allocated final join or final resource audit. Validation, tests and diagnostics receive zero optimizer/exploration credit.

### Frozen state aliases

| Alias | Branch | Step | Representation | Pre-seed selection roles | Checkpoint |
|---|---|---:|---|---|---|
| E825 | E_barrier_control | 825 | regular_twofield | E_aggregate, E_axis | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/phase4_E_barrier_control/euler-discovery-NT-control-da6917be9ec5-6905651/E_barrier_control/step_0000825.pt) |
| S1195 | S_wide_Psi | 1195 | separate_psi | S_aggregate | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001195.pt) |
| S1344 | S_wide_Psi | 1344 | separate_psi | S_Omega | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001344.pt) |
| T0 | S_tail_delta_small | 0 | tailmatched | T_aggregate | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_tail_delta_small_clean/euler-discovery-S-tail-d4-clean-a54208a7154c-6908322/S_tail_delta_small/step_0000000.pt) |
| Q350 | S_hotspot_balanced | 350 | quartic | quartic_maximum | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_hotspot_balanced/euler-discovery-S-hotspots-059d98d5a500-6907718/S_hotspot_balanced/step_0000350.pt) |
| T102 | S_tail_delta_large | 102 | tailmatched | additional_all_regions_max_three | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_tail_delta_large/euler-discovery-S-tail-d2-1701382a0801-6908063/S_tail_delta_large/step_0000102.pt) |
| S915 | S_wide_Psi | 915 | separate_psi | additional_broad_RU_rms | [full state](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0000915.pt) |

T0 is the step 0 tailmatched initialization from S1195, using the fixed tail filter and translation. It is a parameterization warm start, not an additional optimized trajectory or a field-identity copy. Selection roles are pre-seed provenance and do not guarantee a final-cohort leader.

### Exact common cohort definitions

All reported norms are normalized sample RMS under the listed measure. Computational dxi deta, physical dr dz area, and cylindrical r dr dz volume remain distinct. Origin balls are centered at physical (r,z)=(0,0); their radius is explicit below. The SHA column shows a prefix; full coordinate hashes and paths are in the extracted JSON.

| Region | Count/state | Seed | Measure and fixed geometry | Coordinate SHA256 prefix |
|---|---:|---:|---|---|
| computational_domain | 1000000 | 123636364 | Uniform dxi deta on [0,30] x [-30,30]; physical r=sinh(xi),z=sinh(eta); metadata {"computational_bounds":[[0,30],[-30,30]]} | `50d2381331d629bc` |
| symmetry_axis | 65536 | 123636465 | Uniform deta on xi=0, eta in [-30,30] | `33de10921aa725b7` |
| farfield_computational | 65536 | 123636575 | Uniform dxi deta: xi in [10,30], 10<=\|eta\|<=30; common finite far-field cohort | `eeb7d89e480f2dfd` |
| narrow_core_computational | 65536 | 123636671 | Uniform dxi deta conditioned on physical 0<=r<=10,\|z\|<=6000; small-r diagnostic, not a required profile width; metadata {"physical_bounds":[[0,10.0],[-6000.0,6000.0]],"qualification":"Diagnostic region only; does not impose a solution scale."} | `ba455d779c3d52e0` |
| origin_ball_0p1_computational | 65536 | 123636765 | Uniform dxi deta conditioned on physical half-ball r>=0 about common physical origin; metadata {"center_r_z":[0.0,0.0],"physical_radius":0.1} | `e0335679defb4116` |
| origin_ball_0p1_physical_area | 65536 | 123636773 | Uniform physical dr dz area in half-disk r>=0; not cylindrical or computational measure; metadata {"center_r_z":[0.0,0.0],"physical_radius":0.1} | `45ab7d1472824f60` |
| origin_ball_1p0_computational | 65536 | 123636785 | Uniform dxi deta conditioned on physical half-ball r>=0 about common physical origin; metadata {"center_r_z":[0.0,0.0],"physical_radius":1.0} | `f6cb913333037795` |
| origin_ball_1p0_physical_area | 65536 | 123636793 | Uniform physical dr dz area in half-disk r>=0; not cylindrical or computational measure; metadata {"center_r_z":[0.0,0.0],"physical_radius":1.0} | `e67a4f7b48aa5f85` |
| origin_ball_10p0_computational | 65536 | 123636805 | Uniform dxi deta conditioned on physical half-ball r>=0 about common physical origin; metadata {"center_r_z":[0.0,0.0],"physical_radius":10.0} | `505876c73c9ce493` |
| origin_ball_10p0_physical_area | 65536 | 123636813 | Uniform physical dr dz area in half-disk r>=0; not cylindrical or computational measure; metadata {"center_r_z":[0.0,0.0],"physical_radius":10.0} | `7f5dcb7d0c121546` |
| near_axis_physical | 65536 | 123637665 | Uniform physical dr dz on [0,0.001] x [-10,10] | `f3cebb699c52c488` |
| core_physical_area | 65536 | 123637773 | Uniform physical dr dz on [0,1000] x [-6000,6000]; not cylindrical | `37041fd1c000ab0d` |
| outside_training_box | 65536 | 123637875 | Uniform dxi deta: xi in [30,40], eta in [-40,40]; extrapolation test | `55ec1fb73ddf8474` |
| active_core_physical_area | 65536 | 123637965 | Uniform physical dr dz on [0,100] x [-500,500]; fixed finite core view, not a boundary or localization constraint | `8c8a648c619546e6` |
| active_core_cylindrical_volume | 65536 | 123638073 | Uniform axisymmetric physical volume r dr dz on [0,100] x [-500,500], normalized; 2pi cancels | `51890971b673c772` |

### Full computational cohort: original equations and RU gradients

Each metric cell is **RMS / sampled maximum absolute value**. All base residuals are original and unscaled. The explicitly weighted r ROmega column is the physical angular-vorticity residual; the derivatives use physical r,z coordinates despite the computational sampling measure. Sampled maxima are not suprema.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000166038 / 0.00281174 | 0.000596664 / 0.022621 | 4.53608e-18 / 1.70477e-16 | 2.42e-05 / 0.000416566 | 7.55439e-06 / 0.000158159 | 0.0845412 / 3.5126 |
| S1195 | 0.000156163 / 0.0029355 | 0.000442477 / 0.0120877 | 4.37925e-18 / 1.69705e-16 | 1.31792e-05 / 0.000378645 | 5.06621e-06 / 0.00014897 | 0.0680116 / 1.7868 |
| S1344 | 0.000165145 / 0.00375171 | 0.00046248 / 0.0158209 | 4.34064e-18 / 1.55691e-16 | 1.73535e-05 / 0.000698879 | 5.44861e-06 / 0.000142469 | 0.0677403 / 2.05091 |
| T0 | 0.000159624 / 0.00283636 | 0.000442656 / 0.0120883 | 4.36161e-18 / 1.5374e-16 | 1.30761e-05 / 0.000377872 | 5.06848e-06 / 0.000149033 | 0.0680515 / 1.78747 |
| Q350 | 0.000155509 / 0.00395684 | 0.000434947 / 0.00990979 | 4.46311e-18 / 1.43169e-16 | 1.22789e-05 / 0.000317839 | 4.85367e-06 / 0.000126775 | 0.0772701 / 2.44957 |
| T102 | 0.000202541 / 0.0036914 | 0.00042059 / 0.00920524 | 4.38088e-18 / 1.59811e-16 | 1.44861e-05 / 0.000383398 | 5.69237e-06 / 0.000141329 | 0.0655261 / 1.8504 |
| S915 | 0.00012648 / 0.00335594 | 0.000509532 / 0.0141941 | 4.27449e-18 / 1.5704e-16 | 1.31069e-05 / 0.000387857 | 4.74854e-06 / 0.000117077 | 0.0689007 / 1.94392 |

### Sampled fields and free C

These field ranges combine sampled minima and maxima across the 15 common residual cohorts. They are finite sampled ranges, not global extrema. C remained free during optimization and was only read during validation. Per-region ranges, every residual maximum location, and diagnostic-window field extrema/locations are retained in JSON.

| State | C | U min | U max | Omega min | Omega max | Psi min | Psi max |
|---|---:|---:|---:|---:|---:|---:|---:|
| E825 | 0.131479 | -1.4821 | -8.77694e-32 | -0.00984755 | 0.0108906 | -55.3752 | 56.1121 |
| S1195 | -0.0251281 | -1.43706 | -1.37963e-31 | -0.00538599 | 0.00419897 | -67.8037 | 74.0827 |
| S1344 | -0.0313474 | -1.4485 | -1.26007e-31 | -0.00689849 | 0.00370954 | -71.2434 | 72.9069 |
| T0 | -0.0251281 | -1.43722 | -1.37963e-31 | -0.00538734 | 0.00420064 | -67.8147 | 74.0965 |
| Q350 | -0.0233981 | -1.43516 | -1.25792e-31 | -0.0046772 | 0.0043341 | -65.5883 | 77.8524 |
| T102 | -0.0239879 | -1.44525 | -1.34091e-31 | -0.00464415 | 0.00411158 | -64.5049 | 76.4243 |
| S915 | -0.0272897 | -1.43783 | -1.32732e-31 | -0.00581101 | 0.00485605 | -62.6042 | 73.8453 |

### All fourteen regional tables

Each cell is RMS / sampled maximum absolute value. This includes exact axis, near-axis, both active-core measures, the larger physical core, finite far field, outside-training extrapolation, narrow computational core, and each origin ball under both declared measures. No regions are pooled.

#### symmetry_axis

Uniform deta on xi=0, eta in [-30,30]. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000102461 / 0.000748782 | 5.35982e-05 / 0.000306388 | 9.58451e-18 / 1.33872e-16 | 0 / 0 | 4.78682e-06 / 3.53374e-05 | 0 / 0 |
| S1195 | 0.000140962 / 0.00128095 | 0.00029115 / 0.00198108 | 9.27331e-18 / 1.47777e-16 | 0 / 0 | 6.66818e-06 / 5.33587e-05 | 0 / 0 |
| S1344 | 0.000125277 / 0.000628663 | 0.000208165 / 0.00151291 | 9.38802e-18 / 1.56776e-16 | 0 / 0 | 7.08551e-06 / 2.98723e-05 | 0 / 0 |
| T0 | 0.000139624 / 0.00130748 | 0.000290613 / 0.00198252 | 9.09067e-18 / 1.47235e-16 | 0 / 0 | 6.71344e-06 / 5.52661e-05 | 0 / 0 |
| Q350 | 6.31502e-05 / 0.000390969 | 0.000164633 / 0.00139458 | 9.11503e-18 / 1.46903e-16 | 0 / 0 | 2.51562e-06 / 1.53532e-05 | 0 / 0 |
| T102 | 0.000129807 / 0.000849753 | 0.000222032 / 0.00149762 | 9.17023e-18 / 1.41597e-16 | 0 / 0 | 6.20428e-06 / 3.72865e-05 | 0 / 0 |
| S915 | 0.000111149 / 0.000801198 | 0.000197595 / 0.00103488 | 9.23479e-18 / 1.37216e-16 | 0 / 0 | 6.3077e-06 / 3.92233e-05 | 0 / 0 |

#### farfield_computational

Uniform dxi deta: xi in [10,30], 10<=|eta|<=30; common finite far-field cohort. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 2.57242e-11 / 1.37403e-09 | 4.05454e-12 / 5.32309e-10 | 3.3469e-25 / 2.89513e-23 | 6.89145e-15 / 4.93451e-13 | 2.79261e-15 / 2.26678e-13 | 5.37626e-08 / 5.87616e-06 |
| S1195 | 2.16905e-10 / 1.08867e-08 | 1.29016e-12 / 8.80612e-11 | 1.16499e-25 / 9.92617e-24 | 3.90576e-14 / 2.47372e-12 | 9.48073e-15 / 5.47958e-13 | 2.0742e-08 / 1.38742e-06 |
| S1344 | 2.26202e-10 / 1.09526e-08 | 1.41963e-12 / 9.59773e-11 | 1.53405e-25 / 1.32349e-23 | 4.30215e-14 / 2.44558e-12 | 7.38374e-15 / 5.08745e-13 | 2.13239e-08 / 1.39856e-06 |
| T0 | 2.16716e-10 / 1.08818e-08 | 1.28923e-12 / 8.81259e-11 | 1.43956e-25 / 1.32349e-23 | 3.9059e-14 / 2.47396e-12 | 9.47939e-15 / 5.48133e-13 | 2.07278e-08 / 1.38629e-06 |
| Q350 | 2.59693e-10 / 1.31222e-08 | 2.57547e-12 / 2.1724e-10 | 1.53536e-25 / 1.24077e-23 | 4.44985e-14 / 2.91496e-12 | 1.43505e-14 / 1.05236e-12 | 4.59314e-08 / 3.6063e-06 |
| T102 | 4.94708e-11 / 2.83881e-09 | 5.89584e-13 / 4.07672e-11 | 1.48627e-25 / 1.8198e-23 | 1.24755e-14 / 8.30595e-13 | 2.5171e-15 / 1.61457e-13 | 8.82195e-09 / 6.89864e-07 |
| S915 | 2.31868e-10 / 1.17228e-08 | 1.52789e-12 / 1.03799e-10 | 1.30213e-25 / 9.92617e-24 | 4.2258e-14 / 2.66005e-12 | 8.64198e-15 / 4.81825e-13 | 2.34085e-08 / 1.47638e-06 |

#### narrow_core_computational

Uniform dxi deta conditioned on physical 0<=r<=10,|z|<=6000; small-r diagnostic, not a required profile width; metadata {"physical_bounds":[[0,10.0],[-6000.0,6000.0]],"qualification":"Diagnostic region only; does not impose a solution scale."}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000463012 / 0.0020211 | 0.000425056 / 0.00301477 | 1.70394e-17 / 1.50128e-16 | 0.000109412 / 0.000292131 | 1.94862e-05 / 0.000131788 | 0.00321256 / 0.0301252 |
| S1195 | 0.000284653 / 0.00160157 | 0.00049502 / 0.00198085 | 1.63105e-17 / 1.45012e-16 | 4.62889e-05 / 0.000248337 | 1.22157e-05 / 6.54086e-05 | 0.00182871 / 0.0118505 |
| S1344 | 0.000285809 / 0.00313932 | 0.000357562 / 0.00151233 | 1.65838e-17 / 1.63931e-16 | 5.6236e-05 / 0.000452366 | 1.29607e-05 / 8.43708e-05 | 0.00138093 / 0.0099635 |
| T0 | 0.000280325 / 0.00162101 | 0.00049404 / 0.00198235 | 1.62372e-17 / 1.82634e-16 | 4.60995e-05 / 0.000247457 | 1.22743e-05 / 6.55489e-05 | 0.00182507 / 0.011859 |
| Q350 | 0.000210801 / 0.0012993 | 0.000274428 / 0.00139432 | 1.60735e-17 / 1.67875e-16 | 4.35153e-05 / 0.000187907 | 8.37126e-06 / 5.81706e-05 | 0.00100468 / 0.00759235 |
| T102 | 0.000273297 / 0.00152768 | 0.000379007 / 0.00149745 | 1.6348e-17 / 1.50704e-16 | 4.9866e-05 / 0.000187965 | 1.3283e-05 / 6.38993e-05 | 0.00138925 / 0.0107647 |
| S915 | 0.000198016 / 0.00178477 | 0.00034402 / 0.00103481 | 1.63011e-17 / 1.64917e-16 | 4.74424e-05 / 0.000324611 | 9.99989e-06 / 6.45056e-05 | 0.00133588 / 0.00928959 |

#### origin_ball_0p1_computational

Uniform dxi deta conditioned on physical half-ball r>=0 about common physical origin; metadata {"center_r_z":[0.0,0.0],"physical_radius":0.1}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 9.16672e-05 / 9.27579e-05 | 3.46963e-05 / 3.69988e-05 | 4.43297e-18 / 7.90654e-17 | 4.24749e-06 / 8.47421e-06 | 9.83478e-06 / 9.86083e-06 | 1.73745e-06 / 3.47839e-06 |
| S1195 | 0.000137621 / 0.000137745 | 0.000171405 / 0.000178991 | 4.4161e-18 / 2.7864e-17 | 6.57041e-07 / 1.31094e-06 | 1.05253e-06 / 1.13451e-06 | 8.58024e-06 / 1.71293e-05 |
| S1344 | 0.000184087 / 0.000185718 | 0.000181659 / 0.000186143 | 4.71645e-18 / 2.94903e-17 | 2.47464e-07 / 4.94468e-07 | 1.62017e-05 / 1.63096e-05 | 9.09415e-06 / 1.81343e-05 |
| T0 | 2.82444e-05 / 2.83437e-05 | 0.000171531 / 0.000179089 | 4.43406e-18 / 2.94361e-17 | 6.39378e-07 / 1.2757e-06 | 1.17133e-06 / 1.25328e-06 | 8.58655e-06 / 1.71417e-05 |
| Q350 | 5.71931e-05 / 5.74631e-05 | 9.1762e-05 / 9.40906e-05 | 4.38765e-18 / 2.83925e-17 | 5.8308e-07 / 1.16325e-06 | 2.56844e-06 / 2.61158e-06 | 4.59342e-06 / 9.17386e-06 |
| T102 | 8.60532e-06 / 9.04481e-06 | 2.81477e-05 / 3.32798e-05 | 4.57161e-18 / 2.76472e-17 | 6.7692e-07 / 1.35004e-06 | 4.60436e-06 / 4.61314e-06 | 1.40708e-06 / 2.84927e-06 |
| S915 | 0.000132438 / 0.000133582 | 1.70229e-05 / 2.15272e-05 | 4.39272e-18 / 3.24481e-17 | 4.10012e-07 / 8.17922e-07 | 1.14275e-05 / 1.1553e-05 | 8.49453e-07 / 1.74572e-06 |

#### origin_ball_0p1_physical_area

Uniform physical dr dz area in half-disk r>=0; not cylindrical or computational measure; metadata {"center_r_z":[0.0,0.0],"physical_radius":0.1}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 9.16686e-05 / 9.27584e-05 | 3.4694e-05 / 3.69974e-05 | 4.40937e-18 / 7.54198e-17 | 4.23676e-06 / 8.4822e-06 | 9.83481e-06 / 9.86084e-06 | 1.73306e-06 / 3.47608e-06 |
| S1195 | 0.000137621 / 0.000137746 | 0.000171397 / 0.000178987 | 4.41566e-18 / 2.86229e-17 | 6.55381e-07 / 1.31218e-06 | 1.05245e-06 / 1.13447e-06 | 8.55856e-06 / 1.71293e-05 |
| S1344 | 0.000184088 / 0.000185718 | 0.000181655 / 0.00018614 | 4.72613e-18 / 3.01408e-17 | 2.46839e-07 / 4.94275e-07 | 1.62018e-05 / 1.63096e-05 | 9.07118e-06 / 1.81596e-05 |
| T0 | 2.82444e-05 / 2.83438e-05 | 0.000171523 / 0.000179085 | 4.44518e-18 / 2.89482e-17 | 6.37763e-07 / 1.27691e-06 | 1.17125e-06 / 1.25324e-06 | 8.56486e-06 / 1.71419e-05 |
| Q350 | 5.71935e-05 / 5.74632e-05 | 9.17643e-05 / 9.40914e-05 | 4.38058e-18 / 2.90973e-17 | 5.81607e-07 / 1.16446e-06 | 2.56839e-06 / 2.61156e-06 | 4.58182e-06 / 9.17371e-06 |
| T102 | 8.6048e-06 / 9.04444e-06 | 2.8153e-05 / 3.32817e-05 | 4.60559e-18 / 2.9924e-17 | 6.7521e-07 / 1.35183e-06 | 4.60434e-06 / 4.61314e-06 | 1.40355e-06 / 2.85006e-06 |
| S915 | 0.000132437 / 0.000133582 | 1.70276e-05 / 2.15289e-05 | 4.40643e-18 / 2.92701e-17 | 4.08976e-07 / 8.1882e-07 | 1.14276e-05 / 1.1553e-05 | 8.47333e-07 / 1.74578e-06 |

#### origin_ball_1p0_computational

Uniform dxi deta conditioned on physical half-ball r>=0 about common physical origin; metadata {"center_r_z":[0.0,0.0],"physical_radius":1.0}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 8.27089e-05 / 0.000101702 | 3.83141e-05 / 5.85276e-05 | 3.0279e-17 / 1.71135e-16 | 4.06462e-05 / 8.3522e-05 | 9.74367e-06 / 1.00001e-05 | 1.90444e-05 / 4.73291e-05 |
| S1195 | 0.00013622 / 0.000139109 | 0.000175556 / 0.000247002 | 3.00686e-17 / 1.57426e-16 | 6.31961e-06 / 1.30659e-05 | 1.14471e-06 / 1.90866e-06 | 8.42838e-05 / 0.00018633 |
| S1344 | 0.000183775 / 0.000200812 | 0.000183133 / 0.000225603 | 3.03236e-17 / 1.89627e-16 | 2.40632e-06 / 5.20558e-06 | 1.60041e-05 / 1.72314e-05 | 8.84248e-05 / 0.000187984 |
| T0 | 2.96634e-05 / 3.46525e-05 | 0.000175646 / 0.000246832 | 3.01593e-17 / 1.62088e-16 | 6.14957e-06 / 1.27146e-05 | 1.25697e-06 / 2.02636e-06 | 8.43317e-05 / 0.000186352 |
| Q350 | 5.58282e-05 / 5.95403e-05 | 9.20507e-05 / 0.000115006 | 3.01842e-17 / 1.73222e-16 | 5.60796e-06 / 1.15983e-05 | 2.59177e-06 / 2.95858e-06 | 4.41595e-05 / 9.30256e-05 |
| T102 | 1.05586e-05 / 1.63071e-05 | 3.75757e-05 / 7.94661e-05 | 3.01757e-17 / 1.53198e-16 | 6.53192e-06 / 1.35845e-05 | 4.71659e-06 / 5.21563e-06 | 1.67792e-05 / 4.7161e-05 |
| S915 | 0.00013149 / 0.000143211 | 2.80428e-05 / 6.34416e-05 | 3.0163e-17 / 1.58388e-16 | 3.94079e-06 / 8.14766e-06 | 1.13955e-05 / 1.26185e-05 | 1.20163e-05 / 3.55198e-05 |

#### origin_ball_1p0_physical_area

Uniform physical dr dz area in half-disk r>=0; not cylindrical or computational measure; metadata {"center_r_z":[0.0,0.0],"physical_radius":1.0}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 8.2059e-05 / 0.000101699 | 3.85549e-05 / 5.85282e-05 | 3.12243e-17 / 1.83474e-16 | 4.20792e-05 / 8.35257e-05 | 9.7372e-06 / 1.00001e-05 | 1.98258e-05 / 4.73603e-05 |
| S1195 | 0.000136116 / 0.00013911 | 0.0001758 / 0.000247014 | 3.12547e-17 / 1.67238e-16 | 6.54342e-06 / 1.30667e-05 | 1.15035e-06 / 1.90869e-06 | 8.74039e-05 / 0.000186301 |
| S1344 | 0.000183754 / 0.000200801 | 0.000183219 / 0.000225609 | 3.17828e-17 / 1.65775e-16 | 2.49144e-06 / 5.20742e-06 | 1.599e-05 / 1.72308e-05 | 9.16285e-05 / 0.000188214 |
| T0 | 2.97677e-05 / 3.46523e-05 | 0.000175888 / 0.000246844 | 3.12303e-17 / 1.64365e-16 | 6.36734e-06 / 1.27152e-05 | 1.26223e-06 / 2.02639e-06 | 8.74526e-05 / 0.000186319 |
| Q350 | 5.57295e-05 / 5.95394e-05 | 9.2071e-05 / 0.000114992 | 3.12905e-17 / 1.64765e-16 | 5.80676e-06 / 1.16049e-05 | 2.59334e-06 / 2.9586e-06 | 4.57099e-05 / 9.3013e-05 |
| T102 | 1.06936e-05 / 1.6315e-05 | 3.81017e-05 / 7.94342e-05 | 3.14395e-17 / 1.67943e-16 | 6.76499e-06 / 1.35866e-05 | 4.72505e-06 / 5.21672e-06 | 1.7485e-05 / 4.71648e-05 |
| S915 | 0.000131418 / 0.000143218 | 2.86024e-05 / 6.34121e-05 | 3.12862e-17 / 1.66486e-16 | 4.08048e-06 / 8.15535e-06 | 1.13935e-05 / 1.26178e-05 | 1.25766e-05 / 3.55521e-05 |

#### origin_ball_10p0_computational

Uniform dxi deta conditioned on physical half-ball r>=0 about common physical origin; metadata {"center_r_z":[0.0,0.0],"physical_radius":10.0}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000621974 / 0.00181627 | 0.000349255 / 0.00173505 | 2.94991e-17 / 1.77331e-16 | 0.000168654 / 0.000286115 | 1.3241e-05 / 5.54534e-05 | 0.00226048 / 0.0144507 |
| S1195 | 0.000137109 / 0.000416151 | 0.000321689 / 0.000779187 | 2.93416e-17 / 1.67618e-16 | 4.09767e-05 / 9.39202e-05 | 5.49966e-06 / 2.46119e-05 | 0.00112756 / 0.0047125 |
| S1344 | 0.000174012 / 0.000378909 | 0.000247698 / 0.000480159 | 2.95939e-17 / 1.58944e-16 | 2.43261e-05 / 8.52268e-05 | 1.5186e-05 / 4.17232e-05 | 0.00101786 / 0.00386699 |
| T0 | 0.000158019 / 0.000566636 | 0.000320761 / 0.00077561 | 2.94503e-17 / 1.66913e-16 | 3.98054e-05 / 9.11561e-05 | 5.55068e-06 / 2.48067e-05 | 0.00112468 / 0.00469517 |
| Q350 | 0.000109095 / 0.000440483 | 0.000110967 / 0.000305131 | 2.91112e-17 / 1.4859e-16 | 3.62513e-05 / 8.63349e-05 | 5.05381e-06 / 2.15237e-05 | 0.000278467 / 0.00110935 |
| T102 | 0.000180075 / 0.000717612 | 0.000185329 / 0.000540764 | 2.94991e-17 / 1.67834e-16 | 5.07148e-05 / 0.000130851 | 1.296e-05 / 4.12131e-05 | 0.000547282 / 0.00237307 |
| S915 | 0.000109346 / 0.000196217 | 0.000165264 / 0.000450568 | 2.90838e-17 / 1.81597e-16 | 2.44205e-05 / 6.09205e-05 | 9.84442e-06 / 1.65127e-05 | 0.000494712 / 0.00206797 |

#### origin_ball_10p0_physical_area

Uniform physical dr dz area in half-disk r>=0; not cylindrical or computational measure; metadata {"center_r_z":[0.0,0.0],"physical_radius":10.0}. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000840464 / 0.00181578 | 0.000601526 / 0.0017421 | 2.78592e-17 / 1.79192e-16 | 0.00019779 / 0.000286119 | 2.09e-05 / 5.54958e-05 | 0.00401283 / 0.0144822 |
| S1195 | 0.000144378 / 0.000415889 | 0.00039442 / 0.000779499 | 2.51048e-17 / 1.5992e-16 | 5.22785e-05 / 9.39141e-05 | 8.9733e-06 / 2.48251e-05 | 0.00174503 / 0.0047302 |
| S1344 | 0.000166676 / 0.000378764 | 0.000283801 / 0.000480217 | 2.55757e-17 / 1.88217e-16 | 3.55882e-05 / 8.52321e-05 | 1.63756e-05 / 4.19054e-05 | 0.00143929 / 0.00386973 |
| T0 | 0.000209013 / 0.000566394 | 0.000393061 / 0.000775919 | 2.53427e-17 / 1.67834e-16 | 5.07417e-05 / 9.11483e-05 | 9.01755e-06 / 2.50228e-05 | 0.00173956 / 0.00471301 |
| Q350 | 0.000142831 / 0.000439766 | 0.000121919 / 0.000304981 | 2.50328e-17 / 1.45951e-16 | 4.61827e-05 / 8.63642e-05 | 7.08845e-06 / 2.15978e-05 | 0.00043143 / 0.00110987 |
| T102 | 0.000247682 / 0.000720126 | 0.000241436 / 0.000541238 | 2.538e-17 / 1.70437e-16 | 6.67312e-05 / 0.000131069 | 1.67431e-05 / 4.12316e-05 | 0.000951849 / 0.00238043 |
| S915 | 9.67719e-05 / 0.000196836 | 0.000216464 / 0.000450244 | 2.51676e-17 / 1.66622e-16 | 3.09592e-05 / 6.09484e-05 | 8.46467e-06 / 1.65126e-05 | 0.00086419 / 0.00207302 |

#### near_axis_physical

Uniform physical dr dz on [0,0.001] x [-10,10]. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000105381 / 0.000166228 | 0.000104284 / 0.000181473 | 2.46948e-17 / 1.4775e-16 | 4.46168e-08 / 8.51875e-08 | 7.5427e-06 / 1.00102e-05 | 6.05016e-08 / 1.81419e-07 |
| S1195 | 0.000150366 / 0.000190522 | 0.000438515 / 0.000779546 | 2.28804e-17 / 1.44416e-16 | 6.45273e-09 / 1.31437e-08 | 4.23036e-06 / 8.57259e-06 | 2.54124e-07 / 7.77584e-07 |
| S1344 | 0.000219654 / 0.000379091 | 0.000285295 / 0.000480232 | 2.30749e-17 / 1.60896e-16 | 5.86349e-09 / 1.61531e-08 | 1.60504e-05 / 2.07618e-05 | 1.65373e-07 / 4.79514e-07 |
| T0 | 2.16559e-05 / 2.90947e-05 | 0.000436938 / 0.000775966 | 2.28266e-17 / 1.60354e-16 | 6.25291e-09 / 1.27942e-08 | 4.2781e-06 / 8.67097e-06 | 2.5321e-07 / 7.74023e-07 |
| Q350 | 5.19369e-05 / 6.30779e-05 | 0.000157389 / 0.00030523 | 2.27251e-17 / 1.61316e-16 | 5.51629e-09 / 1.18068e-08 | 2.64029e-06 / 4.40677e-06 | 9.07353e-08 / 3.02771e-07 |
| T102 | 1.68745e-05 / 2.85772e-05 | 0.000286859 / 0.000541306 | 2.28865e-17 / 1.55041e-16 | 7.79905e-09 / 1.91555e-08 | 3.84369e-06 / 9.35323e-06 | 1.66133e-07 / 5.38697e-07 |
| S915 | 0.000128087 / 0.000175876 | 0.000255738 / 0.000450713 | 2.27963e-17 / 1.5355e-16 | 3.74045e-09 / 8.45215e-09 | 1.15971e-05 / 1.65129e-05 | 1.47874e-07 / 4.4601e-07 |

#### core_physical_area

Uniform physical dr dz on [0,1000] x [-6000,6000]; not cylindrical. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000120806 / 0.00281489 | 0.000625471 / 0.0221754 | 1.93871e-18 / 8.84709e-17 | 5.8852e-06 / 0.000416737 | 2.54268e-06 / 0.000136678 | 0.0946019 / 3.45911 |
| S1195 | 0.000155019 / 0.00243925 | 0.000600795 / 0.0119384 | 6.96457e-19 / 4.81386e-17 | 7.0517e-06 / 0.00024344 | 2.5493e-06 / 0.000148572 | 0.121452 / 1.78495 |
| S1344 | 0.000169277 / 0.00368584 | 0.000620608 / 0.0155229 | 6.72451e-19 / 4.91144e-17 | 9.79145e-06 / 0.000587283 | 2.64654e-06 / 0.000130385 | 0.118873 / 2.02943 |
| T0 | 0.000154682 / 0.00235311 | 0.000601033 / 0.0119343 | 8.36162e-19 / 6.13116e-17 | 7.04449e-06 / 0.000244801 | 2.54846e-06 / 0.000148653 | 0.121504 / 1.78564 |
| Q350 | 0.000162952 / 0.00379655 | 0.000610074 / 0.00953262 | 8.50643e-19 / 8.99346e-17 | 7.50884e-06 / 0.000266973 | 2.77329e-06 / 0.000109358 | 0.13554 / 2.44995 |
| T102 | 0.000172695 / 0.0033252 | 0.000563151 / 0.00918969 | 8.11979e-19 / 7.22621e-17 | 7.64809e-06 / 0.000382618 | 2.83767e-06 / 0.000129075 | 0.11838 / 1.85785 |
| S915 | 0.000163459 / 0.00333604 | 0.000658906 / 0.014017 | 7.73342e-19 / 7.53521e-17 | 7.53248e-06 / 0.000333498 | 2.52438e-06 / 0.000110616 | 0.116512 / 1.94324 |

#### outside_training_box

Uniform dxi deta: xi in [30,40], eta in [-40,40]; extrapolation test. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 1.69325e-36 / 2.84805e-35 | 1.16582e-46 / 8.9769e-45 | 1.05578e-39 / 5.61706e-38 | 8.30889e-49 / 1.53279e-47 | 1.47795e-48 / 1.57203e-47 | 7.22151e-34 / 5.0036e-32 |
| S1195 | 1.51885e-35 / 1.3281e-34 | 6.09404e-45 / 7.86054e-44 | 7.86225e-39 / 5.65498e-37 | 7.34939e-48 / 7.45373e-47 | 3.28804e-49 / 1.04992e-47 | 3.76086e-32 / 4.20452e-31 |
| S1344 | 1.4076e-35 / 1.22629e-34 | 5.24315e-45 / 5.79314e-44 | 7.32716e-39 / 4.09901e-37 | 6.81197e-48 / 6.88204e-47 | 1.6977e-49 / 8.80739e-48 | 3.23507e-32 / 3.09869e-31 |
| T0 | 1.64275e-39 / 3.14488e-38 | 2.8826e-50 / 1.36846e-48 | 8.13963e-39 / 4.61481e-37 | 7.96337e-52 / 2.06715e-50 | 2.61305e-53 / 1.01853e-51 | 1.90663e-37 / 7.45759e-36 |
| Q350 | 2.08195e-35 / 1.84236e-34 | 4.15762e-45 / 1.03356e-43 | 5.93044e-39 / 3.39891e-37 | 1.00739e-47 / 1.03231e-46 | 5.86329e-49 / 1.95679e-47 | 2.57028e-32 / 5.63255e-31 |
| T102 | 1.55863e-39 / 3.1498e-38 | 2.72944e-50 / 1.06911e-48 | 7.78642e-39 / 5.75245e-37 | 7.84959e-52 / 2.84529e-50 | 2.53928e-53 / 9.58697e-52 | 1.81265e-37 / 5.79912e-36 |
| S915 | 1.52089e-35 / 1.32693e-34 | 5.53936e-45 / 6.6478e-44 | 7.34596e-39 / 4.67041e-37 | 7.35828e-48 / 7.44744e-47 | 1.98616e-49 / 9.72602e-48 | 3.41864e-32 / 3.55584e-31 |

#### active_core_physical_area

Uniform physical dr dz on [0,100] x [-500,500]; fixed finite core view, not a boundary or localization constraint. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000982096 / 0.00281465 | 0.0020282 / 0.0123661 | 1.80311e-17 / 1.99927e-16 | 5.99995e-05 / 0.000416504 | 2.69043e-05 / 0.000158197 | 0.145569 / 1.23612 |
| S1195 | 0.000949186 / 0.00295426 | 0.00287858 / 0.0119075 | 4.12454e-18 / 9.67379e-17 | 7.03297e-05 / 0.000379269 | 2.28494e-05 / 0.000148823 | 0.212957 / 1.18672 |
| S1344 | 0.00109362 / 0.00375511 | 0.00282915 / 0.0151723 | 4.27944e-18 / 1.03758e-16 | 9.8762e-05 / 0.000706799 | 2.43062e-05 / 0.000143324 | 0.214482 / 1.51511 |
| T0 | 0.000940064 / 0.00285797 | 0.00287952 / 0.0119075 | 4.52089e-18 / 1.09992e-16 | 7.03184e-05 / 0.000378518 | 2.28367e-05 / 0.000148905 | 0.213028 / 1.18679 |
| Q350 | 0.00110391 / 0.0039559 | 0.00308234 / 0.00993806 | 4.44736e-18 / 1.11131e-16 | 7.48511e-05 / 0.00031742 | 2.50155e-05 / 0.00012658 | 0.219905 / 0.880128 |
| T102 | 0.00108648 / 0.00368976 | 0.00289274 / 0.00819107 | 4.4705e-18 / 9.25367e-17 | 7.01092e-05 / 0.000384264 | 2.65895e-05 / 0.000141365 | 0.2057 / 0.809213 |
| S915 | 0.00114918 / 0.00336996 | 0.00418582 / 0.0141959 | 4.21872e-18 / 1.22515e-16 | 7.85831e-05 / 0.000390327 | 2.41511e-05 / 0.000116988 | 0.306705 / 1.36688 |

#### active_core_cylindrical_volume

Uniform axisymmetric physical volume r dr dz on [0,100] x [-500,500], normalized; 2pi cancels. Count 65536 per state.

| State | RU | ROmega | RPsi | d_r RU | d_z RU | r ROmega |
|---|---:|---:|---:|---:|---:|---:|
| E825 | 0.000951742 / 0.00281794 | 0.00233828 / 0.0123671 | 1.52823e-17 / 1.34441e-16 | 4.88125e-05 / 0.000416223 | 2.24776e-05 / 0.000158162 | 0.184317 / 1.23639 |
| S1195 | 0.000937066 / 0.00294643 | 0.00341894 / 0.0119171 | 4.24983e-18 / 1.17094e-16 | 5.66638e-05 / 0.000378085 | 1.99574e-05 / 0.000148324 | 0.269622 / 1.18938 |
| S1344 | 0.00104906 / 0.00375076 | 0.00339315 / 0.0151867 | 4.36887e-18 / 1.41055e-16 | 7.61028e-05 / 0.000698437 | 2.05724e-05 / 0.000142709 | 0.273186 / 1.51805 |
| T0 | 0.000932924 / 0.00285454 | 0.00342005 / 0.0119164 | 4.39798e-18 / 1.13516e-16 | 5.65859e-05 / 0.000377333 | 1.99549e-05 / 0.000148367 | 0.269712 / 1.18928 |
| Q350 | 0.00116232 / 0.00395708 | 0.00359468 / 0.00994909 | 4.35857e-18 / 1.28532e-16 | 6.99244e-05 / 0.000316603 | 2.43446e-05 / 0.000126679 | 0.2751 / 0.884713 |
| T102 | 0.00112071 / 0.00368634 | 0.00336799 / 0.00819143 | 4.52922e-18 / 1.42518e-16 | 5.9512e-05 / 0.000383579 | 2.41913e-05 / 0.000141058 | 0.257685 / 0.807648 |
| S915 | 0.00120178 / 0.00337039 | 0.00496972 / 0.0141932 | 4.37715e-18 / 1.14925e-16 | 6.65097e-05 / 0.000390781 | 2.249e-05 / 0.000116062 | 0.387172 / 1.36623 |

### Metric-specific leaders among the seven audited states

These rankings apply only to the seven states actually evaluated on the final common cohorts. RPsi roundoff ordering is not used to promote a candidate. No joint leader is implied by winning one row. Exact numeric ties are retained; no tolerance was chosen after seeing final data.

| Cohort | Metric | State | Value |
|---|---|---|---:|
| computational_domain | Three-base sum of squared RMS | Q350 | 2.133614261390181e-7 |
| All 15 declared cohorts | Largest sampled absolute original base residual | T102 | 0.009205240077912749 |
| computational_domain | RU rms | S915 | 0.00012648 |
| computational_domain | ROmega rms | T102 | 0.00042059 |
| computational_domain | RU sampled_max_abs | E825 | 0.00281174 |
| computational_domain | ROmega sampled_max_abs | T102 | 0.00920524 |
| computational_domain | d_rRU rms | Q350 | 1.22789e-05 |
| computational_domain | d_zRU rms | S915 | 4.74854e-06 |
| computational_domain | rROmega rms | T102 | 0.0655261 |
| computational_domain | rROmega sampled_max_abs | S1195 | 1.7868 |
| symmetry_axis | RU rms | Q350 | 6.31502e-05 |
| symmetry_axis | ROmega rms | E825 | 5.35982e-05 |
| symmetry_axis | ROmega sampled_max_abs | E825 | 0.000306388 |
| near_axis_physical | ROmega rms | E825 | 0.000104284 |
| active_core_physical_area | RU rms | T0 | 0.000940064 |
| active_core_physical_area | ROmega rms | E825 | 0.0020282 |
| active_core_cylindrical_volume | rROmega rms | E825 | 0.184317 |
| active_core_cylindrical_volume | rROmega sampled_max_abs | T102 | 0.807648 |

The full-computational three-base aggregate is the sum of the three unscaled RMS squares, not a physical energy or a gauge-invariant accuracy norm. Q350's value is2.133614261390181e-7 versus T102's2.179188193741154e-7. The all-cohort minimax row ranges over the three original base residuals and all 15 fixed cohorts, among these seven states only. Its largest surviving value is T102 R_Ω=.009205240077912749 in the computational cohort at (r,z)=(186.29629706160748,−131.76843672510478). It is a sampled maximum, not a global supremum.

### Ranking reversals and regional tradeoffs

S1344 carried the pre-seed S_Omega selection role, but its fresh computational ROmega RMS is 0.00046248 versus S1195 0.000442477; its ROmega maximum is 0.0158209 versus 0.0120877. The selection ranking therefore does not transfer uniformly to the new cohort. This is an observed finite-cohort comparison, not a statistical significance claim.

Q350 reduces the computational unweighted ROmega maximum to 0.00990979 from S1195 0.0120877 while the computational r ROmega maximum rises to 2.44957 from 1.7868. Its max-control benefit depends on which residual and measure is evaluated. The full regional tables show the corresponding physical-core and axis tradeoffs.

Near-roundoff RPsi reflects the structural U/Psi-to-Omega relation checked by the independent physical evaluator. It does not certify either nonlinear transport equation. No single scalar or pre-seed role substitutes for the regional and weighted comparisons above.

### Diagnostic plots and restart artifacts

All five diagnostic views per state completed with field/residual plots, streamline plots and saved numerical arrays. Their window count totals 1,160,355 across the seven states, separately from the common residual-cohort evaluation count. Saved radial rays, fixed-r axial rays and axis-regularity arrays also exist. Finite windows/rays are diagnostics, not global decay or smoothness proofs.

- E825: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/diagnostics.json).
- S1195: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/diagnostics.json).
- S1344: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/diagnostics.json).
- T0: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/diagnostics.json).
- Q350: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/diagnostics.json).
- T102: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/diagnostics.json).
- S915: [validation JSON](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/validation.json), [core fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/core.png), [near-axis fields/residuals](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/near_axis.png), [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/core_streamlines.png), [far-field view](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/farfield.png), [all diagnostic metadata](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/diagnostics.json).

### Execution scope and limitations

Original GPU attempts 6909214/6909216 passed StageB but failed the production output guard because the central .resnick-owner.json already occupied the default output root. The saved seed was parsed, but the guard preceded the 215-test suite, region construction, and any final coordinate generation/evaluation. Replacement 6909285/6909287 changed only the command-level /audit output path; source, seed, protocol, checkpoints and cohort definitions stayed frozen. Failed allocations remain resource costs and receive zero optimizer credit.

All results concern finite domains, fixed measures, sampled maxima, finite diagnostic grids/rays and floating-point evaluation of seven preselected states. They do not establish an exact Euler solution, global decay, global smoothness or nontriviality. Geometry, actual multiprecision checks, asymptotic coefficients and final resource accounting are separate evidence. No final holdout result was used to resume training.


## E. Profile plots

Every primary state has five 129×257 raw-field/residual grids (129 radial and 257 axial nodes): physical core, near axis, broad physical domain, computational domain and far field. Each displays U, Ω, Ψ and all three original residuals with its own labeled colorbar. Companion streamline panels separately show physical meridional velocity and self-similar profile transport. The following links give the actual durable images; diagnostic directories also contain PDF versions and the underlying NPZ arrays. No plot, streamline or targeted grid adds to the 1,917,504-point RMS cohort or optimizer clock.


| State | Core | Near axis | Broad | Computational | Far field | Physical velocity / transport | Raw arrays |
|---|---|---|---|---|---|---|---|
| [E825](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/phase4_E_barrier_control/euler-discovery-NT-control-da6917be9ec5-6905651/E_barrier_control/step_0000825.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/E_barrier_control_step_0000825_2c4ab4e1/candidate/diagnostics/core.npz) |
| [S1195](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001195.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/core.npz) |
| [S1344](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001344.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0001344_df6ab062/candidate/diagnostics/core.npz) |
| [T0](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_tail_delta_small_clean/euler-discovery-S-tail-d4-clean-a54208a7154c-6908322/S_tail_delta_small/step_0000000.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_small_step_0000000_b223b140/candidate/diagnostics/core.npz) |
| [Q350](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_hotspot_balanced/euler-discovery-S-hotspots-059d98d5a500-6907718/S_hotspot_balanced/step_0000350.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_hotspot_balanced_step_0000350_c94e0033/candidate/diagnostics/core.npz) |
| [T102](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_tail_delta_large/euler-discovery-S-tail-d2-1701382a0801-6908063/S_tail_delta_large/step_0000102.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_tail_delta_large_step_0000102_eee10df4/candidate/diagnostics/core.npz) |
| [S915](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0000915.pt) | [core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/core.png) | [near_axis](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/near_axis.png) | [broad](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/broad.png) | [computational](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/computational.png) | [farfield](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/farfield.png) | [core streamlines](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/core_streamlines.png) | [core NPZ](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu0/euler-final-gpu0-audit-58b3ec171b29-6909285/audit/S_wide_Psi_step_0000915_beab1256/candidate/diagnostics/core.npz) |


![S1195 original fields and residuals in the physical core](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_gpu1/euler-final-gpu1-audit-a72ce6f9a9f3-6909287/audit/S_wide_Psi_step_0001195_dca8c1f8/candidate/diagnostics/core.png)

Representative core, broad, axis, far-field and streamline images were actually opened and inspected, including E825, S1195 and a tail-matched state. The core images show a narrow U core with much wider signed Ω and Ψ lobes; the R_Ω lobes remain visible outside the main U core. Near-axis fields are visually smooth at this display resolution. Poisson panels fluctuate on about 10^-16 scales and must be read with their colorbars; that texture is consistent with algebraic closure/roundoff. Broad views can hide narrow core features. Far-field panels use the explicitly labeled computational coordinates ξ,η and tiny raw scales. Streamline spacing is a plotting choice, not a velocity norm or topological certificate. The physical and transport panels differ, as required by their definitions.

The [complete file-format/hash inventory](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_artifact_inventory.json) and [visual inspection record](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/visual_inspection_final.json) identify the actual reviewed artifacts. The plots do not establish that all possible thin residual layers are resolved. The independent random cohorts, physical derivatives, width refinement and MP points provide complementary finite evidence.


## F. Physical interpretation, localization, tails and precision

The physical velocity and vorticity reconstructed from these reduced fields are

\[
v=(-r\Psi_z,\ rU,\ 2\Psi+r\Psi_r),\qquad
\omega=(-rU_z,\ r\Omega,\ 2U+rU_r).
\]

Reduced-field decay alone would be insufficient to establish physical velocity decay. The compact regular heads impose the explicit test family U=O(R^-2), Ω=O(R^-3), Ψ=O(R^-1), with bounded smooth compact heads and corresponding differentiated orders. This gives physical velocity O(R^-1) and vorticity O(R^-2). It is a restriction of the search, not a theorem that all admissible Euler profiles must have those exponents; no global finite-energy condition is imposed. For the frozen states, finite radial-ray and fixed-r axial-tail scans and high-precision coefficients supplement this analytical representation property. The outer finite-ray velocity values near 10^-15 are only observations at the saved very large radii.

### Own-field geometry and the coupled obstruction

Seven states have the final RMS audit. The two additional paired final iterates below receive targeted geometry/precision comparisons only. They are not extra final-holdout candidates. Peaks are bounded-search stationary candidates, not certified global extrema. A radial connected half-amplitude interval at r=0 is one-sided on r≥0 and is not doubled; axial spans are full connected half-amplitude widths. The90 underlying field/direction/lobe spans are reported at 257 and 513 resolutions, giving180 width estimates. All crossings were found; the largest relative refinement change is.001505. This supports stability of those field spans, not a global support bound or resolution certificate for every residual layer.

| State | C | U peak | U width r/z (513) | Psi width r/z (513) | Omega width r/z (513) | Status |
|---|---:|---:|---|---|---|---|
| E_barrier_control_step_0000825_2c4ab4e1 | 0.131479 | -1.4821 | 37.4583/415.624 | 321.71/654.243 | 91.3778/186.136 | COMPLETED |
| S_wide_Psi_step_0001195_dca8c1f8 | -0.0251281 | -1.43706 | 40.9241/547.105 | 628.532/629.048 | 224.763/203.671 | COMPLETED |
| S_wide_Psi_step_0001344_df6ab062 | -0.0313474 | -1.4485 | 39.8829/551.317 | 661.02/663.608 | 158.729/176.428 | COMPLETED |
| S_tail_delta_small_step_0000000_b223b140 | -0.0251281 | -1.43722 | 40.9231/547.119 | 628.495/628.934 | 224.794/203.712 | COMPLETED |
| S_hotspot_balanced_step_0000350_c94e0033 | -0.0233981 | -1.43516 | 40.1823/553.675 | 650.949/622.947 | 303.428/202.493 | COMPLETED |
| S_tail_delta_large_step_0000102_eee10df4 | -0.0239879 | -1.44525 | 40.2985/536.823 | 623.633/629.423 | 270.857/241.851 | COMPLETED |
| S_wide_Psi_step_0000915_beab1256 | -0.0272897 | -1.43783 | 39.1738/535.45 | 577.523/580.4 | 203.307/188.508 | COMPLETED |
| paired_small_delta_final | -0.0243106 | -1.44249 | 40.2935/537.023 | 626.88/634.941 | 236.336/228.946 | COMPLETED |
| paired_large_delta_final | -0.0239969 | -1.44265 | 40.2406/537.459 | 626.774/633.155 | 272.038/242.426 | COMPLETED |

At each nonzero stationary U extremum, the exact equation requires Psi_z=1/2; the table below reports finite defects rather than enforcing that shape. Omega own extrema test its separate transport/coupling balance. Widths are connected half-amplitude intervals at each field's own peak on physical r>=0: an interval ending at the axis is one-sided and is not doubled. Censored intervals remain censored, not zero.

| State | U-peak Psi_z−1/2 | U-peak RU | Omega-peak ROmega | Omega-peak rROmega | 2UUz/(1.5Omega) at Omega peak | Outer finite-ray max velocity |
|---|---:|---:|---:|---:|---:|---:|
| E_barrier_control_step_0000825_2c4ab4e1 | -3.59626e-05 | -0.0001066 | 0.0163797 | 2.61489 | 5.81313e-05 | 4.91922e-16 |
| S_wide_Psi_step_0001195_dca8c1f8 | -6.27465e-05 | -0.00018034 | -0.00808202 | -1.29473 | -7.83521e-05 | 8.51559e-16 |
| S_wide_Psi_step_0001344_df6ab062 | 9.52025e-06 | 2.75803e-05 | -0.0103529 | -1.41737 | -1.89367e-05 | 8.92233e-16 |
| S_tail_delta_small_step_0000000_b223b140 | -5.26469e-06 | -1.5133e-05 | -0.00808395 | -1.29539 | -7.82098e-05 | 8.51559e-16 |
| S_hotspot_balanced_step_0000350_c94e0033 | -1.99613e-05 | -5.72953e-05 | -0.00701805 | -1.17372 | -0.000153545 | 7.07868e-16 |
| S_tail_delta_large_step_0000102_eee10df4 | 5.47733e-05 | 0.000158322 | -0.00697397 | -1.32885 | -5.29174e-05 | 8.39688e-16 |
| S_wide_Psi_step_0000915_beab1256 | -4.23353e-05 | -0.000121742 | -0.00872234 | -1.09852 | -0.000397265 | 7.60338e-16 |
| paired_small_delta_final | -7.82038e-05 | -0.000225617 | -0.00746051 | -1.40339 | -3.2419e-05 | 8.37622e-16 |
| paired_large_delta_final | -7.57595e-05 | -0.000218589 | -0.00701734 | -1.33445 | -4.33884e-05 | 8.36173e-16 |

Omega own-extremum balance retains the actual gradients; it does not assume the optimizer made them exactly zero. At an exact stationary Omega point the necessary relation is 1.5Omega=2UUz. These are reduced-Omega extrema, not certified maxima of physical rOmega.

| State / lobe | (r,z) | Stationary flag / grad(r,z) | A Omega_r+B Omega_z | 1.5Omega | 2UUz | ROmega | rROmega | abs(U)/Upeak; abs(Psi)/Psipeak |
|---|---|---|---:|---:|---:|---:|---:|---|
| E_barrier_control_step_0000825_2c4ab4e1 / 1 | (159.642,92.2992) | True / (-2.68103e-15,-3.67713e-15) | -5.27363e-13 | 0.0163807 | 9.5223e-07 | 0.0163797 | 2.61489 | 0.0336857; 0.774628 |
| E_barrier_control_step_0000825_2c4ab4e1 / 2 | (154.159,-74.5942) | True / (-1.60392e-13,-5.50636e-14) | 1.83002e-12 | -0.0147724 | -1.32434e-06 | -0.0147711 | -2.2771 | 0.0371889; 0.684716 |
| S_wide_Psi_step_0001195_dca8c1f8 / 1 | (160.199,-129.956) | True / (-1.93965e-15,-1.64513e-15) | 1.97777e-13 | -0.00808138 | 6.33194e-07 | -0.00808202 | -1.29473 | 0.0480383; 0.761159 |
| S_wide_Psi_step_0001195_dca8c1f8 / 2 | (166.162,185.712) | True / (6.0949e-18,-2.146e-17) | -4.48535e-15 | 0.00629977 | -5.75087e-07 | 0.00630035 | 1.04688 | 0.0450339; 0.926793 |
| S_wide_Psi_step_0001344_df6ab062 / 1 | (136.906,-106.784) | True / (9.70408e-16,5.85368e-16) | -6.57538e-14 | -0.0103527 | 1.96047e-07 | -0.0103529 | -1.41737 | 0.0597789; 0.748206 |
| S_wide_Psi_step_0001344_df6ab062 / 2 | (0,-234.395) | True / (0,2.68159e-17) | -6.78105e-15 | 0.00550022 | 0.00553508 | -3.48605e-05 | -0 | 0.563516; 0.929871 |
| S_tail_delta_small_step_0000000_b223b140 / 1 | (160.242,-129.96) | True / (-9.71524e-16,-7.98703e-16) | 9.48153e-14 | -0.00808332 | 6.32194e-07 | -0.00808395 | -1.29539 | 0.0480077; 0.761304 |
| S_tail_delta_small_step_0000000_b223b140 / 2 | (166.191,185.754) | True / (7.32882e-18,-2.61871e-17) | -5.48053e-15 | 0.00630228 | -5.74776e-07 | 0.00630286 | 1.04748 | 0.0450143; 0.926804 |
| S_hotspot_balanced_step_0000350_c94e0033 / 1 | (167.243,-94.6487) | True / (3.98376e-17,-1.92482e-17) | 3.44767e-15 | -0.00701697 | 1.07742e-06 | -0.00701805 | -1.17372 | 0.0390911; 0.553143 |
| S_hotspot_balanced_step_0000350_c94e0033 / 2 | (251.806,146.925) | True / (-3.47855e-13,-6.04397e-13) | -1.37593e-10 | 0.00650252 | -4.73512e-08 | 0.00650257 | 1.63739 | 0.0180518; 0.833286 |
| S_tail_delta_large_step_0000102_eee10df4 / 1 | (190.544,-159.967) | True / (1.29735e-13,9.81733e-14) | -1.01431e-11 | -0.0069736 | 3.69025e-07 | -0.00697397 | -1.32885 | 0.0325636; 0.727461 |
| S_tail_delta_large_step_0000102_eee10df4 / 2 | (0,-182.315) | True / (0,4.49344e-16) | -9.23939e-14 | 0.00616738 | 0.0071086 | -0.000941226 | -0 | 0.665148; 0.748575 |
| S_wide_Psi_step_0000915_beab1256 / 1 | (125.943,-113.383) | True / (-7.16742e-20,2.52981e-19) | -3.89511e-17 | -0.00871888 | 3.46371e-06 | -0.00872234 | -1.09852 | 0.0718443; 0.654168 |
| S_wide_Psi_step_0000915_beab1256 / 2 | (133.653,167.2) | True / (-1.53869e-14,-1.16678e-13) | -2.60886e-11 | 0.00728536 | -2.30991e-06 | 0.00728767 | 0.974021 | 0.0646555; 0.931684 |
| paired_small_delta_final / 1 | (188.109,-157.323) | True / (-6.52786e-14,-5.74812e-14) | 6.74963e-12 | -0.00746027 | 2.41854e-07 | -0.00746051 | -1.40339 | 0.0335417; 0.746045 |
| paired_small_delta_final / 2 | (0,-183.303) | True / (0,1.224e-15) | -2.53939e-13 | 0.00627638 | 0.00714936 | -0.000872987 | -0 | 0.667218; 0.761349 |
| paired_large_delta_final / 1 | (190.165,-159.629) | True / (6.01914e-14,3.74326e-14) | -3.27734e-12 | -0.00701704 | 3.04458e-07 | -0.00701734 | -1.33445 | 0.0327202; 0.730016 |
| paired_large_delta_final / 2 | (0,-179.884) | True / (0,2.67679e-13) | -5.4698e-11 | 0.00642955 | 0.00726093 | -0.000831378 | -0 | 0.675515; 0.74841 |

The fixed active cylindrical core ends at r=100, so it does not cover an extremum at r about 126–191. The already declared broader physical-core cohort extends to r=1000 and remains a separate common measure. No cohort is changed here. Broader Psi/Omega lobes can reduce unweighted Omega/ROmega magnitudes; the observed rROmega values and local coupling balance must be reported alongside that gain. The data alone do not establish its cause.

MP counters are preserved as (unexpected jets, residual disagreements, FP64 nonfinite); passing arithmetic agreement does not make a nonzero PDE residual small.

| State | MP60 points / counters | All-point MP80 points / counters | Tail MP |
|---|---|---|---|
| E_barrier_control_step_0000825_2c4ab4e1 | 6 / 0,0,0 | 9 / 0,0,0 | not applicable |
| S_wide_Psi_step_0001195_dca8c1f8 | 6 / 0,0,0 | 9 / 0,0,0 | not applicable |
| S_wide_Psi_step_0001344_df6ab062 | 6 / 0,0,0 | 9 / 0,0,0 | not applicable |
| S_tail_delta_small_step_0000000_b223b140 | 6 / 0,0,0 | 9 / 0,0,0 | 6 MP60 +2 MP80; actual shell coefficients and reference drift saved in JSON |
| S_hotspot_balanced_step_0000350_c94e0033 | 6 / 0,0,0 | 9 / 0,0,0 | not applicable |
| S_tail_delta_large_step_0000102_eee10df4 | 6 / 0,0,0 | 9 / 0,0,0 | 6 MP60 +2 MP80; actual shell coefficients and reference drift saved in JSON |
| S_wide_Psi_step_0000915_beab1256 | 6 / 0,0,0 | 9 / 0,0,0 | not applicable |
| paired_small_delta_final | 6 / 0,0,0 | 9 / 0,0,0 | 6 MP60 +2 MP80; actual shell coefficients and reference drift saved in JSON |
| paired_large_delta_final | 6 / 0,0,0 | 9 / 0,0,0 | 6 MP60 +2 MP80; actual shell coefficients and reference drift saved in JSON |

Actual MP tail coefficients (targeted saved points, not RMS or amplitude criteria):

| State | Delta | Shell MP R4RU | Shell MP R5ROmega | Max relative MP60→80 coefficient drift | Max R≈1e10 FP64 coefficient error RU / RO |
|---|---:|---:|---:|---:|---|
| S_tail_delta_small_step_0000000_b223b140 | 0.0001 | -1.89362e+12 | 6.02266e+13 | 9.9359e-36 | 0.00312559 / 0.00154831 |
| S_tail_delta_large_step_0000102_eee10df4 | 0.01 | -1.82927e+10 | 5.40574e+11 | 7.09837e-35 | 0.597747 / 0.148511 |
| paired_small_delta_final | 0.0001 | -2.06732e+12 | 6.18439e+13 | 1.27087e-35 | 0.000846145 / 0.00134489 |
| paired_large_delta_final | 0.01 | -1.84277e+10 | 5.43452e+11 | 6.58202e-34 | 0.578775 / 0.05548 |

Shell maxima are selected at each model's declared transition and can occur at different physical radii/directions. Compare the preserved coordinates, δsqrt(q) range and term-relative defects; large dimensional coefficients alone are not rejection criteria. Nonzero stable coefficients show unresolved higher-order transport balance even when the imposed critical powers and physical velocity decay hold. Outermost FP64 subleading rescalings are not accepted as asymptotic certificates.

No retained state has convincing simultaneous pointwise transport balance at its dominant off-axis Omega stationary candidate: its term-relative defect remains near one. This is failure of these approximate fields, not a mathematical nonexistence claim. The GPU cohort audit and its measure-specific leader scopes remain separate.

Seven PRIMARY_FINAL_HOLDOUT states retain their frozen GPU-audit roles. The two PAIRED_DELTA_FINAL_TARGETED_ONLY states add no final RMS evaluation or leader label. Source widths/C values are not amplitude or published-shape acceptance rules. Finite rays do not certify uniform decay; subleading outer FP64 powers can magnify cancellation, so intermediate-shell MP values/reference stability take precedence. Gamma quadrature closure and the signed integrated PDE defect are stored separately in JSON.

Detailed extrema coordinates, boundary/stationarity flags, both 257/513 width estimates, censoring/refinement, transport roots and original residuals, anglewise physical tails, signed Gamma flux, MP residual values and 60→80 reference drift are preserved in the JSON draft with raw-report paths/hashes.

Completion evidence: CPU job 6909289 exited 0; scheduler walltime 32:25, maximum RSS 1.70 GB. The application recorded 1931.339 seconds. All 215 tests passed in 68.895 seconds. Frozen source, checkpoints and seed remained unchanged; no scientific rerun or training occurred.

Targeted MP comparisons: 54 geometry points at 60 digits, 81 at 80 digits (all 54 original points retained plus axis companions), 9 legacy single-point 80-digit repeats, and 24 tail 60-digit / 8 tail 80-digit comparisons. All five aggregate disagreement/nonfinite counters are zero. These 176 reported comparisons include repeats and add zero RMS/optimizer credit.

Largest absolute MP60→MP80 reference drift on common geometry points: RU1.3883048987466041108614E-61, ROmega1.9304625495470788117884032E-58, RPsi6.07716335728627119840346528287752469437397394221065153429349351832493849130874563090841434E-64. Maximum relative tail-coefficient reference drift is6.58202e-34. Agreement confirms the observed residual values, including their nonzero coupling defects; it does not certify an exact Euler solution.



At the dominant off-axis Ω candidates, actual Ω advection is at most1.02×10^-11, while |2UU_z/(1.5Ω)|≤3.973×10^-4. The minimum |R_Ω| divided by the sum of absolute original-equation terms is.9998837. Eight of nine dominant candidates have opposite signs of source and linear term. Their r positions span125.943–190.544, outside the fixed weighted core r≤100. These are the strongest local defects, even where a bounded-core weighted RMS is smaller. Some secondary axis lobes do balance: S1344 at (0,−234.395) has1.5Ω=.005500216 and 2UU_z=.005535077, leaving R_Ω≈−3.486×10^-5. The conclusion concerns the dominant off-axis lobes, not every extremum. Q350's second lobe has |rR_Ω|≈1.637, larger than its dominant reduced-Ω lobe's1.174; Ω extrema are not automatically extrema of physical rΩ or residual suprema.

At an exact nonzero U stationary point, the necessary relation Ψ_z=1/2 is generally matched to about 10^-4 here. This local condition is insufficient: the wider Ω lobes sit where U is only a few percent of its own peak, leaving inadequate swirl coupling. Broader Ω lobes can accompany smaller reduced Ω/R_Ω values without improving rR_Ω. The measurements do not establish a causal theorem that broadening produced the apparent gains.

The dimensionless source/linear ratio and rR_Ω at corresponding points are invariant under the true isotropic length symmetry and axial translation; flipping U leaves UU_z unchanged. Thus those simple gauge changes cannot repair the observed coupling defect. No published parity, amplitude, shape or fixed-point condition is used in this diagnosis. Meridional transport roots and signed fluxes are saved as diagnostics, not admission targets or stability tests.

### Far-field admissibility and precision limits

For Γ=r²U, the original equation gives (A,B)·∇Γ=r²R_U and ∇·[r(A,B)]=3r/2. Under compact-level-set/integrability hypotheses, the associated flux identity obstructs a nonzero exact profile with uniformly vanishing Γ at infinity. This motivates avoiding an unexamined Gaussian or faster-decay requirement; it does not prove nonexistence for the original target class. The compact critical ansatz allows nonzero angular limits of r²U.

In the original compact wrapper, even inverse-radius corrections generically leave uncancelled C U_z and C Ω_z subleading terms when C≠0. The earlier independent three-field Ω also lacks the leading angular Poisson balance. The tail-matched representation uses Z=z+2C and filters the inverse-root feature with φ_δ(t)=t²/(sqrt(t²+δ²)+δ), with both tested δ values explicitly labeled. In this restricted family the parity gives R_U=O(R^-4) and R_Ω=O(R^-5). It removes the tested lower-order mismatch, while the next coefficients and the transition near scale L/δ remain nonzero. Neither translation-plus-filtering nor its warm start is an exact identity of the original field.

Across the nine targeted states there are 54 MP60 geometry evaluations,81 all-point MP80 evaluations including axis companions,9 additional legacy single-point MP80 repeats,24 tail MP60 evaluations and 8 tail MP80 repeats:176 targeted point-evaluations, each with multiple jets/operators. All saved unexpected-jet, residual-disagreement, FP64-nonfinite and related counters are zero. The maximum absolute MP60→80 drift in the geometry residual references is1.39×10^-61 for R_U,1.93×10^-58 for R_Ω and 6.08×10^-64 for R_Ψ. These arithmetic checks reproduce the nonzero defects; they do not certify small PDE error.

The four tail helpers have relative MP60→80 coefficient drift at most6.59×10^-34, confirming genuine nonzero finite-ray higher coefficients. Raw FP64 absolute-tolerance passes still conceal sizeable relative error after multiplying very small residuals by R^4 or R^5: at R≈10^10 the large-δ primary has about 59.8% RU-coefficient error and 14.9% Ω-coefficient error; its final sibling has57.9% and 5.55%. Thus MP references, original term magnitudes and saved physical coordinates are essential. Large dimensionful coefficients alone are not a gauge-independent rejection criterion, and different δ shell maxima occur at different saved coordinates. The independent off-axis coupling defect is the stronger acceptance obstruction.

Earlier direct legacy near-axis Poisson derivative quotients exhibit severe FP64 cancellation—d_rR_Ψ can be around−10^4 at r≈10^-10 while MP is around10^-13 despite accurate individual jets. This is evaluator cancellation, distinct from the legacy model's actual Poisson mismatch elsewhere. Regular r² heads avoid that quotient. Smooth finite tanh/regular heads, stable tested widths and sampled higher-derivative checks give no evidence of a singular layer in the retained family; finite checks do not certify global smoothness or exclude unobserved thin layers.


## G. Restart and reproducibility

The exact primary full-state paths below are immutable retained checkpoints, rather than mutable best-state aliases. They include model/C, optimizer/H, objective batches and archive, original NT cohort/reference, RNG, controls and cumulative clock lineage. T0 is a tail-filter warm-start at step0 selected before any tail optimization; its subsequent run was completed and its final state is separately preserved.

| State | Selection role | Native full-state checkpoint | SHA256 |
|---|---|---|---|
| E825 | E_aggregate, E_axis | [step_0000825.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/phase4_E_barrier_control/euler-discovery-NT-control-da6917be9ec5-6905651/E_barrier_control/step_0000825.pt) | `1b910969bec9e24b9990a8fd4397fbaa079399e774768a607e67b64eebac76d7` |
| S1195 | S_aggregate | [step_0001195.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001195.pt) | `d942f1032506912be6ced5a89ad713736faf056df7b0c9faf29b0ea689f4e0a6` |
| S1344 | S_Omega | [step_0001344.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001344.pt) | `a6d552561c1161b4cbc10dc8c27c57a3afee800b4a99aa7c5ae394deb9a62d8e` |
| T0 | T_aggregate | [step_0000000.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_tail_delta_small_clean/euler-discovery-S-tail-d4-clean-a54208a7154c-6908322/S_tail_delta_small/step_0000000.pt) | `42bdb9bab1d49ccf2110e9d48c1ba78f04985fa3eb5b604a254a5935fb60cf02` |
| Q350 | quartic_maximum | [step_0000350.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_hotspot_balanced/euler-discovery-S-hotspots-059d98d5a500-6907718/S_hotspot_balanced/step_0000350.pt) | `d8b4b4b41c0c14047e3038e06f3e73e07aa1776923eae4aeb12543d738528b0a` |
| T102 | additional_all_regions_max_three | [step_0000102.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_tail_delta_large/euler-discovery-S-tail-d2-1701382a0801-6908063/S_tail_delta_large/step_0000102.pt) | `cf70a79e5812772b52b41f76a259c763a85060c92d8a64b5746704360c948f74` |
| S915 | additional_broad_RU_rms | [step_0000915.pt](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0000915.pt) | `e7169f6a983456857f3ff7e960a0c8d00742823ccd1d030cb71ce0e74f7dbc77` |


The complete [restart index](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/restart_manifest.md) and [machine-readable index](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/restart_manifest.json) provide exact native final-state paths, original configurations, manifests, matching immutable source releases, source versions, important historical A/B starts and all 30 invocation lineages. This includes states that lost a final selection ranking and the two paired tail final iterates. Use each state's corresponding training release rather than treating the newer audit source as its exact optimizer implementation.

An exact continuation uses `discovery_train.py --config NEW_CONFIG --resume EXACT_FULL_STATE`, restores the saved objective/RNG/H, starts a new invocation, and sets a cumulative `optimizer_seconds` target larger than the saved clock. A changed objective instead uses `initial_checkpoint`, a new accounting clock and fresh curvature; its experimental original NT policy must be explicit. Inherited clocks are never new campaign credit. Current holdout data must not be reused for candidate tuning while claiming that the same holdout is untouched. No further training was performed after the freeze.

For example, a future separately authorized S1195 continuation stages a NEW project outside the protected repository: copy the matching `releases/S_exact_resume_v1/src` and `environment.sh`, and copy its [original config](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/results/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/config.json) to that new project's `configs/resume.json`. Change only the cumulative `optimizer_seconds` target to7200 for this exact continuation. Its saved selected clock is4818.110682506114 seconds, so the requested new work would be about 2382 seconds. Exact resume restores the other saved objective settings and ignores a supplied branch rename; unique central output/checkpoint roots identify the new invocation. Freeze the new config together with this copied source before Stage B. Use the following explicit central command shape after replacing `/ABSOLUTE/FUTURE_PROJECT` and output roots:

```bash
CTL=(python3 /resnick/groups/Hou-group/Changhe/hpc/slurm/scripts/slurmctl.py)
"${CTL[@]}" prepare --experiment euler-S-future \
  --project /ABSOLUTE/FUTURE_PROJECT \
  --entrypoint src/discovery_train.py --language python \
  --command-json '["/resnick/groups/Hou-group/Changhe/Euler/environments/euler-torch28-cu126/bin/python","-B","{snapshot}/src/discovery_train.py","--config","{snapshot}/configs/resume.json","--resume","/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/checkpoints/S_exact_resume/euler-discovery-S-continue-ced9769b9760-6906248/S_exact_resume/step_0001195.pt"]' \
  --smoke-command-json '["/resnick/groups/Hou-group/Changhe/Euler/environments/euler-torch28-cu126/bin/python","-B","{snapshot}/src/discovery_train.py","--config","{snapshot}/configs/resume.json","--smoke"]' \
  --include src --include configs --include environment.sh --environment environment.sh \
  --dependency numpy --dependency torch --gpu p100 --cpus 2 --mem 16G \
  --time 02:00:00 --qos normal --smoke-timeout 300 \
  --output-dir /ABSOLUTE/NEW_RESULTS --checkpoint-dir /ABSOLUTE/NEW_CHECKPOINTS
# Record the returned plan and job IDs; submit with future campaign authorization:
"${CTL[@]}" submit --plan PLAN_ID --authorized-by 'REFERENCE_TO_FUTURE_AUTHORIZATION'
"${CTL[@]}" mark-ready --plan PLAN_ID
"${CTL[@]}" check-ready --plan PLAN_ID --job-id JOB_ID
```

This is a future reproduction template, not an executed extension of the completed holdout campaign. Stage A rechecks live resource fit; readiness binds the copied source/config; Stage B runs on the same production allocation. The scientific trainer must never run on the login node. A continuation informed by the current holdout requires a new prospective final evaluation.

The actual audit environment was Python3.9.21, PyTorch2.8.0+cu126, FP64 on allocated P100 GPUs (sm60), one thread per numerical process; Matplotlib3.9.4 used Agg. No environment was reinstalled. The [frozen final release](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/releases/final_audit_v1/source_manifest.json) covers98 listed source/configuration files, SHA256 `2ebb1d17fc3a61823d2a6d6b0acc0877eedaa5f6236f14abd786b4896f50bdce`. The [protocol](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/releases/final_audit_v1/configs/final_validation_protocol.md), [shortlist](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_shortlist_frozen.json), [seed record](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_seed_record.json) and [seed exclusions](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_seed_exclusions.json) preserve the chronology: optimization stop00:38:56Z, shortlist00:38:59Z, complete source freeze00:40:03Z, one seed draw00:40:58Z. The seed 123636364 was drawn once after excluding2777 recorded seeds/offsets. Audit Stage A/B binds central code version `80fd26988998d47d46104cd55ec12759eac442a205758f82886214c0d0c5de96`.

Both GPU audits and the CPU geometry audit each passed their allocated215-test suite before production diagnostics. Counts overlap and must not be summed as645 unique tests. Tests cover numerical transformations/gradients, original equations, axis limits, chunk equivalence, saved-state restoration, source/cohort binding and orchestration. Actual allocated validator mutation fixtures also verified that changing a model buffer fails the state-immutability gate. Final file joins and the independent reviews supplement those tests; they are integrity checks, not mathematical convergence certification.

The allocated final [cross-bundle integrity join](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/validation/final_artifact_join/euler-final-artifact-join-e27a208992c9-6911242/final_gpu_join.json) completed under job6911242 with `actual_artifacts_rechecked=true`, checking actual coordinate headers/counts/digests, report/checkpoint files, source/shortlist/seed bindings and exact seven-state coverage. Its [runtime record](/resnick/groups/Hou-group/Changhe/hpc/slurm/records/euler-final-artifact-join-e27a208992c9/runtime-6911242.json) and parent scheduler record both report normal exit0. The final common cohort signature is `f6c82cc9ab22131c838f7a2bce32acd6d687dc24e96dbf7c710d9ab98501c3e6`.

Independent file review verified all 168 primary diagnostic artifacts (56 NPZ,70 PNG,35 PDF,7 JSON), including ZIP CRCs/NPY headers and image/PDF structure, plus 86 linked CPU artifacts across nine states. It also rehashed all 98 manifest-listed files in the frozen release and actual ready snapshots. This establishes artifact integrity, not a numerical global bound. The13 representative PNG images actually opened by the controller are separately recorded. The [geometry/MP evidence table](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_geometry_results_draft.md) links every state's original geometry, widths and precision reports.

Independent final reviews are retained for [scientific interpretation](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_science_report_review.md), [time/resource accounting](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_accounting_independent_review.md), and [artifact integrity and links](/resnick/groups/Hou-group/Changhe/euler_discovery_20261114T2012Z/research/final_artifact_review.md). Their reviewed report digests and scopes distinguish the finite evidence from a certificate. The protected Git repository receives only this new Markdown report; all code, arrays, plots, logs and native states remain in the timestamped research directory. Existing prompt/report pairs and unrelated user files are preserved.



## H. Next steps

The regular elliptic two-field formulation is the strongest starting point because it removes a real inconsistency and has independently tested stable axis evaluation. The next campaign should address the measured coupling failure before extending the same objective or increasing network capacity.

1. Build coupling-aware initializations in which nonzero Ω stationary lobes overlap a swirl source of the required sign and magnitude. Treat the identity1.5Ω=2UU_z as a PDE diagnostic, not a prescribed amplitude, parity or published shape.
2. Use physical rR_Ω, term-relative balance and both lobes alongside reduced-field RMS and derivatives. Cover the actual r≈126–252 defect locations; the current fixed r≤100 weighted score omits them. Declare new regions before new selection/final testing, and retain broad coverage so local sampling does not merely move defects.
3. Compare a global elliptic-inverse representation with the regular differentiated-Ψ representation, respecting the axis and correct infinite-domain tails. This may improve how Ω geometry and Ψ are coupled; no arbitrary finite-radius boundary condition should become part of the target problem.
4. Test nontriviality controls through controlled relative-residual/width trajectories and multiple independent basins. Keep the soft sampled RMS term explicitly experimental; neither removing it nor fixing an amplitude is a solution by itself. Account for true length/translation gauges before calling states distinct branches.
5. Resolve transition-shell and next asymptotic transport coefficients with MP-guided analysis, while keeping dimensionful coefficients and raw absolute errors in their proper units. A larger δ changes core conditioning strongly; do not select it solely because a nominal coefficient is smaller.
6. For a genuinely improved branch, freeze a new source/protocol/candidate set and draw a fresh holdout seed only after optimization has stopped. Strengthen adaptive resolution of suspected residual layers before claiming numerical convergence, then consider rigorous validation or stability work.

The useful outcome is a preserved, reproducible negative result with a specific coupled-PDE obstruction and several controlled formulation/normalization/sampling comparisons. It neither establishes an exact Euler profile nor rules one out.
