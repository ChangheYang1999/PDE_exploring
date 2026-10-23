# Artifacts for the report on two-fold 3D Euler self-similar profiles (case 1)

This folder accompanies the report Euler1.report.md and the task Euler1.prompt.md in the parent folder. Its root
is also the root of the training project, so the commands below are run from this folder. All paths are relative.

Final status: RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS for the primary class (exact C^2 globally decaying
profiles with 0.4 < c_l < 0.5; Theorem L2, an informal proof checked independently, not machine-checked). Numerical
search: NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH. The 96-hour active minimum was NOT met: the campaign ledger
gives a credited non-overlapping training union of 0.999 to 1.180 hours (1.144 to 1.326 hours including the
independent validation intervals).

## Contents

| Path | Content |
|---|---|
| EQUATIONS.md, SOURCE_NOTES.md, THEORY_NOTES.md | conventions and derivations; sources and what was borrowed; proofs of L1, L2 and the residual floor with the dated audit log |
| train.py, euler_ss/ | solver: vector potential and pressure networks, hard m = 2 symmetry, two representations, losses, samplers, FP64 derivatives |
| runner.py, ledger.py, bin/ | supervised job runner, campaign ledger tools, launch/status/stop/resume/hold/release scripts |
| evaluate.py, export_npz.py, snapshot.py, publish.py, make_configs.py | trainer-side audit, weight export, snapshots, configuration generator |
| configs/, queue/, runner_config.json | all experiment configurations and the directory queue as left at the end of the run |
| runs/v1_M1_cl050/, runs/v2_M1_cl050/ | last and best atomic checkpoints, holdout sets and metric tables of the two resumable c_l = 0.50 runs |
| CAMPAIGN_LEDGER.jsonl | training ledger, 64 records, SHA256 9f9477b05b19cafb4b8cd911b06c188db5ab1eb22933ae1510703fd3647505ff |
| STATE.json, NEXT_STEPS.md | restart state, credited active-time enclosure, prioritized continuation |
| CHECKPOINT_FORMAT.md | checkpoint layout |
| tests/ | 17 trainer unit tests and the resume-test summaries |
| checkpoints/ | best evaluated state per representation and exponent (12 files, with INDEX.tsv giving full SHA256 and the independent evaluation file of each) |
| verification/code/ | independent evaluator (separate NumPy decoder, finite differences, cylindrical check, whole-space quadrature, ledger reconstruction) and its tests |
| verification/proofs/ | the independent written proofs (INDEX.md gives the reading order) |
| verification/final_snapshot/20261023T075719Z/ | frozen evidence used by the report |
| verification/*.md, *.json, *.tsv | independent verification report, report audits, theory and runtime audits, checkpoint table, validation ledger |
| verification/evidence/ | audit and test evidence files |
| verification/checkpoint_evaluations.tar.gz | one independent evaluation file for each evaluated checkpoint (88 files) |
| analysis/ | symbolic equation checks and their log, active-time enclosure script, table statistics, selected-checkpoint table |
| referee_reviews/ | reviews by an external referee (a second model) of the equations, L1, L2 (second proof, hostile review, scope), the residual floor and an earlier report version |

Files of the frozen evidence that the report cites by SHA256 prefix are byte-identical here: CAMPAIGN_LEDGER.jsonl
(9f9477b05b19cafb), verification/final_snapshot/20261023T075719Z/VALIDATION_LEDGER.jsonl (f596f809df539d3a) and
verification/final_snapshot/20261023T075719Z/CHECKPOINT_TABLE.tsv (9f6b5d16fae9af40). All checkpoint files are byte-identical to the evaluated ones. For
publication, local absolute path prefixes inside text files were replaced by paths relative to this folder; such
files (for example several JSON evidence files and the snapshot manifest) therefore no longer match SHA256 values
recorded for them before publication. Run logs and scratch files are not included. Only 12 of the 77 evaluated
checkpoint files are included (size limit); the others are identified by SHA256 in the checkpoint table.

## Commands

Requirements: Python 3 with NumPy, SciPy and PyTorch (FP64; a CUDA GPU for training, CPU is enough for evaluation), SymPy
for the symbolic checks, pytest optional.

    python3 -m pytest -q tests                      # trainer unit tests (or: python3 tests/test_physics.py)
    python3 analysis/check_equations.py             # symbolic checks of the equations document
    cd verification/code && python3 test_validation.py && python3 test_checkpoint.py && cd ../..

Independent evaluation of a checkpoint (the selected state at c_l = 0.43):

    python3 verification/code/checkpoint.py checkpoints/v2_M1_cl043_step6565_0b690cfd0b74062c.pt \
        --n 256 --holdout-seed 736291 --output my_eval.json
    python3 analysis/selected_table.py checkpoints/evaluations/checkpoint-0b690cfd0b74062c-b401c544dd-d33806fc.json

Active-time enclosure from the ledgers, and the statistics of the frozen checkpoint table:

    python3 analysis/ledger_bound2.py CAMPAIGN_LEDGER.jsonl \
        verification/final_snapshot/20261023T075719Z/VALIDATION_LEDGER.jsonl
    python3 verification/code/ledger_reconstruction.py CAMPAIGN_LEDGER.jsonl
    tar -xzf verification/checkpoint_evaluations.tar.gz -C verification/evidence
    python3 analysis/table_stats.py verification/final_snapshot/20261023T075719Z/CHECKPOINT_TABLE.tsv \
        verification/VALIDATION_COMPLETED.json

Trainer-side audit of a checkpoint: `python3 evaluate.py <ckpt.pt> --device cpu --out report.json`.

## Status, stop and resume

    bin/status.sh        # runner, queue, running experiments, ledger hours
    bin/stop.sh          # graceful stop: workers checkpoint and exit, queue kept
    bin/resume.sh        # continuation: requeue stopped entries and start the supervised runner
    bin/launch.sh        # start the runner without requeueing

Before resuming on another machine, edit runner_config.json so that "gpus" lists devices that exist there. The
exact continuation command, from this folder, is

    bin/resume.sh

It restarts only c_l = 0.50 entries: the stopped runs v1_M1_cl050 and v2_M1_cl050 from their last atomic
checkpoints in runs/, and the never-started entries v2_M3_cl050, v2_Z0_cl050 and v2b_BL_cl050. The 25 primary-range
entries are in queue/archived_primary/; moving one to queue/pending/ restarts it from scratch, because its run
directory is not included. No experiment with c_l > 1/2 or with a free exponent is queued; NEXT_STEPS.md lists how to
add them. Resume fidelity is demonstrated only for the tested cases described in the report (section 9).
