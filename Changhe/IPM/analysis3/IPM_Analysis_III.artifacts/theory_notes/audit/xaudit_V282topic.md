# Independent audit of proof 246 (exact strain hyperplanes, S1J1 input only)

Target: verification/proofs/246_exact_strain_hyperplane/PROOF.md
- PROOF.md SHA256 (start and end): c90fc65d68d34e2656484279b1cb91469674a90b87b42ffe0c2c34af166f9970 (matches expected)
- Certificate SHA256 8714fd38312d89f348cbb5b700dc31e9300c48ccb98a8c9ba6515da8d97cd0d2 = evidence/check.json
  (the primary 640-bit certificate). RESULTS.md calls it "Primary certificate SHA256", and
  direct_replay.json lists it as a dependency.
- Other hashes agree with what is recorded: code/check.py 5397bd..., code/replay_direct.py d7292d...,
  dyadic_whiteners.json a6eb01..., direct_replay.json 3a3cbe..., deps 239 c6d2e2..., 240 96f271...,
  242 meta.json bd16b7.... check.json proof_sha256 equals the current PROOF.md hash, so the proof
  has not changed since the run.

## VERDICT: PASS WITH REMARKS

There are no binding findings. The theorem, its derivation, the dimension counts and the numbers
all hold. My independent exact-rational recomputation reproduces every reported constant.

## (1) Finite-dimensional linear algebra

- Lines 38-46: n is the Riesz representer of c|W in the W-restricted LOW inner product, so
  P_W v = v - c(v) n/||n||^2. For v in ker b, ||v-P_W v|| = |c(v)|/||c|W||* = |(c-b)(v)|/||c|W||*
  <= (D_W/A_W)||v||. Pythagoras gives (2). Injectivity plus equal dimension gives the isomorphism.
  This is correct. delta_W bounds sin of the angle between the two W-normals. The bound can be
  slightly loose but is valid.
- The remark at line 46 is right: the representer must be taken in W. The code does this, because
  it computes the dual norms with G_W = Q^T G Q and a_W = Q^T a, not with the 38-space normal.
- Lines 54-66: the whitening argument is correct. Write M = T^T G_W T. Then
  ||M - I||_2 <= eps < 1 gives (1-eps)I <= M <= (1+eps)I. Also G_W^{-1} = T M^{-1} T^T, so
  ell^T G_W^{-1} ell lies in [||T^T ell||^2/(1+eps), ||T^T ell||^2/(1-eps)]. That is (5), and the
  dual norm in coordinates z (with v = QTz) is exactly sqrt(ell^T G_W^{-1} ell). D_W uses the
  upper inequality and A_W the lower one, so the directions are correct (check.py lines 59-60).
- The row-sum bound is rigorous. The interval max-abs-row-sum bounds ||.||_inf for every matrix
  in the ball, including the exact symmetric matrix, and for a symmetric matrix
  ||.||_2 <= ||.||_inf. T is exact dyadic (I checked every entry), so after a non-rigorous Cholesky
  proposal the certification is fully rigorous. No uncertain matrix is inverted.
- The norms are consistent. G, a (proof 239 runs[1], 640 bits, antiderivative moments) and cvec use
  the same scaled metadata columns: max_i |a_i - b_i| = 2.0527e-17, which agrees with 239's bound
  2.053e-17. Q is in the scaled coordinates, as AUDIT_CLARIFICATIONS item 7 of proof 240 requires.

## (2) Dimension counts 37/31/28

- From 240's export, the constraint matrices (6x38 and 9x38) have exact zeros in column 13
  (asserted in check.py line 55, and checked again by me). Their nonzero columns are {0..8, 31..37}
  and {0..9, 30..37}, consistent with 240 clarification 6. I also checked exactly that rank(matrix)
  is 6 and 9, that rank(basis) is 32 and 29, and that matrix*basis = 0. So span(Q) = ker(matrix)
  contains e_13 (sp10), and c(e_13) = a_13 in [0.18393358959551484...] > 0. Line 32's formula
  matches 239(1). I re-derived it myself: the angular integral of cos^4 sin sin3theta over
  [0,2pi] is 3pi/16, giving (1/pi)(2/s)(3pi/16) int e^{2t}B dt = 3/(8s) int e^{2t}B dt.
- b_13 = 6626905964506227/2^55 > 0 (asserted in the code). So b|W is also nonzero.
- Independent extra certificates exist in the same run. eps < 1 makes G_W positive definite, which
  certifies dim W = n. A_W > 0.052 certifies c|W != 0. A_W - D_W > 0 certifies b|W != 0. The
  counts n-1 = 37, 31, 28 follow without any numerical rank decision.

## (3) Scope

- Lines 5, 70-76 and the RESULTS.md closing paragraph limit the claim correctly. It covers input
  hyperplanes, their dimensions and their LOW-metric distance only. It makes no claim about an
  image Gram, quadrature, singular value, inverse or high norm. Both scripts state, and their code
  confirms, that no output matrix is read. The operator-transfer caveat (Lambda_W delta_W) at line
  74 is correct.

## (4) Evidence

