# LINUX_QUALIFICATION.md (numerics lane c4-num)

Status of this document: written 2026-10-24 during shift 1 (last revision 04:00Z, all background jobs finished). All commands ran in the independent copy; nothing was executed in or written to
the protected tree.

## 1. Source isolation and before/after integrity

| Item | Value |
|---|---|
| SOURCE_REALPATH (protected, read-only) | `@SOURCE_REALPATH@` |
| WORK_REALPATH (independent physical copy) | `@WORK_REALPATH@` |
| OUTPUT_REALPATH | `@OUTPUT_REALPATH@` |
| Copy method | `cp -a` of the whole handoff, then `chmod -R u+w` on the copy only |
| Files copied / symlinks | 217 files (matches the handoff count), 0 symlinks in source and copy |
| Checksum comparison | `outputs/integrity/source_before.sha256` (217 lines) is byte-identical to `outputs/integrity/work_copy_initial.sha256` (diff empty) |
| accepted278 SHA-256 | `812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955` in both trees |
| Before-integrity record of protected tree | `outputs/integrity/source_before.sha256`, `source_before.stat` (265 entries with size, mtime, mode), `case4_other_before.sha256` (prompt file and .DS_Store) |
| After-integrity record | PASS at 2026-10-26T03:06:03Z (after the 48 h mark 03:05Z; same read-only commands: find -type f, sort, sha256sum; find, stat -c "%n %s %Y %A"; sha256sum of the prompt file and .DS_Store): `outputs/integrity/source_after_20261026T030603Z.sha256` (217 lines; sha256 42f3633409af7787...) byte-identical to `source_before.sha256`; `source_after_20261026T030603Z.stat` (265 entries; 1b1bcde8cf7abe72...) byte-identical to `source_before.stat` (no size, mtime or mode changed); `case4_other_after_20261026T030603Z.sha256` (6539f1d044bcd050...) identical to `case4_other_before.sha256`; accepted278 sha256 812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955 unchanged. Verifier interim checks (03:26Z on 2026-10-24 onward, hourly): all 219 protected files unchanged. A final repeat is taken at the end of the last shift. |
| Absolute-path audit | 60 text files in the handoff contain historical `/Users/caltech/...` paths; the relocation adapter `tools/runtime.py` maps the production root to `WORK/research` and the six other historical roots to nonexistent `WORK/unshipped_provenance/<i>`; a CPython audit hook denies reads under any historical root. No path in the handoff points at `@BUILD_VOLUME@/.../repo`. `inspect`/`restart-audit`/all guarded checks report `blocked_original_reads: []`. |
| Python environment | `@NUM_DIR@/env` (venv from `/usr/bin/python3.9`, Python 3.9.25), packages installed from `environment/requirements.lock.txt` only: numpy 1.23.5, scipy 1.9.3, psutil 6.0.0, threadpoolctl 3.6.0 (`pip check` clean). Interpreter prefixes `@BUILD_VOLUME@/.../c4-num/env` and `/usr` are the only non-copy paths readable by the audit hook. |

The relocation adapter's allowed data roots are the copy and `WORK/research`; `tools/entrypoint.py` refuses a
workspace inside the repository or any historical root. The qualification workspace is a second rsync copy at
`outputs/qual/current181_01` (148 files from `work/research`).

## 2. Host

| Item | Value |
|---|---|
| Host | ip-10-0-18-154.ec2.internal, Linux 6.12.95 (Amazon Linux 2023), x86_64 |
| CPU | 2x Intel Xeon Platinum 8275CL (Cascade Lake, AVX-512), 96 logical CPUs, 2 NUMA nodes; this lane pinned by affinity to CPUs 78-89 (12 hyperthreads of node 1) |
| RAM | 1,121 GiB total, about 935 GiB available at start; no cgroup memory limit visible (`cgroup_limit_mib: null`) |
| Disk | `@BUILD_VOLUME@` NVMe 876 GB, 183 GB free at start; lane budget 40 GB |
| GPUs | 8x NVIDIA A100 80 GB visible; GPU 2 assigned (`CUDA_VISIBLE_DEVICES=2`); not used (no GPU implementation required) |
| BLAS/LAPACK | numpy wheel OpenBLAS 0.3.20 (SkylakeX kernels), scipy wheel OpenBLAS 0.3.18 (SkylakeX); threadpoolctl reports both |
| libm | glibc; `math.exp` and `numpy.exp` differ by 1 ulp in 24% of random arguments in [-40,40] |
| Load at start | 1-minute load 17.9 on 96 CPUs (0.19 per CPU), well under the guard ceiling 1.5 |
| Temperature sensors | none exposed (`temperature_c: null`) |

