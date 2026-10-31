# Accompanying artifacts of the report Euler3_step2.report.md

This folder holds the code, configurations, records, end states and analysis outputs behind the report
"Joint optimization of c_l and omega at angular degree 6 (Euler3, step 2)". All paths here are relative to this
folder. Total size about 43 MB.

## Layout

- optimization/ : the optimization campaign (its own README.md and SHA256SUMS.txt).
  - code/ : the production code (src, scripts, tests, configs) copied from the frozen code of the previous
    fixed-parameter campaign with versioned changes: every changed file keeps its earlier versions beside it
    (suffix .vN_HASH), and status/RELEASE_SNAPSHOT_*.md and status/FROZEN_CODE_SHA256.txt give the hashes of the
    production files and of the frozen originals.
  - code/configs/ : supervisor, queue and lineage configurations; final_states_list.txt names the final states.
  - starts/ : the immutable starting states (S01, S05, S09, S20 and the derived starts), with starts_MANIFEST.json.
  - runs/JOB/ : per job, job.json (the full configuration), the worker and standard-output logs of record (one line
    per accepted iteration), the start record and the end record. Periodic checkpoints are not included.
  - final_states/ROLE__JOB.pt : the segment-end checkpoint (coefficients, c_l, omega, optimizer state) of every
    selected or frozen end state of section 11 of the report.
  - validation/ : validation scripts and records (derivative gates, the 6.3 (a) end records, J_c evaluation
    records, branch distances, PROFILE records, parameter-evolution tables).
  - status/ : the job ledger (ledger.jsonl.gz, every launch and end) and the closed GPU-hours ledger by label
    (gpu_hours.json).
  - LINEAGE_STATUS.md : the final status of every lineage segment with end-state hashes.
- independent_checks/ : a subset of the independent verifier's records (see its README.md): the final-outcome
  review and sign-off, the final-test cohort and plan, the independent holdout recomputations and comparisons of the
  frozen ends, the independent field and pressure code, and the proofs with their verification notes.
- evolution/ : parameter, objective, gradient and residual evolution of every lineage (CSV, JSON and figures
  fig1 to fig5; deliverable B).
- ranking/ : dated ranking tables of the end states.
- branch_field/ : branch-identity field distances between end states, including the rotation and twist variants.
- sensitivity/NAME/ : the reduced parameter sensitivity of the end states named (section 6 of the report).
- analysis_tools/ : the scripts that made evolution/, ranking/, branch_field/ and sensitivity/, with self-tests.
- resources/util_samples.csv : GPU utilization and memory and host load, sampled every 10 minutes from 08:40 to
  15:41 UTC on 30 October 2026 (all GPUs of the shared host are listed).
- specification/specification.md : the registered specification of the campaign with every dated amendment; section
  numbers such as 6.3, 7.4 or 8.3 in the report and in the records refer to it.
- detailed_validation_record.md : the long working report as of 02:12 UTC on 30 October (Phases I and II), not
  updated later; where it differs, the report holds.
- custody_receipt.json : the receipt of a byte-exact copy of the raw arrays of one closed independent check (not
  included because of their size).
- PROVENANCE_rewrite.json : for retained files with an accepted original, their path and SHA-256 in the complete
  package that the independent verifier accepted at the end of the run, and their published SHA-256 here. It also
  records final publication changes; the checksum lists cover the publication-only documentation as well.
- SHA256SUMS.txt : the SHA-256 of every file in this folder.

## Paths and interpreters

The records were written on the machine on which the campaign ran. In every text file of this folder (JSON, CSV,
logs of record, scripts, Markdown and the gzipped text records) the absolute paths of that machine were replaced
by labels: RUN_ROOT/numerics (the optimization side; its experiment directory is
RUN_ROOT/numerics/degree6_free_parameters_48h), RUN_ROOT/verifier (the independent checks), RUN_ROOT/lead
(coordination and analysis) and RUN_ROOT/frozen_euler3 (the frozen previous campaign); other locations are RUN_FS,
HOME or TMPDIR. Interpreter paths are written python3. In the Markdown files, internal working-file names were
replaced by descriptions and the names of the working directories by roles, and a few Markdown files were renamed
(for example queue_plan.md and specification.md). The initial publication rewriting changed only those strings. The final review also corrected the resume
helper to resolve the relative starting-state labels, and updated the report references and this documentation.
The published hashes record those additional changes; the original accepted hashes are preserved. PROVENANCE_rewrite.json
lists, for each retained file with an accepted original, the hash of that original that the independent verifier accepted (top checksum
digest of that package 1d7087800445fa91695b1e964e40a3b506ff18b2b803de4d07ba722c06f93b1a) and the published hash.

The binary checkpoints (.pt) were not changed, because the report and the independent records cite their SHA-256;
their stored metadata still contains original absolute paths as strings. Scripts that take an absolute run
directory (ABS_RUN_DIR) or refer to RUN_ROOT need a copy of the original tree and do not run from this folder alone.

## Commands

All commands start in this folder.

Integrity:

    sha256sum -c SHA256SUMS.txt
    (cd optimization && sha256sum -c SHA256SUMS.txt)

