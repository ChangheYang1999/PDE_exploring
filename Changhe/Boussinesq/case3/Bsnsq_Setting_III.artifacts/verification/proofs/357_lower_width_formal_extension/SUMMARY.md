# Order12 finite extension and width comparison

Updated 2026-10-22T12:23:08.423339+00:00. CONFIRMED816/816 own finite consistency controls. The width200 run completed order12 at2026-10-22T12:19:21.508498+00:00 with368/368 internal controls; requested order12 was reached. The timeout wrapper and child were absent at the freeze observation2026-10-22T12:20:55.281617+00:00. The exact exit instant was not observed. Metadata and coefficient bytes were stable across two reads and their completed field indices and leading coefficients agree.

The comparison to width300 covers finalized theta<=11, omega<=10, v<=11. All16610 powers agree, with6526 nonzero and10084zero values. The exactly polynomial v0 uses a10000-power sentinel range with3nonzero and9997zero values. Excluding that polynomial range leaves6610 powers,6523nonzero and87zero. At least186 shared powers are compared for every field; the new run's minimum internal residual range is182powers. Stage12 has internal controls but no width300 comparison.

Both runs share the verifier's recurrence source and exact Fraction arithmetic. This proves equality at the two tested widths on the finite shared ranges, not width-independence at all truncations, an independent derivation of the PDE, or a convergence theorem. Poisson updates are definitional consistency controls. No full-plane profile or endpoint follows.

Actual Opus631 returned claude-opus-5-5 and reviewed the reporting scope. Its proposed shorthand about ruling out width-dependent truncation is restricted here to the two observed widths. Its compressed sentinel/process wording is not adopted; the exact counts and observed event are stated above. General B2 remains OPEN.

Evidence: [standalone proof](PROOF.md), [checks](verification/checks.json), [freeze and hashes](verification/freeze.json).
