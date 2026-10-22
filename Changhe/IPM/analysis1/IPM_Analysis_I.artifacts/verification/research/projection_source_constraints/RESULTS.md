# Literal exact source-constraint results

Primary check completed2026-10-21T20:43:27.666518+00:00. Final review and adjudication still pending.

All results use the explicit frozen-column interpretation. The v2 vector files do not contain join coordinates or a column-pickle hash; historical execution is not attested.

|vector|nonzero rows / rows|maximum absolute exact defect, strict decimal window|location|
|---|---:|---|---|
|NJ0,free=False|32/32|(162336474/10^20,162336475/10^20)|[{'mode': 2, 'join_index': 0, 'order': 0}]|
|NJ1,free=False|64/64|(1360810768/10^20,1360810769/10^20)|[{'mode': 12, 'join_index': 0, 'order': 1}]|
|NJ1,free=True|64/64|(1347159955/10^20,1347159956/10^20)|[{'mode': 1, 'join_index': 0, 'order': 1}]|

All160 rows are nonzero. The maximum windows are strict because none equals its displayed rational lower endpoint. Exact row fractions and tighter outward windows are in evidence/checks.json.

These are source-only function-column constraints. No inference about physical joins, KP/TAU cancellation, an ideal projection, Sobolev norms or the IPM inverse follows. The normalized cancellation diagnostics and convention checks are complete below.

The supplemental checker completed2026-10-21T20:45:22.507532+00:00. Each of the160 source matrix rows has a nonzero entry and a positive absolute-product sum. The exact maximum cancellation ratios have these strict upper bounds:

- Kproj2_M16_s16_NJ0.npz: 214838/10^20.
- Kproj2_M16_s16_NJ1.npz: 752953/10^20.
- Kproj2_M16_s16_NJ1_free.npz: 574764/10^20.

These scale-free numbers are literal cancellation levels, not roundoff-error or correction-distance estimates. All7812 source endpoint floating diagnostics were compared with exact traces, plus4 manufactured signed endpoints,10 interior value/derivative cases and2 explicit exceptional-incidence/gate cases. The first manufactured derivative target was18 instead of13; the diagnostic rejected it. MANUFACTURED_CORRECTION.md is mandatory and preserves that failed attempt.