One-command resume of a published end state (python3 must be python 3.9 with torch 2.8 for CUDA 12.8, the
environment of the previous campaign; the second argument is a GPU index or cpu):

    (cd optimization && PYTHON=python3 bash code/scripts/resume_from_artifacts.sh P1_FREE_s4__cont1_s4_S01_L6_cl0.4500_om1.0000_free.pt 0 1 ./resume_scratch_1 1800)

The arguments are the end state in final_states/, the device, the number of further LM iterations requested, a new
scratch directory (an existing one is refused) and the LM time allowance in seconds. The helper builds the scratch
tree with relative paths and runs the production worker, which resumes from the checkpoint. It normalizes
starting-state paths labeled RUN_ROOT as well as original absolute paths. The campaign version was tested twice
during the run on the P1 segment-4 end (section 11 of the report). After publication path changes, only shell and
embedded-Python syntax and starting-state path resolution were checked; the optimizer was not rerun.

Independent validation of the parameter derivatives (derivative gates of section 3 of the specification; one case,
CPU, one thread). The validation scripts expect src/, scripts/ and starts/ next to validation/, so they run from a
copy:

    cp -r optimization work && cp -r work/code/. work/ && (cd work && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 python3 validation/gates.py --tag check --cases S01_own --device cpu)

Other entry points (from the copy work/): python3 scripts/summary_table.py (table of every run), python3
scripts/gpu_hours.py (GPU-hours by label, needs the original launcher logs), python3 validation/record_63a.py and
python3 validation/jc_eval_state.py (end records and complete-Jacobian evaluation of an end state, see
optimization/README.md). The validation commands are given as recorded by the optimization side; they were not
rerun from this folder at publication.

## Checkpoint paths

Checkpoint paths (relative to the artifacts folder; the SHA-256 prefixes of the frozen files are those of section 8).
- P1 FREE, segment 4: optimization/final_states/P1_FREE_s4__cont1_s4_S01_L6_cl0.4500_om1.0000_free.pt
- P1 FIXED-CONTROL, segment 2: optimization/final_states/P1_FIXED_CONTROL_s2__p1c_s2_S01_L6_cl0.4500_om1.0000_fixed.pt
- F2 FREE, segment 4: optimization/final_states/F2_FREE_m3__f2_S01_k0_keep_m3_L6_cl0.4597_om1.3389_free.pt
- F2 FREE, segment 5 (excluded, diagnostic): optimization/final_states/F2_m4_excluded_diag__f2_S01_k0_keep_m4_L6_cl0.4597_om1.3389_free.pt
- P3 FREE, segment 4: optimization/final_states/P3_FREE_cont4free__cont4free_S20_L6_cl0.4500_om1.0000_free.pt
- P3 FREE, segment 3 (superseded): optimization/final_states/P3_cont3free_superseded__cont3free_S20_L6_cl0.4500_om1.0000_free.pt
- F1 FREE, segment 4: optimization/final_states/F1_m3__f1_S05_m3_L6_cl0.4500_om0.3000_free.pt
- P2 FREE, segment 6: optimization/final_states/P2_s6__cont2_s6_S09_L6_cl0.4500_om0.3000_free.pt
- F1 FREE, segment 5 (Phase III end, information): optimization/final_states/F1_m4_PhaseIII_end__f1_S05_m4_L6_cl0.4500_om0.3000_free.pt
- P3 FREE, segment 5 (Phase III end, information): optimization/final_states/P3_cont5free_PhaseIII_end__cont5free_S20_L6_cl0.4500_om1.0000_free.pt
- P3 FIXED-CONTROL, segment 2 (information): optimization/final_states/P3_FIXED_CONTROL_s2__p3c_s2b_S20_L6_cl0.4500_om1.0000_fixed.pt
- the saved starts S01, S05, S09 and S20: optimization/starts/ (listed in starts_MANIFEST.json).
The file names carry the job names used in the logs; a job's run directory is optimization/runs/JOB.

## Large records

The compressed job ledger (optimization/status/ledger.jsonl.gz) is retained to audit launches, endings and resource
accounting. The iteration table (evolution/iterations.csv) supports the reported progress windows. The only other
file larger than 1 MB is the P2 segment-6 checkpoint listed above. These are required records, not disposable
scratch output.

## Software

Optimization: python 3.9 with torch 2.8 (CUDA 12.8), the unchanged environment of the previous campaign. Analysis
tools: python 3.12 with numpy; the sensitivity and branch-field tools also need torch. Independent checks: python 3
with numpy, one CPU core and one numerical thread. No package was installed for this campaign.

## Not included

Periodic checkpoints; process logs of validation chains and analysis runs (listed in PROVENANCE_rewrite.json; the
logs of record of every job, worker.log and stdout.log in optimization/runs/JOB/, are included); the complete archive of the independent checks (15,616 files, 349 MB; manifest SHA-256
0837f4a23bd9fa348002d3ab9e2750907e2bf1aa3fe922796ee41ac4214a58a6), of which independent_checks/ is a subset; the raw
arrays named in custody_receipt.json; the dated working records and notes of the three sides of the team, which the
report replaces.
