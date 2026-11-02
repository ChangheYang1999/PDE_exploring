# Decision timing and prescribed prefixes

## Statement, notation and assumptions

For a completed match with R rounds, let P be the number of the candidate's prescribed prefix rounds actually played. Assume the evaluator calls its timing wrapper exactly once per player per round, and the prefix wrapper returns a prescribed action without invoking the underlying policy during those P rounds. Then the timing wrapper records R calls and the policy receives R-P calls. The recorded wrapper seconds include prefix-copy overhead and do not isolate policy-only time.

This is an accounting statement about evaluate.TimedBot around isolated_match.OpeningPrefix, not a performance bound. Every prefix in the two audited pool C campaigns ends before the corresponding match does. Each fresh entry-point audit records whether the policy was invoked on every round.

## Argument

In evaluate, each player is wrapped by TimedBot before collect_actions is called once in each game round. TimedBot appends one elapsed time in its finally block on each invocation. OpeningPrefix is inside that wrapper. Its first P invocations return deep copies of prescribed actions; only subsequent invocations call the candidate. Thus the R recorded durations comprise P prefix operations and R-P candidate operations. Summing this identity over conditions proves the aggregate count identity. The individual prefix durations cannot be recovered from only the total and maximum durations, so those aggregates must retain their wrapper meaning.

The independent check will compare R with the recorded game length, P with the actual job's prescribed action count and the per-round entry audit, and R-P with the regenerated-policy count. It will also reject a deliberately wrong wrapper count. It will read the completed best_v9e and archived best_v9f pool C campaigns without rerunning their policies. No pool D game or policy call is authorized by this check.

## Dependencies and scope

Dependencies are the original evaluator and prefix wrapper, the two completed pool C strict audits, their source archives and fresh-entry summaries, and publish_terminal_validation.timing_accounting. Existing result files remain unchanged. Addenda identify the earlier ambiguous field names. The corrected final publisher must keep policy calls, prefix turns and wrapper timings separate. These checks do not add independent strength samples or change any W/D/L result.
