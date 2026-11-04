# Reproducing the certified numbers

Paths in this file are relative to the root of the accompanying artifacts. Start each command block afresh from that root; each block changes to the role directory it runs from. REPRODUCE_FILES.tsv lists, for every certified number, the published proofs, scripts, inputs and summary records. The publication review reran the closure arithmetic and reproduced its retained case values, with `CLOSURE OPEN`. The N1 binding row fails for the edited note, program and runner. No full certification chain was rerun. Only the scripts, their direct inputs and the summary records are published; the large intermediate records named below as size exceptions are not, so a full replay of the hash bindings needs the complete working trees of the campaign, which are not part of this publication.

## Requirements for every replay

- Run every script of the numerical auditor from its role directory (`cd numerical_audit`). The scripts set `ROOT=Path(__file__).resolve().parents[3]`, and `background_complete_union/code/check_v01.py:11` and `scripts/run_complete_background_union_v01.py:11` assert that the working directory is that root.
- CPU pinning is checked in code. The numerical auditor's scripts assert `os.sched_getaffinity(0)=={50}` and nice >= 19. Examples: `research/source013_norms/code/evidence_v01.py:45`, `research/background_complete_union/code/check_v01.py:12`, `research/source013_near_norms/code/common_v03.py:72`, `research/source013_wholeplane_audit/code/check_v01.py:10` and `run_v01.py:7`, `research/closure_current_tuple_audit/code/check_v01.py:7`, `research/reference_b18s2_audit/code/freeze_v01.py:12` and `run_v01.py:15`, `research/source013_admission/code/import_v01.py:117`. The theory auditor's tools assert CPU `{40}`: `theory_audit/tools/audit_source013_moment_refinement_v01.py:9` and `audit_source013_hermite_majorant_v01.py:9`. So prefix the numerical auditor's commands with `taskset -c 50 nice -n 19` and the theory auditor's commands with `taskset -c 40 nice -n 19`. On another machine, edit those asserts in a copy.
- Python 3.12.13 with python-flint. `source013_norms/code/evidence_v01.py:45` asserts `sys.version_info[:3]==(3,12,13)`. The first theory agent's runner names python-flint 0.9.0. Also set `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1` and `NUMEXPR_NUM_THREADS=1`.
- Most outputs are opened write-once (`open('x')`), so a rerun fails if the record already exists. `closure_check_v08.py` (`open(...,'w')`) and `reference_b18s2_audit/code/publish_v01.py` instead overwrite files or append to ledgers. Replay in a copy of the artifacts tree.
- Hash bindings. Many checkers rehash their complete transitive evidence, for example `scripts/campaign_bindings_v01.py` `Bindings.recheck()`. The minimal set below supports inspection and selected arithmetic replays. Several final checkers stop at original hash bindings that differ from the publication copies; in particular, the independent closure checker rejects its three edited source programs. A byte-exact replay of the binding checks needs the original unedited programs and the rest of the working tree, with the relative layout `numerical_audit/`, `theory_audit/`, `exchange/`, `numerics_agent_1/`, `numerics_agent_2/` as siblings.

## Hardcoded absolute paths (file:line)

The selected scripts contain no hardcoded local data paths. Every path is computed from `__file__` or is relative. The only absolute paths are these:
- `numerical_audit/research/reference_b18s2_audit/code/run_v01.py:6`: hardcoded `PID=256524`.
- `numerical_audit/research/reference_b18s2_audit/code/run_v01.py:16` and `:19`: read `/proc/256524/cmdline` and `/proc/256524/stat`. The script paused a specific concurrent process, so it cannot be rerun as-is. Use the three direct stage commands under item 5 instead.
- `numerical_audit/research/reference_b18s2_audit/code/freeze_v01.py:25`: lists four local filesystem prefixes only as forbidden prefixes and does not read them (in the published copy the list is built from the four names instead of being written out).
- `numerical_audit/research/reference_b18s2_audit/code/run_v01.py:13` and `numerical_audit/scripts/run_complete_background_union_v01.py:56`: redact local paths from logs. They do not read them.

Other conditions that block a rerun:
- `numerical_audit/research/source013_admission/code/import_v01.py:11` sets the deadline `datetime(2026,11,4,17,5,30)` with `CUTOFF=DEADLINE-30`. Line 117 asserts `time.time()<CUTOFF`, so this importer refuses to run after 2026-11-04T17:05:00Z unless that line is edited in a copy.

