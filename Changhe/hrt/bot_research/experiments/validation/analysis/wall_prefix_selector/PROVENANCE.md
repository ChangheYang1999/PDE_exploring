# Amended-checker provenance supplement

Recorded 2026-10-31T21:15:24.256837+00:00, after the game and checker executions. This document supplements the existing final receipt; it does not replace or edit any declared input or prior result.

The version-two checker verified its four amendment pins at entry and exit, but its branch and final receipt builders initialized their input maps from the original declaration and campaign freezes. They consequently omitted direct edges to the amendment and the new checker/helper. The separate source review identified this receipt-closure gap before publication. `verification/provenance_supplement.json` adds those edges, checks every direct input edge of the declaration, amendment, three branch receipts and final receipt, and pins this sealer and the source review. The amendment time precedes each campaign's recorded start. These are checks of retained bytes and recorded timestamps, not a new independent attestation of past process state.

The review also identified two conditional reporting gaps. A changed actual branch would make the preselected baseline label inaccurate, and a non-draw self result would stop the publisher before its final falsification report. Neither was exercised here: every observed branch equals its predeclared branch, the full predicted row check passes, and both self games draw. The supplement explicitly checks these conditions before accepting the successful finite certificate. It rechecks that certificate with exact rational arithmetic.

Logical-state comparisons exclude shared module globals, alias identity and process time. The conditional common-prefix proof and measured execution scope remain unchanged. There are no new policy calls or strength games in this supplement.
