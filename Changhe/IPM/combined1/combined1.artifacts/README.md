# Accompanying artifacts: S1/IPM combined campaign 1, joint closure report

This folder holds the code, certificates, candidate snapshots and audit records that accompany the joint closure report of the S1/IPM combined campaign 1. It lets a reader re-run the computations behind the certified numbers of the report and check the integrity of every file. The joint closure report is published beside this folder; reports/ holds the companion reports and exchange/ the final exchange records of the campaign.

Software: Python 3.12 with numpy, scipy, mpmath, sympy and python-flint. Set `export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1` before running anything.

## Directory map

- reports/: THEORY_FINAL.md (final report of the theory batch), NUMERICS_FINAL.md (final report of the numerics batch), NEXT_24H_PLAN.md (prioritized plan for a next campaign), REPRODUCE.md (exact commands, inputs and expected checks, row by row for every certified number and theory certificate), T2_final_summary.md (sharp linear estimates and weak spaces) and N3_certification_summary.md (full-plane residual norm certification).
- exchange/: closure_matrix.md (final closure matrix, version v185, every theory-numerics pair with its status and gap), theory_v08.md and numerics_v16.md (the latest theory and numerics exchange versions), the run contracts (norm definitions, normalization, candidate ID and hash rules shared by both batches).
- code/theory_closure/: T1/T3 theory worker. Nonlinear closure constants (closure_calc/), graded estimates (graded_calc/), the arithmetic of the conditional theorems and the audit-item checks (checks/), transfer checks, and run_all.sh. See its README.md.
- code/theory_linear/: T2 theory worker. Weak spaces, sharp linear estimates and exact-rational threshold arithmetic (arith/), input data (data/), and a self-contained reproduction of one audit item (repro/). See its README.md.
- code/numerics_basis/: N1/N2 numerics worker. Far-field asymptotics, generator basis and candidate construction (code/), with far-field tables, held-out tests and construction records (data/). See its README.md and SHA256SUMS.
- code/numerics_certification/: N3 numerics worker. Two-sided norm certification of candidate residuals (code/), the stored certificates (results/), audit probe inputs (t4_probes/) and the certification summaries (notes/). See its README.md. In its README the code directory is written certification/; in this folder it is code/.
- candidates/: candidate profile snapshots, with INDEX.md and README.md (which snapshots are complete, which are manifest-only, and the original sha256 of every snapshot file).
- audit/theory_audit/: The T4 theory audit. FINAL_AUDIT.md, FINAL_ADDENDA.md (and the through-514 copy), AUDIT_SUMMARY.md, VERDICT_LEDGER.md (the full verdict ledger), AUDIT_REPRODUCE.md (audit reproduction commands), the evidence files FINAL_EVIDENCE.json and FINAL_ADDENDA_EVIDENCE_v04.json, finalization/ (evidence validator and its output) and research/INDEX.md.
- audit/numerical_audit/: The N4 numerical audit. AUDIT_SUMMARY.md, the N4 final numerical audit, FINAL_AUDIT_ADDENDA.md (and the through-446 copy), FINAL_HANDOFF.md, VERDICT_LEDGER.md, AUDIT_REPRODUCE.md, the evidence indexes the N4 evidence index v03 and the N4 post-freeze evidence index v02, and audit_tools/.
- audit/*/research_code/ (where present): the audit research scripts, added separately; see the README files there.
- SHA256SUMS: sha256 of every file in this folder except itself (relative paths).

## Reproducing the certified numbers

Every command below is run from the root of this folder. Commands that need a different working directory change into it inside a subshell. Output goes to a scratch directory `$OUT` outside the folder, so the stored records are not overwritten. Compare the printed values with the stored records named in each item.

```
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1
OUT=$(mktemp -d)
```

### 1. Candidate 007: forcing norms with two-sided enclosures

Reference candidate C1-N1-007-d2w-j7-e2bal (complete in candidates/). Stored records: code/numerics_certification/results/C1-N1-007-d2w-j7-e2bal_e2norms.json, _hminus1_summary.json and _registered_norms.json. Total runtime of the components about 12900 s; the F record of step (b) is about 1.3 GB.

```
ID=C1-N1-007-d2w-j7-e2bal
SRC=../../candidates/$ID/d2w_j7_n4_E2bal_mid180_exact.json
# (a) exact Beta-integral norms; G0 = ||F||_2 = 0.376689324705894261944645766874... (two-sided ball), G1, P2, Q3, rF
(cd code/numerics_certification && python3 -B code/e2norms.py "$SRC" "$ID" "$OUT")
# (b) exact F record, then the two-sided enclosure of ||F|| in Hdot^-1
F_RECORD=$OUT/d2w_j7_n4_E2bal_mid180_exact_Fpoly_cache.json
(cd code/numerics_certification && python3 -B code/build_F_record.py "$SRC" "$OUT")
(cd code/numerics_certification && python3 -B code/hminus1.py "$ID" "$F_RECORD" "$OUT" 24 20 61)
# (c) Hardy sharpening of the upper bounds; approximate display of the ||F||_H enclosure: [0.6355243760000922, 0.6355322685705509]
(cd code/numerics_certification && python3 -B code/hminus1_hardy_fix.py "$ID" "$F_RECORD" "$OUT")
(cd code/numerics_certification && python3 -B code/hminus1_mode_hardy.py "$ID" "$OUT")
# (d) registered norms: the four N_s norms (Ns18, Ns28, Ns16, Ns13 enclosures) and the sharpw norm X_(s,w)(F)
(cd code/numerics_certification && python3 -B code/assemble_norms.py "$OUT" "$ID")
```

Expected rounded displays from (d), rather than directed enclosure endpoints: Ns18 in [606.739449321, 606.910167092], Ns28 in [606.818076598, 606.820304991], Ns16 in [606.503336911, 607.180018172], Ns13 in [604.299621083, 609.698718714], sharpw X_(s,w)(F) in [756.5312630768, 757.8514372426]. assemble_norms.py takes the results directory first and then one or more IDs (the copied README shows the older one-argument form). It needs the full <ID>_hminus1.json from step (b); without it the H bound falls back to the rF estimate.

### 2. Exact-rational threshold arithmetic of the conditional theorems

```
# sharpw framework: s = 1/5184, w = (2^15, 2^20), r = 1351/10^6, eta = 4207/(2*10^7) = 2.1035e-4, so X_(s,w)(F) <= 2.1035e-4 suffices (a few seconds)
(cd code/theory_linear && python3 -B arith/t4l2_sharp_framework.py --no-float)
# optimum of the sharpw threshold: eta* = mu^2/(4A) = 40722836401/193491763200000, with mu = 201799/648000 and A = 576/5 (20 checks, under 1 s)
(cd code/theory_closure/checks && python3 -B check_v50.py)
# the same optimum at r* = 201799/149299200 (17 checks)
(cd code/theory_linear && python3 -B -u arith/t4_479_sharpw_max.py)
```

t4_479_sharpw_max.py first checks the sha256 of two working notes that are not part of this folder (a frozen report copy and a T2 working note), so it stops at that check here; the arithmetic itself is the same as in check_v50.py.

### 3. TB-sharp threshold

```
# s = 2^-13, r = 43/50000, rate >= 123/1000, eta = 5289/50000000 = 1.0578e-4, so N_s(F) <= 1.0578e-4 suffices (under 1 s; without --no-float it adds a floating-point cross-check, under 3 min)
(cd code/theory_linear && python3 -B arith/sharp_kernel_constants.py --no-float)
```

For candidate 007 the lower endpoint of N_s(F)/threshold is approximately 5712796.57, and the sharpw ratio exceeds 3596535.59 (from item 1).

### 4. Exclusion bounds for candidates 021 and 022

The data files of both candidates are in candidates/ as gzip files; restore them first:

```
gunzip -k candidates/C1-N1-021-heldin14-legqs25p50/legqs25p50_heldin14_gpu_m16_exact.json.gz
gunzip -k candidates/C1-N1-022-legqs25-m16to23/legqs25_m16to23_gpu_m16_exact.json.gz
(cd candidates/C1-N1-021-heldin14-legqs25p50 && sha256sum -c --ignore-missing SHA256SUMS)
(cd candidates/C1-N1-022-legqs25-m16to23 && sha256sum -c --ignore-missing SHA256SUMS)
```

The certified bounds (distance bound at the probe (n, K) = (19, 1800) and the point test) were computed by the numerical audit with its joint scaled factored weak-test script, `check_candidates.py <ID> 19,1800`, and confirmed by the theory audit with its candidate weak and point checks. Results: 021 distance > 466174213699793/2.5e17 (about 0.0018646969), point test F(1/10, 73/100) = 0.1004988054901384 with graded gap 0.0800973541730740; 022 strict floor 0.00135251075726327, point test F = 0.08875964289635570 against allowance 0.02039863807164356. Both candidates are excluded. These scripts live in the audit research code (audit/numerical_audit/research_code/joint_scaled_factored_weak/ and audit/theory_audit/research_code/candidate021_* and candidate022_*) and expect the audit research directory layout with the snapshot copied to audit/numerical_audit/research_code/candidate_audits/data/<ID>/; see audit/numerical_audit/AUDIT_REPRODUCE.md and audit/theory_audit/AUDIT_REPRODUCE.md, and the verdict ledgers, for the recorded runs and runtimes (about 200 to 260 s per probe).

### 5. Full check suites

```
bash code/theory_closure/run_all.sh "$OUT/theory_closure"   # all closure, graded and audit-item checks; one .out file per check
```

The copied READMEs (code/*/README.md) list every other command with its expected output and runtime. Scripts with rewritten paths expect to be run from the root of this folder, or from the working directory named in their README.

