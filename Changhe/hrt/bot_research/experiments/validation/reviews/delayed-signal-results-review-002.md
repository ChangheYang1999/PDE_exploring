# Protocol 159 explanation revision review

Reviewed 2026-10-31T21:52:14Z. Actual reviewer model: GPT-6 Astra. I authored the underlying informal proof and the earlier checker and results reviews. This is a source and retained-byte review, with zero engine replays and zero policy calls.

**RESOLVED.** `analysis/delayed_signal_ambiguity/EXPLANATION_v2.md`, relative to `bot_research/experiments/validation/`, explicitly restricts the common G/L opening to the H and S comparisons. This resolves the local qualification issue recorded in `reviews/delayed-signal-results-review-001.md`. The only other changes from the retained first explanation are the dated revision paragraph and spacing in the expression `-1/3`. The payoff table, restricted selector class, normalization of names, continuation-coupling hypothesis and deadline limitation are unchanged.

**CONFIRMED.** I rehashed every direct input in both narrative receipts: all eight entries in `verification/explanation_inputs.json` and all six in `verification/explanation_inputs_v2.json` match. The second receipt includes the first explanation and its receipt, the new explanation, the proof, results and full verification receipt. This preserves the earlier narrative and evidence while recording a separate post-result correction. It does not amend the prospective protocol 159 declaration retroactively.

The v2 explanation SHA-256 is `c713499459c7e2b3c6f01cf7307ebe45b06eaa537c8eded78867e380d38d43a6`. Its receipt SHA-256 is `f9ab600a7801556b65a1721b9a302966ba7431f5e7896e084f10ff71b0d9a58f`. The preceding review remains unchanged at `6eb6b1fc845ff63337314b5aaa1d93226b0da44a11bff9d32e6733624e4be6d8`.

No additional material consistency issue was found in the three changes. The retained finite outcomes do not establish unconditional cross-execution deadline coupling or a bound on unrestricted policies. Those limitations remain explicit in v2 and in the preceding review.
