# Exact-resume test (2026-10-23 06:35Z)

Config: configs/pilot_cl045.json (width 64, depth 4, c_l=0.45, Adam), GPU A100, FP64.

- Run A: 120 steps, STOP (checkpoint ckpt_last.pt), then relaunch with the same command, which resumed
  from the checkpoint (model, Adam state, sampler generator state, torch/cuda/numpy/python RNG states,
  stage/step counters, active seconds) and ran to step 180.
- Run B: continuous 180 steps in a fresh run directory (same seed).
- Result: max |parameter difference| = 0.0 (bitwise identical), max |Adam exp_avg difference| = 0.0,
  identical step counters; the logged loss at step 150 agrees to all printed digits (1.7094e-02).
- Also fixed on the way: torch>=2.6 weights_only default (our checkpoints are loaded with weights_only=False),
  and RNG/generator states must be moved back to CPU after map_location to the GPU.
Command used:
  python3 train.py --exp configs/pilot_cl045.json --device cuda:0 --run-root runs_test --max-steps 120 --no-ledger
  python3 train.py --exp configs/pilot_cl045.json --device cuda:0 --run-root runs_test --max-steps 180 --no-ledger
  python3 train.py --exp configs/pilot_cl045.json --device cuda:1 --run-root runs_test_cont --max-steps 180 --no-ledger

# L-BFGS mid-block exact-resume test (2026-10-23 07:09Z)

Config: width 32 depth 3 'dir_tau' model, stage 0 Adam 30 steps, stage 1 L-BFGS (max_iter 10, history 10, resample_every 5).
- Run A: stopped at global step 33 (stage 1, step 3, i.e. inside the first 5-step collocation block), relaunched with the same
  command: it resumed from ckpt_last.pt, restored the saved collocation batch drawn at step 0 of the block ("restored saved
  batch drawn at step 0") and the L-BFGS history, and ran to step 36.
- Run B: continuous run to step 36 in a fresh directory.
- Result: max |parameter difference| = 0.0 (bitwise identical), same stage/step counters.
Both tests used GPU (A100) FP64. Commands:
  python3 train.py --exp tmp/e1num_lbfgs_test.json --device cuda:1 --run-root tmp/e1num_rt_a --max-steps 33 --no-ledger
  python3 train.py --exp tmp/e1num_lbfgs_test.json --device cuda:1 --run-root tmp/e1num_rt_a --max-steps 36 --no-ledger
  python3 train.py --exp tmp/e1num_lbfgs_test.json --device cuda:1 --run-root tmp/e1num_rt_b --max-steps 36 --no-ledger
(the test config is the pilot config with the stages replaced; see WORKLOG 07:10Z).

# Repaired worker: stage-boundary and mid-block resume (2026-10-23 07:58Z, after the campaign stop; --no-ledger, test dirs in /tmp)

Repairs (train.py): the collocation batch is cleared before the stage_advance checkpoint and a saved batch carries its stage,
counts and sampler configuration (restored only inside a block of the same stage); eligible-work accounting now records
instrumented intervals [begin of batch draw, end of optimizer step after GPU synchronization] and validation intervals,
excluding checkpoint I/O, logging and pauses (accounting_version 3; intervals are stored unmerged, verified 08:08Z: 12 steps -> 13
intervals incl. the stop validation, inter-interval gaps 0-1 ms not credited, sum of lengths = credited seconds).
- Stage boundary: run A stopped at global step 30 (= end of stage 0; the stop happened right after the stage_advance checkpoint,
  at stage 1 step 0), resumed to step 34 (stage 1 step 4, inside the first L-BFGS block); run B continuous to 34.
  Result: max |parameter difference| = 0.0 (bitwise). This is the verifier's counterexample scenario (RUNTIME_REPAIR_AUDIT.md,
  which found 4.0e-3 with the previous code).
- Mid-block: run A stopped at step 33 (stage 1 step 3), resumed to 36 ("restored saved batch drawn at stage 1 step 0"); run B
  continuous to 36. Result: max |parameter difference| = 0.0.
Commands: python3 train.py --exp tmp/e1num_lbfgs_test.json --device cuda:0 --run-root tmp/e1num_sa_a --max-steps 30 --no-ledger --ignore-global-stop
          (then --max-steps 34 in the same root; run B with --run-root tmp/e1num_sa_b --max-steps 34); analogous for 33/36.
The frozen campaign ledger was not touched (--no-ledger); the campaign remains stopped.

# Preserved evidence (2026-10-23T08:21Z)
Both post-stop tests were re-run with all outputs kept in tests/evidence/ (README.md there): stage_boundary_resume/SUMMARY.json
(max parameter difference 0.0) and accounting_v3/test_ledger.jsonl + SUMMARY.json (13 unmerged intervals, gaps <= 2 ms uncredited).