## 3. Standard-library checks in the copy (no numerical execution)

| Command (cwd `WORK`) | Result |
|---|---|
| `env/bin/python -B tools/verify_repository.py` | PASS: 216 inventoried files, 18,286,669 bytes, no failures |
| `env/bin/python -B tools/prepare_assets.py` | PASS: restored `research/base/inputs/assessment_grids_stage12.json` (11,329,369 bytes, SHA-256 `24de3177...30aeb`) |
| `tools/portable.py inspect --output outputs/checks/inspect.json` | PASS: candidate hash matches, 24/162/162 dimensions, state agrees with JSON, 46 translated paths, 0 blocked reads |
| `tools/portable.py restart-audit --output outputs/checks/restart.json` | PASS: 125 hash bindings (candidate, arrays, epoch, coordinate map, parents, 7 parent commits, 51+42 frozen sources, meshes, provider proofs); last event 318; 1 V3 commit shipped |

## 4. Guarded numerical checks (session `outputs/checks/session`, policy = shipped `smoke_policy.json`)

| Label | Wall s | Peak RSS MiB | Result |
|---|---:|---:|---|
| value_smoke | 2.2 | 102 | PASS |
| whole_axis_objective | 255.0 | 134 | PASS |
| strict_replay_01 | 29.0 | 1577 | FAIL (strict 64-epsilon gate), see below |
| strict_replay_02 | 27.4 | 1578 | FAIL (identical numbers to replay_01) |

Smoke (13 fixed physical locations, 288-node finite rule, Decimal five-Taylor, saved NPZ norm):

| Quantity | Max abs difference from Mac reference | Tolerance |
|---|---:|---:|
| spot R_f | 2.40e-14 | 3.97e-12 |
| spot R_rho | 8.88e-14 | 4.61e-10 |
| spot f | 1.42e-14 | 1.48e-08 |
| spot psi | 3.64e-12 | 8.49e-06 |
| fresh finite-rule J (not J_abs) | 1.16e-20 | 4.44e-16 |

Five-Taylor maximum defect 4.8882934568586e-14 (reference 4.88829345686e-14), a0 = 14.767729990606481, Poisson jet
identities 3.6e-67, center defect 0 (analytic elimination).

Objective (fresh adaptive independent whole-axis integral, target 1e-16):

| Quantity | Linux value | Reference | Difference |
|---|---:|---:|---:|
| J_abs | 4.268372607095559e-09 | 4.2683726070948805e-09 | 6.8e-22 |
| error diagnostic | 2.867e-19 | 2.898e-19 | within diagnostic |
| origin tail / infinity / radial / angular errors | 0 / 2.85e-19 / 8.5e-22 / 1.8e-22 | | |
| 85-digit overlap at r=0.02 | order-24 error 1.65e-24, PASS | | |

Strict replay (actual production source/parent/epoch gates, fresh four-thread V3 cached residual on the 90,624-node
training mesh, compared to the saved NPZ vector):

| Quantity | Value |
|---|---:|
| residual difference norm | 2.172678134506999e-15 |
| unchanged threshold 64*eps*max(norms) | 1.3130049377939713e-18 |
| fresh mesh J | 4.268372607096007e-09 (saved 4.268372607096841e-09, relative 2.0e-13) |
| bitwise equal | no |
| gates before the comparison | source closure, immutable parent, EpochIntegrator.require_qualified, verify_epoch_sources all PASS |

Verdict: FAIL on the strict gate, a possibility DEPLOY_LINUX.md names for a different BLAS. The tolerance was not
widened and the saved vector was not replaced. Consequence: `tools/make_qualification.py` cannot be produced on this
host and the exact 181D optimizer resume is blocked here; this does not affect the agreed plan (no 181D continuation).

