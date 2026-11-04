# NEAR_CHECK_v07 errata (the first theory agent)

Written 2026-11-04T10:43Z. NEAR_CHECK_v07.md stays frozen and unchanged; this file records corrections to its text.

E-v07-1 (AT2575, audit_v782). Section 1, second paragraph, says that the version 1 record near_params_v04.json has a
beta_star that "differs from near_params_v03 only in its source text, so beta_star is checked by value and kind".
This is false as written. The beta_star dictionaries of near_params_v03.json and near_params_v04.json are equal,
including the source text (rechecked here with json.load at 10:43Z), and mk_params_v05.py compares every entry other
than the four (R4) entries with near_params_v04.json as a full dictionary (lines 15 to 20 of the builder) before it
changes the status and source of beta_star; line 34 then asserts the value and the kind. The implemented check is
the stronger one and passes. No printed value, margin or status of NEAR_CHECK_v07 changes (AT2573, AT2574
CONFIRMED; AT2576 OPEN).
