ACC FINAL (num -> lead, cc verifier; posted 2026-10-22T04:54:40Z; frozen record of the accurate-map solves; NUM_REPORT 4P(b)(xvi) items 14-15)

Record cutoff: 2026-10-22T04:54:40Z.  Runs A-F' and item N as audited by external referee audit7 (03:56Z) with F' and the sequence item G added afterwards from the saved records. This record reports saved numerical output, not certified regional error bounds.

All runs have c = 2. The full accurate map rule has parameters n0 = 32, per_decade = 10, ngl = 16, n_tail = 400, q = 2. The inner integral uses 32 Gauss points on [0, min(1,y)]. On [1,y], the implementation uses n_pan = ceil(10 log10(max(Y_max,10))) panels equally spaced in log t on each row's interval, with 16 Gauss points per panel; Y_max is the largest y in the map point set. This gives at least 10 panels per decade, not exactly 10 for every row. The tail uses t = y + (1+y)(u/(1-u))^2 and 400 Gauss points on 0 < u < 1. The standard comparison maps use n0 = 24, per_decade = 4, ngl = 8, n_tail = 80, q = 3. The central difference for g_xixi uses h = 1e-5(1+sqrt(xi^2+t^2)) at the integration point (xi,t).

The unweighted residual vector consists of the PDE rows and the two normalization rows g_y(0)-1 and K-1 (centre=drop, no extra rows). The reported node residual is its largest absolute entry. The solver retains singular values exceeding 1e-13 times the largest singular value. Backtracking accepts only ||F(u+lambda d)||_2 < (1-1e-4 lambda)||F(u)||_2. Iteration indices in the logs start at zero; accepted update counts are stated below.

The between-node values use hs_layer.hydro_V_log with (n0,per_decade,ngl,n_tail) = (32,10,16,400), the same integration-point finite difference, and q = 3 for A–C and q = 2 for E. The number of inner panels is set by the largest y in the whole validation point set. A–C were evaluated before the diagnostic tail exponent was matched to the maps. Their recorded tables are retained with that provenance; invariance of the complete tables under changing q is not asserted.

The sample consists of midpoints in the compactified radial coordinate, mapped to physical radius, crossed with midpoints of the original M-angle grid and four added angles: theta_0/4, theta_0/2, (theta_last+pi/2)/2, and pi/2. This is also the angular sample used for E, whose solve rows instead use 3M angles. The maxima below are over these finite sets in 1 <= r < 100 and 100 <= r <= r_max. The outermost midpoint radius is 2.279476e6 for N=96 and 7.166401e6 for N=128.

Here R_h = (c xi+V_1)g_xi + (c y+V_2)g_y - g, and N_f = |(c xi+V_1)g_xi| + |(c y+V_2)g_y| + |g|, with velocities from the stated evaluator. The function comparison is max |h|/sqrt(1+r) over the annular subset of the common 19649-point sample (401 logarithmically spaced radii from 1e-3 to 1e7, and 49 angles including both axes), where h is the run's represented function minus the standard-map function of the same size.

The simple start is the solver's projection of g = y(1+r^2)^(-1/4). Standard-96 means runs/hsG_c2.0_N96_log.pt; standard-128c means runs/hsG_c2.0_N128_log_cont.pt.

| Run | Size and start | Updates and ending | Raw node residual | Sampled annulus max | Sampled far max | Annular weighted difference to standard |
|---|---|---|---:|---:|---:|---:|
| A | 96x24, simple | 80 accepted updates, indices 0–79; iteration cap | 5.322795e-3 | 1.562725e-3 | 1.182212e-2 | 0.182 |
| B | 128x32, simple | 51 accepted updates, indices 0–50; line-search failure at index 51 | 2.778624e-9 | 9.677470e-2 | 5.976590e-1 | 0.232 |
| C | 96x24, standard-96 | 23 accepted updates, indices 0–22; line-search failure at index 23 | 3.692623e-8 | 5.435683e-2 | 1.793139e-1 | 0.0808 |
| D | 128x32, standard-128c | Interrupted after the last logged update, index 30 (31 accepted updates); unconverged | Last logged 8.938e-3 | Unavailable | Unavailable | Unavailable |
| E | 96x24, simple; 3M=72 solve angles | 10 accepted updates, indices 0–9; line-search failure at index 10 | 8.108104e-6 | 3.149601e-5 | 5.356755e-7 | 0.348 |

For D, the last logged ||F||_2 is 3.893e-2, from an initial 4.29e-2. No endpoint state was saved, so endpoint validation, function comparison, and state hash are unavailable.