The full suite requires the omitted inputs listed below; its command alone does not restore them.

## External inputs

Some computations read Changhe Yang's published IPM case 4 / analysis2 artifacts. They are not included here. Obtain them and place each file at the path given (paths relative to this folder). Code that used an absolute path to these artifacts now reads them under external/ipm_source/.

| Needed at | Changhe Yang's published IPM case 4 / analysis2 artifacts, file | Size (bytes) | sha256 of the omitted copy |
|---|---|---|---|
| code/theory_linear/data/a2_nb_d2_exact.json.gz | gzip of analysis2/IPM_Analysis_II.artifacts/numerics/data/nb_d2_exact.json (identical to certificates/numerics_data/nb_d2_exact.json) | 450551 | `2c9c4a675509f3e609293cf07c75f6a35ae115f26814c1ff27646e1d5c1cc1ef` |
| code/theory_linear/data/a2_nb_Mpen2_exact.json.gz | gzip of analysis2/IPM_Analysis_II.artifacts/numerics/data/nb_Mpen2_exact.json (identical to certificates/P10_refit_inputs/nb_Mpen2_exact.json) | 427456 | `529b025f9052dba4ad136991e9f3dfb98da290ec105b61c74d49807302a9a685` |
| code/theory_closure/checks/data/state131_exact.json | analysis2/IPM_Analysis_II.artifacts/certificates/P1_source/state131_exact.json | 112350 | `e525e9d55f74e227b1ad9d2138032eb67f43261c05848e53844f33f8c55162b5` |
| code/theory_closure/checks/data/state131_field_points.json | analysis2/IPM_Analysis_II.artifacts/certificates/P1_source/state131_field_points.json | 11458 | `f384928cf76efc23517a5751ed104bc3d966e5437d51a28f6b9cb271167e02d8` |
| code/theory_linear/data/a2_state131_exact.json | analysis2/IPM_Analysis_II.artifacts/certificates/P18_weight_radius/state131_exact.json | 112350 | `8b52b460866d620c452edcfa3f9181481a1966b0de35f9d7dc38e46ff35342b8` |
| code/theory_closure/closure_calc/data/nb_stableA2_exact.annular.json | analysis2/IPM_Analysis_II.artifacts/certificates/P25_admissible_tail_gap/nb_stableA2_exact.annular.json | 613982 | `6aebb0482b6af0285bc43e6b7d3fa9dd4a616d080be9d562e410957bc2d0de49` |
| code/theory_linear/data/a2_p25_nb_stableA2_exact.annular.json.gz | gzip of analysis2/IPM_Analysis_II.artifacts/certificates/P25_admissible_tail_gap/nb_stableA2_exact.annular.json | 289742 | `b5ebe0cf42f37f7fcd5f14f9eefa7efe36a5433fadd6e9a556611277708b28da` |
| code/theory_linear/data/a2_state131_farfield.json | analysis2/IPM_Analysis_II.artifacts/numerics/data/state131_farfield.json | 370801 | `b340c06531f113027523e9aa171f6b1ceb0800fe7971f777f195271afb09e14b` |
| external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json | analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json (read by code/numerics_basis/code/optimization scripts) | | |
| (documentation only) | case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json | | |