Diagnosis (`outputs/diag/replay_diag.json`, guarded, read-only): on this host the V3 production residual is bitwise
repeatable across processes and identical for 1 and 4 BLAS threads. V3 (private scalar exp), V2 cached (numpy exp)
and V2 stateless differ from the Mac-saved vector by 2.17e-15, 2.52e-15 and 2.61e-15 in norm (max entry 1.6e-16,
73k-83k of 90,624 entries differ in the last bits) and from each other by 1.5e-15 to 1.7e-15. The residual is a
cancellation of O(10) field terms to O(1e-3), so single-ulp differences in exp/BLAS on the fields are amplified to
the observed level. The cause is not uniquely isolated (see 4b); the measured fact is that the fresh J_mesh differs from
the saved value by 2.0e-13 relative, and the other quantities are listed in 4d and in the verdict table.

### 4b. Per-node rounding model of the replay difference (lead criterion, NOTES_FOR_TEAM 03:41Z)

Scripts `outputs/diag/rounding_model.py` and `rounding_model_S.py` (guarded, read-only on the copy; outputs
`rounding_model.json`, `rounding_model_S.json`). 212 training-mesh nodes: 84 origin block (all r <= 0.02, the
Taylor-series nodes), 64 middle, 64 infinity; each block includes its four nodes nearest the x-axis and four nearest
the y-axis; plus 12 extra r <= 0.02 nodes and the 8 nodes nearest r = 0.02. Reference R_f: the handoff's own 85-digit
Decimal point-centered Cartesian Taylor evaluator `field_tests.independent_fields` with the analytic c0 at precision
90 (mpmath is not part of the pinned environment; Decimal at 85 digits serves the same purpose). Mac vector: saved NPZ.
Linux vector: fresh V3 production residual (4 BLAS threads).

Predeclared criterion: at every node both |r_Mac - r_ref| and |r_Linux - r_ref| <= 64 eps S_i, with the raw envelope
S_i = sqrt(2 w_i/(pi a_ref^2)) [ (c_l|x| + sum_g|c_g psi_y,g|) sum_g|c_g f_x,g| + (c_l|y| + sum_g|c_g psi_x,g|) sum_g|c_g f_y,g|
+ (|c_l-1| + sum_g|c_g ratio_g|) sum_g|c_g f_g| ] over the 24 core (analytic c0) and 162 Global generators (raw ratio field).

| Ratio to eps S_i (raw S) | median | p95 | max | nodes > 64 |
|---|---:|---:|---:|---:|
| Mac vs 85-digit reference | 0.115 | 5.53 | 12.530 | 0 |
| Linux vs 85-digit reference | 0.083 | 5.04 | 9.272 | 0 |
| Linux vs Mac | 2e-12 | 1.29 | 5.348 | 0 |

Per-block maxima (Mac / Linux): origin series 4.6e-12 / 7.6e-13; middle 9.83 / 9.27; infinity 12.53 / 8.43. Worst Linux
node 64974 (middle block, r = 6.66e6, theta = 1.443): R_f(ref85) = 6.212101715402188e-07, Mac 6.212101716120133e-07,
Linux 6.212101716154828e-07. Result: PASS, no node outside the predeclared envelope. These three maxima agree with the
verifier's independent computation (`c4-ver/evidence/baseline/generator_rounding_scale85.json`: 12.530, 9.272, 5.348).
Mac and Linux R_f are bit-identical at 59 of 212 nodes and differ in the last bits elsewhere.

Labeled separate diagnostic (not the criterion): with the center-subtracted ratio field sum_g|c_g (ratio_g - strain_g)|
the same ratios have maxima 0.507 (Mac and Linux, node 4608), p95 0.18, median 0.01.

Finding (recorded, not a Linux discrepancy): with the plain term sum |w_x f_x| + |w_y f_y| + |q f| as scale, node 4608
(middle block, r = 0.0200273, theta = 2.44e-4) has ratio 17278 for both machines: R_f(ref85) = 1.4889933597980429e-08,
R_f(Mac) = R_f(Linux) = 1.4889902818539247e-08, relative error 2.07e-6 in R_f, identical on both platforms. Just outside
the Taylor radius the direct evaluator sums generator contributions of size about 273 to a residual of 1.5e-8, leaving
about 3e-14 absolute error in R_f. Eight further middle-block nodes (r between 0.02 and 0.41) exceed 64 on this plain
scale and all pass on S_i. This is a precision property of the 181D production evaluator near r = 0.02 on both machines;
its effect on J is negligible (those nodes contribute (1e-8)^2-level terms). It is relevant for the 860 evaluator design.

