# Runtime-audit amendment

Written 2026-10-31T20:50:27.513820+00:00. Both original policy children stopped at the initial-header equality check at 20:48:15 UTC, before constructing or calling the policy. No component child was started. Their logs are retained.

The original Engine generates the game header. The research harness adds exactly research_specs, research_scenario and research_metadata (harness/match.py, lines264 onward). The checker omitted these fields. Version2 reconstructs their exact expected values from the pinned result row and compares the entire initial record, including game state and metadata. It does not strip fields or edit any input. Both initial headers now agree; altering the initial gold is rejected.

The hypotheses, selected histories, candidate, all original source pins, call counts and output names are unchanged. Version1 and the first declaration remain pinned. This amendment additionally pins version2, this explanation, the original declaration and both failure logs. This is a checker correction, not an outcome-dependent retry. No candidate timing was obtained in the first attempt.