A gzip copy must decompress to the listed source file; recompressing with `gzip -9 -n` may not give the same gzip bytes, so scripts that check the sha256 of a .gz input may need the original copy. closure_calc/six_branch_K.py and the other closure computations in code/theory_closure read closure_calc/data/nb_stableA2_exact.annular.json.

## Data files omitted for size

To keep the folder small, the following large data files of the copied directories are not included. Copies of candidate data can be restored from candidates/ (or from the full snapshot set, using candidates/README.md); the others are intermediate data. The per-directory SHA256SUMS files and the copied READMEs still list them.

| Path | Size (bytes) | sha256 | Note |
|---|---|---|---|
| code/theory_closure/checks/data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json | 2926809 | `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21` | byte-identical to candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json; restore with cp |
| code/theory_closure/checks/data/c1n1_013_pairU_m16_exact.json | 2928285 | `c07f87ddfe35e1fd82cfb86e01949749381aac7209a752c713dd01b48a478940` | byte-identical to snapshot C1-N1-013-pairU-from007 data file d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json (manifest-only here) |
| code/theory_closure/checks/data/c1n1_014_pairB_m16_exact.json | 2931981 | `8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746` | byte-identical to snapshot C1-N1-014-pairB-from007 data file d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json (manifest-only here) |
| code/theory_closure/checks/data/N3_016_hdual_m13deep.json | 383069 | `a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5` | byte-identical to code/numerics_certification/results/C1-N1-016-legqs25-quot013_legqs_hdual_m13deep.json; restore with cp |
| code/theory_closure/checks/data/T4295_013_tail_repair.json | 472668 | `5485a201200fe4cdd57560775c32c0e09938a06f352127a605a780dceaa1c0e4` | tail-repair data of the 013 check (013 data not included) |
| code/theory_closure/checks/data/T4295_014_tail_repair.json | 472668 | `b69aa6a844b89409b92c6e3c94de220289a6f6c486b7d5e3e6a8c91b1327999d` | tail-repair data of the 014 check (014 data not included) |
| code/theory_closure/checks/data/T4251_inputs.json | 667801 | `0282a067664e36f0c4faa6e5360c29e97a6610bb2959c0aa3d558d1d4ff1a5bb` | fields copied from the theory audit research files (audit check input) |
| code/theory_closure/checks/data/closure_matrix_v155.md | 475776 | `1751c1c9286d6857de72ce20fc345b18996b885a3f091b8dbe0b8ee10e13acbf` | older frozen copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v157.md | 478798 | `c94780adb23e986e6ff1a885e6c889291456523b07d3855367adea6bcc4ed7c4` | older frozen copy of the closure matrix (consistency check input only) |
| code/theory_linear/data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json.gz | 1289496 | `c1f7e1bdb4bb5bbe52bbe810a4b3c86e2badc4aef7cf0bb946c06a02faedcd04` | gzip of candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json |
| code/theory_linear/data/c1n1_005_d2w_j7_n4_X3_mid180_exact.json.gz | 1289173 | `f9156062b3021094ed444e68b50e668ac63a6119a10c809555b221590e89e11c` | gzip of snapshot C1-N1-005-d2w-j7-x3 data file d2w_j7_n4_X3_mid180_exact.json (manifest-only here) |
| code/theory_linear/data/t4_281_inputs/c1n1_013_d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json.gz | 1289961 | `16ea81e8b2d2b17b89df80b7ff3863936b9d10abdaa37ce7e89c6d3bdd65d39b` | gzip of snapshot C1-N1-013-pairU-from007 data file (manifest-only here) |
| code/theory_linear/data/t4_281_inputs/c1n1_014_d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json.gz | 1291245 | `0f6fe4d339b2b77665022150eece893af87d1582c40483a83a037ba2eef4471c` | gzip of snapshot C1-N1-014-pairB-from007 data file (manifest-only here) |
| code/theory_linear/data/n1_016_inputs/quot013_legqs25_m9to15_cpu_m16_exact.json.gz | 1269739 | `2d360bf7d74a38a1037490ea99f31089ba35d049f8b75e43a8fccfba2b007dd6` | gzip of candidates/C1-N1-016-legqs25-quot013/quot013_legqs25_m9to15_cpu_m16_exact.json |
| code/theory_linear/data/n1_016_inputs/n4_242_direct.json.gz | 1193712 | `2b414c5367cee02d322e2a980ac35aa0ffc1e8c5c7cc62d6a463b4347e57dbaf` | numerical audit output used by the 016 sector review (audit research data) |
| code/theory_linear/data/n4_forcing_sin_6_8.json.gz | 1150602 | `747db9d74e73c985653d1f1c6255151aa06460587a6ec15364a0cf5329b920f8` | exact residual sine vectors of the 6-, 7-, 8-branch stationary families; regenerable with arith/extract_sector_vectors.py from numerical audit research data |
| code/numerics_basis/data/far_field/E_n_fixed_sector_norms_exact_4_16.json | 958324 | `bb9eefe6fd3c30839b53e2ccdc15efbd3a4fba42c2c75f29387d8761af4e2299` | far-field fixed-sector norm table, n = 4..16 (large output table) |
| code/theory_closure/checks/data/closure_matrix_v135.md.gz | 111361 | `3815cfce34d3f08240d46828eddee0ddc34e64b12505932af707613594438600` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v137.md.gz | 115546 | `1dd1bcbc88b04eb1f4fd7cf0cf03ad8ffd233521202479a1c639d7234452388f` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v138.md.gz | 117944 | `80dc671a1e689ff1737d29499c90f577235bc20f55a0194e14a09b7ea356bcac` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v139.md.gz | 120270 | `ff700f8256de2b0fddacbbde0e13a39da3e9462688144abae2f1c63fb03a9b75` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v140.md.gz | 123113 | `54ac0e26e9bbf829f0972b297a82e111fdbde56a07d8e454f5c16aeaa87eda97` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v146.md.gz | 135893 | `c1431b770553f5cc90540596fcc19f1ba7d1197ffa66537be2fe14f3488d2906` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v151.md.gz | 141084 | `82400cb35d385da109dc5e6f6c09fd13910c228ee34d77f01285a5a7cd7aca10` | older gzip copy of the closure matrix (consistency check input only) |
| code/theory_closure/checks/data/closure_matrix_v153.md.gz | 145035 | `b02f50b6ed5e954b01c451535b9d2d274fe9f7c97b9de84a25439f227c792c92` | older gzip copy of the closure matrix (consistency check input only) |