Reads across role directories, all relative:
- `freeze_v01.py:13` reads `../exchange/candidate_snapshots/C2-N1-013-...`.
- `closure_current_tuple_audit/code/check_v01.py:6`, `source013_hermite_majorant_audit/code/check_v01.py:8` and `source013_moment_refinement_audit/code/check_v01.py:12` read `../theory_audit`.
- `source013_near_norms/code/provenance_v03.py:54-55` and `source013_admission/code/import_v01.py:68` read the `../numerics_agent_1` and `../numerics_agent_2` worker directories.

None of the selected scripts reads the source data directly. Candidate 007 is read from the local copy `numerical_audit/data/candidate007_exact.json`, which is not republished because it is a byte copy of the source file C1-N1-007-d2w-j7-e2bal.json of the previous campaign's candidate archive (restore it as described in README.md), SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. `candidate007/PROOF.md:5` and `:93` describe it as the immutable copied JSON.

## 1. ||F_007||_2: 0.3766893247058942619446457 < ||F_007||_2 < 0.3766893247058942619446458

Proof: `numerical_audit/research/candidate007/PROOF.md`. Final record: `research/candidate007/verification/moments_2048.json`.

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 research/candidate007/code/exact_structure.py      # defaults: --input data/candidate007_exact.json --output-dir research/candidate007/verification
sh research/candidate007/code/run_full.sh                                           # = taskset -c 50 nice -n 19 python3 research/candidate007/code/full_residual.py --bits 2048
```

- Input: `data/candidate007_exact.json` (2,926,809 bytes).
- Not listed because step 1 regenerates them:
  - `verification/canonical.json` (3,812,197 bytes), which `full_residual.py` reads.
  - `verification/structure.json` (1,367,238 bytes).
- The large intermediate expansion `full_residual.json.gz` was retired under `numerical_audit/storage/COMPLETED_REFERENCE_RETENTION_V04.md`. Its storage and retirement records are listed, and `run_full.sh` regenerates it. `full_residual.py` also has `--resume-moments`.

## 2. Source 013: ||F_*||_2 in [7.959400186993612e-7, 7.961206656880281e-7]; P-S1 norm in [0.0035510975483434412497, 0.0055545729030073655758]

The L2 interval and the first P-S1 interval come from `numerical_audit/research/source013_norms`. The proof is `results/whole_plane/PROOF.md`. The commands are recorded in `research/post_handoff_preparation/verification/compute_source013_complete_norms_v01/execution.json` (6 stages).

```
cd numerical_audit
M=55bbbee074de66aab59fd80aed97aec4a531ce8955f68f118f91534bc7ed7979   # sha256 of research/source013_norms/verification/manifest_v01.json
R=f477b08200c72b21e0cbebeaa5b523bcafd973805ef83b9190cb57f2f07edbbd   # sha256 of research/source013_norms/verification/external_review_v01.json
for K in weighted unweighted; do
  taskset -c 50 nice -n 19 python3 -B research/source013_norms/code/compute_v01.py --kind $K --mode primary   --manifest-sha256 $M --review-sha256 $R
  taskset -c 50 nice -n 19 python3 -B research/source013_norms/code/compute_v01.py --kind $K --mode reduction --manifest-sha256 $M --review-sha256 $R
  taskset -c 50 nice -n 19 python3 -B research/source013_norms/code/publish_v01.py --kind $K --manifest-sha256 $M --review-sha256 $R