For E, there are 6912 PDE rows and 6914 entries in the complete residual vector. Its sampled core maximum for r < 0.1 is 4.690173e-4. The centre-defect formula evaluated on the coefficients gives -1.121368e-3, and E = 34.70708.

Run F, 128x32 with 3M=96 angles and the full accurate rule, failed during setup before any optimization updates. The saved exception reports a failed allocation of 20.79 GiB, with 65.74 GiB already in use by the process on a 79.25 GiB device. No endpoint state or diagnostics are available.

Run F', 128x32 with 3M=96 solve angles (12288 PDE rows, 12290 entries), uses the reduced rule (n0,per_decade,ngl,n_tail,q) = (32,6,12,240,2) in the maps (at least 6 log panels per decade, 12 Gauss points each; 240-point tail with exponent 2), the default simple start, cap 150 updates: 8 accepted updates (indices 0-7), line-search failure at index 8 (04:07:06Z). Raw node residual 2.349474e-6 (|F|_2 3.144542e-5). Between-node table (evaluator (32,10,16,400) with q = 2; sample as above): annulus 7.977523e-6, far 6.696662e-8 (r_max 7.166401e6); r < 0.1: 1.679544e-5; [0.1,1): 2.420690e-5. Coefficient centre defect -9.365200e-6; E = -1.57012, B = -9.55216. Annular weighted difference to standard-128c: 0.220 (runs/hs_cauchy_acc_fine_vs_std.txt line 4). Annular weighted difference between the two oversampled states E (96x24, full rule) and F' (128x32, reduced rule): 4.30e-3 (same file, line 3; a between-size difference of two different rules, reported as a number only). State runs/hsQ_c2.0_N128_acc6_fine.pt, SHA-256 3658ff1e504b477ff194b546a3f0612e321f816b3e891ee4b332755974d15bc6. Node check with the full reference rule (q = 2) over all 12288 rows: 1.513e-5 / 2.436e-5 / 1.034e-5 / 2.932e-8 by region (absolute 2.79e-7 / 2.35e-6 / 1.74e-6 / 1.09e-7). Annular weighted difference to the standard 160x40 state: 0.161 (runs/hs_cauchy_acc6_128_vs_std160.txt).

Item N (node checks of the STANDARD-map states, requested by the lead 04:04Z). Evaluator: hs_layer.hydro_V_log with 32 inner Gauss points on [0, min(1,y)],
at least 10 log panels per decade x 16 Gauss points on [1, y] (n_pan = ceil(10 log10(max y of the node set))), 400-point tail with t = y + (1+y)(u/(1-u))^2
(exponent 2), g_xixi by central differences with step 1e-5 (1 + r); R_h and N_f as defined above; evaluated at ALL collocation nodes of each state (the N Radau
nodes i >= 1 times the M quadrant angles: 6400 at 160x40, 9216 at 192x48, 12544 at 224x56). Maxima of |R_h|/N_f over the node set by region r < 0.1 / [0.1, 1) /
[1, 100) / r >= 100 (absolute max |R_h| in brackets), against the solver's own node residual (largest absolute entry of its unweighted residual vector, from
its standard maps):
  160x40: 1.334e-5 / 4.381e-5 / 3.616e-5 / 8.613e-5  (1.84e-6 / 1.57e-5 / 7.51e-5 / 1.45e-3); solver 1.243e-7; maximum at (233.8, 4.592).  Between-node table of this
          state (4.10): 1.3e-5 / 4.2e-5 / 5.7e-5 / 3.1e-4.  File runs/hs_node_check_c2_N160.txt; state runs/hsG_c2.0_N160_log.pt, SHA-256 60e3a92f81620d109192e1557e5da3e27d4d8b0c534fac63afd07dac09c9ac20.
  192x48: 3.228e-5 / 2.449e-5 / 2.947e-5 / 1.105e-5  (1.81e-6 / 1.14e-5 / 4.60e-5 / 4.65e-4); solver 1.770e-7; maximum at (0.004081, 6.679e-5).  Between-node table:
          3.4e-5 / 2.5e-5 / 4.4e-5 / 8.8e-5.  File runs/hs_node_check_c2_N192.txt; state runs/hsG_c2.0_N192_log.pt, SHA-256 5177b5ae4c8a480353f7d855e27cfb735accab264c56f53c1f54881476d737a0.
  224x56: 3.279e-5 / 4.615e-5 / 4.946e-5 / 2.248e-5  (2.04e-6 / 2.40e-5 / 4.45e-5 / 3.76e-4); solver 1.318e-7; maximum at (1.115, 0.2056).  Between-node table:
          3.3e-5 / 4.6e-5 / 4.8e-5 / 4.5e-5.  File runs/hs_node_check_c2_N224.txt; state runs/hsG_c2.0_N224_log.pt, SHA-256 fd0bc052d8a5eb54d759cb4c29cbcaf2983d92c94e13eabc953503a131abc632.
  (96x24, for completeness, evaluator tail exponent 3: 8.749e-6 / 1.556e-5 / 7.361e-4 / 5.001e-3; solver 3.931e-8; maximum at (1998, 65.39); file runs/hs_node_check_c2_N96.txt.)