- check.json: precision_bits 640, n = 38/32/29, kernel dims 37/31/28 (exact and binary). eps:
  5.43e-66, 6.16e-62, 2.93e-59. D_W uppers: 3.25282e-17, 3.23571e-17, 3.22126e-17. A_W lowers:
  0.0521017, 0.0520589, 0.0520240018. delta_W uppers: 6.24321e-16, 6.21547e-16, 6.19187e-16.
  All are < 6.244e-16. check.log is the matching one-line summary.
- direct_replay.json (ctx.prec=768, arb solve, no whiteners): the values agree with check.json to
  about 50 digits. It asserts dn < 3253/10^20, an > 52024/10^6 and ratio < 6244/10^19 for each W.
- The RESULTS claim that per-W ratios are needed is correct:
  (3253e-20)/(52024e-6) = 6.2529e-16 > 6.244e-16.
- The runtimes in RESULTS (0.760252 s, 0.072061 s) match the JSON. initial_schema_failure.log is
  a KeyError ('constraints' instead of 'matrix') that occurred before any output was written. The
  recorded script hash belongs to the corrected script.

## Cosmetic / non-binding remarks

C1 (line 54) "Every entry of Q and b ... enters the calculation exactly" is true for b (53-bit
   dyadics) and for Q = I. The 240 nullspace entries, however, are non-dyadic rationals
   (denominators up to 349 bits for S_H and 452 bits for S_D). In check.py aa() and in replay val()
   they enter as 640-/768-bit Arb balls that contain the exact rational. This is still rigorous, but
   the wording should say "enters as a rigorous enclosure". My recheck uses them exactly.
C2 (line 58) The justification should be spelled out: the interval row sums bound ||.||_inf of the
   exact member, and symmetry gives ||.||_2 <= sqrt(||.||_1||.||_inf) = ||.||_inf.
C3 (lines 30-34) The e_13 argument silently uses 240's equality span(Q) = ker(constraint rows). It
   could also cite the run's own certificates (eps<1, A_W>0, A_W>D_W), which give dim W and both
   nonvanishings directly.
C4 (lines 11, 76; also the task summary) The theorem concerns the EXACT kernel of the binary64 row
   b. Any floating-point computed nullspace basis of cvec in the reports carries its own extra
   error, which this result does not cover. Line 76 says roughly this. Its phrase "if certified"
   reads oddly, because the difference is certified here.
C5 The uniform constants 3253/10^20, 52024/10^6 and 6244/10^19 are asserted only in
   replay_direct.py, not in check.py. The check.json values satisfy them, as I verified. The replay
   records dependency hashes after loading them instead of asserting them first, and it omits the
   meta.json hash (the source of b). The recorded hashes match.
C6 The margins are small but certified. Whole-space delta is 6.24321e-16 against 6.244e-16.
   High_graph A is 0.0520240018 against 0.052024 (relative margin 3.5e-8), while the enclosure
   radii are about 1e-50.
C7 Typography: missing spaces before numerals ("are32 and29", "dimensions37,31,28", "in(1),(2)",
   "column13", "by640-bit"). The radius in the 239 "ball" strings (e.g. +/-2.1e-41) is a display
   artifact of str(45). The binary endpoints actually used have radii near 1e-158.

## What I independently re-checked

Script: theory-working-files/audit/agent_246/recheck.py
Log: theory-working-files/audit/agent_246/recheck.log
It uses Python fractions only (no Arb or mpmath), is single-threaded, runs under nice 19 and
takes 3.3 s. Steps:
- Assert the hashes of the 239, 240, 242 and whitener inputs. Read the exact 640-bit dyadic
  endpoints of G and a, check lo <= hi, and check that the (i,j) and (j,i) enclosures overlap.
- For S_H and S_D: check exactly that matrix*basis = 0, the ranks (6/9 and 32/29) and the zeros
  in column 13. Check that a_13 > 0, b_13 > 0 and that label 13 is sp10.
- For each W, take the exported dyadic T and exact Q. Compute M = (QT)^T Gmid (QT) - I exactly,
  plus the radius term |QT|^T R |QT| (outward dyadic rounding). Then eps = max row sum. Bound
  ||T^T Q^T a||^2 from below and ||T^T Q^T (a-b)||^2 from above exactly, with the radii included.
- Results: eps <= 5.428e-66 / 6.155e-62 / 2.929e-59. D <= 3.252818208551e-17 / 3.235706581512e-17
  / 3.221257723298e-17. A >= 5.210166838521e-2 / 5.205894516666e-2 / 5.202400180233e-2.
  delta <= 6.243213143391e-16 / 6.215467046352e-16 / 6.191868390935e-16. All three directed
  constants pass for every W, in agreement with check.json and direct_replay.json to 12+ digits.
- Analytic checks by hand: the derivation of the strain kernel to formula (3), the Riesz
  projection identity, the Gram-whitening dual-norm sandwich (5), and the injective-hence-
  bijective argument.
Not re-run: the full 239/240 pipelines (accepted dependencies), check.py and replay_direct.py.
Nothing under verifier, source or repo was modified.
