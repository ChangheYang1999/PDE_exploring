# Notes for the team from numerics team (newest first)

## 2026-10-28 17:02Z (num, a session, team message 30: S1J1 input Gram against the verifier's exact V267 export; C7 family values re-derived with directed rounding; no further computation)

Theory author (note 6x item "Numerics"), verifier (V267).
1. S1J1 input Gram G_Z (38 columns, four parts summed, symmetrized; part asymmetry 7e-15) against proofs/239_s1j1_full_input/evidence/check.json
   runs[1] (640-bit balls, antiderivative moments; the export records the SHA256 of my runs/S1J1/meta.json and of the frozen producer files, all
   matching): largest entrywise relative discrepancy |G_ij - mid_ij| / sqrt(mid_ii mid_jj) = 6.01e-7 at the diagonal of (sp9, m = 1) (non-outer
   block); the outer power-column block agrees to 1.2e-9 and the cross block is exactly zero (compact supports); median 0; ball radii at most
   1.0e-163 relative. Whitened quadratic-form relative error 4.31e-4 (60-digit mpmath whitener of the exact midpoints; identity defect 1e-50;
   the radius term is 1e-152): the entrywise 6e-7 is amplified along the near-null directions of the extended columns (sp0+in/sp1+in at
   normalized Gram eigenvalue 2e-11, sp2+in 1.3e-8), the same value on the 33-column non-outer block alone. Since S1J1 used the exact VM
   templates, the 6e-7 at sp9 is not the quotient error of V187 but the floating input quadrature (3 Gauss nodes per spline cell against the
   weight e^{8t + mu_a}) and double accumulation; it is of the same size as the S1M4P discrepancy (7.4e-7 at sp9, m = 3; 2.7e-6 quadratic form
   there, where no extended columns are present). FLOATING comparison, input side only; nothing follows for B_Y. work/gram_compare_s1j1.py,
   logs/s1j1_gram_compare.log, runs/S1J1/gram_compare.json (artifacts/data/S1/S1J1_gram_compare.json).
2. For the NUMERICAL row (your note): smallest floating generalized singular value of S1J1 4.7481 (Rayleigh quotient of the computed direction
   weakly resolved, [3.74, 5.58] under the accumulation model; the direction is the near-null matching combination of out5/out8/out9), next to
   4.1552 ([4.137, 4.174]) of S1 with the junction at t_+; without the outer power columns 50.32; details in team message 29 and basis report 7.8.
3. C7 re-derivation (second-model referee follow-up, work/family_recheck.py): the whole-plane family combination recomputed with every float operation
   rounded toward the valid side (no 1e-12 slack; Delta rounded up where q >= 0, down where q < 0; every box finite; refinement arrays on the
   base geometry): m_fam(4, 0.3) >= 1.129601 before the outer-cover addenda and m_fam(3.6, 0.3) >= 0.959670, floats identical to the
   family_combine.py values. C7 stands (truncated 1.1296 and 0.9596; with the outer covers 1.250190 for (4, 0.3)).
4. This team runs no further computation. Until 18:15Z: artifacts and documentation only (artifacts/README.md lists every command and data file).

## 2026-10-28 16:58Z (num, a session, team message 29: S1J1 junction test done: the far-junction value moves from 4.16 to about 4.7 (weakly resolved) and stays in the outer power columns; bulk unchanged; a rounding correction (m_fam >= 1.250190); referee-hardened scripts)

Theory author (team message 32, team message 59 item 6), verifier.
1. S1J1 DONE 16:52Z (4165 s on 4 workers; one worker was guard-paused 10 min behind OUTER_F8): the S_1 core section with Mh = 2 (angular
   remainder mode m = 1 only), the four sp+out columns dropped and the five outer power columns out5..out9 attached at t_+ + 1 instead of t_+
   (basis.py BASIS_OUT_SHIFT=1, fsec.py FSEC_DROP=+out; 38 columns; exact VM templates; settings record and frozen producer copies with SHA256 in
   work/runs/S1J1/). Coverage 1569/1569 (assembler v3), never resumed. Diagnostics: axis residual 1.2e-15, division residual 8.8e-8, trace-jet
   1.4e-14. logs/s1j1_prod.log, s1j1_chain.log; work/runs/S1J1/fsec_result.json.
2. Values (FLOATING; accumulation-only rounding model; division errors not covered, V187/V189): 50-digit generalized singular values 4.7481,
   15.1419, 34.287, 44.210, 51.576, 53.158, ...; on c[h_0] = 0: 4.7482, 15.142, 34.289. The weakest direction is again the near-null combination of
   the outer power columns, -0.79 out9 + 0.56 out5 + 0.25 out8 (normalized Gram eigenvalue 9.0e-12), with x^T G_Z x = 1.98e-8 against the rounding
   estimate 9.8e-11 and x^T B_Y x = 4.47e-7 against 1.7e-7: its Rayleigh quotient is only WEAKLY resolved, in [3.74, 5.58] under the model (S1 at
   the junction t_+: 4.1552 in [4.137, 4.174]). The next two values (15.1, 34.3) sit in the same outer-column near-null space with image quotients
   at the rounding level: undetermined. Dropping normalized-Gram directions below 1e-10 leaves 5.84, 22.0, 44.2; below 1e-6: 8.31, 35.6, 45.7.
   Without the outer power columns (33 columns): 50.32, 51.58, 53.16; the 26 pure splines: 50.3201 (identical to S1 and S1M4P m = 1, same columns).
3. Reading for team message 32: the small far value is NOT tied to the junction location t_+ (it moves only from about 4.2 to about 4.7 when the power
   laws are attached one unit further out) but it IS tied to the outer power-law columns themselves: it lives in their near-dependent matching
   combination (the shared e^{alpha_1 tau} tail), where the image quotient is at the rounding level of the computation, and it disappears when
   those columns are removed (>= 50 on the splines, m = 1). So on the m = 1 subspace the only value below 50 is an ill-conditioned power-law
   artifact of the far basis, not a bulk phenomenon; the genuinely small values of the sections are the pure-spline mode-coupling values
   (3.46 for m <= 2, 2.77 for m <= 3, team message 24 and 27). Numerical evidence only. Entered as S2_BASIS_CERTIFICATION 7.8, N4, NUMERICS_REPORT 10(g).
4. Correction to team message 28 (second-model referee merge_gram_ref, 16:05Z, on outer_merge2.py and gram_compare.py): printing with %.6f rounded two lower
   bounds UP. m_fam(4, 0.3) >= 1.250191 must read >= 1.250190 (float 1.2501909638); the C4 addendum-1 figure 3.058367 on [t_+, t_+ + 1/2] must
   read 3.058366 (float 3.0583669728). The headline values are safe: inf m_a >= 3.000000 (float 3.000000251655344), 2.9270 (V197), 2.482724.
   Both scripts were hardened as the referee asked (contiguity and exact tiling of the computed cells, every retained or replacing box finite,
   Delta >= 0 and a_ang <= 17/4, refinement arrays on the base geometry, directed float recomputation of m_fam, floored printing; mpmath
   entrywise comparison, e + r < 1 check, ball-radius term) and rerun: all floats identical (logs/outer_merge2_f403_f8_v2.log,
   s1m4p_gram_compare_v2.log: 7.414e-7 entrywise, 2.688e-6 quadratic form, radius term 2.2e-144). All files corrected 16:10Z.
5. Remaining for this team: documentation and artifacts until 18:15Z; no further computation is planned.

## 2026-10-28 15:58Z (num, a session, team message 28: finer outer cover of the whole outer region: inf m_a >= 3.000000 over the plane; m_fam(4, 0.3) unchanged at 1.2502 and no longer limited by the outer region)

Theory author, verifier (a small certified improvement for the record; verify if time allows, otherwise it stays team-certified).
1. OUTER_F8 (margin.py, 15:43Z-15:53Z, one process, 620 s): the outer region [t_+ + 1/2, t_+ + 8] covered by 16 cells of widths 1/8, 1/4,
   1/2, 1 (the 24-offset cover MARGIN_OUTER_EXTRA = 1/16, ..., 7/16, 1/2, 5/8, 3/4, 7/8, 1, 5/4, 3/2, 7/4, 2, 5/2, 3, 7/2, 4, 5, 6, 7, 8; cells
   1571..1586, work/runs/outer_cells_f8.json), every angular box refined to depth 6 (4096 leaves), family (4, 0.3) tracked, otherwise exactly the
   C4 setting (same exact trial, weights, encl.py enclosures, 160/512 bits). Per cell: m_a >= 3.0368 .. 3.0896 (old production bounds on the four
   cells [t_+ + 1/2, 1], [1, 2], [2, 4], [4, 8]: minimum 2.9271), m >= 2.9942, m_fam(4, 0.3) >= 1.3407 .. 1.4169.
2. Combined with OUTER_F403 (the first half unit, 12:44Z) and the production arrays elsewhere (new script work/outer_merge2.py: each run replaces
   exactly the production cells it tiles, asserted; logs/outer_merge2_f403_f8.log; work/runs/OUTER_F8/outer_merge2.json):
   inf over the plane m_a >= 3.000000 (float 3.000000251655344; before 2.9270 = V197), now attained as a bound at the production cell 1188
   (t_a = 5.1695, r about 176), angular box 3, a refined bulk box (31 leaves), with 4455 production boxes within 0.01 of 3: the far region no
   longer limits m_a, the bulk does. inf m >= 2.482724 unchanged (cell 525). m_fam(4, 0.3) >= 1.250191 (unchanged to six digits; the limiting cell
   moved from the outer sub-cell to the production cell 1338, t_a = 6.3452, r about 570, box 61, inside the near-axis refined range: deeper
   refinement there would be the next step; not run).
3. Status: directed lower bounds from the same box data as C4 (the dropped-constant conditionality of C4 applies). Entered as C4 addendum 2 and
   C7 addendum in S2_NUMERICAL_CERTIFICATES.md (team-certified, "not independently verified"), NUMERICS_REPORT 7 and 11, S2_RESTART. Data for a check:
   work/runs/OUTER_F8/margin.npz (per-box arrays MA_ref, M_ref, MF_ref, NREF on the 1588-cell cover; cells 1571..1586 computed), margin.json,
   and runs/OUTER_F403/margin.npz; base arrays runs/MARGIN_REF2/margin.npz. If you adopt the value, the theory author's "m_a >= 2.9270 THEOREM (V197)"
   can read "m_a >= 2.9270 (V197); the numerics team has 3.000000 (unverified)". Nothing else changes.
4. S1J1 (junction test) is at about 50/393 cells per worker (one worker was guard-paused for 10 min behind OUTER_F8): expected 17:10Z-17:20Z.

## 2026-10-28 15:52Z (num, a session, team message 27: S1M4P complete: the pure-spline section falls further with m = 3 (2.7655); m <= 2 reproduces 3.4557; input Gram against V202: 2.7e-6; S1J1 and the finer outer cover running)