These are sampled maxima on the node sets under one evaluator, not bounds. Same-node comparison of the two quadrature rules on one state (the only direct one
available): for the 96x24 state the velocities rebuilt with the solver's standard rule and those of the resolved rule differ at the nodes by up to 8.9e1 in V_1
and 4.5e2 in V_2 (far nodes), 5.5e-3 / 8.1e-3 in 1 <= r < 100, and the forcing b = R_ref - R_map has max |b|/N_f = 8.8e-6 / 1.6e-5 / 7.4e-4 / 5.0e-3 by region
(runs/hs_stationarity_c2_N96.txt; node-level export artifacts/data/hs_points_export/hsG_c2.0_N96_log_nodes_maps.npz; checker 309 admitted the export).

Item G (homogeneous oversampled sequence, reduced rule, completed 04:51Z; runs/launch_acc5.sh). Same formulation as F' (maps (32,6,12,240,2), 3M solve angles,
simple start, cap 150) at 80x20, 96x24, 112x28, 128x32 (the 128 state is F'). All four end in line-search failures (at indices 12, 10, 13, 8; accepted updates 12, 10,
13, 8). Raw node residual 2.597e-5, 8.107e-6, 6.567e-6, 2.349e-6. Between-node maxima of |R_h|/N_f (evaluator (32,10,16,400), q = 2, sample as above): annulus
1.03e-4, 3.15e-5, 2.38e-5, 7.98e-6; far (100 <= r <= r_max; r_max 1.1e6, 2.3e6, 4.2e6, 7.2e6) 7.91e-7, 5.35e-7, 4.74e-7, 6.70e-8; r < 0.1: 2.14e-3, 4.69e-4, 2.05e-4,
1.68e-5. Resolved evaluator at ALL 3M-angle solve rows (same rule, q = 2): annulus 1.15e-4, 3.06e-5, 2.20e-5, 1.03e-5; far 7.70e-7, 1.88e-7, 2.30e-7, 2.93e-8;
r < 0.1: 2.08e-3, 4.52e-4, 2.15e-4, 1.51e-5 (128: runs/hs_node_check_c2_N128_acc6_fine.txt, 05:04Z; maximum at (0.6176, 0.005053)). Coefficient centre defect -4.806e-3, -1.121e-3, -3.722e-4, -9.365e-6; E = +120.36, +34.70, +7.750,
-1.570; B = +211.5, +54.81, +12.75, -9.552. Far-field coefficients: Q = -0.1313, -0.1592, -0.1558, -0.1585; form-3 C_p/K at cutoff S = 1e6: +2.09e-4, +1.49e-4, +4.79e-5,
+4.16e-6; rough-fit B_log +1.9e-3, +1.3e-2, +8.4e-3, +6.8e-4. Annular weighted differences of consecutive states (max |h|/sqrt(1 + r), 1 <= r < 100, common 19649-point
sample): 80 -> 96: 2.67e-2; 96 -> 112: 2.29e-3; 112 -> 128: 3.82e-3 (pointwise relative 5.8e-2, 4.8e-3, 7.8e-3). The full-rule and reduced-rule oversampled 96
states differ by 9.7e-7 in the same metric. Files runs/hsQ_c2.0_N80_acc6_fine.pt (SHA-256 59bd27e778be5daf8c8f51123a9b19c27c7efd4b5aed3406970f9fb1688f2dd6), runs/hsQ_c2.0_N96_acc6_fine.pt (1532aec6e6f06e7f50a5e7f15a6310d5a95518c75f126693af64479f32a7cd78),
runs/hsQ_c2.0_N112_acc6_fine.pt (91f128727792cfe347106fda452c36119330ea6f8723481feaee4c64e29eed50), runs/hsQ_c2.0_N128_acc6_fine.pt (3658ff1e504b477ff194b546a3f0612e321f816b3e891ee4b332755974d15bc6);
runs/hs_cauchy_acc6_fine_seq.txt, runs/harvest_hsQ_acc6_fine.txt, runs/hs_node_check_c2_N{80,96,112}_acc6_fine.txt; copies in artifacts/data/hs and artifacts/results.

State files and independently checked SHA-256:

```text
A  runs/hsQ_c2.0_N96_acc.pt
   138134e56b0d0d47470786b7deca35421d9caa55f1dca9001f1d916609f9ba33
B  runs/hsQ_c2.0_N128_acc.pt
   f8b2b6ef3d926e6af94b4a36e6d62102cdb85a4501284a5b6c2a43ce001fdc37
C  runs/hsQ_c2.0_N96_acc_fromG.pt
   d439203f0e90c0b7454e0c3009dae1ace7e00139260a3291f412b2438eb05917
E  runs/hsQ_c2.0_N96_acc_fine.pt
   cd07dbccad526d6dac5c157ff041bf265194726dcb2359b9ebfe8b4799ccbcd4
standard-96  runs/hsG_c2.0_N96_log.pt
   4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01
standard-128c  runs/hsG_c2.0_N128_log_cont.pt
   7e3d650e2cf34016d9b2c2059e6370a29e6176b85f675ac291de2d9067eb9321
```

Source records: A/B/C/E are the # RESULT lines in runs/hsQ_c2.0_N96_acc.log:343, hsQ_c2.0_N128_acc.log:512, hsQ_c2.0_N96_acc_fromG.log:287, and hsQ_c2.0_N96_acc_fine.log:274. D is hsQ_c2.0_N128_acc_fromG.log:489–490. Function differences are line 3 of hs_cauchy_acc_96.txt, hs_cauchy_acc_128.txt, hs_cauchy_acc_96_fromG.txt, and hs_cauchy_acc_96_fine.txt. F's setup exception is hsQ_c2.0_N128_acc_fine.out:10.

Interpretation (ours, labelled as such): the sequence G is a third family of trial states, different from the standard-map stalls (0.22 away at 128); its members from 96 on agree to below one percent as functions in the annulus while their centre defect shrinks with the size and is at the level of the standard states only at 128; four states, no convergence claim. B shows angular residual aliasing directly at r=30, 300, and 3000: the scans have 32 sign changes and dominant fitted mode k=32, with tiny values at the original angular rays. At r=3 the recorded scan instead has 31 sign changes and dominant k=33. C has a large sampled off-node defect despite a small assembled residual, consistent with aliasing; the supplied angular scans do not establish the same mode pattern for C. E substantially reduces the observed annular and far defects on its stated sample while retaining a larger centre defect. These observations do not establish that E is free of aliasing, that any endpoint is an exact discrete root, or that a continuum solution has been obtained.


QUALIFICATIONS appended 2026-10-22T05:24:38Z (verifier 320 static review; the record above is unchanged): (1) Run F' timing: the line-search failure at index 8 occurred before
the raw state was saved at 04:02:28Z; 04:07:06Z is the completion of the run including its diagnostics.  (2) The angular-scan values 'at the collocation angles'
(for state B and for F') are numpy.interp interpolations of the normalised residual R_h/N_f over the scanned angles onto the collocation rays, and the fitted
dominant angular modes are those of R_h/N_f, not of R_h; they are not direct evaluations on the rays.  Finite scans; no claim of absence of aliasing or of a
mechanism follows from them.


CORRECTION (2026-10-22T06:23:25Z, note 175): in item N the evaluator description 'exponent 2' is accurate for the 192x48 and 224x56 node checks (03:27Z, 03:41Z) and INACCURATE for the 160x40 row: that check (01:52Z) ran before the 02:55Z patch of src/hs_node_check.py and used the evaluator's then-default tail exponent 3 (same inner rule, panels and 400 tail points).  Exponent-2 values at the same 6400 nodes, from the 06:16Z export run (runs/hs_node_check_c2_N160_export.txt; arrays artifacts/data/hs_points_export/hsG_c2.0_N160_log_nodes_resolved.npz): 1.334e-5 / 4.382e-5 / 3.616e-5 / 8.613e-5 against the recorded 1.334e-5 / 4.381e-5 / 3.616e-5 / 8.613e-5.  Readings unchanged.

ADDENDUM TO THE CORRECTION (2026-10-22T07:24:55Z, notes 176-176d): controlled re-runs confirm the provenance at the level of the printed records: tail exponent 3 with chunks of 100 reproduces the 01:52Z 160x40 record in every numeric line, exponent 2 with chunks of 100 reproduces the 06:16Z export run in every numeric line (six tokens differ between the two: three maxima in the last digit, three medians); at 192 / 224 exponent 3 changes the recorded (exponent-2) maxima by at most one printed unit (2.448 vs 2.449e-5; 2.247 vs 2.248e-5).  Files runs/hs_node_check_c2_N160_q3_ch100.txt, _q2_ch100.txt, _N192_q3.txt, _N224_q3.txt (copies in artifacts/results).