done
```

- Outputs: `verification/{weighted,unweighted}_publication_v01/result.json`.
- At this stage the P-S1 interval is the looser [0.00343868989..., 0.03982840140...] (`results/whole_plane/verification/bindings_v01.json`).
- `scripts/publish_source013_norms_actual_v02.py --request-number 75 --publication <n>` only publishes the ledger entry. It does not change the numbers. The `--publication` value is not recorded in the files read here.
- Size exception: `compute_v01.py` loads and hash-checks the 391 upstream regional records listed in `verification/manifest_v01.json`, 395,260,429 bytes in total. They include `research/source013_admission/verification/table_v01/source013_table_v01.json.zst` (238,724,220 bytes) and `research/campaign_origin_energy/verification/n2_c5_ps2_v01/result.json` (40,493,229 bytes). They are not listed. Only the scripts, the manifest, the review and the final summary records are.

The displayed P-S1 endpoints come from the theory auditor. Its tools are named `audit_*` but they produce these numbers:

```
cd theory_audit
taskset -c 40 nice -n 19 python3 -B tools/audit_source013_moment_refinement_v01.py   # lower 0.0035510975483434412497 -> research/source013_moment_refinement/verification/{result,display,check,bindings}_v01.json
taskset -c 40 nice -n 19 python3 -B tools/audit_source013_hermite_majorant_v01.py    # upper 0.0055545729030073655758 -> research/source013_hermite_majorant/verification/{result,check}_v01.json
```

- Inputs:
  - `theory_audit/research/source013_norms_actual_audit/verification/{check_v01,norms_v01,weighted_actual_review_v02}.json`
  - `theory_audit/research/source013_hermite_majorant/source/*.json`, which are copies of the moment-refinement outputs.

Independent checks of those results by the numerical auditor (they read `../theory_audit` and the numerical auditor's weighted publication and its actual review):

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 -B research/source013_moment_refinement_audit/code/check_v01.py
taskset -c 50 nice -n 19 python3 -B research/source013_hermite_majorant_audit/code/check_v01.py
```

## 3. Whole-plane background: M >= (704955805507/10^12) I, |grad h_*| <= 1/4, ||Sym Du||_op <= 137/125

Proof: `numerical_audit/research/background_complete_union/PROOF.md`. Adoption: `verification/actual_review_v01.json`. Command, as recorded in `verification/execution_v01.json`:

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 -B scripts/run_complete_background_union_v01.py     # runner; or directly:
taskset -c 50 nice -n 19 python3 -B research/background_complete_union/code/check_v01.py \
  --host-adoption research/ordinary_slabs_host_method/verification/actual_review_v01.json \
  --host-sha256 1c4f2aa77efb1d5a24e1452a7afd937ba76423922fe1ec8abd157ffa44e6537a \
  --matrix-adoption research/ordinary_host_matrix_margin/verification/actual_review_v01.json \
  --matrix-sha256 e93663a092e2d69286bef255e71966a215c3d26b64980b8b70305daa1c8a3f25 \
  --output research/background_complete_union/verification/check_v01.json
```

The union combines these regions:

| Region in r^2 | Matrix lower | Records and producing code |
| --- | --- | --- |
| Inner [0,61/67], radial indices 0..60 | 704955805507/10^12 | `background_matrix_margin_recount/verification/actual_balanced_review_v02.json`; code `background_matrix_margin_recount/code/check_v02.py`, `batch_v01.py` |
| Middle [7/9,49/15], 42 host slabs, indices 56..97 | 890672299617/10^12 | `ordinary_slabs_host_method/verification/recount_v01.json` from `ordinary_slabs_host_method/code/recount_v01.py` and `run_local_recount_v01.py`; `ordinary_host_matrix_margin/verification/check_v01.json` from `ordinary_host_matrix_margin/code/check_v01.py`; their actual reviews and execution receipts |
| Exterior [49/15,infinity) | 761272835221/10^12 | `background_matrix_margin_recount/verification/actual_rectangular_review_v01.json`; code `rectangular_v01.py` |

- The earlier 60-index mask is `background_progressive_union/verification/check_v03.json` and `actual_review_v03.json`, produced by `background_progressive_union/code/check_v01.py`.
- The ordinary-region adoption `background_matrix_margin_recount/verification/actual_review_v01.json` is also read.
- Size exception: `check_v01.json` binds 1359 files, 900,560,396 bytes in total. Most are per-slab and per-cell records under `source013_background_admission`, `finite_long_preparation`, `background_slabs_independent` and others, plus `../theory_audit` records. `b.recheck()` rehashes them all. Only the scripts, direct inputs and summary records are listed.

## 4a. Whole-plane near derivative norms D4, D5, D6 (all 561 middle panels, origin, exterior)

Proofs:
- `numerical_audit/research/source013_near_norms/PROOF.md`
- `results/wholeplane_v02/PROOF.md` and `ACTUAL_ADOPTION_PROOF_v01.md`
- `numerical_audit/research/source013_wholeplane_audit/PROOF.md`

Command, as recorded in `research/finite_long_preparation/verification/assemble_source013_wholeplane_near_norms_v02/execution.json`:

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 -B research/source013_near_norms/code/assemble_v03.py \
  --request research/source013_near_norms/verification/application_request_v02.json \
  --request-sha256 0fdac8bf7865f867fa2df7320ea3e0e306549da68ed2d2c75a90724109bdfc1b
taskset -c 50 nice -n 19 python3 -B research/source013_wholeplane_audit/code/run_v01.py   # independent arithmetic; runs code/check_v01.py
```

- Imports: `common_v03`, `arithmetic_v01`, `provenance_v03`, `contracts_v03`, plus `contract_v02` and `chunks_v01` from `research/source013_near_admission/code`.
- Output: `verification/wholeplane_v02/result.json` (3,918,594 bytes, listed).
- Size exceptions:
  - The 561 per-panel and per-chunk records are not listed. They are under `research/source013_near_admission`, `research/source013_near_cover` and `../numerics_agent_1`, `../numerics_agent_2` worker directories (`provenance_v03.py:54-55`). The whole `source013_near_norms` tree alone is 16.9 MB in 1122 files.
  - Two records the commands regenerate are not listed: `source013_wholeplane_audit/verification/check_v01.json` (5,591,932 bytes) and `wholeplane_v02/actual_review_v01.json` (5,593,913 bytes).

## 4b. Closure arithmetic (AN926: rates, prices, allowances 123369792300 / 99695324090, rooms 9941475955 and 47277952671/5)

The original producer is the second theory agent's closure program. It reads `nearcopy_v08/` and `ps1copy/` next to itself (`closure_check_v08.py:56-57`, `:124`). It writes `closure_check_v08.json` in place, so run it on a copy:

```
cd theory_agent_2/research/closure_check
python3 -B closure_check_v08.py inputs_v08.json > closure_check_v08.out    # writes ./closure_check_v08.json (overwrite)
```

The near input `nearcopy_v08/near_check_v09.result.json` was produced by the first theory agent. It must run from the role directory `theory_agent_1`: the runner calls `rm -rf scratch/nc09` and also runs `research/h4rest/hi_kq_v06.py`.

```
cd theory_agent_1
PYTHON=python3.12 bash research/closure_check/run_nc09.sh                   # near_check_v04.py near_params_v06.json, taskset -c 41
```

The numerical auditor's independent check compares the archived copies in `closure_current_tuple_audit/source/`. `closure_check_v08.py` and `inputs_v08.json` there are byte-identical to the second theory agent's files. It also reads `../theory_audit/research/closure_v07_v08_audit` and `../theory_audit/runs/closure_v07_v08_v02/execution_v01.json`.

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 -B research/closure_current_tuple_audit/code/check_v01.py   # -> verification/check_v01.json (463 checks)
```

## 5. Exact identity of correction 013 (raw SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a)

Structural identity: `numerical_audit/research/reference_b18s2_audit/PROOF.md` and `RESULT_PROOF.md`. `run_v01.py` cannot be reused (PID and `/proc`, see above). Its stages, from `run_v01.py:7-9`:

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 -B -X int_max_str_digits=0 research/reference_b18s2_audit/code/freeze_v01.py   # copies ../exchange snapshot into data/, writes freeze_v01.json and bridge_request_v01.json
taskset -c 50 nice -n 19 python3 -B -X int_max_str_digits=0 research/legendre_exact_bridge/code/convert.py --request research/reference_b18s2_audit/verification/bridge_request_v01.json --tag reference_b18s2_v01
taskset -c 50 nice -n 19 python3 -B -X int_max_str_digits=0 research/fitted_center_constraints/code/check.py --request research/legendre_exact_bridge/verification/reference_b18s2_v01/structural_request.json --tag reference_b18s2_v01 --bits 1024
taskset -c 50 nice -n 19 python3 -B -X int_max_str_digits=0 research/fitted_center_constraints/code/reduce_v02.py --record research/fitted_center_constraints/verification/reference_b18s2_v01/result.json --tag reference_b18s2_reduction_v01
python3 -B research/reference_b18s2_audit/code/publish_v01.py    # writes RESULT_PROOF.md, publication_v01.json; APPENDS to AUDIT_LEDGER.md, work log, research/README.md and rewrites team notes: scratch copy only
```

Required inputs not listed, for size:

| File | Bytes | Note |
| --- | --- | --- |
| `research/reference_b18s2_audit/data/phi_007_b18s2_phi_exact.json` | 5,707,695 | Byte copy of the item 6 snapshot file, recreated by `freeze_v01.py` |
| `research/galerkin_conditioning/source/quotient_exact.json` | 3,012,094 | |
| `research/fitted_center_constraints/verification/reference_base_alias_v01/structure.json` | 6,287,207 | |
| `research/fitted_center_constraints/verification/reference_base_alias_v01/origin.json` | 612,356 | |
| `research/legendre_exact_bridge/verification/reference_b18s2_v01/canonical_elementary.json` | 3,330,452 | Output of `convert.py` |

Complete residual-source identity: `numerical_audit/research/source013_admission/PROOF.md` and `TABLE_RESULT_PROOF.md`.

```
cd numerical_audit
taskset -c 50 nice -n 19 python3 -B research/source013_admission/code/import_v01.py --job {planner_a|planner_b|table|combine} \
  --manifest-sha256 <sha256 of research/source013_admission/verification/manifest_v01.json> --review-sha256 <sha256 of verification/external_review_v01.json>
```

- The current hashes of those two files are 2c127b0f...4298 and effc48ff...a2a4. The executions recorded do not store the argv, so these hashes were not confirmed as the original arguments.
- The time cutoff at `import_v01.py:11` blocks reruns.
- The importer copies the owner computations from `../numerics_agent_1` and `../numerics_agent_2` (`research/source013_startup/worker_*`). The `table` job was owned by the first numerics agent on CPU 45.
- Not listed: the 238,724,220-byte table archive `verification/table_v01/source013_table_v01.json.zst`, and the planner outputs `planner_{a,b}_v01/output_result.json` (449,399 and 413,761 bytes). Their receipts and the combined result are listed.

## 6. Coefficient files of the best accepted candidate C2-N1-013 and its Pareto alternatives

Listed in the manifest:
- `exchange/candidate_snapshots/INDEX.md` (14,929)
- In `C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/`:
  - `phi_007_b18s2_phi_exact.json` (5,707,695; the exact coefficients, raw SHA256 a16e9d85...)
  - `MANIFEST.json` (30,324; SHA256 615f09c5...)
  - `SHA256SUMS` (561)
  - `phi_007_b18s2_summary.json` (22,382)
  - `eval_007quot_mid32_ang256_fx1000.json` (13,087)
  - `nqfft_007quot_mid32_ang256_fx1000.json` (4,428)
- In `C2-N1-013-...SUPPLEMENT-01-exact-far-sectors/`: `README.md` (2,811) and `SHA256SUMS` (169).

Not listed:
- `phi_007_b18s2.log` (10,353; a log).
- `SUPPLEMENT-01.../far_sectors_013_exact.json` (118,080,864 bytes). It is the exact far-sector table, over the size budget, and none of the six certified numbers above reads it directly.

Earlier candidate alternatives. In `NUMERICAL_OPTIMIZATION.md` section 8 (version 18), the only current non-dominated state in (||F_*||_2, P-S1 N_2) is the FLOAT research state b28s, frozen SHA256 0a77881a.... It is not snapshotted in `exchange/candidate_snapshots` and has no certificate. b29s exports the same function. So no current Pareto alternative exists among the snapshots.

The only snapshots once named as Pareto points come from the superseded version 1 summary: Pareto in (G0, P2, N_2), with C2-N2-001 (E6a) dominating the existing-basis points, which include the a3 P2-penalty endpoints C2-N1-004 and C2-N1-005. They are listed here for reference only, with byte counts, and are not in the manifest:

| Snapshot | Files (bytes) |
| --- | --- |
| C2-N2-001-e6a-inner07 | exact.json 3,114,915; sectors.json 13,406; eval_n1_mid32_ang256.json 11,748; SF_E6a_v3.json 44,403; MANIFEST.json 11,982; SHA256SUMS 409 |
| C2-N1-004-p2pen1e-6-wp6 | n1_p2_a3_wP1e-6_exact.json 2,798,215; _sectors.json 13,406; _eval_mid32.json 11,713; _SF.json 33,246; MANIFEST.json 11,782; SHA256SUMS 456 |
| C2-N1-005-p2pen1e-5-wp5 | n1_p2_a3_wP1e-5_exact.json 2,798,245; _sectors.json 13,416; _eval_mid32.json 11,725; _SF.json 33,283; MANIFEST.json 11,746; SHA256SUMS 456 |

## Published copies and hashes

Markdown files were edited only to replace internal agent names, local paths and internal file names by role directory names and words. Scripts had local paths and agent directory names replaced by the role directory names, so a script's own SHA256 can differ from the value recorded in the records that bind it. Data records (JSON, CSV, NPY and text outputs) are byte-identical to the working files, so their SHA256 values match the records. Each snapshot directory has a regenerated SHA256SUMS; files that were left out (run logs, and the far-sector table of the supplement) are listed with their original SHA256 in OMITTED_FILES_SHA256.txt next to it.
