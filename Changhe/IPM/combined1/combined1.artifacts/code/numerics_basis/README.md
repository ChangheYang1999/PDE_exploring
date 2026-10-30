# the N1/N2 numerics worker artifacts: reproduction of every number reported by batch N lane the N1/N2 numerics worker (frozen with NUMERICS_FINAL at 2026-10-29T18:30:12Z)

All paths relative to the lane directory the N1/N2 numerics worker. Python: python3 -B
with PYTHONDONTWRITEBYTECODE=1 (numpy, torch, gmpy2, python-flint, mpmath, scipy). Runs before 2026-10-29T00:58Z used GPU 7 (set IPM_DEVICE=cuda);
between 00:58Z and 08:30Z every command ran with CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1 (the CPU runs 011 to 020); GPU 7 was restored at 02:51Z and the runs from 08:32Z (021, 022, ...) use CUDA_VISIBLE_DEVICES=7 IPM_DEVICE=cuda (numerics/optimization/chain021_core53_gpu.sh, chain022_core54_gpu.sh: exact commands, held-out sets in the header comments). FLOAT/LOSS results; exact statements come
from numerics/lib/ipm_exact.py (gmpy2 rationals) only. Copy numerics/source_copy from the read-only sources before running anything
(cp -r source data (read-only, not included): case4 numerics/source_copy/case4).

## Code (numerics/lib)
- ipm_exact.py: exact rational reconstruction of case4 T1 checkpoints (load_case4_state), canonical monomial expansion of generator lists
  (generators_to_terms; specs mono/leg/legq/legqs), far-field potential, density and stream sectors, residual sectors (residual_sectors),
  stationary recursion (stationary_orders), Poisson identity check.
- ipm_origin.py: exact Taylor expansion at the origin (center relation, five Taylor equations, a0).
- ipm_eval.py: polar separable evaluator (fields f, f_x, f_y, psi_x, psi_y, psi_x/y, stable transport; whole-axis Gauss mesh; midpoint rule).
- ipm_polar.py: symbolic polar derivative layer (F, grad F, D^2 F from the potential); ipm_opt.py / ipm_opt2.py: constrained Gauss-Newton
  (linear rows by null space, five Taylor equations by SQP + Newton projection; objectives J_abs, FrF, E_2 / X3 proxies, near-field log term,
  kappa penalty); exact finalization with pivots (finalize_exact, flint fmpq_mat).
- ipm_farpart.py (exact-formula far parts beyond R), ipm_hminus1.py (FLOAT Hdot^-1 with exact exponential moments), ipm_tail.py (fixed tail),
  ipm_snapshot.py (immutable snapshots).