Example restore: `cp candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json code/theory_closure/checks/data/c1n1_007_d2w_j7_n4_E2bal_mid180_exact.json`.

Not included at all: run logs, scratch and cache files, the audits' full research trees (only the research code and indexes), and any copy of the read-only source data.

## Changes made to copied files

- Absolute local paths that pointed into the copied material were replaced by paths relative to the root of this folder (for example code/theory_closure/..., candidates/...), and the local Python interpreter path by python3, in 179 text files. No numerical code was changed. Paths that point to working directories not included here are left as provenance. Two evidence files whose sha256 is recorded elsewhere were left unchanged: audit/numerical_audit/the N4 post-freeze evidence index v02, audit/theory_audit/finalization/validation_v09.json.
- Markdown files were edited for publication: internal working names were replaced by role names and local paths by folder-relative paths or by a short description. The audit ledgers are named VERDICT_LEDGER.md and the audit reproduction files AUDIT_REPRODUCE.md. The frozen copy of the closure matrix used by the reading-only consistency checks row_refs.py and h18_verdicts.py (code/theory_closure/checks/data/closure_matrix_v170.md) was edited the same way, so those two checks no longer give byte-identical output.
- Because of these edits and the omitted files, the per-directory SHA256SUMS files (code/numerics_basis, code/numerics_certification, each candidate snapshot) are the original manifests and do not all match. Use the root SHA256SUMS for this folder.

