# Provenance loss across a logarithmic-checkpoint restart

Status: CONFIRMED provenance-loss defect, V375. Source-level inspection and an actual save/load roundtrip agree.

## Claim and scope

A continuation whose input coefficient balls were replaced by their midpoints remains conditional on those midpoint arrays after saving and loading a checkpoint. Saving and loading do not restore the discarded input uncertainty. Consequently, narrow arithmetic radii after a restart must not change that continuation's classification to an unconditional enclosure of the original canonical coefficients.

The inspected numerical implementation writes coefficient arrays, statistics, parameters and resonance information to its checkpoint, but does not write the object attributes `radii_reset_at` or `perturbed_seed`. Its loader likewise does not restore these attributes, including from the saved historical statistics. The method computing subsequent statistics uses the presence of `radii_reset_at` to force `midpoint_only=True`. This dependence loses the conditional classification across a restart.

## Argument

Let C be an exact canonical coefficient array contained in a previously certified interval array I. Replacing I by its midpoint array M chooses one possible numerical state; it does not prove C=M. A subsequent recurrence evaluation from M therefore concerns that selected state. A lossless serialization of its coefficient balls leaves their mathematical meaning unchanged. Discarding a provenance attribute cannot supply the missing equality or propagate the discarded uncertainty. Thus the conditional classification is an invariant that the checkpoint representation must preserve.

The finite reproduction creates a low-order logarithmic state at delta=2/3 and assigns the same conditional attributes used by the production command. It computes statistics, saves, reloads, and recomputes statistics. The expected mathematical classification is unchanged. If the attributes disappear and the flag changes from true to false, this demonstrates the metadata defect without making any claim about the numerical recurrence values.

The observed production log supplies a separate instance: its first segment resumes from329 with `radii_reset_at=329`; its second segment resumes from350 with `radii_reset_at=null`; the order351 row has `midpoint_only=false`. It is still the same conditional continuation.

## Required interpretation

All descendants of a reset state must remain explicitly conditional unless an independent error argument certifies the discarded input uncertainty. Persist the reset and perturbation provenance in the checkpoint. For old checkpoints, recover a reset only from unambiguous saved history or explicit external provenance; missing metadata alone is not evidence that no reset occurred. Existing coefficient enclosures and earlier unreset certificates are unaffected.

This is an implementation/provenance result. It is not a convergence theorem or a claim that the conditional numerical midpoint values are inaccurate.

## Completed reproduction at 2026-10-31T14:06:30+00:00

A low-order512-bit save/load/recompute test changes radii_reset_at=1 and perturbed_seed=17 to missing attributes, and midpoint_only=True to False. The production log independently shows resumed_from350 with radii_reset_at=null followed by order351 with midpoint_only=false. The unchanged lineage remains conditional on the329midpoints. Runtime0.006024031899869442seconds; source snapshots and the production excerpt are retained in topic190.

## V406 | 2026-10-31T14:43:09+00:00 | Tested local repair of lost checkpoint provenance

Claim: The proposed patch repairs the demonstrated reset/perturbation metadata loss for new checkpoints and legacy checkpoints with unambiguous reset statistics.

Method: Apply a textual patch to a local source copy and perform four serialization/restart/statistics checks against the unmodified loader.

Result: A local proposed patch persists radii_reset_at and perturbed_seed and recovers the earliest unambiguous reset from legacy saved statistics. Four actual low-order roundtrips pass: unreset, midpoint-reset, boundary-perturbed, and legacy-reset checkpoints. All coefficient arrays equal those returned by the unmodified loader, so the patch changes provenance only. An old perturbation seed that was never saved cannot be reconstructed from the checkpoint alone. No numerical-experiment source or active process was modified. Runtime 0.13666130090132356 seconds.

Verdict: CONFIRMED for the proposed local patch and stated cases. Production remains affected until its owner applies the repair and handles active processes and historical logs. This does not certify discarded canonical input uncertainty.

## Production adoption, 2026-10-31T14:59:14+00:00, V412

The production source is byte-identical to the source tested by the four V406 roundtrips. Hashes are recorded in verification/production_applied_check.json. Already running processes still use the old source; their later outputs require the external provenance correction.