Cause of the Mac/Linux difference: not uniquely isolated. What is established: the Linux vector is bitwise repeatable
across processes and BLAS thread counts; the OpenBLAS kernel family (Haswell vs SkylakeX) leaves it unchanged (4c);
numpy.exp and glibc math.exp differ by one ulp on 24% of inputs here; the three Linux providers differ among themselves
by 1.5e-15 to 1.7e-15 in norm; and every sampled per-node difference lies inside the declared first-order rounding
envelope. A specific Mac libm or Accelerate operation has not been identified and is not claimed.

### 4c. OpenBLAS kernel diagnostic (diagnostic only, never a replay pass)

`OPENBLAS_CORETYPE=Haswell` fresh guarded process, `tools/portable.py replay` into `outputs/diag/haswell/replay_haswell.json`:
threadpools report Haswell kernels; residual difference norm to the Mac vector 2.172678134506999e-15 (identical to the
SkylakeX run to all printed digits); fresh mesh J 4.268372607096013e-09 (SkylakeX 4.268372607096007e-09, 7 ulps of
the final dot product). The verifier found the Haswell and SkylakeX residual vectors bitwise equal.

### 4d. Measured Linux-minus-reference differences, quantity by quantity

| Quantity | Linux value | Reference (Mac/handoff) | Difference |
|---|---:|---:|---:|
| production training residual vector (norm of difference) | | saved NPZ | 2.1727e-15 (||r|| = 9.2395e-05; relative 2.35e-11) |
| J_mesh = r.r/2 | 4.268372607096007e-09 | 4.268372607096841e-09 | -8.3e-22 (relative 2.0e-13) |
| independent whole-axis J_abs (target 1e-16) | 4.268372607095559e-09 | 4.2683726070948805e-09 | 6.8e-22 (error diag. 2.87e-19) |
| independent whole-axis J_abs (tight, target 1e-18) | 4.268372607095585e-09 | 4.2683726070948805e-09 | 7.0e-22 (error diag. 2.07e-21) |
| spot R_f (13 points, max abs) | | smoke reference | 2.40e-14 |
| spot R_rho / f / psi (max abs) | | smoke reference | 8.9e-14 / 1.4e-14 / 3.6e-12 |
| five-Taylor maximum defect | 4.8882934568586004e-14 | 4.88829345686e-14 | 0 to printed digits |
| a_0 | 14.767729990606481 | 14.767729990606481 | 0 |
| frozen-grid E_f maximum | 1.2384963974302376e-04 (r 8.712, theta 0) | 1.23849639744e-04 | -9.76e-16 (relative 7.9e-12) |
| frozen-grid E_rho maximum | 7.165829214239423e-05 (r 267.16, y-axis) | 7.16582921424e-05 | 1e-17 |
| refined E_f maximum | 1.2386302084775014e-04 | 1.23863020848e-04 | 2.5e-16 |
| refined E_rho maximum | 7.165860703847401e-05 | 7.16586070385e-05 | 3e-17 |
| canonical Green inverse (17 points) | max abs error 1.64e-11 vs point tolerance 1e-7 + 1e-9|value|; center strain error 7.8e-16 | handoff PASS | PASS |
| origin overlap r = 0.005 / 0.01 / 0.02 (order-24 series vs 85-digit) | 4.0e-28 / 2.6e-26 / 1.7e-24 | tolerances 1e-18 + 1e-7|R_f| | PASS |

## 5. Complete derivative/provider qualification of the frozen code on this host

Detached under `outputs/qual/qualification_session` (policy = shipped production example: 32 GiB RSS ceiling, 3600 s per
run, 1 BLAS thread forced by the guard, worker raises it internally): `stage13_model_benchmark_v3.py --workers 1 4 8
--block-size 1024` through `tools/entrypoint.py` in the rsync workspace `outputs/qual/current181_01`
(`results/new_host_model_benchmark/checks.json`). Wall 1197 s, peak family RSS 2524 MiB, return code 0,
`completed = passed = True`. Reference stateless evaluator: fun 19.4 s, Jacobian 30.6 s.

