# Corrected interpretation of pool C timing counts

Checked 2026-10-31T18:55:52.947126+00:00.

CONFIRMED: the old candidate_calls metric counts calls to the outer timing wrapper. It includes prescribed prefix turns. The fresh-entry policy-call counts were already correct. Every one of the 144 completed game records agrees with its job prefix and per-round fresh-entry audit; a deliberately wrong wrapper count is rejected. No candidate or opponent is executed by this check.

| Candidate | Start | Wrapper calls | Prefix turns | Actual policy calls |
|---|---|---:|---:|---:|
| best_v9e | standard | 596 | 0 | 596 |
| best_v9e | mirror_7493_3 | 298 | 72 | 226 |
| best_v9e | asym_8669_2 | 330 | 48 | 282 |
| best_v9f | standard | 580 | 0 | 580 |
| best_v9f | mirror_7493_3 | 298 | 72 | 226 |
| best_v9f | asym_8669_2 | 330 | 48 | 282 |

For best_v9e the totals are 1,224 wrapper calls, 120 prefix turns and 1,104 policy calls. For best_v9f they are 1,208, 120 and 1,088. Original total_candidate_decision_seconds and max_candidate_call_seconds retain the timing-wrapper interpretation, including prefix-copy operations. They cannot be relabeled as isolated policy-only timings.

The original reports and receipts are preserved. The final pool D publisher now has explicit timed_decision_wrapper_calls, actual_policy_calls and prescribed_prefix_turns fields, together with wrapper total and maximum seconds. This check exercises that same accounting function on completed data. The declared D opponents, histories, protocol and start restriction are unchanged.

Reproduce with python -B -m bot_research.experiments.validation.check_decision_timing_accounting from the project root using the supplied environment, a free assigned low-priority core, disabled bytecode and research-local temporary files. The receipt is verification/accounting.json.
