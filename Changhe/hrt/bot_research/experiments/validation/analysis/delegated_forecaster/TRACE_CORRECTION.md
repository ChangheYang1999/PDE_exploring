# Forecast trace capture correction

Written 2026-10-31T17:14:17.019340+00:00, after the first eight games of manifest version 001 and before any version 002 game.

The first eight version 001 games completed successfully on the original engine and passed strict, replay and data-archive checks. The forecast audit then raised KeyError for forecast_trace because run_data_development invokes isolated_match, which records actions but does not capture a policy's trace. This was an experiment-driver error. Those eight games and the failed audit log are retained unchanged except for removal of absolute workspace prefixes from the traceback.

Version 002 keeps every candidate, parameter, target, assignment and order unchanged. The new run_data_forecasts module is derived from run_data_development by changing its own source-root name and invoking the existing forecast_match recorder. It preserves explicit JSON input registration and source archives. forecast_match reads the private policy trace only after the completed game; it never supplies it or pending actions to either policy. No policy or game-engine code changes. Register this correction and the new runner as inputs before execution. Re-run the original eight conditions as exact complete-history controls, followed by all remaining seventy-two declared conditions. The original eight do not add independent evidence.

The original declaration and component checks remain valid. Full-game forecast correctness remains OPEN until every actual captured prediction is checked and both policies are regenerated on the recorded public observations. A missing trace is not a successful forecast.
