## 2026-10-28 13:00Z (num, a session, team message 26: V186 to V189 taken up: assembler v3 with the expected cell set, exact quotient templates, the error model is accumulation-only)

Verifier, theory author. Thank you for V187 to V189; all three points are accepted and acted on.
1. V188 (coverage). fsec_assemble.py v3 (13:00Z): the run's cell set is now written to meta.json at launch (fsec.py cells_expected) and, for the
   three existing runs S1, S1M3, S1M4P, recorded in a sidecar runs/<tag>/cells_expected.json (all 1569 cells, four workers, never resumed).
   The assembler requires union(done sets) == expected set (missing and extra listed; an incomplete run aborts unless FSEC_PARTIAL=1 marks an
   explicitly partial diagnostic). Legacy parts without done sets get their cell sets reconstructed from the deterministic assignment
   sorted(expected)[w::nw] (the chunks line of fsec.py), checked against the diag counts. S1 re-assembled under v3: 1569 cells, missing 0,
   extra 0, values unchanged (4.15523, 6.08407, 23.31349). The S1M3 re-assembly is paused by the CPU guard behind S1M4P and will be confirmed
   when a core frees (same parts, so the same values are expected). The eigen-solve is now a 50-digit whitening followed by a double
   eigen-solve of the whitened matrix (entries O(1e6)), which gives the same digits as the 50-digit eigsy and takes seconds instead of minutes.
2. V187/V189 (division). The input quotients VM[m] are now the exact integer templates Q_j = 2 (-1)^(m-1-j) (2m-2j-1) (fsec.py prints the
   difference to the former pinv value). The three runs on disk (S1, S1M3, and S1M4P, which started 12:42Z before the fix) used the pinv
   quotients, so their domain Grams G_Z carry the padding-dependent input error of about 1e-7 relative (your 9.31e-8 for m = 1); my statement
   in team message 24 that the m = 1 block of S1M3 "reproduces S1 exactly" is therefore wrong at that level and is corrected to "to 1e-7 relative" in
   the deliverables. The output division (image quotients through the same pseudoinverse) is NOT controlled by any model I have; with your
   amplification factor 5.4e10 at padding 533 the accumulation-only estimate 1.3e-12 (sum |x_i| sqrt(diag))^2 is incomplete, so the words
   "resolved" / "quotient in [a, b]" in team message 22, 24, 25 and in the files now read "resolved with respect to the accumulation rounding only;
   the division errors are not covered". All section values remain FLOATING diagnostics; nothing about them was ever labelled certified.
3. Not changed: the qualitative statements (near-null outer-column directions; the pure-spline m = 1 + m = 2 coupling value 3.4557, which you
   reproduced independently, against 50.32 and 25.47 for the single modes). S1M4P (pure splines, m = 1, 2, 3) is at 38/392 cells per worker
   (21 s per cell, done about 15:00Z); its assembly uses v3 and the double eigen-solve.
