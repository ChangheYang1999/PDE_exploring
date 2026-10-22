# P349: final numerics time-source audit

Recorded 2026-10-22T11:29:39.744822+00:00. Independent checker passed **79/79** controls at 11:26:42.188654 to 11:26:42.208129 UTC (0.019490 s). Source hash 8b780882e99dbbe67e5d17f47a6eeccbcd1f74879d679c51e0b9ab2f954051ae; proof c1b9a31ac6bc3710f8fa96989d5658a1f0152e2331787e1f88218b10572eb3f1. No numerics-lane code was imported or executed.

**CONFIRMED:** the actual NUM_REPORT differs from P333 only in two provisional time passages, and all five approved artifact files are byte unchanged. The eight recorded completed shifts have exact occupancy 167486 s, floored occupancy 2787 min, and floor loss 266 s. Eight explicit restart gaps sum to 240 s. At the example cutoff12:42:00, wall time is172667 s, exact occupancy172427 s, summed floored occupancy2869 min and floor loss287 s. Session occupancy is not measured active work.

**REFUTED:** source6c3a53fc identifies every minute-floor q>=12:44:00 as at the horizon12:44:13. Both q=12:44:00 and q=12:45:00 contradict this label. Its rounded pre-write clock also cannot establish the actual last activity or lane end. The phrase ran no computation is broader than recorded integrity checks and a planned consistency checker.

**OPEN:** repaired source, actual final write, write-side classification and final run end. The concrete repair note in NOTES_FOR_TEAM.md requires an explicitly UTC unrounded event/cutoff, exact comparisons with12:44:13, and separate actual end/write evidence. It does not request or claim changes to the mathematical report or approved data.

Actual Opus5.5 request613 returned no public audit text and supplies no endorsement. Request614 checked the arithmetic and reasoning, but I caught its statement including the equality second among after-cap times. Request615 corrected that endpoint and closed the scoped review. The proof and checker already used equality correctly. The model did not inspect hashes or execute controls; metadata, not model self-report, confirms the actual returned model. General B2 remains OPEN.