## Verify integrity

```
sha256sum -c SHA256SUMS
```

The Markdown files were edited for publication as described above; the hashes recorded inside the reports and ledgers
identify the audited bytes of the original files. Provenance paths in code and JSON files were rewritten after the run: RUN_ROOT stands for the original run directory, and
its working areas are named by role (coordinator, theory_T1T3, theory_T2, theory_audit_T4, numerics_N1N2, numerics_N3,
numerics_audit_N4, shared, source); interpreter paths became python3. Where such a path names an input, the input is either
in this folder (see the path mapping above) or listed under External inputs or Data files omitted for size. Hashes recorded
inside manifests and ledgers refer to the files as they were before this rewrite; the top-level SHA256SUMS covers the published bytes. Use it for bundle integrity; the per-folder manifests are historical and may include omitted inputs.

## Report reference concordance

The report uses descriptive names. Its numbered theory audits, numerical audits and closure reviews correspond to `T4-NNN`, `N4-NNN` and `R1-NNN` in the recorded evidence. Candidate NNN corresponds to snapshot `C1-N1-NNN` (including any suffix); state 131 and the baseline profiles retain their numerical names. Numbered theory and numerics exchanges correspond to `theory_vNN` and `numerics_vNN`. Linear-estimate result N and weighted estimate N correspond to `T2-RN` and `T2-WN`. This concordance preserves the references without exposing working names in the report.