## Commands (numerics/optimization)
1. State 131 reproduction and sector table: from numerics/optimization, `python3 -B run_sanity.py` (first lines); the exact stationary recursion from numerics/optimization is `python3 -B ../far_field/run_recursion_exact.py 16` (the script lives in numerics/far_field/; its outputs state131_stationary_orders_0_12.json (42782123 bytes, sha256 6a51a4f837c20c8a...) and state131_stationary_orders_exact_0_16.json (122592067 bytes, sha256 bd82d6d0c40b2488...) stay in numerics/far_field/ and are not copied into artifacts/data/, which holds only the two fixed-sector energy tables).
2. Candidate A (constrained refit, 860 basis): `python3 -B run_candA.py Jabs 60` -> candA/candA_Jabs_{exact.json,sectors.json}.
3. Seven/eight-branch candidates: `ANGRULE=midpoint python3 -B run_candB.py FrF 120 7 4 0,1,2 200 1e4`; finalization `finalize_from_npy.py`.
4. Four-branch L^2 candidate: `python3 -B run_e2.py STATE131 3 4 none 80 80 x_j3_n4_L2fw_mid80_s131 262144 16384 1 0`.
5. d2 warm start (C1-N1-005): `python3 -B run_from_d2.py 7 4 180 60 d2w_j7_n4_X3_mid180 0 16`. C1-N1-007 (balanced E_2 objective; the command reconstructed from the exact JSON meta: JMAX 7, NRAD 4, ANG 180, 60 attempted steps, hw 0.952380952380952, MID 16, init = 005's coefficient array, HOM 0, WOFF 0, no legqs, NIN 12, WLOG 26214400, WKAP 1e6; GPU 7 at the time): `CUDA_VISIBLE_DEVICES=7 IPM_DEVICE=cuda python3 -B run_from_d2.py 7 4 180 60 d2w_j7_n4_E2bal_mid180 0.952380952380952 16 candD2/d2w_j7_n4_X3_mid180_coefs.npy 0 0 none 12 26214400 1000000` (argv order in run_from_d2.py lines 8 to 16; the run accepted 45 of 60 iterations, log candD2/d2w_j7_n4_E2bal_mid180.log).
6. Diagnostics (theory_v01 quantities): `python3 -B diag2.py <exact.json> <ANG> 8356.474846731926 <out.json> 32`.
7. Hdot^-1 check on d2: `python3 -B hminus1_check.py <nb_d2_exact.json> 160 8356.474846731926`.
8. Snapshot: `python3 -B snap_from_diag2.py <ID> <parent> <exact.json> <sectors.json> <diag2.json> <loss> "<objective>" "<description>" "<notes>"`.
Expected checks: canonical sha of state 131 = 4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01; E_1 quarter norm 0.0910394455355629;
J_abs(131) excl. r<0.02 = 1.26730668564e-11; d2 sectors (6,0) 1540.637 quarter; d2 ||F||_H = 390.2169 (N4: 390.2168).

## Added in an earlier work session (2026-10-29T02:27Z on): weak probes, pairing rows, diagnostics
- numerics/lib/ipm_opt3.py: Problem3 = Problem2 + weak-pairing rows I_k = int F phi_k dX (NORM-T-WEAK-v1 test functions), as penalty rows
  sqrt(w_k) I_k ('penalty', uniform or per-k weights) or as linearized constraint rows ('constraint'); FD-validated (logs/test_pair2.out).
- optimization/weak_tests2.py <exact.json> 180 8356.474846731926 <out.json> 32 [k list]: NORM-T-WEAK-v1 probes (I_k, A_k, B_k, C_k, H_k, m_k) over
  k in {0..8, 12, ..., 4096} (default) or any comma list (we used 6144..65536 'highk' and 1e5..1e7 'bridge'), NORM-T-WL2-v1, NORM-T-WLAP-v1 N_a
  cover, per-annulus k = 0 pairing. Calibration: d2 pairing -0.02880208111 (N4-053), 007 m_128 = 4.3987e-5 (N4-091), N_a(d2) vs the N3 numerics worker exact
  (1161.625 / 1161.6596 at a = 0). Outputs candD2/<tag>_weaktests2*.json.
- optimization/test_ik_mid.py <exact.json> 180 16,24: pairings on the reduced radial rules against the 32-point rule (8 points: wrong sign at k = 0;
  16 points: 5e-7 absolute; 24: 5 digits).
- optimization/run_pair.py: run_from_d2.py with Problem3; argv[15] WPAIR, argv[16] k list, argv[17] weaktests2 json for per-k weights (or none),
  argv[18] penalty|constraint; env IPM_DESC_ZERO=0,1,2[,3] selects the branches whose q = 1 descendants are zeroed. Runs: chainI_core54_cpu.sh
  (uniform 1e15, MID 16, 12 steps, tag d2w_j7_n4_E2bal_pairU_cpu_m16 -> C1-N1-013); the per-k-weight (tag pairD) and constraint (tag pairC) variants
  explode at step 1 (logs/d2w_j7_n4_E2bal_pair{D,C}_cpu_m16.out); desc3 (tag d2w_j7_n4_E2bal_desc3_cpu_m16) destroyed by the projection (log).
- optimization/gn_spectrum.py <exact.json> 180 16 <out.json>: singular values of the column-scaled reduced Gauss-Newton Jacobian at a candidate,
  constraint rank, reduced gradient, smallest directions (candD2/007_gn_spectrum.json; logs/gn_spectrum_007.out).
- optimization/far_weak.py <exact.json> -7 <G0> <weaktests2.json> <out.json>: exact sector table to exponent -7, far-field weak probe
  I_far(k) = |sum_e pi s_1(e) T_e(k)| (Beta functions), A_k exact, B_k/C_k scaled estimates, near-field bounds (candD2/007_far_weak.json).
- optimization/v05_tables.py, assemble_v05.py, v06_tables.py: table generators for numerics_v05/v06 from the JSON records.
- the second model referee records: the second model/farfield-structure/answer.md (tail formula), the second model/weakprobe-asympt/answer.md (+ PROOF.md: large-k asymptotics).
- optimization/weak_tests3.py <exact.json> 180 8356.474846731926 <out.json> 32: FLOAT weak probes over the N4-160 angular family phi_(n,K) = r v^2 t^K
  sin(n theta) (n = 1..31 odd, K = (n-1)/2 + {0, 8, 32, 128, 512}) plus the first-mode k list; A exact-mesh, B/C/H bounds, m. Calibration: 007 at (7,131)
  2.866e-3 against N4-160's 2.8653e-3. Outputs candD2/<tag>_weaktests3.json (007, 013, 014).
- optimization/newton_step.py <exact.json> 180 24 <out.json> <lam>: theory_v03 R6(b) Galerkin L^2 Newton step in the constraint null space (||h0||_2,
  linearized residual, held-out pairings of F + J delta); lam = LM damping on the column-scaled normal matrix (1e-10 gives a garbage step in this
  rank-deficient basis; 1e-6 and 1e-4 reported).
- optimization/na_modes_cells.py <exact.json> 180 8356.474846731926 <out.json> 32: FLOAT proxy of theory_v03 section 9 item 1 (modes 1 + 3 weighted
  Laplacian at the cell right ends against the NC-T-ORIGIN-INV thresholds) for 008, 009, 010.
- optimization/fill_v06_013.py, assemble_v06.py, v06_tables.py: numerics_v06 assembly from the JSON records (numerics/NUMERICS_v06_draft.md -> stage1 -> published).
- Chains (exact commands and core assignment): optimization/chain{F,G,H,H2,I,J,K,L,M,M2,N,O,P,Q,R,R2,S,T,U}_core5x_cpu.sh (an earlier work session); each writes logs/<name>.out.
- Snapshots of an earlier work session: C1-N1-011 (03:27:48Z), 012 (03:01:34Z), 013 (04:39:56Z), 014 (pending) in working file candidate_snapshots (not published) with MANIFEST.json and SHA256SUMS.
- optimization/quotient_basis.py <exact.json> <out.json>: exact removal of the zero-potential directions (block rref with python-flint; Legendre pivots preferred;
  identical canonical terms verified): 007, 013, 014 -> 1922 generators (logs/quotient_0{07,13,14}.out).
- optimization/run_quot.py <exact.json> ANG steps tag hw MID wlog wkap WPAIR probes mode: optimization from any exact generator list (quotient bases); env
  IPM_ADD_LEGQS=j1,j2,..:mmin:mmax:R0:NIN appends multi-scale legqs functions; env IPM_DESC_ZERO as in run_pair. Runs: chainW (015), chain016 (R0 = 25),
  chain017 (R0 = 50); diagnostics follow in each chain script.
- optimization/gn_svd.py <exact.json> 180 16 <out.json>: SVD of the explicit weighted design matrix on the admissible tangent and the mesh L^2 density Gram
  (candD2/007_quot_gn_svd.json; logs/gn_svd_007_quot.out).
- optimization/fill_v08.py: numerics_v08 assembly; weak_tests3.py now includes the theory_v04 held-out set (n in {19,23,25,29,31} x K in {600..2400});
  baselines candD2/<tag>_weaktests3b.json for 007, 013, 014, 015 (chainAA, chainAB).
- Snapshots of an earlier work session (continued): C1-N1-015-pairQ-quot013 (06:18:19Z), C1-N1-016-legqs25-quot013 (06:46:04Z), C1-N1-017-legqs50-quot013 (07:11:15Z), C1-N1-018-legqs25-cont12 (08:02:27Z); 019 (017 continued, chain019_core53_cpu.sh) and 020 (scales 25 + 50, chain020_core52_cpu.sh) running at 08:03Z for the next shift. Publications: numerics_v05..v09 (assembly scripts assemble_v05.py, assemble_v06.py + fill_v06_013.py, fill_v07.py + fill_v07_final.py, fill_v08.py, fill_v09.py).

## an earlier work session additions (2026-10-29T08:42Z)
- C1-N1-019: chain019_core53_cpu.sh (run_quot.py from candD2/quot013_legqs50_m9to15_cpu_m16_exact.json, 12 steps, 67 rows), then weak_tests2/3 and diag2;
  snapshot command: see work log 08:28Z (snap_from_diag2.py C1-N1-019-legqs50-cont12 C1-A2-d2 ... loss 1.425139e7).
- C1-N1-020: chain020_core52_cpu.sh (IPM_ADD_LEGQS=1,2,3:9:15:50:12 on the 016 exact JSON, 12 steps, 67 rows); snapshot as for 019 with loss 1.350190e7.
- C1-N1-021 / 022: chain021_core53_gpu.sh / chain022_core54_gpu.sh (GPU 7); the row lists are in the scripts; held-out sets in the header comments and in
  team notes 08:33Z.
- Held-out probe tables (013/016/017/019/020): candD2/<tag>_weaktests3.json, key 'probes' -> 'n:K' -> 'm_lower_bound' (FLOAT, MID 32).
- NUMERICS_FINAL.md repairs of 08:50Z (T4-340): the frozen 08:02Z draft is numerics/NUMERICS_FINAL_0802Z_frozen.md.

## an earlier work session additions (2026-10-29T10:46Z): GPU runs 021 to 025
- Runs: chain021_core53_gpu.sh (021), chain022_core54_gpu.sh (022), chain023_core52_gpu.sh (023), chain024_coreXX_gpu.sh <core> (024), chain025_coreXX_gpu.sh <core> (025);
  run_quot.py options added this shift: IPM_NHELDIN (number of trailing rows with their own weight) and IPM_WPAIR_HELDIN (that weight); ipm_opt3.optimize2 logs per-step
  density L2 step norms when IPM_STEPNORM=1 (columns dRho2, dCoef in candD2/<tag>.log).
- Held-out registration: numerics/optimization/heldout/HELDOUT_024.md, HELDOUT_025.md (written before launch), HELDOUT_021_022_023_record.md (after launch).
- Snapshots: snap021.sh (021); snap_gpu.py <TAG> <ID> "<intro>" "<notes>" "<heldout sha>" "<heldin rows>" "016,017,020" (022, 023 and later; composes the held-out table
  from the JSON records). Mode 33-47 sweeps: IPM_NMAX=47 weak_tests3.py ... <tag>_weaktests3c_n47.json (chain54_after022.sh, chain52_after023.sh).
- numerics_v11 assembly: make_table_v11.py (summary table), fill_v11.py <table> <status> "<new IDs>" (reads candD2/<tag>_{weaktests3,diag2,weaktests2}.json).
- NC-T-ORIGIN-INV FLOAT proxies (modes 1 + 3) for 011 to 021: chain52_after023.sh -> candD2/<tag>_na_cells.json.

## an earlier work session additions (2026-10-29T12:39Z): runs 026, 027; snapshot scripts; numerics_v12
- chain026_core54_gpu.sh (022 + 14 mid-field rows at 1e16, 60 steps), chain027_coreXX_gpu.sh <core> (control: 022 + 60 steps, 67 rows); held-out files heldout/HELDOUT_026.md,
  HELDOUT_027.md (dated, before launch). chain52_nacells2.sh: seven-cell proxies for 022 to 025.
- snap025.sh, snap026.sh, snap027.sh: snapshot commands (snap_gpu.py) with the full intro texts; run after CHAIN_DONE appears in logs/diag2_<tag>.out.
- numerics_v12 assembly: fill_v12.py <table> <status> "<new IDs>" (make_table_v11.py builds the table; numerics/v12_status.md, v12_nacells.md hold the text parts).
- chain028_core53_gpu.sh (022 + 252 legqs R0 = 25 functions n = 12..23 in m = 9..15, 67 rows, 60 steps; heldout/HELDOUT_028.md before launch). fill_v13.py (adds 027; add 028 the same way).

## an earlier work session additions (2026-10-29T14:43Z): packaged copies, run 028, numerics_v14, H18 checks
- Layout: `bash artifacts/make_artifacts.sh` copies into artifacts/code/ (numerics/lib, numerics/optimization *.py and *.sh, numerics/far_field *.py, the two
  check scripts) and artifacts/data/ (heldout/ files written before each launch; candD2/ weak-test, diag2, na_cells, sector and step-log files; far_field/ exact
  recursion JSONs; logs/ optimizer outputs with the FINAL lines; reports/ per-probe tables, status texts, the published numerics_vNN copies and a copy of
  NUMERICS_FINAL.md) and writes artifacts/SHA256SUMS. Exact coefficient files (*_exact.json, 81 MB) are not copied: each snapshotted candidate's exact JSON is
  immutable in candidates/<ID>/ with its sha256 in SHA256SUMS there.
- Run 028: `bash numerics/optimization/chain028_core53_gpu.sh` (022 + 252 legqs R0 = 25 functions n = 12..23 in m = 9..15; 2666 generators; 67 rows; 60 GN steps on
  GPU 7; then weak_tests3, weak_tests2, diag2 at MID 32); snapshot `bash numerics/optimization/snap028.sh` after CHAIN_DONE. Held-out file heldout/HELDOUT_028.md
  (sha256 caf3517a..., 12:51Z, before the 12:51:53Z launch). Expected FINAL line (FLOAT, MID 16): P2 1.973494e+02 G1 3.252719e+00 G0 2.436548e-01 rF 6.550651e+00 supF 1.2899e-01.
- Per-probe tables: `cd numerics/optimization && python3 -B perprobe.py <old_tag> <new_tag> "<label>"` (registered 25 probes, m_lower_bound of weak_tests3; counts,
  extreme factors, K >= 1800 factors, largest value). Used for 028 against 022 (legqs25_m16to23_gpu_m16), 027 (legqs25_m16to23_cont60_gpu_m16) and 016
  (quot013_legqs25_m9to15_cpu_m16): outputs numerics/perprobe_028_vs_{022,027,016}.txt. Check: 027 vs 022 reproduces N4-375 (0.8259 at (19,600), 1.3432 at (25,900)).
- numerics_v14: `python3 -B numerics/optimization/make_table_v11.py numerics/optimization/candD2/table_v14.md` then
  `python3 -B numerics/optimization/fill_v14.py numerics/optimization/candD2/table_v14.md numerics/v14_status.md "C1-N1-027, C1-N1-028"` -> numerics/NUMERICS_v14_stage.md,
  copied to working file numerics_v14.md (not published) (chmod 444; sha256 in team notes). numerics/status026.txt holds the 026 verdict sentence (matrix v132/v133).
- H18 checks (the coordinator 14:29Z part 8): `python3 -B numerics/check_ids.py` (every N4/T4 ID cited in NUMERICS_FINAL is a ledger header of the N4 numerical auditor or the T4 theory auditor; expected
  'missing: none') and `python3 -B numerics/check_certified.py` (every long decimal in NUMERICS_FINAL is verbatim in the closure matrix or a prefix variant of a value
  in the matrix, the N4/T4 ledgers or theory_v03; expected 'unmatched: 0').
- 15:28Z: run 028 complete and snapshotted (C1-N1-028-legqs25-nin24, 15:24:01Z): `bash numerics/optimization/snap028.sh` then `python3 -B numerics/optimization/post028.py`
  (patches NUMERICS_FINAL and numerics/v15_changes.md from candD2/legqs25_nin24_m9to15_gpu_m16_diag2.json; expected MID 32: G0 0.2442, G1 3.260, P2 197.1, rF 6.608, H 0.6104,
  sup|F| 0.1214, kappa_inner 0.7311). numerics_v15: `python3 -B make_table_v15.py candD2/table_v15.md; python3 -B fill_v15.py candD2/table_v15.md ../v15_status.md "<new IDs>"`
  (from numerics/optimization; texts numerics/v15_changes.md, v15_status.md, status026.txt). First-mode comparison of 028/027/022: the weaktests2 JSONs (key NORM-T-WEAK-v1_a0, per k
  'm_lower_bound' and 'I_k') and the 'FINAL pairings' lines of logs/<tag>.out (67 raw pairings; penalty = 1e12 sum I^2). Referee passes: the second model/final028/, the second model/final028b/.
- 16:08Z: diagnostics for 027 and 028 (CPU): `bash numerics/optimization/chain52_nacells3.sh` (seven-cell proxies 026, 027, 028 -> candD2/<tag>_na_cells.json; about 8 to 20 min each)
  and `python3 -B newton_step.py candD2/<tag>_exact.json 180 24 candD2/<ID>_newton_step_lam1e-6.json 1e-6` for tags legqs25_m16to23_cont60_gpu_m16 (027) and
  legqs25_nin24_m9to15_gpu_m16 (028) (about 20 min each). numerics_v16 (final exchange version): `python3 -B fill_v16.py candD2/table_v15.md ../v15_status.md "<ids>"` with the texts
  numerics/v16_changes.md, v15_changes.md, v15_status.md. The FLOAT E_2 assembly of NUMERICS_FINAL section 4 is the one-line formula E_2^2 = P2^2 + 2^14 G1^2 + 2^18 G0^2 + (20/21) 2^18 H^2
  applied to each candD2/<tag>_diag2.json (values printed in work log 15:43Z).
