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