Theory author (team message 47 item 4 and 5, 50 item 5), verifier (M4P audit).
1. S1M4P finished 15:41Z (10758 s on 4 workers, 27 s per cell): 1569 cells in four disjoint parts, coverage 1569/1569 against the sidecar
   expected set, never resumed (no base_*.npz, no 'resume:' in logs/s1m4p_prod.log, four 'worker N done' lines). meta.json is untouched
   since 12:45Z (the SHA the verifier recorded). The producer was the 12:41Z fsec.py with the pinv input quotients; that file was NOT frozen
   before the 13:00Z edit and no byte copy exists: runs/S1M4P/PRODUCER_PROVENANCE.md records what is known about it (the three later edits
   touched only the VM templates, the settings record and the resume refusal; sampling, images and accumulation unchanged) and the SHA of the
   current fsec.py. The verifier's check.py expectations (four parts, round-robin done sets, no resume, 78 new columns) are met.
2. Values, all FLOATING diagnostics (accumulation-only rounding model; the division errors of the image quotients are not covered, V187/V189;
   the input Gram carries the pinv quotient error measured in item 3). Pure splines sp4..sp29, modes m = 1, 2, 3, 78 columns, S_1 section on
   L^2(w_a), complete mode set (NMAX 534):
   - 78 columns: smallest generalized singular values 2.7655, 3.2685, 4.3913, 5.3953, 5.6169, 6.8798 (50-digit whitening, double eigen-solve;
     scipy agrees to all digits shown); on the subspace c[h_0] = 0: 2.7662, 3.2695, 4.3933. Rayleigh quotient of the weakest computed vector in
     [2.7655, 2.7656] under the accumulation model. Normalized input Gram smallest eigenvalue 1.36e-5; dropping normalized-Gram directions below
     1e-6 removes nothing, below 1e-4 removes four and gives 2.766: the value is not an artifact of near-dependent columns.
   - m <= 2 sub-block (52 columns): 3.4557, 4.2477, 5.4604: the S1M3 pure-spline value reproduces to the digits shown (padding 534 against 533).
   - single modes: m = 1 alone 50.3201, m = 2 alone 25.4729, m = 3 alone 12.1142.
   - the 60 columns sp7..sp26 (the pure columns in the theory author's high graph, V210), in the LOW norms of this computation: m <= 3: 2.8648, 3.4089,
     4.6170; m <= 2: 3.7223; m <= 1: 53.6343. These are not high-norm values.
   - weakest direction: the bulk splines sp21..sp27 (centres t = 3.9 to 6.9, r about 48 to 1000) with nearly proportional mode coefficients per
     spline (sp23: m = 1, 2, 3 coefficients -0.289, -0.298, -0.140; sp25: -0.292, -0.285, -0.130; sp24: -0.271, -0.280, -0.132): one angular
     profile times a broad radial profile, as in S1M3. Export: runs/S1M4P/vectors.json.
   - the pure-spline section value against the mode cutoff: 50.32 (m <= 1), 3.456 (m <= 2), 2.766 (m <= 3). The fall continues but slows (factor
     0.80 after 0.069). It is not converged in m; an m <= 4 run (about 3.5 h) does not fit in the window. In the deliverables the S1 core
     section is reported as "not bounded below by these runs; the floating values decrease with the angular cutoff".
   - producer diagnostics: axis residual max 1.2e-15, division residual max 9.9e-8 (the pinv quotient mismatch), trace-jet max 5e-14.
3. Input side (team message 47 item 5), work/gram_compare.py, logs/s1m4p_gram_compare.log, runs/S1M4P/gram_compare.json: the assembled 78 x 78 G_Z
   against the exact V202 Gram midpoints (640-bit balls, radii at most 1.3e-149 relative): largest entrywise relative discrepancy
   |G_ij - mid_ij| / sqrt(mid_ii mid_jj) = 7.41e-7 at the diagonal entry of (sp9, m = 3); median 0 (the exact zeros of the compact supports are
   exact zeros in the floating matrix too); congruent quadratic-form relative error 2.69e-6 (50-digit mpmath whitener of the exact midpoint
   Gram; whitener identity defect 4.9e-57; the same form as the verifier's check.py, which does it in Arb). Consistent with V187: the pinv
   input error is largest for m = 3. Floating comparison, input side only; nothing about B_Y follows.
4. Running since 15:43Z: (a) S1J1 (theory author message 32; junction test with the outer power columns attached at t_+ + 1 instead of t_+, BASIS_OUT_SHIFT=1,
   FSEC_DROP=+out, Mh 2, 4 workers, logs/s1j1_prod.log; about 1.2 h: expected about 17:05Z; its far-junction value is to be compared with 4.1552
   of S1); the shifted basis conformity is archived in logs/basis_shift_test.log (one-sided jets to order 3: max mismatch 5.1e-51; J conformity
   to order 6: 1.4e-46; ball radii of exact-zero differences). (b) OUTER_F8: finer outer cover of [t_+ + 1/2, t_+ + 8] (16 cells of widths
   1/8, 1/4, 1/2, 1; family (4, 0.3) tracked; all boxes refined to depth 6; logs/outer_f8.log; about 20 min), then outer_merge.py: the plane
   values inf m_a (now 2.9270, limited by the production cell [t_+ + 1, t_+ + 2] box 0) and inf m_fam(4, 0.3) (1.2501) may improve. Any
   improvement will be reported as certified by this team and marked "not independently verified" unless the verifier has time.
5. Plan for the rest of the run: deliverables (S2_BASIS_CERTIFICATION 7, S2_NUMERICAL_CERTIFICATES N3, NUMERICS_REPORT, S2_RESTART) by 16:40Z,
   artifacts refreshed (runs/S1M4P results and logs, gram_compare.py, the chain script) by 17:00Z, S1J1 assembled when it lands (before 17:15Z
   if it finishes by 17:05Z, else as a PARTIAL diagnostic at about 17:30Z for this team's files only).

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
## 2026-10-28 12:44Z (num, a session, team message 25: finer cover of the first outer sub-cell: inf m_a >= 2.9270, m_fam(4, 0.3) >= 1.2501; a refinement bug (no certified value affected); S1M4P running)

Theory author, verifier.
1. Finer radial cover of [t_+, t_+ + 1/2] (8 cells of width 1/16; margin.py MARGIN_OUTER_EXTRA; work/runs/OUTER_F403, OUTER_MA; outer_merge.py;
   logs/outer_merge_*.log). On that range the depth-6 refined bounds are m_a >= 3.0584 (old cell bound 2.8715) and m_fam(4, 0.3) >= 1.3277 (old
   1.1296). Combined with the production arrays elsewhere (which stand unchanged): inf_plane m_a >= 2.9270 (C4 improved from 2.8715), now
   attained at the production cell [t_+ + 1, t_+ + 2], theta box 0 (x-axis side), and inf_plane m_fam(4, 0.3) >= 1.2501 (same cell and box).
   So the first outer sub-cell WAS width-limited; the next limit is the next outer sub-cell, and a finer cover of [t_+ + 1/2, t_+ + 8] (about 40
   cells, 20 minutes) would move both bounds up toward the local values 3.06 / 1.33. Queued behind S1M4P (CPU). Values truncated.
2. Bug disclosure. In margin.py the refinement routine gained a family placeholder at 08:35Z (my team message 21 edit) whose non-finite default made the
   leaf-validity test fail in NON-family runs, so in such runs the adaptive refinement was silently skipped (the box bounds returned were the
   unrefined ones, still rigorous, just coarser). Affected: only work/runs/OUTER_MA of 12:36Z (its m_a bounds are the unrefined 2.871026 on the
   8 cells and are superseded by the refined OUTER_F403 bounds above, which come from the same leaves at depth 6). NOT affected: the certified
   production rounds of C4 (MARGIN, MARGIN_REF, MARGIN_REF2: 05:00Z-06:14Z, before the edit), the (Z) refinement, all family runs (family mode
   was never affected) and C5. Fixed 12:43Z (artifacts/code/margin.py).
3. Junction test code: the fixture test confirms the shifted outer columns live on the cells from t_+ + 1 on (exact conformity at the shifted
   junction; second-model referee junction_ref item 1 CORRECT). S1J1 itself runs after S1M4P.
4. S1M4P (pure splines, m = 1, 2, 3, 78 columns, complete modes; the smoke test on 6 cells gave axis residual 6e-16 and division residual 9e-8)
   started 12:42Z on 4 workers, about 2 h. Its m <= 2 sub-block must reproduce the 3.4557 of team message 24 item 3; the m <= 3 block answers whether
   the bulk value keeps falling.
## 2026-10-28 12:38Z (num, a session, team message 24: assembler repaired (team message 38); S1 re-assembled; S1M3 (m = 1, 2) results with flags; family (3.6, 0.3) final; next runs)

Theory author, verifier. team message 38 done, nothing deleted.
1. fsec_assemble.py v2 (old file kept as fsec_assemble_v1.py): blocks are the base_*.npz (merged earlier checkpoints, with done sets), the
   final part_<wid>.npz of the current launch (done sets stored from now on) and, only for a worker WITHOUT a final part, its latest
   checkpoint; the done sets must be pairwise disjoint with union = the run's cells, parts without done sets (runs before 12:40Z) are
   accepted only for never-resumed completed runs with sum(diag cells) = 1569. It then solves the generalized problem at 50 digits (as
   s1_robust.py). fsec.py resume now also excludes the cells of earlier bases and parts (item 4) and moves old parts aside as base blocks.
2. S1 re-assembled (logs/s1_assemble_v2.log; 4 parts, 1569 cells, no bases): 4.15523, 6.08407, 23.31349, 51.57616, 53.10667, ... = the
   s1_robust.py values. On c[h_0] = 0: 4.45631, 6.08437, 23.31351, 51.69929 (NUMERICAL, replacing the withdrawn 4.4438). Correction to my team message 22:
   the rounding model bounds the Rayleigh quotient of the FIXED computed direction (4.1552 lies in [4.137, 4.174] under the accumulation
   model), hence an upper bound of the section's smallest value; it does not bound the ordered smallest value from below (second-model referee
   junction_ref item 3; S2_BASIS_CERTIFICATION.md 7.4 corrected).
3. S1M3 (Mh = 3: the 84 remainder columns m = 1 and m = 2 of the 42 radial functions; complete 533-mode images; 8709 s on 4 workers; never
   resumed; logs/s1m3_assemble_v2.log, s1m3_robust.log, s1m3_bulk.log; work/runs/S1M3/fsec_result.json). 50-digit generalized singular values
   of the 84 x 84 pair: 2.3443, 2.9209, 3.5011, 3.8285, 3.9096, 4.6996, 5.6894, 6.3370, ...; largest 2389.5; on c[h_0] = 0: 2.3457, 2.9281, 3.5083.
   Flags (accumulation-rounding model on the computed directions): 2.3443, 2.9209, 3.8285, 3.9096, 4.6996 UNDETERMINED (near-null
   combinations of out5/out8/out9 with x^T G_Z x = 2.5e-8 .. 4.5e-10, image quotients below the rounding estimate); 3.5011 weakly resolved
   (quotient in [2.55, 4.25]), direction out9/out5 in both modes. Sub-blocks: m = 1 alone reproduces S1 exactly (4.1552, 6.0836, 23.314:
   same columns and nodes); m = 2 alone: 3.6676 (quotient in [3.655, 3.680], direction out9/out5/out8 at the far junction), 4.3411
   (undetermined), 12.44, 28.49; without the seven most dependent directions (normalized Gram eigenvalue < 1e-6): 3.024, 3.345, 4.048.
   THE NEW POINT (resolved, well conditioned): the 52 PURE SPLINE columns (sp4..sp29 in m = 1 and m = 2; no inner or outer power law;
   normalized Gram eigenvalue min 1.3e-4; rounding estimates 1e-9 relative) give smallest values 3.4557, 4.2477, 5.4604, 6.9419, while the
   m = 1 splines alone give 50.32 and the m = 2 splines alone 25.47. The weakest vector mixes the two modes with comparable weights:
   sp25 (m=1) -0.39, sp23 (m=1) -0.36, sp24 (m=1) -0.31, sp22 (m=1) -0.28, sp21 (m=1) -0.25, sp25 (m=2) -0.24, sp23 (m=2) -0.23, sp19 (m=1)
   -0.22 (coefficient vector; the coarse splines sp19..sp25 are centred at t = 2.9 .. 5.9, r = 18 .. 360). So the smallest value of S_1 on
   this subspace drops from 50 (angular mode m = 1 only) to 3.46 (m <= 2) through the coupling of the two angular modes in the bulk region
   r = 20..400, the region where the margins m_a and m_fam have their minima; the far-junction values (4.16 in m = 1, 3.67 in m = 2) are a
   separate, ill-conditioned matter. Whether the bulk value keeps falling with m = 3 is now the decisive question for Lemma INJ-S.
   All NUMERICAL; a section value is an upper bound of the infimum over its subspace.
4. Family (3.6, 0.3) final (774 refined cells, t_a >= 2.5; family_combine.py, truncated): inf over the plane >= 0.9596, attained INSIDE the
   refined range at t_a = 5.70 (r = 299), theta box 61 (85.8 to 87.2 deg); unrefined cells elsewhere >= 2.2822. Both pairs are now limited
   only by the box enclosures themselves: (4, 0.3) >= 1.1296 at the first outer sub-cell (radial width), (3.6, 0.3) >= 0.9596 at r = 299.
   A finer radial cover of the first outer sub-cell (8 cells of width 1/16) is running for m_a and for (4, 0.3) (10 minutes).
5. Next runs, in this order (your team message 32 asked for S1J1 next; given item 3 I put the m-trend first, please object if you disagree):
   (a) S1M4P: Mh = 4 on the pure spline columns only (26 radial x m = 1, 2, 3 = 78 columns; the in/out columns are dropped and their images
   skipped, so this costs about 2 h on 4 workers; its m <= 2 sub-block reproduces item 3); smoke test running now. (b) S1J1 (junction test,
   33 + 5 columns, outer power columns attached at t_+ + 1; about 1.2 h) after it, i.e. in the last shift with the resume logic if needed.
## 2026-10-28 10:16Z (num, a session, team message 23: near-axis refinement of the decoupled-family margin (directed), team message 28; Mh = 3 running; junction test planned)

Theory author (team message 28, team message 32). The near-axis refinement is done for the two pairs you asked for. Method: margin.py with MARGIN_FAMILY tracks the
ball m_fam = m_a + (a_ang - 17/4) tang_hi - Delta q_hi 1_{t>=0} on every box (tang_hi, q_hi the upper ends of the certified box enclosures of
tan(theta) V.grad(theta) and q = V.X/r^2; cells meeting both t < 0 and t >= 0 use max(q_hi, 0)) and refines the theta boxes 56-63 (84.4 to
90 deg) adaptively to depth 6 (up to 64 leaves per box) wherever m_fam < 1.5, with the lower end of every leaf ball as its bound; the
whole-plane minimum is then the minimum over all 1569 x 64 boxes of max(refined leaf bound, boxwise value from the certified MA_ref/TANG/Q data
of the production run), the latter in float arithmetic with a slack of 1e-12 (work/family_combine.py). Refined cells: all 469 cells with
t_a >= 4.5 (t_a in [4.5, 6] as you asked, plus t_a >= 6 including the outer sub-cells and the half-line, because the minimum moved there).
Results (lower bounds; artifacts/data/MARGIN/family_refined/family_4_03.json, family_36_03.json):
   a_ang = 4,   Delta = 0.3:  whole-plane minimum 0.7268 -> 1.1296 (values truncated, i.e. lower bounds), attained at the first outer sub-cell [t_+, t_+ + 1/2] (t_+ = 8.135,
       r = 3413), theta box 63 (88.6 to 90 deg); on the refined cells 1.1296 (near-axis boxes) and 1.3196 elsewhere (cell t_a = 4.50,
       theta 5.6 deg, from the Delta q term, which costs 0.3 q about 1.7 near the x-axis); no negative box.
   a_ang = 3.6, Delta = 0.3:  whole-plane minimum 0.2154 -> 0.7139, now attained at the first UNREFINED cell below the range (t_a = 4.4999,
       r = 90, theta box 60, 84.4 to 85.8 deg); on the refined cells (t_a >= 4.5) the near-axis minimum is 0.9596. The refinement of the
       cells 2.5 <= t_a < 4.5 for this pair is queued (two processes, paused by the CPU guard behind the Mh = 3 section; about 5 minutes of
       work once they resume); I will post the final whole-plane value then.
Remarks. (i) For (4, 0.3) the binding box is now the first outer sub-cell at the y-axis, where the radial width 1/2 of the enclosure limits
the bound, exactly as it limited m_a (2.8715 there); a radial split of that sub-cell would raise both. The far limit of the family margin,
b_0 - (5/8 + Delta) c_l = 1.42 for Delta = 0.3, is approached from below there. (ii) The 'FAMILY' summary line printed by margin.py for
these restricted runs is meaningless (the boxes outside 56-63 are coarse in those runs): only family_combine.py's output counts.
(iii) These are lower bounds for the boxwise minimum of the exact variation formula of your team message 27 applied to the certified box data; they
are not a new certificate of the weight family's mapping properties (your caveat in team message 28 stands).
Running: the S_1 core section with Mh = 3 (84 remainder columns, m = 1 and m = 2, complete modes; 4 workers since 10:05Z, done about
12:15-12:45Z; checkpoints). Planned after it (your team message 32): the junction test, the Mh = 2 section with the 33 spline columns and the five
outer power columns attached at t_+ + 1 instead of t_+ (zero on [t_+, t_+ + 1], zero 6-jet at t_+ + 1), about 1.2 h on 4 workers; code
(BASIS_OUT_SHIFT, FSEC_DROP) is being written now and will be smoke-tested on the fixture before the run.
## 2026-10-28 09:52Z (num, a session, team message 22: S_1 core section with the complete angular mode set, FLOATING result; family refinement running)

Theory author (team message 19 item 3, team message 29). The floating core section of S_1 = T_R + C_R on R = L^2(w_a) is done (work/runs/S1/fsec_result.json,
logs/s1_prod.log, logs/s1_assemble.log; 4817 s on 4 workers). NUMERICAL, not a certificate. Setup: Mh = 2 gives the remainder columns
x^2 y b_i(t)(cos 2 theta + 1) for the 42 radial functions b_i of the stride-60 S0 basis (4 splines extended inward by the inner power laws,
3 inner power columns in5-in7, 26 interior splines, 4 splines extended across t_+ by the outer power laws, 5 outer power columns out5-out9),
i.e. ONLY the first angular remainder mode m = 1 (Mh = 2 has no m = 2 column; the Mh = 3 run that adds m = 2 is next). Images with every
mode (531 sine modes), exact jet split (axis residual <= 1.2e-15 relative) and exact cos^4 quotient (division residual <= 9e-8 relative,
energy-weighted 2.5e-12 of the total 2130), the strain term with the exact cutoff chi_J, R norm on both sides, Gauss nodes 3/8/16 per cell
type, column pre-scaling by the weighted radial norm. The verifier's V111 caveat (non-contractive truncated angular map) does not apply
here because no mode is dropped; what remains floating is the quadrature and the double-precision accumulation.
Result (generalized singular values of the 42 x 42 pair (B_Y, G_Z), solved at 50 digits from the stored double matrices; the double
Cholesky whitening gave 4.136 for the first because cond G_Z = 1.5e13):
   4.1552, 6.0843, 23.314, 51.576, 53.109, 53.158, ...; largest 1038.2; on the subspace c[h_0] = 0: 4.44, 6.09, 23.3, 51.7, ...
Reliability. The columns are nearly dependent in the R norm: the normalized G_Z has eigenvalues 8.9e-13 (0.78 out9 - 0.59 out5 - 0.20 out8:
the outer power columns share the matching tail e^{alpha_1 tau}), 2.1e-11 (sp0+in against sp1+in), 4.4e-9, 1.3e-8, 2.6e-8, ... (seven below
1e-6). For each singular vector x (unit coefficient vector) I compared x^T G_Z x and x^T B_Y x with a worst-case rounding estimate
1.3e-12 (sum_i |x_i| sqrt(diag))^2 (eps times the number of accumulated node terms):
   sigma = 4.1552: x^T G_Z x = 8.8e-6 (estimate 1.5e-10), x^T B_Y x = 1.5e-4 (estimate 1.3e-6): resolved to about 1 percent;
     direction 0.75 out9 - 0.55 out5 - 0.23 sp32+out - 0.22 out8, i.e. a function concentrated just beyond t_+ = 8.135 (r about 3400)
     where the matching combinations cancel the common tail; m = 1.
   sigma = 6.08 and 23.3: x^T G_Z x = 2.1e-9 and 1.8e-10, x^T B_Y x = 7.7e-8 and 9.6e-8, both BELOW the estimate 7e-7: unresolved
     (these two directions are the near-null combinations of out5/out8/out9; the quotient could be anything up to about 50).
   Removing the seven near-dependent directions (normalized eigenvalue < 1e-6; 35 directions kept): 10.13, 13.63, 50.96, 52.33, ...;
   the 33 pure spline columns (no outer power law): 50.32, 51.58, 53.16, 55.82; keeping the two most dependent directions out changes nothing.
Reading: on this subspace (m = 1 only) S_1 has no singular value below 50 except in the far junction region t >= t_+, where the value 4.16
appears (comparable to m_a = 2.87 and to the far transport scale |c_l alpha_j - 1| about 20-40, so a cancellation between T_R and C_R there,
or an effect of the junction itself; the m = 2 run will tell whether it moves). A section bound is an upper bound of the infimum over its
subspace and proves nothing about injectivity; it is evidence for Lemma INJ-S only in the sense that no small value appears in the bulk.
Certification (your team message 19 condition "of order 1 -> certify") is NOT feasible in the remaining window with this machinery: the certified
version needs the R-norm Grams of 531-mode exponential-polynomial images integrated rigorously on 1569 cells; a Taylor-model quadrature
with the sub-interval splitting that the spline cells require (encl.py) costs about 6 times the floating run per Taylor order, i.e. of the
order of 18 h on our 4 cores for this 42-column basis. I record the method and the cost in S2_BASIS_CERTIFICATION.md section 7 instead.
Next from this team: (1) the near-axis family refinement of your team message 28 is running now (4 processes, theta boxes 56-63 refined to depth 6 on
the 195 cells with t_a in [4.5, 6], directed bounds; test on 2 cells: (4, 0.3) refined near-axis minimum >= 1.50 where 0.75 to 1.02 before,
the cell minimum then moves to the x-axis side, 1.396 at t_a = 5.26, from the Delta q term); results in about 20 minutes. (2) Then the
S_1 section with Mh = 3 (adds the m = 2 columns; about 2 h on 4 workers).
Environment note for the restart file: in this shift `python3` resolves to the system Python 3.9 (python-flint 0.6); every command must
use python3 (python-flint 0.9.0) explicitly, as the production commands in S2_RESTART.md now do.

## 2026-10-28 08:27Z (num, a session, team message 21: decoupled weight family, boxwise margin lower bounds (FLOATING), team message 26)

Theory author. From the certified per-box data of the refined production (work/runs/MARGIN_REF2: m_a lower bound MA_ref, tan(theta) V.grad(theta) upper
bound, q upper bound; cells meeting t >= 0 count as r >= 1; float arithmetic, the directed version is a one-line change), the lower bound
of m_a + (a_ang - 17/4) tan(theta) V.grad(theta) - Delta q 1_(r>=1):
     a_ang=4.0,Delta=0.2: min >= 1.3807 at t_a = 5.330 (r = 206), theta box 61 (85.8 deg), negative boxes 0
     a_ang=4.0,Delta=0.3: min >= 0.7269 at t_a = 5.330 (r = 206), theta box 61 (85.8 deg), negative boxes 0
     a_ang=4.0,Delta=0.4: min >= 0.0731 at t_a = 5.330 (r = 206), theta box 61 (85.8 deg), negative boxes 0
     a_ang=3.8,Delta=0.2: min >= 1.1289 at t_a = 5.330 (r = 206), theta box 61 (85.8 deg), negative boxes 0
     a_ang=3.8,Delta=0.3: min >= 0.4751 at t_a = 5.330 (r = 206), theta box 61 (85.8 deg), negative boxes 0
     a_ang=3.8,Delta=0.4: min >= -0.1788 at t_a = 5.314 (r = 203), theta box 61 (85.8 deg), negative boxes 126
     a_ang=3.6,Delta=0.2: min >= 0.8757 at t_a = 5.284 (r = 197), theta box 61 (85.8 deg), negative boxes 0
     a_ang=3.6,Delta=0.3: min >= 0.2155 at t_a = 5.222 (r = 185), theta box 61 (85.8 deg), negative boxes 0
     a_ang=3.6,Delta=0.4: min >= -0.4492 at t_a = 5.169 (r = 176), theta box 61 (85.8 deg), negative boxes 457
   (artifacts/data/MARGIN/margin_family.json). The minimum sits at r ~ 180-210 next to the y-axis (theta box 61 of 64, 85.8 deg), not at infinity:
   there the far limit b_0 - (5/8 + Delta) c_l (1.98, 1.42, 0.86 for Delta = 0.2, 0.3, 0.4) is still approached from below by the box bounds, and
   the tan(theta) V.grad(theta) upper bound of those near-axis boxes is the unrefined production bound (the refinement rounds refined m and m_a
   only), so the true minima are probably higher; angular refinement of the tang bound near the y-axis would sharpen them if you want to adopt
   one of these weights. Negative boxes appear only for Delta = 0.4 with a_ang <= 3.8.

## 2026-10-28 08:25Z (num, a session, team message 20: eta withdrawn from this team; S_1 core section runs with the complete angular mode set)

Theory author, verifier. Read team message 25 and V111-V114. Agreed on both points: (i) my eta runs (raw-sine truncation at N = 40 plus least-squares
division) are not a controlled approximation of the Y norm and are withdrawn (stopped at 08:25Z, no output used); the reference values are
your all-mode point densities (||F||_Y about 7.24e3, axis part 123, 70% of the energy from log r in [8.135, 12]) and the proved lower bound
||F||_Y > 933.47 (V110). (ii) The same caveat applies to the floating sections at finite angular truncation, so the core section of
S_1 = T_R + C_R on L^2(w_a) now runs with the COMPLETE mode set of every image (535 sine modes, exact jet split and exact cos^4 quotient:
residual fractions 1e-32 and 1e-15 in the 5-cell test) on the smaller basis Mh = 2 (42 remainder columns x^2 y b_i(t)(cos 2 theta + 1),
coarse stride 60), 4 workers, about 4.5 h (done ~13:00Z, i.e. reported by the next shift). The L_red jet-realization section is not run
(cross-check only). All code is in work/ and artifacts/code (fsec.py, fsec_ang.py, fsec_assemble.py; eta.py/eta2.py kept only as a record
of the withdrawn attempt).

## 2026-10-28 08:20Z (num, a session, team message 19: floating sections need the complete angular mode set; S_1 core section started; eta at 09:00Z)

Theory author, verifier.
1. Truncation study for the floating sections in the jet realization (logs/dbg_div.log, complete 522-mode images of compensated columns versus
   truncations at a node): at t = 1.95 the weighted remainder density is within 0.5% at N = 80 (N = 19: -35%/+15% depending on the column);
   at t = 6.05 N = 19 gives 5% of the full value, N = 40 70%, N = 80 92%. The quotient (B - gamma)/cos^2 (equivalently the cos^4 division of
   the sine modes) in a truncated basis is ill-conditioned by ~N^3 (the division recurrence has the fourfold root -1), and the far weight
   e^{6.75 t} multiplies the truncation error by up to e^{88}. With the complete set the jet split and the division are exact: in the
   5-cell test of the S_1 section the axis-residual and division-residual energy fractions are 5e-32 and 4e-15 (they were 1e-10 before).
   The far region genuinely dominates the Y norm of a column image in this normalization (density 1e11 at t = 6 for a mid spline, m = 1).
2. S_1 = T_R + C_R on L^2(w_a) (team message 19 item 3): the floating section (126 remainder columns x^2 y b_i(t)(cos 2m theta - (-1)^m), m = 1..3,
   coarse stride 60; chi_0 = the exact J cutoff; R norm on both sides; images with angular truncation N = 100 as the cost compromise, 35 s per
   cell) is running in production (work/runs/S1, checkpoints every 10 min, 1 worker until eta finishes, then 4; ~4 h). Result: smallest
   generalized singular values and vectors, FLOATING, in NUMERICS_REPORT and a note when done (next shift).
3. eta (exact residual modes, N <= 40): finishes about 09:00Z; its truncation caveat is the same as above (N = 40 underestimates the far
   remainder part by up to ~30%); I will report it with that caveat and compare with your directed point densities.
4. The L_red jet-realization section (with the KP column, 260 velocity modes) costs ~1 min per cell with the complete mode set; it is a
   cross-check only (your team message 19) and is not started.

## 2026-10-28 07:16Z (num, a session, team message 18: eta status (the pointwise/FFT route is withdrawn), floating sections, fixes)

Verifier, theory author.
1. eta. I agree with your 07:03Z audit: eta2.py (pointwise residual on an angular grid, FFT modes, least-squares division by cos^4) is noise-
   dominated and withdrawn; its 680 on the inner half-line is the float noise of the O(1) cancellation amplified by the division and by e^{-t/2}.
   The run now in progress uses the exact residual modes (Operator.residual_modes in ball arithmetic, no cancellation noise) truncated at
   N <= 40, the same jet split and exact cos^4 quotient (equivalent to your proof 98 integrand), Gauss nodes per cell and the e^{8t + mu_a} / G
   weights; 3 workers, ~14 s per cell, finished around 09:10Z (work/runs/ETA/eta.json: eta_Y, axis and remainder parts, regions r < 1,
   1..100, > 100, and the L^2(e^{mu~}) value). I will compare its node integrands with your directed point values (t = 0: 1.06e-15 / 1.44e-8;
   t = 4: 1.04e-4 / 1.71e5; t = 10: 8.13 / 1.18e7; t = 30: 3.4e-3 / 527) before reporting; your values already show that the far strong-target
   energy of the residual is large (the remainder density 1.2e7 at t = 10), so eta in this normalization will be of order 1e3 or more; the
   directed enclosure should then use your angular module (proof 98) on the ball cosine coefficients; I will do that if time allows.
2. Floating sections. The scaling blow-up of the jet-realization Gram was traced (logs/dbg_far.log) to the '+out' columns (coarse splines
   extended across t_+ by alpha_2..alpha_5; the tail alpha_1 = k - 3 is excluded, basis.py line 114): their Vandermonde coefficients are 1e4..1e8
   (strain c ~ 3e8) and they are still 2e-4 at t = 12.6 where the weight is e^{88}; the images are ~ T u and the KP compensation cancels the
   strain tail to 1e-2 relative at those nodes. Fix: every column is divided by its weighted radial norm (pre-pass); the generalized singular
   values are invariant. Your DK remark is fixed: the compensation coefficients are now the exact Arb quotients -(c_j k)/(3 c_l + k c_KP)
   throughout. Agreed that the jet B-norm in the floating domain Gram is only the ||z'||_omega part (the Hardy/J terms are omitted); it is a
   floating estimate, not a bound in Z. The 5-cell diagnostic is rerunning; production (L_red jet realization, then S_1 = T_R + C_R on
   L^2(w_a) with chi_0 = the exact J cutoff, both Mh 4 / stride 60 / N <= 19 / 2 workers) follows, into the next shift.

## 2026-10-28 06:16Z (num, a session, team message 17: second refinement round: m >= 2.482724, m_a >= 2.871539)

Theory author, verifier. Round 2 (targets m >= 2.55, m_a >= 3.0, angular bisection to depth 6 on the 1027 cells still below those targets; merged into
work/runs/MARGIN_REF2/margin.json, copy artifacts/data/MARGIN/margin_refined2.json):
  inf m   >= 2.482724  at cell 525 (t = 1.4962, r = 4.46, theta ~ 51 deg; depth 6 reached, so a box-width floor in the source region);
  inf m_a >= 2.871539  at cell 1563, theta box 0: the first outer sub-cell [t_+, t_+ + 1/2] next to the x-axis, where the
            radial width (h = 1/2 in t) is the limiting factor; angular bisection cannot help there. A radial subdivision of the outer sub-cells
            would bring m_a to the far limit 3.0908 (your grid value); I can add it if you want the last 0.2.
  31127 boxes refined, 263417 leaves, 0 negative, all finite, full coverage (1569 cells, 100416 boxes). These replace the production values
  as the certified margins (same inputs; refinement only subdivides boxes); C4 records both rounds.
Floating jet-realization section (fsec): the 24-cell test ran (36 s per cell) but its Gram was indefinite because the KP compensation was
combined in floating point at the far nodes, where the cancelling e^{(k-3)t} tails exceed the remainder by 1e4; now the images are combined in
ball arithmetic per node before conversion. Retesting; production afterwards (~1.5-3 h on 4 cores, so it will run into the next shift).

## 2026-10-28 05:58Z (num, a session, team message 16: margins improved to m >= 2.471224 and m_a >= 2.500023; (Zb) leaf counts corrected)

Theory author, verifier.
1. Margin improvement (team message 16 item 3): the 855 cells whose minimum of m or m_a was below 2.5 were recomputed with adaptive angular bisection
   (depth 5, target 2.5) and a sharper tail bound in the anisotropic term, |sin(2n theta)/cos theta| <= min(2n, 1/min cos theta) for n > 8
   (the old factor 2n was the whole 0.97-versus-3.09 gap at r ~ 52 near the x-axis: there the tail sum of |Qe_n| 2n with slowly decaying far
   modes cost about 2 in a tan(theta) V.grad(theta)). Merged into the production arrays (work/runs/MARGIN_REF/margin.json; merge_override.py):
     inf m   >= 2.471224  (was 1.029821; argmin cell 525, t = 1.4962, theta box 36 of 64, i.e. r = 4.46, theta ~ 51 deg, in the source region;
                            the bisection reached depth 5 there, so this is a box-width floor, not necessarily the true minimum),
     inf m_a >= 2.500023  (was 0.965918; every refined box reached the target 2.5, so the true infimum is larger).
   17242 boxes refined into 133255 leaves, 0 negative, all finite, coverage 1569 cells / 100416 boxes. A second round with targets
   m >= 2.55 and m_a >= 3.0 (depth 6) on the 1027 cells still below those targets is running (~30 min); I will report the new minima and
   their locations. Radial bisection is not implemented in margin.py yet; if the source-region boxes stall I will add it.
2. (Zb) bookkeeping corrected (verifier 05:34Z): rectangle Q: 463 nodes, 359 terminal leaves = 34 inside Q + 325 positive +
   0 unresolved, smallest positive |V|/r >= 2.8297e-04; disc B_99/2000(P): 595 nodes, 425 terminal leaves = 3 inside + 422 positive +
   0 unresolved, smallest positive 8.4400e-06. Every positive leaf is exported with exact rational t endpoints, theta/pi as exact
   rationals and directed q, u bounds (work/runs/ZREF2/zrefine.json, ZREFD2/zrefine.json; copies in artifacts/data/ZREF/). Containment uses
   the V071 corner tests with an absolute margin 1e-3 in x and y for the center uncertainty of P.
3. Note headers now carry the real date -u time (team message 13-15 corrected to 05:28Z, 05:32Z, 05:42Z).

## 2026-10-28 05:42Z (num, a session, team message 15: L_fix section in L^2(e^{mu~}) certified: sigma_min >= 0.510914 (finite statement))

Theory author, verifier. The L_fix section in your Theorem R realization (169 conforming columns, modes m = 0..3, stride 60; 69 active test splines x 12
output modes; weight e^{mu~} of team message 5; exact integration at 256 bits) is certified: sigma_min(Q_M L_fix P_N) >= 0.510914 (float 0.52134, 0.52147,
0.52163, 0.52178, 1.0105, ..., 146.22). The raw Grams span 68 orders of magnitude (inner power columns ~1e-23, far ~1e28; test splines up to
1e48), so certify_l2.py now whitens both sides exactly (mpmath 140 digits from exact midpoints, applied in ball arithmetic); whitened Grams PD with
||E|| = 1e-38 and 9e-45; PSD check of K - s^2 G with ||E|| = 4.4e-12. The weakest direction is the inner power columns in5/in6/in7 (m = 0, 1):
functions living at r < 0.0077 where the weight is tiny. Record: C6 in my certificates file; matrices_dyadic.json.gz in work/runs/L2fix_M4_s60_o12/
for an independent check (same format as S0). This is a finite statement; the continuum complement still needs the split (S) of Lemma IV.1.
Decision: I dropped S0's Phase 2 (run_norms/run_tailbound2/offbasis, a pipeline test for a realization that cannot carry an inverse, Prop IV.O)
and the identity rerun from the chain to free the cores for the floating jet-realization section (team message 14 item 3), whose test is running.

## 2026-10-28 05:32Z (num, a session, team message 14: (Zb) done against the verifier's Q; re-merge confirms full coverage)

Theory author, verifier. zrefine.py (mode rect, Q = [p - 1/2, p + 1/2] x [-1/2, 1/2], p = 8.600064): the 255 production boxes with |V|/r lower bound
below 0.1 were bisected (theta or t, depth <= 9) into 463 leaves: 34 leaves inside Q, all 429 others with a positive certified bound, the
smallest |V|/r >= 2.8297e-04 at cell 670 (t in [2.14874, 2.15065]), theta in [0.14726, 0.17181] rad; unresolved leaves: 0 (149 s). With
|V|/r >= 0.100068 on all other boxes, (Zb) holds with Q as the excluded set (V070 supplies uniqueness in Q). Record: C4 of my certificates
file; work/runs/ZREF/zrefine.json lists every leaf inside Q. Disc version (Lemma Z, B_99/2000(P)): 595 leaves, 3 inside B_P, all others positive (min |V|/r >= 8.4400e-06 at cell 672, theta in [0.02148, 0.02454]), unresolved 0: (Zb) holds with B_P too (work/runs/ZREFD/zrefine.json).
Re-merge of the margin production (V066/V068 guards): cells 1569/1569, boxes 100416/100416, refined leaves all finite, 0 negative boxes;
numbers unchanged (inf m >= 1.029821, inf m_a >= 0.965918).

## 2026-10-28 05:28Z (num, a session, team message 13: outward-rounded decimals (V070), (Z) refinement against the verifier's Q, status)

Verifier: thank you for V070. Corrections to the short decimals of team message 12 (all now outward in C4, C5, NUMERICS_REPORT, S2_BASIS_CERTIFICATION 6.5;
the JSON files hold the stored endpoints): kappa_* >= 3.037693 (not 3.0377); sup kappa_w <= 125.4206; d in [5.575203, 21.301451];
sup |d'| <= 5.6012; sup_{t>=0} |d - c_l| e^{(1-k)t} <= 89.3342 and sup |d'| e^{(1-k)t} <= 73.3113; M_Q <= 337.6560; M_P <= 1075.5156;
sup b_+ <= 11.2281; sup du <= 125.7436 (du is the component-sum bound |psi_rr| + 2|psi_rth|/r + |psi_thth|/r^2 + |psi_r|/r + |psi_th|/r^2 >=
the operator norm of DU; its origin limit is 2c for this bound while the operator norm of DU(0) is c; c_l + sup du is a global Lipschitz
constant of V); q in [-10.150726, 21.301451]; |V|/r >= 0.100068 outside the 255 small boxes; DV on the P box xx [9.9588, 10.3327],
xy [-1.7668, 1.8053], yx [-0.5901, 0.5699], yy [0.8180, 1.1919]; inf m >= 1.029821 and inf m_a >= 0.965918 were already floors.
(Z): zrefine.py now classifies the zero-VLO boxes against your Q = [p - 1/2, p + 1/2] x [-1/2, 1/2] (p = 8.600064; mode 'rect', the default)
and bisects (theta or t, whichever is longer in arc length, depth <= 9) every box not inside Q until its |V|/r lower bound is positive;
output: the minimum positive bound outside Q with its location, the leaves inside Q, and any unresolved leaf (which would break (Zb)). It is
queued behind the re-merge (logs/zrefine.log -> work/runs/ZREF/zrefine.json); the theory author's disc B_{99/2000}(P) is available as mode 'disc'.
(Z0) table (work/runs/MARGIN/Z0.json): sup over boxes with r <= r_0 of the Frobenius deviation of DV from diag(-A, D): 4.5895 (r_0 = 0.05),
4.5965 (0.1), 4.6248 (0.2), 4.6708 (0.3), 4.8167 (0.5); below A = 10.1507 up to r_0 = 2.5116 (10.1314). The 4.59 near 0 is the angular box
width acting on the O(c) mode sums; |V|/r >= 10.0988 on the inner half-line boxes.
Guards added (V068): non-finite refined leaves propagate -inf; coverage counts every angular entry; the re-merge reports both.
Status: L_fix section assembling (4 workers; 3 of 4 near completion, one delayed by the CPU guard); fsec test (floating jet-realization
section) queued; zrefine queued.

## 2026-10-28 05:15Z (num, a session, team message 12: CERTIFIED: m >= 1.0298 (Theorem R, mu~), m_a >= 0.9659 (H_m'), d in [5.5752, 21.3015] (A), kappa_* >= 3.0377, (CB) constants)

Theory author, verifier. The production runs finished (all 1569 radial cells x 64 angular boxes, every cell computed, no refinement needed, zero
negative boxes). Full records with inputs, methods and files: my S2_NUMERICAL_CERTIFICATES.md C4 and C5; JSON summaries in
work/runs/MARGIN/margin.json and work/runs/HYPA/hypA.json (per-box arrays in the npz files next to them).
- Theorem R margin (weight e^{mu~}, team message 5): inf m >= 1.029821 (argmin t = 2.145, theta ~ 45.7 deg, cell 668 box 32); inner half-line
  m >= 5.3065, outer half-line m >= 3.0889. So (H_m) holds with m_* >= 1.0298 and Theorem R is unconditional for L_fix on L^2(e^{mu~}).
- Anisotropic margin (w_a, a = 17/4, team message 7): inf m_a >= 0.965918 (argmin cell 1022, t = 3.95, theta box 5, i.e. r ~ 52 near the x-axis);
  aniso NaN boxes 0. So (H_m') holds with m_a >= 0.9659.
- kappa_* = ess inf kappa_{w_a} >= 3.037693 (cell 1135, box 4; far limit 3.0908), sup kappa_w <= 125.42.
- (A): d in [5.575203, 21.301451] on the whole y-axis (d > 0); sup |d'| <= 5.6011; sup_{t<=0} |d - D| e^{-2t} <= 0.100883 and
  sup_{t<=0} |d'| e^{-2t} <= 0.202073 (both attained on the inner half-line); sup_{t>=0} |d - c_l| e^{(1-k)t} <= 89.334 and
  sup_{t>=0} |d'| e^{(1-k)t} <= 73.311 (both on the outer half-line). Conditional on the exact normalization (V005) for the dropped
  constant of d - D at the origin (ball -4.3e-37 +/- 2.0e-35).
- (CB): M_Q = sup |q - d|/cos^2 <= 337.66 (cell 1091, box 49), M_P = sup max(e^{-2t},1) |p - p_axis|/cos^2 <= 1075.5 (the t <= 0 weighted part is
  1.09). The sizes come from the slow n-decay of the far angular modes (a_1 near the axis is 2 sum (-1)^n n^2 Pe_n); they are what they are.
- (Z) data: per-box lower bounds of |V|/r and enclosures of the four DV entries. On the P box (cell 671, t_a = 2.1507, theta box 0):
  DV_xx in [9.959, 10.333], DV_xy in [-1.767, 1.805], DV_yx in [-0.590, 0.570], DV_yy in [0.818, 1.192]. The boxes where the |V|/r lower bound is
  below 0.1 form a neighbourhood of P only (see C4 for its t- and theta-extent); outside them |V|/r >= 0.10007. Finer boxes around P can be
  produced on request (margin.py takes a cell list; the P region is cells 660-680).
- Other certified numbers: sup b_+ <= 11.228, sup |grad rho~| <= 30.42 (finite cells), sup |DU| <= 125.74 (global Lipschitz constant of V on the
  quadrant minus the two half-lines' interiors, where |DU| -> 2c at 0 and -> 0 at infinity), q in [-10.1507, 21.3015].
- Checks: the Green-data identity n Qe_n = Pe_n + Pe_n'/2 holds to 4.1e-35 on every cell; the enclosure method was validated by containment
  tests (S2_BASIS_CERTIFICATION.md 6.2); verifier audits V054, V058, V061, V066 are incorporated (merge repair done before the production merge).
Verifier: the merged runs are ready for your audit (the parts' logs list every cell). I rounded the S0 bound down to 4.3337e-07 as you asked (V066).
Next in my team: the L_fix section in L^2(e^{mu~}) is assembling (4 workers, ~1 h), then certify_l2; a floating-point section of L_red in the
w_a jet realization (team message 12 item 4) is coded (work/fsec.py) and in test.

## 2026-10-28 04:55Z (num, a session, team message 11: S0 certified (finite statement), enclosures validated, margin/hypA production running, (Z) added)

Theory author, verifier.
1. S0 certificate (C3, C3b in my S2_NUMERICAL_CERTIFICATES.md): whitened Gram PD with ||E|| = 1.753e-27 (V056's value). With the TAU
   column sigma_min >= 4.3337e-07 (float 4.42e-07; weakest direction 0.9964 TAU): the compensated TAU + dk KP image is almost invisible
   to test splines ending at t = 16.1. Without TAU: sigma_min >= 2.0685e-02 (float 0.02111; weakest: out5/out8/out9, m = 1, 0). Finite
   statements only (Prop IV.O).
2. Enclosures: encl.py (V058 repaired, V061 accepted) now also merges near-resonant clusters with |e - e_0| h <= 1 (J = 20; the outer
   cells have cancelling pairs with gaps 0.1..1) and prunes negligible modes. Containment tests at 512 bits, 0 violations: cell 4 (inner,
   h = 1/2) sum of mode radii 4.3e-6 (old 3.4e78), cell 1 (h = 2) 1.2e-7 (9.2e33), cell 1563 (outer, h = 1/2) 1.9e-2 (1.3e5), cell 1566
   (h = 2) 8.8e-3, cell 800 (t = 2.52) 1.8e-2 (1.9e3). Non-mid cells run at 512 bits (V054).
3. Test results (ntheta 16, selected cells; logs/hypA_test5.log, margin_test.log, margin_test2.log):
   - d: 21.30145 on the inner side, [14.83, 14.85] at t = 2.52, [6.193, 6.197] at t = 6.04, [5.5752, 5.5755] on the outer half-line;
     inner half-line sup |d - D| e^{-2t} = 0.1009, sup |d'| e^{-2t} = 0.2018; outer half-line sup |d - c_l| e^{(1-k)t} = 89.3,
     sup |d'| e^{(1-k)t} = 73.3 (the far constants are large because the far modes decay slowly in n; d itself is fine).
   - kappa_w (w_a): >= 36.3 inner, 3.23 at t = 2.52, 2.908 at t = 6.04, 3.0039 at t = 8.14, 3.0899 on the outer half-line (your far limit
     1 + 3 ell/8 = 3.0908). The ess inf over all boxes comes from the production run.
   - M_Q, M_P (CB): on the test cells sup |a_1| <= 598, sup max(e^{-2t}, 1)|a_0| <= 1888 (both at t = 8.14, box near the y-axis); a_1 near
     the y-axis is genuinely 2 sum (-1)^n n^2 Pe_n in size, so these constants reflect the slow angular decay of the far modes, not
     looseness; on the outer half-line a_1 <= 0.87, a_0 <= 2.73; at r <= 1 a_1 = 31.45 = 2c (the origin value -(A + D)).
   - Theorem R margin m (mu~ of team message 5): the standard boxes near the source region give NEGATIVE lower bounds (-1.24 at t = 2.52, -3.65 on
     the P cell t = 2.15 with ntheta 16); with adaptive angular refinement (boxes with lower bound < 0.5 split recursively, depth <= 4)
     the same cells give m >= 1.13, 0.79, 0.76, and m_a >= 0.52 (cell t = 2.78). So the negatives were box looseness of b_+ where
     |grad rho~| varies fast. Production uses ntheta 64 plus refinement; the certified value is the min over the refined leaves.
   - (Z) (team message 12): |V|/r lower bounds per box (test cells away from P: >= 0.826 at t = 2.52), and the four entries of DV per box
     (DV = c_l I + DU from the exact polar second derivatives of psi); the P cell (t_a = 2.1507, theta box 0) is reported separately.
     Also sup |DU| per box (global Lipschitz bound of V) as before.
4. Production (04:50Z, chain logs/run_phase2e.sh): margin.py and hypA.py in two cell-range parts each on the 4 cores (~1 h), merged
   into work/runs/MARGIN/margin.json and work/runs/HYPA/hypA.json; then the L_fix section (4 workers), certify_l2, S0 Phase 2, identity.
   The JSON summaries will carry failure counts (negative_boxes_refined, aniso_negative_boxes_refined, aniso_nan_boxes_computed_cells,
   dropped constants with radii, identity_check_max, cells_computed).
5. Conventions to keep in mind when you read the numbers: d(t) = c_l - sum (-1)^n Pe_n (V_2(0, e^t)/e^t); p_axis = D - d - 2d' (cross-checked
   by n Qe_n = Pe_n + Pe_n'/2 on every cell: identity_check_max 4e-46); the exponent-0 constant of d - D on the inner half-line is dropped
   as the exact normalization zero (V005), its ball is reported; kappa_w is an a.e. identity (knot t = 0, axes); M_P uses max(e^{-2t}, 1)
   on both sides of every cell crossing t = 0.

## 2026-10-28 04:15Z (num, a session, team message 10: S0 assembled; certificate blocked by Gram conditioning; enclosure method replaced; hypA.py for (A), (CB), kappa_*)

Theory author, verifier. Status and two findings that affect the certificates.
1. S0 assembled (02:06Z to 03:58Z, 2 workers, 256 bits; work/runs/S0_M4_s60_o12/matrices.npz, max entry radius 1.2e-62 (Gram), 6e-28 (rows)).
   certify.py failed: the raw domain Gram has condition number 2.3e24 (the two '+in' spline columns next to t_- are parallel to
   1 - 1.3e-10 because their common inner continuation dominates the norm (diagonal 8e10); the m = 1 'out5..out9' far columns are
   nearly dependent too), so the float Cholesky fails. Fix (certify.py, 04:10Z): a whitening change of basis T = L^{-T} from an
   80-digit mpmath Cholesky of the exact midpoint Gram; G -> T^T G T and K -> T^T K T in ball arithmetic. The generalized
   singular values of (B, G) are invariant under any invertible real T, so the certificate is unchanged in meaning. Rerun queued.
   By Prop IV.O (V039) the S0 number is a finite statement only; I keep it as a pipeline test, as you asked.
2. The box enclosures of margin.py (and my new hypA.py) used f(h/2) +/- sup|f'| h/2 with sup|f'| from coefficient sums. On the
   spline cells the Green data are exponential polynomials with large cancelling coefficients (e.g. Pe_3 on the cell at t = 6.04
   has coefficients of size 4 to 9 for a function of size 0.07), so the radii were 100 to 1e5 times too large near the source
   radius and on the inner sub-cells (d(t) enclosed in [-1879, 1909] at r = 12; +/- 3e78 on the inner sub-cell next to t_-).
   Replaced (work/encl.py, 04:20Z) by a Taylor enclosure of order 8 about the cell midpoint with the rigorous remainder
   sup|f^(9)| (h/2)^9/9! (coefficient-sum bound of the 9th derivative), on sub-intervals of width <= 6/|e|_max for the
   half-line-like sub-cells. Containment test against sampled values running (logs/dbg_encl.log). margin.py was stopped at
   04:03Z before producing a certificate and is relaunched with the new enclosure together with hypA.py (chain logs/phase2c.log).
3. hypA.py (theory author team message 10, 11), definitions used (second-model referee round second-model referee/hypA_ids/answer.md: all identities CORRECT; its code
   findings fixed at 04:20Z: arb tail coefficients, cells crossing t = 0 counted on both sides for M_P, geometric cell selection
   with +inf propagation, directed sums):
   - d(t) = V_2(0, e^t)/e^t = c_l - sum_n (-1)^n Pe_n(t), with U_r/r = -sum Pe_n cos 2n theta, U_theta/r = sum Qe_n sin 2n theta;
     d'(t) exact derivative. Per cell: enclosures of d, d'; sup |d - D| e^{-2t}, |d'| e^{-2t} on cells meeting t <= 0 (inner
     half-line included); sup |d - c_l| e^{(1-k)t}, |d'| e^{(1-k)t} on cells meeting t >= 0 (outer half-line included).
   - a_1 = (q - d)/cos^2 theta = 2 sum (-1)^n Pe_n U_{n-1}(sin theta)^2 (Chebyshev U), M_Q = sup |a_1| (direct, sharper than the
     (pi^2/8) sup |d_theta^2 q| route by the factor pi^2/4; the second-derivative route gives the same with 4 sum n^2 |Pe_n|).
   - a_0 = (p - p_axis)/cos^2 theta = 6 sum (-1)^n Pe_n U_{n-1}(s)^2 - 2 sum Qe_n g_n + 2 sum Qe_n U_{n-1}(cos 2 theta), with
     g_n = 2 (-1)^n sum_{k<=n} [U_{k-2}(s)^2 + U_{k-1}(s)^2] (exact trigonometric identities, see the hypA.py docstring);
     the n = 1 part is exactly 6 (Qe_1 - Pe_1) = -6 e^{-2t} A_1 (no constant term). M_P = sup max(e^{-2t}, 1) |a_0|.
   - kappa_w = b_0 + (mu_a'/2) q + a tan(theta) V_theta/r, a = 17/4, mu_a' = -17/2 (t < 0), -5/4 (t > 0), both values on cells
     touching t = 0; an a.e. identity (knot, axes). kappa_* = inf of the lower bounds, sup kappa_w also reported.
   - Exact modes n <= 12 per theta box, tails n > 12 by |U_{n-1}| <= min(n, 1/min cos theta), |g_n| <= (4n^3 + 2n)/3, etc.
   - Conditional step: on the inner half-line the exponent-0 constant of d - D is dropped; it equals c[rho~] - (3 c_l - 1), which is
     exactly zero for the repaired trial by the definition of z (V005). The ball of that constant is checked to contain 0 with
     radius < 1e-30 before dropping. All other dropped constants are structural (no e^{0 t} term exists), as second-model referee confirmed.
   - Consistency check per cell: n Qe_n = Pe_n + Pe_n'/2 (Green data), reported as identity_check_max.
   The 10-cell test with the old enclosure gave on the sane cells: d in [21.3014, 21.3015] at t = -4.87, [21.229, 21.230] at
   t = -0.17, [6.06, 6.33] at t = 6.04 (grid said 5.58 <= d <= 21.31); kappa_w >= 36.3, 35.6, 1.20 there; inner half-line
   sup |d - D| e^{-2t} = 0.1009, sup |d'| e^{-2t} = 0.2021; outer half-line sup |d - c_l| e^{(1-k)t} = 89.3, |d'| e^{(1-k)t} = 73.3.
   Final numbers after the full 1569 x 64 run go to S2_NUMERICAL_CERTIFICATES.md C5.
4. Guard test (test_minf.py) on the fixture reports a non-decaying (exponent 0) term in the J column image: for the fixture trial
   the normalization 3 c_l - c[rho] = 1 does not hold exactly, so L(J) has a genuine constant (3 c_l - 1 - c[rho]) times x^2 y near
   0; for the exact trial that constant is a ball around 0. The guard test needs the exact trial (or that term excluded) to be
   meaningful; I will adapt it. Not a pipeline defect.
5. run_tailbound2 part (b): umul(umul(apj, 0.5), ...) applied (verifier 03:13Z).
6. Queue (chain logs/phase2c.log): margin || hypA -> L_fix section (2 workers) -> certify_l2 -> run_norms -> run_tailbound2 ->
   offbasis -> identity rerun. certify (whitened) for S0 runs as soon as a slot is free.

## 2026-10-28 03:00Z (num, a session, team message 9: V037 points fixed)

- offbasis.t_of: the positivity test is now the exact sign of the dyadic upper end (arb comparison), so a positive subnormal is never replaced by 0.
- run_tailbound2.py float bookkeeping is now directed throughout: every scalar product/sum of nonnegative upper bounds is followed by an upward
  nextafter (uadd, umul); the vectorized terms use np.nextafter after each elementwise operation; after each scatter-add two upward steps
  (your collision count of at most two additions per target); the final energy sum uses correctly rounded math.fsum stepped upward, squares
  stepped upward, in both the per-row sums and the sum over modes. Table entries are fup() conversions (a 1e-5000 ball becomes the smallest
  positive subnormal, never 0). No multiplicative fudge factor remains.
- Anisotropic margin: reported with aniso_nan_boxes; it will be called global only if that count is 0.

## 2026-10-28 02:51Z (num, a session, team message 8: theory author team message 7 and 8 answered)

- team message 8 items 1 to 3: done at 02:44Z (notes team message 7). Item 4 noted: the mu~ margin certifies Theorem R for the piecewise weight directly (V031).
- team message 7 (anisotropic weight, a = 17/4, mu_a' = -17/2 for t < 0 and -5/4 for t >= 0): added to margin.py in the same box loop, isolated from the
  main certificate. T_ang = tan(theta) U_theta/r = tan(theta) sum_n Qe_n sin 2n theta is enclosed with sin(2n theta)/cos theta =
  2 sum_{k=1}^{n} (-1)^{n-k} sin((2k-1) theta) for n <= 8 (exact identity, checked) and |sin(2n theta)/cos theta| <= 2n beyond; boxes touching
  t = 0 carry both mu_a' values. Output fields aniso_inf_ma_lower_bound, aniso_argmin, tang_range in work/runs/MARGIN/margin.json and the per-box
  array MA_lo in margin.npz. (My T_ang agrees with your sin V_2/r - sin^2 V_1/(r cos) after inserting V = c_l X + U: the c_l parts cancel.)

## 2026-10-28 02:45Z (num, a session, team message 7: V033 defects fixed before the queued run)

- margin.py: |grad rho~| is bounded above by sqrt(R^2 + T^2) with R, T the exact upper ends of |rho_r|, |rho_theta/r| (no correlated interval
  square; your NaN example reproduces with the old formula and the new one returns [1.4142 +/- 1e-5]); b_+ <= (gr_up - dy_lo)/2 and m_lo
  from the lower end of the ball; every float written is a directed conversion (work/outward.py: fup/flo move to the next float until the
  float encloses the exact dyadic end); non-finite values abort.
- run_tailbound2.py part (c) now uses the PLAIN Green data B_1 (the ColumnFix method bound to the same column data), so part (d) with
  (C/3) dR_N^rem is the complete strain term and no (-x, y)-velocity term is missing; the aggregated columns use their signed Pcol.
- offbasis.py: stale tailbound.json read removed; the row-norm maximum and every reported maximum use exact dyadic comparisons
  (outward.max_upper); all final floats are directed upper bounds. certify.py's infinity norm uses the same exact comparison.
- The queued chain (logs/run_phase2.sh) will pick up the fixed files: certify at about 03:10Z, margin right after, the L_fix section
  (section_l2.py, your V033 structural check noted) after that, then S0's Phase 2.

## 2026-10-28 02:27Z (num, a session, team message 6: piecewise weight adopted; L_fix section in your norm scheduled)

- Margin certificate: work/margin.py now uses your piecewise-constant mu~' (knots 3/2, 7/4, 3, ..., 10; values 4, 17, ..., -20 sixteenths),
  with the hull rule on closed box intervals (a box touching a knot carries both neighbouring values; checked on examples). It runs right
  after certify.py in the chain (expected 03:10Z to 03:30Z). Output: inf over boxes of the lower end of b_0 + mu~' q/2 - b_+, plus the
  per-box arrays, sup |grad rho~| and an entrywise bound of D U[rho~] (work/runs/MARGIN/).
- Second section (your option (a)): L_fix h = (V.grad - 1) h + U[h].grad rho~ on L^2(e^{8t + mu~(t)} dt dtheta) = L^2(e^{mu~(log r)} dX)
  (mu~(0) = 0), both sides, with the trial's cells split at the knots so that the weight is one exponential per cell, the exact angular
  coupling of the x^2 y factor (Aang_mm' = pi [I(m-m') + I(m+m')]/2, I(0) = 1/8, I(+-1) = 1/32, I(+-2) = -1/16, I(+-3) = -1/32), L^2 rows
  (no derivative), the same conforming columns (4 modes, stride 60, 169 columns incl. J as an ordinary column), no tail columns (r^k Theta
  and r^k log r Theta are not in the space), 12 output modes, test splines as in S0 with the end splines removed. The strain term is absent
  (L_fix) and no compensation is needed. Scheduled in the chain after the margin certificate (assembly about 1 hour with 2 workers, then
  certify_l2.py -> work/runs/L2fix_M4_s60_o12/certificate.json). The code is new and untested; I will test it on the fixture in a free
  slot before it runs, and fix and rerun if it fails.
- Ordering: S0's off-basis phases (2a, 2b) run after the L_fix section; the identity rerun on the current code closes the chain.

## 2026-10-28 02:17Z (num, a session, team message 5: margin certificate scheduled; V027 fixed; norm for a second section)

- Theory author team message 4, request 1 (margin of Theorem R): scheduled right after certify.py in the queued chain (logs/run_phase2.sh; expected start
  about 03:15Z, 10 to 20 minutes, single process). work/margin.py encloses on every box [t_a, t_b] x [theta_i, theta_{i+1}] (the trial's
  1558 radial cells, the 9 finite sub-cells and the two half-lines x 64 angular boxes of the first quadrant) the quantities q, b_+, mu'(t)
  (your closed form, with H(z) = (1 + tanh z)/2 enclosed by arb; on the half-lines by monotonicity) and m = b_0 + mu' q/2 - b_+ in ball
  arithmetic, and reports inf over boxes of the lower end of m (the asymptotic regions are the half-line boxes: there q and b_+ are enclosed
  with their exact constant parts, so the limits 5.31 and 3.09 appear as box bounds, not as separate analytic statements). It also reports
  sup |grad rho~| per box (hence the O(r^2) behaviour at 0 as the half-line box value, and the decay at infinity) and an entrywise bound of
  D U[rho~] per box via the polar second derivatives of psi~ (the Frobenius norm is at most twice the entrywise bound); the global Lipschitz
  constant of V is then c_l + 2 sup DU. Outputs: work/runs/MARGIN/margin.json and margin.npz (per-box arrays so you can see where the
  minimum sits). If the box enclosures are too loose somewhere (the angular boxes are 0.0245 rad; high modes enter with the full cosine
  range), I will refine the angular partition locally.
- Theory author team message 4, point 2 (norm for a second section: plain spatial L^2(e^{mu(log r)})): my exact integration needs weights that are
  exponential polynomials in t on each cell; e^{mu} with the tanh profile is not. Two options, your choice: (a) replace mu by a piecewise
  linear mu~ (so e^{mu~} is piecewise exponential) with mu~' in the same range (sup |mu~'| < 2) and the same asymptotic values, and prove
  Theorem R with mu~ (your proof only uses mu' bounds and the margin, if I read it right); (b) keep mu and certify the Gram and operator
  matrices with rigorous quadrature (acb_calc integration) instead of closed forms, slower by a large factor. At the present CPU budget a
  second section is unlikely before the end of the run; I will state it as the recommended next computation.
- Verifier V027: both defects fixed at 02:14Z (run_tailbound2.py uses the aggregated columns' signed sine coefficients colobj.Pcol and
  |pj|.upper(); offbasis.py keeps balls through the final inequality: the square root is taken of the ball of the upper end, the norm ||E|| is
  a ball and 1/sqrt(1 - ||E||) uses its upper end). Thank you; please re-audit the snapshot when the chain has run.

## 2026-10-28 02:06Z (num, a session, team message 4: CPU limit, identity test passed, timeline, offer for (H_m) enclosures)

- CPU limit (01:50Z): my team now has 2 cores and may run 2 workers. The exact section S0 (Mh = 4, stride 60, Mout = 12) is being
  assembled with 2 workers (about 1 hour, started 02:06Z); the chain certify -> Phase 2a norms -> Phase 2b tail bound -> off-basis
  assembly -> identity rerun is queued behind it (logs/phase2_S0.log; about 2.5 hours more). Larger sections (Mh = 8, stride 16,
  Mout = 24) are out of reach at this budget unless the chain is much faster than estimated; I will report what S0 gives.
- Identity test PASSED (logs/test_identity3.log): sum_m L(a_m) = 2 eps~ + rho~ + (c/3 - c_l) X.grad rho~ holds on the fixture to 1.7e-46
  (ball-radius level) in all 42 output modes at eight cells from the inner half-line to the outer half-line; the first run had caught a
  Green-step error (fixed). The inner half-line cell is rechecked at the end of the chain with the current code (V020 fix).
- Theory author (S2_L2_THEORY.md open item 2, "certification of (H_m) with interval arithmetic on all of R^2"): I can produce rigorous box
  enclosures of b_+(X) = (|grad rho~| - d_y rho~)/2 and q(X) = V.X/|X|^2 for the exact modal trial on a cover of R^2 by cells
  [t_a, t_b] x [theta_1, theta_2] (t-cells = the trial's 1558 spline cells plus the two half-lines, which give the asymptotic regions
  exactly: b_+ -> 0, q -> -A cos^2 + D sin^2 at 0 and q -> c_l at infinity), from the same exact Green data (261 velocity modes as
  exponential polynomials on each cell, 261 density modes; angular factors by monotone trig bounds). To certify m_* = inf [b_0 + (1/2)
  mu'(t) q - b_+] > 0 I also need your mu'(t) as an exact piecewise function (piecewise polynomial or exponential in t) and the b_0 you use;
  with it the margin is enclosed box by box. Cost at 2 cores: about 1 to 2 hours for a full cover at the fine radial resolution; say
  whether you want it after the S0 chain (about 05:30Z) or instead of Phase 2b.

## 2026-10-28 01:50Z (num, a session, team message 3: reply to verifier V020; fixes applied)

- V020(1) end test splines: fixed at 01:50Z. TestSplines now retains only the splines 1..nb-2 (zero at both ends of the finite test
  range, so their zero extension is in the global H^1 forcing space); for the section S0 already assembled, certify.py and offbasis.py
  drop the rows of the two end splines (a subspace of the assembled test space; nothing else changes). Q_M is then the Y-orthogonal
  projection onto that smaller space.
- V020(2) TAU: stated as a DEFINITION in basis.py: TAU uses the first 260 cosine coefficients of Theta_0~ cos 2theta and omits the
  mode-260 coefficient A_{259,0}/2 (TAU is a selected far angular direction; its only required properties, c_l k = 1 and the exact
  cutoff, hold for the truncated direction). It is not claimed to be the exact product.
- V020(3) inner half-line Green term: fixed at 01:50Z. On (-oo, t_a] the column's A_n is now the canonical primitive alone; the
  homogeneous e^{-2n sigma} coefficient (identically zero) is checked to contain 0 and not represented; on [t_a, oo) no exact-zero
  homogeneous term is added. Rows of S0 are unaffected (no test function lives on the half-lines); the image norms (Phase 2a) use the
  fixed code. The n = 1 strain cancellation and the far KP compensation are imposed before any infinite integration (image() removes
  the exponent-0 term on the inner cells by the two exact identities; the compensated column's far bracket is omitted by definition
  of dk_j). Every omitted term is asserted to contain 0 in ball arithmetic as a consistency check, never as the justification.
- test_identity.py now also reports zero containment of every difference ball; the fixture is not exactly normalized (3/k - 1 - c =
  8.5e-15) and the J-constant removal is switched off for it; the identity itself is exact for any exp-poly background.
- Thanks for confirming the compensation coefficient and the inverse-Gram lower bound.

## 2026-10-28 01:34Z (num, a session, team message 2: exact pipeline status, first section running)

- Reproducibility of the earlier sections (6.1): CONFIRMED in floating point (logs/repro_M16.log; numbers in work log and
  S2_BASIS_CERTIFICATION.md section 1).
- Exact trial in ball arithmetic (work/exact_trial.py, independent code): c[rho~] - (3/k - 1) in [-1.62e-43, 1.62e-43] by three
  formulas, uniform over the verifier's z enclosure. The Green boundary values agree with the Analysis I float data (A_1(t_-) =
  5.71238711e-10 both). This is my input for every Avenue IV matrix; the verifier may want to spot-check A_n(t_i), B_n(t_i)
  (work/exact_trial.py build_green; 320 bits; 100 s).
- Exact operator images (work/opimage.py) and conforming basis (work/basis.py) were refereed by second-model referee (second-model referee/opcheck/answer.md):
  modal formulas and the two cancellations correct; implementation defects it found in the certificate code are fixed. A bug in my
  forward Green step across cells with exponential pieces (factor e^{(4+e)h}, not e^{4h}) was found by the identity test
  sum_m L(a_m) = 2 eps~ + rho~ + (c/3 - c_l) X.grad rho~ and fixed at 01:31Z; the rerun is in logs/test_identity2.log.
- Norm choice for the first section (theory author, please confirm or amend in CONVENTIONS; everything is parametrized): factor H^1-type norms in
  t with piecewise exponential weights: X: W_X = e^{-2 eps0 (t - t_-)} for t < t_- (eps0 = 1: remainder factor vanishes like r at 0),
  1 on [t_-, t_+], e^{2(3 - gamma)(t - t_+)} beyond (gamma = (3k-1)/2: remainder decays faster than r^gamma, so the tail r^k is
  excluded and the outer powers r^{2k-1} are included), mode weights (1 + (2m)^2); Y the same on the image factor modes
  G_N = e^{-3t} (Lh)_N with weights (1 + (2N+1)^2). Jet-plus-remainder: J (x^2 y times an exact C^6 cutoff), the exponent
  variation dk (KP direction, forced by the far-field cancellation: every column is compensated by dk_j KP with
  dk_j = -c_j k/(3 c_l + k c[KP]), the first-variation relation delta k = -k^2 delta c_l) and dtau (TAU direction) are scalar
  coordinates with unit weights. This is the S5.3(c) type: J is a coordinate. I note the verifier's warning (01:22Z) that an
  explicit J coordinate plus local weights do not reduce the frozen kernel; in my framework the global weighted graph norm must do
  it, and the section's sigma_min will show whether it does at the finite level.
- RUNNING: section S0 (exact trial, Mh = 4 modes, coarse stride 60: 169 columns + TAU, Mout = 12 output modes, 69 test splines per
  mode, 256 bits, 7 workers), then certify.py (verified lower bound of sigma_min of Q_M L P_N). Expected within the hour.
- Section 8 numbers for the theory author: I can certify coefficient suprema on annuli (|V - c_l X|, |grad rho~|, Pe_n, Qe_n bounds) from the
  same exact data on request; tell me which quantities and regions.

## 2026-10-28 00:36Z (num, a session, team message 1: recovered construction, background decision, Avenue IV plan)

Recovered earlier finite-section construction (Analysis I, numerics src; all floating point, evidence only there):
- Background of the sections: the explicit modal trial rho~ = x^2 y sum_{m<260} a_m(t) cos(2m theta), t = log r, each a_m an
  exponential-polynomial spline in t: inner r < e^{t_-}: delta_{m0} + sum_{j=1}^7 D_mj e^{2j tau'} + e^{bi tau'} sum_{i<7} Ei_mi tau'^i;
  middle: degree-7 B-spline on 1565 functions (1558 cells; knots = X3 knots mapped to t, subdivided to <= 0.008, 0.02 below the first);
  outer r > e^{t_+}: sum_q A_mq e^{alpha_q tau} + e^{-bo tau} sum_i Eo_mi tau^i, alpha_q = (k-3) - j(1-k) - 2l. Exact definition
  (verifier topic modal_repair, CONFIRMED there): all stored doubles exact; joins at the knot endpoints t_- = knots[0], t_+ = knots[-1];
  Ei, Eo by exact 6-jet matching; A_00 corrected by z in [-1.1986052364537349e-20, -1.1986052364537348e-20] so that
  c[rho~] = 3/k - 1 exactly. Exact export: analysis1 verification/data_exact/modal_v2.json.xz (hex doubles).
- Columns (src/c2_fminus.py): h = x^2 y b(t) cos(2m theta), m < Mh; per mode: inner powers e^{2j tau'} (j = 1..7), coarse degree-7
  B-splines in t on every stride-th trial knot (clamped at t_-, t_+), outer power laws e^{alpha_q tau} (q = 1..9), the J column
  (x^2 y on r < R0) for m = 0; two scalar columns KP, TAU (k'-derivative of the tail and the Theta_1 tail); free sections add pure tails.
- Operator (src/lin_fast.py): L h = (V.grad - 1) h + (U[h] + c[h] X/3).grad rho~ evaluated exactly in angular modes (sin((2N+1)theta)),
  Green data of each column in closed form, c[h] = int_0^oo r (b_0/4 + b_1/8 - b_2/8 - b_3/8) dr (cosine modes).
- Rows: residual modes N < Mout (40 or 32) at collocation radii (21 inner, ppc points per coarse cell, 10 in the cutoff zone, 40 outer
  up to 1e5 L), row weight (1+u)^{1/2}/m(r), m = u^3 (1+u^2)^{(k-3)/2}; 'H1q' rows add radial finite differences and the factor
  sqrt(1+(2N+1)^2), with trapezoid quadrature weights.
- Gram (src/c2_gram2.py): <h,g> = int (hg + r^2 grad h.grad g) m^{-2} (1+u^2)^{-3/2} dX with piecewise (broken) gradients, composite
  Gauss-Legendre with every piece endpoint as breakpoint; equilibration; C^0 or C^1 join constraints at t_-, t_+ imposed numerically
  (nullspace of the constraint matrix, relative rank cut 1e-10); eigen-cut 1e-10 relative; whitening; SVD of the row-weighted matrix.
- Reproducibility: the shipped fixture chain (c2_fminus Mh4/s60/Mout16/ppc2 then c2_gram2) runs here (logs/repro_fixture.log,
  smallest values 0.277, 0.341, 0.382 for the free section); the production M16/s16/Mout40 ppc4 section is being regenerated
  (logs/repro_M16.log) to compare with the archived 0.4131, 0.5200, 0.5465 (H1q, C^1) and 0.1698 (L2, C^0).
- Known defects (verifier topics 130-132 of Analysis I): the saved spline columns have value jumps 1e-22 to 1e-14 at internal piece
  endpoints (floating evaluation of the pieces), so they are not in the H^1 space; the earlier 'NJ1' rows mis-specified the C^0 rows at R0.

Decisions for Avenue IV (num; the theory author may amend in CONVENTIONS.md):
1. Background for every rigorous computation: the exact trial rho~ above (modal_v2.json + the z enclosure). I will reload it into ball
   arithmetic myself and recompute its Green boundary data (A_n, B_n at all cell boundaries) and the strain as a consistency check
   against the verifier's modal_green/modal_repair values.
2. Exactly conforming basis: degree-7 B-splines in t on exact dyadic knots (conforming C^6 by construction, no numerical join),
   joined to the inner powers and outer power laws by exact rational nullspace computations (fmpq), so conformity of order q >= 1 at
   t_-, t_+ is an identity of the defining data, not a floating check. Each column is then C^1 (at least) in t, in the x^2 y class, with
   the parity and axis vanishing built in, and L h is in H^1_loc under the verified background hypotheses.
3. Finite section: Galerkin least squares. Domain norm on the factor modes b_m (cosine), ||h||_X^2 = sum_m w_m^2 int (b_m^2 + b_m'^2)
   W_X dt; forcing norm on the image's sine modes G_N(t) = e^{-3t} (Lh)_N, ||g||_Y^2 = sum_N w'_N^2 int (G_N^2 + G_N'^2) W_Y dt, with W_X,
   W_Y piecewise exponential in t (pure powers of r) so that every Gram and operator entry is an exact exponential-polynomial integral
   (closed form in Arb). Weights are parameters; I will start from the Analysis I H1m/H1q pair expressed with power weights and the
   theory author can change them. The certified outputs: G_X, G_Y, B_ij = <L phi_j, psi_i>_Y, the full image Gram <L phi_i, L phi_j>_Y, a
   verified lower bound of sigma_min(Q_M L P_N) and a verified upper bound of ||(I - Q_M) L P_N|| (exact: the trial has finite angular
   bandwidth 260, so the image of every column has finitely many modes; nothing beyond is dropped).
4. The blocks Q_M L (I - P_N) and D_{M,N} need the analytic high-frequency theorem; I will list the coefficient suprema that such a
   theorem needs and certify them (sup of |U_r/r|, |U_theta/r|, |grad rho~| etc. on annuli) once the theory author fixes the form.
Request to the theory author: the two weights W_X, W_Y (exponents at 0 and infinity) and the mode weights, and whether J and the tail
coordinates are explicit scalar unknowns (F- formulation) in the section; default if no answer: F- as in Analysis I.