| BLAS threads | cold fun s | Jacobian s | same-cl trial fun s | trial Jacobian s | cached vs stateless residual (rel) | Jacobian (rel) | reject-and-return cycle |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 27.11 | 5.55 | 0.59 | 5.59 | 1.80e-11 | 4.43e-16 | bitwise, within 64 eps |
| 4 | 25.71 | 5.31 | 0.52 | 5.31 | 1.80e-11 | 4.43e-16 | bitwise |
| 8 | 25.75 | 5.29 | 0.49 | 5.30 | 1.80e-11 | 4.43e-16 | bitwise |

Thresholds (unchanged): residual 5e-9, Jacobian 5e-11, raw FD 3e-5, feasible FD 1e-3, adjoint 1e-12. Raw finite
differences: all 186 columns pass (worst relative error 1.01e-10, median 1.5e-14; c_l column 4.4e-12 and 8.5e-12 at the
two steps). Feasible directions: 19 core plus 4 mixed pass (worst 1.34e-9; maximum HP defect 2.8e-12). Adjoint checks
9.6e-18, 0, 1.6e-17. Original stateless provider unchanged after private-cache evaluations: PASS. Selected runtime
workers 4 (fastest cold fun + Jacobian). Multithreading gives no speedup for this problem size (25.7 vs 27.1 s).

Independent residual assessment (`verification/scripts/independent_residual_assessment.py --labels stage13_v3_accepted278`,
same session, 1081 s wall, peak RSS 216 MiB, return code 0, `passed = True`; output
`outputs/qual/current181_01/results/independent_current_assessment/stage13_v3_accepted278/assessment.json`): 32 frozen
regions, exact axes from r = 1e-12 to 1e20, two dense resolution levels (769x199, 1537x397 points on r in [0.02, 1e12]),
distant bands 1e8 to 1e20, local refinements (4 levels) for E_f, E_rho and the two relative measures, fresh independent
integral (target 1e-16), tight independent integral (target 1e-18: J_abs 4.268372607095585e-09, error 2.07e-21, origin
0, infinity 2.2e-22, radial 6.9e-22, angular 9.2e-22, PASS), canonical Green inverse (orders 24..192 plus angular
refinement: PASS, center strain error 7.8e-16, worst point error 1.6e-11), 85-digit checks at the refined E_f and E_rho
peaks (differences 7.5e-15 and 1.0e-14 against tolerances 3.0e-10 and 1.7e-10), origin overlap checks PASS. Maxima are in
the 4d table. Band maxima of E_f: 0 for r < 1e-7, 9.4e-18 on [1e-5, 1e-3), 3.73e-10 on [1e-3, 0.02), 4.44e-6 on [0.02, 0.1),
6.36e-5 on [0.1, 1), 1.238e-4 on [1, 10) (the handoff reports 4.61e-10 for 0 <= r < 0.02 and 4.44e-6 for [0.02, 0.1)).

## 6. Verdict table

| Gate | Status |
|---|---|
| Copy complete, checksummed, no links into protected tree | PASS |
| Fresh environment with exact pins | PASS |
| verify_repository / prepare_assets / inspect / restart-audit | PASS |
| Smoke (fields, Taylor, saved norm) | PASS |
| Independent whole-axis J_abs reproduction | PASS (difference 6.8e-22) |
| Strict 64-epsilon production replay | FAIL (cause not uniquely isolated; preserved) |
| Per-node rounding model (lead criterion 64 eps raw S_i) | PASS (max ratios Mac 12.53, Linux 9.27, 212 nodes) with one recorded precision finding near r = 0.02 |
| Haswell kernel diagnostic | residual unchanged (diagnostic only) |
| Full derivative/provider benchmark (old code) | PASS (completed 03:35:46Z, all checks) |
| Independent 32-region assessment of accepted278 (old code) | PASS (completed 03:53:47Z; maxima, Taylor, tight integral, canonical inverse, 85-digit peaks all within unchanged tolerances) |
| make_qualification.py attestation | NOT PRODUCIBLE (requires passing replays) |
