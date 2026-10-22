# Actual adoption of the numerical clock repairs

Prepared 2026-10-22T11:57:29.626432+00:00, before controls. This packet checks actual source22cff613 against the frozen source7e83086d of P352. It does not execute or import numerical-lane code and does not certify a final APPLY.

## Statement and method

The P352 equality defect is repaired if the source now explicitly distinguishes pre<CAP, pre==CAP and pre>CAP. The record-format defect is repaired if one formatter puts the fraction before the terminal Z and that formatter is used exactly once per sample in the record. The report's retained whole-second display is honest if its surrounding text explicitly says it truncates an underlying unrounded sample and identifies the record containing microseconds. The conservative write bracket remains before when post<CAP, after when pre>CAP, unresolved otherwise; a label saying contains or touches correctly covers equality and straddling cases. Confirm these exact changes by AST/text inspection and a complete source diff, then evaluate their elementary formatter and order rules in independently written code. No foreign function or AST is executed.

The formatter round trip preserves every microsecond for the tested values because strftime places six fractional digits before Z, and the independent parser restores them. The three-way classifier is correct by trichotomy of real timestamps. The bracket assertions are correct under the ordered-write hypothesis of P352 by transitivity. Source timestamps remain naive UTC, and our independent samples use aware UTC consistently. Source repair proves conditional behavior only. Actual final APPLY, the current output hash and manual log entries still require a separate readback.

The current document's opening shorthand 'UNROUNDED UTC clock sample (seconds)' is less precise than the implemented fractional sample; the report passage itself explicitly distinguishes sample and display precision. It does not justify reading its displayed seconds as an exact fractional timestamp. The report still refers prospectively to the actual session end and later manual entries. Those future events are OPEN until observed. The script's temporary-file close/flush ordering remains a CPython implementation assumption as disclosed in P352.

## Scope

CONFIRMED or REFUTED is restricted to the exact source changes and independent elementary controls. It cannot certify a future execution, measured active research duration, numerical PDE result or general B2 endpoint. Dependence: P352. Restrictions: no JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake, commits/pushes/posts or human contact; writes only in verification.