| Name used in the report | Recorded identifier |
|---|---|
| sharp Sobolev framework | `FW-T-TB-sharp-v1` |
| rebalanced Sobolev framework | `FW-T-TB-rebal-v1` |
| graded Sobolev framework | `FW-T-TB-graded-v1` |
| graded L2 framework | `FW-T-TB-gradedL2-v1` |
| fractional framework | `FW-T-TB-frac-v1` |
| L2 framework | `FW-T-T4L2-v1` |
| weighted sharp L2 framework | `FW-T-T4L2-sharpw-v1` |
| sharp L2 framework | `FW-T-T4L2-sharp-v1` |
| variable-margin L2 framework | `FW-T-T4L2-bL-v1` |
| transient-low L2 framework | `FW-T-T4L2-trans-v1` |
| L2 defect framework | `FW-T-T4L2-defect-v1` |
| stationary L2 framework | `FW-T-T4L2-statL-v1` |
| alternative defect framework | `FW-T-T4ALT-defect-v1` |
| dyadic Y framework | `FW-T-DYADIC-Y-v1` |
| tail-exponent framework | `FW-T-TE-eqthr-v1` |
| Woodbury framework | `FW-T-TC-woodbury-v1` |
| Analysis II D(b) framework | `FW-A2-Db` |
| Analysis II D(a) framework | `FW-A2-Da` |
| Analysis II Dw1/2 frameworks | `FW-A2-Dw1/2` |
| Analysis II Dw1 framework | `FW-A2-Dw1` |
| Analysis II Dw2 framework | `FW-A2-Dw2` |
| Analysis II logarithmic framework | `FW-A2-LOGP` |
| X3 norm | `NORM-T-X3-v1` |
| weighted X norm | `NORM-T-XSW-v1` |
| X7744 norm | `NORM-T-X7744-v1` |
| weighted X5184 norm | `NORM-T-Xw5184-v1` |
| weighted L2 norm | `NORM-T-WL2-v1` |
| weak-test norm | `NORM-T-WEAK-v1` |
| dyadic Y norm | `NORM-T-DYADIC-Y-v1` |
| weighted Laplacian norm | `NORM-T-WLAP-v1` |
| Ns13 norm | `NORM-T-Ns13-v1` |
| Ns16 norm | `NORM-T-Ns16-v1` |
| graded norm | `NORM-T-GRADED-v1` |
| necessary point-test norm | `NORM-T-PTNEC-v1` |
| symmetric point-test norm | `NORM-T-PTSYM-v1` |
| dyadic norm | `NORM-T-DYADIC-v1` |
| weighted lower-order norm | `NORM-T-WLOW-v1` |
| graded defect norm | `NORM-T-DEFECTG-v1` |
| L2 distance condition | `NC-T-DIST` |
| weighted distance condition | `NC-T-WDIST` |
| graded L2 budget condition | `NC-T-GRADED-L2` |
| packet condition | `NC-T-PACKET` |
| origin inverse condition | `NC-T-ORIGIN-INV` |
| origin condition | `NC-T-ORIGIN` |
| weighted rate condition | `NC-T-WRATE` |
| dyadic radius condition | `NC-T-DYADIC-R` |
| dyadic inverse-floor condition | `NC-T-DYADIC-FLOOR` |
| dyadic Laplacian condition | `NC-T-DYADIC-LAP` |
| screening condition | `NC-T-SCREEN` |
| tail-recurrence condition | `NC-T-TAILREC` |
| held-out rule | `R-HOLDOUT` |
| screening rule | `R-SCREEN` |
| tangent-step rule | `R-TANGENT` |
| tail-exponent rule | `R-TE` |
