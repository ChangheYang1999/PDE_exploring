# Numerical code and data: commands that reproduce the certified numbers of the numerical work (S1, case 4)

Notes for the published folder. Each certified result of the numerical report referred to below is stated, with its
method and independent audit, in ../S1_NUMERICAL_CERTIFICATES.md; the numerical report itself and the run logs
(paths logs/...) are not shipped. Five floating-point fit outputs of 2.9 to 3.3 MB (data/nb_stable_result.json,
nb_stableA_result.json, nb_stableA2_result.json, nb_m10proj_result.json, nb_nodesc_result.json) are omitted for size;
they are FLOAT intermediates and certify nothing. The large cell files of the box coverings are not shipped either;
their SHA-256 hashes are in certM_131_hashes.txt. The original case 4 checkpoints are read from the published case 4
artifacts (Changhe/IPM/case4/IPM_case4.artifacts), here at ../../../case4/IPM_case4.artifacts.

All commands are run from this directory with PY=python3 (Python 3.12 with numpy, scipy, mpmath, python-flint 0.9).
The checkpoint of state 88 is the read-only file
  CKPT=../../../case4/IPM_case4.artifacts/checkpoints/state088_handoff/accepted_00000088.json
(identical to Changhe/IPM/case4/IPM_case4.artifacts/checkpoints/state088_handoff/accepted_00000088.json of the original repository).

1. Exact state (rationals, SHA check):        $PY code/state_exact.py $CKPT data/state088_exact.json
2. Origin Taylor polynomials (exact):           $PY code/origin_taylor.py data/state088_exact.json data/state088_origin_taylor.json 14
                                                $PY code/origin_taylor.py data/state088_exact.json data/state088_origin_taylor_deg34.json 34
3. Far-field sectors (exact):                   $PY code/farfield_exact.py data/state088_exact.json data/state088_farfield.json
4. Arb evaluator self-test (a_0, c, DV(0)):     $PY code/ipm_arb.py data/state088_exact.json
5. Scaling identity L K_bar = R_bar - X.grad R_bar at points:   $PY code/check_identities.py data/state088_exact.json
6. c[rho_bar] by whole-plane quadrature (FLOAT diagnostic):     $PY code/check_c_quadrature.py data/state088_exact.json data/state088_farfield.json 50 320 64
7. Far-field certificate for M (C1):            $PY code/farfield_M_cert.py data/state088_exact.json 100 300 1000 3000 10000
8. Far-field certificate for F (C2):            $PY code/farfield_F_cert.py data/state088_exact.json 10 20 30 50 100 300 1000 10000
                                                $PY code/farfield_F_sharp.py data/state088_exact.json 10 300 1e9 0.02
9. Near-origin constants (C3):                  $PY code/origin_N4.py data/state088_origin_taylor_deg34.json data/state088_exact.json $CKPT
10. Box coverings (hours on 6 cores; outputs are JSON lines, not included in full):
    M:  $PY code/cert_M.py data/state088_exact.json $CKPT data/certM_088.jsonl 0.005 10000 1.02 80 6 3.79 8 ; $PY code/post_certM.py data/certM_088.jsonl data/farfield_M_cert_088.json data/certM_088_summary.json
    F:  $PY code/cert_F.py data/state088_exact.json $CKPT data/certF_088.jsonl 0.005 300 1.02 80 6 0.45 8 0.3 data/state088_origin_taylor.json
    W,K: $PY code/cert_W.py data/state088_exact.json $CKPT data/certW_088.jsonl 0.005 2.0 1.02 80 6 8
Module roles: ipm_arb.py (ball evaluator of all fields from directional series), boxenc3.py (box enclosures: exact center Taylor polynomial +
crude remainder with the T1 Legendre structure), fcert.py (F = rho[phi_L] + U.grad rho decomposition, K_bar = rho[phi_K]), cert_*.py (drivers),
farfield_*.py (sector expansions and tails). Conventions and derivations are in the module docstrings and in ../S1_NUMERICAL_CERTIFICATES.md.

