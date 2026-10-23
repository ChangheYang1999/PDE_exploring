# Post-stop software test evidence (no campaign-time credit; the frozen campaign ledger was never touched)

Generated 2026-10-23T08:21Z with the repaired train.py (stage-boundary batch clearing, accounting_version 3).
- lbfgs_resume_test_config.json: the small test experiment (width 32, depth 3, dir_tau, Adam 30 steps then L-BFGS, resample_every 5).
- accounting_v3/: 12-step run writing to its own test ledger (test_ledger.jsonl via --ledger-path). SUMMARY.json: 13 unmerged work
  intervals (12 optimizer steps + the stop validation), inter-interval gaps <= 2 ms not credited, sum of interval lengths equals
  the credited seconds. accounting_v3.log is the worker log.
- stage_boundary_resume/: run A stopped at global step 30 (right after the stage_advance checkpoint), resumed to 34; run B
  continuous to 34. SUMMARY.json: max |parameter difference| 0.0 (bitwise), identical stage/step counters. Logs and both
  ckpt_last.pt files are kept.
These tests used --ignore-global-stop (the campaign STOP file stays in place) and --no-ledger or a test ledger path.
