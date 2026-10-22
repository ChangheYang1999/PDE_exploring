Written 2026-10-21T20:11:00.597327+00:00 before rerunning the corrected scalar audit. Read with PROOF.md.

The last source-code paragraph in PROOF.md is superseded: the live code changed between the earlier read and the20:08:38.557454 snapshot. The frozen current main_B now reads dist_rel conditionally and no longer reads cos2_low. The first scalar audit reached the source assertion only after the numerical checks and failed there; its source and log are preserved. No completed result or verdict was written.

The new assertion checks that main_A saves cos2_full and dist_rel but not cos2_low, and that main_B now reads the first two names and not cos2_low. Thus the schema objection applies only to the earlier unsnapshotted live read and is withdrawn for this frozen version. The new B outputs must still use the actual v2A files; the three snapshotted old B JSON files all refer to v1A files. Those binding claims and the projection-energy arithmetic are unchanged.

No Gram or image is recomputed here. The1.8percent distances are scalar diagnostics from saved floating energies. They are not rigorous distances of an independently verified physical projection.