## N12 (state 131): improved approximate solutions with exact stationary far-field sectors
CK131=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json   (exact stationary density orders, computed by the independent verifier)
11. Float generator evaluator test (jets to order 6 vs arb):   $PY code/n12_eval.py data/state131_exact.json $CK131
12. Constrained refit (Levenberg-Marquardt), e.g. run m5:      $PY code/n12_run.py $CK131 $FT data/n12_m5 120 16 0.3 1:19:16 40 1e3 1.0
    arguments: ns ntheta sigma branches(j:Mj:kradial,...) iterations beta_Taylor mu0 [init.npy] [near-field boost]
13. Exact projection and exact sector check (E_(1,0) = 0):       $PY code/n12_exact.py data/n12_m5_result.json $CK131 $FT data/n12_m5_exact.json
14. Residual norms (S14) with exact far tails, checkpoint vs refit: $PY code/n12_norms.py data/state131_T1_exact.json -6.9 9.21 240 24 0.15,0.3,0.4 data/state131_norms.json
                                                                   $PY code/n12_norms.py data/n12_m5_exact.json -6.9 9.21 240 24 0.15,0.3,0.4 data/n12_m5_norms.json
15. Hdot^-1 diagnostic of the sector-subtracted residual:        $PY code/hminus1_diag.py data/state131_exact.json data/hminus1_diag_131_c50_100.json -7 9 0.05 64 2 50 100
Exact coefficient files: data/n12_m4_exact.json, data/n12_m5_exact.json (chi = H_m (1+r^2)^(p_j-m) T(t); spec [mono,h]: T = t^h; [leg,w,n]: T = t^w P_n(2t-1)).
16. Route U norms (||r F||_2, ||F||_2, ||grad F||_2, ||<r>^0.7 D^2 F||_2 with far parts and dyadic profiles):
    $PY code/n12_norms.py data/n12_m5_exact.json -6.9 9.21 240 24 -2,-1,0,0.3 data/n12_m5_exact_routeU.json ; $PY code/routeU_table.py data/*_routeU.json
17. Ball cross-check of a refit potential at sample points: $PY code/n12_ball_check.py data/n12_m5_exact.json data/state088_exact.json $CKPT
Options of n12_run.py (positional): ckpt formal_tail out_prefix ns ntheta sigma branches iters [beta_Taylor] [mu0] [init.npy|none] [near_field_boost] [tikhonov]
  branches: "j:Mj:k" (k monomials t^h per new m), "j:Mj:L26" (Legendre block n < 26), "j:Mj:B8+26" (both); several separated by commas.
  Runs reported: m4 = 1:19:4, m5 = 1:19:16, m7 = 1:19:8,2:29:8,3:39:8, m8 = m5 continued on 48 angles, m10 = 1:19:B8+26 (48 angles), m11 = 1:19:B4+14,2:29:B4+14,3:39:B4+14 (24 angles), m12 = m10 with tikhonov 1e-2.
18. Certified sups of D^1, D^2 of rho and U (weighted by (1+4r^2)^0.4) by the box method (hours, one worker):
    $PY code/cert_sups.py data/state131_exact.json $CK131 data/certSups_131.jsonl 0.005 100 1.02 80 1 6 ; $PY code/post_certSups.py data/certSups_131.jsonl data/certSups_131_summary.json
19. Lead weight set of residual norms and octave profile: $PY code/n12_norms.py data/n12_m10_exact.json -6.9 9.21 240 24 L data/n12_m10_exact_lead.json ; $PY code/lead_table.py data/*_lead.json
  m14 = 1:19:B8+26,2:29:B4+14,3:39:B4+14 (24 angles, 80 steps, init from data/n12_m10_result.json via the JSON init option);
  m16 = m10 family + 1:19:X8+8 (far-field-only monomials t^8..t^15 for all m <= 19): no change of the optimum (reported).
  Five-sector candidate (not run): add 4:49:B4+10,5:59:B4+10 (branches 4 and 5 use p_4, p_5; targets from stationary orders 5, 6).
cert_sups scope (state 131, K = 6, 2 percent cells, 80 angles, r <= 101.8): see data/certSups_131_scope.json; cells whose Lagrange remainder overflowed are listed as uncertified; D^2 U is certified on about 70 percent of the cells only (the crude bounds of 12th derivatives are too loose there); |D rho| is certified on every cell.
n12_run.py: the fit grid radii can be overridden with the environment variables N12_RMIN and N12_RMAX (defaults 1e-3 and 1e4); argv[11] accepts the verifier's stable initializer (gens/coefs JSON).
N-B runs (FLOAT): logs/nb_stable.log, logs/nb_stableA.log, logs/nb_m10proj.log and data/nb_*_result.json were produced by code/n12_run.py with N12_RMAX=64, grid 48 x 32, spec "0:9:F@K16,1:19:F@K16,1:19:B8+26,2:29:F@K16,3:39:F@K16,4:49:F@K16,5:59:F@K16", beta_T 1e3, descendant branches 0,1 (the exact command lines were kept in the run notes, which are not shipped).

## Additions (2026-10-28, from 06:12Z)
20. FLOAT weighted low norm of the state-131 residual (numerical report, section "Weighted low norm"): $PY code/wnorm_float.py data/state131_farfield.json 0.002  (log logs/wnorm_float_131.log)
21. C8, CERTIFIED single-mode annular lower bound L(F_131) >= 8.254901e9 / 1.873079e16 / 1.122153e19 at T = 2^20 / 2^30 / 2^35:
    $PY code/wnorm_cert.py data/state131_exact.json 3 20,30,35   -> data/wnorm_cert_131.json, logs/wnorm_cert_131.log  (acb.integral, exact sectors, binomial tails of farfield_F_cert.py)
22. C9, CERTIFIED independent recomputation of the verifier's 20-mode annular bound (R = 2^35, 2^32, 2^31):
    $PY code/wnorm_cert_multi.py data/state131_exact.json 3 35,32,31   -> data/wnorm_cert_multi_131.json, logs/wnorm_cert_multi_131.log
23. C2 summary corrections (V083/V094): $PY code/post_certSups2.py data/certSups_131.jsonl data/certSups_131_summary2.json (rounded-up decimals, origin-square weight);
    $PY code/post_certSups3.py data/certSups_131.jsonl data/certSups_131_frob_recombined.json (Frobenius recombination from the saved scalar component uppers).
    (The 40,081-cell input data/certSups_131.jsonl, 24 MB, is not shipped.)
24. N-B exactly admissible references: code/n12_exact.py now takes a 5th argument (descendant branches, e.g. 0,1) and imposes D_(j,m) = 0 exactly with two
    zero-strain pivots per block; code/n12_run.py has the env options N12_RMIN/N12_RMAX (fit radii), N12_MTAU/N12_MBETA (energy-matrix penalty rows
    sqrt(beta wq)(tau - lambda_min M)_+), N12_DPEN="j1,j2:beta" (soft descendant rows). Launchers: code/nb_launch.sh NAME NS NTH ITERS MU0 INIT DESC [EXTRA_SPEC]
    (spec and paths inside), code/diag_chain.sh NAME (M scan, Hdot^-1 low component, lead-weight norms of data/NAME_exact.json).
    Exact files shipped: data/nb_Mpen2_exact.json, data/nb_b6_exact.json, data/nb_d2_exact.json (the final reference, item 28); logs/nb_*_exact.log list the exact sectors of every candidate (A2..A5, A6dpen, Mpen, Mpen2, b6, d2).
    Diagnostics (same for every candidate NAME): $PY code/n12_Mscan.py data/NAME_exact.json data/NAME_Mscan.json 128 0.001 1024 12 ;
                 $PY code/n12_hminus1.py data/NAME_exact.json data/NAME_hm1.json 300 128 1e-3 1e4 0.02 3 ;
                 $PY code/n12_norms.py data/NAME_exact.json -6.9 9.21 240 128 L,0.3 data/NAME_exact_lead.json   (results in data/ and logs/ for A4, A5, Mpen, Mpen2, b6, d2)
25. Energy matrix on the symmetry axis (numerical report, section): $PY code/axis_profile.py data/state131_exact.json data/state131_origin_taylor.json data/nb_Mpen2_exact.json  (BALL for state 131, FLOAT for candidates; logs/axis_profile.log)
26. Stationary order n from the exact sector recursion (validated: n = 6 reproduces the verifier's order 6 exactly):
    $PY code/stationary_order.py data/nb_Mpen_exact.json 6 data/stationary_order6_check.json $FT ; $PY code/stationary_order.py data/nb_Mpen_exact.json 7 data/stationary_order7.json $FT
27. Penalized N-B runs (fit grid 48 x 32 on [1e-3, 64], sigma 0.3, descendants j = 0,1 exact):
    nb_Mpen:  N12_MTAU=3.805 N12_MBETA=1e6 code/nb_launch.sh nb_Mpen 48 32 40 0.0005 data/nb_stableA4_result.json 0,1
    nb_Mpen2: N12_MTAU=3.805 N12_MBETA=1e6 N12_DPEN=2:100 code/nb_launch.sh nb_Mpen2 48 32 40 0.0002 data/nb_Mpen_result.json 0,1
    nb_b6:    N12_EXTRA_ORDERS=data/stationary_order7.json N12_MTAU=3.805 N12_MBETA=1e6 N12_DPEN=2:100 code/nb_launch.sh nb_b6 48 32 40 0.0005 data/nb_Mpen2_result.json 0,1 6:69:X16+8
    exact projection: [N12_EXTRA_ORDERS=...] $PY code/n12_exact.py data/<run>_result.json $CK131 $FT data/<run>_exact.json 0,1
    Exact files shipped: data/nb_Mpen_exact.json, data/nb_Mpen2_exact.json (the (j, m, spec, coef) generator lists; rho = -d_y Lap sum coef H_m (1+r^2)^(p_j-m) T(t)).
28. Best exact reference of the run: data/nb_d2_exact.json (hard descendants j = 0,1,2; nine residual sectors exactly zero), produced by
    N12_MTAU=3.805 N12_MBETA=1e6 code/nb_launch.sh nb_d2 48 32 40 0.0002 data/nb_Mpen2_result.json 0,1,2 2:29:2
    and $PY code/n12_exact.py data/nb_d2_result.json $CK131 $FT data/nb_d2_exact.json 0,1,2 (log logs/nb_d2_exact.log; axis profile logs/axis_profile_d2.log).
29. FLOAT scan of the verifier's W1-W3 reference hypotheses (numerical report, section "FLOAT scan of the verifier's reference hypotheses"):
    $PY code/w_scan.py data/nb_d2_exact.json data/w_scan_d2.json 128 0.001 1024 12 ; same for data/state131_T1_exact.json and data/nb_Mpen2_exact.json
    (results data/w_scan_{d2,131,Mpen2}.json, logs/w_scan_*.log; order-7 float jets validated against the arb evaluator for state 131 to 1e-12).
    Fit option for the fourth-derivative bound: env N12_D4TAU/N12_D4BETA of code/n12_run.py (run nb_d2w: see logs/nb_d2w*.log).

## Further additions (2026-10-28, from 11:55Z)
30. C10: independent global certificate of hypothesis (B1), M = (2c_l+1)I + sym DU + A >= (19/5) I, for STATE 131 by the Taylor-box method (the same code as C5 for state 88):
    far field:  FARFIELD_M_OUT=$PWD/data/farfield_M_cert_131.json $PY code/farfield_M_cert.py data/state131_exact.json 100 300 1000 3000 10000     (seconds; data/farfield_M_cert_131.json)
    covering:   $PY code/cert_M.py data/state131_exact.json $CK131 data/certM_131.jsonl 0.005 10000 1.02 80 3 3.8 8     (58,640 cells + 3 origin squares; 1.5 h on 3 cores; the 65 MB JSONL is not shipped)
    NOTE: the cell files data/certM_131.jsonl and data/certM_131_far.jsonl are NOT shipped here (65 MB and 20 MB); regenerate them with the two cert_M commands
    and compare them with the SHA-256 hashes of the originals in certM_131_hashes.txt.
    summary:    $PY code/post_certM.py data/certM_131.jsonl data/farfield_M_cert_131.json data/certM_131_summary.json 1.810319210199998 10.300294891831177
    byproducts: $PY code/post_certM_B2.py data/certM_131.jsonl data/farfield_M_cert_131.json 4076476460239181/2251799813685248 data/certM_131_B2.json
                (exact Fraction tests on the stored outward-rounded endpoints: (B2) A >= -(1/20) I via rho_x^2 <= rho_y/5 + 1/100; ||sym DU|| via the trace-free formula; rho_y > 0; far field from the coefficient bounds)
    The same byproduct script on the state-88 covering: $PY code/post_certM_B2.py data/certM_088.jsonl data/farfield_M_cert_088.json 4072466420739489/2251799813685248 data/certM_088_B2.json
    Results and the proof structure: ../S1_NUMERICAL_CERTIFICATES.md (certificate of (B1) for state 131); logs/certM_131.log, logs/farfield_M_cert_131.log.
    (B4)-(B6):  $PY code/post_certM_Mk.py data/certM_131.jsonl 4076476460239181/2251799813685248 data/certM_131_Mk.json     (arb balls of the stored enclosures; M_1, M_2, M_3 of S1_CLOSURE section 3)
    exterior:   FARFIELD_MK_OUT=$PWD/data/farfield_Mk_cert_131.json $PY code/farfield_Mk_cert.py data/state131_exact.json 10000 100000 1000000 10000000   (uniform bounds for M, M_1, M_2, M_3, (B2) for r >= R)
    far cells:  $PY code/cert_M.py data/state131_exact.json $CK131 data/certM_131_far.jsonl 10000 1000000 1.02 80 2 3.8 8   (18,640 cells on 10^4 <= r <= 10^6; post-process with post_certM.py / post_certM_B2.py / post_certM_Mk.py as above -> data/certM_131_far_*.json)
    decay (W1 partial): $PY code/post_certM_decay.py data/certM_131.jsonl data/certM_131_far.jsonl data/farfield_Mk_cert_131.json 4076476460239181/2251799813685248 1000000 data/certM_131_decay.json
31. C3-131 (exact near-origin Taylor constants for state 131): $PY code/origin_taylor.py data/state131_exact.json data/state131_origin_taylor_deg34.json 34 ;
    ORIGIN_N4_OUT=$PWD/data/origin_N4_131.json $PY code/origin_N4.py data/state131_origin_taylor_deg34.json data/state131_exact.json $CK131    (logs/origin_N4_131.log)
    C2-131 (far-field residual bound): FARFIELD_F_OUT=$PWD/data/farfield_F_cert_131.json $PY code/farfield_F_cert.py data/state131_exact.json 10 20 30 50 100 300 1000 10000
    (optional sharper constant: copy that file to data/farfield_F_sharp_131.json, then FARFIELD_F_CERT=$PWD/data/farfield_F_sharp_131.json FARFIELD_F_OUT=$PWD/data/farfield_F_sharp_131.json $PY code/farfield_F_sharp.py data/state131_exact.json 10 300 1e9 0.02 ; it runs longer than 10 minutes)
    The env variables FARFIELD_M_OUT, FARFIELD_F_OUT, FARFIELD_F_CERT, ORIGIN_N4_OUT, FARFIELD_MK_OUT redirect the output files (defaults are the state-88 names).
    FARFIELD_ARB_GRID=4000 switches farfield_bounds.sup_trig (and farfield_M_cert.inf_trig) to the all-arb grid variant (no numpy sine); the shipped *_131_arb.json files were made with it:
    FARFIELD_ARB_GRID=4000 FARFIELD_M_OUT=$PWD/data/farfield_M_cert_131_arb.json $PY code/farfield_M_cert.py data/state131_exact.json 1000 10000 ; same pattern for farfield_Mk_cert.py (10000 100000 1000000) and farfield_F_cert.py (10 300 10000);
    then post_certM.py / post_certM_B2.py / post_certM_decay.py with the _arb exterior files -> data/certM_131_{summary,B2,decay}_arb.json.

## Manifest
32. ../SHA256SUMS.txt lists the SHA-256 of every file of the published folder (relative paths). Verify with `sha256sum -c SHA256SUMS.txt` from the folder root.
