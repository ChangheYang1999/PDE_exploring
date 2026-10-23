# Runtime repair audit

Updated 2026-10-23T07:19:34.870056+00:00. All verdicts below concern the immutable sources in `snapshots/repair-project-dd9c125438565393/MANIFEST.json`. The directory name records the first snapshot; its actual tested train.py SHA256 is **4444390f7ffb17b82c18c3765a5af7884aa2f488e6f920d754c8c418f1b2fe6f**. The actual ledger.py SHA256 is **e5d0d7cc089e51aae165866a6104091d6ac1747763992bbf1827ff9d8b8eec97**. This audit supersedes old source verdicts only for the repaired behaviors explicitly checked here. No other lane's files or processes were changed.

| Check | Method and result | Verdict |
|---|---|---|
| Copied physics and decoder tests | Ran all 17 tests on CPU, one thread. Every test passed; see `logs/repaired-numerics-tests.log`. | CONFIRMED |
| Physical-volume validation measure | Inspected validate: the global norm now uses disjoint core plus shell weights; axis and origin diagnostics remain separate. No retroactive correction of earlier metric files is implied. | CONFIRMED |
| Constant axial drift denominator | The norm of C times partial_z U is counted once. | CONFIRMED |
| L-BFGS objective resampling | A fresh batch at a resampling boundary with positive stage step reconstructs the optimizer, clearing history. Mid-block resume can retain a saved batch and its matching history. | CONFIRMED |
| Disk parameter rollback | NaN handling loads model bytes from ckpt_last, removing the old live-tensor alias defect. | CONFIRMED |
| Full NaN recovery | Counters, sampler, random generators and current batch are not rolled back. L-BFGS history is neither reloaded nor reset. The finite check uses the loss evaluated before the parameter step, so it does not itself certify finite new parameters or gradients. | REFUTED |
| Empty new activity record | An explicit chunks=[] produces zero activity, without legacy fallback. | CONFIRMED |
| Union of recorded numerical intervals | The union routine correctly unions the recorded rounded chunks. Those chunks are not yet exclusively eligible numerical computation. | OPEN |
| Exact eligible activity measurement | See the explicit step/I/O counterexample below. Short pauses and checkpoint I/O are credited; first steps and some long validation intervals are omitted. | REFUTED |
| Legacy enclosing intervals | The repaired ledger still treats floored display timestamps as exact containing endpoints, contrary to the saved records and the legacy source. | REFUTED |
| Resume across stage advance | The executed interruption test below produces parameter differences up to 0.004001681978285876 after the same four optimization steps. | REFUTED |
| Fast-derivative accuracy claim | The copied test passes, but its tolerances are function 1e-12, Jacobian 1e-11, Hessian 1e-10 and relative parameter gradient 1e-9. It does not establish all quantities to 1e-12. | CONFIRMED with stated tolerances |

## Executed stage-transition counterexample

`validation/run_stage_resume_probe.py` executes the frozen trainer in continuous, interrupted, and resumed modes. Both stages use two Adam steps and resample_every=5. The real Euler objective, collocation draws, parameter updates, RNG, serialization and stage counters are unchanged. Only validation is replaced by inexpensive deterministic metrics; validation does not supply the optimization loss. The interrupted run exits immediately after the atomic stage-advance checkpoint. All work is local, one CPU thread. These software tests receive no campaign-time credit.

At stage advance, train.py lines 517-520 advance stage and reset step and optimizer, but retain cur_batch from the previous stage. Checkpoint lines 354-355 save that old batch using only step_drawn, without a stage identifier. Resume line 422 accepts it when step_drawn matches the new stage's block start. In this test both are zero. The resumed log confirms restoration of the old batch. The continuous run draws a fresh one.

Both final states have stage=2, step=0 and global_step=4. Their maximum parameter difference is **0.004001681978285876**. Full tensor differences and scope are in `evidence/stage_advance_resume_counterexample.json`; logs are `logs/stage-resume-continuous.log`, `logs/stage-resume-interrupt.log`, and `logs/stage-resume-resume.log`. The existing mid-block resume test is compatible with this distinct failure.

Repair: clear cur_batch before saving stage_advance, and attach and validate the saved batch's stage, sampling configuration and counts. Test both an interruption inside a block and one immediately after stage advance. Saving sampler state alone does not establish batch identity.

## Activity counterexamples

The worker credits t minus t_last_step between accepted step ends whenever this gap is at most 30 seconds. It does not instrument the actual numerical work boundaries. For a previous step ending at epoch 100, checkpoint I/O until 110, and one numerical step from 110 to 111, the recorded chunk is [100,111]. Its union is 11 seconds, though the additional eligible optimization interval is only one second. Closing a chunk during checkpoint does not solve this: t_last_step is retained, so the next chunk starts before the I/O. A short suspension has the same problem. A gap over 30 seconds can instead discard legitimate validation and computation.

Instrument explicit optimization and validation begin/end events, synchronize the GPU at boundaries, and exclude serialization, setup, logs and pauses. Use monotonic duration and full-resolution epoch placement. Only merge adjacent intervals that actually contain continuous eligible work. A union can be exact for the stored rounded endpoints while the inputs still fail the prompt's activity definition.

The legacy synthetic record [0,1] with active_seconds=1.4 causes the repaired lower and upper bounds both to be 1.0, which cannot enclose 1.4 seconds. Real legacy data have the same endpoint failure: four of 22 immutable records report longer activity than the displayed interval. `research/ledger-bounds/PROOF.md` and `evidence/ledger-bounds-ace268c70c2f4ad9.json` give conservative corrected bounds with explicit clock/protocol assumptions. Those bound credited elapsed chunks, not uninstrumented eligible compute.

All interval and branch counterexamples were executed using the copied ledger functions. See `validation/runtime_repair_audit.py` and `evidence/runtime_repair_counterexamples.json`. No 96-hour claim is supported.
